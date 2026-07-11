# Forked skills get a pristine mirror in `vendor-cache/`, never symlinked

- Status: accepted
- Date: 2026-07-11 (backfilled — decision made during Goal 2)
- Scope: `vendor-skills.json`'s `forks[]` array, `vendor-cache/`,
  `skills/two-axis-code-review/`

## Context

Vendoring Matt Pocock's full engineering flow surfaced a naming collision:
upstream `mattpocock/skills` ships an `engineering/code-review` skill, but
this repo already had an established, general-purpose `code-review` skill
serving a different scope. Faithfully vendoring Pocock's skill under its own
name would silently shadow or conflict with the existing one; skipping it
entirely would lose real value (Standards+Spec parallel-subagent review is
genuinely useful and not redundant with the general reviewer).

## Decision

1. Rename the vendored skill to `two-axis-code-review` in `skills/` — the
   actual, usable, loadable copy.
2. Keep a **pristine, untouched mirror** of the unrenamed upstream skill at
   `vendor-cache/two-axis-code-review` → tracked as `vendor-cache/code-
   review/` — git-tracked, pinned in `vendor-skills.json` like any normal
   vendor entry, but deliberately placed **outside** `skills/` so it is
   never symlinked or loaded.
3. Link the two via a new `forks[]` array in `vendor-skills.json`
   (`forked_from`, `forked_at_commit`, `local_path`, `reason`).

## Alternatives rejected

- **Vendor faithfully, accept the collision** — would require the user to
  disambiguate every time either skill might apply; rejected as a usability
  regression baked into the catalog permanently.
- **Skip the skill entirely** — loses genuine value (parallel Standards +
  Spec review) with no naming conflict, but throws out something useful to
  avoid a naming problem that has a cheap fix.
- **Rename with no pristine mirror kept** — simplest option, but loses the
  ability to diff against upstream changes later (`update-vendor-
  skills.ipynb` has nothing to compare the renamed, edited copy against).

## Consequences

- Future upstream changes to `mattpocock/skills`' `code-review` skill can be
  diffed against the pristine `vendor-cache/` mirror to see what changed,
  before deciding whether to pull updates into the renamed fork.
- `vendor-cache/` entries are explicitly excluded from the per-skill
  install/symlink loop (see
  [ADR-0003](0003-junction-vs-symlink-fallback.md)) — anything added there
  must never be duplicated into `skills/` under its original name, or the
  original collision returns.
- This is the first fork; the pattern (and `update-vendor-skills.ipynb`'s
  lack of automation for it) is real, scoped future work — see repo root
  `README.md` Roadmap.
