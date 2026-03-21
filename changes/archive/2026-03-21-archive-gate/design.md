# Design: Archive Gate
**Status: Approved**

## Approach

Two related changes: consolidating `proposal.md` into `change.md`, and adding an explicit archival gate.

`change.md` becomes the single document for all change types. The type is declared at the top with `**Type**`; `**Status**` replaces the per-document status field. Type-specific sections follow. The separate `proposal.md` is dropped; `design.md` and `findings.md` are retained as supplementary documents.

The archival gate is a simple explicit rule: the agent must not archive without a direct user instruction. It is added prominently to the archive section of `PROPOSAL.md`, the adoption section of `SPIKE.md`, and the archival expectations section of `PROCESS/README.md`.

The existing `change.md` and `proposal.md` in this change folder are a transitional artefact; no migration of other open changes is needed (there are none).

## Tasks

1. ✓ Process: Update `AGENT/PROCESS/README.md` — consolidate starting a change section; add archival gate to archival expectations; drop `proposal.md` references
2. ✓ Process: Update `AGENT/PROCESS/PROPOSAL.md` — rewrite phase 1 template to use `change.md`; add archival gate to phase 4; update phase table
3. ✓ Process: Update `AGENT/PROCESS/SPIKE.md` — rewrite template to use `change.md` without redundant `**Type**` line; add archival gate to adoption section
4. ✓ Spec: Update `SPEC.md` — reflect consolidated `change.md` structure and archival gate
5. Process: Confirm ready to archive
