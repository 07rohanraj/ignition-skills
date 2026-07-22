# Ignition Named Query

**When to Use:** Creating, modifying, or understanding Named Queries in an Ignition Perspective project. This covers the directory structure, file schemas, query types, parameter definitions, and how to call them from Python scripts.

---

## Directory Structure

Named queries are stored under `ignition/named-query/` in the project directory. Each query is a folder containing exactly two files:

```
ignition/
  named-query/
    <Category>/
      <QueryName>/
        resource.json    <- Metadata, config, parameters
        query.sql        <- The SQL statement
```

Categories are project-specific groupings (e.g., Dashboard, Users, Reports). Choose names that match your project's domain.

---

## resource.json Schema

Every named query has a `resource.json` with this structure:

### Queries WITHOUT parameters:

```json
{
  "scope": "DG",
  "version": 2,
  "restricted": false,
  "overridable": true,
  "files": [
    "query.sql"
  ],
  "attributes": {
    "useMaxReturnSize": false,
    "autoBatchEnabled": false,
    "fallbackValue": "",
    "maxReturnSize": 100,
    "cacheUnit": "SEC",
    "type": "Query",
    "enabled": true,
    "cacheAmount": 1,
    "cacheEnabled": false,
    "database": "<DatabaseName>",
    "fallbackEnabled": false,
    "lastModificationSignature": "<64-char-hex-string>",
    "permissions": [
      {
        "zone": "",
        "role": ""
      }
    ],
    "lastModification": {
      "actor": "admin",
      "timestamp": "<ISO-8601-UTC>"
    }
  }
}
```

### Queries WITH parameters:

Same as above, plus a `"parameters"` array inside `"attributes"`:

```json
{
  "scope": "DG",
  "version": 2,
  "restricted": false,
  "overridable": true,
  "files": [
    "query.sql"
  ],
  "attributes": {
    "useMaxReturnSize": false,
    "autoBatchEnabled": false,
    "fallbackValue": "",
    "maxReturnSize": 100,
    "cacheUnit": "SEC",
    "type": "Query",
    "enabled": true,
    "cacheAmount": 1,
    "cacheEnabled": false,
    "database": "<DatabaseName>",
    "fallbackEnabled": false,
    "lastModificationSignature": "<64-char-hex-string>",
    "permissions": [
      {
        "zone": "",
        "role": ""
      }
    ],
    "lastModification": {
      "actor": "admin",
      "timestamp": "<ISO-8601-UTC>"
    },
    "parameters": [
      {
        "type": "Parameter",
        "identifier": "<paramName>",
        "sqlType": <sqlTypeNumber>
      }
    ]
  }
}
```

### Field Reference

| Field | Value | Notes |
|-------|-------|-------|
| `scope` | `"DG"` | Design/Gateway scope. Observed as `"DG"` in all queries. |
| `version` | `2` | Always 2 in observed queries. |
| `restricted` | `false` | Whether the query is restricted. |
| `overridable` | `true` | Whether the query can be overridden. |
| `files` | `["query.sql"]` | Always this exact value. |
| `attributes.type` | `"Query"` or `"UpdateQuery"` | See Query Types below. |
| `attributes.enabled` | `true` | Whether the query is active. |
| `attributes.database` | `"<DatabaseName>"` | Must match a configured DB connection name. |
| `attributes.maxReturnSize` | `100` | Max rows returned. |
| `attributes.cacheEnabled` | `false` | Whether results are cached. |
| `attributes.cacheAmount` | `1` | Cache duration (when enabled). |
| `attributes.cacheUnit` | `"SEC"` | Cache time unit. |
| `attributes.fallbackEnabled` | `false` | Whether fallback value is used on error. |
| `attributes.fallbackValue` | `""` | Fallback value (empty string). |
| `attributes.autoBatchEnabled` | `false` | Whether auto-batching is enabled. |
| `attributes.useMaxReturnSize` | `false` | Whether to enforce max return size. |
| `attributes.permissions` | `[{"zone":"","role":""}]` | Always one entry with empty zone/role. |
| `attributes.lastModification.actor` | `"admin"` | Who last modified. |
| `attributes.lastModification.timestamp` | ISO-8601 UTC | When last modified. |
| `attributes.lastModificationSignature` | 64-char hex | Integrity signature. |

---

## Query Types

### `"type": "Query"`
For SELECT statements (read operations). Returns a dataset.

**Example query.sql:**
```sql
SELECT
    Col1,
    Col2,
    Col3
FROM MyTable
WHERE IsActive = 1
ORDER BY Col2;
```

### `"type": "UpdateQuery"`
For INSERT, UPDATE, DELETE statements (write operations). Returns update count.

**Example query.sql:**
```sql
INSERT INTO MyTable
(
    Col1,
    Col2,
    Col3,
    IsActive
)
VALUES
(
    :Col1,
    :Col2,
    :Col3,
    1
);
```

---

## Parameter Definitions

Parameters are defined in the `parameters` array inside `resource.json` attributes. Each parameter has:

```json
{
  "type": "Parameter",
  "identifier": "<paramName>",
  "sqlType": <sqlTypeNumber>
}
```

### SQL Type Numbers (observed)

| sqlType | SQL Server Type | Typical Use |
|---------|----------------|-------------|
| `2` | `INT` / `INTEGER` | Keys, IDs, boolean flags |
| `3` | `BIGINT` | Large ID values |
| `4` | `FLOAT` / `REAL` | Threshold values, percentages |
| `5` | `DECIMAL` | Precise numeric values |
| `7` | `VARCHAR` / `NVARCHAR` | Names, descriptions, text |

### Parameter Naming Convention
- Use PascalCase for parameter identifiers
- The `identifier` must match the `:paramName` used in the SQL

---

## SQL Syntax Patterns

### Parameters in SQL
Parameters are referenced with a colon prefix: `:paramName`

```sql
SELECT * FROM MyTable WHERE PrimaryKey = :key
```

### Common SQL Patterns

**Soft delete pattern (IsActive flag):**
```sql
WHERE IsActive = 1
```

**Insert with auto-timestamp:**
```sql
INSERT INTO MyTable (Col1, Col2, DateOfInsert, InsertedBy, IsActive)
VALUES (:Col1, :Col2, GETDATE(), :InsertedBy, 1);
```

**Update with auto-timestamp:**
```sql
UPDATE MyTable
SET
    Col1 = :Col1,
    Col2 = :Col2,
    LastModifiedDate = GETDATE(),
    ModifiedBy = :ModifiedBy
WHERE PrimaryKey = :PrimaryKey;
```

**Delete:**
```sql
DELETE FROM MyTable WHERE PrimaryKey = :PrimaryKey;
```

**Insert with conditional existence check:**
```sql
INSERT INTO TargetTable (Col1, Col2)
SELECT
    src.Col1,
    src.Col2
FROM SourceTable src
WHERE src.Col1 = :Col1
AND NOT EXISTS (
    SELECT 1 FROM TargetTable t
    WHERE t.Col1 = src.Col1
);
```

**Aggregate with CASE for status counts:**
```sql
SELECT
    COUNT(*) AS Total,
    SUM(CASE WHEN StatusKey = 1 THEN 1 ELSE 0 END) AS Status1Count,
    SUM(CASE WHEN StatusKey = 2 THEN 1 ELSE 0 END) AS Status2Count
FROM MyTable
WHERE IsActive = 1;
```

**Join pattern:**
```sql
SELECT
    t1.PrimaryKey,
    t1.Name,
    t2.Name AS RelatedName
FROM MainTable t1
INNER JOIN LookupTable t2
    ON t1.ForeignKey = t2.PrimaryKey
WHERE t1.IsActive = 1;
```

---

## Calling Named Queries from Python Scripts

### Without Parameters
```python
result = system.db.runNamedQuery("Category/QueryName")
```

### With Parameters
```python
result = system.db.runNamedQuery("Category/QueryName", {
    "paramName": paramValue
})
```

### Multiple Parameters
```python
result = system.db.runNamedQuery("Category/QueryName", {
    "Param1": value1,
    "Param2": value2
})
```

### Converting to PyDataSet
```python
dataset = system.db.runNamedQuery("Category/QueryName")
pyData = system.dataset.toPyDataSet(dataset)

for row in pyData:
    print(row["ColumnName"])
```

### Converting to List of Dicts
```python
dataset = system.db.runNamedQuery("Category/QueryName")
pyData = system.dataset.toPyDataSet(dataset)

results = []
for row in pyData:
    results.append({
        "Key": row["PrimaryKey"],
        "Name": row["Name"]
    })
```

### Safe Access with Fallback
```python
def coalesce(value, fallback):
    return fallback if value is None else value

result = system.db.runNamedQuery("Category/QueryName", {"key": value})
if len(result) == 0:
    return {"Key": "", "Name": ""}

row = result[0]
return {
    "Key": coalesce(row["PrimaryKey"], ""),
    "Name": coalesce(row["Name"], "")
}
```

---

## Creating a New Named Query - Step by Step

1. **Determine the category** — a logical grouping for the query (e.g., Dashboard, Users, Reports)
2. **Determine the query name** — use camelCase (e.g., `getItemsById`, `insertRecord`, `updateStatus`)
3. **Determine query type** — `"Query"` for SELECT, `"UpdateQuery"` for INSERT/UPDATE/DELETE
4. **Create the folder:** `ignition/named-query/<Category>/<QueryName>/`
5. **Write `query.sql`** — use `:paramName` syntax for parameters
6. **Write `resource.json`** — use the schema above (include `parameters` array if query has parameters)
7. **Set `database`** — must match your configured DB connection name in Ignition
8. **Test** — call from a script with `system.db.runNamedQuery()`

---

## Complete Examples

### Simple SELECT (no parameters)
**resource.json:**
```json
{
  "scope": "DG",
  "version": 2,
  "restricted": false,
  "overridable": true,
  "files": ["query.sql"],
  "attributes": {
    "useMaxReturnSize": false,
    "autoBatchEnabled": false,
    "fallbackValue": "",
    "maxReturnSize": 100,
    "cacheUnit": "SEC",
    "type": "Query",
    "enabled": true,
    "cacheAmount": 1,
    "cacheEnabled": false,
    "database": "MyDatabase",
    "fallbackEnabled": false,
    "lastModificationSignature": "",
    "permissions": [{"zone": "", "role": ""}],
    "lastModification": {"actor": "admin", "timestamp": "2026-01-01T00:00:00Z"}
  }
}
```
**query.sql:**
```sql
SELECT PrimaryKey, Name, Description
FROM MyTable
WHERE IsActive = 1
ORDER BY Name;
```

### SELECT with Parameters
**resource.json parameters section:**
```json
"parameters": [
  {"type": "Parameter", "identifier": "primaryKey", "sqlType": 2}
]
```
**query.sql:**
```sql
SELECT PrimaryKey, Name, Description
FROM MyTable
WHERE PrimaryKey = :primaryKey AND IsActive = 1;
```

### INSERT with Parameters
**resource.json type and parameters:**
```json
"type": "UpdateQuery",
"parameters": [
  {"type": "Parameter", "identifier": "ForeignKey", "sqlType": 2},
  {"type": "Parameter", "identifier": "Name", "sqlType": 7},
  {"type": "Parameter", "identifier": "Description", "sqlType": 7},
  {"type": "Parameter", "identifier": "InsertedBy", "sqlType": 7}
]
```
**query.sql:**
```sql
INSERT INTO MyTable (ForeignKey, Name, Description, InsertedBy, IsActive)
VALUES (:ForeignKey, :Name, :Description, :InsertedBy, 1);
```

### UPDATE with Parameters
**resource.json type and parameters:**
```json
"type": "UpdateQuery",
"parameters": [
  {"type": "Parameter", "identifier": "ForeignKey", "sqlType": 2},
  {"type": "Parameter", "identifier": "Name", "sqlType": 7},
  {"type": "Parameter", "identifier": "Description", "sqlType": 7},
  {"type": "Parameter", "identifier": "ModifiedBy", "sqlType": 7},
  {"type": "Parameter", "identifier": "PrimaryKey", "sqlType": 2}
]
```
**query.sql:**
```sql
UPDATE MyTable
SET
    ForeignKey = :ForeignKey,
    Name = :Name,
    Description = :Description,
    LastModifiedDate = GETDATE(),
    ModifiedBy = :ModifiedBy
WHERE PrimaryKey = :PrimaryKey;
```

### Aggregate Query (no parameters)
**query.sql:**
```sql
SELECT
    CategoryKey,
    CategoryName,
    COUNT(*) AS TotalItems,
    SUM(CASE WHEN StatusKey = 1 THEN 1 ELSE 0 END) AS ActiveCount,
    SUM(CASE WHEN StatusKey = 2 THEN 1 ELSE 0 END) AS InactiveCount,
    ROUND(
        SUM(CASE WHEN StatusKey = 1 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 0
    ) AS ActivePercentage
FROM MyTable
WHERE IsActive = 1
GROUP BY CategoryKey, CategoryName
ORDER BY CategoryName;
```
