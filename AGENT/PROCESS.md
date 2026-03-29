# Change Process

A change is typically a single file: `changes/open/<change-name>.md`. If the change produces assets, it can be converted to a folder: `changes/open/<change-name>/change.md`.

## Structure

```markdown
# <Change Name>

## Intent
Why this change is needed.  Focus on behaviours and use domain language.

## Approach
How it will be implemented.  May include constraints, example code, technical language.

## Plan / Log
Choose between upfront planning or a more iterative log-based appraoch.

**Plan** — ordered task list.
- [ ] Pending task
- [x] Completed task
- [-] Parked task

*— or —*

**Log** — iterative notes, findings, attempts.

## Conclusion
What was done or found.
```

## Stage Gates

Sections are added sequentially, only after approval from the user — e.g. "approved", or "yes" after a direct prompt. Each section must be written to the change file before approval is sought — do not draft in chat and write only after approval.

For each completed section, before asking for approval to move to the next section use the following checklists:

**Intent**
- Brief — no implementation detail
- Consistent with `RATIONALE.md` if present

**Approach**
- No text repeated from Intent
- Change document reviewed for consistency and any issues flagged to user
- Consistent with `RATIONALE.md` if present

**Plan** (if in use)
- All tasks written to the file before seeking approval
- Tasks prefixed with a type, e.g. `ADD TEST`, `UPDATE IMPL`, `REVIEW`.
- Tasks suitable for ticking off one by one as completed — never batch-completed at the end
- Change document reviewed for consistency and any issues flagged to user
- Consider whether any SPEC update tasks are required
- If using versioning, agree bump size - major, minor, or patch (captured in approach)
- Review cadence (per-task or at the end) must be agreed and captured in approach
- Additional questions may be required depending on circumstances. Answers should be noted in `## Approach`.

**Conclusion**
- `## Conclusion` written to the change file
- Log entries retrofitted into Intent, Approach, and Plan as appropriate
- Change document reviewed to remove duplication across sections

## Active Change

`changes/open/active.md` is a lock file. Its presence blocks a second change from touching project assets outside the `changes/` folder.

```markdown
# Active Change
**Name**: <change-name>
```

Create it when work on project assets begins. Delete on archive (see below)

If asked to create a new change, proposal, or note while a change is active, pause the active change and capture the new proposal's Intent in a new change file — writing into `changes/` is always permitted regardless of active change state. After capturing the Intent, offer to return to the interrupted change.

If the user requests further modifications during an active change, capture them in a `## Log` section of the change document (add the section if not present). Before archival, retrofit log entries back into the appropriate sections — Intent, Approach, and Plan — so the change document accurately reflects what was done.

## Archival

Archival requires explicit user instruction after the `## Conclusion` section has been completed. The archived change mirrors the open structure — a single file or folder — moved to `changes/archive/YYYY-MM-DD-<change-name>`.
