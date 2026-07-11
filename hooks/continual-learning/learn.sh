#!/bin/bash
# Continual Learning — Claude Code port of microsoft/skills' Copilot CLI hook
# (github.com/microsoft/skills/tree/main/hooks/continual-learning).
# Usage: learn.sh <sessionStart|postToolUse|sessionEnd> [outcome]
#
# Ported, not copied — Claude Code already splits tool outcomes into two
# distinct events (PostToolUse vs. PostToolUseFailure) instead of one event
# carrying a result field, so the caller passes the outcome as $2 (see
# settings-snippet.json). Everything else (schema, decay, two-tier scope) is
# a faithful port of upstream's design.
#
# Two-tier memory:
#   global: ~/.claude/learnings.db                         (cross-project tool patterns)
#   local:  $CLAUDE_PROJECT_DIR/.claude/learnings.db        (repo-specific, only inside a git repo)

set -euo pipefail

[[ "${SKIP_CONTINUAL_LEARNING:-}" == "true" ]] && exit 0

EVENT="${1:-}"
OUTCOME="${2:-}"
INPUT=$(cat 2>/dev/null || echo "{}")

GLOBAL_DB="$HOME/.claude/learnings.db"
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
LOCAL_DB="$PROJECT_DIR/.claude/learnings.db"

has_sqlite() { command -v sqlite3 &>/dev/null; }
has_jq() { command -v jq &>/dev/null; }
in_git_repo() { git -C "$PROJECT_DIR" rev-parse --is-inside-work-tree &>/dev/null; }
repo_name() { basename "$(git -C "$PROJECT_DIR" rev-parse --show-toplevel 2>/dev/null || echo "$PROJECT_DIR")"; }

init_db() {
  local db="$1"
  mkdir -p "$(dirname "$db")"
  has_sqlite || return 0
  sqlite3 "$db" <<'SQL'
CREATE TABLE IF NOT EXISTS learnings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scope TEXT NOT NULL,          -- 'global' or 'local'
    category TEXT NOT NULL,       -- 'pattern', 'mistake', 'preference', 'tool_insight'
    content TEXT NOT NULL,
    source TEXT,                  -- repo name, session id, etc.
    created_at TEXT DEFAULT (datetime('now')),
    last_seen TEXT DEFAULT (datetime('now')),
    hit_count INTEGER DEFAULT 1
);
CREATE TABLE IF NOT EXISTS tool_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool_name TEXT,
    result TEXT,
    ts TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_learnings_scope ON learnings(scope);
CREATE INDEX IF NOT EXISTS idx_learnings_category ON learnings(category);
SQL
}

init_db "$GLOBAL_DB"
in_git_repo && init_db "$LOCAL_DB"

# ─── SESSION START ──────────────────────────────────────────
# Claude Code injects stdout straight into context on exit 0 for SessionStart
# (and UserPromptSubmit) — no JSON wrapper needed, unlike PreToolUse's
# permissionDecision-style output.
on_session_start() {
  has_sqlite || exit 0

  local context=""
  local global_count
  global_count=$(sqlite3 "$GLOBAL_DB" "SELECT COUNT(*) FROM learnings;" 2>/dev/null || echo "0")
  if [[ "$global_count" -gt 0 ]]; then
    local top_global
    top_global=$(sqlite3 "$GLOBAL_DB" \
      "SELECT '- [' || category || '] ' || content FROM learnings
       ORDER BY hit_count DESC, last_seen DESC LIMIT 5;" 2>/dev/null || echo "")
    [[ -n "$top_global" ]] && context="Global learnings ($global_count total):
$top_global"
  fi

  if in_git_repo && [[ -f "$LOCAL_DB" ]]; then
    local local_count
    local_count=$(sqlite3 "$LOCAL_DB" "SELECT COUNT(*) FROM learnings;" 2>/dev/null || echo "0")
    if [[ "$local_count" -gt 0 ]]; then
      local top_local
      top_local=$(sqlite3 "$LOCAL_DB" \
        "SELECT '- [' || category || '] ' || content FROM learnings
         ORDER BY hit_count DESC, last_seen DESC LIMIT 5;" 2>/dev/null || echo "")
      [[ -n "$top_local" ]] && context="$context

Repo learnings for $(repo_name) ($local_count total):
$top_local"
    fi
  fi

  [[ -n "$context" ]] && echo "$context"
  exit 0
}

# ─── POST TOOL USE (success and failure share this) ─────────
on_post_tool_use() {
  has_sqlite || exit 0

  local tool_name=""
  has_jq && tool_name=$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null || echo "")
  [[ -z "$tool_name" ]] && exit 0

  sqlite3 "$GLOBAL_DB" \
    "INSERT INTO tool_log (tool_name, result) VALUES ('$(echo "$tool_name" | tr "'" "''")','$(echo "$OUTCOME" | tr "'" "''")');" \
    2>/dev/null || true
  exit 0
}

# ─── SESSION END ─────────────────────────────────────────────
on_session_end() {
  has_sqlite || exit 0

  local fail_tools
  fail_tools=$(sqlite3 "$GLOBAL_DB" \
    "SELECT tool_name FROM tool_log
     WHERE result='failure' AND ts > datetime('now','-4 hours')
     GROUP BY tool_name HAVING COUNT(*) > 2;" 2>/dev/null || echo "")

  if [[ -n "$fail_tools" ]]; then
    while IFS= read -r tool; do
      [[ -z "$tool" ]] && continue
      local safe_tool
      safe_tool=$(echo "$tool" | tr "'" "''")
      sqlite3 "$GLOBAL_DB" \
        "INSERT INTO learnings (scope, category, content, source)
         SELECT 'global','tool_insight','Tool \"$safe_tool\" frequently fails — check usage pattern','auto:$(date -u +%Y%m%d)'
         WHERE NOT EXISTS (SELECT 1 FROM learnings WHERE content LIKE '%$safe_tool%frequently fails%');
         UPDATE learnings SET hit_count = hit_count + 1, last_seen = datetime('now')
         WHERE content LIKE '%$safe_tool%frequently fails%';" 2>/dev/null || true
    done <<< "$fail_tools"
  fi

  sqlite3 "$GLOBAL_DB" "DELETE FROM tool_log WHERE ts < datetime('now','-7 days');" 2>/dev/null || true
  sqlite3 "$GLOBAL_DB" \
    "DELETE FROM learnings WHERE last_seen < datetime('now','-60 days') AND hit_count < 3;" 2>/dev/null || true
  if in_git_repo && [[ -f "$LOCAL_DB" ]]; then
    sqlite3 "$LOCAL_DB" \
      "DELETE FROM learnings WHERE last_seen < datetime('now','-60 days') AND hit_count < 3;" 2>/dev/null || true
  fi
  exit 0
}

case "$EVENT" in
  sessionStart) on_session_start ;;
  postToolUse)  on_post_tool_use ;;
  sessionEnd)   on_session_end ;;
  *) echo "Usage: learn.sh <sessionStart|postToolUse|sessionEnd> [outcome]" >&2; exit 1 ;;
esac
