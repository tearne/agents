# Planning Process

A change is a single file: `changes/planning/<change-name>.md`.

## Structure

```markdown
# <Change Name>

## Intent
Why this change is needed. Focus on behaviours and use domain language.

## Approach
How it will be implemented. May include constraints, example code, technical language.

## Plan
- [ ] Pending task
- [x] Completed task
- [-] Parked task

## Conclusion
Left blank — completed by the builder.
```

## Stage Gates

Sections are added sequentially, only after explicit user approval. Each section must be written to the file before approval is sought — do not draft in chat and write only after approval.

For each completed section, verify the checklist before asking for approval:

**Intent**
- Domain language only — stakeholders should be able to read it without technical knowledge
- Brief — no implementation detail
- Consistent with `RATIONALE.md` if present

**Approach**
- Technical language is appropriate here
- No text repeated from Intent
- Consistent with `RATIONALE.md` if present
- Change document reviewed for consistency; any issues flagged to user

**Plan**
- Tasks must be concrete and specific — the builder must be able to act on each without guessing
- All tasks written to the file before seeking approval
- Tasks prefixed with a type: `ADD`, `UPDATE`, `REMOVE`, `REVIEW`, `TEST`
- Tasks suitable for ticking off one by one — never batch-completed
- Consider whether any SPEC update tasks are required
- If versioning applies, agree bump size and capture in Approach
- Review cadence (per-task or at the end) agreed and captured in Approach
- Change document reviewed for consistency; any issues flagged to user

## Writing Conventions

- Do not insert manual line breaks in prose — write paragraphs as single unbroken lines so text reflows correctly with soft wrap
- No restatement of what the document already shows — capture *why*, not *what*
- No abbreviations that save typing but cost reading

## Picking Up from Feedback

When a change is in `changes/feedback/`, the builder has surfaced something requiring planner action. Read the `## Feedback` section and act based on the delivery status:

- **Delivered** — the intent was met; open new change documents for any incidental discoveries, then ask the user to archive the original
- **Partially delivered** — rework the plan to address what remains, remove completed tasks, and ask the user to move it back to `ready/`
- **Not delivered** — assess whether the original plan is salvageable; either rework it and resubmit to `ready/`, or archive and open a fresh change

## Handing Off

When the Plan is approved, tell the user the change is ready to move to `changes/ready/`. The user moves it — you do not.
