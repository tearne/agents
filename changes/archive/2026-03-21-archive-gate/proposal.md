# Proposal: Archive Gate
**Status: Approved**

## Intent
Two related problems: agents proceed to archive as soon as all tasks are complete without waiting for explicit user instruction; and the current process introduces an unnecessary `proposal.md`/`change.md` split where `change.md` is little more than a stub. This proposal adds an explicit archival gate and consolidates all change content into `change.md`.

## Specification Deltas

### MODIFIED
- **`change.md`** — becomes the single document for all change types; type-specific content (intent, spec deltas, scope for proposals; goal, log, outcome for spikes; log for fixes) lives here rather than in a separate `proposal.md`; type is declared at the top with `**Type**: Fix | Proposal | Spike`; separate `proposal.md` is dropped
- **`AGENT/PROCESS/PROPOSAL.md`** — update all references from `proposal.md` to `change.md`; phase 4 gains explicit gate: archival requires a direct user instruction; task completion alone is not sufficient
- **`AGENT/PROCESS/SPIKE.md`** — update template to use `change.md`; adoption section gains same archival gate
- **`AGENT/PROCESS/README.md`** — update starting a change section and archival expectations; add one-liner that archival is always user-triggered
- **`SPEC.md`** — reflect consolidated `change.md` structure and archival gate
