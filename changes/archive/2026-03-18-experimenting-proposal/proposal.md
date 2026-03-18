# Proposal: Experimenting Form
**Status: Approved**

## Intent
When exploring solutions or trying out different approaches, there is currently no structure to track what has been attempted, what was learned, and where things stand. An "experimenting" form provides a lightweight way to log this work — separate from the change management process, since experiments may not lead to a spec change at all.

## Specification Deltas

### ADDED

- **Experiment files** — An experiment is a single `experiment.md` file in `changes/open/<experiment-name>/`, following this template:

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

- **One active item** — No more than one proposal or experiment may have `Active` status at a time. Starting a new experiment requires the current active item to be completed, parked, or abandoned first.

- **Adoption path** — When an experiment is adopted (including cases where the experiment has done most or all of the implementation work), write a `washup.md` in the same folder capturing intent and spec deltas. The washup takes the place of a proposal for archive purposes. Archive the folder to `changes/archive/YYYY-MM-DD-<experiment-name>/` with both files present.

- **Abandonment and parking** — Abandoned and parked experiments are archived as-is with no washup required. A parked experiment may be resumed by moving it back to `changes/open/`.
