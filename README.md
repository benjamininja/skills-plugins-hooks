# skills-plugins-hooks

The central repository for [Claude Code](https://claude.ai/code) skills, plugins, and hooks — modular instruction sets, bundled plugin packages, and event-triggered automations. Every skill lives at a flat, loadable path (`skills/<name>/SKILL.md`) so the whole collection can be dropped straight into a Claude Code skills directory.

Some skills are authored here; others are vendored from upstream projects and credited below. Attribution lives in this README and in each skill's `SKILL.md` — not in the folder names.

---

## Repository Structure

```
.
├── manifest.json                               # top-level inventory: skills / plugins / hooks membership
├── vendor-skills.json                          # manifest: pins each vendored skill's upstream commit + forks
├── vendor-cache/                               # pristine, never-loaded mirrors of forked skills (diff target)
│   └── code-review/                            # upstream mirror of engineering/code-review
├── tools/
│   └── update-vendor-skills.ipynb              # checks upstream for newer versions & re-pins
├── skills/                                     # every folder here gets symlinked/loaded as one library
│   ├── caveman/                                # token-compression communication
│   ├── fantasy-football-python/                # dynasty fantasy football ETL
│   │   └── references/data_model.md
│   ├── frontend-design/                        # production-grade frontend UI (+ LICENSE.txt)
│   ├── azure-resource-manager-playwright-dotnet/   # Azure Playwright Testing ARM SDK (.NET)
│   ├── everything-claude-code/                 # Claude Code conventions reference
│   ├── grill-me/                               # stress-test a plan via interview (no codebase)
│   ├── grilling/                               # sequential interview discipline (grill-with-docs dependency)
│   ├── domain-modeling/                        # CONTEXT.md/ADR discipline (grill-with-docs dependency)
│   ├── grill-with-docs/                        # thin pointer: runs /grilling using /domain-modeling
│   ├── handoff/                                # compact a session into a handoff doc
│   ├── ask-matt/                               # router over the idea→ship engineering flow below
│   ├── codebase-design/                        # deep-module vocabulary (module/interface/depth/seam)
│   ├── diagnosing-bugs/                        # diagnosis loop for hard bugs/perf regressions
│   ├── implement/                              # build a spec/ticket via /tdd, closes with /two-axis-code-review
│   ├── improve-codebase-architecture/          # scan for deepening opportunities, visual HTML report
│   ├── prototype/                              # throwaway code to answer a design question
│   ├── resolving-merge-conflicts/              # resolve an in-progress git merge/rebase conflict
│   ├── setup-matt-pocock-skills/               # bootstrap: issue tracker, triage labels, doc layout
│   ├── tdd/                                    # red-green-refactor discipline, seam-based testing
│   ├── to-spec/                                # synthesize the conversation into a spec/PRD
│   ├── to-tickets/                             # break a spec into tracer-bullet tickets with blocking edges
│   ├── triage/                                 # state machine for incoming issues/external PRs
│   ├── two-axis-code-review/                   # FORK of code-review: Standards+Spec review (see below)
│   ├── wayfinder/                              # chart huge, foggy efforts as a shared ticket map
│   ├── teach/                                  # multi-session teaching workspace for any topic
│   └── writing-great-skills/                   # reference for authoring skills well
├── plugins/                                    # reserved: bundled skill+hook+MCP packages (empty — see Roadmap)
└── hooks/                                      # reserved: standalone event-triggered hooks (empty — see Roadmap)
```

`manifest.json` tracks *membership* (what's in this repo, by category). `vendor-skills.json` tracks *provenance* (upstream repo/commit for vendored skills, plus a `forks[]` list for skills that diverged from a faithful vendor copy) — the two are separate and both authoritative for their own concern.

### Forked skills

A **fork** happens when we need a skill to diverge from its upstream vendor copy — usually a rename to avoid a naming collision — while still being able to diff against upstream later. The pattern: keep a pristine, untouched mirror in `vendor-cache/<name>/` (git-tracked, pinned in `vendor-skills.json` like any normal vendor, but **never symlinked** since `skills/` is loaded wholesale), and put the actual usable, edited version in `skills/<fork-name>/`. `vendor-skills.json`'s `forks[]` array links the two. First (and so far only) case: `two-axis-code-review`, forked from `mattpocock/skills`' `engineering/code-review` to avoid colliding with this repo's existing general-purpose `code-review` skill.

---

## Installation

To use these in Claude Code, link or copy the skills into a discovered skills directory (personal `~/.claude/skills/` or a project's `.claude/skills/`). For example, to symlink the entire library on Windows (run as admin):

```powershell
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\library" -Target "C:\Users\benha\OneDrive\Documents\GitHub\skills\skills"
```

Or link individual skills as needed. Each `skills/<name>/SKILL.md` is self-contained and loadable on its own.

---

## Skills

### Authored / maintained here

| Skill | Description | Trigger |
|-------|-------------|---------|
| **caveman** | Token-compression communication. Strips filler, preamble, hedging, and pleasantries; technical content passes through untouched. Two modes: **lite** (default, full grammar) and **ultra** (telegraphic fragments). *Modified from [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman).* | `/caveman`, `/caveman ultra`, `/caveman lite` |
| **fantasy-football-python** | Python Data Engineer / Fantasy Sports Architect for a 28-team, dual-conference dynasty league. Rookie draft pipelines, combine data, salary cap ($500M / 3-yr contracts), Fantrax scraping, star-schema Parquet, Jupyter conventions. | Auto-activates on dynasty league ETL, nflverse/nflreadpy, Fantrax ADP, or the star-schema tables |

### Vendored from upstream

**Idea → ship engineering flow** (see `ask-matt` for the full map):

| Skill | Description | Source |
|-------|-------------|--------|
| **grill-with-docs** | Thin orchestrator: runs a `/grilling` session using the `/domain-modeling` skill. Start here when you have a codebase. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **grill-me** | Same relentless interview, but stateless — for when you have no codebase. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **grilling** | Sequential, one-question-at-a-time interview discipline: withhold execution until shared understanding is reached. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **domain-modeling** | Active discipline for building/sharpening a project's domain model: challenge terminology, stress-test with scenarios, maintain `CONTEXT.md` and ADRs inline. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **to-spec** | Synthesize the current conversation into a spec/PRD, publish to the issue tracker. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **to-tickets** | Break a spec/plan into tracer-bullet tickets, each declaring its blocking edges. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **implement** | Build a ticket via `/tdd` at pre-agreed seams, close out with `/two-axis-code-review`. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **tdd** | Red-green-refactor discipline: what a good test is, seams, anti-patterns. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **two-axis-code-review** *(forked)* | Standards + Spec review of a diff against a fixed point, in parallel sub-agents. Forked from upstream `code-review` — renamed to avoid colliding with this repo's general-purpose `code-review` skill. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **triage** | Move incoming issues/external PRs through a state machine: categorize, verify, grill if needed, write agent-ready briefs. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **diagnosing-bugs** | Diagnosis loop for hard bugs/perf regressions — tight feedback loop, then fix with a regression test. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **wayfinder** | Chart a huge, foggy effort as a shared map of investigation tickets, resolved one at a time. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **improve-codebase-architecture** | Scan for deepening opportunities, present as a visual HTML report, grill through the chosen one. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **codebase-design** | Deep-module vocabulary (module, interface, depth, seam, adapter, leverage, locality). | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **prototype** | Small, throwaway program that answers one design question. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **resolving-merge-conflicts** | Resolve an in-progress git merge/rebase conflict. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **ask-matt** | Router: which skill or flow fits your situation, given everything above. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **setup-matt-pocock-skills** | Bootstrap: configures the issue tracker (GitHub/GitLab/local-markdown), triage labels, and domain doc layout the flow above assumes. Run once first. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **handoff** | Compact the current conversation into a handoff document for another agent to pick up. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **teach** | Multi-session teaching workspace for any topic — not engineering-specific. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **writing-great-skills** | Reference for writing and editing skills well. | [mattpocock/skills](https://github.com/mattpocock/skills) |

**Other:**

| Skill | Description | Source |
|-------|-------------|--------|
| **frontend-design** | Create distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **azure-resource-manager-playwright-dotnet** | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET — management-plane ops (workspaces, quotas, name availability). | [microsoft/skills](https://github.com/microsoft/skills) |
| **everything-claude-code** | Development conventions and patterns reference generated from the everything-claude-code project. | [affaan-m/ECC](https://github.com/affaan-m/ECC) |

**Deliberately not vendored:** Pocock's `research` skill (thin background-agent-reads-primary-sources tool) — the existing `deep-research` skill already covers this with more rigor (multi-source fan-out, adversarial claim verification).

---

## Sources & Credits

Vendored skills are static copies of a single skill folder from each upstream repo. The authoritative pins live in [`vendor-skills.json`](vendor-skills.json); the table below mirrors it for readability. To check for and apply updates, run [`tools/update-vendor-skills.ipynb`](tools/update-vendor-skills.ipynb) (see **Maintaining vendored skills** below).

| Skill | Upstream repo | Pinned ref | Source path within repo |
|-------|---------------|-----------|-------------------------|
| frontend-design | `anthropics/claude-code` | `295dee8` (v2.1.158) | `plugins/frontend-design/skills/frontend-design/` |
| azure-resource-manager-playwright-dotnet | `microsoft/skills` | `684313b` | `.github/plugins/azure-sdk-dotnet/skills/azure-resource-manager-playwright-dotnet/` |
| everything-claude-code | `affaan-m/ECC` | `64cd1ba` | `.claude/skills/everything-claude-code/` |
| grill-me | `mattpocock/skills` | `e3b90b5` | `skills/productivity/grill-me/` |
| grilling | `mattpocock/skills` | `391a270` | `skills/productivity/grilling/` |
| domain-modeling | `mattpocock/skills` | `391a270` | `skills/engineering/domain-modeling/` |
| grill-with-docs | `mattpocock/skills` | `391a270` | `skills/engineering/grill-with-docs/` |
| handoff | `mattpocock/skills` | `e3b90b5` | `skills/productivity/handoff/` |
| ask-matt | `mattpocock/skills` | `391a270` | `skills/engineering/ask-matt/` |
| codebase-design | `mattpocock/skills` | `391a270` | `skills/engineering/codebase-design/` |
| diagnosing-bugs | `mattpocock/skills` | `391a270` | `skills/engineering/diagnosing-bugs/` |
| implement | `mattpocock/skills` | `391a270` | `skills/engineering/implement/` |
| improve-codebase-architecture | `mattpocock/skills` | `391a270` | `skills/engineering/improve-codebase-architecture/` |
| prototype | `mattpocock/skills` | `391a270` | `skills/engineering/prototype/` |
| resolving-merge-conflicts | `mattpocock/skills` | `391a270` | `skills/engineering/resolving-merge-conflicts/` |
| setup-matt-pocock-skills | `mattpocock/skills` | `391a270` | `skills/engineering/setup-matt-pocock-skills/` |
| tdd | `mattpocock/skills` | `391a270` | `skills/engineering/tdd/` |
| to-spec | `mattpocock/skills` | `391a270` | `skills/engineering/to-spec/` |
| to-tickets | `mattpocock/skills` | `391a270` | `skills/engineering/to-tickets/` |
| triage | `mattpocock/skills` | `391a270` | `skills/engineering/triage/` |
| wayfinder | `mattpocock/skills` | `391a270` | `skills/engineering/wayfinder/` |
| teach | `mattpocock/skills` | `391a270` | `skills/productivity/teach/` |
| writing-great-skills | `mattpocock/skills` | `391a270` | `skills/productivity/writing-great-skills/` |
| code-review *(pristine mirror — see `forks[]`)* | `mattpocock/skills` | `391a270` | `skills/engineering/code-review/` → `vendor-cache/code-review/` |

### Related (not a skill)

- [mbtiusa/awesome-mbti](https://github.com/mbtiusa/awesome-mbti) — a curated list of MBTI resources, tools, and research.

---

## Maintaining vendored skills

[`tools/update-vendor-skills.ipynb`](tools/update-vendor-skills.ipynb) reads [`vendor-skills.json`](vendor-skills.json) and, for each vendored skill, queries the GitHub API for the latest commit touching its source path:

1. **Check** — running all cells prints a status table (pinned vs latest commit, with a `compare` link for anything out of date).
2. **Update** — `update_skill("<name>", apply=True)` re-downloads that skill's folder from the latest upstream commit, replaces the local copy, and re-pins `vendor-skills.json`. It's a dry run unless `apply=True`.
3. Review the resulting `git diff` before committing — upstream skills can change structure or licensing.

> Set a `GITHUB_TOKEN` environment variable to lift the GitHub API rate limit from 60 to 5,000 requests/hour.

To add a new vendored skill, copy its folder into `skills/` and add a matching entry to `vendor-skills.json`.

---

## Conventions

- One skill per folder under `skills/`, named for the skill, each with a `SKILL.md` at its root.
- `SKILL.md` frontmatter carries `name` and `description` (and a trigger hint in the description).
- Authored skills and vendored copies live side by side; provenance is tracked in **Sources & Credits**, not in the directory layout.

---

## Roadmap

`plugins/` and `hooks/` are scaffolded but intentionally empty. Status:

- ~~**Vendor drift fix**: `grill-with-docs` had diverged from upstream.~~ **Done** — both dependencies (`grilling`, `domain-modeling`) vendored, `grill-with-docs` realigned to upstream's thin pointer.
- ~~**Saturate `mattpocock/skills`**: evaluate the full `productivity`/`engineering` catalog.~~ **Done** — adopted the full idea→ship engineering flow (see Skills table above) using its local-markdown tracker mode. Skipped `research` (redundant with `deep-research`). Forked `code-review` → `two-axis-code-review` (naming collision with the existing general-purpose `code-review` skill) using the `vendor-cache/` pristine-mirror pattern documented above.
- **ponytail evaluation**: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) is a direct competitor to `caveman` (its own benchmark suite scores against caveman) and ships a real multi-platform `plugin.json`/`marketplace.json` pattern worth using as a reference for populating `plugins/`. Not yet evaluated.
- **`update-vendor-skills.ipynb` rework**: still has no drift-detection (only staleness-of-pinned-commit) and no incoming/outgoing manifest concept. Fork-handling now has a real first case (`two-axis-code-review`) to design against — currently a manual process (see `forks[]` in `vendor-skills.json`).
- **`project-memory-template`**: synthesize a reusable project memory-architecture template from `Python-PowerBI-DynastyFantasyFootball`, informed by the engineering flow now vendored above.
- **Enforcement**: hooks/subagents that scan repo structure on check-in for compliance with the agreed template, and flag any skill/plugin/hook checked in from a non-central source.
