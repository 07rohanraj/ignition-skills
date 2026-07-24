# Memory Tag

## Description

Memory tags are internal Ignition values used for setpoints, configuration, or storing information that doesn't come from a PLC. They are read/write and persist in the tag provider.

## JSON Structure

```json
{
  "name": "TagName",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "DataType",
  "value": initialValue,
  "enabled": true,
  "readOnly": false,
  "documentation": "Optional description"
}
```

## Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Tag name (must be unique within folder) |
| `tagType` | string | Always `"AtomicTag"` for memory tags |
| `valueSource` | string | Always `"memory"` |

## Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `dataType` | string | `"Float8"` | Data type (see below) |
| `value` | any | `0` | Initial value |
| `enabled` | boolean | `true` | Whether tag is active |
| `readOnly` | boolean | `false` | Prevent writes from sessions |
| `documentation` | string | `""` | Tag description |
| `engineeringUnit` | string | `""` | Engineering units (e.g., "psi", "degF") |
| `limitEng` | object | `{}` | Engineering value limits |
| `limitRaw` | object | `{}` | Raw value limits |
| `scaleMode` | string | `"none"` | Scaling mode |
| `tooltip` | string | `""` | Tooltip text |

## Data Types

| DataType | Description | Example Value |
|----------|-------------|---------------|
| `Boolean` | True/False | `true` |
| `Int1` | 8-bit integer | `42` |
| `Int2` | 16-bit integer | `1000` |
| `Int4` | 32-bit integer | `100000` |
| `Int8` | 64-bit integer | `1000000` |
| `Float4` | 32-bit float | `3.14` |
| `Float8` | 64-bit float | `3.14159265` |
| `String` | Text | `"Hello"` |
| `DateTime` | Date/time | `"2024-01-15T10:30:00Z"` |
| `ArrayOf*` | Array type | `[1, 2, 3]` |

## Examples

### Simple Float Setpoint

```json
{
  "name": "TemperatureSetpoint",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "Float8",
  "value": 72.5,
  "engineeringUnit": "degF"
}
```

### Boolean Flag

```json
{
  "name": "EnableAlarm",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "Boolean",
  "value": true
}
```

### String Configuration

```json
{
  "name": "DeviceName",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "String",
  "value": "Pump-001"
}
```

### Integer Counter

```json
{
  "name": "CycleCount",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "Int4",
  "value": 0,
  "readOnly": true
}
```

### Read-Only Setpoint

```json
{
  "name": "MaxPressure",
  "tagType": "AtomicTag",
  "valueSource": "memory",
  "dataType": "Float8",
  "value": 150.0,
  "readOnly": true,
  "engineeringUnit": "psi",
  "documentation": "Maximum allowable pressure"
}
```

## Use Cases

| Use Case | Description |
|----------|-------------|
| Setpoints | Operator-entered values for process control |
| Configuration | Device settings, mode selections |
| Counters | Internal counters not from PLC |
| Flags | Enable/disable features |
| Templates | Default values for UDT members |

---

*For OPC tags, see `OPC Tag.md`. For expression calculations, see `Expression Tag.md`.*
