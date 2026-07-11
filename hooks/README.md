# hooks/

Reserved for standalone Claude Code hooks (event-triggered shell commands
configured via `settings.json`) that belong to this central repo.

## `continual-learning` — ported and ready to install

[`continual-learning/`](continual-learning/) is a Claude Code port of
[microsoft/skills](https://github.com/microsoft/skills)'
[`hooks/continual-learning`](https://github.com/microsoft/skills/tree/main/hooks/continual-learning)
(built for GitHub Copilot CLI's hook format — ported, not copied, onto
Claude Code's actual `settings.json`/`SessionStart`/`PostToolUse`/
`PostToolUseFailure`/`SessionEnd` event system). SQLite-backed, two-tier
scope (global `~/.claude/learnings.db` for cross-project tool patterns,
local `<repo>/.claude/learnings.db` per repo) — surfaces prior learnings at
session start, logs tool outcomes silently, detects repeated tool-failure
patterns and decays stale/low-value learnings at session end (60-day TTL,
low hit count). See its own README for install steps and the full list of
what changed porting from Copilot CLI's format.

## Reference candidate, ready to adapt (not yet activated): git-guardrails-claude-code

[mattpocock/skills/misc/git-guardrails-claude-code](https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code)
is a real, working Claude Code `PreToolUse` hook (unlike `continual-learning`
above, this one is already Claude-Code-native — no porting needed). It
intercepts the Bash tool and blocks dangerous git commands
(`git push`, `reset --hard`, `clean -f`, `branch -D`, `checkout .`/`restore .`)
via pattern-matching before they execute (`scripts/block-dangerous-git.sh`),
wired in via `.claude/settings.json`'s `hooks.PreToolUse`.

**Adaptation needed before use**: as-is it blanket-blocks *all* `git push` —
too broad for "never push directly to `main`," which should still allow
pushing feature branches. Needs a branch/ref check, not a blanket pattern.

**Layered-defense note**: this hook only intercepts when Claude Code itself
runs git via the Bash tool. It does not stop a direct terminal `git push`,
another tool, or another machine. Treating this as sufficient for an
absolute "never" would be wrong — the durable version of this rule likely
wants at least one more layer (a native `.git/hooks/pre-push` check and/or
GitHub branch protection on `main`, which can't be bypassed locally at all).

**Not yet vendored or activated** — this is a planning-phase pointer per the
2026-07-11 discussion: whether this becomes a project-local hook, a global
hook (`~/.claude/settings.json`, all repos), a `setup-pre-commit`-style
skill that installs it, or some combination, is an open scope decision.
See the repo root README's Roadmap for the tracked task.

## Population status

Otherwise empty as of the `skills` → `skills-plugins-hooks` restructure.
Further population is scoped to a later phase of the saturation effort —
see the repo root README's Roadmap section.
