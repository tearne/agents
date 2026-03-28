# Change Process

A change is typically a single file: `changes/open/<change-name>.md`. If the change produces assets, it becomes a folder: `changes/open/<change-name>/change.md`.

```markdown
# <Change Name>

## Intent
Why this change is needed.  Focus on behaviours and domain language.

## Approach
How it will be implemented.

## Plan / Log
**Plan** — ordered task list, agreed upfront, with prefixes such as TEST, ADD, CHANGE, REMOVE.
- [ ] Pending task
- [x] Completed task
- [-] Parked task

*— or —*

**Log** — iterative notes, findings, attempts.

## Conclusion
What was done or found.
```

Sections are added sequentially, only after approval from the user — e.g. "approved", or "yes" after a direct prompt.

## Kickoff

Before the user approves a Plan, agree:
- **Review cadence** — per-task (pause after each task) or end (implement freely, then review)
- **Version bump** — major, minor, or patch? *(only if versioning applies)*

Additional questions may be required depending on which guides are active. Answers should be noted in `## Approach`.

## Active Change

`changes/open/active.md` is a lock file. Its presence blocks a second change from touching project assets outside the `changes/` folder.

```markdown
# Active Change
**Name**: <change-name>
```

Created when work on project assets begins. Removed on archive.

## Archival

Archival requires explicit user instruction after the `## Conclusion` section has been completed. The archived change mirrors the open structure — a single file or folder — moved to `changes/archive/YYYY-MM-DD-<change-name>`.
