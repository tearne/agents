# Proposal: Add Tests
**Status: Ready for Review**

## Intent
Add automated tests to verify that `setup.py` correctly configures Claude Code and OpenCode. Currently the verification section in SPEC.md has no test coverage.

## Scope
- **In scope**:
  - Create test file that verifies setup.py detection logic
  - Create test file that verifies config file generation
  - Use temporary directories to mock the user home directory (`$HOME`)
  - Patch `pathlib.Path.home()` to return temp directories for isolation
- **Out of scope**:
  - Integration tests that require actual CLI tools installed
  - Test setup.py execution itself (that would require uv)

## Delta

### ADDED
- Test file for setup.py behavior verification
- Update SPEC.md to reference test existence
