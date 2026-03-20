# Proposal: Move SPEC Introduction to AGENT/README.md
**Status: Approved**

## Intent
The concept of SPEC is currently introduced in `PROCESS/README.md`, alongside change types and active change tracking. This is the wrong home — SPEC is a project-level concept (what a project is supposed to do), not a process concept (how changes are managed). A reader looking for spec guidance has to know to look inside the process directory, which isn't intuitive. `AGENT/README.md` is the natural entry point for project-level concepts and is the first place a reader would look.

## Specification Deltas

### MODIFIED
- `AGENT/README.md` — becomes the single always-loaded entry point; introduces SPEC and `changes/` as project-level concepts; uses `@`-includes to fan out to `BEHAVIOUR.md`, `STYLE.md`, `STYLE-RUST.md`, and `PROCESS/README.md`
- `AGENT/PROCESS/README.md` — Specifications section removed; scope tightened to change management only; opening sentence updated to reflect its focused purpose
- `setup.py` — simplified to write a single `@`-reference to `AGENT/README.md` per tool, rather than listing all always-loaded files individually
- `test.py` — updated to reflect new always-loaded structure
- `SPEC.md` — updated to reflect new loading model

## Scope
- **In scope**: moving the SPEC content; making `AGENT/README.md` the single entry point; simplifying `setup.py`
- **Out of scope**: changes to SPEC structure or conventions
