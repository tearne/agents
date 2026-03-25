# Process
This file covers how changes are managed. For project-level concepts (specs, changes directory), see `AGENT/README.md`.

## Types of Change

**Fix** — A small, well-understood change. If it grows in complexity or uncertainty, escalate to a Proposal or Spike.

User approval of `change.md` is required before any fix work begins.

```markdown
# <Change Name>
**Type**: Fix
**Status**: Draft | Approved

## Log
Freeform record of what was done.
```

**Proposal** — A change where the intent and approach can be defined upfront. See `PROCESS/PROPOSAL.md`.

**Spike** — Exploration towards a clear goal where the path is unknown. See `PROCESS/SPIKE.md`.

Changes may move between types as understanding evolves; update `**Type**` in `change.md` accordingly.

## Starting a Change

All changes begin with a `change.md` in `changes/open/<change-name>/`. The type and status are declared at the top.

## Active Change Tracking

`changes/open/active.md` identifies the current active change for project resources. Change documents are exempt from the following controls.

- **Session start** — if `active.md` exists, remind the user of the active change
- **Before editing any project asset** — check `active.md` does not exist, then create it; if missed, create it retrospectively and flag the gap; the user may explicitly waive this
- **If `active.md` already exists** — stop and escalate to the user before proceeding; do not pause, replace, or set aside the active change without explicit user instruction
- **On archive** — remove `active.md`

```markdown
# Active Change
**Name**: <change-name>
**Type**: Fix | Proposal | Spike
```

## Archival Expectations

Archival requires an explicit user instruction — task completion alone is never sufficient to proceed.

- **Fix** — `change.md` with log
- **Proposal** — `change.md` and `design.md`, plus any other assets produced during implementation
- **Spike** — `change.md` and `findings.md`, plus any other assets as relevant

## Additional Guides

Optional guides live in `ADDITIONAL/`. See `ADDITIONAL/README.md`.
