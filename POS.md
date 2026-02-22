# Python Orchestrated Script (POS)
The POS style helps Python take the place of native shell scripts. It strategically breaks some Python idioms to combine the different strengths of Python and shell scripts, such as favouring subprocess calls for shell commands while using Python control flow.

POS guidance:
- Prefer `subprocess` for shell commands; use Python for control flow. This makes commands easy to discover and copy-paste into a terminal.
    - Examples:
        - To download the latest version of the `helix` `deb` for `amd64`:
        ```py
        subprocess.run(r"""curl -s https://api.github.com/repos/helix-editor/helix/releases/latest | grep -oP '"browser_download_url": "\K[^"]*amd64.deb' | xargs wget""")
        ```
        - To apt install `curl`:
        ```py
        subprocess.run("""DEBIAN_FRONTEND=noninteractive apt-get install -y curl""")
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
- Key functions at the top of the file (easy to comment out or jump to); utility functions at the bottom.
- Use a "main guard" at the bottom of the file. Include the `uv`/venv check here — it is an invocation-mode concern, not business logic — before calling `main()`:
    ```py
    if __name__ == "__main__":
        if not os.environ.get("VIRTUAL_ENV"):
            print("Error: no virtual environment detected. Run this script via './<script-name>' (requires uv), or activate a virtual environment first.")
            sys.exit(100)
        main()
    ```
- Prefer built-in libraries to maximise future compatibility. Suggested (when relevant): `argparse`, `getpass`, `os`, `pathlib`, `shutil`, `subprocess`, `sys`, `time`. Pre-approved external: `rich`. Other third-party libraries may be proposed if they are mainstream or would significantly enhance readability.
