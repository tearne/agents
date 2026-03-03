# Design: Add Tests
**Status: Ready for Review**

## Approach
Create a pytest-based test file that:
1. Patches `pathlib.Path.home()` to return a temporary directory
2. Creates mock installation directories (`.claude/` and `.config/opencode/`) within the temp directory
3. Tests each function in setup.py in isolation:
   - `is_claude_installed()` returns True when `.claude/` exists
   - `is_opencode_installed()` returns True when `.config/opencode/` exists
   - `setup_claude()` writes correct content to CLAUDE.md
   - `setup_opencode()` writes correct JSON config with instructions array
   - Graceful warning when neither tool is installed

## Tasks
1. Create `test_setup.py` with pytest and temp directory fixtures
2. Add tests for Claude Code detection
3. Add tests for OpenCode detection
4. Add tests for Claude Code config generation
5. Add tests for OpenCode config generation
6. Add test for graceful handling when neither tool installed
7. Run tests and verify all pass
8. Confirm implementation complete and ready to archive
