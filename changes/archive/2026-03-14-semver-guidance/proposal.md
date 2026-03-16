# Proposal: Semver Guidance
**Status: Approved**

## Intent
Projects should follow semantic versioning. The final pre-archival review can be hard to distinguish from a mid-implementation task review. Announcing a new version number at that point acts as a clear signal that implementation is complete and the software is ready for final review — not just a step within it. Each subsequent tweak or correction after that point typically warrants a patch increment.

## Specification Deltas

### ADDED
- A new `VERSIONING.md` file provides semver guidance; it is loaded globally (all projects should version their output)
- `PROCESS_FORMAL.md` and `PROCESS_LITE.md`: at the final pre-archival review stage, the agent announces a new version number (following semver principles) as a deliberate signal that implementation is complete and the software is ready for overall review — distinguishing it from a mid-implementation task review
- Each round of post-review corrections is treated as a patch bump

### MODIFIED
- `POS.md`: scripts should carry a version and expose it via a `--version` argument
- `setup.py`: add `@`-reference to `VERSIONING.md` in the global config written for both Claude Code and OpenCode
- `SPEC.md`: add `VERSIONING.md` to the list of configuration files
