# Design: Process Consolidation
**Status: Draft**

## Approach

Create a `PROCESS/` directory containing four files distilled from the two existing process files:
- `README.md` — shared elements: SPEC conventions, Note guidance and mode selection, proposal template, archive rules
- `FORMAL.md` — implement phase only: per-task signoff, TDD note, version announcement
- `LITE.md` — implement phase only: free implementation, single review, version announcement
- `EXPERIMENT.md` — experimenting form (extracted from both process files)

Update `setup.py` to reference `PROCESS/README.md` instead of the old files in both the Claude Code and OpenCode content strings. Update this project's `CLAUDE.md` to match. Delete the old `PROCESS_FORMAL.md` and `PROCESS_LITE.md`. Update `SPEC.md` to reflect the new structure.

## Tasks

1. ✓ Impl: Create `PROCESS/README.md` — shared elements, Note guidance, mode selection prompt, and `active.md` guidance (agent checks `changes/open/active.md` at session start; creates/updates it when a proposal or experiment becomes active; warns if a new one is started while one is already recorded; removes it on archive)
2. ✓ Impl: Create `PROCESS/FORMAL.md` — Implement phase detail from `PROCESS_FORMAL.md`
3. ✓ Impl: Create `PROCESS/LITE.md` — Implement phase detail from `PROCESS_LITE.md`
4. ✓ Impl: Create `PROCESS/EXPERIMENT.md` — Experimenting section extracted from either process file
5. ✓ Impl: Update `setup.py` — replace process file references in both Claude Code and OpenCode content
6. ✓ Impl: Update this project's `CLAUDE.md` — reference `PROCESS/README.md`
7. ✓ Impl: Delete `PROCESS_FORMAL.md` and `PROCESS_LITE.md`
8. ✓ Impl: Update `SPEC.md` — Configuration Files, Behaviour, and Verification sections
9. ✓ Impl: Slim `PROCESS/README.md` to entry point only; structure as: SPEC conventions → overview of change types (Notes, Formal, Lite, Experiment) → Active Change Tracking → mode selection; move proposal template and archive rules into `PROCESS/FORMAL.md` and `PROCESS/LITE.md` so each is self-contained; update Notes to use `note.md`, exempt from active tracking, retained on graduation; remove `Status: Note` from proposal template; rename proposal files to `proposal_formal.md` / `proposal_lite.md` in templates and guidance
10. ✓ Impl: Remove `---` horizontal rules from all `PROCESS/` markdown files (already absent after Task 9 rewrite)
11. ✓ Process: confirm ready to archive
