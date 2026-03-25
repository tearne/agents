#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.12.*"
# ///

import os
import shutil
import sys
import pathlib
import subprocess
from datetime import datetime


def setup():
    repo_dir = pathlib.Path(__file__).parent.resolve()

    claude_installed = is_claude_installed()
    opencode_installed = is_opencode_installed()

    if not claude_installed and not opencode_installed:
        print("Warning: Neither Claude Code nor OpenCode appears to be installed.")
        print("Skipping configuration.")
        return

    if claude_installed:
        setup_claude(repo_dir)
    else:
        print("Claude Code not detected — skipping configuration.")

    if opencode_installed:
        setup_opencode(repo_dir)
    else:
        print("OpenCode not detected — skipping configuration.")


def is_claude_installed():
    return shutil.which("claude") is not None


def is_opencode_installed():
    return shutil.which("opencode") is not None


def setup_claude(repo_dir):
    claude_dir = pathlib.Path.home() / ".claude"
    claude_dir.mkdir(parents=True, exist_ok=True)
    claude_md = claude_dir / "CLAUDE.md"
    content = f"""\
Before writing or editing any project file, the current change must be recorded in `changes/open/active.md`. The following are always permitted without an active change:
- Reading any project file
- Writing or editing files inside `changes/`

Do not make any change management decision — starting, pausing, advancing, or archiving a change — without explicit user instruction.

See `AGENT/PROCESS/README.md` for the change process.

@{repo_dir}/AGENT/README.md
"""

    if claude_md.exists() and claude_md.read_text() == content:
        print(f"{claude_md} already contains the correct content.")
        return

    backed_up = backup_if_exists(claude_md)
    claude_md.unlink(missing_ok=True)
    claude_md.write_text(content)
    print(f"Wrote {claude_md}")
    if backed_up:
        print(
            "Warning: a pre-existing CLAUDE.md was backed up — review it to check for content that should be preserved."
        )


def setup_opencode(repo_dir):
    config_dir = pathlib.Path.home() / ".config" / "opencode"
    agents_md = config_dir / "AGENTS.md"

    config_dir.mkdir(parents=True, exist_ok=True)

    content = f"""\
Before writing or editing any project file, the current change must be recorded in `changes/open/active.md`. The following are always permitted without an active change:
- Reading any project file
- Writing or editing files inside `changes/`

Do not make any change management decision — starting, pausing, advancing, or archiving a change — without explicit user instruction.

See `AGENT/PROCESS/README.md` for the change process.

@{repo_dir}/AGENT/README.md
"""

    if agents_md.exists() and agents_md.read_text() == content:
        print(f"{agents_md} already contains the correct content.")
        return

    backed_up = backup_if_exists(agents_md)
    agents_md.unlink(missing_ok=True)
    agents_md.write_text(content)
    print(f"Wrote {agents_md}")
    if backed_up:
        print(
            "Warning: a pre-existing AGENTS.md was backed up — review it to check for content that should be preserved."
        )


# --- utilities ---


def backup_if_exists(path):
    if path.exists():
        backup = (
            path.parent
            / f"{path.stem}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        )
        subprocess.run(f"cp -P '{path}' '{backup}'", shell=True)
        print(f"Backed up existing {path.name} to {backup.name}")
        return True
    return False


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print(
            "Error: no virtual environment detected. Run this script via './setup.py' (requires uv), or activate a virtual environment first."
        )
        sys.exit(1)
    setup()
