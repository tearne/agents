# Design: Semver Guidance
**Status: Approved**

## Approach

A new `VERSIONING.md` is added to the repo and referenced globally in `setup.py`. It covers semver principles and the expectation that all projects carry a version.

`PROCESS_FORMAL.md` and `PROCESS_LITE.md` are updated at their final pre-archival review points. The agent announces a new version number (e.g. "v1.2.3") alongside the review invitation, making the transition from implementation to final review unambiguous. Post-review corrections each warrant a patch bump.

`POS.md` gains a note that scripts should carry a version constant and expose it via `--version`.

`setup.py` adds `@{repo_dir}/VERSIONING.md` to the global config written for both tools.

## Tasks
1. ✓ Impl: Create `VERSIONING.md`
2. ✓ Impl: Update `PROCESS_FORMAL.md` — announce version at final review stage
3. ✓ Impl: Update `PROCESS_LITE.md` — same
4. ✓ Impl: Update `POS.md` — add `--version` guidance
5. ✓ Impl: Update `setup.py` — add `VERSIONING.md` reference to global configs
6. ✓ Spec: Update `SPEC.md`
7. ✓ Process: Confirm ready to archive
