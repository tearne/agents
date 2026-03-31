# Builder Feedback Loop

## Intent

A build may surface issues the planner needs to act on: a plan that cannot be executed as written, bugs noticed in passing, or other concerns that warrant new changes. The builder currently has no way to communicate these back. A `changes/feedback/` state gives the builder a permitted path to park a change with a `## Feedback` section describing what it found. The feedback must clearly state whether the intent of the change was successfully delivered, partially delivered, or not delivered — so the planner can determine whether to rework and resubmit the plan, open new changes for incidental discoveries, or archive.

## Approach

`changes/feedback/` is added as a state in the machine. The builder gains one new permitted transition: `building/` → `feedback/`.

**When the builder uses feedback**

The builder moves a change to `feedback/` instead of `archive/` when it has surfaced something the planner should act on. This replaces the Conclusion section — the `## Feedback` section serves the same closing purpose but signals that planner action is required.

The `## Feedback` section must include:
- **Delivery status**: one of — *delivered*, *partially delivered*, or *not delivered*
- A brief description of what was found and why it warrants planner attention
- Any specific questions or suggested next steps

Moving to `changes/feedback/` requires explicit user instruction — the builder writes the section and presents it to the user before moving the file.

**When the planner picks up from feedback**

The planner reads the Feedback section and chooses one of:
- Rework the plan in the change document and move it back to `ready/`
- Open new change documents for incidental discoveries, then archive the original
- Archive without further action if the work is no longer relevant

**Files to update**

- `SPLIT/BUILDER/README.md` — add `building/` → `feedback/` to permitted transitions
- `SPLIT/BUILDER/PROCESS.md` — add guidance on when and how to write a Feedback section
- `SPLIT/PLANNER/PROCESS.md` — add guidance on picking up from `feedback/`
- `SPLIT/SUPERVISOR/README.md` — add `changes/feedback/` to state machine diagram and project setup
- `SPLIT/opt-in.py` — create `changes/feedback/` during setup

## Plan

- [x] UPDATE `SPLIT/BUILDER/README.md` — add `building/` → `feedback/` to permitted transitions
- [x] UPDATE `SPLIT/BUILDER/PROCESS.md` — add Feedback section guidance
- [x] UPDATE `SPLIT/PLANNER/PROCESS.md` — add guidance on picking up from `feedback/`
- [x] UPDATE `SPLIT/SUPERVISOR/README.md` — add `feedback/` to state machine diagram and project setup
- [x] UPDATE `SPLIT/opt-in.py` — create `changes/feedback/` during setup

## Log

- Builder moved file to `feedback/` without user approval — same pattern as archival; explicit user instruction required before moving to `feedback/`

## Conclusion

Completed with one fix identified during testing: the builder moved to `feedback/` without user approval. Explicit user instruction is now required before moving, consistent with archival.
