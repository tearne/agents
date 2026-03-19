# Python Orchestrated Script (POS)
The POS style helps Python take the place of native shell scripts. It strategically breaks some Python idioms to combine the different strengths of Python and shell scripts, such as favouring subprocess calls for shell commands while using Python control flow.

POS guidance:
- Prefer `subprocess` for shell commands; use Python for control flow. This makes commands easy to discover and copy-paste into a terminal.
    - Always use `shell=True` with a plain string — this keeps commands terminal-ready and avoids the need for `FileNotFoundError` handling (the shell handles command resolution; use `returncode` or `check=True` for error detection instead).
    - Examples:
        - To download the latest version of the `helix` `deb` for `amd64`:
        ```py
        subprocess.run(r"""curl -s https://api.github.com/repos/helix-editor/helix/releases/latest | grep -oP '"browser_download_url": "\K[^"]*amd64.deb' | xargs wget""", shell=True)
        ```
        - To apt install `curl`:
        ```py
        subprocess.run("""DEBIAN_FRONTEND=noninteractive apt-get install -y curl""", shell=True)
        ```
    - But don't take this to an extreme and force trivial actions like loops into the shell.
- Prefer a single Python source file, unless it compromises readability.
- Make the python file executable and use a `uv` shebang:
    ```sh
    #!/usr/bin/env -S uv run --script
    # /// script
    # requires-python = "==3.12.*"
    # ///
    ```
- Scripts should carry a version constant and expose it via `--version`:
    ```py
    VERSION = "1.0.0"
    ```
    ```py
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    ```
- Key functions at the top of the file (easy to comment out or jump to); utility functions at the bottom.
- Use a "main guard" at the bottom of the file. Include the `uv`/venv check here — it is an invocation-mode concern, not business logic — before calling `main()`:
    ```py
    if __name__ == "__main__":
        if not os.environ.get("VIRTUAL_ENV"):
            print("Error: no virtual environment detected. Run this script via './<script-name>' (requires uv), or activate a virtual environment first.")
            sys.exit(100)
        main()
    ```
- Prefer built-in libraries to maximise future compatibility. Suggested (when relevant): `argparse`, `atexit`, `getpass`, `os`, `pathlib`, `shutil`, `subprocess`, `sys`, `time`. Pre-approved external: `rich`. Other third-party libraries may be proposed if they are mainstream or would significantly enhance readability.
- When a `Path` object is already in hand, prefer `path.open(mode)` over `open(path, mode)` to keep pathlib usage consistent and avoid mixing idioms within the same file.
- Use `atexit` for cleanup of resources that must be released on normal exit and on `sys.exit()` (e.g. a log file opened at startup). Note: `atexit` handlers do not run on `os._exit()` or unhandled signals such as `SIGKILL`.
    ```py
    log = log_path.open("w")
    atexit.register(log.close)
    ```

## Sudo

Scripts that require elevated privileges for specific commands should ask for the password once upfront — after argument parsing, before the work begins — rather than running the whole script as root or prompting mid-execution.

Call `init_sudo()` at the start of the privileged section. It skips the prompt if already root or if passwordless sudo is available. Otherwise it prompts once, retries up to 3 times on failure, and caches the result. All privileged `subprocess` calls then use the `sudo()` helper.

```python
import getpass
import os
import subprocess
import sys

_PASSWORDLESS = object()  # sentinel: sudo works without a password
_sudo_password = None     # None = uninitialised; _PASSWORDLESS or str = ready


def init_sudo():
    global _sudo_password
    if os.geteuid() == 0:
        _sudo_password = _PASSWORDLESS
        return
    if subprocess.run("sudo -n true", shell=True, capture_output=True).returncode == 0:
        _sudo_password = _PASSWORDLESS
        return
    for attempt in range(3):
        password = getpass.getpass("sudo password: ")
        result = subprocess.run(
            "sudo -S true", shell=True, text=True,
            input=password + "\n",
            capture_output=True,
        )
        if result.returncode == 0:
            _sudo_password = password
            return
        print("Incorrect password, try again." if attempt < 2 else "")
    print("Error: too many incorrect attempts.")
    sys.exit(1)


def sudo(cmd):
    if _sudo_password is None:
        raise RuntimeError("init_sudo() must be called before sudo()")
    if os.geteuid() == 0 or _sudo_password is _PASSWORDLESS:
        _run(cmd)
    else:
        proc = subprocess.Popen(
            f"sudo -S {cmd}", shell=True, text=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        proc.stdin.write(_sudo_password + "\n")
        proc.stdin.close()
        output, _ = proc.communicate()
        if output:
            print(output, end="")
        if proc.returncode != 0:
            print(f"FAILED (exit {proc.returncode}): {cmd}")
            sys.exit(1)
```

Use `sudo()` exactly as you would use `subprocess.run()` for shell commands. The `init_sudo()` call belongs in `main()`, alongside other startup concerns like argument parsing — not in a helper buried in the business logic.

## Testing

Tests can be included in the same file using pytest with an inline dependency and self-executing main guard:

```py
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.12.*"
# dependencies = ["pytest"]
# ///

import pathlib
import sys
from unittest.mock import patch

import pytest

@pytest.fixture
def temp_home(tmp_path):
    with patch("pathlib.Path.home", return_value=tmp_path):
        yield tmp_path

def test_example(temp_home):
    assert temp_home.exists()

if __name__ == "__main__":
    if "pytest" not in sys.modules or "pytest.pytest_source" not in dir():
        sys.exit(pytest.main([__file__, "-v"]))
```

Key points:
- The `dependencies` in the script header ensures pytest is available when run via `./test_file.py`
- The main guard uses a simple check to avoid nesting pytest when collected by an external pytest run
- Tests can be run via `./test_file.py` (uses uv to run) or `uv run --with pytest pytest test_file.py`
