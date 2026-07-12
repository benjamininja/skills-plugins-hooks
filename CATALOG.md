# Catalog

> **Generated file — do not hand-edit.** Rebuild with
> `python tools/build_catalog.py`. Descriptions come from each
> skill's `SKILL.md` frontmatter, provenance from
> `vendor-skills.json`, membership + tags from `manifest.json`.

## What's in this repo

- **Skills** (36 loadable: 4 authored, 31 vendored, 1 forked) — one folder per skill under `skills/`, each with a `SKILL.md`; junctioned into `~/.claude/skills/` per machine.
- **Plugins** (3, manifest-only) — cataloged upstream bundles whose ~30 skills are deliberately not vendored (unused Fabric workloads). See `plugins/README.md` / ADR-0002.
- **Hooks** (3, all installed on this machine) — deterministic event-triggered scripts under `hooks/`, registered in `~/.claude/settings.json`. See `hooks/README.md`.
- **Vendor cache** (1) — pristine, never-loaded upstream mirrors of forked skills, for diffing. See ADR-0001.
- **Agents** (0 here) — none cataloged yet; the first real `.claude/agents/` definitions live in the Dynasty repo (its ADR-0009), produced by `/subagent-audit`.

## Skills

Tags follow the routing-map axes (see README "Routing: which skill, when"): stage = plan / crystallize / execute / cross-cutting; domain = engineering-flow / powerbi-fabric / dynasty / frontend / comms / reference / meta.

| Skill | Stage | Domain | Source | Summary |
|---|---|---|---|---|
| **ask-matt** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Ask which skill or flow fits your situation. |
| **azure-resource-manager-playwright-dotnet** | execute | powerbi-fabric | [microsoft/skills](https://github.com/microsoft/skills) | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| **caveman** | cross-cutting | comms | authored here | Token-compression communication skill. |
| **codebase-design** | crystallize | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Shared vocabulary for designing deep modules. |
| **diagnosing-bugs** | execute | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Diagnosis loop for hard bugs and performance regressions. |
| **domain-modeling** | crystallize | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Build and sharpen a project's domain model. |
| **everything-claude-code** | cross-cutting | reference | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Development conventions and patterns for everything-claude-code. |
| **fantasy-football-python** | cross-cutting | dynasty | authored here | Expert Python Data Engineer and Fantasy Sports Architect for a 28-team, dual-conference dynasty fantasy football league. |
| **frontend-design** | execute | frontend | [anthropics/claude-code](https://github.com/anthropics/claude-code) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. |
| **grill-me** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. |
| **grill-with-docs** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| **grilling** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Grill the user relentlessly about a plan or design. |
| **handoff** | crystallize | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Compact the current conversation into a handoff document for another agent to pick up. |
| **implement** | execute | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Implement a piece of work based on a spec or set of tickets. |
| **improve-codebase-architecture** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| **microsoft-docs** | cross-cutting | powerbi-fabric | [microsoft/skills](https://github.com/microsoft/skills) | Understand Microsoft technologies by querying official documentation. |
| **ponytail** | execute | engineering-flow | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Lazy senior dev mode for any coding task (write, refactor, fix, review): YAGNI, stdlib first, no unrequested abstractions. |
| **ponytail-debt** | execute | engineering-flow | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Harvest every ponytail: shortcut comment into one debt ledger, so deferrals get tracked instead of forgotten. |
| **powerbi-report-authoring** | execute | powerbi-fabric | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Create and modify Power BI report files in PBIR/PBIP format using the `powerbi-report-author` and `powerbi-desktop` CLIs. |
| **powerbi-report-design** | plan | powerbi-fabric | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Generate Power BI report visual design guidance before PBIR files are written. |
| **powerbi-report-management** | execute | powerbi-fabric | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Manage Power BI report workspace items and PBIR definitions in Microsoft Fabric via `az rest` CLI against the Fabric REST API. |
| **powerbi-report-planning** | plan | powerbi-fabric | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Build a guided requirements-to-implementation workflow for new Power BI reports and dashboards from semantic models, datasets, or PBIP projects. |
| **prototype** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Build a throwaway prototype to answer a design question. |
| **resolving-merge-conflicts** | execute | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Use when you need to resolve an in-progress git merge/rebase conflict. |
| **semantic-model-authoring** | execute | powerbi-fabric | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Develops and manages Power BI semantic models across Desktop, PBIP projects, and Fabric Service. |
| **setup-matt-pocock-skills** | plan | meta | [mattpocock/skills](https://github.com/mattpocock/skills) | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. |
| **setup-project-memory** | plan | meta | authored here | Fully wire a brand-new (or partially-wired) project — memory scaffold, engineering-skills config, and pre-commit hooks — in one pass instead of three separate manual steps. |
| **subagent-audit** | plan | meta | authored here | Structural audit of the current repo to find high-ROI subagent opportunities — the specific architectural boundaries where delegating to an isolated agent improves speed, reliability, or context integrity. |
| **tdd** | execute | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Test-driven development. |
| **teach** | crystallize | reference | [mattpocock/skills](https://github.com/mattpocock/skills) | Teach the user a new skill or concept, within this workspace. |
| **to-spec** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed. |
| **to-tickets** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker — edges as text in one file per ticket locally, or native block… |
| **triage** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. |
| **two-axis-code-review** | execute | engineering-flow | forked from [mattpocock/skills](https://github.com/mattpocock/skills) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating i… |
| **wayfinder** | plan | engineering-flow | [mattpocock/skills](https://github.com/mattpocock/skills) | Plan a huge chunk of work — more than one agent session can hold — as a shared map of investigation tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. |
| **writing-great-skills** | crystallize | meta | [mattpocock/skills](https://github.com/mattpocock/skills) | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |

## Plugins (manifest-only)

| Plugin | Upstream | Note |
|---|---|---|
| **fabric-authoring** | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Manifest only — the ~12 skills it references are not physically vendored (unused Fabric workloads: Spark, Warehouse, Eventhouse, Eventstream, Activator, medallion). |
| **fabric-operations** | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Manifest only — see plugins/README.md. |
| **fabric-skills** | [microsoft/skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | Manifest only — the full bundle (~30 skills), largely superset of fabric-authoring/fabric-operations. |

## Hooks

| Hook | Summary |
|---|---|
| **continual-learning** | A Claude Code port of [microsoft/skills](https://github.com/microsoft/skills)' [`hooks/continual-learning`](https://github.com/microsoft/skills/tree/main/hooks/continual-learning), which was built for GitHub Copilot CLI… |
| **git-guardrails** | A Claude-Code-native `PreToolUse` hook adapted from [mattpocock/skills](https://github.com/mattpocock/skills)' [`skills/misc/git-guardrails-claude-code`](https://github.com/mattpocock/skills/tree/main/skills/misc/git-gu… |
| **skill-catalog-health** | A `SessionStart` hook with two jobs, both driven by the same scan of `~/.claude/skills/` (see [ADR-0005](docs/adr/0005-skill-routing-and-drift-detection.md) for the full reasoning): |
