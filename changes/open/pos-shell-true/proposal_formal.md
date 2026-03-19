# Proposal: POS — Prefer shell=True for subprocess commands
**Status: Draft**

## Intent
POS scripts are meant to bridge Python control flow with shell commands. A key goal is that commands should be easy to read, copy, and paste directly into a terminal. Passing a list to `subprocess.run` obscures this by hiding the command inside Python syntax. Using `shell=True` with a plain string keeps each command immediately recognisable and terminal-ready.

## Specification Deltas

### MODIFIED
- POS guidance on `subprocess` usage: explicitly state that `subprocess.run` calls should use `shell=True` with a string argument, not a list. List-style invocations require the reader to mentally reconstruct the shell command, defeating the copy-paste goal.

### ADDED
- Note that `FileNotFoundError` handling is unnecessary when using `shell=True` (the shell handles command resolution); error detection should use `returncode` or `check=True` instead.

## Scope
- **In scope**: updating the POS style guide (`POS.md`) to codify `shell=True` as the default
- **Out of scope**: retroactively updating existing scripts
