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

All agent configuration lives under `AGENT/`. `AGENT/README.md` is the single always-loaded entry point; it fans out via `@`-includes to the always-loaded files and introduces project-level concepts (specs, changes directory).

There are two layers of instruction:
- **Preamble** — written to `CLAUDE.md`/`AGENTS.md` by `setup.py`, before the `@`-include. Reserved for preconditions that must be established before any other context loads (e.g. the active change constraint). Intentionally terse.
- **Always-loaded files** — version-controlled rules loaded via the `@`-include chain. Cover behaviour, style, and process in full detail.

Always loaded (via `AGENT/README.md`):
- `AGENT/BEHAVIOUR.md` — general agent behaviour rules (e.g. no unsolicited git writes)
- `AGENT/STYLE.md` — language-agnostic coding style (terse rules); see `AGENT/ADDITIONAL/STYLE-elaboration.md` for examples and references
- `AGENT/STYLE-RUST.md` — Rust-specific coding style addendum; applies to Rust projects only
- `AGENT/PROCESS/README.md` — change management entry point: change types (Fix, Proposal, Spike), active change tracking, archival expectations (including explicit archival gate), additional guides, and how to start a change
- `AGENT/PROCESS/PROPOSAL.md` — four-phase change management process (propose → design → implement → archive); `change.md` is the single proposal document; review cadence agreed at the start of implementation
- `AGENT/PROCESS/SPIKE.md` — process for iterative exploration; `change.md` is the single spike document; `findings.md` added on adoption

Additional (opt-in or prompted — see `AGENT/ADDITIONAL/README.md`):
- `AGENT/ADDITIONAL/VERSIONING.md` — semantic versioning conventions; prompted by the agent when relevant
- `AGENT/ADDITIONAL/POS.md` — Python Orchestrated Script style; named in spec or proposal when applicable

## Behaviour
- `setup.py` determines its own absolute location
- Detects whether Claude Code is installed by checking for the `claude` CLI via `shutil.which("claude")`
- Detects whether OpenCode is installed by checking for the `opencode` CLI via `shutil.which("opencode")`
- If neither tool is detected, prints a warning and exits gracefully
- If only one tool is installed, configures that tool and warns about the missing one
- For Claude Code:
  - Creates `~/.claude/` directory if it doesn't exist
  - If `~/.claude/CLAUDE.md` already exists, it is backed up with a timestamped filename before being overwritten
  - Writes `~/.claude/CLAUDE.md` containing a preamble line enforcing the active change constraint, followed by a single `@`-reference to `AGENT/README.md` using its absolute path
  - Claude Code loads `~/.claude/CLAUDE.md` globally
- For OpenCode:
  - Creates `~/.config/opencode/` if it doesn't exist
  - If `~/.config/opencode/AGENTS.md` already exists, it is backed up with a timestamped filename before being overwritten
  - Writes `~/.config/opencode/AGENTS.md` containing a preamble line enforcing the active change constraint, followed by a single `@`-reference to `AGENT/README.md` using its absolute path
  - OpenCode loads `~/.config/opencode/AGENTS.md` globally (takes precedence over CLAUDE.md)
- `AGENT/README.md` is always loaded globally as the single entry point; it fans out to all always-loaded files
- The agent also ensures the local config file is listed in the project's `.gitignore`, since it is personal/local configuration
- `CLAUDE.md` and `AGENTS.md` are listed in this repo's `.gitignore`

## Constraints
- `setup.py` must be run via `uv` (i.e. `./setup.py`), not directly with `python`
- Requires Python 3.12

## Verification
- After running `setup.py`, Claude Code has `~/.claude/CLAUDE.md` containing the active change preamble followed by a single `@`-reference to `AGENT/README.md` at the correct absolute path (if Claude Code is installed)
- After running `setup.py`, OpenCode has `~/.config/opencode/AGENTS.md` containing the active change preamble followed by a single `@`-reference to `AGENT/README.md` at the correct absolute path (if OpenCode is installed)
- The preamble appears before the `@`-reference in both files
- A Claude Code session started in any directory has the definitions from `AGENT/README.md` and all files it references in its context
- An OpenCode session started in any directory has the definitions from `AGENT/README.md` and all files it references in its context
- Automated tests exist in `test.py` and can be run via `./test.py`. Tests use temporary directories to mock the user home directory (`$HOME`) by patching `pathlib.Path.home()` for isolation.
