# POS Shebang Hardening
**Type**: Fix
**Status**: Approved

## Intent
When POS scripts are invoked, the shebang expands to `uv run --script /path/to/script <args>`. Adding `--` explicitly terminates `uv`'s own argument parsing, making it unambiguous that all subsequent arguments belong to the script. This guards against any future `uv` version introducing a short flag that collides with a script argument.
