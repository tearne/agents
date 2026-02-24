# Specification

## Overview
Reusable agent configuration files for Claude Code, distributed as a git repo. Cloning the repo into `~/.claude/` and running the setup script makes the configurations available globally across all projects, while keeping them version-controlled and easy to update.

## Usage
```sh
git clone https://github.com/tearne/agents ~/path/to/agents
cd ~/path/to/agents && ./setup.py
```

The repo may be cloned anywhere. After setup, Claude Code will load the configurations automatically in every project.

## Behaviour
- `setup.py` determines its own absolute location
- If `~/.claude/CLAUDE.md` already exists, it is backed up with a timestamped filename before being overwritten
- `setup.py` writes `~/.claude/CLAUDE.md` containing `@`-references to `PROCESS.md` and `POS.md` using absolute paths to the repo
- Claude Code loads `~/.claude/CLAUDE.md` globally, making the definitions available in all projects without per-project configuration

## Constraints
- `setup.py` must be run via `uv` (i.e. `./setup.py`), not directly with `python`
- Requires Python 3.12

## Verification
- After running `setup.py`, `~/.claude/CLAUDE.md` exists and contains `@`-references pointing to `PROCESS.md` and `POS.md` at the correct absolute paths
- A Claude Code session started in any directory has the definitions from `PROCESS.md` and `POS.md` in its context
