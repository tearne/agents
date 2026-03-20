# Process
This file covers how changes are managed. For project-level concepts (specs, changes directory), see `AGENT/README.md`.

## Types of Change

**Note** — A `note.md` in `changes/open/<name>/`. Freeform, no required structure. Notes do not touch code and are exempt from active change tracking. To progress a Note, the user selects a type (Proposal or Experiment); the `note.md` is retained alongside the new `proposal.md` or `experiment.md` as a record of the original capture.

**Proposal** — A four-phase process: Propose, Design, Implement, Archive. Review cadence during implementation (per-task or end review) is agreed with the user at the start of that phase. See `PROCESS/PROPOSAL.md`.

**Experiment** — Exploratory work outside the change process. May or may not lead to a spec change. See `PROCESS/EXPERIMENT.md`.

## Active Change Tracking

A file `changes/open/active.md` records the current active change — one that is modifying project assets. The agent must:
- Check for `changes/open/active.md` at the start of each session and remind the user of the active change if one is recorded.
- Create or update `active.md` when a change begins touching code.
- Warn the user if a second change is about to begin *implementation* while one is already recorded in `active.md`.
- Remove `active.md` when the active change is archived.

Notes, proposals, and experiment documents may be created freely at any time — none become active until project assets are modified. A change stops being active when it is archived.

Format:
```markdown
# Active Change
**Name**: <change-name>
**Type**: Proposal | Experiment
**Phase**: <current phase or status>
```

## Additional Guides

The `ADDITIONAL/` directory contains guides that are not always loaded. `ADDITIONAL/README.md` lists what is available. Two loading modes:
- **Passive** — the user names the guide in a spec or proposal; the agent applies it from there
- **Prompted** — the agent raises the guide when context warrants, without waiting to be told (e.g. `VERSIONING.md` when a project is being set up or a breaking change is being made)

Companion files named `*-elaboration.md` exist alongside some guides. They contain examples and references and need not be loaded unless the agent judges additional context is needed.

## Starting a Change

Changes can begin as a Note (freeform capture) or directly as a Proposal or Experiment. A Note can be progressed to either type when the intent is clear enough to commit to a direction.
