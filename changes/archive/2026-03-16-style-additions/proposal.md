# Proposal: Style Additions
**Status: Approved**

## Intent
Three conventions introduced during the configurable-disease-models change are not yet documented in `STYLE-RUST.md`. Capturing them together keeps the guide current and ensures they are applied consistently going forward.

## Scope
- **In scope**: add three new sections to `STYLE-RUST.md`
- **Out of scope**: changes to existing style guidance

## Specification Deltas

### ADDED

- **Test support modules** — Where a source file needs to expose test-only types or helpers to other modules, group them in a single `#[cfg(test)] pub(crate) mod test_support { ... }` block rather than scattering `#[cfg(test)]` gates across individual items. This mirrors the convention for `mod tests`, keeps test-only code visually distinct, and means the cfg gate appears once per file. Items inside use `pub(crate)` visibility.

- **Serde config conventions** — Apply `#[serde(deny_unknown_fields)]` to all config structs to make unrecognised keys a deserialisation error rather than a silent no-op. For config enums that select between named variants with associated parameters, use internally-tagged representation (`#[serde(tag = "...")]`); the tag name should follow Principle 4 and reflect the domain concept being selected (e.g. `"model"`, `"strategy"`). The key rule is `deny_unknown_fields` — it catches typos and version drift at the boundary.

- **Runtime-to-static dispatch** — Where a component is selected at runtime via config but the variant set is closed and known at startup, bridge with a single `match` that routes into separate monomorphized codepaths (e.g. `run::<ConcreteImpl>(...)`). This keeps hot-path overhead at zero. `dyn Trait` should be treated as an opt-in that requires justification — it is appropriate when the variant set is open, unknown at compile time, or assembled dynamically (e.g. a plugin system). When in doubt, start with monomorphization.

### MODIFIED

- **Principle 8 — `dyn Trait` guidance**: reframe `dyn Trait` from a natural choice for runtime polymorphism to an explicit opt-in. Monomorphization (generics / `impl Trait`) is the default; `dyn Trait` is reached for only when the variant set cannot be closed at compile time. The "When `dyn Trait` is appropriate" note should reflect this: the question is not "is this runtime?" but "is the variant set open?"
