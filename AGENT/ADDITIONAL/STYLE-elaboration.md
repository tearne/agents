# Coding Style: Examples and References

## 1. Orchestration functions read like prose

```
# Hard to scan — implementation detail mixed with flow
function main():
    open "config.json" and parse it into config
    for each line in "data.csv":
        split and validate the line, append to records
    send records and api_key to API

# Reads like a summary — details are one level down
function main():
    config = load_config()
    records = parse_input_data()
    send_to_api(records, config)
```

- *Clean Code*, Chapter 3 — Robert C. Martin (the Stepdown Rule)
- *Smalltalk Best Practice Patterns* — Kent Beck (Composed Method Pattern)
- [Composed Method on c2 wiki](https://wiki.c2.com/?ComposedMethod)

---

## 2. One abstraction level per function

- *Clean Code*, Chapter 3 — Robert C. Martin (SLAP)
- *Principles of OOD* — Robert C. Martin (SRP)
- [Single Level of Abstraction on c2 wiki](https://wiki.c2.com/?SingleLevelOfAbstraction)

---

## 3. Modules organised by domain concept

- *Clean Architecture* — Robert C. Martin (component cohesion)
- *Domain-Driven Design* — Eric Evans (bounded contexts and modules)
- [Package by Feature (vs. Layer)](https://philipcalcado.com/2019/09/23/package-by-feature.html)

---

## 4. Names communicate intent

- *Clean Code*, Chapter 2 — Robert C. Martin (Meaningful Names)
- *Domain-Driven Design* — Eric Evans (Ubiquitous Language)

---

## 5. Comments explain *why*, not *what*

```python
# ❌ Restates the code — adds nothing
i += 1  # increment i

# ❌ Comment is redundant — the code is already self-evident
# if the list is empty, return early
if len(items) == 0:
    return

# ❌ Comment is doing the naming job — extract and name instead
# check if the discount applies
if user.subscription == "premium" and order.total > 100:

# ✅ Condition named — comment gone
if user.qualifies_for_discount(order):

# ✅ Explains a non-obvious constraint
# Offset by 1 because the API uses 1-based pagination
page = requested_page + 1

# ✅ Records a decision that would otherwise look like a mistake
# Intentionally not caching here — responses vary per user session
result = fetch_live(user_id)
```

- *Clean Code*, Chapter 4 — Robert C. Martin (Comments)
- *The Art of Readable Code* — Dustin Boswell & Trevor Foucher
