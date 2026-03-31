# Build Process

## Starting a Build

1. Check that `changes/building/` is empty — if not, stop and tell the user
2. Move the change file from `changes/ready/` to `changes/building/`
3. Read the change document in full before doing any work

## Executing the Plan

Work through tasks in order, ticking each off in the change document as it is completed. Never batch-complete tasks — tick them off one by one as each is done.

If a task cannot be completed as written, stop and raise it with the user before proceeding.

## Mid-Build Changes

If the user requests a change to requirements or approach during a build, capture it in a `## Log` section of the change document (add the section if not present). Then:

- If the change is minor and consistent with the original Intent, adapt the plan and continue
- If the change materially alters the Intent or scope, stop and ask the user whether to proceed or return to planning

Before writing the Conclusion, retrofit log entries back into Intent, Approach, and Plan so the change document accurately reflects what was built.

## Feedback

When the build surfaces something the planner needs to act on — a plan that cannot be executed as written, bugs discovered in passing, or other concerns warranting new changes — move the change to `changes/feedback/` instead of `archive/`. Write a `## Feedback` section to the change document before moving it:

- **Delivery status**: one of — *delivered*, *partially delivered*, or *not delivered*
- What was found and why it warrants planner attention
- Any specific questions or suggested next steps

The Feedback section replaces the Conclusion in this path — do not write both.

Moving to `changes/feedback/` requires explicit user instruction, just as archival does. Write the Feedback section, present it to the user, and wait for instruction before moving the file.

## Conclusion

When all tasks are complete, write a `## Conclusion` section to the change document:

- If the build went to plan with no surprises, a single sentence confirming completion is sufficient
- Note any deviations, discoveries, or decisions made during the build that were not anticipated in the plan
- Do not restate the plan — the tasks already record what was done

## Archival

Archival requires explicit user instruction. When instructed:

1. Move the change file from `changes/building/` to `changes/archive/YYYY-MM-DD-<change-name>.md`
2. The `changes/building/` folder should now be empty, unblocking the next build
