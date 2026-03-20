# Proposal: Restructure for Conciseness and Selective Loading
**Status: Approved**

## Intent
As the repo grows, always-loading everything becomes expensive in context and unwieldy for humans. The current structure makes no distinction between what is always relevant and what is context-dependent. This proposal reorganises around that distinction, making the always-loaded surface minimal and stable, and providing a well-indexed pool of additional guides that are loaded when relevant.

## Specification Deltas

### ADDED
- `ADDITIONAL/` directory — guides that are beyond the always-loaded core; named by the user in a spec or proposal when relevant, or raised by the agent when context warrants
- `ADDITIONAL/README.md` — single-sentence entry point stating what it is there to answer; one-line description per guide sufficient to make the opt-in decision without reading the guide
- `STYLE-elaboration.md` — companion to `STYLE.md` containing examples and references under matching numbered headings; follows the `*-elaboration.md` naming convention (agent need not load unless additional context is judged necessary)
- Passive/prompted distinction within `ADDITIONAL/`: **passive** guides are named by the user; **prompted** guides are raised by the agent when context warrants (e.g. `VERSIONING.md` when a project is being set up, changes are accumulating, or a breaking change is being made)
- Note in the root-level README that `STYLE-RUST.md` applies to Rust projects — the agent infers this from project context without the user naming it explicitly

### MODIFIED
- `STYLE.md` — refactored to terse, agent-optimised rules only (matching the `STYLE-agent.md` produced in the `style-guide-split` experiment)
- `setup.py` — updated to reflect the new always-loaded file set: `BEHAVIOUR.md`, `STYLE.md`, `STYLE-RUST.md`, `PROCESS/README.md`
- `SPEC.md` — updated to reflect new structure

### REMOVED
- `VERSIONING.md` from root (moved to `ADDITIONAL/`)
- `POS.md` from root (moved to `ADDITIONAL/`)
- Always-loading of `VERSIONING.md` and `POS.md`

## Scope
- **In scope**: restructuring files, splitting `STYLE.md`, creating `ADDITIONAL/` with README, consolidating all agent config under `AGENT/`, updating `setup.py` and `SPEC.md`
- **Out of scope**: splitting `STYLE-RUST.md` into a terse + elaboration pair (can follow later using the same pattern); changes to `PROCESS/`
