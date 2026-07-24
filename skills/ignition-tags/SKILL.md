---
name: ignition-tags
description: Create, export, and manage Ignition tags via the Gateway REST API. Supports Memory, Expression, OPC, Query tags, Folders, and User-Defined Types (UDTs).
---

# Ignition Tags Skill

---

## CRITICAL RULES — READ BEFORE PROCEEDING

1. **NEVER guess tag JSON structures.** Always load the relevant tag-type skill first to get the correct schema.

2. **ALWAYS validate JSON before importing.** Malformed JSON can corrupt the tag provider.

3. **ALWAYS use environment variables for authentication.** Never hardcode API tokens.

4. **Back up before bulk operations.** Warn the user before importing large numbers of tags.

---

## Prerequisites

### Environment Variables

The following environment variables must be set:

```bash
IGNI_HOST    # Gateway URL (e.g., http://localhost:8088)
IGNI_TOKEN   # API token from Gateway > Platform > Security > API Keys
```

### Python Dependencies

```bash
pip install requests
```

---

## How to Use

1. Identify what tags the user wants to create
2. Find the matching tag type(s) below
3. Load ONLY the relevant tag-type skill(s)
4. Generate the tag JSON following the skill's schema exactly
5. Save JSON to a temp file in the workspace
6. Run the import script
7. Report results to the user

---

## Tag Types Reference

| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `ignition-tag-memory` | Creating memory tags (setpoints, internal values) | `tag-types/Memory Tag.md` |
| `ignition-tag-expression` | Creating expression tags (calculated values) | `tag-types/Expression Tag.md` |
| `ignition-tag-opc` | Creating OPC-UA tags (PLC data) | `tag-types/OPC Tag.md` |
| `ignition-tag-query` | Creating SQL query tags (database values) | `tag-types/Query Tag.md` |
| `ignition-tag-folder` | Creating tag folders (organization) | `tag-types/Folder.md` |
| `ignition-tag-udt` | Creating UDT definitions and instances | `tag-types/UDT.md` |

---

## Common Tasks

| Task | Load These Skills |
|------|-------------------|
| Create memory tags | `ignition-tag-memory` |
| Create expression tags | `ignition-tag-expression` |
| Create OPC tags from PLC | `ignition-tag-opc` |
| Create SQL query tags | `ignition-tag-query` |
| Organize tags in folders | `ignition-tag-folder` |
| Create reusable tag templates | `ignition-tag-udt` |
| Create UDT instances | `ignition-tag-udt` |
| Bulk create motor tags | `ignition-tag-udt`, `ignition-tag-opc` |
| Export existing tags | Use `scripts/export-tags.py` |

---

## API Reference

### Import Tags

```
POST /data/api/v1/tags/import
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| provider | string | Yes | Tag provider name (e.g., "default") |
| path | string | No | Root path for import |
| type | string | Yes | "json", "xml", or "csv" |
| collisionPolicy | string | Yes | "Abort", "Overwrite", "Rename", "Ignore", "MergeOverwrite" |

### Export Tags

```
GET /data/api/v1/tags/export
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| provider | string | Yes | Tag provider name |
| path | string | No | Root path to export |
| type | string | Yes | "json" or "xml" |
| recursive | boolean | No | Export sub-folders (default: true) |
| includeUdts | boolean | No | Include UDT definitions (default: true) |

---

## Scripts

### Import Tags

```bash
python scripts/import-tags.py --file tags.json --provider default --path "" --collision Overwrite
```

### Export Tags

```bash
python scripts/export-tags.py --provider default --path "Motors" --output exported-tags.json
```

---

## Collision Policies

| Policy | Description |
|--------|-------------|
| `Abort` | Stop import if any tag already exists |
| `Overwrite` | Replace existing tags with imported ones |
| `Rename` | Rename imported tags to avoid conflicts |
| `Ignore` | Skip tags that already exist |
| `MergeOverwrite` | Merge properties, overwriting existing values |

---

## Quick Examples

### Create a Memory Tag

```json
{
  "name": "Setpoint",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "Float8",
  "value": 100.0
}
```

### Create an OPC Tag

```json
{
  "name": "MotorAmps",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[Device]Motor/Amps"
}
```

### Create a Folder

```json
{
  "name": "Motors",
  "tagType": "Folder",
  "tags": []
}
```

### Create a UDT Definition

```json
{
  "name": "Motor",
  "tagType": "UdtType",
  "tags": [
    {"name": "Amps", "tagType": "AtomicTag", "valueSource": "opc", "opcItemPath": "ns=1;s=[PLC]Amps"},
    {"name": "HOA", "tagType": "AtomicTag", "valueSource": "opc", "opcItemPath": "ns=1;s=[PLC]HOA"}
  ]
}
```

---

## Important Notes

1. **Tag Paths:** Use `[provider]path/to/tag` format (e.g., `[default]Motors/Motor1`)

2. **OPC Item Paths:** Use `ns=1;s=[Device]path/to/tag` format for OPC-UA

3. **Data Types:** Common types include `Boolean`, `Int4`, `Int8`, `Float4`, `Float8`, `String`, `DateTime`

4. **UDT Instances:** Override OPC paths per instance using parameter bindings

5. **Expression Syntax:** Use `{[.]TagName}` for relative references, `{[~]Path/Tag}` for provider-relative

---

*This skill handles tag creation via the Ignition Gateway REST API. For Perspective view creation, use the `perspective-master` skill.*
