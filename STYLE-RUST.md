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
- Prefer `impl Trait` in function signatures over `dyn Trait` where the type is known at compile time
- Use `dyn Trait` when runtime polymorphism is genuinely needed (e.g. pluggable audio sources)

### ❌ Don't
- Define a trait for a concept that has only one implementation and no foreseeable variation
- Use traits as a substitute for a module boundary — a well-structured module with `pub`/private visibility often suffices
- Add blanket impls without considering the effect on readability of trait resolution

### When `dyn Trait` is appropriate
Audio pipelines (sources, filters, sinks) are a legitimate use case for `dyn Trait`: the chain is assembled at runtime and each stage is interchangeable. The trait should describe the *contract* of that stage, not expose its internals.

---

## Summary Table

| Principle | Rust Concern | Guidance |
|---|---|---|
| 3 (Modules) | Visibility as boundary | Default private; widen deliberately |
| 6 (Errors) | Domain error types | `thiserror` at boundaries; `anyhow` at app layer |
| 7 (Ownership) | `Arc`/`clone` as design smells | Match ownership semantics to real data relationships |
| 8 (Traits) | Abstraction vs indirection | Traits for real variation; `dyn` for runtime polymorphism |
