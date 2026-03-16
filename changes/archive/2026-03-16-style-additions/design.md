# Design: Style Additions
**Status: Approved**

## Approach

All changes are to `STYLE-RUST.md` in `/root/agents`. Three new sections are appended and one existing section (Principle 8) is updated. No code changes; no tests required.

The three new sections slot in as Principles 9, 10, and 11 (continuing the existing numbering). The summary table at the end of the file is updated to include all three.

Principle 8's `dyn Trait` guidance is tightened: the existing "When `dyn Trait` is appropriate" note is rewritten to frame monomorphization as the default and `dyn Trait` as an explicit opt-in, with the criterion being whether the variant set is open or closed.

## Tasks

1. ✓ Impl: Update Principle 8 — reframe `dyn Trait` as opt-in; rewrite the "When `dyn Trait` is appropriate" note
2. ✓ Impl: Add Principle 9 — Test support modules
3. ✓ Impl: Add Principle 10 — Serde config conventions
4. ✓ Impl: Add Principle 11 — Runtime-to-static dispatch
5. ✓ Impl: Update the summary table to include Principles 9–11
6. ✓ Process: confirm ready to archive
