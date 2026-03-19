# Proposal: Unify Formal and Lite into a Single Process
**Status: Approved**

## Intent
With proposal documents now unified to `proposal.md`, the only remaining distinction between Formal and Lite is implementation cadence — how often the agent pauses for review. Two separate process files to express a single axis of variation is unnecessary complexity. A single process file with a cadence choice at the start of implementation is cleaner and easier to follow.

## Specification Deltas

### ADDED
- A single unified change process file (replacing `FORMAL.md` and `LITE.md`) covering four phases: Propose, Design, Implement, Archive
- Review cadence (per-task vs end review) is decided ad hoc by the user — not a prescribed selection step

### MODIFIED
- `README.md` updated to describe one process type (Proposal) instead of Formal and Lite

### REMOVED
- `PROCESS/FORMAL.md`
- `PROCESS/LITE.md`

## Scope
- **In scope**: consolidating the two process files; updating all references in `README.md`
- **Out of scope**: changes to Note or Experiment; changes to proposal/design document structure; `CLAUDE.md`
