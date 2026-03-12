# Coding Style Guide: Readable Abstraction Layers

Follow this guide to write code that communicates intent clearly, regardless of language.

## Core Philosophy

Code is read far more often than it is written. Structure should reveal intent at every level of the call stack.


## Principle 1: Orchestration Functions Read Like Prose

**Also known as:** The Stepdown Rule, Composed Method Pattern, Intention-Revealing Names

Top-level functions — entry points and high-level coordinators — should read almost like pseudocode. A reader should understand the overall flow without reading any function body.

### ✅ Do
- Name functions after *what* they accomplish, not *how* they work
- Keep orchestration functions free of implementation detail
- Aim for a reading level of "table of contents" at the top level
- Make each function call self-documenting: `validate_inputs()`, `load_config()`, `generate_report()`

### ❌ Don't
- Inline logic in orchestration functions, even when it's short
- Use vague names like `process()`, `handle()`, `do_thing()`
- Write comments explaining *what* code does — the function name should do that
- Mix abstraction levels within a single function (coordinating *and* implementing)

### Example

```
# ❌ Hard to scan — implementation detail mixed with flow
function main():
    open "config.json" and parse it into config
    for each line in "data.csv":
        split and validate the line, append to records
    send records and api_key to API

# ✅ Reads like a summary — details are one level down
function main():
    config = load_config()
    records = parse_input_data()
    send_to_api(records, config)
```

### Further Reading
- *Clean Code*, Chapter 3 — Robert C. Martin (the Stepdown Rule)
- *Smalltalk Best Practice Patterns* — Kent Beck (Composed Method Pattern)
- [Composed Method on c2 wiki](https://wiki.c2.com/?ComposedMethod)

---

## Principle 2: One Level of Abstraction Per Function

**Also known as:** Single Level of Abstraction Principle (SLAP), Single Responsibility Principle (SRP)

Each function should either *coordinate* steps or *implement* a step — not both. Mixing abstraction levels is a key source of hard-to-read code.

### ✅ Do
- Extract even small operations if naming them adds clarity
- Keep functions short enough to fit on a screen without scrolling
- Ensure every statement in a function operates at the same conceptual level

### ❌ Don't
- Justify inline logic with "it's only 5 lines" or "it's only used once"
- Allow a function to both call other functions *and* do raw computation
- Nest multiple levels of logic inside a single function body

### Further Reading
- *Clean Code*, Chapter 3 — Robert C. Martin (SLAP)
- *Principles of OOD* — Robert C. Martin (SRP; originally about classes, applies to functions too)
- [Single Level of Abstraction on c2 wiki](https://wiki.c2.com/?SingleLevelOfAbstraction)

---

## Principle 3: Modules Organised by Domain Concept

**Also known as:** Cohesion, Package by Feature, Domain-Driven Design (DDD) modules

When many small functions exist, they should be grouped by the *concept* they belong to, not by their code type. A reader should be able to predict which file to open based on what they're looking for.

### ✅ Do
- Name modules after domain concepts: `ingestion`, `validation`, `reporting`, `auth`
- Group functions that change for the same reasons
- Use module structure to communicate the architecture of the system

### ❌ Don't
- Create catch-all modules: `utils`, `helpers`, `misc`, `common`
- Organise by code type alone: `functions.py`, `classes.py`, `constants.py`
- Let modules grow without asking "does this still belong here?"

### Further Reading
- *Clean Architecture* — Robert C. Martin (component cohesion)
- *Domain-Driven Design* — Eric Evans (bounded contexts and modules)
- [Package by Feature (vs. Layer)](https://philipcalcado.com/2019/09/23/package-by-feature.html)

---

## Principle 4: Names Communicate Intent

**Also known as:** Intention-Revealing Names, Ubiquitous Language

Naming is the primary tool for communication in code. A well-named function or variable removes the need for a comment.

### ✅ Do
- Use names that answer "what does this do?" or "what does this represent?"
- Use domain language — the vocabulary your stakeholders use
- Prefer longer, descriptive names over short, cryptic ones

### ❌ Don't
- Use abbreviations that save typing but cost reading (`usr`, `cfg`, `proc`)
- Use comments to explain what a name should already convey
- Use technical names (`manager`, `processor`, `handler`) where a domain name exists

### Further Reading
- *Clean Code*, Chapter 2 — Robert C. Martin (Meaningful Names)
- *Domain-Driven Design* — Eric Evans (Ubiquitous Language)

---

## Principle 5: Comments Explain *Why*, Not *What*

Code shows what is happening. Comments should explain *why* — the rationale, constraints, or non-obvious context that can't be expressed in code.

### ✅ Do
- Comment on business rules, gotchas, and trade-offs
- Explain *why* a surprising or counterintuitive approach was chosen
- Reference tickets, specs, or decisions that motivated the code

### ❌ Don't
- Write comments that restate what the code clearly shows
- Let comments substitute for a better name or cleaner structure
- Leave outdated comments — they actively mislead

### Further Reading
- *Clean Code*, Chapter 4 — Robert C. Martin (Comments)
- *The Art of Readable Code* — Dustin Boswell & Trevor Foucher

---

## Summary Table

| Principle | Common Name | Primary Reference |
|---|---|---|
| Top-level reads like pseudocode | Stepdown Rule / Composed Method | *Clean Code* Ch. 3 |
| One abstraction level per function | SLAP / SRP | *Clean Code* Ch. 3 |
| Modules organised by domain | Package by Feature / Cohesion | *Clean Architecture* |
| Names communicate intent | Intention-Revealing Names | *Clean Code* Ch. 2 |
| Comments explain why, not what | — | *Clean Code* Ch. 4 |

---

## Recommended Reading

1. **Clean Code** — Robert C. Martin. The most direct reference for most of these principles.
2. **The Art of Readable Code** — Boswell & Foucher. Practical, example-driven, language-agnostic.
3. **Smalltalk Best Practice Patterns** — Kent Beck. Origin of the Composed Method pattern; foundational thinking on small functions.
4. **Clean Architecture** — Robert C. Martin. Extends these principles to module and system structure.
5. **Domain-Driven Design** — Eric Evans. For naming that reflects the problem domain rather than the implementation.
