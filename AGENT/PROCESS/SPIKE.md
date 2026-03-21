# Spike Process

Spikes are iterative exploration towards a clear goal where the path is unknown. The log is the primary record of the journey — keep it updated throughout. A spike may or may not lead to a spec change.

A spike begins with a `change.md` in `changes/open/<spike-name>/`, following this template:

```markdown
# <Change Name>
**Type**: Spike
**Status**: Active | Parked | Adopted | Abandoned

## Goal
What are we trying to achieve? (The path to get there is unknown.)

## Log
Freeform — attempts, observations, dead ends.

## Outcome
What was decided, and what happens next (if anything)?
```

**Adoption** — When a spike is adopted, write a `findings.md` in the same folder capturing: the journey summary, the final selected approach, and how the goal evolved (if it did). **Do not archive without an explicit user instruction.** Archive the folder to `changes/archive/YYYY-MM-DD-<spike-name>/` with both files present.

**Parking** — Leave in `changes/open/`; the spike may be resumed at any time.

**Abandonment** — No findings required. Archive to `changes/archive/YYYY-MM-DD-<spike-name>/` on explicit user instruction.
