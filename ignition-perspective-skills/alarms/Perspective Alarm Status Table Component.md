# Perspective Alarm Status Table Component

## Description

These instructions detail the configuration and usage of the Perspective Alarm Status Table component. They cover how to control the component's core functionality, including the setup of data filters, customization of column display for both standard and associated alarm data, application of conditional visual styles, and management of user interaction controls for actions like acknowledging and shelving alarms.

## Documentation

# Instructions
### Perspective Alarm Status Table Component Instructions

Here is a detailed set of instructions and tips for an LLM on how to interact with and configure the Perspective Alarm Status Table component in Ignition.

---

### **Object Overview**

The Alarm Status Table is a primary component for displaying and managing alarm information within a Perspective session. Its core function is to present a real-time view of the alarm system's state. Users can view currently active and shelved alarms, inspect their details, acknowledge them, and shelve them for specified durations.

The component is highly interactive. In a live session, users can sort by columns, resize column widths by dragging their margins, reorder columns (if `dragOrderable` is true), and show or hide columns by right-clicking the header. It features a built-in toolbar for filtering, configuration, and switching between active and shelved alarm views. For efficiency, the table utilizes a shared polling engine, which caches and shares polling tasks across multiple sessions, reducing the performance impact on the gateway.

---

### **Core Configuration & Properties**

#### **1. Data Source and Filtering**

The alarms displayed are controlled by a set of filter properties.

*   **Gateway-Side Filtering (`filters.active.conditions`)**: This is the most efficient way to filter alarms, as it happens on the Gateway before data is sent to the session.
    *   `provider`: Filter by a specific alarm provider (e.g., "default").
    *   `source`: Filter by the alarm's source path. You can list multiple paths separated by commas. The wildcard `✷` is supported (e.g., `*/Area1/*`).
    *   `displayPath`: Filter by the alarm's display path. This also supports multiple comma-separated paths and the `✷` wildcard.
*   **Client-Side Filtering**: These filters are applied in the user's session.
    *   `filters.active.states`: A set of booleans (`activeAcked`, `clearUnacked`, `activeUnacked`, `clearAcked`) to pre-filter alarms by their state.
    *   `filters.active.priorities`: A set of booleans (`critical`, `high`, `medium`, `low`, `diagnostic`) to pre-filter by priority level.
    *   `filters.active.text` & `filters.shelved.text`: Binds to the text entered in the toolbar's search bar to filter the currently visible alarms.
*   **Polling**:
    *   `refreshRate`: Defines how often the table polls for updates, in milliseconds. The default is 5000ms.

#### **2. Columns and Data Display**

You have extensive control over the columns shown in both the "Active" and "Shelved" tabs.

*   **Standard Columns (`columns`)**: This property contains two objects, `active` and `shelved`, which list all available columns for each view (e.g., `activeTime`, `priority`, `state`, `source`, `expires`). For each column, you can configure:
    *   `enabled`: A boolean to show or hide the column by default.
    *   `order`: The numerical index for the column's position (lower numbers appear first).
    *   `width`: Sets the column width. By default, this is a proportional value (flex grow).
    *   `strictWidth`: If `true`, the `width` becomes a fixed pixel value instead of a proportion.
    *   `sort`: The default sort direction for the column (`ascending`, `descending`, or `none`).
*   **Associated Data Columns (`columnsAssociated.active`)**: Use this to display custom data that is attached to an alarm. This is an array of column configuration objects.
    *   **CRITICAL**: The `field` property for an associated data column **must not** match any of the standard alarm property names (e.g., `priority`, `source`, `state`). You must provide the name of your custom associated data property here.
    *   Configuration options (`enabled`, `order`, `width`, `strictWidth`, `sort`) are the same as for standard columns.
*   **Date Formatting**:
    *   `dateFormat`: A string that formats how any date values are displayed (e.g., "MM/DD/YYYY HH:mm:ss").

#### **3. Styling and Appearance**

*   **Row Styles (`rowStyles`)**: This is the primary way to visually indicate alarm status. You can define separate styles for four different states: `activeUnacked`, `activeAcked`, `clearUnacked`, and `clearAcked`.
    *   Within each state, you can define a `base` style and then override that style for each `priority` (`critical`, `high`, `medium`, `low`, `diagnostic`).
    *   Styles can include `backgroundColor`, `color`, `fontWeight`, etc., or you can assign a pre-defined Style Class.
*   **Layout & Pager**:
    *   `pager.enabled`: Toggles the pager at the bottom of the table.
    *   `pager.options`: An array of numbers defining the "rows per page" options available to the user (e.g., `[10, 25, 50, 100]`).
    *   `pager.initialOption`: The number of rows to show when the component first loads.
    *   `responsive.enabled`: If true, the table will switch to a "card" based layout when the component's width is less than the `responsive.breakpoint` value. This disables some table features that are not applicable to the card layout.
*   **General**:
    *   `enableHeader`: Toggles the visibility of the main table header row.
    *   `style`: Apply standard CSS styles to the component's main container.

#### **4. User Interaction and Actions**

*   **Toolbar (`toolbar`)**: The toolbar's visibility and its features can be configured.
    *   `enabled`: Toggles the entire toolbar.
    *   `enableActiveTab` / `enableShelvedTab`: Show or hide the "Active" and "Shelved" tabs.
    *   `enableFilter`: Shows the filter icon, which reveals the text search bar.
    *   `enablePreFilters`: Shows the icon for toggling states and priorities.
    *   `enableConfiguration`: Shows the icon for toggling column visibility.
*   **Alarm Actions**:
    *   `enableAcknowledge`: Allows users to acknowledge selected alarms.
    *   `enableShelve`: Allows users to shelve selected alarms.
    *   `enableUnshelve`: Allows users to unshelve selected alarms from the shelved list.
    *   `enableDetails`: Allows users to view the details for a selected alarm.
*   **Selection**:
    *   `selection.active.mode` & `selection.shelved.mode`: Determines selection behavior. Can be `"multiple"`, `"single"`, or `"none"`.
    *   `selection.active.data` & `selection.shelved.data`: Read-only properties that contain the alarm objects for the currently selected rows. This is useful for scripting.
*   **Shelving Times**:
    *   `shelvingTimes`: An array of numbers (in seconds) that populates the duration options when a user clicks the "Shelve" button (e.g., `[300, 900, 1800]` for 5, 15, and 30 minutes).

---

### **Extension Functions**

*   **`filterAlarm(alarmEvent)`**: This function is called for every active alarm event before it is displayed. Return `False` to exclude the alarm from the table. Use `alarmEvent.get('propertyName')` to inspect properties like `name`, `source`, and `priority`.
    *   **Example**: `return alarmEvent.get('priority') > 2` would only show High and Critical priority alarms (assuming High=3, Critical=4).
*   **`filterShelvedAlarm(shelvedAlarmEvent)`**: This function is called for every shelved alarm before it is displayed. Return `False` to exclude it. You can inspect properties like `shelvedAlarmEvent.sourcePath` and `shelvedAlarmEvent.shelvedBy`.

---

### **Helpful Tips & Best Practices**

*   **Performance**: For best performance, use the gateway-side filters (`filters.active.conditions`) whenever possible. Avoid enabling `filters.active.results.enabled` or `filters.shelved.results.enabled` unless you absolutely need to bind to the filtered dataset, as it can cause performance degradation.
*   **Default Sort**: Be aware that the `state` and `priority` columns are configured by default to sort in `descending` order. Other columns default to alphanumerical ascending order when sorted. You can set up a multi-column default sort order by adding column names to the `activeSortOrder` or `shelvedSortOrder` arrays.
*   **Associated Data**: When adding `columnsAssociated`, double-check that the `field` name does not overlap with a standard alarm property. This is a common source of errors.
*   **Column Widths**: Remember that column `width` is a proportional "flex" value by default. To set a static pixel width, you must set `strictWidth` to `true`.
*   **Selection Data**: To act on the selected alarms (e.g., with a button outside the component), bind to the `selection.active.data` or `selection.shelved.data` properties. These arrays will contain the full alarm event objects for the selected rows.
*   **Wildcards**: When filtering `source` or `displayPath`, remember to use the `✷` wildcard character to match any characters in a path segment.
*   **Interactivity**: User changes in the session (like reordering or resizing columns) do not automatically save back to the Designer. These are temporary session-based changes. The component will revert to its configured defaults on a page refresh.

* EXAMPLE ARTIFACT CONFIG
{
  "activeSortOrder": [],
  "columns": {
    "active": {
      "ackNotes": {
        "enabled": false,
        "order": 15,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "ackPipeline": {
        "enabled": false,
        "order": 16,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "ackTime": {
        "enabled": false,
        "order": 13,
        "sort": "none",
        "strictWidth": false,
        "width": 150
      },
      "ackUser": {
        "enabled": false,
        "order": 14,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "activePipeline": {
        "enabled": false,
        "order": 17,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "activeTime": {
        "enabled": true,
        "order": 0,
        "sort": "none",
        "strictWidth": false,
        "width": 150
      },
      "clearPipeline": {
        "enabled": false,
        "order": 19,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "clearTime": {
        "enabled": false,
        "order": 18,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "deadband": {
        "enabled": false,
        "order": 20,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "displayPath": {
        "enabled": true,
        "order": 1,
        "sort": "none",
        "strictWidth": false,
        "width": 200
      },
      "eventId": {
        "enabled": false,
        "order": 7,
        "sort": "none",
        "strictWidth": false,
        "width": 150
      },
      "eventValue": {
        "enabled": false,
        "order": 8,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "isAcked": {
        "enabled": false,
        "order": 11,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "isActive": {
        "enabled": false,
        "order": 10,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "isClear": {
        "enabled": false,
        "order": 12,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "label": {
        "enabled": false,
        "order": 5,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "name": {
        "enabled": true,
        "order": 6,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "notes": {
        "enabled": false,
        "order": 9,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      },
      "priority": {
        "enabled": true,
        "order": 2,
        "sort": "descending",
        "strictWidth": false,
        "width": 150
      },
      "source": {
        "enabled": true,
        "order": 4,
        "sort": "none",
        "strictWidth": false,
        "width": 200
      },
      "state": {
        "enabled": true,
        "order": 3,
        "sort": "descending",
        "strictWidth": false,
        "width": ""
      }
    },
    "shelved": {
      "expires": {
        "enabled": true,
        "order": 0,
        "sort": "descending",
        "strictWidth": false,
        "width": 100
      },
      "shelvedBy": {
        "enabled": true,
        "order": 1,
        "sort": "none",
        "strictWidth": false,
        "width": 100
      },
      "sourcePath": {
        "enabled": true,
        "order": 2,
        "sort": "none",
        "strictWidth": false,
        "width": 200
      }
    }
  },
  "columnsAssociated": {
    "active": [
      {
        "enabled": true,
        "field": "",
        "order": 0,
        "sort": "none",
        "strictWidth": false,
        "width": ""
      }
    ]
  },
  "dateFormat": "MM/DD/YYYY HH:mm:ss",
  "dragOrderable": true,
  "enableAcknowledge": true,
  "enableDetails": true,
  "enableHeader": true,
  "enableShelve": true,
  "enableUnshelve": true,
  "filters": {
    "active": {
      "conditions": {
        "displayPath": "",
        "provider": "",
        "source": ""
      },
      "priorities": {
        "critical": true,
        "diagnostic": false,
        "high": true,
        "low": true,
        "medium": true
      },
      "results": {
        "data": [],
        "enabled": false
      },
      "states": {
        "activeAcked": true,
        "activeUnacked": true,
        "clearAcked": false,
        "clearUnacked": true
      },
      "text": ""
    },
    "shelved": {
      "results": {
        "data": [],
        "enabled": false
      },
      "text": ""
    }
  },
  "pager": {
    "activePage": 1,
    "enabled": true,
    "hide": false,
    "initialOption": 25,
    "options": [
      5,
      10,
      25,
      50,
      100
    ],
    "shelvedPage": 1
  },
  "refreshRate": 5000,
  "responsive": {
    "breakpoint": 500,
    "enabled": false
  },
  "rowStyles": {
    "activeAcked": {
      "base": {
        "backgroundColor": "#7C2320",
        "classes": "",
        "color": "#FAFAFB"
      },
      "priorities": {
        "critical": {
          "backgroundColor": "#7C2320"
        },
        "diagnostic": {
          "backgroundColor": "#FFFFFF",
          "color": "#222222"
        },
        "high": {
          "backgroundColor": "#913837"
        },
        "low": {
          "backgroundColor": "#C47977"
        },
        "medium": {
          "backgroundColor": "#AA5553"
        }
      }
    },
    "activeUnacked": {
      "base": {
        "backgroundColor": "#DB3939",
        "classes": "",
        "color": "#FAFAFB",
        "fontWeight": "500"
      },
      "priorities": {
        "critical": {
          "backgroundColor": "#DB3939"
        },
        "diagnostic": {
          "backgroundColor": "#FFFFFF",
          "color": "#222222"
        },
        "high": {
          "backgroundColor": "#E25353"
        },
        "low": {
          "backgroundColor": "#F28787"
        },
        "medium": {
          "backgroundColor": "#E86D6D"
        }
      }
    },
    "clearAcked": {
      "base": {
        "backgroundColor": "#DCDCDC",
        "classes": "",
        "color": "#222222"
      },
      "priorities": {
        "critical": {
          "backgroundColor": "#DCDCDC"
        },
        "diagnostic": {
          "backgroundColor": "#FFFFFF",
          "color": "#222222"
        },
        "high": {
          "backgroundColor": "#E8E8E8"
        },
        "low": {
          "backgroundColor": "#F9F9F9"
        },
        "medium": {
          "backgroundColor": "#F2F2F2"
        }
      }
    },
    "clearUnacked": {
      "base": {
        "backgroundColor": "#2E5EAA",
        "classes": "",
        "color": "#FAFAFB",
        "fontWeight": "500"
      },
      "priorities": {
        "critical": {
          "backgroundColor": "#2E5EAA"
        },
        "diagnostic": {
          "backgroundColor": "#FFFFFF",
          "color": "#222222"
        },
        "high": {
          "backgroundColor": "#507ABF"
        },
        "low": {
          "backgroundColor": "#A0BEEF"
        },
        "medium": {
          "backgroundColor": "#7198D6"
        }
      }
    }
  },
  "selection": {
    "active": {
      "data": [],
      "mode": "multiple"
    },
    "shelved": {
      "data": [],
      "mode": "multiple"
    }
  },
  "shelvedSortOrder": [],
  "shelvingTimes": [
    300,
    900,
    1800,
    3600,
    7200,
    14400
  ],
  "style": {
    "classes": ""
  },
  "toolbar": {
    "enableActiveTab": true,
    "enableConfiguration": true,
    "enableFilter": true,
    "enableFilterResults": true,
    "enablePreFilters": true,
    "enableShelvedTab": true,
    "enabled": true,
    "toggleableFilter": true
  }
}


# Schema - raw
{"schema":{"type":"object","definitions":{"columnConfig":{"type":"object","properties":{"sort":{"description":"Default sort order of this column.","type":"string","enum":["none","ascending","descending"],"default":"none"},"enabled":{"description":"Toggle visibility of column.","type":"boolean","default":false},"strictWidth":{"description":"If enabled, the width of the column becomes fixed.","type":"boolean","default":false},"width":{"description":"The column's width which, when not strict, represents a proportion of the available space, i.e. flex grow. If strictWidth is enabled, will be fixed and static.","type":["number","string"],"default":""},"order":{"description":"The index position of this column relative to other columns.","type":"number","default":0}}}},"properties":{"shelvedSortOrder":{"description":"The default weighted order in which columns and their contents are sorted relative to other columns and their contents. Used when the component first loads. Shelved event columns need to have sort configured in order for this to work.","type":"array","default":[]},"rowStyles":{"description":"Styles to apply to rows given their alarm state and designated priority.","type":"object","properties":{"activeAcked":{"type":"object","properties":{"priorities":{"type":"object","properties":{"critical":{"default":{"backgroundColor":"#7C2320"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"medium":{"default":{"backgroundColor":"#AA5553"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"high":{"default":{"backgroundColor":"#913837"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"low":{"default":{"backgroundColor":"#C47977"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"diagnostic":{"default":{"backgroundColor":"#FFFFFF","color":"#222222"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"base":{"default":{"backgroundColor":"#7C2320","color":"#FAFAFB","classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"clearUnacked":{"type":"object","properties":{"priorities":{"type":"object","properties":{"critical":{"default":{"backgroundColor":"#2E5EAA"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"medium":{"default":{"backgroundColor":"#7198D6"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"high":{"default":{"backgroundColor":"#507ABF"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"low":{"default":{"backgroundColor":"#A0BEEF"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"diagnostic":{"default":{"backgroundColor":"#FFFFFF","color":"#222222"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"base":{"default":{"backgroundColor":"#2E5EAA","color":"#FAFAFB","classes":"","fontWeight":"500"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"activeUnacked":{"type":"object","properties":{"priorities":{"type":"object","properties":{"critical":{"default":{"backgroundColor":"#DB3939"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"medium":{"default":{"backgroundColor":"#E86D6D"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"high":{"default":{"backgroundColor":"#E25353"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"low":{"default":{"backgroundColor":"#F28787"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"diagnostic":{"default":{"backgroundColor":"#FFFFFF","color":"#222222"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"base":{"default":{"backgroundColor":"#DB3939","color":"#FAFAFB","classes":"","fontWeight":"500"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"clearAcked":{"type":"object","properties":{"priorities":{"type":"object","properties":{"critical":{"default":{"backgroundColor":"#DCDCDC"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"medium":{"default":{"backgroundColor":"#F2F2F2"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"high":{"default":{"backgroundColor":"#E8E8E8"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"low":{"default":{"backgroundColor":"#F9F9F9"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"diagnostic":{"default":{"backgroundColor":"#FFFFFF","color":"#222222"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"base":{"default":{"backgroundColor":"#DCDCDC","color":"#222222","classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}}},"dateFormat":{"description":"A date format string to be applied against dates.","type":["string","number"],"default":"MM/DD/YYYY HH:mm:ss","suggestions":{"time [3:59:00 PM]":"h:mm:ss a","date [10/15/2018]":"MM/DD/YYYY","none":"none","date time [10/15/2018 15:59:00]":"MM/DD/YYYY HH:mm:ss"}},"columns":{"description":"Used only for determining what columns to show on load.","type":"object","properties":{"active":{"description":"Active alarm event columns to display on load.","type":"object","properties":{"activePipeline":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":17},"$ref":"#/definitions/columnConfig"},"eventId":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":150,"order":7},"$ref":"#/definitions/columnConfig"},"ackTime":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":150,"order":13},"$ref":"#/definitions/columnConfig"},"notes":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":9},"$ref":"#/definitions/columnConfig"},"clearTime":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":18},"$ref":"#/definitions/columnConfig"},"activeTime":{"default":{"sort":"none","enabled":true,"strictWidth":false,"width":150,"order":0},"$ref":"#/definitions/columnConfig"},"ackNotes":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":15},"$ref":"#/definitions/columnConfig"},"displayPath":{"default":{"sort":"none","enabled":true,"strictWidth":false,"width":200,"order":1},"$ref":"#/definitions/columnConfig"},"source":{"default":{"sort":"none","enabled":true,"strictWidth":false,"width":200,"order":4},"$ref":"#/definitions/columnConfig"},"label":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":5},"$ref":"#/definitions/columnConfig"},"priority":{"default":{"sort":"descending","enabled":true,"strictWidth":false,"width":150,"order":2},"$ref":"#/definitions/columnConfig"},"isActive":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":10},"$ref":"#/definitions/columnConfig"},"ackUser":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":14},"$ref":"#/definitions/columnConfig"},"isClear":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":12},"$ref":"#/definitions/columnConfig"},"isAcked":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":11},"$ref":"#/definitions/columnConfig"},"eventValue":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":8},"$ref":"#/definitions/columnConfig"},"name":{"default":{"sort":"none","enabled":true,"strictWidth":false,"width":"","order":6},"$ref":"#/definitions/columnConfig"},"deadband":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":20},"$ref":"#/definitions/columnConfig"},"state":{"default":{"sort":"descending","enabled":true,"strictWidth":false,"width":"","order":3},"$ref":"#/definitions/columnConfig"},"clearPipeline":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":19},"$ref":"#/definitions/columnConfig"},"ackPipeline":{"default":{"sort":"none","enabled":false,"strictWidth":false,"width":"","order":16},"$ref":"#/definitions/columnConfig"}}},"shelved":{"description":"Shelved alarm columns to display on load.","type":"object","properties":{"expires":{"default":{"sort":"descending","enabled":true,"strictWidth":false,"width":100,"order":0},"$ref":"#/definitions/columnConfig"},"shelvedBy":{"default":{"sort":"none","enabled":true,"strictWidth":false,"width":100,"order":1},"$ref":"#/definitions/columnConfig"},"sourcePath":{"default":{"sort":"none","enabled":true,"strictWidth":false,"width":200,"order":2},"$ref":"#/definitions/columnConfig"}}}}},"enableAcknowledge":{"description":"Enable acknowledge action.","type":"boolean","default":true},"filters":{"type":"object","properties":{"active":{"type":"object","properties":{"states":{"description":"Pre filters for filter active alarm events.","type":"object","properties":{"activeAcked":{"type":"boolean","default":true},"clearUnacked":{"type":"boolean","default":true},"activeUnacked":{"type":"boolean","default":true},"clearAcked":{"type":"boolean","default":false}}},"priorities":{"description":"Alarm state priority pre-filters.","type":"object","properties":{"critical":{"type":"boolean","default":true},"medium":{"type":"boolean","default":true},"high":{"type":"boolean","default":true},"low":{"type":"boolean","default":true},"diagnostic":{"type":"boolean","default":false}}},"text":{"description":"The active alarm events filter text.","type":"string","default":""},"conditions":{"description":"Gateway side alarm query conditions.","type":"object","properties":{"source":{"description":"Filter alarms by alarm source path. Specify multiple paths by separating them with commas. Supports the wildcard ✷","type":"string","default":""},"displayPath":{"description":"Filter alarms by alarm display path, falling back to the source path if a custom display path isn't set. Specify multiple paths by separating them with commas. Supports the wildcard ✷.","type":"string","default":""},"provider":{"description":"Filter alarms by alarm provider.","type":"string","default":""}}},"results":{"description":"Active alarm filtering results configuration and data.","type":"object","properties":{"data":{"description":"An array of objects representing the current filtered data. If enabled and active.","type":"array","default":[],"items":{"type":"object","properties":{}}},"enabled":{"description":"Enable filter results to be written back to props.  Warning, doing so may cause performance decline.","type":"boolean","default":false}}}}},"shelved":{"type":"object","properties":{"text":{"description":"The filter text for shelved alarms.","type":"string","default":""},"results":{"description":"Shelved alarm filtering results configuration and data.","type":"object","properties":{"data":{"description":"An array of objects representing the current filtered data. If enabled and active.","type":"array","default":[],"items":{"type":"object","properties":{}}},"enabled":{"description":"Enable filter results to be written back to props.  Warning, doing so may cause performance decline.","type":"boolean","default":false}}}}}}},"activeSortOrder":{"description":"The default weighted order in which columns and their contents are sorted relative to other columns and their contents. Used when the component first loads. Active event columns need to have sort configured in order for this to work.","type":"array","default":[]},"dragOrderable":{"description":"Users may drag column headers to reorder columns of the table.","type":"boolean","default":true},"enableDetails":{"description":"Enable active events table details action.","type":"boolean","default":true},"enableShelve":{"description":"Enable shelve action.","type":"boolean","default":true},"toolbar":{"type":"object","properties":{"toggleableFilter":{"visibleWhen":{"equals":true,"property":"enableFilter"},"description":"If false, the text filter will not require user interaction to open, and instead will remain open.","type":"boolean","default":true},"enablePreFilters":{"description":"Enables the visibility of the pre filter toggle.","type":"boolean","default":true},"enableConfiguration":{"description":"Enables the visibility of the configuration toggle.","type":"boolean","default":true},"enabled":{"description":"Enables the visibility of the table toolbar.","type":"boolean","default":true},"enableFilterResults":{"description":"Enables the visibility of the filters results count message.","type":"boolean","default":true},"enableActiveTab":{"description":"Enables the visibility of the active events tab.","type":"boolean","default":true},"enableFilter":{"description":"Enables the visibility of the text filter toggle.","type":"boolean","default":true},"enableShelvedTab":{"description":"Enables the visibility of the shelved events tab.","type":"boolean","default":true}}},"selection":{"description":"Currently selected alarms and alarm selection configuration","type":"object","properties":{"active":{"description":"Active alarm selection configuration and read-only list of currently selected active alarms","type":"object","properties":{"data":{"description":"A read-only list of currently selected active alarms.","type":"array","default":[]},"mode":{"description":"Active alarm selection configuration","type":"string","enum":["single","multiple","none"],"default":"multiple"}}},"shelved":{"description":"Shelved alarm selection configuration and read-only list of currently selected shelved alarms","type":"object","properties":{"data":{"description":"A read-only list of currently selected shelved alarms.","type":"array","default":[]},"mode":{"description":"Shelved alarm selection configuration","type":"string","enum":["single","multiple","none"],"default":"multiple"}}}}},"pager":{"description":"","type":"object","properties":{"initialOption":{"description":"The initial option to use when the table first loads. It must exist as an available option.","type":"number","default":25},"activePage":{"description":"Represents the current active page and corresponds to the value of the page jump input field.","type":"number","default":1},"enabled":{"description":"Enable pager.","type":"boolean","default":true},"hide":{"description":"Visually hides the pager from view.  Useful when pager is manipulated in a controlled fashion via the activePage prop.","type":"boolean","default":false},"options":{"description":"Rows to show per pager option.","type":"array","default":[5,10,25,50,100],"items":{"type":"number"}},"shelvedPage":{"description":"Represents the current shelved page and corresponds to the value of the page jump input field.","type":"number","default":1}}},"refreshRate":{"description":"The rate at which the table will poll for updates in milliseconds.","type":"number","default":5000},"responsive":{"description":"Responsive layout configuration.  Rows are converted to cards. While in responsive layout, disables or removes certain table features that are no longer applicable.","type":"object","properties":{"enabled":{"description":"Enables responsive layout.","type":"boolean","default":false},"breakpoint":{"description":"Width, in pixels, that triggers change in responsive layout.","type":"number","default":500}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"enableUnshelve":{"description":"Enable unshelve action.","type":"boolean","default":true},"shelvingTimes":{"description":"Available alarm shelving times in seconds.","type":"array","default":[300,900,1800,3600,7200,14400],"items":{"type":"number"}},"enableHeader":{"description":"Enable table header.","type":"boolean","default":true},"columnsAssociated":{"description":"Columns of associated data and their configurations.","type":"object","properties":{"active":{"description":"A list of columns and their configurations used in the retrieval and display of associated alarm data.","type":"array","items":{"type":"object","additionalProperties":false,"properties":{"sort":{"description":"Default sort order of this column.","type":"string","enum":["none","ascending","descending"],"default":"none"},"enabled":{"description":"Toggles the visibility of column.","type":"boolean","default":true},"strictWidth":{"description":"If enabled, the width of the column becomes fixed.","type":"boolean","default":false},"field":{"description":"The name of the associated alarm data property.  It must not match any of the common properties listed in the 'columns' property.","type":"string","default":"","not":{"enum":["activeTime","displayPath","priority","state","source","label","name","eventId","eventValue","notes","isActive","isAcked","isClear","ackTime","ackUser","ackNotes","ackPipeline","activePipeline","clearTime","clearPipeline","deadband"]}},"width":{"description":"The column's width which, when not strict, represents a proportion of the available space, i.e. flex grow. If strictWidth is enabled, will be fixed and static.","type":["number","string"],"default":""},"order":{"description":"The index position of this column relative to other columns.","type":"number","default":0}}}}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"AlarmStatusTable","name":"Alarm Status Table","palette":{"variants":[{"tooltip":"Displays the current state of the alarm system. Can be configured to show active, cleared, and acknowledged events.","label":"Alarm Status Table"}],"category":"display"},"extensionFunctions":[{"defaultImplementation":"\treturn True","description":"Called for each alarm event before it is displayed in the table. Return False to exclude the alarm from the table.","name":"filterAlarm","arguments":[{"description":"The alarm event itself. Use <code>alarmEvent.get('propertyName')</code> to inspect. Common properties include 'name', 'source', and 'priority'.","type":"AlarmEvent","name":"alarmEvent"}]},{"defaultImplementation":"\treturn True","description":"Called for each shelved alarm event before it is displayed in the table. Return False to exclude the shelved alarm from the table.","name":"filterShelvedAlarm","arguments":[{"description":"Holds details about the shelved alarm.","type":{"methods":[],"name":"ShelveEvent","attributes":[{"kind":"INSTANCE_MEMBER","type":"str","name":"sourcePath","location":"ShelveEvent"},{"kind":"INSTANCE_MEMBER","type":"str","name":"shelvedBy","location":"ShelveEvent"},{"kind":"INSTANCE_MEMBER","type":"long","name":"expires","location":"ShelveEvent"}],"items":[]},"name":"shelvedAlarmEvent"}]}],"id":"ia.display.alarmstatustable"}