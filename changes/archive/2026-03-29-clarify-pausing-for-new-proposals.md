# Clarify Pausing for New Proposals

## Intent

Agents are confused when asked to create a new change, proposal, or note while another change is active. They incorrectly treat the `changes/` exemption as blocking rather than enabling: since writing into `changes/` is always permitted, an agent can pause the active change, capture the new proposal's Intent in a new change file, and then offer to return to the active change. PROCESS.md should make this behaviour explicit.

## Approach

Add a short paragraph to the **Active Change** section of `PROCESS.md` clarifying that pausing is permitted: the `changes/` exemption means a new proposal's Intent can always be captured, and after doing so the agent should offer to return to the interrupted change. No other sections need touching.

No SPEC impact. Patch-level change. Review at the end.

## Approach

Add a paragraph to the **Active Change** section of `PROCESS.md` clarifying that pausing is permitted: since `changes/` is always exempt, a new proposal's Intent can be captured at any time. After doing so, the agent should offer to return to the interrupted change. No other sections need touching.

No SPEC impact. Patch-level change. Review at the end.

## Plan

- [x] UPDATE IMPL: add pausing-for-new-proposals paragraph to the Active Change section of `PROCESS.md`

## Conclusion

Added a paragraph to the Active Change section of `PROCESS.md` making explicit that pausing is permitted, that `changes/` is always writable, and that the agent should offer to return to the interrupted change after capturing a new proposal's Intent.
