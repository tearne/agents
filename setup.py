#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.12.*"
# ///

import json
import os
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
    return pathlib.Path.home() / ".claude" / "CLAUDE.md"


def is_opencode_installed():
    return pathlib.Path.home() / ".config" / "opencode"


def setup_claude(repo_dir):
    claude_md = pathlib.Path.home() / ".claude" / "CLAUDE.md"
    content = f"""\
@{repo_dir}/PROCESS.md
@{repo_dir}/POS.md
"""

    if (
        claude_md.exists()
        and not claude_md.is_symlink()
        and claude_md.read_text() == content
    ):
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
    config_file = config_dir / "opencode.json"

    config_dir.mkdir(parents=True, exist_ok=True)

    instructions = [str(repo_dir / "PROCESS.md"), str(repo_dir / "POS.md")]

    existing_config = {}
    if config_file.exists():
        try:
            existing_config = json.loads(config_file.read_text())
        except json.JSONDecodeError:
            pass

    new_config = {**existing_config, "instructions": instructions}

    if existing_config.get("instructions") == instructions:
        print(f"{config_file} already contains the correct instructions.")
        return

    backup_if_exists(config_file)
    config_file.write_text(json.dumps(new_config, indent=2) + "\n")
    print(f"Wrote {config_file}")


# --- utilities ---


def backup_if_exists(path):
    if path.exists() or path.is_symlink():
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
