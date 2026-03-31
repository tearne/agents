# Getting Started

## Opt a project in to the split system

**1. Create `CLAUDE.md` at the project root:**
```markdown
@/root/agents/SPLIT/SUPERVISOR/README.md
```

**2. Create `.claude/settings.local.json` at the project root:**
```json
{
  "claudeMdExcludes": ["~/.claude/CLAUDE.md"]
}
```

**3. Run the opt-in script from the project root:**
```sh
~/agents/SPLIT/opt-in.py
```

Then run `claude` — the supervisor will verify the setup and guide any remaining steps.

## Starting a planning session

```sh
cd planner && claude
```

## Starting a build session

```sh
cd builder && claude
```

The builder will refuse to start if a build is already in progress (`changes/building/` is non-empty). Ask the supervisor for help if a previous builder was interrupted.
