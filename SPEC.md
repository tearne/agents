# Specification

## Overview
Reusable agent configuration files for Claude Code and OpenCode, distributed as a git repo. Cloning the repo and running the setup script makes the configurations available globally across all projects, while keeping them version-controlled and easy to update.

## Usage
```sh
git clone https://github.com/tearne/agents ~/path/to/agents
cd ~/path/to/agents && ./setup.py
```

The repo may be cloned anywhere. After setup, both Claude Code and OpenCode will load the configurations automatically in every project.

## Behaviour
- `setup.py` determines its own absolute location
- Detects whether Claude Code is installed by checking for `~/.claude/`
- Detects whether OpenCode is installed by checking for `~/.config/opencode/`
- If neither tool is detected, prints a warning and exits gracefully
- If only one tool is installed, configures that tool and warns about the missing one
- For Claude Code:
  - If `~/.claude/CLAUDE.md` already exists, it is backed up with a timestamped filename before being overwritten
  - Writes `~/.claude/CLAUDE.md` containing `@`-references to `PROCESS.md` and `POS.md` using absolute paths
  - Claude Code loads `~/.claude/CLAUDE.md` globally
- For OpenCode:
  - Creates `~/.config/opencode/` if it doesn't exist
  - Writes `~/.config/opencode/opencode.json` with an `instructions` array pointing to `PROCESS.md` and `POS.md` using absolute paths
  - Preserves existing config keys when updating
  - OpenCode loads instructions from `opencode.json` globally

## Constraints
- `setup.py` must be run via `uv` (i.e. `./setup.py`), not directly with `python`
- Requires Python 3.12

## Verification
- After running `setup.py`, Claude Code has `~/.claude/CLAUDE.md` containing `@`-references pointing to `PROCESS.md` and `POS.md` at the correct absolute paths (if Claude Code is installed)
- After running `setup.py`, OpenCode has `~/.config/opencode/opencode.json` containing an `instructions` array pointing to `PROCESS.md` and `POS.md` at the correct absolute paths (if OpenCode is installed)
- A Claude Code session started in any directory has the definitions from `PROCESS.md` and `POS.md` in its context
- An OpenCode session started in any directory has the definitions from `PROCESS.md` and `POS.md` in its context
