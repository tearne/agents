#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.12.*"
# ///

import os
import sys
import pathlib
import subprocess
from datetime import datetime

if not (os.environ.get("VIRTUAL_ENV") or os.environ.get("UV_INTERNAL__PARENT_INTERPRETER")):
    print("Error: run this script via './setup.py', not directly.")
    sys.exit(1)


def main():
    repo_dir = pathlib.Path(__file__).parent.resolve()
    claude_dir = pathlib.Path.home() / ".claude"

    try:
        rel_path = repo_dir.relative_to(claude_dir)
    except ValueError:
        print(f"Error: repo must be checked out somewhere under {claude_dir}/")
        print(f"  Current location: {repo_dir}")
        sys.exit(1)

    content = f"@{rel_path}/DEFINITIONS.md\n@{rel_path}/POS.md\n"
    claude_md = claude_dir / "CLAUDE.md"

    backup_if_exists(claude_md)

    claude_md.write_text(content)
    print(f"Written {claude_md}:")
    for line in content.splitlines():
        print(f"  {line}")


# --- utilities ---

def backup_if_exists(path):
    if path.exists():
        backup = path.parent / f"{path.stem}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}{path.suffix}"
        subprocess.run(f"cp '{path}' '{backup}'", shell=True)
        print(f"Backed up existing {path.name} to {backup.name}")


main()
