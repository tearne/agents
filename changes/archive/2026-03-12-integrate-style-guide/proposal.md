# Proposal: Integrate Style Guide
**Status: Approved**

## Intent
`STYLE.md` is a coding style guide covering five principles of readable code. It is well-suited as an agent instruction and should be loaded globally alongside the other configuration files.

## Specification Deltas

### ADDED
- `STYLE.md` is loaded globally by `setup.py` alongside `BEHAVIOUR.md`, `PROCESS.md`, and `POS.md`

### MODIFIED
- `STYLE.md`: the Python code example in Principle 1 is replaced with language-agnostic pseudocode, since its purpose is only to illustrate calling well-named functions
- `setup.py`: includes `@`-reference to `STYLE.md` in generated config files
- `SPEC.md`: updated to reflect `STYLE.md` as a configuration file

## Scope
- **Out of scope**: changes to the principles themselves or their wording
- `STYLE.md` and `POS.md` do not overlap: POS is Python-only and covers file-level layout for a specific script format; `STYLE.md` covers function-level design for any language.
