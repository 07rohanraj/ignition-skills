# Folder

## Description

Folders organize tags into a hierarchical structure. They don't hold values themselves but provide logical grouping and path organization.

## JSON Structure

```json
{
  "name": "FolderName",
  "tagType": "Folder",
  "tags": []
}
```

## Required Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Folder name |
| `tagType` | string | Always `"Folder"` |

## Optional Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `tags` | array | `[]` | Child tags and folders |
| `enabled` | boolean | `true` | Whether folder is active |
| `documentation` | string | `""` | Folder description |

## Examples

### Empty Folder

```json
{
  "name": "Motors",
  "tagType": "Folder",
  "tags": []
}
```

### Folder with Tags

```json
{
  "name": "Sensors",
  "tagType": "Folder",
  "tags": [
    {
      "name": "Temperature",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[PLC1]Sensors/Temp"
    },
    {
      "name": "Pressure",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[PLC1]Sensors/Pressure"
    }
  ]
}
```

### Nested Folders

```json
{
  "name": "Plant",
  "tagType": "Folder",
  "tags": [
    {
      "name": "Area1",
      "tagType": "Folder",
      "tags": [
        {
          "name": "Motors",
          "tagType": "Folder",
          "tags": [
            {
              "name": "Motor1",
              "tagType": "AtomicTag",
              "valueSource": "opc",
              "opcServer": "Ignition OPC UA Server",
              "opcItemPath": "ns=1;s=[PLC1]Area1/Motors/Motor1/Amps"
            }
          ]
        }
      ]
    }
  ]
}
```

### Folder with Mixed Content

```json
{
  "name": "Process",
  "tagType": "Folder",
  "tags": [
    {
      "name": "Setpoints",
      "tagType": "Folder",
      "tags": [
        {
          "name": "Temperature",
          "tagType": "AtomicTag",
          "valueSource": "memory",
          "dataType": "Float8",
          "value": 100.0
        }
      ]
    },
    {
      "name": "Readings",
      "tagType": "Folder",
      "tags": [
        {
          "name": "CurrentTemp",
          "tagType": "AtomicTag",
          "valueSource": "opc",
          "opcServer": "Ignition OPC UA Server",
          "opcItemPath": "ns=1;s=[PLC1]Temp/Sensor1"
        }
      ]
    }
  ]
}
```

## Path Structure

Folders create the tag path hierarchy:

```
[default]Plant/Process/Setpoints/Temperature
         ^^^^^ ^^^^^^^ ^^^^^^^^^ ^^^^^^^^^^^
         provider folder folder   folder     tag
```

## Use Cases

| Use Case | Description |
|----------|-------------|
| Equipment | Group tags by equipment (Motors, Pumps, Tanks) |
| Location | Organize by physical area (Area1, Building2) |
| Function | Separate by purpose (Setpoints, Readings, Alarms) |
| UDT Members | Contain UDT member tags |

---

*For creating tag templates, see `UDT.md`. For individual tags, see `Memory Tag.md`, `OPC Tag.md`, etc.*
