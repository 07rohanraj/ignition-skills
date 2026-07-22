# How to build a new Perspective View

## Description

This set of instructions provides a step by step guide on how to construct the basic JSON configuration for a new Perspective View.

## Documentation

# This set of instructions provides a step by step guide on how to construct the basic JSON configuration for a new Perspective View.

1. Start by selecting a container type for the root of the View. You can select Coordinate, Flex, Column, Breakpoint, Split, Tab.

2. Use the starter JSON for that root type.
## Coordinate
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "meta": {
      "name": "root"
    },
    "type": "ia.container.coord"
  }
}

## Breakpoint
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "meta": {
      "name": "root"
    },
    "type": "ia.container.breakpt"
  }
}

## Column
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "meta": {
      "name": "root"
    },
    "type": "ia.container.column"
  }
}

## Flex
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "meta": {
      "name": "root"
    },
    "props": {
      "direction": "column"
    },
    "type": "ia.container.flex"
  }
}

## Split
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "meta": {
      "name": "root"
    },
    "type": "ia.container.split"
  }
}

## Tab
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "meta": {
      "name": "root"
    },
    "type": "ia.container.tab"
  }
}


3. Adjust the View's own properties if needed. Default size can be used to adjust the size of the view. Standard monitor sizes are typically used (1080p, 4k) as well as mobile/tablet if this is purely a mobile/tablet view only. Drop config is for use within the Designer and is not likely necessary for your view here.
{
  "type": "object",
  "properties": {
    "defaultSize": {
      "type": "object",
      "properties": {
        "width": {
          "type": "integer",
          "default": 800
        },
        "height": {
          "type": "integer",
          "default": 800
        }
      }
    },
    "dropConfig": {
      "type": "object",
      "properties": {
        "udts": {
          "type": "array",
          "default": [],
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "default": "",
                "format": "udt-path"
              },
              "param": {
                "type": "string",
                "default": ""
              },
              "action": {
                "type": "string",
                "default": "bind",
                "enum": ["bind", "path"]
              }
            }
          }
        },
        "dataTypes": {
          "type": "array",
          "default": [],
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "default": "Int4",
                "enum": [
                  "Int1",
                  "Int2",
                  "Int4",
                  "Int8",
                  "Float4",
                  "Float8",
                  "Boolean",
                  "String",
                  "DateTime",
                  "Text",
                  "Int1Array",
                  "Int2Array",
                  "Int4Array",
                  "Int8Array",
                  "Float4Array",
                  "Float8Array",
                  "BooleanArray",
                  "StringArray",
                  "DateTimeArray",
                  "ByteArray",
                  "DataSet",
                  "Document"
                ]
              },
              "param": {
                "type": "string",
                "default": ""
              },
              "action": {
                "type": "string",
                "default": "bind",
                "enum": ["bind", "path"]
              }
            }
          }
        }
      }
    },
    "loading": {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "blocking",
            "non-blocking"
          ],
          "default": "non-blocking",
          "description": "If this view has a high number of children, non-blocking loading will indicate progress as components are loaded."
        }
      }
    },
    "inputBehavior" : {
      "type": "string",
      "enum": [
        "merge",
        "replace"
      ],
      "description": "Controls how input and in/out parameters are either merged with or replace their defaults",
      "default": "replace"
    }
  }
}

4. Add an array to the "root" object with the key "children".
...
"root": {
  "children": [
  ]
...

5. Place component objects into this "children" array. Each component will have its own schema. There are many types of components, including displays, charts, containers, inputs, embedding, and more. Follow the specific instructions for each component.

6. Write out your completed JSON as a View artifact using the provided tool.