#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.12.*"
# dependencies = ["pytest"]
# ///

import pathlib
import sys
import tempfile
from unittest.mock import patch, MagicMock

import pytest


@pytest.fixture
def temp_home():
    with tempfile.TemporaryDirectory() as td:
        yield pathlib.Path(td)


@pytest.fixture
def mock_home(temp_home):
    with patch("pathlib.Path.home", return_value=temp_home):
        yield temp_home


@pytest.fixture
def reload_setup():
    import importlib
    import setup

    importlib.reload(setup)
    return setup


def test_is_claude_installed_when_not_installed(mock_home, reload_setup):
    from setup import is_claude_installed

    with patch("shutil.which", return_value=None):
        result = is_claude_installed()
    assert result is False


def test_is_claude_installed_when_installed(mock_home, reload_setup):
    from setup import is_claude_installed

    with patch("shutil.which", return_value="/usr/bin/claude"):
        result = is_claude_installed()
    assert result is True


def test_is_opencode_installed_when_not_installed(mock_home, reload_setup):
    from setup import is_opencode_installed

    with patch("shutil.which", return_value=None):
        result = is_opencode_installed()
    assert result is False


def test_is_opencode_installed_when_installed(mock_home, reload_setup):
    from setup import is_opencode_installed

    with patch("shutil.which", return_value="/usr/bin/opencode"):
        result = is_opencode_installed()
    assert result is True


def test_setup_claude_creates_directory(mock_home, temp_home, capsys, reload_setup):
    import setup

    repo_dir = pathlib.Path("/fake/repo")
    with patch("shutil.which", return_value="/usr/bin/claude"):
        setup.setup_claude(repo_dir)

    claude_md = mock_home / ".claude" / "CLAUDE.md"
    assert claude_md.exists()
    content = claude_md.read_text()
    assert f"@{repo_dir}/PROCESS.md" in content
    assert f"@{repo_dir}/POS.md" in content


def test_setup_claude_preserves_existing_different(
    mock_home, temp_home, capsys, reload_setup
):
    import setup

    (mock_home / ".claude").mkdir()
    existing = mock_home / ".claude" / "CLAUDE.md"
    existing.write_text("old content")

    repo_dir = pathlib.Path("/fake/repo")
    with patch("shutil.which", return_value="/usr/bin/claude"):
        with patch.object(setup, "backup_if_exists", return_value=True):
            setup.setup_claude(repo_dir)

    content = existing.read_text()
    assert f"@{repo_dir}/PROCESS.md" in content


def test_setup_opencode_creates_agents_md(mock_home, temp_home, capsys, reload_setup):
    import setup

    repo_dir = pathlib.Path("/fake/repo")
    with patch("shutil.which", return_value="/usr/bin/opencode"):
        setup.setup_opencode(repo_dir)

    agents_md = mock_home / ".config" / "opencode" / "AGENTS.md"
    assert agents_md.exists()
    content = agents_md.read_text()
    assert f"@{repo_dir}/PROCESS.md" in content
    assert f"@{repo_dir}/POS.md" in content


def test_setup_warns_when_neither_installed(mock_home, temp_home, capsys, reload_setup):
    import setup

    with patch("shutil.which", return_value=None):
        setup.setup()

    captured = capsys.readouterr()
    assert "Warning: Neither Claude Code nor OpenCode" in captured.out
    assert "Skipping configuration" in captured.out


def test_setup_warns_when_only_claude_installed(
    mock_home, temp_home, capsys, reload_setup
):
    import setup

    def mock_which(cmd):
        if cmd == "claude":
            return "/usr/bin/claude"
        return None

    with patch("shutil.which", side_effect=mock_which):
        with patch.object(setup, "setup_claude"):
            setup.setup()

    captured = capsys.readouterr()
    assert "OpenCode not detected" in captured.out


def test_setup_warns_when_only_opencode_installed(
    mock_home, temp_home, capsys, reload_setup
):
    import setup

    def mock_which(cmd):
        if cmd == "opencode":
            return "/usr/bin/opencode"
        return None

    with patch("shutil.which", side_effect=mock_which):
        with patch.object(setup, "setup_opencode"):
            setup.setup()

    captured = capsys.readouterr()
    assert "Claude Code not detected" in captured.out


if __name__ == "__main__":
    if "pytest" not in sys.modules or "pytest.pytest_source" not in dir():
        sys.exit(pytest.main([__file__, "-v"]))
