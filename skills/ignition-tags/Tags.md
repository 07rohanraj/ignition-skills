---
name: ignition-tags
description: Create, import, and export Ignition tags via the Gateway REST API. Use this skill when the user is creating tags, managing tags, or working with Ignition tag structures.
---

# Ignition Tags Skill

## Description

This skill enables creating, importing, and exporting Ignition tags using the Gateway REST API. It provides a complete workflow for generating tag JSON and executing it against an Ignition Gateway.

---

## Agent Workflow Overview

When a user requests tag creation, follow this workflow:

1. **Identify Tag Types**: Determine what types of tags the user needs (Memory, OPC, Expression, Query, Reference, Derived, UDT)
2. **Generate JSON**: Create the tag JSON structure based on the schemas in `schemas/` directory
3. **Validate**: Run the import script with `--validate-only` to check JSON
4. **Import**: Run the import script to create tags in the Gateway

## Step 1: Identify Tag Types

Based on user request, determine which tag type to use:

| User Request | Tag Type | Schema File |
|--------------|----------|-------------|
| Setpoints, configuration values, internal data | Memory Tag | `schemas/memory-tag.json` |
| PLC data, OPC-UA addresses | OPC Tag | `schemas/opc-tag.json` |
| Calculated values, expressions | Expression Tag | `schemas/expression-tag.json` |
| Database queries, SQL results | Query Tag | `schemas/query-tag.json` |
| Reference another tag | Reference Tag | `schemas/reference-tag.json` |
| Derived with read/write expressions | Derived Tag | `schemas/derived-tag.json` |
| Organize tags into groups | Folder | `schemas/folder.json` |
| Reusable templates, parameterized tags | UDT Definition | `schemas/udt-definition.json` |
| Instance of a UDT | UDT Instance | `schemas/udt-instance.json` |

## Step 2: Generate Tag JSON

After identifying the tag type, generate JSON following the Ignition tag format. Use the schemas for validation:

```json
{
  "tags": [
    {
      "name": "TagName",
      "tagType": "AtomicTag",
      "valueSource": "memory",
      "dataType": "Float8",
      "value": 0.0
    }
  ]
}
```

### Key Rules

- **Top-level key**: Always `"tags"` (array of tag objects)
- **tagType values**: `"AtomicTag"`, `"Folder"`, `"UdtType"`, `"UdtInstance"`
- **valueSource values**: `"memory"`, `"opc"`, `"expression"`, `"db"`, `"reference"`, `"derived"`
- **Never guess properties**: Only use properties documented in the schemas

## Step 3: Save JSON to File

Save the generated JSON to a file:

```python
import json
import os

output_dir = os.path.join(os.environ.get('TEMP', '.'), 'ignition-tags')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'generated-tags.json')

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(tag_data, f, indent=2)
```

## Step 4: Validate JSON

Before importing, validate the JSON structure:

```bash
python skills/ignition-tags/scripts/import-tags.py --validate-only --file generated-tags.json
```

## Step 5: Import Tags

Import the tags to the Ignition Gateway:

```bash
# Basic import (default provider, root path)
python skills/ignition-tags/scripts/import-tags.py --file generated-tags.json

# Import to specific provider and path
python skills/ignition-tags/scripts/import-tags.py --file generated-tags.json --provider default --path "Motors"

# Dry run (validate without importing)
python skills/ignition-tags/scripts/import-tags.py --file generated-tags.json --dry-run
```

## Configuration

The scripts support three configuration methods (in priority order):

### 1. CLI Arguments (Highest Priority)
```bash
python import-tags.py --file tags.json --provider default --path "Motors"
```

### 2. Environment Variables
```bash
set IGNI_HOST=http://localhost:8088
set IGNI_TOKEN=your-api-token-here
python import-tags.py --file tags.json
```

### 3. config.json File (Lowest Priority)
Create `config.json` in the project root or `scripts/` directory:
```json
{
  "host": "http://localhost:8088",
  "token": "your-api-token-here",
  "provider": "default"
}
```

## API Token Setup

1. Open Ignition Gateway in browser
2. Go to **Config** → **System** → **Security** → **API Tokens**
3. Click **Create New Token**
4. Set **Provider Scope** to the tag provider you want to manage
5. Copy the generated token

## Collision Policies

| Policy | Description |
|--------|-------------|
| `Abort` | Stop if any tag exists |
| `Overwrite` | Replace existing tags (default) |
| `Rename` | Rename new tags to avoid conflicts |
| `Ignore` | Skip existing tags |
| `MergeOverwrite` | Merge properties, overwriting values |

## Export Tags

Export existing tags from the Gateway:

```bash
# Export all tags
python skills/ignition-tags/scripts/export-tags.py --output exported-tags.json

# Export specific path
python skills/ignition-tags/scripts/export-tags.py --path "Motors" --output motors.json

# Export without UDTs
python skills/ignition-tags/scripts/export-tags.py --no-udts --output tags.json
```

## Common Tag Structures

### Memory Tags (Setpoints)
```json
{
  "tags": [
    {
      "name": "TemperatureSetpoint",
      "tagType": "AtomicTag",
      "valueSource": "memory",
      "dataType": "Float8",
      "value": 100.0,
      "engUnit": "degF"
    }
  ]
}
```

### OPC Tags (PLC Data)
```json
{
  "tags": [
    {
      "name": "Temperature",
      "tagType": "AtomicTag",
      "valueSource": "opc",
      "opcServer": "Ignition OPC UA Server",
      "opcItemPath": "ns=1;s=[PLC1]/Temperature",
      "engUnit": "degF"
    }
  ]
}
```

### Expression Tags (Calculated)
```json
{
  "tags": [
    {
      "name": "TemperatureC",
      "tagType": "AtomicTag",
      "valueSource": "expr",
      "dataType": "Float8",
      "expression": "({[.]Temperature} - 32) * 5/9",
      "engUnit": "degC"
    }
  ]
}
```

### Folder Structure
```json
{
  "tags": [
    {
      "name": "Motors",
      "tagType": "Folder",
      "tags": [
        {
          "name": "Motor1",
          "tagType": "AtomicTag",
          "valueSource": "memory",
          "dataType": "Boolean"
        }
      ]
    }
  ]
}
```

### UDT Definition and Instances
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
    }
  ]
}
```

## Error Handling

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Connection refused` | Gateway not running | Start Ignition Gateway |
| `401 Unauthorized` | Invalid API token | Check token in Gateway config |
| `403 Forbidden` | Token lacks permissions | Create token with tag provider scope |
| `404 Not Found` | Invalid API endpoint | Check Gateway version supports REST API |
| `JSON validation failed` | Malformed JSON | Check JSON syntax and structure |

## File Locations

```
ignition-tags/
├── Tags.md                    # This file (workflow + reference)
├── config.example.json        # Configuration template
├── schemas/                   # JSON Schema files for validation
│   ├── memory-tag.json
│   ├── opc-tag.json
│   ├── expression-tag.json
│   ├── query-tag.json
│   ├── reference-tag.json
│   ├── derived-tag.json
│   ├── folder.json
│   ├── udt-definition.json
│   └── udt-instance.json
└── scripts/
    ├── import-tags.py         # Import tags to Gateway
    └── export-tags.py         # Export tags from Gateway
```

---

# Tag Reference Documentation

## Tag Types

| Tag Type |
|----------|
| Memory tag |
| OPC tag |
| Expression tag |
| Query tag |
| Reference tag |
| Derived tag |
| System Client tags, Vision Client tags |

---

## OPC Tags

An OPC tag is driven by an OPC Item Path and OPC server. The OPC Item Path is a string path to a particular device connection. The exact path is defined by the driver and OPC server used to communicate with the device. Many drivers support browsing, allowing you to automatically create OPC tags by dragging-and-dropping from the OPC Browser. However, in cases where browsing isn't supported, OPC tags can manually be created.

---

## Memory Tags

Memory tags are simple tags, that do not automatically poll or update their value. They hold the same value until some other user-created mechanism (most likely a script or binding) changes their value. They're useful in situations where a value must be stored outside of a PLC or database.

The Value Persistence setting determines how the Memory tag values are stored. This option will impact whether the tag value is retained across Gateway restarts.

---

## Expression Tags

Expression tags are driven by an expression, allowing their values to be determined from a calculation.

The Expression property on Expression tags determines their value. The expression can reference values and properties on other Gateway-scoped tag values. However, due to scoping, they can not reference property values on Vision Client and Perspective Session components.

The expression on an Expression tag executes based off of the Execution Mode. More information on Execution Mode can be found on the Tag Properties page.

---

## Query Tags

A Query tag executes a SQL Query; the result of that query is returned to the value on the tag. Query tags can reference other Gateway-scoped tags to build dynamic queries. The Query property dictates the query that will execute, and the Execution Mode determines how often the query will run. Furthermore, the Datasource property determines which database connection the query will execute against.

---

## Reference and Derived Tags

### Reference Tags

A Reference tag simply refers to an existing tag, using the Source Tag Path property to determine which other tag to reference. Writes targeting the Reference tag will send a write request to the source tag.

### Derived Tags

A Derived tag is an abstracted tag that refers to another tag. They are similar conceptually to Reference tags in that that value is dependent on the Source Tag Path property, but Derived tags have some additional functionality. Namely, they can apply expressions to the referenced value with the Read Expression property, allowing the value on the Derived tag to differ from the source tag.

In addition, The Write Expression property will apply an expression to the value of any write requests targeting the Derived tag, allowing the expression to modify the value of the incoming write before it's applied back to the source tag.

---

## User Defined Types (UDTs)

UDTs are created out of standard tag types, but they offer a variety of additional features. You can think of them as a way to create "data templates", where a particular structure of tags is defined, and can then be created as if it were a single tag. This UDT example shows two Motor instances, the data type Motor, and all the parameters and tags that make up the structure (i.e., Amps and HOA).

---

## System Tags

System tags provide status about the Ignition system. They're generally cannot be modified, but provide use information about how the system is performing.

---

## Tag Configuration on the File System

Tag configurations are grouped by the folder they exist in and are stored in the following locations:

| Type | Path |
|------|------|
| Atomic Tags | `/data/config/core/ignition/tag-definition/<provider>/<path to folder>/tags.json` |
| UDT Instances | `/data/config/core/ignition/tag-definition/<provider>/<path to folder>/udts.json` |
| UDT Definitions | `/data/config/core/ignition/tag-type-definition/<provider>/<path to folder>/udts.json` |

---

## Tag Object Types

Some features, such as system.tag.browse, can access the Object Type of the tag (sometimes called "tagType"). Below is a table representing the possible types.

| Object Type | Description |
|-------------|-------------|
| `Property` | A single value underneath an node. |
| `Node` | An entity that may have a value and may have children. Node is a generic term for other objects in this table, such as a Folder or AtomicTag. |
| `Folder` | Represented by a folder in the Tag Browser. Folders generally have child nodes, but don't have values or other properties that make up a tag. |
| `AtomicTag` | A normal type of tag. Objects with this type can be one of the following (based on the Value Source property): OPC tag, Query tag, Expression tag, Derived tag, Reference tag, Memory tag |
| `UdtInstance` | An instance of a complex tag (UDT Instance). It's important to note that UdtInstances contain other nodes, so this type is generally only seen at the root of a UDT instance. Thus, nodes under a UdtInstance are not considered to have a type of UdtInstance, unless the child node is actually a UdtInstance, in other words, a nested UDT instance. |
| `UdtType` | Represents the root of a complex tag definition (UDT Definition). Similar to UdtInstance, nodes under a UdtType have their own object type, so a UdtType represents the root of a complex tag. |
| `Provider` | Represents a Tag Provider. |

---

## Basic Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Name | `name` | How the tag will be presented and referenced in the system. The tag path will be the provider, the folder structure, and this name. Valid names begin with either a letter or underscore and can contain: Letters, Digits, Underscores, Spaces, Parentheses, Single quotes, Dashes, Colons. Additionally, the name must be less than 256 characters in length. | String | OPC, Query, Expression, Derived, Client, Reference, Memory |
| Tag Group | `tagGroup` | The Tag Group that will execute the tag. The Tag Group dictates the rate and conditions on which the tag will be evaluated. For more details, see Tag Groups. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Enabled | `enabled` | Whether the tag will be evaluated by the Tag Group. If false, the tag will still be present, but will not return a value or good quality. Default value is Enabled. | Boolean | OPC, Query, Expression, Derived, Reference, Memory |

---

## Value Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Tag Type (unlisted) | `tagType` | The type of the node, automatically determined by the tag type created. See the Tag Object Types table for more information. Commonly used values are folder, UdtInstance, UdtType, and AtomicTag. Default value is AtomicTag. Note: This property does not appear in the Tag Editor, but is accessible via scripting. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Type ID | `typeId` | Returns a path representing which UDT this instance is derived from. If the node is not a UDT, then this property will return a None object. Note: This property appears in a UDT Definition/Instance editor as Parent Data Type. Additionally, parent data types can only be set from UDT Definitions within the same provider. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Value Source | `valueSource` | Specifies how the tag determines its value. In other words, sets the type of the tag (Memory, OPC, Expression, etc). Below is a list of possible values and their JSON representation: Derived - `derived`, Expression - `expr`, Memory - `memory`, OPC - `opc`, Query - `db`, Reference - `reference`. Default value is Memory. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Data Type | `dataType` | The data type of the tag. It is important that this be set as correctly as possible with regards to the tag's underlying data source. The tag system will attempt to coerce any raw incoming value (for example, from OPC or a SQL query) into the desired type. For detailed information and a list of possible values, see Tag Data Types. Default value is Integer. Note: Regarding Array data types, Alarming, Scaling, and Historical settings applied to an array tag are propagated down to elements in the array. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Default Value | `defaultValue` | The default value of an individual Memory tag, which typically only applies on creation when a value doesn't exist within the Value Persistence Database or Configuration behavior. This property will always apply if Value Persistence is set to None, since no value is ever stored. Note that if the Default Value is not set and the Value property is set, the Default Value will inherit the Value property. | Object (depends on the data type of the tag) | Memory |
| Value | `value` | The value of the tag. Can only be modified if the tag allows value writing and the user has sufficient privileges. If the Default Value is set for individual tags, and this Value is not, the Default Value will be inherited. Note: In UDT instances, certain types of tag values, such as DB and OPC, can get stored within the definition, causing a tag to appear to have an override when it actually doesn't. | Object (depends on the data type of the tag) | Memory |
| Value Persistence | `valuePersistence` | The behavior for storing a Memory tag's value. This property defaults to Inherited, which means the memory tag will use the Value Persistence option set on the Tag Provider. Possible values to override the Tag Provider setting include: None: Memory tag value changes will persist in the memory only and on Gateway restarts, the value will revert to the Default Value property. Database: Memory tag value changes will persist to a SQLite DB and be reloaded on start, but will not modify the Default Value in the configuration file when changed. Note that the configuration file will be modified with an edit to the tag, such as adding an alarm. Configuration: Memory tag value changes will persist to the tag configuration. This option should be used sparingly to avoid performance hits. | String | Memory |
| OPC Server | `opcServer` | The server against which to subscribe the data point. The list displayed is the OPC Clients in Ignition section. | String | OPC |
| OPC Item Path | `opcItemPath` | The path to the node to subscribe to via the OPC Client. The point will be subscribed at the rate dictated by the Tag Group. It's possible to escape curly braces in the item path by using additional curly braces. For example: `{{device_name}}` would evaluate to `{<device_name value>}`, allowing you to include braces in the Item Path. | String | OPC |
| Source Tag Path | `sourceTagPath` | The path to the tag that this tag is referencing. | String | Derived, Reference |
| Execution Mode | `executionMode` | Determines how and when the tag executes. Possible values are listed below along with JSON names and descriptions: Event Driven `EventDriven`: Updates when something happens (i.e., value event or alarm event) within the expression. Fixed Rate `FixedRate`: Tag will be executed at the set or fixed rate. Adds the Execution Rate property, which determines how often the tag executes in milliseconds. Tag Group `TagGroupRate`: Tags are executed by Tag Groups, which dictate the rate of execution. Default value is Event Driven. Note: In certain tag types such as DB, the default value may not make sense as there are no events generated via a change. In these cases, a different execution mode should be set. | String | Expression, Query |
| Expression | `expression` | The expression the tag will use to determine its value. | String | Expression |
| Read Expression | `deriveExpressionGetter` | The expression that determines how the value on the Derived tag is read from the source tag. | String | Derived |
| Query | `query` | The SQL query to be run, which drives the tag's value. Queries doing database reads and writes are possible, see the Query Type property description for details. | String | Query |
| Write Expression | `deriveExpressionSetter` | The expression that determines how the value on the Derived tag is written to the source tag. | String | Derived |
| Datasource | `datasource` | The database connection that the Query tag will execute against. The list displayed is the DB connections section. | String | Query |
| Query Type | `queryType` | Defines whether the query is executing a database read or a database write. Important for determining the value behavior of the tag. Possible values are: AutoDetect - Query type is determined from the query itself. Select - Dictates that the query is reading data from the database. The query result set will be stored on the tag's value. Update - Dictates that the query is writing data to the database (but does not require an UPDATE statement in the query, specifically). The value on the Query tag will be the number of affected rows. | String | Query |
| Preserve Source Timestamp | `preserveSourceTimestamp` | New in 8.3.1 If true, the derived value will use the timestamp from the source value. If false, the derived value will use the current time as the timestamp. | Boolean | Derived |

---

## Numeric Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Deadband | `deadband` | A numerical value used to prevent unnecessary updates for tags whose values change by small amounts. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Deadband Mode | `deadbandMode` | Defines how the deadband value is used. Possible values along with JSON names and descriptions are listed below: Absolute `Absolute`: The deadband setting is considered to be an absolute value. Percent `Percent`: The actual deadband is calculated as a percent of the tag's engineering unit span, including Engineering Low and Engineering High. Off `Off`: The deadband setting is the equivalent to a value of 0.0, so that all values pass through if their timestamp has changed. Default value is Absolute. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Scale Mode | `scaleMode` | If and how the tag value will be scaled between the source, and what is reported for the tag. A listing of possible values along with their JSON names and numerical representation can be found below: Off `Off`: 0, Linear `Linear`: 1, Square Root `SquareRoot`: 2, Exponential Filter `ExponentialFilter`: 3, Bit Inversion `BitInversion`: 4. Default value is Off. Note: When using system functions like system.tag.configure to set the Scale Mode, the JSON string value must be used. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Raw Low | `rawLow` | Start of the "raw" value range. Only present if Scale Mode is set to Linear or Square Root. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Raw High | `rawHigh` | End of the "raw" value range. Only present if Scale Mode is set to Linear or Square Root. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Scaled Low | `scaledLow` | Start of "scaled" value range. Raw low will map to Scaled low for the tag. Only present if Scale Mode is set to Linear or Square Root. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Scaled High | `scaledHigh` | End of "scaled" value range. Raw high will map to Scaled high for the tag. Only present if Scale Mode is set to Linear or Square Root. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Clamp Mode | `clampMode` | How values that fall outside of the ranges will be treated. Clamped values are only present if Scale Mode is set to Linear or Square Root, and will be adjusted to the low/high scaled value as appropriate. Possible values along with their JSON names and numerical representation are listed below: No_Clamp `No_Clamp`: 0, Clamp_Low `Clamp_Low`: 1, Clamp_High `Clamp_High`: 2, Clamp_Both `Clamp_Both`: 3. Default value is No_Clamp. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Scale Factor | `scaleFactor` | The factor parameter for the equation, used when the Scale Mode property is set to Exponential Filter | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Engineering Units | `engUnit` | The engineering units of the value, which can be manually entered or selected from a list. Some Vision components, such as the Numeric Label, will automatically show these units. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Engineering Low Limit | `engLow` | The lowest expected value of the tag. This property can be leveraged for use by: Out of Range alarms, Engineering Limit modes, History Deadband mode calculations. In some cases, using drag and drop onto Vision components may automatically bind this property to the Minimum property of the component. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Engineering High Limit | `engHigh` | The highest expected value of the tag. This property can be leveraged for use by: Out of Range alarms, Engineering Limit modes, History Deadband mode calculations. In some cases, using drag and drop onto Vision components may automatically bind this property to the Maximum property of the component. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Engineering Limit Mode | `engLimitMode` | Dictates how the engineering range should be enforced on the tag. If not "Off", the tag will change to bad quality ("limit exceeded"), when the value falls outside the specified range. Possible values along with their JSON names and numerical representations are listed below: No_Clamp `No_Clamp`: 0, Clamp_Low `Clamp_Low`: 1, Clamp_High `Clamp_High`: 2, Clamp_Both `Clamp_Both`: 3. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Format String | `formatString` | How the value should be formatted when converted to a string (only applies to numerical data types). Uses # and 0 characters to describe the format. #: If the number in this position is non-zero, then do not show the position. Otherwise, show the number. Useful when you only want to show a decimal position if the value is non-zero. 0: If the number in this position is non-zero, then show that number. Otherwise, show a zero. Useful to add leading and trailing zeros to a value. See Data Type Formatting Reference for more information. In some cases, using drag and drop onto Vision components may automatically bind this property to the Decimal Format property of the component. | String | OPC, Query, Expression, Derived, Reference, Memory |

---

## Meta Data Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Tooltip | `tooltip` | The tooltip provides a hint to visual components as to what should be displayed when the user hovers their mouse cursor over the component that is being driven by the value of this tag. In some cases, using drag and drop onto Vision components may automatically bind this property to the Mouseover Text property of the component. Hovering over the tag itself in the Tag Browser will also display this hint. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Documentation | `documentation` | A freeform text property for information about the tag. | String | OPC, Query, Expression, Derived, Reference, Memory |

---

## Security Data Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Read Permissions | `readPermissions` | Defines the security levels required in order to read values from a tag. Roles under authenticated will show up based on property Security Levels being configured. For more information, see Tag Security Properties. See the Permission Values section for a description of possible values. | JSON Object | OPC, Query, Expression, Derived, Reference, Memory |
| Read Only | `readOnly` | Defines whether a tag is read-only or writeable. For more information, see Tag Security Properties. | Boolean | OPC, Query, Expression, Derived, Reference, Memory |
| Write Permissions | `writePermissions` | Defines the security levels required in order to read values from a tag. Roles under authenticated will show up based on property Security Levels being configured. For more information, see Tag Security Properties. See the Permission Values section for a description of possible values. | JSON Object | OPC, Query, Expression, Derived, Reference, Memory |

---

## Permission Values

| Property | JSON/Scripting Name | Description |
|----------|---------------------|-------------|
| Type | `type` | Represents the selected radio button on the security level UI, determining if all of the elements in the securityLevels array are required, or if any of the elements are allowed. Possible values are: `AnyOf`, `AllOf`. In other words, a user logging in must satisfy either any of the selected criteria or all criteria selected. |
| Security Levels | `securityLevels` | Represents allowed security levels for this permission. Each level is represented as a JSON object, containing a "name" value that represents the name of a security level, and a "children" array which represents any levels under the current. The actual "selected" levels are any levels that have an empty "children" object. See the example below for more information. |

### JSON Example

The JSON in this example uses the configuration shown in the image below. Permission is granted if the security levels on the request are from either an "Administrator" user, or if the request originated from the "Zone A" Security Zone.

```json
"readPermissions": {
    "type": "AnyOf",
    "securityLevels": [
      {
        "name": "Authenticated",
        "children": [
          {
            "name": "Roles",
            "children": [
              {
                "name": "Administrator",
                "children": []
              }
            ]
          }
        ]
      },
      {
        "name": "SecurityZones",
        "children": [
          {
            "name": "Zone A",
            "children": []
          }
        ]
      }
    ]
  }
```

---

## Scripting Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Tag Event Scripts | `eventScripts` | Each tag has the option to have Tag Event Scripts on it. When you edit a tag, you can navigate to the Tag Events screen to see a list of all of the tag scripts. You can then select which event you would like to write a script for. You can even write a script for multiple events if you like. For detailed information, see Tag Event Scripts. When interacting with a tag from a script, the Tag Event Scripts are represented as an array of JSON objects. Each JSON object is described below in the Key Description section. | JSON Array | OPC, Query, Expression, Derived, Reference, Memory |

### Key Description

| Key | Description |
|-----|-------------|
| `eventid` | A value representing the type of event script. See values below for a list of possible events: Quality Changed: `qualityChanged`, Value Changed: `valueChanged`, Alarm Active: `alarmActive`, Alarm Cleared: `alarmCleared`, Alarm Acknowledged: `alarmAcked` |
| `script` | A value representing the content of the script |

---

## Alarms Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| Alarms | `alarms` | Tags have the ability to define any number of alarms. Each alarm is a condition that will be evaluated when the value of the tag changes. When the condition becomes true, the alarm is said to be active. When it becomes false, the alarm is said to be cleared. For detailed information, see Tag Alarm Properties. | JSON Array of JSON objects. For detailed information, see Tag Alarm Properties. | OPC, Query, Expression, Derived, Reference, Memory |
| Alarm Eval Enabled | `alarmEvalEnabled` | Determines if alarms will be evaluated on this tag. | Boolean | OPC, Query, Expression, Derived, Reference, Memory |

---

## History Properties

| Property | JSON/Scripting Name | Description | Data Type | Applicable Tag Type |
|----------|---------------------|-------------|-----------|---------------------|
| History Enabled | `historyEnabled` | Whether the tag will report its history to the Tags Historian system. | Boolean | OPC, Query, Expression, Derived, Reference, Memory |
| Storage Provider | `historyProvider` | Which Tag Historian data store the tag will target. A particular tag can only target one history store. For more information, refer to History Providers on the Tag History Gateway Settings page. Note: The Storage Provider dropdown displays the provider names as they are written at the time of tag configuration. If the Storage Provider name is updated later, this setting will need to be adjusted to match the new Storage Provider name. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Deadband Style | `historicalDeadbandStyle` | There are three styles to choose from: Auto, Analog, or Discrete. When set to Auto, this setting will automatically pick from Analog or Discrete, based on the data type of the tag: If the data type of the tag is set to a float or double, then Auto will use the Analog Style. If the data type of the tag is any other type, then the Discrete style will be used. More information on the Analog and Discrete types can be found on the Configuring Tag History page. A list of possible values along with their JSON name are below: Auto `Auto`, Analog `Analog_Compressed`, Discrete `Discrete` | String | OPC, Query, Expression, Derived, Reference, Memory |
| Deadband Mode | `historicalDeadbandMode` | Defines how the deadband value is used. Possible values along with JSON names and descriptions are listed below: Absolute `Absolute`: The deadband setting is considered to be an absolute value. Percent `Percent`: The actual deadband is calculated as a percent of the tag's engineering unit span. Off `Off`: The deadband setting is the equivalent to a value of 0.0, so that all values pass through if their timestamp has changed. See the Numeric Properties section above for the Percent calculation. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Historical Deadband | `historicalDeadband` | A deadband that applies only to historical evaluation. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Sample Mode | `sampleMode` | Determines how often to check if a historical record should be collected. Possible values include: `OnChange`, `Periodic`, `TagGroup` | String | OPC, Query, Expression, Derived, Reference, Memory |
| Sample Rate | `historySampleRate` | When the Sample Mode property is set to "Periodic", this property (working in conjunction with the Sample Rate Units property) determines how often a record should be collected. | Numeric | OPC, Query, Expression, Derived, Reference, Memory |
| Sample Rate Units | `historySampleRateUnits` | When the Sample Mode property is set to "Periodic", this property (working in conjunction with the Sample Rate property) determines the unit of time that will be use in record collection. For a list of units, see the Units of Time section. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Historical Tag Group | `historyTagGroup` | When the Sample Mode property is set to Tag Group, this property determines which Tag Group will be used to collect records. See Tag Groups for more information. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Min Time Between Samples | `historyTimeDeadband` | Minimum time between records. Prevents multiple consecutive tag changes from triggering consecutive record collections. Works in conjunctions with the Min Time Units property. The Value is calculated off of the value timestamp. Useful in restricting the number of records collected when the Sample Mode is set to On Change. However, the behavior will differ slightly when using On Change, as the latest timestamp after the Min Time Between Samples threshold is used instead of timestamps from before the minimum time. | Integer | OPC, Query, Expression, Derived, Reference, Memory |
| Min Time Units | `historyTimeDeadbandUnits` | Units of time to use with the Min Time Between Samples property. For a list of units, see the Units of Time section. | String | OPC, Query, Expression, Derived, Reference, Memory |
| Max Time Between Samples | `historyMaxAge` | Maximum time between samples. Works in conjunction with the Max Time Units property. If a sample has not been collected by the time range specified by these two properties, then a record will be collected on the next sample interval. This setting cannot be less than 1000ms. Setting this value to 0 will disable automatic record collection. Default is 0. Note: This setting will be ignored if the Sample Mode is set to Tag Group, and the targeted Tag Group is using non-default values for its Max Time Between Samples setting. The implication being that non-default values on the Tag Group settings take precedence over this setting. | Integer | OPC, Query, Expression, Derived, Reference, Memory |
| Max Time Units | `historyMaxAgeUnits` | Maximum time in units. For a list of units, see the Units of Time section. | String | OPC, Query, Expression, Derived, Reference, Memory |

---

## Units of Time

| Unit of Time | JSON/Scripting Name |
|--------------|---------------------|
| Milliseconds | `MS` |
| Seconds | `SEC` |
| Minutes | `MIN` |
| Hour | `HOUR` |
| Day | `DAY` |
| Week | `WEEK` |
| Month | `MONTH` |
| Year | `YEAR` |

---

## Read-Only Properties

| Property | Description |
|----------|-------------|
| `CanRead` | A read-only property that represents whether or not this tag can be read from the current security context. This is determined by looking at the read permission settings on the tag and the Tag Provider's permission settings. |
| `CanWrite` | A read-only property that represents whether or not this tag can be written to from the current security context. This is determined by looking at the write permission settings on the tag, the Read Only property, and the Tag Provider's permission settings. |

---

## Tag Data Types

This page describes the data types that can be applied to standard tags.

The data type of a tag is determined by the Data Type property in the Tag Editor The tag system will attempt to coerce incoming raw values (for example, from OPC or a SQL query) to the configured type.

| Data Type | String Value | Integer Value |
|-----------|--------------|---------------|
| Byte | `Int1` | 0 |
| Short | `Int2` | 1 |
| Integer | `Int4` | 2 |
| Long | `Int8` | 3 |
| Float | `Float4` | 4 |
| Double | `Float8` | 5 |
| Boolean | `Boolean` | 6 |
| String | `String` | 7 |
| DateTime | `DateTime` | 8 |
| Text (Deprecated) | `Text` | 10 |
| Byte Array | `Int1Array` | 17 |
| Short Array | `Int2Array` | 18 |
| Integer Array | `Int4Array` | 11 |
| Long Array | `Int8Array` | 12 |
| Float Array | `Float4Array` | 19 |
| Double Array | `Float8Array` | 13 |
| Boolean Array | `BooleanArray` | 14 |
| String Array | `StringArray` | 15 |
| DateTime Array | `DateTimeArray` | 16 |
| Binary Data | `ByteArray` | 20 |
| Dataset | `DataSet` | 9 |
| Document | `Document` | 29 |

---

## Tag Paths

Tags and their properties can be referenced by a string-based path in many areas of Ignition, such as expressions and scripts. Each tag has a unique absolute path and often has many equivalent relative paths when referenced from other tags. In most cases these paths are generated automatically via helper buttons. However, it's a good idea to understand how tag paths work, particularly if you need to configure an Indirect Tag Binding, or access a tag from an expression or script.

A tag path looks something like this: `[Tag Provider]folder/path/tag.property`

The `folder/path/tag.property` portion of the path may contain the following:

- A tag
- Any number of nested folders followed by a tag, separated by forward slashes (/)
- A period (.) followed by a property name after the tag. Omitting this is equivalent to using the `.value` property

The `[Tag Provider]` portion surrounded by square braces can have the following options:

| Source Option | Meaning |
|---------------|---------|
| `[Tag Provider Name]` | The name of the Tag Provider that hosts the tag. |
| `[]` or not specified | The default Tag Provider for the current project. If used in the Gateway scope, this notation can (generally) result in an invalid path, as the Gateway doesn't have a default Tag Provider. |
| `[.]` | Relative to the folder of the tag that is being bound. This is especially useful in UDT definitions. |
| `[~]` | Relative to the Tag Provider of the tag that is being bound (root node). |
| `[Client]` | Refers to the Vision Client Tag Provider, which contains only Vision Client Tags. |
| `[System]` | Refers to a System Tag. |

---

## Tag Path Manipulation

Ignition provides a great deal of flexibility for tag addressing since tag paths and tag properties are string-based. The underlying strings that compose a valid tag path can be assembled from many different parts in which the eventual construction results in a valid tag path.

The following scripting demonstrates this concept. Suppose there was a tag path to a level indicator in a tank. In this case it is the default Tag Provider, Tanks folder, Tank 1 Folder, and the Level tag.

```python
tagPath = "[default]Tanks/Tank 1/Level"
```

But suppose that there was more than just Tank 1, and instead there was Tank 2, Tank 3, Tank 4, etc. Dynamically changing the tag paths is simple because Ignition's tag paths are string representations. The following takes the tank number and inserts it into a new tag path. The tankNumber variable changes the eventual creation of the tagPath. Using this method in scripting or in an expression binding will look slightly different.

In the following example, tankNumber is a variable for a python script:

### Python Dynamic Tag Path

```python
tankNumber = 2
tagPath = "[default]Tanks/Tank %i/Level" % tankNumber
```

Then, in this next example, tankNumber is a separate tag being referenced within an expression tag of the same folder:

### Expression Dynamic Tag Path

```
tag("[default]Tanks/Tank "+{[.]tankNumber}+"/Level")
```

The result of the tagPath variable will be `[default]Tanks/Tank 2/Level` which is a valid tag path to the level sensor for Tank 2.

---

## Array Type Tag Paths

When a path leads to an array type tag, individual elements can be accessed using square brackets, and the index offset.

```
[default]Folder/myArrayTag[0]
```

---

## Historical Tag Paths

Components like the Power Chart and the Tag Browse Tree use historical tag paths when historical values are needed. The system.historian functions also support historical paths.

### Historical Tag Path Syntax

```
histprov:test:/sys:myGateway:/prov:default:/tag:_Simulator_/Ramp/Ramp0
```
