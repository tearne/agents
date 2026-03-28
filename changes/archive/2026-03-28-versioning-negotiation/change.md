# Versioning: Negotiated Bumps
**Type**: Proposal
**Status**: Approved

## Intent
Several things need to be agreed with the user at the start of implementation, but they are currently scattered — review cadence is in `PROPOSAL.md`, version bump is not defined at all. Consolidate these into a defined kickoff moment at the start of the `Approved → Designing` or `Designing → Implementing` transition, so the agent asks for everything upfront in one go.

Things to agree at implementation kickoff (may evolve during the change):
- **Review cadence** — per-task or end review (currently in PROPOSAL.md, to be consolidated here)
- **Version bump level** — major/minor/patch, agreed based on what the change represents; it is acceptable for this to change as implementation progresses

## Specification Deltas

### MODIFIED
- `AGENT/PROCESS/PROPOSAL.md` `Designing → Implementing` — replace the current review cadence paragraph with an explicit kickoff checklist: review cadence (required), plus any items added by active guides; note that VERSIONING.md contributes version bump when in use
- `AGENT/ADDITIONAL/VERSIONING.md` — add a negotiated-bump section: when a project manages releases manually, agree the bump level (major/minor/patch) with the user at implementation kickoff based on what the accumulated changes represent; acceptable for the level to change as implementation progresses
