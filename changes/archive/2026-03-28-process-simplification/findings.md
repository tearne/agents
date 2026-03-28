# Findings: Process Simplification

## Summary

The new process collapses three change types (Fix, Proposal, Spike) into one. A single `change.md` with four sections — Intent, Approach, Plan/Log, Conclusion — handles all cases. The document shape describes the change; no type or status field is needed.

## Key Simplifications

- Single file per change (folder only if assets are produced)
- `PROCESS/README.md` + `PROCESS/PROPOSAL.md` + `PROCESS/SPIKE.md` → single `PROCESS.md`
- `design.md` and `findings.md` eliminated
- Sections added sequentially, approval-gated

## Retained from Current System

- `active.md` as a lock file (name only)
- Archival convention (`changes/archive/YYYY-MM-DD-<change-name>`)
- Kickoff questions before work begins

## Trade-offs Accepted

- Spec deltas structure lost — agent reads `SPEC.md` and applies judgement
- TDD guidance removed from process — left to user review of tasks

## Next Step

Proceed to a proposal to replace the current system, using `process-draft.md` as the basis.
