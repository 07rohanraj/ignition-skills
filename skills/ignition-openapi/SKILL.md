---
name: ignition-openapi
description: Use this skill when the user asks about Gateway APIs, needs to find an API endpoint, or wants to understand how to interact with the Ignition Gateway via REST. Contains the full OpenAPI specification for searching.
---

# Ignition Gateway API Discovery

## What This Skill Contains

- `openapi.json` - Full OpenAPI specification for the Ignition Gateway (12MB)

## How to Use

When the user asks about Gateway APIs, REST endpoints, or how to do something via the Gateway API:

1. Search `openapi.json` using grep for the keyword (e.g., "tag", "alarm", "project")
2. Read the relevant section to find the endpoint, method, and parameters
3. Provide the user with the API details

## Quick Reference

```bash
# Search for APIs
grep -i "keyword" skills/ignition-openapi/openapi.json

# Count total endpoints
grep -c '"paths"' skills/ignition-openapi/openapi.json
```

## Common API Patterns

| Task | Search Term | Likely Endpoint Pattern |
|------|-------------|------------------------|
| Read/browse tags | `tag` | `/system/tag/...` |
| Alarms | `alarm` | `/system/alarm/...` |
| Projects | `project` | `/system/webdev/projects/...` |
| Database | `db` | `/system/db/...` |
| OPC-UA | `opc` | `/system/opc/...` |
| Sessions | `session` | `/system/session/...` |
| Gateway info | `gateway` | `/system/gateway/...` |
| Users/roles | `user` | `/system/user/...` |

## Response Format

When reporting API findings, include:
- HTTP method (GET, POST, PUT, DELETE)
- Full path
- Required parameters
- Brief description if available
