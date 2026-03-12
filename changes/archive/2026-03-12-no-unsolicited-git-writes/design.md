# Design: No Unsolicited Git Writes
**Status: Approved**

## Approach

Create `BEHAVIOUR.md` in this repo with the git write rule. Update `setup.py` to include it in the generated global config files. Update `SPEC.md` to reflect the new file and its role.

## Tasks

1. ✓ **Impl**: Create `BEHAVIOUR.md`
2. ✓ **Impl**: Update `setup.py` to `@`-include `BEHAVIOUR.md` in `~/.claude/CLAUDE.md` and `~/.config/opencode/AGENTS.md`
3. ✓ **Tests**: Update `test.py` to verify `BEHAVIOUR.md` is referenced in generated config files
4. ✓ **Verify**: Run `./test.py`
5. ✓ **Spec**: Update `SPEC.md`
6. ✓ **Process**: Confirm ready to archive
