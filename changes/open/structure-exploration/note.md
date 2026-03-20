# Note: Structural Exploration — Conciseness and Selective Loading

## Context
As the repo grows, always-loading everything becomes expensive (context window cost) and unwieldy (harder to read and reason about). The current structure doesn't distinguish between things that are always relevant and things that are only relevant to certain languages or project types.

## Emerging Shape

Three distinct concerns are already present:

- **Rules** — non-negotiable constraints, always relevant, should stay lean: `BEHAVIOUR.md`, `VERSIONING.md`
- **Craft** — how to build things well: `STYLE.md`, `STYLE-RUST.md`, `POS.md`, and future additions. These are reference guides, often language- or paradigm-specific.
- **Process** — how to manage change: `PROCESS/`. Already has its own directory and entry-point pattern.

## Key Tensions

**Two audiences, opposite needs:**
- **Human readers** — benefit from rationale, examples, further reading, and motivation
- **AI agents** — need terse, actionable constraints; rationale is mostly redundant

These pull in opposite directions on document length and style.

**Growability vs digestibility:**
A large repository of guidance carries its own risk — humans won't read it, won't encapsulate it, and won't build on it. The structure needs to be digestible enough that a human can hold the shape of it in their head, and growable enough that new guidance slips in naturally without requiring a restructure. If the system can only be understood by reading all of it, it has already failed.

## Promising Directions

**Craft as opt-in pool:** Craft documents become opt-in per project or change, rather than always loaded. The user explicitly flags which guides apply. This could be a per-project config (e.g. `CLAUDE.md` @-references) or a setup convention. This mirrors how `PROCESS/README.md` acts as a lightweight entry point with detail files consulted on demand — applied more broadly.

**Folder structure reflects loading priority:** If always-loaded items are few and concentrated in one place, both humans and agents know immediately where to focus. A possible shape:
- A root-level core (always loaded) — terse rules, process entry point, and an index of available craft guides
- `PROCESS/` — detail files, entered via the always-loaded entry point
- `CRAFT/` — pool of opt-in guides, known about via the index but not loaded until opted into

This makes the "what really matters" question answerable by looking at one directory, and makes growth natural — new craft guides slot into the pool without touching the always-loaded core.

**Hierarchical entry points, each with a stated purpose:** Two levels is the right starting point — deep enough to separate concerns, shallow enough to maintain. Each index or README file should open with a single sentence stating the one question it is there to answer. This keeps entry points honest and prevents them drifting into catch-all documents. `PROCESS/README.md` already follows this pattern and can serve as the model. A `CRAFT/README.md` would do the same for the craft pool — one sentence per guide, enough to make the opt-in decision without reading the guide itself. Deeper levels can be introduced if a clear need emerges, but should not be anticipated.

## Open Questions
- Do craft guides need a terse "agent summary" alongside the human-readable version, or can they be restructured to serve both? (See experiment: `style-guide-split` — resolved in favour of a naming convention: `*-elaboration.md` companion files, loaded only when the agent judges additional context is needed)
- Does VERSIONING belong in core, or is it a craft concern?

## Key Insight: File Boundaries, Not Sections
Sections within a document don't control agent context cost — the agent reads the whole file regardless. The only lever is the file boundary: a file is either loaded or it isn't. This means a document cannot simultaneously serve as a terse agent constraint file and a human learning resource. `STYLE.md` currently attempts both. These may need to be separate files — one optimised for agents, one for humans — with the question of whether the maintenance burden of two versions is worth it left to be judged empirically.

## Resolved
**Where does opt-in happen?** It doesn't need a mechanism — it's a convention. When a craft guide is relevant, the user names it in the spec, proposal, or wherever the context lives. The agent loads it from there. This is already how things work in practice (e.g. POS is named explicitly when needed). The `CRAFT/README.md` index supports discovery, but the opt-in act itself is human and informal.
