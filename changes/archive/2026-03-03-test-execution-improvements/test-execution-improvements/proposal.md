# Proposal: Test Execution Improvements
**Status: Draft**

## Intent
Improve test execution pattern for POS-style scripts with inline pytest dependencies, avoiding nested pytest execution and documenting the pattern in POS.md.

## Scope
- **In scope**: test_setup.py main guard optimization, POS.md testing section
- **Out of scope**: Other test files, pytest configuration

## Specification Deltas

### ADDED
- Guidance in POS.md for self-executing test files with inline pytest dependencies
- Pattern to avoid nested pytest when tests are collected externally

### MODIFIED
- test_setup.py main guard to check if pytest is already running before invoking pytest.main()

## Unresolved
1. Should the pytest nesting check be documented as required or optional in POS.md?
2. Is the current check (`"pytest" not in sys.modules or "pytest.pytest_source" not in dir()`) robust enough?