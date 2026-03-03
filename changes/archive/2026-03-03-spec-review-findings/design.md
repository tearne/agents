# Design: Spec Review Findings
**Status: Approved**

## Approach

### 1. README.md Update
Update README to describe file-content behavior for both Claude Code and OpenCode, replacing the outdated symlink mention.

### 2. setup.py Symlink Code Removal
Remove dead symlink handling code from setup.py:
- Lines 55, 84: Remove `and not *.is_symlink()` checks that prevented writing to symlinks
- Line 104: Remove `or path.is_symlink()` from backup check

### 3. SPEC.md Verification Command Update
Update test verification command from `uv run --with pytest python test_setup.py` to `./test_setup.py` to match the actual execution pattern.

### 4. test_setup.py Cleanup
Remove relic test `test_setup_opencode_does_not_create_json` that tests behavior not in spec.

## Tasks
1. ✅ Impl: Update README.md
2. ✅ Impl: Remove symlink handling from setup.py
3. ✅ Impl: Update SPEC.md test verification command
4. ✅ Impl: Remove JSON test relic from test_setup.py
5. ✅ Verify: Tests pass
6. ✅ Process: Design ready for review