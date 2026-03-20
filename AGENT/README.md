# Agent Configuration
This is the single entry point for all agent configuration. It loads the always-loaded files and introduces the two key project-level concepts: specifications and changes.

@BEHAVIOUR.md
@STYLE.md
@STYLE-RUST.md
@PROCESS/README.md

## Specifications

Project specifications live in `SPEC.md` files (or a `SPEC/` directory when a single file would be too large):
- The **root** `SPEC.md` covers the project as a whole (structure, shared requirements, integration testing)
- Directory `SPEC.md` files are scoped to components in that directory and below, inheriting project-wide requirements unless explicitly overridden

A specification will typically follow this structure:
```markdown
# Specification
## Overview
## Usage
## Behaviour
## Constraints
## Verification
```

## Changes

Work in progress and completed changes live in a `changes/` directory alongside the root `SPEC.md`:
- `changes/open/` — active notes, proposals, experiments, and the current `active.md`
- `changes/archive/` — completed and abandoned changes, named `YYYY-MM-DD-<change-name>/`
