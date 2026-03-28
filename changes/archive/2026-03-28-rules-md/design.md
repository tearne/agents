# Design: Rules.md
**Status: Approved**

## Approach

`AGENT/README.md` is restructured to lead with two new sections before the `@`-includes:

**Rules** — positively-framed gates, one line each:
- Git writes require explicit user instruction
- Change management decisions (starting, pausing, advancing, archiving) require explicit user instruction
- Approval is always a user action — the agent never approves
- Change documents (`changes/`) may always be created or edited freely

**Change Process** — one-liner per type with a pointer to the detail document; replaces the high-level orientation currently spread across PROCESS/README.md's opening.

The git rule is removed from BEHAVIOUR.md since it moves to README.md. BEHAVIOUR.md retains the markdown rule.

The preamble in `setup.py` is unchanged — it already points to README.md.

## Tasks

1. ✓ Impl: Restructure `AGENT/README.md` — add Rules and Change Process sections before `@`-includes
2. ✓ Impl: Update `AGENT/BEHAVIOUR.md` — remove git rule
3. ✓ Impl: Update `setup.py` and `test.py` — slim preamble to single pointer
4. ✓ Impl: Move markdown rule from `AGENT/BEHAVIOUR.md` to `AGENT/STYLE.md`; delete `AGENT/BEHAVIOUR.md`; update `@`-include in `AGENT/README.md`
5. ✓ Spec: Update `SPEC.md` — reflect restructured README.md, slimmed preamble, BEHAVIOUR.md removal
6. Process: Confirm ready to archive
