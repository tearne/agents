# Proposal: Use AGENTS.md for OpenCode Global Rules
**Status: Ready for Review**

## Intent
Change OpenCode configuration to use `~/.config/opencode/AGENTS.md` instead of `~/.config/opencode/opencode.json` with `instructions` array. OpenCode's preferred approach for global rules is AGENTS.md, which takes precedence over Claude Code's CLAUDE.md.

## Scope
- **In scope**:
  - Update `setup.py` to create `~/.config/opencode/AGENTS.md` instead of `opencode.json`
  - AGENTS.md should contain `@`-references to PROCESS.md and POS.md (similar to how CLAUDE.md works)
  - Update tests to verify AGENTS.md creation
- **Out of scope**:
  - Removing Claude Code support (still uses CLAUDE.md)

## Delta

### MODIFIED
- `setup.py`: Write `~/.config/opencode/AGENTS.md` instead of `~/.config/opencode/opencode.json`
- `test_setup.py`: Update tests for AGENTS.md
- `SPEC.md`: Update to reflect AGENTS.md approach for OpenCode
