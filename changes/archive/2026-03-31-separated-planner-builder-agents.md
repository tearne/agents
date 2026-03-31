# Separated Planner and Builder Agents

## Intent

Agents lose fidelity to process instructions when context grows large or when a single agent must hold both planning and execution concerns simultaneously. The goal is to explore a model where planning and building are handled by entirely separate agents — each started fresh per task with its own focused configuration — so that neither role can drift into the other's concerns.

The planner may read any project file but may only write to a dedicated `changes/planning/` folder. The builder works from a `changes/ready/` queue, moving changes through a state machine: `planning/ → ready/ → building/ → archive/`, with an `interrupted/` holding state for disconnected builders awaiting resumption. Only one builder may run at a time, enforced by the presence of a file in `changes/building/`.

This experiment lives in a separate folder alongside the existing `AGENT/` configuration so the current system is not disrupted while the new model is being developed. As part of this work, the existing directives in `AGENT/` will be reviewed and split into planner-specific and builder-specific variants.

Projects opt in to the split system by adding a project-level `CLAUDE.md` pointing to `~/agents/SPLIT/SUPERVISOR/README.md` and a `.claude/settings.local.json` that excludes `~/.claude/CLAUDE.md`, preventing the global config from loading alongside it. The global `~/.claude/CLAUDE.md` is left untouched, so all existing projects continue to work without modification.

## Approach

The new system lives at `~/agents/SPLIT/` with three role subdirectories: `SUPERVISOR/`, `PLANNER/`, and `BUILDER/`.

**Role configs**

Each role has a `README.md` as its entry point, equivalent to `AGENT/README.md` in the current system. The existing directives in `AGENT/` are reviewed and redistributed:

- `STYLE.md` and `STYLE-RUST.md` → `BUILDER/` only; code style is irrelevant to planning
- `PROCESS.md` → split: `PLANNER/` receives the planning-phase process (Intent, Approach, Plan authoring); `BUILDER/` receives the execution-phase process (plan execution, Conclusion, archival)
- Style guidance for writing change documents (prose quality, markdown conventions) → `PLANNER/`

**Supervisor**

The supervisor is the default entry point when running `claude` from a project root. Its concerns are: setting up the project's `planner/` and `builder/` subdirectories, verifying `.gitignore` excludes the `planner/`, `builder/`, and root `CLAUDE.md` entries, showing change state across the state machine folders, moving files between states on user instruction, and assisting recovery when a builder is interrupted. It refuses to plan or build.

When setting up a project, the supervisor creates:
- `planner/CLAUDE.md` — points to `~/agents/SPLIT/PLANNER/README.md`
- `planner/.claude/settings.local.json` — sets `claudeMdExcludes` to suppress all parent `CLAUDE.md` files, giving the planner genuine isolation
- `builder/CLAUDE.md` — points to `~/agents/SPLIT/BUILDER/README.md`
- `builder/.claude/settings.local.json` — same exclusion, isolating the builder

**State machine folders**

`changes/` uses five subfolders. The supervisor creates these during project setup:

```
changes/planning/    ← planner writes here
changes/ready/       ← user moves files here to queue for building
changes/building/    ← builder moves one file here on start; its presence blocks a new build
changes/interrupted/ ← user moves a file here when a builder disconnects
changes/archive/     ← builder moves the file here on completion
```

The builder refuses to start if `changes/building/` is non-empty. When a builder is interrupted, the user asks the supervisor to handle recovery: the supervisor moves the file from `building/` to `interrupted/` and instructs the user to start a fresh builder session from the `builder/` subdirectory, which will read the partially-completed plan and continue from the last checked-off task.

**Opt-in instructions**

A short, terse `SPLIT/GETTING-STARTED.md` guides a user through opting a project in: create the project `CLAUDE.md`, create `.claude/settings.local.json` with the exclusion, then run `claude` from the project root to let the supervisor complete setup.

**Review cadence**

Review after each role's files are complete: supervisor, then planner, then builder.

## Plan

- [x] REVIEW existing `AGENT/` directives (README, PROCESS, STYLE, STYLE-RUST) to identify what is planner-specific, builder-specific, or shared
- [x] ADD `SPLIT/SUPERVISOR/README.md`
- [x] REVIEW supervisor role config
- [x] ADD `SPLIT/PLANNER/README.md`
- [x] ADD `SPLIT/PLANNER/PROCESS.md` — planning phase only; writing conventions folded in; STYLE.md dropped
- [x] ADD `SPLIT/PLANNER/STYLE.md` — folded into PROCESS.md instead
- [x] REVIEW planner role config
- [x] ADD `SPLIT/BUILDER/README.md`
- [x] ADD `SPLIT/BUILDER/PROCESS.md` — execution phase only (plan execution, Conclusion, archival)
- [x] ADD `SPLIT/BUILDER/STYLE.md` — adapted from `AGENT/STYLE.md`
- [x] ADD `SPLIT/BUILDER/STYLE-RUST.md` — adapted from `AGENT/STYLE-RUST.md`
- [x] REVIEW builder role config
- [x] ADD `SPLIT/GETTING-STARTED.md` — minimal opt-in instructions

## Conclusion

The `SPLIT/` system was created alongside the existing `AGENT/` configuration without modifying it. All three roles are in place: supervisor (setup, state, recovery), planner (change document authoring only), and builder (plan execution only). The planner's writing conventions were folded into `PROCESS.md` rather than kept as a separate style file. The builder's `PROCESS.md` includes mid-build change handling via a log-and-retrofit approach, and Conclusion guidance that discourages restating the plan. Opt-in is via `GETTING-STARTED.md` and requires no changes to the global `~/.claude/CLAUDE.md`.
