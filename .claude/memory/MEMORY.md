# Memory Index — skills-plugins-hooks-agents (project)

> Project-local memory. Cross-project preferences, terminology, and working
> method live in root (`C:\Users\benha\.claude\`). Consolidated 2026-07-11
> from the harness-tier scratch store (`~/.claude/projects/c--Users-benha-
> OneDrive-Documents-GitHub-skills/memory/`), which now holds only a
> redirect — this file and root are the authoritative copies going forward.

## Active Files

- [Program status](program-status.md) — the 3-goal restructure/saturation
  program: what's shipped across all three goals, what's next, sequencing
  rationale; 2026-07-12 second-session checkpoint (subagent-audit + first
  Dynasty agents, plan gate + dotclaude, tags/CATALOG.md, three-state
  vendor-drift ontology, full upstream currency)

## Related decision records elsewhere

- `vendor-skills.json` `known_local_edits` entries — the three-state
  vendor ontology's per-skill annotations (grilled 2026-07-12, design in
  PR #25 body and README "Maintaining vendored skills")
- Dynasty `docs/adr/0009-first-subagent-roster.md` — first subagent
  roster + rejected-candidates record (informs this repo's open `agents/`
  directory question)
- `benjamininja/dotclaude` — versioned root tier; RESTORE.md documents
  new-machine bootstrap order

## Decisions (ADRs)

- `docs/adr/0001-vendor-cache-fork-pattern.md` — pristine-mirror fork
  pattern for skills that must diverge from a faithful vendor copy
- `docs/adr/0002-plugin-manifests-only.md` — manifest-only cataloging for
  large upstream plugin bundles with mostly-unused content
- `docs/adr/0003-junction-vs-symlink-fallback.md` — directory junctions as
  the practical install mechanism when symlinks need elevation
- `docs/adr/0004-ci-over-local-pr-hook.md` — why a server-side CI gate
  beats a client-side pre-PR hook for "tests must pass before merge"
- `docs/adr/0005-skill-routing-and-drift-detection.md` — router-skill
  nudge-not-auto-invoke design, junction drift detection; status now notes
  partial supersession by ADR-0006
- `docs/adr/0006-blast-radius-tiered-model-invocation.md` — flips
  `disable-model-invocation` off for 5 skills (`grill-me`,
  `grill-with-docs`, `teach`, `writing-great-skills`, `ask-matt`) whose
  worst-case wrong-trigger is conversation/local-file-write only; `triage`
  and `wayfinder` stay manual (external issue-tracker writes)
- `docs/adr/0007-first-subagents-vendor-sync-and-safety-audit.md` — first
  `.claude/agents/` roster in this repo: `vendor-sync-reapply` (background)
  and `skill-safety-auditor` (foreground), both born from gaps found while
  executing ADR-0006 in the same session
- `docs/adr/0008-plan-gate-sync-auditor.md` — third agent, homed here
  despite auditing `project-memory-template`'s tier CLAUDE.md files against
  the private `dotclaude` root — chosen over homing it in either of those
  repos since this repo is the one every project already junction-installs
  from
