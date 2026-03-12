# Design: Integrate Rust Style Guide
**Status: Approved**

## Approach

Update `setup.py` to `@`-include `STYLE-RUST.md` in both generated config files, with a comment indicating it is only relevant for Rust projects. Also add a comment before the `POS.md` reference indicating it is only relevant for Python projects. Update `test.py` and `SPEC.md`.

## Tasks

1. ✓ **Impl**: Update `setup.py` to include `@`-reference to `STYLE-RUST.md` with a language annotation comment; add equivalent comment before `POS.md`
2. ✓ **Tests**: Update `test.py` to verify `STYLE-RUST.md` is referenced in generated config files
3. ✓ **Verify**: Run `./test.py`
4. ✓ **Spec**: Update `SPEC.md`
5. ✓ **Process**: Confirm ready to archive
