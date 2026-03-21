# Design: Process Enforcement and Change Type Simplification
**Status: Approved**

## Approach

Changes are spread across the process documents, `setup.py`, and `SPEC.md`. The implementation order follows dependencies: process docs first (they define the new types), then `setup.py` (adds the preamble), then `SPEC.md` (reflects the new structure).

The preamble written to `~/.claude/CLAUDE.md` and `~/.config/opencode/AGENTS.md` by `setup.py` will be a single imperative line appearing before the `@`-include:

> Before editing any project files outside `changes/`, the current change must be recorded in `changes/open/active.md`. See `AGENT/PROCESS/README.md` for the change process.

## Tasks

1. ✓ Process: Update `AGENT/PROCESS/README.md` — replace Note/Experiment with Fix/Spike; update active change tracking section (asset scope, change.md, retrospective creation, user waiver)
2. ✓ Process: Update `AGENT/PROCESS/PROPOSAL.md` — freeform Draft, structure required only before Approved; remove Note references
3. ✓ Process: Rename `AGENT/PROCESS/EXPERIMENT.md` → `AGENT/PROCESS/SPIKE.md`; update content (findings.md, goal evolution)
4. ✓ Process: Update `active.md` format in `AGENT/PROCESS/README.md` — add Type field
5. ✓ Impl: Update `setup.py` — prepend preamble line to CLAUDE.md/AGENTS.md before the `@`-include
6. ✓ Tests: Update `test.py` — verify preamble appears before `@`-include in written config files
7. ✓ Spec: Update `SPEC.md` — reflect new change types, active.md format, setup.py preamble behaviour
8. Process: Confirm ready to archive
