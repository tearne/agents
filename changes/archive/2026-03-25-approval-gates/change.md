# Approval Gates
**Type**: Proposal
**Status**: Approved

## Intent
Agents are skipping approval steps — setting active proposals aside autonomously, and starting fix work without getting change.md approved. The current rules gate edits but not decisions. This proposal adds explicit decision gates to both the preamble and README.md.

## Specification Deltas

### MODIFIED
- **Preamble** (`setup.py`) — add a second rule: no change management decision (starting, pausing, advancing, or archiving a change) without explicit user instruction
- **`AGENT/PROCESS/README.md`** — add explicit rule that the active change cannot be paused or replaced without user instruction; make fix approval gate more prominent

### REMOVED
- **`AGENT/PROCESS/PROPOSAL.md`** — "Do not advance status without explicit user instruction" line; superseded by the rule in README.md
