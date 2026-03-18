# Formal Process

A four-phase process with per-task signoff at each step.

| Phase | Action | Output |
|-------|--------|--------|
| **1. Propose** | Define intent and scope | `changes/open/<change-name>/proposal_formal.md` |
| **2. Design** | Plan the technical approach and tasks | `changes/open/<change-name>/design.md` |
| **3. Implement** | Execute tasks one at a time, pausing for review after each | Updated code/tests |
| **4. Archive** | Apply the proposal delta to `SPEC.md`; move the change folder | Updated `SPEC.md` |

Each phase requires explicit approval before the next begins.

> **Getting started**: When setting up a new project, create the initial `SPEC.md` directly. Once it is in place, open a change using the name `initial-implementation` to design and carry out the first implementation.

## 1. Propose

Create a `proposal_formal.md` in `changes/open/<change-name>/`. If the change originated as a Note, retain the `note.md` alongside it.

A proposal in `Status: Draft` is a work in progress; `Status: Approved` means the user has approved it and the next phase may begin.

```markdown
# Proposal: <Change Name>
**Status: Draft | Approved**

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

> **Behaviour over implementation**: Intent is often expressed in technical or implementation terms — that is fine for drafts. Before a proposal is finalised, guide the user towards expressing required behaviours instead. Reserve technical specification for genuine constraints or non-functional requirements.

## 2. Design

Create a `design.md` in the same change folder. It should explain *how* the approved spec changes will be realised and include an ordered task list — implementation-specific detail belongs here, not in the proposal or spec.

```markdown
# Design: <Change Name>
**Status: Draft | Approved**

## Approach
Technical explanation of how the change will be implemented,
referencing relevant code, libraries, and patterns.

## Tasks
Tasks should clearly indicate the asset they will work on. e.g. "Spec", "Tests", "Impl", "Verify", "Process"
1. Tests: <testing task>
2. Impl: <implementation task>
3. Verify: <verification task>
4. Process: <confirm ready to archive>
```

Where possible, tests should be listed as separate items, written first, and verified to fail (TDD style).

## 3. Implement

Work through the task list one item at a time. Mark each task complete with a tick (`✓`) in `design.md` as it is completed. Pause after each task, referencing it by number, and invite the user to review before proceeding to the next (e.g. "Task 1 ready for review"). Do not modify `SPEC.md` during this phase.

When all tasks are complete, announce the new version number (e.g. "v1.2.3 ready for review") before inviting the user to review the finished work. Each round of corrections after this point warrants a patch bump.

## 4. Archive

Apply the proposal delta to the `SPEC.md` alongside the `changes/` directory. Move the change folder to `changes/archive/YYYY-MM-DD-<change-name>/`. Remove `changes/open/active.md`.

Before archiving, ensure the change folder is complete:
- **No proposal**: prompt the user to retrospectively capture intent in a `proposal_formal.md` before proceeding
- **No design, or no formal design phase followed**: create a minimal `design.md` describing what was done, marked `*(retrospective)*`
- **Proposal not marked Approved**: if the change was approved, update the status to `Approved`; otherwise flag to the user before proceeding
