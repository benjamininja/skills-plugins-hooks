"""Generate CATALOG.md from the repo's real sources of truth.

Composes, without duplicating:
  - skills/*/SKILL.md frontmatter  -> name, description
  - vendor-skills.json             -> provenance (upstream repo = author)
  - manifest.json                  -> membership + tags (the only data
                                      authored specifically for the catalog)
  - hooks/*/README.md              -> first paragraph as summary

Also validates that manifest.json membership matches the skills/ directory
and that every tag is in manifest.json's _tag_taxonomy. Exits non-zero on
any drift so this can run as a check, not just a generator.

Usage:  python tools/build_catalog.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "CATALOG.md"


def frontmatter(path: Path) -> dict[str, str]:
    """Parse `key: value` YAML frontmatter, including block scalars (>, >-, |, |-)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    fields: dict[str, str] = {}
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", lines[i])
        i += 1
        if not kv:
            continue
        key, value = kv.group(1), kv.group(2).strip()
        if value in (">", ">-", "|", "|-"):
            block: list[str] = []
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            value = " ".join(part for part in block if part)
        fields[key] = value.strip().strip("\"'")
    return fields


def first_sentence(text: str, limit: int = 220) -> str:
    """Trim a long trigger-hint description to its first sentence."""
    text = " ".join(text.split())
    m = re.search(r"(?<=[.!?])\s", text)
    s = text[: m.start()] if m else text
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def hook_summary(hook_dir: Path) -> str:
    readme = hook_dir / "README.md"
    if not readme.exists():
        return ""
    for block in readme.read_text(encoding="utf-8").split("\n\n"):
        block = " ".join(block.split())
        if block and not block.startswith("#"):
            # hook READMEs are two levels deep; re-anchor their relative links
            return first_sentence(block.replace("](../../", "]("))
    return ""


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def main() -> int:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    vendors = json.loads((ROOT / "vendor-skills.json").read_text(encoding="utf-8"))
    errors: list[str] = []

    taxonomy = manifest["_tag_taxonomy"]
    allowed_tags = {t for values in taxonomy.values() for t in values}

    # provenance lookups
    vendor_by_local = {
        v["local_path"].removeprefix("skills/"): v
        for v in vendors["skills"]
        if v["local_path"].startswith("skills/")
    }
    forks = {f["local_path"].removeprefix("skills/"): f for f in vendors["forks"]}
    vendor_by_name = {v["name"]: v for v in vendors["skills"]}

    # membership vs directory drift
    manifest_names = [s["name"] for s in manifest["skills"]]
    dir_names = sorted(
        p.name
        for p in (ROOT / "skills").iterdir()
        if p.is_dir() and not p.name.startswith("_")
    )
    for missing in set(dir_names) - set(manifest_names):
        errors.append(f"skills/{missing}/ exists but is not in manifest.json")
    for ghost in set(manifest_names) - set(dir_names):
        errors.append(f"manifest.json lists '{ghost}' but skills/{ghost}/ does not exist")

    rows = []
    counts = {"authored": 0, "vendored": 0, "forked": 0}
    for entry in sorted(manifest["skills"], key=lambda s: s["name"]):
        name, tags = entry["name"], entry.get("tags", [])
        for t in tags:
            if t not in allowed_tags:
                errors.append(f"'{name}' has tag '{t}' not in _tag_taxonomy")

        skill_md = ROOT / "skills" / name / "SKILL.md"
        if not skill_md.exists():
            if name in dir_names:
                errors.append(f"skills/{name}/ has no SKILL.md")
            continue
        desc = first_sentence(frontmatter(skill_md).get("description", ""))

        if name in forks:
            upstream = vendor_by_name[forks[name]["forked_from"]]
            source, kind = f"forked from [{upstream['repo']}](https://github.com/{upstream['repo']})", "forked"
        elif name in vendor_by_local:
            repo = vendor_by_local[name]["repo"]
            source, kind = f"[{repo}](https://github.com/{repo})", "vendored"
        else:
            source, kind = "authored here", "authored"
        counts[kind] += 1

        stage = next((t for t in tags if t in taxonomy["stage"]), "?")
        domain = next((t for t in tags if t in taxonomy["domain"]), "?")
        rows.append((name, stage, domain, source, md_escape(desc)))

    plugin_rows = [
        (p["name"], f"[{p['repo']}](https://github.com/{p['repo']})", p.get("_comment", ""))
        for p in vendors["plugin_manifests_only"]
    ]
    hook_rows = [
        (h, md_escape(hook_summary(ROOT / "hooks" / h))) for h in manifest["hooks"]
    ]

    lines = [
        "# Catalog",
        "",
        "> **Generated file — do not hand-edit.** Rebuild with",
        "> `python tools/build_catalog.py`. Descriptions come from each",
        "> skill's `SKILL.md` frontmatter, provenance from",
        "> `vendor-skills.json`, membership + tags from `manifest.json`.",
        "",
        "## What's in this repo",
        "",
        f"- **Skills** ({len(rows)} loadable: {counts['authored']} authored, "
        f"{counts['vendored']} vendored, {counts['forked']} forked) — one folder per skill under "
        "`skills/`, each with a `SKILL.md`; junctioned into `~/.claude/skills/` per machine.",
        "- **Plugins** (3, manifest-only) — cataloged upstream bundles whose ~30 skills are deliberately "
        "not vendored (unused Fabric workloads). See `plugins/README.md` / ADR-0002.",
        f"- **Hooks** ({len(hook_rows)}, all installed on this machine) — deterministic event-triggered "
        "scripts under `hooks/`, registered in `~/.claude/settings.json`. See `hooks/README.md`.",
        "- **Vendor cache** (1) — pristine, never-loaded upstream mirrors of forked skills, for "
        "diffing. See ADR-0001.",
        "- **Agents** (0 here) — none cataloged yet; the first real `.claude/agents/` definitions "
        "live in the Dynasty repo (its ADR-0009), produced by `/subagent-audit`.",
        "",
        "## Skills",
        "",
        "Tags follow the routing-map axes (see README \"Routing: which skill, when\"): "
        f"stage = {' / '.join(taxonomy['stage'])}; domain = {' / '.join(taxonomy['domain'])}.",
        "",
        "| Skill | Stage | Domain | Source | Summary |",
        "|---|---|---|---|---|",
        *(f"| **{n}** | {s} | {d} | {src} | {desc} |" for n, s, d, src, desc in rows),
        "",
        "## Plugins (manifest-only)",
        "",
        "| Plugin | Upstream | Note |",
        "|---|---|---|",
        *(f"| **{n}** | {u} | {md_escape(first_sentence(c))} |" for n, u, c in plugin_rows),
        "",
        "## Hooks",
        "",
        "| Hook | Summary |",
        "|---|---|",
        *(f"| **{n}** | {s} |" for n, s in hook_rows),
        "",
    ]

    if errors:
        for e in errors:
            print(f"DRIFT: {e}", file=sys.stderr)
        return 1

    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(rows)} skills, "
          f"{len(plugin_rows)} plugins, {len(hook_rows)} hooks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
