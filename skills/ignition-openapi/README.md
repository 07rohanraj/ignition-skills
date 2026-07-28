# Ignition Gateway OpenAPI

API discovery and exploration for Ignition Gateway REST APIs.

## Files

| File | Description |
|------|-------------|
| `openapi.json` | Full OpenAPI specification (auto-generated) |
| `api-explorer.py` | Search and explore APIs |
| `fetch-openapi.py` | Download the OpenAPI spec |

## Quick Start

```bash
# 1. Fetch the OpenAPI spec (run once)
python fetch-openapi.py --token YOUR_API_TOKEN

# 2. Search for APIs
python api-explorer.py --search "tag"
python api-explorer.py --search "alarm"
python api-explorer.py --list-tags

# 3. Get details for a specific API
python api-explorer.py --get /system/tag/{provider}/browse
```

## API Categories

| Category | Search Term | Description |
|----------|-------------|-------------|
| Tags | `tag` | Tag read/write/browse |
| Alarms | `alarm` | Alarm status/acknowledge |
| Projects | `project` | Project management |
| Database | `db` | Database connections |
| OPC | `opc` | OPC-UA servers |
| Sessions | `session` | Perspective sessions |
| Gateway | `gateway` | Gateway info/config |
| Users | `user` | User/role management |

## Examples

```bash
# List all tag-related APIs
python api-explorer.py --list-tags

# Search for anything with "write"
python api-explorer.py --search "write"

# Count total APIs
python api-explorer.py --count

# List everything
python api-explorer.py --list-all
```
