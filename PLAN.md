
Scratchpad for active/upcoming work. Expected to drift — completed items
collapse to one-liners once their durable signal lands in an ADR or
`.claude/memory/`. Blow-by-blow does NOT live here.

## Working state (2026-07-12)

**Goal 3 is fully shipped, including activation.** All four re-sequenced
items landed and merged to `main` on every repo touched
(`skills-plugins-hooks-agents`, `project-memory-template`,
`Python-PowerBI-DynastyFantasyFootball`) — zero open PRs anywhere. The
`continual-learning` hook is now installed and live on this machine (see
Shipped below). Full detail in `.claude/memory/program-status.md`.

**2026-07-12 rename**: repo renamed `skills-plugins-hooks` →
`skills-plugins-hooks-agents` on GitHub (`gh repo rename`) and locally
(folder renamed by user, `origin` remote updated to match). In-repo
references to the old name updated in `CLAUDE.md`, `README.md`, `PLAN.md`,
`.claude/memory/MEMORY.md`; historical mentions of the Goal-1
`skills`→`skills-plugins-hooks` rename left as accurate history. No
`agents/` directory exists yet — the name anticipates future scope, not
yet scaffolded; revisit when agent content actually lands.

## ➡ NEXT

**Vendor family-batch updates (in progress).** All 34 vendored paths had
upstream updates pending; grilled decision 2026-07-12: one PR per
upstream family, smallest/lowest-risk first. **Batch 1 done** (ponytail,
ponytail-debt, everything-claude-code, frontend-design): only
frontend-design had real content change (rewritten SKILL.md); the other
three were pin-bumps with identical content. First live exercise of the
reapply+`--bless` ritual (frontend-design LICENSE.txt) worked as
designed; also fixed a Windows `--apply` bug found in the process
(replace folder *contents*, not the folder inode — it's a junction
target and OneDrive-synced). **Batch 2 done** (microsoft/skills ×2):
pure pin-bumps. **Batch 3 done** (skills-for-fabric ×6 + 3 plugin
manifests): also entirely content-identical pin-bumps; the sma/mgmt
link-rewrite known edits went through the reapply+`--bless` ritual and
re-blessed to identical hashes. Two more `--apply` Windows fixes:
staging moved to system temp (OneDrive persistently denies Python's
rmdir even with retries), and file-level sync (never delete/rename
directories). **Batch 4 done** (mattpocock ×21): only grill-me (thin
`/grilling` pointer refactor) and handoff (disable-model-invocation +
wording) changed content; the three fork-rename known edits reapplied
and re-blessed to identical hashes; `code-review` mirror content
identical → `forked_at_commit` bumped, nothing to hand-merge.
**All four batches complete — every vendored path and plugin manifest
is at latest upstream, 0 NEW drift, 7 known edits blessed.** Headline
finding: ~95% of the "34 pending updates" were path-level noise with
byte-identical content — the real behavioral surface was 3 files
(frontend-design SKILL.md, grill-me, handoff).

**`subagent-audit` skill + first real run (2026-07-12, shipped — PR #22;
Dynasty roster merged as its PR #21; historical detail below).** User
supplied a "Subagent Opportunity Audit" prompt (six candidate categories,
hard hook-vs-subagent boundary, 3–5 candidate cap, `.claude/agents/*.md`
draft output); decided it belongs here as an authored skill — this repo is
the skill catalog and the `-agents` rename anticipated exactly this scope
(`project-memory-template` was considered and rejected: memory-scoped, and
a doc there isn't invocable). Adaptations over the raw prompt: inventory
step also reads reachable skills so it doesn't propose subagents that
duplicate them; added an explicit skill (vs hook/subagent) definition; new
Step 5 persists accepted/rejected reasoning to the target repo's memory
scaffold. Acceptance test: run the audit for real against
`Python-PowerBI-DynastyFantasyFootball` (richest target: MCP surface,
large data fixtures, scrapers). Its output will produce the first real
`.claude/agents/` definitions anywhere in this ecosystem — which then
informs whether this repo grows an `agents/` catalog directory.

**Add-on tasks (2026-07-12, shipped — PRs #23/#24 merged):**

1. *Plan gate* — sessions were launching request→write instead of
   request→plan→confirm→write. Root cause: the norm existed only as
   descriptive history in root `preferences.md` (lines 122/127) while the
   harness system prompt pushes "act when you can act." Fix shipped: an
   imperative **Plan gate** section in root `CLAUDE.md` (threshold: new
   file / >1 file / any design decision; enforcement: `EnterPlanMode` by
   default; escape hatches: explicit "just do it" or typo-class only).
   Reminder-hook layer deliberately deferred until Layers 1–2 are
   measured.
2. *Unified catalog* — `manifest.json` skills became tagged objects
   (stage/domain, routing-map taxonomy); new `tools/build_catalog.py`
   composes frontmatter descriptions × `vendor-skills.json` provenance ×
   tags into generated `CATALOG.md` (types recap + one-row-per-item), and
   drift-checks membership and tags. Descriptions/authors deliberately
   NOT duplicated into the manifest — derived, not mirrored.
3. *Root-tier durability* (grilled and executed 2026-07-12): `~/.claude`
   is now a git repo — private `benjamininja/dotclaude`, allowlist
   `.gitignore` (CLAUDE.md/settings/memory/commands/hooks only; secrets,
   learnings.db, junctions structurally excluded), `RESTORE.md` manual
   bootstrap doc, direct-to-main by agreement (single-author config).
   Commit cadence manual + a preferences.md nudge (root-tier edit → offer
   commit at turn end). Plan gate mirrored as a distilled invariant into
   `project-memory-template`'s three tier CLAUDE.md templates
   ([PR #9](https://github.com/benjamininja/project-memory-template/pull/9))
   — the piece that reaches cloud/other-machine surfaces.

## [ ] Deferred

- [x] ~~`update-vendor-skills.ipynb` rework~~ — done 2026-07-12 as
  `tools/update_vendor_skills.py` (drift detection via blob-SHA tree
  compare, forks[] hand-merge flagging, `plugin_manifests_only[]` checks;
  notebook retired). First live run: all 34 vendored paths have upstream
  updates; 6 skills carry deliberate-but-unrecorded local edits
  (fork-rename pointers in ask-matt/implement/tdd, `common/` path rewrites
  in semantic-model-authoring/powerbi-report-management, frontend-design's
  added LICENSE.txt). **Both open decisions grilled and resolved
  2026-07-12**: (a) three-state ontology (faithful /
  vendored-with-known-edits / fork) via per-entry `known_local_edits`
  annotations (file + reason + local_sha), two-bucket reporting
  (known/NEW), `--bless`, stale-annotation policing, git-based reapply
  ritual on `--apply` — built, seeded for all 6 skills, verified (0 NEW /
  7 known files; planted edits surface as NEW); (b) family-batched update
  PRs — see NEXT.
- [ ] Skill-stage/domain routing map maintenance — keep in sync if the
  skill catalog churns (flagged as a Divergent-Change risk in review).
  **Partially closed 2026-07-12**: stage/domain now lives as tags in
  `manifest.json` and `tools/build_catalog.py` fails on membership/tag
  drift when regenerating `CATALOG.md`; remaining gap is only the README
  routing *tables* themselves (narrative view, still hand-maintained).
- [ ] Orphan project-skill detection — hook/subagent scanning consuming
  repos' own `.claude/skills/` for skills not in this central catalog.
- [ ] Apply `project-memory-template` to a fresh environment as a test
  case, now via `/setup-project-memory` — not yet run.

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
  hook port and activation (`sqlite3`/`jq` installed via `winget`, hooks
  merged into `~/.claude/settings.json`, verified persisting real rows);
  `git-guardrails` hook (built and activated); `check-in-hygiene` hook;
  regression-testing standard (general doc + Dynasty retrofit, ADR-0008)
  — all merged to `main` across all three repos. Full detail in
  `.claude/memory/program-status.md`.
- **Repo renamed** `skills-plugins-hooks` → `skills-plugins-hooks-agents`
  (2026-07-12, `gh repo rename` + local remote + in-repo references).
- **Post-Goal-3 audit, all 4 gaps fixed**: `continual-learning` re-verified
  live post-restart (real harness-fired `tool_log` rows) and grilled
  against upstream `microsoft/skills` source (two known limitations
  confirmed inherited, not port bugs — see `hooks/continual-learning/README.md`);
  Dynasty's `pre-commit install` activated (`Python-PowerBI-DynastyFantasyFootball#20`);
  `check-in-hygiene` adopted by a real consumer for the first time ever
  (Dynasty + this repo), which surfaced and fixed two genuine cross-platform
  packaging bugs (`project-memory-template#6`); stale docs (`hooks/README.md`,
  root `README.md`) corrected.
- **Skill routing + junction drift detection** (ADR-0005): discovered
  every `~/.claude/skills/` junction on this machine was broken (pointed
  at the repo's pre-Goal-1 name, silently stranding every Pocock-flow
  skill for weeks) — all 34 relinked. New `hooks/skill-catalog-health/`
  (`SessionStart`) injects a self-generated routing index (mirrors
  upstream `mattpocock/skills`' README Reference-table format) so
  `disable-model-invocation: true` router skills still get surfaced, and
  flags future broken junctions instead of failing silently. New
  `skills/setup-project-memory` orchestrates the three previously
  uncoordinated bootstrap steps (memory tier, `setup-matt-pocock-skills`,
  `check-in-hygiene` pre-commit) in one pass — resolves the "apply
  `project-memory-template` to a fresh environment" deferred item below
  (not yet run as a live test).
