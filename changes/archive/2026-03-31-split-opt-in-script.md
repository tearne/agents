# Split Opt-In Script

## Intent

Opting a project in to the split system requires creating several files by hand. A POS (Python Orchestrated Script) automates this so the process is a single command run from a project root.

## Approach

The script lives at `SPLIT/opt-in` and is run from the target project root. It creates or verifies each file required by the split system:

- `CLAUDE.md` — points to `SPLIT/SUPERVISOR/README.md`
- `.claude/settings.local.json` — adds `claudeMdExcludes` for `~/.claude/CLAUDE.md`
- `planner/CLAUDE.md` — points to `SPLIT/PLANNER/README.md`
- `planner/.claude/settings.local.json` — excludes global and parent `CLAUDE.md`
- `builder/CLAUDE.md` — points to `SPLIT/BUILDER/README.md`
- `builder/.claude/settings.local.json` — excludes global and parent `CLAUDE.md`
- `changes/planning/`, `changes/ready/`, `changes/interrupted/`, `changes/archive/` — created if absent
- `.gitignore` — `CLAUDE.md`, `planner/`, and `builder/` appended if absent

All file operations are idempotent — the script checks whether the intended state already exists before writing. For `settings.local.json`, if the file exists but does not already contain `claudeMdExcludes`, the script surfaces a conflict and leaves the file untouched rather than merging blindly into unknown JSON.

The script reports each action taken (created / already present / conflict) using `rich` for clarity.

Version starts at `1.0.0`. Review at the end.

## Plan

- [x] ADD `SPLIT/opt-in` — complete POS script: all file creation steps, `.gitignore` update, and `rich` status reporting
- [x] REVIEW `SPLIT/opt-in`

## Conclusion

Completed as planned. During review, the script was renamed to `opt-in.py` and a missing rule was added to `SPLIT/BUILDER/README.md` prohibiting the builder from moving files between state folders other than its two defined transitions.
