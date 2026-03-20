# Experiment Process

Experiments are a lightweight way to explore solutions or try out approaches outside the change management process. An experiment may or may not lead to a spec change.

An experiment is a single `experiment.md` file in `changes/open/<experiment-name>/`, following this template:

```markdown
# Experiment: <name>
**Status: Active | Parked | Adopted | Abandoned**

## Question
What are we trying to find out?

## Log
Freeform — attempts, observations, dead ends.

## Outcome
What was decided, and what happens next (if anything)?
```

**Adoption** — When an experiment is adopted (including cases where it has done most or all of the implementation work), write a `washup.md` in the same folder capturing intent and spec deltas. Archive the folder to `changes/archive/YYYY-MM-DD-<experiment-name>/` with both files present.

**Parking and abandonment** — Parked and abandoned experiments are archived as-is with no washup required. A parked experiment may be resumed by moving it back to `changes/open/`.
