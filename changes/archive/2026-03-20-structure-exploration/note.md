# Note: Structural Exploration — Conciseness and Selective Loading

## Context
As the repo grows, always-loading everything becomes expensive (context window cost) and unwieldy (harder to read and reason about). The current structure doesn't distinguish between things that are always relevant and things that are only relevant to certain languages or project types.

## Emerging Shape

Three distinct concerns are already present:

- **Rules** — non-negotiable constraints, always loaded: `BEHAVIOUR.md`, `STYLE.md`, `STYLE-RUST.md` *(Rust projects — the rules README notes the condition; the agent applies it from project context)*
- **Craft** — how to build things well: `POS.md`, `VERSIONING.md`, and future additions. Opt-in or prompted, never assumed.
- **Process** — how to manage change: `PROCESS/`. Already has its own directory and entry-point pattern.

Within craft, a distinction exists between **passive** and **prompted** guides:
- **Passive** — loaded when the user names them in a spec or proposal. e.g. `POS.md` — an active choice to use a specific scripting style.
- **Prompted** — the agent raises them when context suggests they are relevant, without waiting to be told. e.g. `VERSIONING.md` (agent prompts when a project is being set up, when changes are accumulating, or when a breaking change is being made). The prompted list should stay short.

## Key Tensions

**Two audiences, opposite needs:**
- **Human readers** — benefit from rationale, examples, further reading, and motivation
- **AI agents** — need terse, actionable constraints; rationale is mostly redundant

These pull in opposite directions on document length and style.

**Growability vs digestibility:**
A large repository of guidance carries its own risk — humans won't read it, won't encapsulate it, and won't build on it. The structure needs to be digestible enough that a human can hold the shape of it in their head, and growable enough that new guidance slips in naturally without requiring a restructure. If the system can only be understood by reading all of it, it has already failed.

## Promising Directions

**Craft as opt-in pool:** Craft documents become opt-in per project or change, rather than always loaded. The user explicitly flags which guides apply. This could be a per-project config (e.g. `CLAUDE.md` @-references) or a setup convention. This mirrors how `PROCESS/README.md` acts as a lightweight entry point with detail files consulted on demand — applied more broadly.

**Folder structure reflects loading priority:** If always-loaded items are few and concentrated in one place, both humans and agents know immediately where to focus. The settled shape:

```
BEHAVIOUR.md
STYLE.md
STYLE-RUST.md
ADDITIONAL/
    README.md
    POS.md
    VERSIONING.md
PROCESS/
    README.md
    PROPOSAL.md
    EXPERIMENT.md
```

Root-level files are always loaded. `ADDITIONAL/` contains guides that are beyond the core — the name signals "not automatically active" without implying the content is unimportant. `PROCESS/` remains unchanged. Growth is natural: new guides slot into `ADDITIONAL/` without touching the always-loaded root.

**Hierarchical entry points, each with a stated purpose:** Two levels is the right starting point — deep enough to separate concerns, shallow enough to maintain. Each index or README file should open with a single sentence stating the one question it is there to answer. This keeps entry points honest and prevents them drifting into catch-all documents. `PROCESS/README.md` already follows this pattern and can serve as the model. `ADDITIONAL/README.md` would do the same — one sentence per guide, enough to make the opt-in decision without reading the guide itself. Deeper levels can be introduced if a clear need emerges, but should not be anticipated.

## Open Questions
- Do craft guides need a terse "agent summary" alongside the human-readable version, or can they be restructured to serve both? (See experiment: `style-guide-split` — resolved in favour of a naming convention: `*-elaboration.md` companion files, loaded only when the agent judges additional context is needed)

## Key Insight: File Boundaries, Not Sections
Sections within a document don't control agent context cost — the agent reads the whole file regardless. The only lever is the file boundary: a file is either loaded or it isn't. This means a document cannot simultaneously serve as a terse agent constraint file and a human learning resource. `STYLE.md` currently attempts both. These may need to be separate files — one optimised for agents, one for humans — with the question of whether the maintenance burden of two versions is worth it left to be judged empirically.

## Resolved
**Where does opt-in happen?** It doesn't need a mechanism — it's a convention. When an additional guide is relevant, the user names it in the spec, proposal, or wherever the context lives. The agent loads it from there. This is already how things work in practice (e.g. POS is named explicitly when needed). `ADDITIONAL/README.md` supports discovery, but the opt-in act itself is human and informal.

**Does VERSIONING belong in core or craft?** Craft — but in the prompted subcategory. It is not always relevant (a one-off script doesn't need versioning), but it is significant enough that the agent should raise it when context warrants rather than waiting to be told.
