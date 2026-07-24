# Query Tag

## Description

Query tags execute SQL queries against a database and use the result as the tag value. They can reference other tags to build dynamic queries.

## JSON Structure

```json
{
  "name": "TagName",
  "tagType": "AtomicTag",
  "valueSource": "query",
  "dataType": "DataType",
  "expression": "SQL query string",
  "database": "DatabaseName",
  "enabled": true,
  "documentation": "Optional description"
}
```

## Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Tag name |
| `tagType` | string | Always `"AtomicTag"` |
| `valueSource` | string | Always `"query"` |
| `expression` | string | SQL query to execute |
| `database` | string | Database connection name |

## Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `dataType` | string | `"Float8"` | Output data type |
| `enabled` | boolean | `true` | Whether tag is active |
| `documentation` | string | `""` | Tag description |
| `engineeringUnit` | string | `""` | Engineering units |
| `tagGroup` | string | `"Default"` | Tag group/scan class |
| `queryType` | string | `"SingleValue"` | Query result type |

## Query Types

| QueryType | Description | Result |
|-----------|-------------|--------|
| `SingleValue` | Returns single value | Scalar |
| `DataSet` | Returns full result set | Dataset/Array |

## SQL Query Syntax

### Static Query

```sql
SELECT value FROM table WHERE id = 1
```

### Dynamic Query with Tag References

```sql
SELECT value FROM table WHERE equipment_id = '{[~]Config/EquipmentID}'
```

### Tag Reference Syntax in Queries

| Syntax | Description |
|--------|-------------|
| `{[.]TagName}` | Relative to current folder |
| `{[~]Path/Tag}` | Relative to provider root |
| `{[provider]Path/Tag}` | Specific provider |

## Examples

### Simple Lookup

```json
{
  "name": "EquipmentStatus",
  "tagType": "AtomicTag",
  "valueSource": "query",
  "dataType": "String",
  "expression": "SELECT status FROM equipment WHERE equipment_id = 'PUMP-001'",
  "database": "ProductionDB"
}
```

### Dynamic Query with Tag Reference

```json
{
  "name": "LastCalibrationDate",
  "tagType": "AtomicTag",
  "valueSource": "query",
  "dataType": "DateTime",
  "expression": "SELECT calibration_date FROM calibrations WHERE equipment_id = '{[~]Config/EquipmentID}' ORDER BY calibration_date DESC LIMIT 1",
  "database": "ProductionDB"
}
```

### Numeric Query

```json
{
  "name": "TargetSetpoint",
  "tagType": "AtomicTag",
  "valueSource": "query",
  "dataType": "Float8",
  "expression": "SELECT setpoint FROM recipes WHERE recipe_name = '{[~]Config/Recipe}' AND parameter = 'Temperature'",
  "database": "ProductionDB",
  "engineeringUnit": "degF"
}
```

### Count Query

```json
{
  "name": "ActiveAlarms",
  "tagType": "AtomicTag",
  "valueSource": "query",
  "dataType": "Int4",
  "expression": "SELECT COUNT(*) FROM alarms WHERE acknowledged = 0 AND equipment_id = '{[.]EquipmentID}'",
  "database": "ProductionDB"
}
```

### Status Lookup with Join

```json
{
  "name": "OperatorName",
  "tagType": "AtomicTag",
  "valueSource": "query",
  "dataType": "String",
  "expression": "SELECT o.name FROM operators o INNER JOIN shifts s ON o.shift_id = s.id WHERE s.is_active = 1",
  "database": "ProductionDB"
}
```

## Database Requirements

Before creating query tags:

1. Database connection is configured in Gateway > Databases
2. Database name matches the `database` property
3. SQL query is valid for the database type
4. Ignition service account has read permissions

## Performance Considerations

| Consideration | Recommendation |
|---------------|----------------|
| Query Frequency | Controlled by tag group/scan class |
| Query Complexity | Keep queries simple and indexed |
| Result Size | Use `LIMIT` for large result sets |
| Caching | Consider using memory tags for static data |

## Common Use Cases

| Use Case | Description |
|----------|-------------|
| Configuration | Read settings from database |
| Recipes | Load recipe parameters |
| Calibration | Get calibration history |
| Status | Look up equipment status |
| Alarms | Count active alarms |

---

*For direct device communication, see `OPC Tag.md`. For internal values, see `Memory Tag.md`.*
