# hooks/

Reserved for standalone Claude Code hooks (event-triggered shell commands
configured via `settings.json`) that belong to this central repo.

## Reference candidate for Goal 3: continual-learning

[microsoft/skills](https://github.com/microsoft/skills)'
[`hooks/continual-learning`](https://github.com/microsoft/skills/tree/main/hooks/continual-learning)
is a real, working example worth designing against when this folder gets
populated: a SQLite-backed memory system with a two-tier scope (global
`~/.copilot/learnings.db` for cross-project tool patterns, local
`.copilot-memory/learnings.db` per repo), firing on session start/end and
after each tool use — it surfaces prior learnings at session start, detects
repeated tool-failure patterns at session end, and decays stale, low-value
learnings automatically (60-day TTL, low hit count).

**Not vendored as-is** — it's built for GitHub Copilot CLI's hook format
(`.github/hooks/`, `hooks.json`, event names `sessionStart`/`postToolUse`/
`sessionEnd`), which doesn't match Claude Code's hook system (`settings.json`,
different event names/config shape). Porting it — not copying it — is real
Goal 3 work: the self-reinforcing-memory pattern (auto-capture + decay,
not hand-maintained markdown) is directly relevant to the project-memory-
template synthesis.

## Population status

Otherwise empty as of the `skills` → `skills-plugins-hooks` restructure.
Further population is scoped to a later phase of the saturation effort —
see the repo root README's Roadmap section.
