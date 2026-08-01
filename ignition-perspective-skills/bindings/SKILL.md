---
name: bindings
description: Perspective binding types (HTTP Binding, Session Properties, Expression Structure Binding). Use ONLY when Query, Tag, Expression, Property, or Tag History bindings do not fit the need.
---

# Perspective Bindings (Shared)

This skill covers the binding types. Each has its own file in this folder. **Read the specific binding file below for the authoritative schema before generating any binding JSON.**

## Bindings

| Binding | File | When to Use |
|---|---|---|
| HTTP Binding | `Perspective HTTP Binding.md` | Connect a property to a REST API endpoint |
| Session Properties | `Perspective Session Properties.md` | Access session/user information |
| Expression Structure Binding | `Perspective Expression Structure Binding.md` | Build an object/array from an expression |

## Frequently Used Bindings (use their individual skills instead)

| Binding | Skill to Load |
|---|---|
| Query Binding | `perspective-query-binding` |
| Tag Binding | `perspective-tag-binding` |
| Expression Binding | `perspective-expression-binding` |
| Property Binding | `perspective-property-binding` |
| Tag History Binding | `perspective-tag-history-binding` |

## Instructions

1. Confirm the needed binding is NOT one of the frequently used five above.
2. Read the corresponding binding file in this folder (e.g., `Read Perspective HTTP Binding.md`).
3. Use ONLY the properties and values documented in that file.
