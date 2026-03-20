# Design: Move SPEC Introduction to AGENT/README.md
**Status: Approved**

## Approach
`AGENT/README.md` becomes the single always-loaded entry point, using `@`-includes to fan out to the always-loaded files. SPEC and `changes/` are introduced there. `setup.py` is simplified to a single reference per tool. `PROCESS/README.md` loses its Specifications section.

## Tasks
1. ✓ Tests: Update `test.py` — check for single `@AGENT/README.md` reference in written config; verify tests fail before impl
2. ✓ Impl: Update `setup.py` — write single `@`-reference to `AGENT/README.md` per tool
3. ✓ Impl: Update `AGENT/README.md` — add `@`-includes for always-loaded files; add SPEC and `changes/` introduction
4. ✓ Impl: Update `AGENT/PROCESS/README.md` — remove Specifications section; tighten opening sentence
5. ✓ Verify: Run `./test.py` and confirm all passing
6. ✓ Impl: Update `SPEC.md`
7. ✓ Process: Confirm ready to archive
