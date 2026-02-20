The following illustrates how to download a file from this repo and reference it from an AI agent configuration file (e.g. `CLAUDE.md` for Claude Code):

```
curl -o DEFINITIONS.md https://raw.githubusercontent.com/tearne/agents/main/DEFINITIONS.md
printf '\n\n# Definitions\n@DEFINITIONS.md\n' >> CLAUDE.md
```
