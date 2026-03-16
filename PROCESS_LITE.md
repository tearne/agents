# Process Lite

## Change Management Process
Project specifications are contained in `SPEC.md` files:
- The **root** `SPEC.md` covers the project as a whole (structure, shared requirements, integration testing).
- During spec changes, relevant assets such as proposals are stored in subfolders of the `changes` directory, which is placed alongside the relevant `SPEC.md`.
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

Changes to `SPEC.md` files follow the three-phase process below.

| Phase | Action | Output |
|-------|--------|--------|
| **1. Propose** | Define intent and scope | `changes/open/<change-name>/proposal.md` |
| **2. Design** | Outline the approach and list tasks | `changes/open/<change-name>/design.md` |
| **3. Archive** | Apply proposal delta to `SPEC.md`; move change folder | Updated `SPEC.md` |

> **Phase transitions**: Announce each move between phases (e.g. "Proposal ready for review", "Work complete — ready to review"). Do not proceed to the next phase without explicit approval.

> **Getting started**: When setting up a new project, create the initial `SPEC.md` directly. Once it is in place, use this process with the change name `initial-implementation` to carry out the first implementation.

### 1. Propose
Create a `proposal.md` in the `changes/open/<change-name>/` directory. A proposal with `Status: Note` is freeform — jot down thoughts and discussion without any required structure. The template below applies from `Draft` onwards.

```markdown
# Proposal: <Change Name>
**Status: Note | Draft | Approved**

## Unresolved (optional)
- Items not yet fully specified
- Use of this section indicates a proposal is not ready for review

## Intent
Why this change is needed.

## Specification Deltas
Omit delta sections which aren't relevant.

### ADDED
- New requirements being introduced

### MODIFIED
- Existing requirements being changed (note previous values)

### REMOVED
- Requirements being eliminated

## Scope (optional)
- **Out of scope**: what is deferred
- **In scope**: what this change covers
```

> **Behaviour over implementation**: Intent is often expressed in technical or implementation terms — that is fine for Notes and drafts. Before a proposal is finalised, guide the user towards expressing required behaviours instead. Reserve technical specification for genuine constraints or non-functional requirements.

### 2. Design
Create a lightweight `design.md` in the same change folder. It should give a broad outline of the approach and include a task list.

```markdown
# Design: <Change Name>
**Status: Draft | Approved**

## Approach
Brief outline of how the change will be implemented.

## Tasks
1. <task>
2. <task>
```

Work through the task list, ticking tasks off (`✓`) in `design.md` as they complete. No per-task signoff is required — implement freely until all tasks are done, then announce the new version number (e.g. "v1.2.3 ready for review") before inviting the user to review the result. This signals that implementation is complete and distinguishes the final review from a mid-implementation task review. Each round of corrections after this point warrants a patch bump.

### 3. Archive
Archive only after the user has approved the outcome of the implementation.

Apply the proposal delta to the `SPEC.md` alongside the `changes/` directory. Move the change folder to `changes/archive/YYYY-MM-DD-<change-name>/`.

Before archiving, ensure the change folder is complete:
- **No proposal**: prompt the user to retrospectively capture intent in a `proposal.md` before proceeding
- **No design**: create a minimal `design.md` describing what was done, marked `*(retrospective)*`
- **Proposal not marked Approved**: if the change was approved, update the status to `Approved`; otherwise flag to the user before proceeding
