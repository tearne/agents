# Proposal: POS Spec Refinements
**Status: Ready for Review**

## Intent
Two patterns identified during a code quality review of a POS script generalise
beyond that script and are worth adding to the POS spec.

## Scope
- **In scope**: two new guidance bullets added to `POS.md`
- **Out of scope**: changes to any existing bullets; changes to any POS scripts

## Delta

### ADDED
- **Prefer `Path.open()` over `open()`** — when a `Path` object is already in
  hand, prefer `path.open(mode)` over `open(path, mode)` to keep pathlib usage
  consistent and avoid mixing idioms within the same file.

- **Use `atexit` for resource cleanup** — when a script holds a long-lived
  resource (e.g. a log file opened at startup), register cleanup with `atexit`
  so the resource is released on normal exit and on `sys.exit()`. (Note: `atexit`
  handlers do not run on `os._exit()` or unhandled signals such as `SIGKILL`.)
