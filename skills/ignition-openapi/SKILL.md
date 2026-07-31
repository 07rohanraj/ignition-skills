---
name: ignition-openapi
description: Use this skill when the user asks about Gateway APIs, needs to find an API endpoint, or wants to understand how to interact with the Ignition Gateway via REST. Contains the full OpenAPI specification for searching.
---

# Ignition Gateway API Discovery

## What This Skill Contains

- `openapi.json` - Full OpenAPI specification for the Ignition Gateway (12MB)

## Configuration

API calls require Gateway host and token. Configuration is shared at project root:

```
ignition-skills/
├── config.json          # Your config (gitignored)
├── config.example.json  # Template
```

**Setup:**
1. Copy `config.example.json` to `config.json`
2. Add your Gateway host and API token
3. Never commit `config.json` (it's gitignored)

**Environment variables (alternative):**
- `IGNI_HOST` - Gateway URL
- `IGNI_TOKEN` - API token

## How to Use

When the user asks about Gateway APIs, REST endpoints, or how to do something via the Gateway API:

1. Search `openapi.json` for the keyword to find relevant endpoints
2. Read the matching section to get endpoint details (method, path, parameters)
3. Provide the user with the API details

## Search Syntax

**PowerShell:**
```powershell
Select-String -Path "skills\ignition-openapi\openapi.json" -Pattern '"keyword' -CaseSensitive:$false
```

**Read endpoint details:** Use the Read tool with offset to view the relevant lines.

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
