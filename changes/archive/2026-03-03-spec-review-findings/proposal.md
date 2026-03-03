# Proposal: Spec Review Findings
**Status: Note**

## Intent
Document inconsistencies found between SPEC.md, README.md, and implementation (setup.py) to determine appropriate resolution.

## Resolved

### 1. Symlink vs File Content Behavior
- **Decision**: README is outdated. Formerly used symlinks but didn't work, replaced with file content containing `@`-references to PROCESS.md and POS.md at absolute paths.
- **Action**: Update README to describe current behavior for both Claude Code and OpenCode.

### 2. Test Verification Command
- **Finding**: SPEC.md:40 says `uv run --with pytest python test_setup.py` but test file uses `uv run --script` with inline dependencies, so `./test_setup.py` works directly.
- **Action**: Update SPEC.md verification to `./test_setup.py`

All findings resolved. Actions:

1. **README.md**: Update to describe file-content behavior (not symlinks) for both Claude Code and OpenCode
2. **setup.py**: Remove symlink handling code:
   - Lines 55, 84: Remove `and not *.is_symlink()` checks
   - Line 104: Remove `or path.is_symlink()` from backup check
3. **SPEC.md**: Update test verification command from `uv run --with pytest python test_setup.py` to `./test_setup.py`
4. **test_setup.py**: Remove relic test `test_setup_opencode_does_not_create_json` (tests behavior not in spec)
