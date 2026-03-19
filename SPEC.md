# Specification

## Overview
Reusable agent configuration files for Claude Code and OpenCode, distributed as a git repo. Cloning the repo and running the setup script makes the configurations available globally across all projects, while keeping them version-controlled and easy to update.

## Usage
```sh
git clone https://github.com/tearne/agents ~/path/to/agents
cd ~/path/to/agents && ./setup.py
```

The repo may be cloned anywhere. After setup, both Claude Code and OpenCode will load the configurations automatically in every project.

## Configuration Files
- `BEHAVIOUR.md` — general agent behaviour rules (e.g. no unsolicited git writes)
- `VERSIONING.md` — semantic versioning guidance; loaded globally
- `PROCESS/README.md` — always-loaded process entry point: SPEC conventions, change types (Note, Proposal, Experiment), active change tracking, and how to start a change
- `PROCESS/PROPOSAL.md` — four-phase change management process (propose → design → implement → archive); review cadence agreed at the start of implementation
- `PROCESS/EXPERIMENT.md` — template for exploratory work outside the change process
- `STYLE.md` — language-agnostic coding style guide (readable abstraction layers)
- `POS.md` — Python Orchestrated Script style guide (Python projects only)
- `STYLE-RUST.md` — Rust-specific coding style addendum (Rust projects only)

## Behaviour
- `setup.py` determines its own absolute location
- Detects whether Claude Code is installed by checking for the `claude` CLI via `shutil.which("claude")`
- Detects whether OpenCode is installed by checking for the `opencode` CLI via `shutil.which("opencode")`
- If neither tool is detected, prints a warning and exits gracefully
- If only one tool is installed, configures that tool and warns about the missing one
- For Claude Code:
  - Creates `~/.claude/` directory if it doesn't exist
  - If `~/.claude/CLAUDE.md` already exists, it is backed up with a timestamped filename before being overwritten
  - Writes `~/.claude/CLAUDE.md` containing `@`-references to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, `STYLE-RUST.md`, and `PROCESS/README.md` using absolute paths
  - Claude Code loads `~/.claude/CLAUDE.md` globally
- For OpenCode:
  - Creates `~/.config/opencode/` if it doesn't exist
  - If `~/.config/opencode/AGENTS.md` already exists, it is backed up with a timestamped filename before being overwritten
  - Writes `~/.config/opencode/AGENTS.md` containing `@`-references to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, `STYLE-RUST.md`, and `PROCESS/README.md` using absolute paths
  - OpenCode loads `~/.config/opencode/AGENTS.md` globally (takes precedence over CLAUDE.md)
- `PROCESS/README.md` is always loaded globally; it instructs the agent on change types and active change tracking
- The agent also ensures the local config file is listed in the project's `.gitignore`, since it is personal/local configuration
- `CLAUDE.md` and `AGENTS.md` are listed in this repo's `.gitignore`

## Constraints
- `setup.py` must be run via `uv` (i.e. `./setup.py`), not directly with `python`
- Requires Python 3.12

## Verification
- After running `setup.py`, Claude Code has `~/.claude/CLAUDE.md` containing `@`-references pointing to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, `STYLE-RUST.md`, and `PROCESS/README.md` at the correct absolute paths (if Claude Code is installed)
- After running `setup.py`, OpenCode has `~/.config/opencode/AGENTS.md` containing `@`-references pointing to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, `STYLE-RUST.md`, and `PROCESS/README.md` at the correct absolute paths (if OpenCode is installed)
- A Claude Code session started in any directory has the definitions from `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, `STYLE-RUST.md`, and `PROCESS/README.md` in its context
- An OpenCode session started in any directory has the definitions from `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, `STYLE-RUST.md`, and `PROCESS/README.md` in its context
- Automated tests exist in `test.py` and can be run via `./test.py`. Tests use temporary directories to mock the user home directory (`$HOME`) by patching `pathlib.Path.home()` for isolation.
