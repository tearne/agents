# Proposal: Process Document Clarifications
**Status: Approved**

## Intent
Two related process clarifications:

1. **Proposal filename**: The process currently names proposal documents `proposal_formal.md` or `proposal_lite.md`, encoding the change mode into the filename. In practice this causes duplicate files when a draft is created before mode selection, and adds no real value — the two proposal formats are identical in structure. The mode is a property of how implementation is executed, not of the proposal document itself.

2. **Active change scope**: The current wording warns against "opening a new change" while one is active, which is too broad. Notes and proposals can legitimately be created at any time — the constraint is on starting implementation (touching code). The distinction should be made explicit.

## Specification Deltas

### MODIFIED
- `proposal_formal.md` and `proposal_lite.md` unified to a single filename: `proposal.md`
- The distinction between Formal and Lite clarified as an implementation cadence choice, not a document type difference
- `active.md` is already the canonical record of change type; the proposal filename need not duplicate it
- Active change warning tightened: the agent should warn when a second change is about to begin *implementation* while one is already active, not when notes or proposals are being created

### REMOVED
- Type suffix from proposal filenames across `README.md`, `FORMAL.md`, and `LITE.md`
