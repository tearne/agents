# Design: Versioning Negotiated Bumps
**Status: Approved**

## Approach

Two targeted edits:

1. **`PROPOSAL.md` `Designing → Implementing`** — replace the single review cadence paragraph with an explicit kickoff checklist. The checklist is required before implementation begins and notes that active guides may contribute additional items (e.g. VERSIONING.md adds version bump when in use).

2. **`VERSIONING.md`** — add a negotiated-bump section after the existing table. Describes the pattern for manual releases: agree bump level at kickoff, acceptable to revise as implementation progresses. The "when in doubt, prefer patch" rule is retained for automated contexts but the negotiated pattern takes precedence when VERSIONING.md is actively in use on a project.

## Tasks

1. ✓ Impl: Update `AGENT/PROCESS/PROPOSAL.md` — replace review cadence paragraph with kickoff checklist
2. ✓ Impl: Update `AGENT/ADDITIONAL/VERSIONING.md` — add negotiated-bump section
3. Process: Confirm ready to archive
