# User-Defined Type (UDT)

## Description

UDTs are reusable tag templates that define a structure of tags. You create a UDT definition once, then instantiate it multiple times with different parameters (e.g., multiple motors with the same structure but different OPC paths).

## Two Parts

1. **UDT Definition** (`UdtType`) - The template/structure
2. **UDT Instance** (`UdtInstance`) - An instance using the definition

---

## UDT Definition

### JSON Structure

```json
{
  "name": "TypeName",
  "tagType": "UdtType",
  "tags": [
    {
      "name": "MemberName",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcItemPath": "ns=1;s=[{equipment}]/path"
    }
  ]
}
```

### Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | UDT type name |
| `tagType` | string | Always `"UdtType"` |
| `tags` | array | Member tag definitions |

### Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `documentation` | string | `""` | Description of the UDT |
| `parameters` | array | `[]` | Parameter definitions |

---

## UDT Instance

### JSON Structure

```json
{
  "name": "InstanceName",
  "tagType": "UdtInstance",
  "typeId": "TypeName",
  "tags": [
    {
      "name": "MemberName",
      "opcItemPath": "ns=1;s=[ActualDevice]/actual/path"
    }
  ]
}
```

### Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Instance name |
| `tagType` | string | Always `"UdtInstance"` |
| `typeId` | string | Name of the UDT definition |

### Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `tags` | array | `[]` | Member overrides |
| `parameters` | object | `{}` | Parameter values |

---

## Parameter System

UDTs support parameters that allow dynamic OPC paths and values.

### Defining Parameters

```json
{
  "name": "Motor",
  "tagType": "UdtType",
  "parameters": [
    {
      "name": "equipment",
      "value": "Motor1"
    }
  ],
  "tags": [...]
}
```

### Using Parameters

Reference parameters in member tags:

```json
{
  "name": "Amps",
  "opcItemPath": "ns=1;s=[{equipment}]/Amps"
}
```

### Overriding Parameters in Instances

```json
{
  "name": "Motor2",
  "tagType": "UdtInstance",
  "typeId": "Motor",
  "parameters": {
    "equipment": "Motor2"
  }
}
```

---

## Examples

### Basic Motor UDT Definition

```json
{
  "name": "Motor",
  "tagType": "UdtType",
  "documentation": "Standard motor monitoring UDT",
  "parameters": [
    {
      "name": "device",
      "value": "PLC1"
    }
  ],
  "tags": [
    {
      "name": "Amps",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Motor/Amps",
      "engineeringUnit": "A"
    },
    {
      "name": "HOA",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Motor/HOA",
      "dataType": "Int4"
    },
    {
      "name": "Running",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Motor/Running",
      "dataType": "Boolean"
    },
    {
      "name": "Setpoint",
      "tagType": "AtomicTag",
      "valueSource": "memory",
      "dataType": "Float8",
      "value": 100.0,
      "engineeringUnit": "%"
    }
  ]
}
```

### Motor UDT Instance

```json
{
  "name": "Pump1",
  "tagType": "UdtInstance",
  "typeId": "Motor",
  "parameters": {
    "device": "PumpPLC"
  }
}
```

### Tank UDT Definition

```json
{
  "name": "Tank",
  "tagType": "UdtType",
  "documentation": "Tank monitoring with level, temperature, and alarms",
  "parameters": [
    {
      "name": "tankId",
      "value": "Tank1"
    }
  ],
  "tags": [
    {
      "name": "Level",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{tankId}]/Level",
      "engineeringUnit": "%",
      "historyEnabled": true,
      "historyProvider": "MySQL"
    },
    {
      "name": "Temperature",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{tankId}]/Temperature",
      "engineeringUnit": "degF",
      "historyEnabled": true,
      "historyProvider": "MySQL"
    },
    {
      "name": "HighAlarm",
      "tagType": "AtomicTag",
      "valueSource": "expression",
      "dataType": "Boolean",
      "expression": "{[.]Level} > 90"
    },
    {
      "name": "LowAlarm",
      "tagType": "AtomicTag",
      "valueSource": "expression",
      "dataType": "Boolean",
      "expression": "{[.]Level} < 10"
    }
  ]
}
```

### Tank UDT Instance with Overrides

```json
{
  "name": "StorageTank1",
  "tagType": "UdtInstance",
  "typeId": "Tank",
  "parameters": {
    "tankId": "StorageTank1"
  },
  "tags": [
    {
      "name": "Level",
      "opcItemPath": "ns=1;s=[TankPLC]Storage/Level"
    },
    {
      "name": "Temperature",
      "opcItemPath": "ns=1;s=[TankPLC]Storage/Temp"
    }
  ]
}
```

### Valve UDT Definition

```json
{
  "name": "Valve",
  "tagType": "UdtType",
  "documentation": "Control valve with feedback",
  "parameters": [
    {
      "name": "device",
      "value": "PLC1"
    }
  ],
  "tags": [
    {
      "name": "Command",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Valve/Cmd",
      "dataType": "Boolean"
    },
    {
      "name": "OpenFeedback",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Valve/Open",
      "dataType": "Boolean"
    },
    {
      "name": "CloseFeedback",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Valve/Close",
      "dataType": "Boolean"
    },
    {
      "name": "Position",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[{device}]/Valve/Position",
      "engineeringUnit": "%"
    }
  ]
}
```

### Multiple Instances from One Definition

```json
[
  {
    "name": "Motor1",
    "tagType": "UdtInstance",
    "typeId": "Motor",
    "parameters": {"device": "Area1_Motors"}
  },
  {
    "name": "Motor2",
    "tagType": "UdtInstance",
    "typeId": "Motor",
    "parameters": {"device": "Area1_Motors"}
  },
  {
    "name": "Motor3",
    "tagType": "UdtInstance",
    "typeId": "Motor",
    "parameters": {"device": "Area2_Motors"}
  }
]
```

---

## Complete Import Example

### UDT Definition + Instances in One File

```json
{
  "tags": [
    {
      "name": "Motor",
      "tagType": "UdtType",
      "parameters": [
        {"name": "device", "value": "PLC1"}
      ],
      "tags": [
        {
          "name": "Amps",
          "tagType": "AtomicTag",
          "valueSource": "opc",
          "opcServer": "Ignition OPC UA Server",
          "opcItemPath": "ns=1;s=[{device}]/Amps"
        },
        {
          "name": "Running",
          "tagType": "AtomicTag",
          "valueSource": "opc",
          "opcServer": "Ignition OPC UA Server",
          "opcItemPath": "ns=1;s=[{device}]/Running",
          "dataType": "Boolean"
        }
      ]
    },
    {
      "name": "Pump1",
      "tagType": "UdtInstance",
      "typeId": "Motor",
      "parameters": {"device": "Pump1"}
    },
    {
      "name": "Pump2",
      "tagType": "UdtInstance",
      "typeId": "Motor",
      "parameters": {"device": "Pump2"}
    }
  ]
}
```

---

## Best Practices

| Practice | Description |
|----------|-------------|
| Use Parameters | Make UDTs reusable with parameterized OPC paths |
| Keep Generic | Don't hardcode device names in definitions |
| Document | Add documentation to UDT definitions |
| Organize | Store UDT definitions in a dedicated folder |
| Version | Export UDTs for version control |

---

*For organizing UDTs, see `Folder.md`. For individual tags, see other tag-type files.*
