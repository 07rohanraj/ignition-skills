# OPC Tag

## Description

OPC tags read values directly from PLCs or other OPC-UA devices. They subscribe to data and update automatically when the device value changes.

## JSON Structure

```json
{
  "name": "TagName",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[Device]path/to/tag",
  "enabled": true,
  "documentation": "Optional description"
}
```

## Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Tag name |
| `tagType` | string | Always `"AtomicTag"` |
| `valueSource` | string | Always `"opc"` |
| `opcServer` | string | OPC server name |
| `opcItemPath` | string | OPC item path |

## Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `dataType` | string | auto-detected | Force data type |
| `enabled` | boolean | `true` | Whether tag is active |
| `readOnly` | boolean | `false` | Prevent writes |
| `documentation` | string | `""` | Tag description |
| `engineeringUnit` | string | `""` | Engineering units |
| `scaleMode` | string | `"none"` | Scaling mode |
| `rawLow` | number | `0` | Raw low for scaling |
| `rawHigh` | number | `100` | Raw high for scaling |
| `scaledLow` | number | `0` | Scaled low |
| `scaledHigh` | number | `100` | Scaled high |
| `clampMode` | string | `"none"` | Clamp mode |
| `deadband` | number | `0` | Deadband value |
| `deadbandMode` | string | `"off"` | Deadband mode |
| `historyEnabled` | boolean | `false` | Log to history |
| `historyProvider` | string | `""` | History provider name |
| `tagGroup` | string | `"Default"` | Tag group/scan class |

## OPC Item Path Formats

### OPC-UA Format (Recommended)

```
ns=1;s=[DeviceName]path/to/tag
```

| Part | Description | Example |
|------|-------------|---------|
| `ns=1` | Namespace index (usually 1) | `ns=1` |
| `s=` | String identifier | `s=` |
| `[DeviceName]` | Device connection name | `[PLC1]` |
| `path/to/tag` | Tag path in device | `Motor/Amps` |

### Examples

| Device | Path | Full OPC Item Path |
|--------|------|-------------------|
| PLC1 | Motor/Amps | `ns=1;s=[PLC1]Motor/Amps` |
| PLC1 | Tank/Level | `ns=1;s=[PLC1]Tank/Level` |
| Kepware | Channel1.Device1.Tag1 | `ns=1;s=[Kepware]Channel1.Device1.Tag1` |
| Modbus | 40001 | `ns=1;s=[ModbusTCP]40001` |

## Examples

### Simple OPC Tag

```json
{
  "name": "MotorAmps",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[PLC1]Motor/Amps"
}
```

### OPC Tag with Scaling

```json
{
  "name": "TankLevel",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[PLC1]Tank/LevelRaw",
  "scaleMode": "linear",
  "rawLow": 0,
  "rawHigh": 4095,
  "scaledLow": 0,
  "scaledHigh": 100,
  "engineeringUnit": "%"
}
```

### Read-Only OPC Tag

```json
{
  "name": "MotorStatus",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[PLC1]Motor/Status",
  "readOnly": true
}
```

### OPC Tag with History

```json
{
  "name": "ProcessTemp",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[PLC1]Temp/Sensor1",
  "historyEnabled": true,
  "historyProvider": "MySQL",
  "engineeringUnit": "degF"
}
```

### Boolean OPC Tag

```json
{
  "name": "MotorRunning",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[PLC1]Motor/Running",
  "dataType": "Boolean"
}
```

### String OPC Tag

```json
{
  "name": "AlarmMessage",
  "tagType": "AtomicTag",
  "valueSource": "opc",
  "opcServer": "Ignition OPC UA Server",
  "opcItemPath": "ns=1;s=[PLC1]Alarm/Message",
  "dataType": "String"
}
```

## Common Data Types

| PLC Data | Recommended DataType |
|----------|---------------------|
| Digital/Bool | `Boolean` |
| 16-bit Int | `Int2` |
| 32-bit Int | `Int4` |
| Float | `Float4` or `Float8` |
| String | `String` |
| DateTime | `DateTime` |

## Device Connection

Before creating OPC tags, ensure:

1. Device is configured in Gateway > Devices
2. Device name matches the `[DeviceName]` in the OPC item path
3. Device is connected and communicating

## Scaling Options

| scaleMode | Description |
|-----------|-------------|
| `"none"` | No scaling |
| `"linear"` | Linear interpolation between raw/scaled values |
| `"power"` | Power curve scaling |

---

*For internal values, see `Memory Tag.md`. For calculated values, see `Expression Tag.md`.*
