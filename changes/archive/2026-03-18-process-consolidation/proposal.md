# Proposal: Process Consolidation
**Status: Approved**

## Intent
`PROCESS_FORMAL.md` and `PROCESS_LITE.md` are almost entirely duplicated. The only genuine difference is implementation supervision: Formal requires per-task signoff; Lite implements freely with a single review at the end. Consolidating into a `PROCESS/` directory eliminates drift, makes the real distinction explicit, and allows projects to select a mode per task rather than committing to one for the whole project.

## Specification Deltas

### ADDED

- **`PROCESS/` directory** — replaces `PROCESS_FORMAL.md` and `PROCESS_LITE.md` with the following structure:
  - `PROCESS/README.md` — always-loaded entry point. Contains: SPEC conventions, the proposal template, archive rules, a description of the available modes, Note guidance, and active change tracking. A Note is a `note.md` file in `changes/open/<name>/` — freeform, no required structure, exempt from active change tracking (Notes do not touch code). To progress a Note, the user selects a mode (Formal, Lite, or Experiment); the `note.md` is retained alongside the new `proposal.md` or `experiment.md` as a record of the original capture. Active change tracking applies from the point code is touched; no more than one active change at a time.
  - `PROCESS/FORMAL.md` — implementation phase detail for the formal mode: per-task signoff, TDD guidance, version announcement.
  - `PROCESS/LITE.md` — implementation phase detail for the lite mode: implement freely, single review at the end, version announcement.
  - `PROCESS/EXPERIMENT.md` — the experimenting form (currently duplicated in both process files).

### MODIFIED

- **Proposal template** — remove `Status: Note`; Draft and Approved are sufficient. Notes are a separate entity (`note.md`), not a proposal status.
- **`setup.py`** — update to write `@PROCESS/README.md` instead of `@PROCESS_FORMAL.md` / `@PROCESS_LITE.md` into both `~/.claude/CLAUDE.md` and `~/.config/opencode/AGENTS.md`.
- **Process Selection instruction** — update to reflect the new model: `PROCESS/README.md` is always loaded; the agent asks the user which mode to use at the start of each change, or reads the project config file if a mode is pre-selected there.
- **This project's `CLAUDE.md`** — update to reference `PROCESS/README.md` (or remove the reference entirely, deferring to the global instruction).
- **`SPEC.md`** — update Configuration Files list and Behaviour/Verification sections to reflect the new `PROCESS/` directory structure for both Claude Code and OpenCode.

### REMOVED

- `PROCESS_FORMAL.md`
- `PROCESS_LITE.md`
