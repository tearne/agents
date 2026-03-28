# Process Replacement
**Type**: Proposal
**Status**: Draft

## Intent
Replace the current three-type change process (Fix, Proposal, Spike) with a single unified process, as designed in the process-simplification spike. Fewer files, fewer concepts, same rigour.

## Specification Deltas

### MODIFIED
- `AGENT/PROCESS/` — replaced by a single `AGENT/PROCESS.md`
- `AGENT/README.md` — `@PROCESS/README.md` include updated to point at `AGENT/PROCESS.md`
- `SPEC.md` — updated to reflect new process structure

### REMOVED
- `AGENT/PROCESS/README.md`
- `AGENT/PROCESS/PROPOSAL.md`
- `AGENT/PROCESS/SPIKE.md`

## Conclusion
Replaced three-file process with a single `AGENT/PROCESS.md`. Updated `AGENT/README.md` and `SPEC.md`. Migrated `misc-improvements` to a single file. All stale references removed.

## Scope
- **In scope**: process documentation and SPEC.md; migration of open changes to new format
- **Out of scope**: ADDITIONAL/ guides (unchanged)
