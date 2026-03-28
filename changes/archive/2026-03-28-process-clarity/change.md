# Process Clarity Improvements
**Type**: Fix
**Status**: Approved

## Intent
Clarify session-end behaviour when an active change is open. The process covers session-start but not session-end, leaving agents uncertain whether to flag the open change or take some other action.

## Log

Reduced from four points to one — points 1, 2 (Complete status, archive prompt) dropped to avoid added complexity; point 4 folded into rules-md. Remaining: point 3 (session-end behaviour).

Add a one-liner to `PROCESS/README.md` active change tracking: if a session ends with `active.md` present, no action is required — the session-start rule will surface it next time.
