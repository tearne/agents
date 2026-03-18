# Lite Process

A three-phase process with a single review at the end.

| Phase | Action | Output |
|-------|--------|--------|
| **1. Propose** | Define intent and scope | `changes/open/<change-name>/proposal_lite.md` |
| **2. Design** | Outline the approach, list tasks, and implement | `changes/open/<change-name>/design.md` + updated code/tests |
| **3. Archive** | Apply the proposal delta to `SPEC.md`; move the change folder | Updated `SPEC.md` |

Each phase requires explicit approval before the next begins.

> **Getting started**: When setting up a new project, create the initial `SPEC.md` directly. Once it is in place, open a change using the name `initial-implementation` to carry out the first implementation.

## 1. Propose

Create a `proposal_lite.md` in `changes/open/<change-name>/`. If the change originated as a Note, retain the `note.md` alongside it.

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

Work through the task list, ticking tasks off (`✓`) in `design.md` as they complete. No per-task signoff is required — implement freely until all tasks are done, then announce the new version number (e.g. "v1.2.3 ready for review") before inviting the user to review the result. Each round of corrections after this point warrants a patch bump.

## 3. Archive

Apply the proposal delta to the `SPEC.md` alongside the `changes/` directory. Move the change folder to `changes/archive/YYYY-MM-DD-<change-name>/`. Remove `changes/open/active.md`.

Before archiving, ensure the change folder is complete:
- **No proposal**: prompt the user to retrospectively capture intent in a `proposal_lite.md` before proceeding
- **No design**: create a minimal `design.md` describing what was done, marked `*(retrospective)*`
- **Proposal not marked Approved**: if the change was approved, update the status to `Approved`; otherwise flag to the user before proceeding
