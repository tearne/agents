# Agent Configuration
This is the single entry point for all agent configuration. Read the Rules and Change Process sections below before starting any work. Detailed guidance is in the `@`-included files.

## Rules

These gates require explicit user instruction before proceeding — when in doubt, ask:
- Git write operations (`git add`, `git commit`, `git push`, `git reset`, `git rm`, etc.)
- Any change management decision: starting, pausing, advancing, or archiving a change
- Approval — the agent never approves anything; only the user can; approval is only valid when the user says "approved", "yes", or "y" in response to an explicit approval prompt
- Archiving a change — implementation alone is never sufficient; explicit user instruction is always required
- Writing or editing any project file without first recording the current change in `changes/open/active.md`

The following are exempt from the active change requirement:
- Reading any project file
- Creating or editing files inside `changes/`

## Change Process

All changes begin in `changes/open/`. See `PROCESS.md` for full detail.

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
- `changes/open/` — open changes (single `.md` files or folders) and the current `active.md`
- `changes/archive/` — completed and abandoned changes, named `YYYY-MM-DD-<change-name>`

@STYLE.md
@STYLE-RUST.md
@PROCESS.md 
