# Proposal: Process Enforcement and Change Type Simplification
**Status: Approved**

## Intent
Agents skip the change process for small tasks because the lightest available track still requires multiple structured documents. Separately, the current change types are more complex than necessary. This proposal introduces a lightweight Fix track, simplifies the type set, and strengthens the ordering constraint to prevent edits happening before any change record exists.

## Specification Deltas

### ADDED
- **Fix** change type — `change.md` with a `## Log` section is the only required document for the change folder; the agent flags for escalation to Proposal or Spike when the fix grows in complexity or uncertainty
- A one-line directive prepended to `~/.claude/CLAUDE.md` and `~/.config/opencode/AGENTS.md` by `setup.py`, ensuring the active change constraint is prominent before the `@`-include chain

### MODIFIED
- **Proposal** — Draft state is freeform (no required structure); structure (Intent, Specification Deltas, Scope) only required before marking Approved; subsumes Note (a Draft proposal *is* a note)
- **Spike** (renamed from Experiment) — iterative exploration towards a clear goal where the path is unknown; `washup.md` renamed to `findings.md` and expanded to capture: journey summary, final selected approach, and goal evolution
- **Starting document** — all change types begin with `change.md`; type-specific documents (`design.md`, `findings.md`) are added as the change progresses
- **Active change tracking** — the agent must create `active.md` *before* editing any project asset (code, documentation, config, etc.); editing change documents is exempt; if the agent realises it has edited without one, it creates it retrospectively and flags the gap; the user may explicitly waive this requirement
- **`active.md` format** — gains `**Type**: Fix | Proposal | Spike`
- **Type mutability** — changes may move between types as understanding evolves; the type at the top of `change.md` is updated accordingly
- **Archival expectations**:
  - Fix — `change.md` with log only
  - Proposal — `change.md`, `design.md`, and any other assets produced during implementation
  - Spike — `change.md` and `findings.md`, plus any other assets as relevant
- **Mid-session recovery** — if a session ends mid-change, `active.md` and `change.md` provide enough context to resume; the agent reads both at session start if present

### REMOVED
- **Note** change type — a freeform Draft proposal serves the same purpose; Note is no longer a distinct type
