Clone this repo into a subdirectory of `~/.claude/`, then run the setup script. It will write `~/.claude/CLAUDE.md` with references pointing to the correct files in the repo, backing up any existing `CLAUDE.md` first.

```sh
git clone https://github.com/tearne/agents ~/.claude/agents
cd ~/.claude/agents && ./setup.py
```

The repo can be cloned into any subdirectory name under `~/.claude/` — the setup script detects its own location and writes the correct paths.
