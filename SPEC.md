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
- `PROCESS_FORMAL.md` — full four-phase change management process (propose → design → implement → archive)
- `PROCESS_LITE.md` — lightweight three-phase change management process (propose → design → archive, no per-task signoff)
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
  - Writes `~/.claude/CLAUDE.md` containing `@`-references to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, and `STYLE-RUST.md` using absolute paths, plus a standing instruction to check for a process file selection in the project's local `CLAUDE.md` at session start
  - Claude Code loads `~/.claude/CLAUDE.md` globally
- For OpenCode:
  - Creates `~/.config/opencode/` if it doesn't exist
  - If `~/.config/opencode/AGENTS.md` already exists, it is backed up with a timestamped filename before being overwritten
  - Writes `~/.config/opencode/AGENTS.md` containing `@`-references to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, and `STYLE-RUST.md` using absolute paths, plus a standing instruction to check for a process file selection in the project's local `AGENTS.md` at session start
  - OpenCode loads `~/.config/opencode/AGENTS.md` globally (takes precedence over CLAUDE.md)
- Process selection is per-project: a project selects its process by `@`-including either `PROCESS_FORMAL.md` or `PROCESS_LITE.md` in its local config file (`CLAUDE.md` for Claude Code; `AGENTS.md` for OpenCode)
- At session start, if no process file is referenced in the project's local config, the agent prompts the user to select one and offers to create or update the local config file
- The agent also ensures the local config file is listed in the project's `.gitignore`, since it is personal/local configuration
- `CLAUDE.md` and `AGENTS.md` are listed in this repo's `.gitignore`; a local `CLAUDE.md` selecting `PROCESS_FORMAL.md` is maintained here but not version-controlled

## Constraints
- `setup.py` must be run via `uv` (i.e. `./setup.py`), not directly with `python`
- Requires Python 3.12

## Verification
- After running `setup.py`, Claude Code has `~/.claude/CLAUDE.md` containing `@`-references pointing to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, and `STYLE-RUST.md` at the correct absolute paths, and a process selection instruction (if Claude Code is installed)
- After running `setup.py`, OpenCode has `~/.config/opencode/AGENTS.md` containing `@`-references pointing to `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, and `STYLE-RUST.md` at the correct absolute paths, and a process selection instruction (if OpenCode is installed)
- A Claude Code session started in any directory has the definitions from `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, and `STYLE-RUST.md` in its context, and prompts for process selection if no process file is configured for the project
- An OpenCode session started in any directory has the definitions from `BEHAVIOUR.md`, `VERSIONING.md`, `STYLE.md`, `POS.md`, and `STYLE-RUST.md` in its context, and prompts for process selection if no process file is configured for the project
- Automated tests exist in `test.py` and can be run via `./test.py`. Tests use temporary directories to mock the user home directory (`$HOME`) by patching `pathlib.Path.home()` for isolation.
