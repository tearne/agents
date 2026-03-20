# Design: Restructure for Conciseness and Selective Loading
**Status: Approved**

## Approach
Reorganise root-level files into always-loaded (root) and opt-in (`ADDITIONAL/`). Refactor `STYLE.md` into a terse rules file with a companion `STYLE-elaboration.md`. Update `setup.py` to reflect the new always-loaded set. The agent learns about `ADDITIONAL/` via a new section in `PROCESS/README.md`.

Always-loaded after this change: `BEHAVIOUR.md`, `STYLE.md`, `STYLE-RUST.md`, `PROCESS/README.md`.

## Tasks
1. ✓ Tests: Update `test.py` — remove stale assertions (`PROCESS_FORMAL.md`, `PROCESS_LITE.md`, `"Process Selection"`); update content assertions to reflect new always-loaded set (remove `VERSIONING.md`, `POS.md`); verify tests fail before impl
2. ✓ Impl: Create `ADDITIONAL/` directory; move `VERSIONING.md` and `POS.md` into it; create `ADDITIONAL/README.md`
3. ✓ Impl: Refactor `STYLE.md` to terse rules-only version; create `STYLE-elaboration.md` as companion
4. ✓ Impl: Add conditional applicability note to top of `STYLE-RUST.md`
5. ✓ Impl: Add `Additional Guides` section to `PROCESS/README.md` — describes the `ADDITIONAL/` pool, passive/prompted distinction, and the `*-elaboration.md` convention
6. ✓ Impl: Update `setup.py` — remove `VERSIONING.md` and `POS.md` from always-loaded content
7. ✓ Verify: Run `./test.py` and confirm all passing
8. ✓ Impl: Update `SPEC.md`
9. ✓ Tests: Update `test.py` path assertions for `AGENT/` prefix
10. ✓ Impl: Create `AGENT/`; move `BEHAVIOUR.md`, `STYLE.md`, `STYLE-RUST.md`, `STYLE-elaboration.md`, `ADDITIONAL/`, `PROCESS/` into it
11. ✓ Impl: Update `setup.py` to reference new paths under `AGENT/`
12. ✓ Impl: Update `SPEC.md` to reference new paths
13. ✓ Verify: Run `./test.py` and confirm all passing
14. ✓ Process: Confirm ready to archive
