# Coding Style Guide: Rust Addendum

Rust-specific extensions to [STYLE.md](./STYLE.md). The five core principles apply as written; this addendum covers areas where Rust's type system, ownership model, or idioms create additional considerations.

---

## Principle 3 Extension: Module Visibility as an API Boundary

Rust's visibility system (`pub`, `pub(crate)`, `pub(super)`) is a first-class tool for enforcing encapsulation. Use it deliberately.

### ✅ Do
- Default to the most restrictive visibility that works — start private, widen only when needed
- Use `pub(crate)` for items that are internal infrastructure, not public API
- Treat a module's `pub` surface as its contract; keep it minimal and stable
- Re-export selectively from `lib.rs` / `mod.rs` to present a clean external API

### ❌ Don't
- `pub` everything to silence compiler warnings — that's a sign of a missing abstraction boundary
- Let `mod.rs` become a pass-through that re-exports everything from every submodule
- Mix public API items and internal helpers at the same visibility level in the same module

---

## Principle 6: Error Types Reflect Domain, Not Implementation

Error handling is a first-class design concern in Rust. The shape of your error types communicates what can go wrong at each layer of the system.

### ✅ Do
- Define domain error types (`enum AudioError`, `enum CacheError`) at module boundaries
- Use `thiserror` for library-style errors; use `anyhow` for application-level aggregation
- Propagate with `?` freely — it is idiomatic and not an abstraction violation
- Convert between error types at layer boundaries, not deep inside implementations

### ❌ Don't
- Use `Box<dyn Error>` or `anyhow` throughout — it erases information that callers may need
- Define a single monolithic `AppError` that lists every possible failure across all modules
- Panic (`unwrap`, `expect`) in paths that are reachable at runtime; reserve for invariants that *cannot* fail by construction

### Note on `expect`
`expect("message")` is preferable to `unwrap()` — the message documents the invariant being assumed. Name the invariant, not the symptom: prefer `expect("mixer is initialised before playback starts")` over `expect("should not be None")`.

---

## Principle 7: Ownership Signals Design

In Rust, how data flows through the system (owned, borrowed, reference-counted) reflects — and should match — the intended ownership semantics. Friction in ownership is often a signal of a design problem, not a borrow checker problem.

### ✅ Do
- Prefer owned types in structs that clearly *own* their data
- Use borrows (`&`, `&mut`) at function boundaries where the callee does not need ownership
- Reach for `Arc<Mutex<T>>` only when shared mutable ownership is genuinely required
- Treat widespread `clone()` calls as a code smell worth investigating — they may indicate unclear ownership

### ❌ Don't
- Add `Arc<Mutex<T>>` to resolve borrow conflicts before understanding why the conflict exists
- Clone to avoid lifetime annotations — lifetimes communicate real constraints
- Mix owned and borrowed variants of the same concept in the same abstraction layer

### The multi-ownership tell
If a type needs to be behind `Arc` to be usable at all, ask whether it represents a *resource* (correct — shared ownership is real) or whether the design has created false shared dependencies (worth restructuring).

---

## Principle 8: Traits Define Behaviour, Not Convenience

Traits are Rust's primary abstraction mechanism. Used well, they define clean interfaces between layers. Used carelessly, they add indirection without clarity.

### ✅ Do
- Define a trait when you have (or anticipate) multiple concrete implementations of the same behaviour
- Keep trait methods at a consistent abstraction level (see Principle 2)
- Default to generics (`impl Trait` / `fn foo<T: Trait>`) — monomorphization is zero-cost and keeps the variant set explicit
- Reach for `dyn Trait` only when the variant set is open or cannot be closed at compile time

### ❌ Don't
- Define a trait for a concept that has only one implementation and no foreseeable variation
- Use traits as a substitute for a module boundary — a well-structured module with `pub`/private visibility often suffices
- Add blanket impls without considering the effect on readability of trait resolution
- Treat "this is chosen at runtime" as sufficient justification for `dyn Trait` — a config-selected variant is still a closed set

### When `dyn Trait` is appropriate
The question is not "is this chosen at runtime?" but "is the variant set open?" Plugin systems, user-supplied callbacks, and chains assembled from external inputs are legitimate uses — the concrete type genuinely cannot be known at compile time. When the set of variants is fixed in the codebase, prefer monomorphization (see Principle 11).

---

## Principle 9: Test Support Modules

When a source file needs to expose test-only types or helpers to other modules, group them in a single `#[cfg(test)] pub(crate) mod test_support { ... }` block rather than scattering `#[cfg(test)]` gates across individual items.

### ✅ Do
- Collect all test-only exports into one `test_support` block per file
- Use `pub(crate)` visibility for items inside the block
- Place the block alongside `mod tests`, at the bottom of the file

### ❌ Don't
- Gate individual items with `#[cfg(test)]` when they need to be visible outside the file
- Mix test helpers into the public API to avoid cfg gating

### Why
This mirrors the convention for `mod tests`, keeps test-only code visually distinct, and means the cfg gate appears exactly once per file regardless of how many helpers are exported.

---

## Principle 10: Serde Config Conventions

Config types deserve extra rigour at deserialisation boundaries — mistakes here produce silent misbehaviour rather than compile errors.

### ✅ Do
- Apply `#[serde(deny_unknown_fields)]` to all config structs — makes unrecognised keys a deserialisation error rather than a silent no-op
- Use internally-tagged enums (`#[serde(tag = "...")]`) for config types that select between named variants with associated parameters
- Name the tag field after the domain concept being selected (e.g. `"model"`, `"strategy"`) — follows Principle 4

### ❌ Don't
- Omit `deny_unknown_fields` — typos and removed fields will silently use defaults instead of failing
- Use untagged or adjacently-tagged enums for config unless there is a specific reason — internally-tagged is the most readable in config files

### The key rule
`deny_unknown_fields` is the most important of these — it catches typos and version drift at the boundary where config enters the system.

---

## Principle 11: Runtime-to-Static Dispatch

Where a component is selected at runtime (e.g. via config) but the variant set is closed and known at compile time, bridge with a single `match` at startup that routes into separate monomorphized codepaths.

```rust
match config.model {
    Model::Seir => run::<SeirModel>(config),
    Model::Sir  => run::<SirModel>(config),
}
```

This keeps hot-path overhead at zero while the selection logic remains in one visible place.

### ✅ Do
- Perform the dispatch `match` once at startup, outside the hot path
- Make the generic function the real entry point — it receives the concrete type and owns all subsequent logic
- Treat this as the default when the variant set is closed (see Principle 8)

### ❌ Don't
- Reach for `Box<dyn Trait>` simply because selection happens at runtime — that conflates *when* with *whether*
- Repeat the dispatch match in multiple places — a single match at the boundary is the point

---

## Summary Table

| Principle | Rust Concern | Guidance |
|---|---|---|
| 3 (Modules) | Visibility as boundary | Default private; widen deliberately |
| 6 (Errors) | Domain error types | `thiserror` at boundaries; `anyhow` at app layer |
| 7 (Ownership) | `Arc`/`clone` as design smells | Match ownership semantics to real data relationships |
| 8 (Traits) | Abstraction vs indirection | Monomorphization by default; `dyn` only for open variant sets |
| 9 (Test support) | Test-only exports | One `#[cfg(test)] pub(crate) mod test_support` block per file |
| 10 (Serde) | Config deserialisation | `deny_unknown_fields` always; internally-tagged enums |
| 11 (Dispatch) | Runtime selection, zero overhead | Closed variant sets: single startup `match` into generic codepaths |
