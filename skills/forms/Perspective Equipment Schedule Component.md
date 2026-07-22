# Perspective Equipment Schedule Component

## Description

This document describes the configuration and usage of the Perspective Equipment Schedule Component, a visual tool for displaying and managing time-based events like production runs and downtime. The instructions cover how to populate the schedule with data, customize its visual appearance, and implement user interactivity by scripting the component's events to handle actions such as creating, moving, and resizing events to update a backend data source.

## Documentation

# Instructions
Of course! Here are the instructions for the LLM on how to use the Perspective Equipment Schedule Component in Ignition.

***

# Perspective Equipment Schedule Component Instructions

## Introduction

The Perspective Equipment Schedule is a powerful visualization component used to display and manage time-based events associated with specific items, such as machinery, production lines, or personnel. It provides a Gantt-chart-like interface where users can view, create, move, resize, and delete events within a configurable time window. Its primary purpose is to offer a clear, concise, and interactive overview of scheduling information.

## Core Concepts

The Equipment Schedule is built around a few key data concepts. Understanding these is crucial for configuring the component effectively.

*   **Items:** These represent the rows in the schedule. Each item corresponds to a piece of equipment, a person, or any entity you want to schedule events for. The `items` property is an array of objects, and each object **must** have a unique `id` that links it to its associated events.
*   **Scheduled Events:** These are the primary blocks of time displayed on the schedule grid. They represent tasks, production runs, or appointments. The `scheduledEvents` property is an array of event objects. Each event is mapped to a specific row using its `itemId` property, which must match the `id` of an item. Each event must also have a unique `eventId`.
*   **Downtime Events:** These are special events used to represent periods when an item is not operational (e.g., for maintenance or a fault). They are visually distinct from scheduled events and can be configured to render underneath them. Like scheduled events, they are mapped to rows using the `itemId` property.
*   **Break Events:** These are global, schedule-wide events, such as a company-wide lunch break or a shift change. They apply to *all* items simultaneously and are displayed across every row. They do not have an `itemId`.
*   **Date & Time:** All events (`scheduledEvents`, `downtimeEvents`, `breakEvents`) are defined by a `startDate` and an `endDate`. These properties can accept date objects, or more commonly, a number representing the milliseconds since the Unix epoch (Jan 1, 1970). Component events (`onMoveEvent`, `onResizeEvent`, etc.) will output start and end times as numbers (milliseconds).
*   **User Interaction & Events:** The component can be made interactive, allowing users to modify events by dragging, resizing, or deleting them. Each of these actions triggers a corresponding component event (e.g., `onMoveEvent`). You must write scripts on these events to process the changes and update your backend data source (like a database).

---

## Configuration & Properties

Below are detailed instructions for configuring the component's properties.

### **Data Properties**

These properties provide the data the component will display. They are almost always bound to a database query or a Tag.

*   **`items`**: An array of objects defining the rows of the schedule.
    *   **`id`**: (Required) A unique identifier (string or number) for the item. This is used to link events to this row. If no `id` is specified, the row will not be created.
    *   **`label`**: The text to display in the row header. Defaults to "New Item".
    *   **Styling**: You can style individual rows using properties like `headerBackgroundColor`, `headerFontColor`, `rowStyle`, `headerStyle`, etc.

*   **`scheduledEvents`**: An array of objects defining the primary events on the schedule.
    *   **`eventId`**: (Required) A unique identifier (string or number) for this specific event.
    *   **`itemId`**: (Required) The `id` of the item this event belongs to.
    *   **`startDate`, `endDate`**: The start and end times for the event.
    *   **`label`**: The text displayed on the event block.
    *   **`percentDone`**: A number from 0 to 100 that controls the fill level of the event's progress bar (if enabled).
    *   **`leadTime`**: A duration in seconds that displays a "lead time" visual before the event's `startDate`.
    *   **Styling**: You can style individual events with `backgroundColor`, `borderColor`, `borderWidth`, `fontColor`, etc. These will override the global `scheduledEventStyle`.

*   **`downtimeEvents`**: An array of objects representing downtime.
    *   **`itemId`**: The `id` of the item this downtime belongs to.
    *   **`startDate`, `endDate`**: The start and end times for the downtime.
    *   **`underlay`**: A boolean. If `true`, the downtime event will render *underneath* any overlapping scheduled events.
    *   **Styling**: Use `color` and `opacity` to define the appearance. These settings override the global `downtimeEventStyle`.

*   **`breakEvents`**: An array of objects for global breaks.
    *   **`startDate`, `endDate`**: The start and end times for the break.
    *   **`style`**: A style object to control the appearance of the break event. This will override the global `breakEventStyle`.

### **Appearance & Style Properties**

These properties control the overall look and feel of the component.

*   **`rowHeight`**: Sets the height in pixels for each item row.
*   **`dateRange`**: An object with `startDate` and `endDate` properties that defines the visible time window of the component. If the range is invalid, it defaults to a week starting from the current day.
*   **`defaultZoom`**: Sets the initial zoom level when the component loads. Options include "month", "day", "12-hr", "8-hr", "6-hr", "3-hr", "hours", and "minutes".
*   **`progressBar`**: An object for configuring the progress bars on scheduled events.
    *   **`enabled`**: Set to `true` to show progress bars.
    *   **`bar` / `track`**: Objects to set the color and style of the progress bar itself and its background track.
    *   **`valueDisplay`**: An object to configure the numeric percentage display on the progress bar, including a `format` string, `justify` position, and `style`.
*   **Global Styles**: Properties ending in `Style` (`rowStyle`, `bodyStyle`, `scheduledEventStyle`, `downtimeEventStyle`, `breakEventStyle`, `selectedEventStyle`) are style objects that apply a base style to all corresponding elements. These can be overridden by more specific styles on individual items or events.
*   **`currentTimeIndicator`**: An object to configure the vertical line that indicates the current time. You can set its `color`, `width`, and `opacity`.

### **Interaction Properties**

These boolean properties enable or disable specific UI interactions.

*   **`addEnabled`**: Allows users to create new events by clicking and dragging on an empty area of the schedule grid.
*   **`moveEnabled`**: Allows users to move existing events by dragging them.
*   **`resizeEnabled`**: Allows users to change the duration of an event by dragging its start or end handles.
*   **`deleteEnabled`**: Allows users to delete events (often via a right-click menu you must configure).
*   **`clickEnabled`**: Allows users to select an event by clicking on it.

### **Read-Only Properties**

*   **`selectedEvent`**: An object containing the `eventId` and `itemId` of the last event the user clicked. You can bind to this property to display details about the selected event elsewhere in the view.

---

## Component Events

To make the schedule interactive, you must add scripts to these component events. The typical workflow is to use the event to run a script (e.g., a Named Query) that updates a database, and then rely on the property binding on `scheduledEvents` to refresh the component's display.

*   **`onAddEvent`**: Fires after a user draws a new event.
    *   **Event Object**: Contains `start`, `end`, and `itemId`. Use this to `INSERT` a new record into your database.
*   **`onMoveEvent`**: Fires after a user drags and drops an event to a new time or a new item row.
    *   **Event Object**: Contains `eventId`, `start`, `end`, and `itemId`. Use this to `UPDATE` the corresponding record in your database.
*   **`onResizeEvent`**: Fires after a user resizes an event.
    *   **Event Object**: Contains `eventId`, `start`, `end`, and `itemId`. Use this to `UPDATE` the start/end times of the record in your database.
*   **`onDeleteEvent`**: Fires after an event is deleted (e.g., via a script you trigger).
    *   **Event Object**: Contains `eventId`, `start`, `end`, and `itemId`. Use this to `DELETE` the record from your database.
*   **`onClickEvent`**: Fires when a user clicks on a scheduled event.
    *   **Event Object**: Contains `eventId`, `start`, `end`, and `itemId`. This is useful for populating other controls with details about the selected event.

---

## **Helpful Tips and Best Practices**

*   **Data Binding is Key**: The `items`, `scheduledEvents`, `downtimeEvents`, and `breakEvents` properties are designed to be bound. The most common and robust pattern is to bind them to a Named Query that returns data in the correct JSON format.
*   **Always Use Unique IDs**: Ensure that `items.id` values are unique among all items, and `scheduledEvents.eventId` values are unique among all scheduled events. Duplicate IDs will cause unpredictable behavior.
*   **Master the Interactivity Loop**: The standard interactive pattern is:
    1.  User modifies an event in the UI.
    2.  The corresponding component event (`onMoveEvent`, etc.) fires.
    3.  Your script on that event runs a Named Query to update your database.
    4.  The binding on the `scheduledEvents` property automatically re-queries the database.
    5.  The component refreshes with the new data, confirming the change.
*   **Styling Precedence**: Remember the styling hierarchy. The most specific style wins. The `selectedEventStyle` overrides everything. An individual event's style (e.g., `scheduledEvents[0].backgroundColor`) will override the global `scheduledEventStyle`.
*   **Handling Overlaps**: The component does *not* natively prevent users from creating overlapping events for the same item. If this is required, you must build this validation logic into your `onAddEvent` and `onMoveEvent` scripts before you commit the changes to your database.
*   **Date Formats**: While the component can interpret different date formats, using milliseconds since the epoch (which is what Ignition's scripting functions and expression language often return) is the most reliable method. Note that component event scripts provide `start` and `end` times as numbers (milliseconds).
*   **Use `selectedEvent` for Details**: Bind other components (like labels or a sub-view) to the `props.selectedEvent` property to create a "details-on-selection" experience for the user.

# Schema - raw
{"schema":{"type":"object","properties":{"headerStyles":{"type":"object","properties":{"primaryHeaderStyle":{"description":"Style applied to the primary, top-level header.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"secondaryHeaderStyle":{"description":"Style applied to the secondary, grouping header. This will only style the backdrop.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"tertiaryHeaderStyle":{"description":"Style applied to the tertiary, unit header. This will only style the backdrop.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"breakEvents":{"description":"List of break events. These are scheduled breaks that are applied to all events.","type":["array","dataset"],"default":[],"items":{"type":"object","properties":{"endDate":{"description":"Defines the end date of the break event.","type":["date","number","null"],"default":null},"style":{"description":"Style applied to the break event.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"startDate":{"description":"Defines the start date of the break event.","type":["date","number","null"],"default":null}}}},"defaultZoom":{"description":"Defines the default zoom level on load. Will be restricted to the maximum possible zoom level.","enum":["month","day","12-hr","8-hr","6-hr","3-hr","hours","minutes"],"default":"hours"},"dateRange":{"description":"The visible date range of the equipment schedule. If a non-valid range is provided, will default a week from today.","type":"object","properties":{"endDate":{"type":["date","number","null"],"default":null},"startDate":{"type":["date","number","null"],"default":null}}},"rowStyle":{"description":"Base style that is applied to all items.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"bodyStyle":{"description":"Style that is applied to the body of the grid space. This will only affect the back drop.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"resizeEnabled":{"description":"Enables or disables the UI interaction and event handling of resizing events.","type":"boolean","default":true},"addEnabled":{"description":"Enables or disables the UI interaction and event handling of adding events.","type":"boolean","default":true},"deleteEnabled":{"description":"Enables or disables the UI interaction and event handling of deleting events.","type":"boolean","default":true},"downtimeEvents":{"type":["array","dataset"],"default":[],"items":{"type":"object","properties":{"color":{"format":"color","description":"Defines the color of the downtime event.","type":"string","default":""},"endDate":{"description":"The end date of the downtime event.","type":["date","number","null"],"default":null},"underlay":{"type":"boolean","descriptions":"Defines whether this downtime even should display above or below other events.","default":false},"itemId":{"description":"The item identifier that is associated with this downtime event.","type":["string","number"],"default":""},"style":{"description":"Style applied to the downtime event.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"Defines the opacity of the downtime event.","type":"number","default":1},"startDate":{"description":"The start date of the downtime event.","type":["date","number","null"],"default":null}}}},"downtimeEventStyle":{"description":"Base style that is applied to all downtime events.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"moveEnabled":{"description":"Enables or disables the UI interaction and event handling of moving events.","type":"boolean","default":true},"clickEnabled":{"description":"Enables or disables the UI interaction and event handling of clicking events.","type":"boolean","default":true},"currentTimeIndicator":{"type":"object","properties":{"color":{"format":"color","description":"The color of the time indicator.","type":"string","default":"#0C7BB3"},"width":{"description":"The width of the time indicator.","type":"number","default":2},"opacity":{"description":"The opacity of the time indicator.","type":"number","default":1}}},"progressBar":{"description":"Style to be applied to all progress bars of scheduled events.","type":"object","properties":{"enabled":{"description":"Determines if progress bars should display on scheduled events.","type":"boolean","default":true},"valueDisplay":{"type":"object","properties":{"format":{"description":"Determines the format of the displayed value.","type":"string","default":"0,0.##","suggestions":{"integer [1,200]":"0,0","none":"none","percent [10.12%]":"0.##%","currency [$1,000.12]":"$0,0.00","duration [24:01:00]":"00:00:00"}},"enabled":{"description":"Determines whether or not to show the value along the progress bar.","type":"boolean","default":false},"justify":{"description":"Determines the location of the value display.","type":"string","enum":["left","center","right"],"default":"center"},"style":{"description":"Style applied to the value display.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"bar":{"type":"object","properties":{"color":{"format":"color","type":"string","default":"#323232"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"track":{"type":"object","properties":{"color":{"format":"color","type":"string","default":"#FFFFFF"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}}},"scheduledEvents":{"description":"List of scheduled events.","type":["array","dataset"],"default":[],"items":{"type":"object","properties":{"eventId":{"description":"The identifier that used to distinguish this event. Should be unique among other events.","type":["string","number"],"default":""},"backgroundColor":{"format":"color","description":"The background color for the scheduled event.","type":"string"},"borderColor":{"format":"color","description":"The border color for the scheduled event.","type":"string"},"percentDone":{"description":"The percent completion of the event.","type":"number","default":0},"endDate":{"description":"The end date of this event.","type":["date","number","null"],"default":null},"leadBackgroundColor":{"format":"color","description":"The background color of the lead time. Will be overwritten by the lead style.","type":"string"},"leadTime":{"description":"The lead time of this event defined in seconds.","type":"number","default":0},"label":{"description":"The label to be used as the title of the event. Uses the ID if empty.","type":["string","number"],"default":"Scheduled Event"},"leadStyle":{"description":"Style applied to the lead time","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"itemId":{"description":"The item identifier that is this event associates with.","type":["string","number"],"default":""},"borderWidth":{"description":"The border width for the scheduled event.","type":"number"},"style":{"description":"Style applied to the scheduled event.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"borderStyle":{"description":"The border color for the scheduled event.","type":"string"},"startDate":{"description":"The start date of this event.","type":["date","number","null"],"default":null},"fontColor":{"format":"color","description":"The font color for the label in the scheduled event.","type":"string"},"fontWeight":{"description":"The font weight for the label in the scheduled event.","type":["number","string"]}}}},"scheduledEventStyle":{"description":"Base style that is applied to all scheduled events.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"breakEventStyle":{"description":"Base style that is applied to all break events.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"style":{"description":"Style that is applied to the equipment schedule.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"selectedEvent":{"description":"The last selected scheduled event.","type":"object","properties":{"eventId":{"type":["number","string"],"default":""},"itemId":{"type":["number","string"],"default":""}}},"items":{"type":["array","dataset"],"items":{"type":"object","properties":{"headerBackgroundColor":{"format":"color","description":"The background color of the label used for the item.","type":"string"},"rowStyle":{"description":"Style applied to the item.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"label":{"description":"The label to be used as the title of the row. Uses the ID if empty.","type":"string","default":"New Item"},"rowBackgroundColor":{"format":"color","description":"The background color for the item.","type":"string"},"rowBottomBorderStyle":{"description":"The border bottom style for the item.","type":"string"},"headerStyle":{"description":"Style applied to the label header.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"iconConfig":{"description":"Icon to be displayed in the item next to the label.","$ref":"urn:ignition-schema:schemas/icon-schema.json"},"headerFontSize":{"description":"The font size of the label used for the item.","type":"number"},"rowBottomBorderWidth":{"description":"The border bottom width for the item.","type":"string"},"rowBottomBorderColor":{"format":"color","description":"The border bottom color for the item.","type":"string"},"id":{"description":"Item identifier that is used to map scheduled events and downtime. If no id is specified, then no row is created in the schedule.","type":["string","number"],"default":""},"headerFontColor":{"format":"color","description":"The font color of the label used for the item.","type":"string"}}}},"selectedEventStyle":{"description":"Style that is applied on the selected event. This will override any styling applied to the scheduled event.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"rowHeight":{"description":"Defined the row item height, as well as the grid size.","type":"number","default":46}}},"defaultMetaName":"EquipmentSchedule","name":"Equipment Schedule","palette":{"variants":[{"tooltip":"A component that provides a visualization that conveys equipment scheduling information in a concise and easily digestible format.","label":"Equipment Schedule"}],"category":"display"},"id":"ia.display.equipmentschedule","events":[{"schema":{"description":"","type":"object","properties":{"start":{"description":"The start date of the created event.","type":["number"]},"itemId":{"description":"The item identifier where this event was created in.","type":["string","number"]},"end":{"description":"The end date of the created event.","type":["number"]}}},"documentationUrl":"https://links.inductiveautomation.com/81-equipment-schedule-component-events","description":"Fired after the event has been added.","name":"onAddEvent"},{"schema":{"type":"object","properties":{"eventId":{"description":"The event identifier of the event that was moved.","type":["string","number"]},"start":{"description":"The new start date of the moved event.","type":["number"]},"itemId":{"description":"The item identifier where this event was moved.","type":["string","number"]},"end":{"description":"The new end date of the moved event.","type":["number"]}}},"documentationUrl":"https://links.inductiveautomation.com/81-equipment-schedule-component-events","description":"Fired after the event has been moved.","name":"onMoveEvent"},{"schema":{"type":"object","properties":{"eventId":{"description":"The event identifier of the event that was resized.","type":["string","number"]},"start":{"description":"The new start date of the resized event.","type":"number"},"itemId":{"description":"The item identifier where this event was resized.","type":["string","number"]},"end":{"description":"The new end date of the resized event.","type":"number"}}},"documentationUrl":"https://links.inductiveautomation.com/81-equipment-schedule-component-events","description":"Fired after the event has been resized","name":"onResizeEvent"},{"schema":{"type":"object","properties":{"eventId":{"description":"The event identifier of the event that was deleted.","type":["string","number"]},"start":{"description":"The start date of the deleted event.","type":"number"},"itemId":{"description":"The item identifier where this event was deleted.","type":["string","number"]},"end":{"description":"The end date of the deleted event.","type":"number"}}},"documentationUrl":"https://links.inductiveautomation.com/81-equipment-schedule-component-events","description":"Fired after the event has been deleted","name":"onDeleteEvent"},{"schema":{"type":"object","properties":{"eventId":{"description":"The event identifier of the event that was clicked.","type":["string","number"]},"start":{"description":"The start date of the clicked event.","type":["number"]},"itemId":{"description":"The item identifier where this event was clicked.","type":["string","number"]},"end":{"description":"The end date of the clicked event.","type":["number"]}}},"documentationUrl":"https://links.inductiveautomation.com/81-equipment-schedule-component-events","description":"Fired after the event has been clicked","name":"onClickEvent"}]}