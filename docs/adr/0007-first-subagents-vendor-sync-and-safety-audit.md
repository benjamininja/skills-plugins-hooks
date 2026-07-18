# First subagents in this repo: closing two judgment gaps found during ADR-0006's own execution

- Status: accepted
- Date: 2026-07-17
- Scope: `.claude/agents/vendor-sync-reapply.md`,
  `.claude/agents/skill-safety-auditor.md`, `tools/update_vendor_skills.py`

## Context

This repo is named `skills-plugins-hooks-agents` but had zero
`.claude/agents/` definitions; the first real roster elsewhere is the
Dynasty repo's (its ADR-0009), produced by the same `/subagent-audit` skill
used here.

Running `/subagent-audit` against this repo surfaced two concrete gaps, both
evidenced by what actually happened during [ADR-0006](0006-blast-radius-tiered-model-invocation.md)'s
own execution, in the same session:

1. The `known_local_edits` reapply step (`tools/update_vendor_skills.py`'s
   own printed "reapply ritual") is explicitly a judgment call — "judgment
   call if upstream rewrote that section" is the tool's own text — with zero
   enforcement today. Nothing catches a silently-lost edit except a human
   remembering to look, the same failure shape as the junction drift
   ADR-0005 already caught once.
2. While tiering skills for ADR-0006's low-blast-radius list, the main agent
   initially mis-classified `triage` and `wayfinder` as low-risk on a first
   pass, and only corrected it after the user pushed back. Both actually
   write to the external issue tracker. This is exactly the kind of
   builder-bias mistake a fresh, adversarial read — not anchored to a
   proposal already made — is suited to catch.

## Decision

Add two subagents:

- **`vendor-sync-reapply`** (background, category E — background
  specialist) — triggered after any `--apply <name>` that prints a
  reapply-ritual notice; reapplies each `known_local_edits` entry, judges
  whether upstream's restructuring still lets the edit apply cleanly,
  re-`--bless`es, and reports back rather than trusting the reminder to be
  read.
- **`skill-safety-auditor`** (foreground, category B — domain auditor) —
  triggered before committing any change to `disable-model-invocation`, a
  new vendored skill, or `vendor-skills.json`'s safety fields; independently
  judges blast radius from each skill's actual body against ADR-0005/0006's
  criteria, without seeing the main agent's proposed tier first, and flags
  any mismatch.

Both are read/isolated-judgment tasks, not deterministic — disqualifying
them from being hooks — and neither duplicates an existing skill.

## Alternatives rejected

- **A single combined "vendor maintenance" agent** — rejected; the two
  triggers don't overlap (post-`--apply` vs. pre-commit) and the safety
  auditor needs to stay read-only/adversarial, which a combined agent doing
  both review and editing would compromise.
- **Turning the reapply ritual into a hook** — rejected; the tool's own text
  calls it a "judgment call," which by this repo's hook/subagent line
  disqualifies a deterministic script.
- **Leaving both as manual human steps** — the status quo; rejected because
  the session that produced this ADR is itself evidence the manual version
  fails silently (a real mis-tiering almost shipped uncorrected).

## Consequences

- First `.claude/agents/` roster in this repo — `CATALOG.md`'s "Agents (0
  here)" line is now stale and should be corrected on a future
  `tools/build_catalog.py` update (the script does not currently enumerate
  agents; follow-up, not blocking).
- `skill-safety-auditor` adds a foreground step before future
  model-invocation-tier changes — mild friction, intentional, given the
  near-miss this session.
- `vendor-sync-reapply` running in the background means its report arrives
  asynchronously; a future `--apply` should be treated as incomplete until
  that report lands, not just until the command exits.
