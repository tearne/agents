# Design: Use AGENTS.md for OpenCode Global Rules
**Status: Ready for Review**

## Approach
Update `setup_opencode()` to:
1. Create `~/.config/opencode/` directory if needed
2. Write `~/.config/opencode/AGENTS.md` with `@`-references to PROCESS.md and POS.md (same format as CLAUDE.md)
3. Remove opencode.json handling entirely

## Tasks
1. Update `setup_opencode()` to write AGENTS.md instead of opencode.json
2. Add test for AGENTS.md creation
3. Run tests and verify all pass
4. Confirm implementation complete and ready to archive
