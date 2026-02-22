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
    repo_claude_md = pathlib.Path(__file__).parent.resolve() / "CLAUDE.md"
    claude_md = pathlib.Path.home() / ".claude" / "CLAUDE.md"

    if claude_md.is_symlink() and claude_md.resolve() == repo_claude_md:
        print(f"{claude_md} is already correctly symlinked.")
        return

    backed_up = backup_if_exists(claude_md)
    claude_md.unlink(missing_ok=True)
    subprocess.run(f"ln -s '{repo_claude_md}' '{claude_md}'", shell=True)
    print(f"Symlinked {claude_md} -> {repo_claude_md}")
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
