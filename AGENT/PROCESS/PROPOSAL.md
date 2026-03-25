# Proposal Process

A proposal moves through five statuses, each requiring explicit user approval to advance:

`Draft` → `Approved` → `Designing` → `Implementing` → `Archived`

The status is recorded in `change.md` throughout.

> **Getting started**: When setting up a new project, create the initial `SPEC.md` directly. Once it is in place, open a change using the name `initial-implementation` to design and carry out the first implementation.

## Draft

Create `change.md` in `changes/open/<change-name>/`. A Draft is freeform — no required structure.

## Draft → Approved

Structure (Intent, Specification Deltas, Scope) is required before the user can mark it Approved.

```markdown
# <Change Name>
**Type**: Proposal
**Status**: Draft

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

## Approved → Designing

Create `design.md` in the same change folder. It should explain *how* the approved spec changes will be realised and include an ordered task list — implementation-specific detail belongs here, not in the proposal or spec.

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

## Designing → Implementing

Agree review cadence with the user before starting:
- **Per-task**: pause after each task and invite review before proceeding
- **End review**: implement freely until all tasks are done, then invite review

Work through the task list, marking each task complete with a tick (`✓`) in `design.md`. Do not modify `SPEC.md` during this phase.

When all tasks are complete, announce the new version number (e.g. "v1.2.3 ready for review") and invite the user to review. Each round of corrections after this point warrants a patch bump.

## Implementing → Archived

**Do not archive without an explicit user instruction. Task completion alone is not sufficient.**

Apply the proposal delta to `SPEC.md`. Move the change folder to `changes/archive/YYYY-MM-DD-<change-name>/`. Remove `changes/open/active.md`.

Before archiving, ensure the change folder is complete:
- **No design**: create a minimal `design.md` describing what was done, marked `*(retrospective)*`
- **`change.md` not marked Approved**: if the change was approved, update the status; otherwise flag to the user before proceeding
