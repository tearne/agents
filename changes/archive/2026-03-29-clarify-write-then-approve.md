# Clarify Write-Then-Approve Sequence

## Intent

Agents repeatedly present change sections (Intent, Approach, Plan) in the chat rather than writing them to the change file first. The process requires writing each section to the file before seeking approval — not drafting in chat and writing only after approval. PROCESS.md should make the sequence unambiguous.

## Approach

Add a sentence or two to the Stage Gates section of `PROCESS.md` making explicit that each section must be written to the change file before approval is sought. No other sections need touching.

No SPEC impact. Patch-level change. Review at the end.

## Plan

- [x] UPDATE IMPL: add write-before-approval clarification to the Stage Gates section of `PROCESS.md`

## Conclusion

Added a sentence to the Stage Gates section of `PROCESS.md` making explicit that each section must be written to the change file before approval is sought.
