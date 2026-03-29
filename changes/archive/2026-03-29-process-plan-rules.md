# Process Plan Rules

## Intent
Plan behavioural rules are currently buried in the Plan description. Agents are less likely to follow rules embedded in descriptive text than explicit behavioural instructions. Moving them to a prominent position will make them harder to miss.

## Approach
Move the two existing Plan rules out of the descriptive text and into a separate bulleted list after the template, alongside the existing approval rule. Add a third rule requiring that all tasks be written to the change file before approval is sought.

Add a per-section completion checklist to the template, surfacing what to verify before asking the user to approve each section and move on:
- **Intent**: brief, no implementation detail; check for consistency with `RATIONALE.md` if present
- **Approach**: no text repeated from Intent; check for consistency with `RATIONALE.md` if present
- **Plan**: all tasks written to the file before seeking approval; check for consistency with `RATIONALE.md` if present

## Plan
- [x] CHANGE: `AGENT/PROCESS.md` — move Plan behavioural rules out of the Plan description and into explicit instructions after the template
- [x] CHANGE: `AGENT/PROCESS.md` — add explicit instruction that all tasks must be written to the change file before approval is sought
- [x] CHANGE: `AGENT/PROCESS.md` — add per-section completion checklists to the template

## Conclusion
Slimmed the Plan template description to remove embedded rules. Added per-section completion checklists after the template covering Intent (brevity, no implementation detail), Approach (no repetition from Intent), and Plan (tasks written before approval, ticked off one by one). Each section also checks consistency with `RATIONALE.md` if present.
