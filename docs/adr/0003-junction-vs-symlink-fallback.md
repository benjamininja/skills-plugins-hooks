# Directory junctions as the practical Windows install mechanism, not true symlinks

- Status: accepted
- Date: 2026-07-11
- Scope: `README.md` Installation section, the actual install run on this
  machine

## Context

The README originally documented a single symlink pointing
`~/.claude/skills/library` at this repo's whole `skills/` folder. That
instruction was wrong on two counts, found during a distribution
verification pass: (1) Claude Code discovers skills **one level deep
only** — `~/.claude/skills/<name>/SKILL.md` — so a nested `library/<name>/
SKILL.md` is never found regardless of link type; (2) `New-Item -ItemType
SymbolicLink` on Windows requires admin privileges or Developer Mode, and
this machine had neither enabled when the install was actually run.

## Decision

1. Fix the install instructions to link **each skill individually** —
   `~/.claude/skills/<name>` per skill, not one library-level link.
2. Use **directory junctions** (`New-Item -ItemType Junction`) as the
   default/fallback when symlinks aren't available — junctions need no
   elevation on Windows and behave identically for local skill discovery.
3. Document both the symlink and junction forms in the README, with the
   junction-specific caveat: an absolute local path is baked in at creation
   time, so moving or renaming this repo's folder silently breaks every
   junction (skills just stop resolving, no error) until re-linked.

## Alternatives rejected

- **Require the user to enable Developer Mode or run elevated** — works,
  but adds a real setup step (a Windows settings change, or remembering to
  open an elevated terminal) for something junctions solve with zero
  privilege escalation.
- **Copy skill folders instead of linking** — avoids the elevation problem
  entirely, but reintroduces the exact live-vs-central drift this same
  verification pass found and fixed (`fantasy-football-python`,
  `grill-with-docs`) — a copy has no mechanism keeping it in sync with the
  source of truth.

## Consequences

- Actual install on this machine uses junctions for all 34 catalog skills
  under `~/.claude/skills/`.
- If this repo's local path ever changes, every junction needs
  re-creation — the install command is idempotent and safe to re-run, but
  nothing currently detects the breakage automatically (a candidate for the
  check-in hygiene hook already logged as future work).
- True symlinks remain documented as the preferred form when elevation is
  available (support cross-volume and relative targets, which junctions
  don't) — junctions are the pragmatic default, not a universal
  replacement.
