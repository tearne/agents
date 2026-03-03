# Design: OpenCode Support
**Status: Ready for Review**

## Approach
The setup.py script will be enhanced to:
1. Detect if Claude Code is installed (check for `~/.claude/` directory or `claude` CLI)
2. Detect if OpenCode is installed (check for `~/.config/opencode/` directory or `opencode` CLI)
3. For each installed tool, configure it to reference PROCESS.md and POS.md
4. If a tool is not installed, log a warning and skip configuration for that tool

OpenCode configuration approach:
- Write `~/.config/opencode/opencode.json` with an `instructions` array pointing to PROCESS.md and POS.md using absolute paths
- OpenCode's `instructions` config is the equivalent of Claude Code's `@`-references in CLAUDE.md

## Tasks
1. Update `setup.py` to detect Claude Code installation status
2. Update `setup.py` to detect OpenCode installation status
3. Add OpenCode configuration logic (write opencode.json with instructions)
4. Add graceful warning messages for missing installations
5. Update SPEC.md to document both Claude Code and OpenCode support
6. Test the implementation by running setup.py in a clean environment
7. Confirm implementation complete and ready to archive
