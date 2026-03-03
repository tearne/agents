# Proposal: OpenCode Support
**Status: Ready for Review**

## Intent
Augment this project to work optimally with OpenCode, in addition to Claude Code. OpenCode is the user's preferred AI coding agent, and the project should provide global configurations for OpenCode alongside the existing Claude Code support.

## Scope
- **In scope**:
  - Update `setup.py` to configure OpenCode global config (`~/.config/opencode/opencode.json`)
  - Create OpenCode-specific instructions that can be referenced from the global config
  - Ensure both Claude Code and OpenCode can use the project's PROCESS.md and POS.md files
  - Graceful handling: if Claude Code or OpenCode are not installed, skip configuration for that tool and warn the user (don't crash)
- **Out of scope**:
  - OpenCode agent/command/skill definitions (deferred to future changes)
  - Project-specific OpenCode configuration (handled per-project with AGENTS.md)

## Delta

### MODIFIED
- `SPEC.md`: Expand to cover OpenCode support in addition to Claude Code
- `setup.py`: Add graceful handling for missing Claude Code and OpenCode installations

### ADDED
- OpenCode global configuration in `setup.py`
- OpenCode-specific instructions file (if needed for agent-specific guidance)
