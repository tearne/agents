# Specification

## Overview
Reusable agent configuration files for Claude Code, distributed as a git repo. Cloning the repo into `~/.claude/` and running the setup script makes the configurations available globally across all projects, while keeping them version-controlled and easy to update.

## Usage
```sh
git clone https://github.com/tearne/agents ~/.claude/agents
cd ~/.claude/agents && ./setup.py
```

The repo may be cloned into any subdirectory name under `~/.claude/`. After setup, Claude Code will load the configurations automatically in every project.

## Behaviour
- `setup.py` determines its own location relative to `~/.claude/`
- If `~/.claude/CLAUDE.md` already exists, it is backed up with a timestamped filename before being overwritten
- `setup.py` writes `~/.claude/CLAUDE.md` containing `@`-references to `DEFINITIONS.md` and `POS.md`, resolved relative to `~/.claude/`
- Claude Code loads `~/.claude/CLAUDE.md` globally, making the definitions available in all projects without per-project configuration

## Constraints
- The repo must be cloned somewhere under `~/.claude/`; `setup.py` will exit with an error if this is not the case
- `setup.py` must be run via `uv` (i.e. `./setup.py`), not directly with `python`
- Requires Python 3.12

## Verification
- After running `setup.py`, `~/.claude/CLAUDE.md` exists and contains `@`-references pointing to `DEFINITIONS.md` and `POS.md` at the correct relative paths
- A Claude Code session started in any directory has the definitions from `DEFINITIONS.md` and `POS.md` in its context
