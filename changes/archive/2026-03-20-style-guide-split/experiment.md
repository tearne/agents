# Experiment: Style Guide Split
**Status: Adopted**

## Question
Can `STYLE.md` be split into a terse agent-optimised version and a separate human-readable version, and is maintaining both worth the overhead?

## Log

Produced two companion files: `STYLE-agent.md` (30 lines, rules only) and `STYLE-human.md` (elaboration: examples and references under matching headings). The human version was initially framed as audience-specific but reframed as an *elaboration* — not restricted to humans, just the next level of detail.

Established a naming convention: `*-elaboration.md` files are companions to their guide. An agent need not load them unless it judges additional context is required. The convention is stated once in the craft index; from there it is self-describing by filename. This avoids the alternative (frontmatter), which would require opening a file to know it shouldn't be opened.

## Outcome

Successful. The split works well — `STYLE-agent.md` is concise enough for routine agent use, and `STYLE-elaboration.md` provides examples and references under matching numbered headings without duplicating the rules. The elaboration file was renamed from `STYLE-human.md` to reflect that it is not audience-specific but simply the next level of detail. The pattern is worth adopting across all craft guides as part of the broader structural proposal.
