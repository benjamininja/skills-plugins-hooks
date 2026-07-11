# PLAN.md

Scratchpad for active/upcoming work. Expected to drift — completed items
collapse to one-liners once their durable signal lands in an ADR or
`.claude/memory/`. Blow-by-blow does NOT live here.

## Working state (2026-07-11)

- On branch `project-memory-architecture`, adding this repo's own memory
  architecture (`CLAUDE.md`, this file, `.claude/memory/`, `docs/adr/`) —
  retroactively, since decision-density here already exceeded what a
  harness-tier scratch store should be carrying (see `program-status.md`
  and the backfilled ADRs).
- PR #6 (skill-distribution fix) still open on `main` — not yet merged.

## ➡ NEXT

- Finish this memory-architecture retrofit, then return to the
  regression-testing standard for `Python-PowerBI-DynastyFantasyFootball`
  (design already grilled and agreed — see session history / handoff).
- After that: apply `project-memory-template` to a fresh environment as a
  test case (not yet chosen).

## [ ] Deferred

- [ ] Check-in hygiene hook — flags empty/stale scaffold files.
- [ ] `update-vendor-skills.ipynb` rework — drift detection, fork-handling
  automation, `plugin_manifests_only[]` awareness.
- [ ] Git guardrail hook (never push directly to `main`) — mechanism
  identified (`git-guardrails-claude-code`), scope not yet decided.
- [ ] Skill-stage/domain routing map maintenance — keep in sync if the
  skill catalog churns (flagged as a Divergent-Change risk in review).
- [ ] Orphan project-skill detection — hook/subagent scanning consuming
  repos' own `.claude/skills/` for skills not in this central catalog.

## Shipped (one-liners; full detail in ADR / `.claude/memory/`)

- **Goal 1**: renamed `skills` → `skills-plugins-hooks`, added
  `plugins/`/`hooks/` scaffolding.
- **Goal 2**: saturated the catalog (Pocock's idea→ship flow, ponytail,
  Power BI/Fabric skills) — merged PR #4.
- **Goal 3, in progress**: `project-memory-template` scaffold shipped
  (separate repo); skill-distribution bugs found and fixed (PR #6, pending
  merge); skill-stage/domain routing map shipped (PR #7); two-axis review
  of both repos' shipped work, findings fixed.
