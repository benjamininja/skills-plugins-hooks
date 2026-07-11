# PLAN.md

Scratchpad for active/upcoming work. Expected to drift — completed items
collapse to one-liners once their durable signal lands in an ADR or
`.claude/memory/`. Blow-by-blow does NOT live here.

## Working state (2026-07-11)

**Goal 3 is fully shipped.** All four re-sequenced items landed and merged
to `main` on every repo touched (`skills-plugins-hooks`, `project-memory-
template`, `Python-PowerBI-DynastyFantasyFootball`) — zero open PRs
anywhere as of this consolidation. Full detail in `.claude/memory/
program-status.md`.

## ➡ NEXT

1. **`continual-learning` hook activation** — the only Goal-3-adjacent item
   still open. Built and merged (PR #11, `hooks/continual-learning/`) but
   **not activated**: this machine's Git Bash has neither `sqlite3` nor
   `jq` on `PATH`, so the hook no-ops if installed as-is. Needs its own
   plan+crystallize pass before installing: which binaries/how (winget vs.
   choco vs. manual download+PATH edit), whether `jq`'s absence is an
   acceptable long-term degrade, and whether the hook's own README should
   test/warn about this at session start. "PR merged" was not "capability
   live" — don't mark this done until the hook is actually persisting
   learnings.
2. Otherwise, the Deferred backlog below — nothing else is actively
   sequenced.

## [ ] Deferred

- [ ] `update-vendor-skills.ipynb` rework — drift detection, fork-handling
  automation, `plugin_manifests_only[]` awareness.
- [ ] Skill-stage/domain routing map maintenance — keep in sync if the
  skill catalog churns (flagged as a Divergent-Change risk in review).
- [ ] Orphan project-skill detection — hook/subagent scanning consuming
  repos' own `.claude/skills/` for skills not in this central catalog.
- [ ] Apply `project-memory-template` to a fresh environment as a test
  case — after the above, not yet chosen.

## Shipped (one-liners; full detail in ADR / `.claude/memory/`)

- **Goal 1**: renamed `skills` → `skills-plugins-hooks`, added
  `plugins/`/`hooks/` scaffolding.
- **Goal 2**: saturated the catalog (Pocock's idea→ship flow, ponytail,
  Power BI/Fabric skills) — merged PR #4.
- **Goal 3, done**: `project-memory-template` scaffold; skill-distribution
  bugs found and fixed; skill-stage/domain routing map; two-axis review of
  both repos' shipped work + fixes; this repo's own `common/` relocation
  (→ `skills/_powerbi-authoring-common/`) and full memory architecture
  (`CLAUDE.md`/`PLAN.md`/`.claude/memory/`/4 ADRs); `continual-learning`
  hook port (built, not yet activated — see NEXT); `git-guardrails` hook
  (built and activated); `check-in-hygiene` hook; regression-testing
  standard (general doc + Dynasty retrofit, ADR-0008) — all merged to
  `main` across all three repos. Full detail in `.claude/memory/
  program-status.md`.
