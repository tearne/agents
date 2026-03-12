# Proposal: Integrate Rust Style Guide
**Status: Approved**

## Intent
`STYLE-RUST.md` is a Rust-specific addendum to `STYLE.md`, covering visibility as an API boundary, domain error types, ownership semantics, and trait design. It should be loaded globally alongside the other configuration files.

## Specification Deltas

### ADDED
- `STYLE-RUST.md` is loaded globally by `setup.py` alongside the other configuration files

### MODIFIED
- `setup.py`: includes `@`-reference to `STYLE-RUST.md` in generated config files, preceded by a comment indicating it is only relevant for Rust projects; similarly annotates the existing `POS.md` reference as only relevant for Python projects
- `SPEC.md`: updated to reflect `STYLE-RUST.md` as a configuration file
