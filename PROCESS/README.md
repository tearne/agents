# Process

This directory contains the change management process for use with Claude Code and OpenCode. It is always loaded via the global config file (`~/.claude/CLAUDE.md` or `~/.config/opencode/AGENTS.md`).

## Specifications

Project specifications are contained in `SPEC.md` files (or a `SPEC/` directory when a single file would be too large):
- The **root** `SPEC.md` covers the project as a whole (structure, shared requirements, integration testing).
- During spec changes, relevant assets such as proposals are stored in subfolders of the `changes` directory, placed alongside the relevant `SPEC.md`.
- Directory `SPEC.md` files are scoped to components in that directory and below, inheriting project-wide non-functional requirements unless explicitly overridden.

A specification will typically follow a structure such as:
```markdown
# Specification
## Overview
## Usage
## Behaviour
## Constraints
## Verification
```

## Types of Change

**Note** — A `note.md` in `changes/open/<name>/`. Freeform, no required structure. Notes do not touch code and are exempt from active change tracking. To progress a Note, the user selects a type (Proposal or Experiment); the `note.md` is retained alongside the new `proposal.md` or `experiment.md` as a record of the original capture.

**Proposal** — A four-phase process: Propose, Design, Implement, Archive. Review cadence during implementation (per-task or end review) is agreed with the user at the start of that phase. See `PROCESS/PROPOSAL.md`.

**Experiment** — Exploratory work outside the change process. May or may not lead to a spec change. See `PROCESS/EXPERIMENT.md`.

## Active Change Tracking

A file `changes/open/active.md` records the current active change — one that is modifying project assets. The agent must:
- Check for `changes/open/active.md` at the start of each session and remind the user of the active change if one is recorded.
- Create or update `active.md` when a change begins touching code.
- Warn the user if a second change is about to begin *implementation* while one is already recorded in `active.md`.
- Remove `active.md` when the active change is archived.

Notes, proposals, and experiment documents may be created freely at any time — none become active until project assets are modified. A change stops being active when it is archived.

Format:
```markdown
# Active Change
**Name**: <change-name>
**Type**: Proposal | Experiment
**Phase**: <current phase or status>
```

## Starting a Change

Changes can begin as a Note (freeform capture) or directly as a Proposal or Experiment. A Note can be progressed to either type when the intent is clear enough to commit to a direction.
