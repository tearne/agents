# Design: POS — Prefer shell=True for subprocess commands
**Status: Approved**

## Approach
Two edits to `POS.md`:
1. Add `shell=True` explicitly to the guidance bullet and its examples (the existing examples omit it, which is actually a bug — without `shell=True`, passing a string with pipes or env vars to `subprocess.run` will fail)
2. Add a note that `FileNotFoundError` handling is unnecessary with `shell=True`

No changes to the sudo section — it already uses `shell=True` correctly throughout.

## Tasks
1. ✓ Impl: Update `POS.md` — add `shell=True` to guidance and examples; add `FileNotFoundError` note
2. ✓ Process: Confirm ready to archive
