# Design: Process Replacement
**Status**: Draft

## Approach

Replace the three-file process (`PROCESS/README.md`, `PROCESS/PROPOSAL.md`, `PROCESS/SPIKE.md`) with a single `AGENT/PROCESS.md`, based on `process-draft.md` from the process-simplification spike. Update `AGENT/README.md` to reference the new file. Update `SPEC.md` to reflect the new structure. Migrate the one other open change (`misc-improvements`) from a folder to a single file.

Review cadence: end.

## Tasks
- [x] ADD: `AGENT/PROCESS.md` from `process-draft.md`
- [x] REMOVE: `AGENT/PROCESS/README.md`, `AGENT/PROCESS/PROPOSAL.md`, `AGENT/PROCESS/SPIKE.md` and the `AGENT/PROCESS/` folder
- [x] CHANGE: `AGENT/README.md` — update Change Process summary and replace `@PROCESS/README.md` with `@PROCESS.md`
- [x] CHANGE: `SPEC.md` — update always-loaded files list and changes directory description
- [x] CHANGE: migrate `changes/open/misc-improvements/change.md` to `changes/open/misc-improvements.md`
- [x] REVIEW: confirm all references to old process files are gone
