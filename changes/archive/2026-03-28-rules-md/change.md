# Rules.md
**Type**: Proposal
**Status**: Approved

## Intent
Agents are violating hard rules despite them being documented across multiple files — staging git changes, self-approving, misreading change creation rules. Restructuring `AGENT/README.md` to lead with gates and a change process orientation gives agents the most critical information immediately on load, before any `@`-includes resolve.

`AGENT/README.md` is restructured to serve two purposes before the `@`-includes:
1. **Gates** — terse, positively-framed rules for actions requiring explicit user instruction
2. **Change process orientation** — a high-level summary of change types with pointers to detail documents

The preamble in `CLAUDE.md`/`AGENTS.md` is slimmed to a single pointer: "Before starting any work, read and apply `AGENT/README.md`."

The discipline for README.md: if something needs more than one line, it belongs in the linked document.

## Specification Deltas

### REMOVED
- `AGENT/BEHAVIOUR.md` — deleted; git rule moved to README.md gates; markdown rule moved to STYLE.md

### MODIFIED
- `AGENT/README.md` — restructured to lead with gates and change process orientation before `@`-includes; existing Specifications and Changes sections retained
- `AGENT/STYLE.md` — add `## Markdown` section (prose line wrapping rule, moved from BEHAVIOUR.md)
- `SPEC.md` — reflect restructured README.md; document the discipline for README.md: each rule and change type summary must fit on one line — if more is needed, it belongs in the linked document
