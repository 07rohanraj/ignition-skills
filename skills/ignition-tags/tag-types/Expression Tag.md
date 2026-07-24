# Expression Tag

## Description

Expression tags calculate their value from an expression that can reference other tags, perform math, and run logic. They are read-only (cannot be written to directly).

## JSON Structure

```json
{
  "name": "TagName",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "DataType",
  "expression": "expression string",
  "enabled": true,
  "documentation": "Optional description"
}
```

## Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Tag name |
| `tagType` | string | Always `"AtomicTag"` |
| `valueSource` | string | Always `"expression"` |
| `expression` | string | The expression to evaluate |

## Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `dataType` | string | `"Float8"` | Output data type |
| `enabled` | boolean | `true` | Whether tag is active |
| `documentation` | string | `""` | Tag description |
| `engineeringUnit` | string | `""` | Engineering units |
| `opcWriteBackServer` | string | `""` | OPC server for writeback |
| `opcWriteBackPath` | string | `""` | OPC item path for writeback |

## Expression Syntax

### Tag References

| Syntax | Description | Example |
|--------|-------------|---------|
| `{[.]TagName}` | Relative to current folder | `{[.]Setpoint}` |
| `{[~]Path/Tag}` | Relative to provider root | `{[~]Motors/Motor1/Amps}` |
| `{[provider]Path/Tag}` | Specific provider | `{[default]Setpoint}` |

### Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `{[.]A} + {[.]B}` |
| `-` | Subtraction | `{[.]A} - {[.]B}` |
| `*` | Multiplication | `{[.]A} * 2` |
| `/` | Division | `{[.]A} / {[.]B}` |
| `%` | Modulo | `{[.]A} % 2` |
| `^` | Power | `{[.]A} ^ 2` |

### Functions

| Function | Description | Example |
|----------|-------------|---------|
| `if(cond, true, false)` | Conditional | `if({[.]Temp} > 100, 1, 0)` |
| `abs(x)` | Absolute value | `abs({[.]Value})` |
| `min(a, b)` | Minimum | `min({[.]A}, {[.]B})` |
| `max(a, b)` | Maximum | `max({[.]A}, {[.]B})` |
| `round(x)` | Round to integer | `round({[.]Value})` |
| `sqrt(x)` | Square root | `sqrt({[.]Value})` |
| `sin(x)` | Sine (radians) | `sin({[.]Angle})` |
| `cos(x)` | Cosine (radians) | `cos({[.]Angle})` |
| `tag(path)` | Read tag value | `tag('[~]Other/Tag')` |

## Examples

### Temperature Conversion (F to C)

```json
{
  "name": "TempCelsius",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "Float8",
  "expression": "({[~]Sensors/TempF} - 32) * 5/9",
  "engineeringUnit": "degC"
}
```

### Temperature Conversion (C to F)

```json
{
  "name": "TempFahrenheit",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "Float8",
  "expression": "{[~]Sensors/TempC} * 9/5 + 32",
  "engineeringUnit": "degF"
}
```

### Percentage Calculation

```json
{
  "name": "LevelPercent",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "Float8",
  "expression": "({[~]Tank/Level} / {[~]Tank/MaxLevel}) * 100",
  "engineeringUnit": "%"
}
```

### Conditional Logic

```json
{
  "name": "AlarmState",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "String",
  "expression": "if({[~]Sensor/High} = 1, 'HIGH', if({[~]Sensor/Low} = 1, 'LOW', 'OK'))"
}
```

### Math with Multiple Tags

```json
{
  "name": "TotalFlow",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "Float8",
  "expression": "{[~]Flow/Line1} + {[~]Flow/Line2} + {[~]Flow/Line3}",
  "engineeringUnit": "gpm"
}
```

### Scaling

```json
{
  "name": "ScaledValue",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "Float8",
  "expression": "({[.]RawValue} - {[.]RawLow}) / ({[.]RawHigh} - {[.]RawLow}) * ({[.]ScaledHigh} - {[.]ScaledLow}) + {[.]ScaledLow}"
}
```

### Writeback to OPC

```json
{
  "name": "ComputedSetpoint",
  "tagType": "AtomicTag",
  "valueSource": "expression",
  "dataType": "Float8",
  "expression": "{[~]Input/Value} * {[~]Config/Gain}",
  "opcWriteBackServer": "Ignition OPC UA Server",
  "opcWriteBackPath": "ns=1;s=[PLC]Setpoint"
}
```

## Use Cases

| Use Case | Description |
|----------|-------------|
| Unit Conversion | Convert between engineering units |
| Calculations | Totals, averages, percentages |
| Logic | State machines, conditional values |
| Scaling | Raw to engineering value conversion |
| Derived Values | Combine multiple tag values |

---

*For tags that read directly from PLC, see `OPC Tag.md`. For internal values, see `Memory Tag.md`.*
