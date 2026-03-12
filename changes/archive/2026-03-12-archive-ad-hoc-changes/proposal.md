# Proposal: Archive Ad-Hoc Changes
**Status: Approved**

## Intent
Some changes are implemented informally without a design phase. The archive should still accurately reflect what happened rather than leaving the proposal in an ambiguous state.

## Specification Deltas

### MODIFIED
- When archiving a change that was approved and implemented without a formal design phase, the proposal status must be updated to `Approved` before archiving
- A minimal `design.md` must be created (or updated) to record what was done, marked `*(retrospective)*` to indicate it was written after the fact rather than as a plan
- When archiving a change that has no proposal at all, the agent must prompt the user to retrospectively capture intent in a `proposal.md` before proceeding
