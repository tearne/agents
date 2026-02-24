#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.12.*"
# ///

import os
import sys
import pathlib
import subprocess
from datetime import datetime


def setup():
    repo_dir = pathlib.Path(__file__).parent.resolve()
    claude_md = pathlib.Path.home() / ".claude" / "CLAUDE.md"

    content = f"""\
@{repo_dir}/PROCESS.md
@{repo_dir}/POS.md
"""

    if claude_md.exists() and not claude_md.is_symlink() and claude_md.read_text() == content:
        print(f"{claude_md} already contains the correct content.")
        return

    backed_up = backup_if_exists(claude_md)
    claude_md.unlink(missing_ok=True)
    claude_md.write_text(content)
    print(f"Wrote {claude_md}")
    if backed_up:
        print("Warning: a pre-existing CLAUDE.md was backed up — review it to check for content that should be preserved.")


# --- utilities ---

def backup_if_exists(path):
    if path.exists() or path.is_symlink():
        backup = path.parent / f"{path.stem}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        subprocess.run(f"cp -P '{path}' '{backup}'", shell=True)
        print(f"Backed up existing {path.name} to {backup.name}")
        return True
    return False


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './setup.py' (requires uv), or activate a virtual environment first.")
        sys.exit(1)
    setup()
