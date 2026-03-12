# Proposal: No Unsolicited Git Writes
**Status: Approved**

## Intent
The agent should not run git write commands (commit, push, add, etc.) or prompt the user to run them unless the user has explicitly asked. This prevents the agent from being proactive about git operations in ways the user didn't request.

## Specification Deltas

### ADDED
- A new file `BEHAVIOUR.md` is introduced to hold general agent behaviour rules, loaded globally alongside `PROCESS.md` and `POS.md`
- Its first rule: never execute git write commands (e.g. `git add`, `git commit`, `git push`, `git reset`) or suggest the user run them, unless explicitly instructed to do so
