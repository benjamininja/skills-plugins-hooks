# skills

A curated personal library of [Claude Code](https://claude.ai/code) skills — modular instruction sets that extend Claude's capabilities for specific domains and workflows. Every skill lives at a flat, loadable path (`skills/<name>/SKILL.md`) so the whole collection can be dropped straight into a Claude Code skills directory.

Some skills are authored here; others are vendored from upstream projects and credited below. Attribution lives in this README and in each skill's `SKILL.md` — not in the folder names.

---

## Repository Structure

```
skills/
├── caveman/                                    # token-compression communication
├── fantasy-football-python/                    # dynasty fantasy football ETL
│   └── references/data_model.md
├── frontend-design/                            # production-grade frontend UI
├── azure-resource-manager-playwright-dotnet/   # Azure Playwright Testing ARM SDK (.NET)
├── everything-claude-code/                     # Claude Code conventions reference
├── skill-seekers/                              # build skills from any source (MCP)
├── grill-me/                                   # stress-test a plan via interview
├── grill-with-docs/                            # grill a plan against your docs
└── handoff/                                    # compact a session into a handoff doc
```

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
| **skill-seekers** | Build AI skills from documentation, repos, PDFs, or videos via the Skill Seekers MCP server. *(Requires the Skill Seekers MCP server.)* | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) |
| **grill-me** | Interview the user relentlessly about a plan until reaching shared understanding, resolving each branch of the decision tree. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **grill-with-docs** | Grilling session that challenges a plan against the existing domain model and updates docs (CONTEXT.md, ADRs) inline. | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **handoff** | Compact the current conversation into a handoff document for another agent to pick up. | [mattpocock/skills](https://github.com/mattpocock/skills) |

---

## Sources & Credits

Vendored skills are static copies of a single skill folder from each upstream repo. To refresh one, re-copy the relevant folder from the source at a newer commit and update the pin below.

| Skill | Upstream repo | Pinned ref | Source path within repo |
|-------|---------------|-----------|-------------------------|
| frontend-design | `anthropics/claude-code` | `295dee8` (v2.1.158) | `plugins/frontend-design/skills/frontend-design/` |
| azure-resource-manager-playwright-dotnet | `microsoft/skills` | `684313b` | `.github/plugins/azure-sdk-dotnet/skills/azure-resource-manager-playwright-dotnet/` |
| everything-claude-code | `affaan-m/ECC` | `64cd1ba` | `.claude/skills/everything-claude-code/` |
| skill-seekers | `yusufkaraaslan/Skill_Seekers` | `ff7d3af` (development) | `skills/skill-seekers/` |
| grill-me | `mattpocock/skills` | `e3b90b5` | `skills/productivity/grill-me/` |
| grill-with-docs | `mattpocock/skills` | `e3b90b5` | `skills/engineering/grill-with-docs/` |
| handoff | `mattpocock/skills` | `e3b90b5` | `skills/productivity/handoff/` |

### Related (not a skill)

- [mbtiusa/awesome-mbti](https://github.com/mbtiusa/awesome-mbti) — a curated list of MBTI resources, tools, and research.

---

## Conventions

- One skill per folder under `skills/`, named for the skill, each with a `SKILL.md` at its root.
- `SKILL.md` frontmatter carries `name` and `description` (and a trigger hint in the description).
- Authored skills and vendored copies live side by side; provenance is tracked in **Sources & Credits**, not in the directory layout.
