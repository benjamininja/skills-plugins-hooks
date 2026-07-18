# `/security-review` required before opening a PR, not on every commit

- Status: accepted
- Date: 2026-07-17
- Scope: `CLAUDE.md` (`## Git`), `.claude/agents/skill-safety-auditor.md`

## Context

The user asked that both this repo and `project-memory-template` "know to
use security-review for any check-in work." Investigating turned up two
facts that shape where this instruction can actually live:

1. `security-review` is one of Claude Code's own **built-in** skills —
   confirmed by exhaustive search (`~/.claude/skills/`,
   `~/.claude/plugins/**/SKILL.md`, this repo's `skills/`): it has no
   `SKILL.md` anywhere. There is nothing to vendor, fork, or flip a
   `disable-model-invocation` flag on — unlike every other skill this repo
   manages, it isn't a file this repo can touch at all.
2. Neither repo has an enforcement mechanism that can invoke a skill.
   `pre-commit`/CI are deterministic-only — this is the same boundary
   [ADR-0004](0004-ci-over-local-pr-hook.md) already drew (CI enforces what's
   mechanically checkable; an agent-in-the-loop step needs a doc
   instruction, not tooling). `project-memory-template`'s
   `check-in-hygiene` hook is explicitly pure-stdlib, working identically
   at terminal/IDE/CI — asking it to invoke an LLM skill would break that
   property, so it's the wrong layer here, same reasoning ADR-0004 already
   established for a different case.

That leaves prose in `CLAUDE.md`'s `## Git` section — the section that
already governs PR workflow in both repos — as the only place this
instruction can actually live.

## Decision

Add one line to both repos' `## Git` section(s): "Before opening a PR, run
`/security-review` on the diff." Trigger is **PR-open time**, not every
commit — matching how both repos already gate merges through PRs rather
than raw commits, and avoiding a review step firing on every intermediate
WIP commit within a branch.

Also cross-reference it in `.claude/agents/skill-safety-auditor.md`'s
Boundaries — that agent already sits at the same "before committing a
safety-relevant skill change" moment, so it's the one place in this repo
where a reader might mistake its blast-radius review for a substitute for
`/security-review`, or vice versa. Noted as complementary, not overlapping.

## Alternatives rejected

- **Wire it into `check-in-hygiene` (project-memory-template) or a new
  local hook** — rejected; a `pre-commit`/CI hook cannot invoke an LLM
  skill, full stop. Same boundary as ADR-0004.
- **Run on every commit, not just PR-open** — rejected; both repos already
  gate merges through PRs, and running a security review on every
  intermediate commit inside a branch (including WIP/fixup commits) adds
  friction without adding safety the PR-time check doesn't already cover.
- **A new `.claude/agents/` wrapper around `/security-review`** — rejected;
  it's a built-in skill, not a file this repo owns, so there's nothing to
  wrap or extend. A doc instruction to invoke it directly is sufficient.

## Consequences

- Both repos now have an explicit, if unenforced (can't be, per Context),
  expectation that `/security-review` runs before any PR — visible to any
  session reading `CLAUDE.md`.
- `project-memory-template`'s three tier `CLAUDE.md` files gained the same
  line, keeping their shared `## Git` preamble identical (the thing that
  repo's own README already asks maintainers to hand-sync).
- No change to `hooks/check-in-hygiene/` or any CI config — deliberately,
  per Context.
