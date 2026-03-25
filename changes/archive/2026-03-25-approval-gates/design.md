# Design: Approval Gates
**Status: Approved**

## Approach

Three targeted changes:

1. **Preamble** — add a second rule below the edit gate covering change management decisions
2. **`PROCESS/README.md`** — strengthen the active change tracking section to cover pausing/replacing, and make the fix approval gate a standalone rule rather than inline text
3. **`PROCESS/PROPOSAL.md`** — remove the now-redundant "Do not advance status without explicit user instruction" line

The new preamble decision gate rule:
> Do not make any change management decision — starting, pausing, advancing, or archiving a change — without explicit user instruction.

## Tasks

1. ✓ Impl: Update `setup.py` — add decision gate rule to preamble
2. ✓ Tests: Update `test.py` — verify decision gate rule appears in written config files
3. ✓ Impl: Update `AGENT/PROCESS/README.md` — strengthen active change tracking; make fix approval gate prominent
4. ✓ Impl: Update `AGENT/PROCESS/PROPOSAL.md` — remove redundant approval line
5. ✓ Spec: Update `SPEC.md` — reflect preamble change
6. Process: Confirm ready to archive
