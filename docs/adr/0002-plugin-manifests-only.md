# Large unused plugin bundles get manifest-only cataloging, not full vendoring

- Status: accepted
- Date: 2026-07-11 (backfilled — decision made during Goal 2)
- Scope: `plugins/fabric-collection/`, `vendor-skills.json`'s
  `plugin_manifests_only[]` array

## Context

`microsoft/skills-for-fabric` ships four plugin bundles:
`powerbi-authoring`, `fabric-authoring`, `fabric-operations`, and
`fabric-skills`. Only `powerbi-authoring` matches real, active work (Power
BI/TMDL in the Dynasty repo). The other three cover ~30 skills for Fabric
workloads not in use anywhere in this repo's projects (Spark, KQL/
Eventhouse, Eventstreams, Warehouse, Activator, migration tooling), and
heavily overlap each other.

## Decision

1. Fully vendor `powerbi-authoring` — 5 skills + `common/` shared reference
   docs, real, active use.
2. For the other three bundles, store **only** their upstream
   `.github/plugin/plugin.json` manifests (listing what skills each bundle
   references) under `plugins/fabric-collection/*.plugin.json`, tracked in
   `vendor-skills.json`'s new `plugin_manifests_only[]` array — without
   vendoring the actual skill files.

## Alternatives rejected

- **Fully vendor all four bundles** — ~30 extra skill folders for unused
  workloads, most overlapping each other 2-4x; pure catalog bloat with zero
  current value.
- **Skip the other three bundles entirely, no record at all** — loses the
  ability to know what upstream offers without re-researching from scratch
  if a Fabric workload beyond Power BI ever becomes relevant.

## Consequences

- If a Fabric workload beyond Power BI becomes relevant later, the matching
  `*.plugin.json`'s `skills` list gives an exact pull list from the same
  pinned upstream repo/commit — no re-discovery needed.
- `manifest.json`'s `plugins[]` array marks these three as
  `(manifest-only)` so membership tracking stays honest about what's
  actually loadable versus merely cataloged.
- Upstream's own `check-updates` skill (a self-update checker for
  skills-for-fabric's releases) was skipped entirely as redundant with this
  repo's own `vendor-skills.json`/`update-vendor-skills.ipynb` mechanism.
