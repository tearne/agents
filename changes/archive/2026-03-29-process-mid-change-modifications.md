# Process: Mid-Change Modifications

## Intent
During an active change, the user may ask for further modifications that were not part of the original plan. These should be tracked and reconciled with the change document before archival — currently there is no guidance on how to handle this.

## Approach
Two additions to `AGENT/PROCESS.md`:

1. **New paragraph in the Active Change section** — explains that mid-change modifications requested by the user should be captured in a `## Log` section of the change document (added if not already present), and that before archival these log entries must be retrofitted back into the appropriate sections (Intent, Approach, Plan) so the change document accurately reflects what was actually done.

2. **New Conclusion checklist in the Stage Gates section** — "Log entries retrofitted into Intent, Approach, and Plan as appropriate" and "`## Conclusion` written to the change file".

## Plan
- [x] UPDATE IMPL: Add mid-change modification guidance paragraph to the Active Change section of `AGENT/PROCESS.md`
- [x] UPDATE IMPL: Add pre-archival checklist to the Archival section of `AGENT/PROCESS.md` with retrofit item

## Conclusion
Added a paragraph to the Active Change section describing how to capture mid-change modifications in a `## Log` section and retrofit them before archival. Added a Conclusion checklist to the Stage Gates section with items for writing the Conclusion and retrofitting log entries.
