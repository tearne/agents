# Proposal: Active Proposal Tracking
**Status: Superseded — incorporated into process-consolidation**

## Intent
When discussions wander towards a new proposal mid-session, there is no standing mechanism to remind the user that another proposal is already in progress. An `active.md` file in `changes/open/` would record the current active proposal or experiment, giving the agent a clear signal to gently redirect if a conversation starts drifting towards opening a second one.

## Unresolved
- Format of `active.md` — pointer only (name + status), or richer context?
- Whether this is maintained by the agent as a standing instruction, or treated as a process artefact the user owns
