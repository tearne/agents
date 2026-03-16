# Design: Process Per Project
**Status: Approved**

## Approach

`PROCESS.md` is renamed to `PROCESS_FORMAL.md`. A new `PROCESS_LITE.md` is added alongside it. Both remain in this repo for version control.

`setup.py` is updated to write a revised `~/.claude/CLAUDE.md` (and OpenCode equivalent) that:
- drops the `@`-reference to `PROCESS.md`
- adds a startup instruction directing the agent to check for a process selection in the project's local config file (`CLAUDE.md` for Claude Code; `AGENTS.md` for OpenCode) and prompt if absent

The agents repo itself gets a local `CLAUDE.md` (gitignored) pointing to `PROCESS_FORMAL.md`, so this repo continues to use the formal process after the global reference is removed.

`SPEC.md` is updated to reflect all of the above.

## Tasks

1. ✓ **Impl**: Rename `PROCESS.md` → `PROCESS_FORMAL.md`
2. ✓ **Impl**: Create `PROCESS_LITE.md`
3. ✓ **Impl**: Update `setup.py` to write the new `~/.claude/CLAUDE.md` and OpenCode equivalent (drop `PROCESS.md` reference; add startup check instruction)
4. ✓ **Impl**: Add `CLAUDE.md` and `AGENTS.md` to `.gitignore` in this repo; create local `CLAUDE.md` pointing to `PROCESS_FORMAL.md`
5. ✓ **Tests**: Update `test.py` to reflect the new `~/.claude/CLAUDE.md` content
6. ✓ **Verify**: Run `./test.py`
7. ✓ **Spec**: Update `SPEC.md`
8. **Process**: Confirm ready to archive
