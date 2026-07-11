# PLAN.md

Scratchpad for active/upcoming work. Expected to drift — completed items
collapse to one-liners once their durable signal lands in an ADR or
`.claude/memory/`. Blow-by-blow does NOT live here.

## Working state (2026-07-11)

- All Goal 3 work-to-date is merged to `main` (PRs #6, #8, #9 here; #2 on
  `project-memory-template`) — no open PRs on either repo. This repo's own
  memory architecture (`CLAUDE.md`, this file, `.claude/memory/`,
  `docs/adr/`) is live, not just proposed.
- User re-sequenced the remaining slate (2026-07-11): this repo needs to be
  fully trustworthy on its own before being used as the pattern for
  elsewhere. Regression-testing standard (Dynasty-facing) moved to *last* —
  it was about to be built next, but the user wants this repo's own
  in-repo tooling (guardrail, hygiene) proven out first.

## ➡ NEXT — in order

1. **`continual-learning` hook port** — `hooks/README.md`'s reference
   candidate (SQLite-backed learning-capture, built for GitHub Copilot
   CLI's hook format) needs porting to Claude Code's `settings.json`/hook
   event shape, not copying. This had dropped off tracking entirely until
   caught 2026-07-11 — first up now.
2. **Git guardrail hook** — never-push-to-`main` enforcement. User: "I
   REALLY feel we've experienced enough to begin this work" (referencing
   the direct-to-`main` incident this same session). Mechanism identified
   (`git-guardrails-claude-code`, needs main-only adaptation — see
   `hooks/README.md`); scope (project-local vs. global, hook vs. installer
   skill) still an open decision to resolve while building.
3. **Check-in hygiene hook** — flags empty/stale scaffold files + README
   staleness (see the `README.md` Roadmap item logged during
   `project-memory-template` planning).
4. **Regression-testing standard** — Dynasty-facing (pytest + pre-commit +
   `check_sources.py`), fully designed and grilled already (notebook
   strategy, pre-commit scope, `offline_smoke.py` rename, no venv wrapper,
   CI deferred with ADR-0004 reasoning) — just needs building. Deliberately
   last in this re-sequencing, not because the design work is stale.

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
- **Goal 3, in progress**: `project-memory-template` scaffold; skill-
  distribution bugs found and fixed; skill-stage/domain routing map;
  two-axis review of both repos' shipped work + fixes; this repo's own
  `common/` relocation (→ `skills/_powerbi-authoring-common/`) and full
  memory architecture (`CLAUDE.md`/`PLAN.md`/`.claude/memory/`/4 ADRs) —
  all merged to `main`.
