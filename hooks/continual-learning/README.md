# continual-learning

A Claude Code port of [microsoft/skills](https://github.com/microsoft/skills)'
[`hooks/continual-learning`](https://github.com/microsoft/skills/tree/main/hooks/continual-learning),
which was built for GitHub Copilot CLI's hook format. Same design — SQLite-backed,
two-tier (global + per-repo) memory that surfaces prior learnings at session
start, logs tool outcomes silently during a session, and reflects on failure
patterns + decays stale entries at session end — rebuilt against Claude Code's
actual hook system (`settings.json`, `SessionStart`/`PostToolUse`/
`PostToolUseFailure`/`SessionEnd` events), not copied.

## What changed from upstream, and why

- **Event names & shape**: Copilot CLI's `hooks.json` uses `sessionStart`/
  `postToolUse`/`sessionEnd` with a single `postToolUse` event carrying a
  `result` field. Claude Code splits tool outcomes into two distinct events,
  `PostToolUse` (success) and `PostToolUseFailure`, each firing the same
  `learn.sh postToolUse <success|failure>` call with the outcome as a fixed
  argument instead of parsed from the payload — see `settings-snippet.json`.
- **Context injection**: Copilot CLI showed session-start context as a
  transcript notice. Claude Code injects a `SessionStart` hook's stdout
  (exit 0) directly into the model's context — no JSON wrapper needed, so
  `learn.sh sessionStart` just echoes the learnings text.
- **Project root**: uses `$CLAUDE_PROJECT_DIR` (Claude Code's own env var)
  instead of relying on `.`-relative paths, so the local DB resolves
  correctly regardless of the hook's actual working directory.
- **DB location**: local DB is `$CLAUDE_PROJECT_DIR/.claude/learnings.db`
  (this repo's existing `.claude/` convention) rather than a separate
  `.copilot-memory/` folder — keep this path **out of git** (see Install
  step 4). It is auto-generated, ephemeral state, not curated memory like
  `.claude/memory/`.
- **Schema, decay (60-day TTL / hit-count-3 floor), and two-tier scope are a
  faithful 1:1 port** — no changes there.

## Activation gate — not yet installed anywhere

Code is merged; the hook is **not active** on any machine yet. Neither
`sqlite3` nor `jq` is on `PATH` in this project's primary Git Bash
environment, so installing as-is today would register a hook that silently
no-ops at every event. Deliberately left un-installed rather than adding
the binaries ad hoc — getting `sqlite3`/`jq` onto `PATH` is its own small
decision (winget vs. choco vs. manual download, whether `jq` is worth
requiring at all vs. accepting its degrade path long-term) that deserves a
plan-and-crystallize pass before flipping this on, not a rushed install
buried inside an unrelated task. Treat "learnings are actually being
captured" as the real done-condition — not "the script exists."

## Install (global — one machine-wide install, works in every repo)

1. Copy the script to a fixed, machine-wide location:
   ```bash
   mkdir -p "$HOME/.claude/hooks/continual-learning"
   cp learn.sh "$HOME/.claude/hooks/continual-learning/learn.sh"
   ```
2. Merge `settings-snippet.json`'s `hooks` block into `~/.claude/settings.json`
   (do not overwrite — merge keys if `hooks` already exists there).
3. Install `sqlite3` if it isn't already on `PATH` — required for any
   persistence to happen at all (the hook silently no-ops without it,
   consistent with upstream's graceful-degrade philosophy). On Windows/Git
   Bash, neither `sqlite3` nor `jq` ships by default; get precompiled
   binaries from [sqlite.org/download.html](https://sqlite.org/download.html)
   and [jqlang.org/download](https://jqlang.org/download/) (jq is optional —
   without it, tool-name logging degrades to a no-op, same as upstream).
4. Add `.claude/learnings.db` to `.gitignore` in any repo where the local
   tier activates (it does, automatically, the first time a Claude Code
   session runs inside that repo's git tree).

## Disable

```bash
export SKIP_CONTINUAL_LEARNING=true
```

## Requirements

- `sqlite3` — hard requirement; without it the hook is a no-op at every
  event (session-start context, tool logging, and end-of-session reflection
  all skip).
- `jq` — soft requirement; without it, tool-name extraction in
  `postToolUse` returns empty and that event no-ops, but `sessionStart`/
  `sessionEnd` still work off whatever's already in the DB.
