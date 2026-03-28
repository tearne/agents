# Rationale Stage

## Intent
The process currently starts from `SPEC.md`, but a spec answers *what* with nothing to anchor it to *why*. When building a new project, the problem and solution deserve explicit debate before requirements are written down. Additionally, as a project evolves, proposals have no obligation to check whether they conflict with the original project rationale — drift can go unnoticed.

This change introduces `RATIONALE.md` as an optional but recommended step for new projects, and adds a rationale-consistency check to the proposal approval gate.

## Approach
- Add `RATIONALE.md` — an optional but recommended document at the project root, created before the initial `SPEC.md`, capturing: the problem being solved, why existing solutions are insufficient, and the key decisions that shape the solution
- Recommend structure: Problem, Existing Solutions (why they fall short), Solution, Key Decisions
- `RATIONALE.md` is written through debate — the agent challenges the user's rationale to surface weak assumptions before they become spec requirements
- Add a rationale-consistency check: before a change is marked Approved, confirm it does not conflict with `RATIONALE.md` if one exists; flag any tension for the user to resolve
- Update `AGENT/README.md` Specifications section to mention `RATIONALE.md` as the upstream document that motivates the spec
- Update `PROCESS.md` getting-started guidance to recommend creating `RATIONALE.md` before `SPEC.md` for new projects
