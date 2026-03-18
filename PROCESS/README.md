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

**Note** — A `note.md` in `changes/open/<name>/`. Freeform, no required structure. Notes do not touch code and are exempt from active change tracking. To progress a Note, the user selects a mode (Formal, Lite, or Experiment); the `note.md` is retained alongside the new `proposal_formal.md`, `proposal_lite.md`, or `experiment.md` as a record of the original capture.

**Formal** — A structured four-phase process with per-task signoff. Use for changes where close review at each step is warranted. See `PROCESS/FORMAL.md`.

**Lite** — A three-phase process with a single review at the end. Use for smaller or lower-risk changes. See `PROCESS/LITE.md`.

**Experiment** — Exploratory work outside the change process. May or may not lead to a spec change. See `PROCESS/EXPERIMENT.md`.

## Active Change Tracking

A file `changes/open/active.md` records the current active change — one that is touching code. The agent must:
- Check for `changes/open/active.md` at the start of each session and remind the user of the active change if one is recorded.
- Create or update `active.md` when a change begins touching code.
- Warn the user if a conversation starts drifting towards opening a new change while one is already recorded in `active.md`.
- Remove `active.md` when the active change is archived.

Notes are exempt — since they do not count as active changes and can't directly effect change on the project.

Format:
```markdown
# Active Change
**Name**: <change-name>
**Type**: Formal | Lite | Experiment
**Phase**: <current phase or status>
```

## Mode Selection

Prompt the user to choose a mode before proceeding with any change.
