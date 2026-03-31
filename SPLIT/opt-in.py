#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

import argparse
import json
import os
import sys
from pathlib import Path

from rich.console import Console

VERSION = "1.0.0"

console = Console()

AGENTS_DIR = Path.home() / "agents" / "SPLIT"


def main():
    parser = argparse.ArgumentParser(
        description="Opt a project in to the split planner/builder system."
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.parse_args()

    project_root = Path.cwd()
    console.print(f"Setting up split system in [bold]{project_root}[/bold]\n")

    create_file(
        project_root / "CLAUDE.md",
        f"@{AGENTS_DIR}/SUPERVISOR/README.md\n",
    )
    create_settings(
        project_root / ".claude" / "settings.local.json",
        excludes=["~/.claude/CLAUDE.md"],
    )
    create_file(
        project_root / "planner" / "CLAUDE.md",
        f"@{AGENTS_DIR}/PLANNER/README.md\n",
    )
    create_settings(
        project_root / "planner" / ".claude" / "settings.local.json",
        excludes=["~/.claude/CLAUDE.md", "../CLAUDE.md"],
    )
    create_file(
        project_root / "builder" / "CLAUDE.md",
        f"@{AGENTS_DIR}/BUILDER/README.md\n",
    )
    create_settings(
        project_root / "builder" / ".claude" / "settings.local.json",
        excludes=["~/.claude/CLAUDE.md", "../CLAUDE.md"],
    )

    for folder in ["changes/planning", "changes/ready", "changes/feedback", "changes/interrupted", "changes/archive"]:
        create_dir(project_root / folder)

    update_gitignore(project_root / ".gitignore")

    console.print("\n[bold green]Done.[/bold green] Run [bold]claude[/bold] from the project root to continue setup.")


def create_file(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text() == content:
            report("already present", path)
        else:
            report("conflict", path, "exists with different content — left untouched")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    report("created", path)


def create_settings(path: Path, excludes: list[str]) -> None:
    desired = {"claudeMdExcludes": excludes}
    if path.exists():
        try:
            existing = json.loads(path.read_text())
        except json.JSONDecodeError:
            report("conflict", path, "could not parse JSON — left untouched")
            return
        if "claudeMdExcludes" in existing:
            if existing["claudeMdExcludes"] == excludes:
                report("already present", path)
            else:
                report("conflict", path, "claudeMdExcludes already set to a different value — left untouched")
            return
        # Merge into existing JSON rather than overwriting
        existing["claudeMdExcludes"] = excludes
        path.write_text(json.dumps(existing, indent=2) + "\n")
        report("updated", path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(desired, indent=2) + "\n")
    report("created", path)


def create_dir(path: Path) -> None:
    if path.exists():
        report("already present", path)
        return
    path.mkdir(parents=True, exist_ok=True)
    report("created", path)


def update_gitignore(path: Path) -> None:
    entries = ["CLAUDE.md", "planner/", "builder/"]
    content = path.read_text() if path.exists() else ""
    to_add = [e for e in entries if e not in content.splitlines()]
    if not to_add:
        report("already present", path)
        return
    block = "\n".join(to_add)
    separator = "\n" if content and not content.endswith("\n") else ""
    with path.open("a") as f:
        f.write(separator + block + "\n")
    report("updated", path, f"added: {', '.join(to_add)}")


def report(status: str, path: Path, note: str = "") -> None:
    colours = {"created": "green", "updated": "cyan", "already present": "dim", "conflict": "yellow"}
    colour = colours.get(status, "white")
    label = f"[{colour}]{status:<15}[/{colour}]"
    detail = f"  [dim]{note}[/dim]" if note else ""
    console.print(f"  {label} {path}{detail}")


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './opt-in' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    main()
