# Design: Fix Missing Directory Bug
**Status: Ready for Review**

## Approach
Replace config-directory existence checks with CLI-based detection using `shutil.which()`:
- `is_claude_installed()`: returns `bool(shutil.which("claude"))`
- `is_opencode_installed()`: returns `bool(shutil.which("opencode"))`

When CLI is detected:
- Create `~/.claude/` directory if needed before writing `CLAUDE.md`
- Create `~/.config/opencode/` directory if needed before writing `opencode.json`

## Tasks
1. Update `is_claude_installed()` to use `shutil.which("claude")`
2. Update `is_opencode_installed()` to use `shutil.which("opencode")`
3. Update `setup_claude()` to create `~/.claude/` directory if needed
4. Update `setup_opencode()` to create `~/.config/opencode/` directory if needed
5. Update tests to mock `shutil.which` instead of directory existence
6. Run tests and verify all pass
7. Confirm implementation complete and ready to archive
