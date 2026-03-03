# Design: Test Execution Improvements
**Status: Draft**

## Approach

### 1. Test Execution Problem
When a Python script with inline pytest dependencies is run directly (`./test_file.py`), it executes `pytest.main()` in its `__main__` guard. However, when pytest collects the same file externally (`pytest test_file.py`), it imports the module and the `__main__` guard is not executed. 

The issue arises when pytest is already running and the script is executed directly (e.g., via subprocess), which can cause nested pytest execution and confusing output.

### 2. Solution: Nesting Detection
Add a check in the `__main__` guard to detect if pytest is already running before invoking `pytest.main()`:

```python
if __name__ == "__main__":
    if "pytest" not in sys.modules or "pytest.pytest_source" not in dir():
        sys.exit(pytest.main([__file__, "-v"]))
```

**Technical rationale:**
- `"pytest" not in sys.modules` checks if pytest is imported at all
- `"pytest.pytest_source" not in dir()` checks if pytest's internal source tracking is active
- This combination reliably detects when pytest is already running vs when the script is being executed standalone

### 3. Documentation Pattern
Add a "Testing" section to POS.md showing the complete pattern for self-executing test files with inline dependencies, including:
- Script header with pytest dependency
- Example test structure
- Main guard with nesting detection
- Execution options (direct vs external pytest)

## Tasks
1. ✅ Impl: Update test_setup.py main guard with pytest nesting check
2. ✅ Impl: Add testing section to POS.md with guidance and example
3. ✅ Verify: Ensure tests pass via both `./test_setup.py` and external pytest
4. ✅ Process: Ready for review and archive