# Proposal: Fix Missing Directory Bug
**Status: Ready for Review**

## Intent
Fix the detection logic to check for the CLI tools instead of config file existence. The previous approach crashed when directories didn't exist. The new approach checks for the CLI binaries (`claude` and `opencode`), which properly identifies if each tool is installed, and creates directories as needed.

## Scope
- **In scope**:
  - Check for `claude` CLI via `shutil.which("claude")`
  - Check for `opencode` CLI via `shutil.which("opencode")`
  - If CLI is present, create config directories and files
  - If CLI is absent, skip with warning
  - Update tests to verify CLI-based detection
- **Out of scope**: Any other changes

## Delta

### MODIFIED
- `setup.py`: Use CLI detection (`shutil.which`) instead of config-directory existence
- `test_setup.py`: Update tests for CLI-based detection
- `SPEC.md`: Update detection method from directory existence to CLI detection
