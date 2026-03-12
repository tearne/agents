# Proposal: Process Per Project
**Status: Draft**

## Intent
The current setup loads a single change management process globally, but different projects have different needs. Some warrant the full four-phase formal process; others need only lightweight intent capture, approval, and direct implementation. A single global process is too rigid.

## Specification Deltas

### ADDED
- A library of named process files lives in this repo (`/root/agents/`), each defining a distinct change management style:
  - `PROCESS_FORMAL.md` — the existing four-phase process (propose → design → implement → archive)
  - `PROCESS_LITE.md` — lightweight: capture and refine intent as a proposal, user approves, implement directly (no design phase, no archive)
- A project selects its process by `@`-including the chosen file in its local config (`CLAUDE.md` for Claude Code; `AGENTS.md` for OpenCode), e.g. `@/root/agents/PROCESS_FORMAL.md`
- `~/.claude/CLAUDE.md` carries a standing instruction: on startup, check whether the project's `CLAUDE.md` references a process file; if not, prompt the user to choose one and offer to create or update the local `CLAUDE.md`
- `~/.config/opencode/AGENTS.md` carries the equivalent instruction, checking the project's `AGENTS.md`
- The setup instruction also directs the agent to ensure the local config file (`CLAUDE.md` / `AGENTS.md`) is listed in the project's `.gitignore`, since it is personal/local configuration

### MODIFIED
- `~/.claude/CLAUDE.md`: remove `@/root/agents/PROCESS.md`; add setup instruction described above
- `PROCESS.md` renamed to `PROCESS_FORMAL.md` in this repo

### REMOVED
- No process is loaded globally by default
