# Design: Integrate Style Guide
**Status: Approved**

## Approach

Update `STYLE.md` to replace the Python example with pseudocode. Update `setup.py` to `@`-include `STYLE.md` in both generated config files. Add tests. Update `SPEC.md`.

## Tasks

1. ✓ **Impl**: Replace Python example in `STYLE.md` Principle 1 with pseudocode
2. ✓ **Impl**: Update `setup.py` to include `@`-reference to `STYLE.md`
3. ✓ **Tests**: Update `test.py` to verify `STYLE.md` is referenced in generated config files
4. ✓ **Verify**: Run `./test.py`
5. ✓ **Spec**: Update `SPEC.md`
6. ✓ **Process**: Confirm ready to archive
