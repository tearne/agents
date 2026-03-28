# POS: Config File Modifications

## Intent
POS scripts frequently need to modify user config files (shell profiles, dotfiles, tool configs). Without a standard, scripts risk silently overwriting user settings or producing duplicate or conflicting entries on repeated runs. This change adds a standard section to `POS.md` covering how config file modifications should behave.

## Approach
Add a **Config file modifications** section to `POS.md` establishing three required properties for any POS script that modifies a config file:

1. **Non-destructive** — never overwrite or delete existing content except where explicitly required; prefer targeted edits
2. **Idempotent** — repeated runs produce the same result; check whether the intended state already exists before making changes
3. **Non-conflicting** — before modifying, check whether a conflicting entry already exists (e.g. another assignment to the same variable); if so, leave the file untouched and surface the conflict to the user

Include a reference implementation covering common cases (appending a block, setting a value, replacing a value), along with guidance on when a conflict check is needed vs. when a modification is always safe.

## Plan
- [x] ADD: `POS.md` — Config file modifications section

## Conclusion
Added Config file modifications section to `POS.md` with three required properties and reference implementations for append and conflict-guarded append cases.
