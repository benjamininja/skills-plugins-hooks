# skills-plugins-hooks

The central repository for [Claude Code](https://claude.ai/code) skills, plugins, and hooks — modular instruction sets, bundled plugin packages, and event-triggered automations. Every skill lives at a flat, loadable path (`skills/<name>/SKILL.md`) so the whole collection can be dropped straight into a Claude Code skills directory.

Some skills are authored here; others are vendored from upstream projects and credited below. Attribution lives in this README and in each skill's `SKILL.md` — not in the folder names.

---

## Repository Structure

```
.
├── manifest.json                               # top-level inventory: skills / plugins / hooks membership
├── vendor-skills.json                          # manifest: pins each vendored skill's upstream commit
├── tools/
│   └── update-vendor-skills.ipynb              # checks upstream for newer versions & re-pins
├── skills/
│   ├── caveman/                                # token-compression communication
│   ├── fantasy-football-python/                # dynasty fantasy football ETL
│   │   └── references/data_model.md
│   ├── frontend-design/                        # production-grade frontend UI (+ LICENSE.txt)
│   ├── azure-resource-manager-playwright-dotnet/   # Azure Playwright Testing ARM SDK (.NET)
│   ├── everything-claude-code/                 # Claude Code conventions reference
│   ├── grill-me/                               # stress-test a plan via interview
│   ├── grilling/                               # sequential interview discipline (grill-with-docs dependency)
│   ├── domain-modeling/                        # CONTEXT.md/ADR discipline (grill-with-docs dependency)
│   ├── grill-with-docs/                        # thin pointer: runs /grilling using /domain-modeling
│   └── handoff/                                # compact a session into a handoff doc
├── plugins/                                    # reserved: bundled skill+hook+MCP packages (empty — see Roadmap)
└── hooks/                                      # reserved: standalone event-triggered hooks (empty — see Roadmap)
```

`manifest.json` tracks *membership* (what's in this repo, by category). `vendor-skills.json` tracks *provenance* (upstream repo/commit for vendored skills) — the two are separate and both authoritative for their own concern.

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

| Skill | Description | Source |
|-------|-------------|--------|
| **frontend-design** | Create distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **azure-resource-manager-playwright-dotnet** | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET — management-plane ops (workspaces, quotas, name availability). | [microsoft/skills](https://github.com/microsoft/skills) |
| **everything-claude-code** | Development conventions and patterns reference generated from the everything-claude-code project. | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **grill-me** | Interview the user relentlessly about a plan until reaching shared understanding, resolving each branch of the decision tree. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **grilling** | Sequential, one-question-at-a-time interview discipline: withhold execution until shared understanding is reached. Depended on by `grill-with-docs`. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **domain-modeling** | Active discipline for building/sharpening a project's domain model: challenge terminology, stress-test with scenarios, maintain `CONTEXT.md` and ADRs inline. Depended on by `grill-with-docs`. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **grill-with-docs** | Thin orchestrator: runs a `/grilling` session using the `/domain-modeling` skill. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **handoff** | Compact the current conversation into a handoff document for another agent to pick up. | [mattpocock/skills](https://github.com/mattpocock/skills) |

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

- ~~**Vendor drift fix**: `grill-with-docs` had diverged from upstream (a full standalone implementation vs. upstream's 4-line pointer to `/grilling` + `/domain-modeling`).~~ **Done** — both dependencies are now vendored and `grill-with-docs` realigned to upstream's thin pointer.
- **Saturate (in progress)**: `mattpocock/skills/productivity` and `/engineering` have ~17 more skills not yet evaluated (`ask-matt`, `code-review`, `codebase-design`, `diagnosing-bugs`, `implement`, `improve-codebase-architecture`, `prototype`, `research`, `resolving-merge-conflicts`, `setup-matt-pocock-skills`, `tdd`, `teach`, `to-spec`, `to-tickets`, `triage`, `wayfinder`, `writing-great-skills`) — pending a relevance pass, not blind-vendored.
- **ponytail evaluation**: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) is a direct competitor to `caveman` (its own benchmark suite scores against caveman) and ships a real multi-platform `plugin.json`/`marketplace.json` pattern worth using as a reference for populating `plugins/`. Not yet evaluated.
- **`update-vendor-skills.ipynb` rework**: still has no drift-detection (only staleness-of-pinned-commit), no fork-tracking, and no incoming/outgoing manifest concept. Deferred until the saturation/ponytail passes above establish real cases to design against.
- **`project-memory-template`**: synthesize a reusable project memory-architecture template from `Python-PowerBI-DynastyFantasyFootball`, informed by whatever lands in `plugins/`/`hooks/` above.
- **Enforcement**: hooks/subagents that scan repo structure on check-in for compliance with the agreed template, and flag any skill/plugin/hook checked in from a non-central source.
