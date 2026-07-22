# Perspective Moving Analog Indicator

## Description

This document explains the usage and configuration of the Perspective Moving Analog Indicator component. The instructions detail how to visually represent a single analog value on a scale that can be segmented into distinct, colored sections. These sections provide immediate context for various operational states, such as normal, alarm, and interlock conditions.

## Documentation

# Instructions
# Perspective Moving Analog Indicator Instructions

This document provides a detailed set of instructions and helpful tips for an LLM to understand and interact with the Perspective Moving Analog Indicator component in Ignition.

## Instructions

### 1. Core Functionality

The primary purpose of the Moving Analog Indicator is to display a single analog value (`processValue`) visually against a scale defined by a `minValue` and `maxValue`. The key feature is the ability to break this scale into different colored sections or ranges that give an operator immediate context about the state of the value (e.g., normal, in alarm, etc.).

The component is composed of a segmented bar and an arrow indicator. The bar shows the various defined ranges, and the arrow points to the current `processValue` on that bar.

### 2. Orientation

The component will automatically orient itself based on its dimensions:
*   If the component's **height is greater than its width**, it will display as a vertical bar.
*   If the component's **width is greater than its height**, it will display as a horizontal bar.

### 3. Key Properties

#### 3.1. Primary Values

*   `processValue` (Number): This is the main value you want to display. The indicator arrow will point to this value on the scale.
*   `setpointValue` (Number | null): An optional value that displays a separate marker on the scale. This is useful for showing a target value in relation to the current `processValue`. If not needed, it should be set to `null`.
*   `minValue` (Number): The minimum value of the scale. Default is `0`.
*   `maxValue` (Number): The maximum value of the scale. Default is `100`.

#### 3.2. Range Definitions

These properties define the boundaries for the different colored sections on the indicator's bar. All range boundaries are optional and can be set to `null` to disable them.

*   **Desired Range:** This typically represents the normal or ideal operating range.
    *   `desiredLow` (Number | null): The lower limit of the 'desired' range.
    *   `desiredHigh` (Number | null): The upper limit of the 'desired' range.

*   **Alarm Ranges (Level 2):** Standard, non-critical alarms.
    *   `lowAlarm` (Number | null): Any value below this is considered a low alarm.
    *   `highAlarm` (Number | null): Any value above this is considered a high alarm.

*   **Alarm Ranges (Level 1):** More critical alarms (e.g., high-high).
    *   `lowLowAlarm` (Number | null): Any value below this is considered a low-low alarm.
    *   `highHighAlarm` (Number | null): Any value above this is considered a high-high alarm.

*   **Interlock Ranges:** The most critical ranges, often indicating a condition that requires immediate shutdown or intervention.
    *   `lowInterlock` (Number | null): Any value below this activates an interlock.
    *   `highInterlock` (Number | null): Any value above this activates an interlock.

#### 3.3. Color Properties

Colors control the appearance of the ranges and indicators.

*   **Range Colors:**
    *   `desiredRangeColor` (Color): The color of the section defined by `desiredLow` and `desiredHigh`.
    *   `defaultRangeColor` (Color): The color for any part of the scale not covered by another defined range.
    *   `inactiveAlarmColor` (Color): The color used for an alarm range's section when the `processValue` is *not* currently within that range.
    *   `level2AlarmColor` (Color): The color used for the `lowAlarm` or `highAlarm` range section when the `processValue` *is* currently within that range.
    *   `level1AlarmColor` (Color): The color used for the `lowLowAlarm` or `highHighAlarm` range section when the `processValue` *is* currently within that range.
    *   `interlockColor` (Color): The color for the interlock range section when the `processValue` is within it.

*   **Indicator and Marker Colors:**
    *   `indicatorColor` (Color): The color of the arrow that points to the `processValue`.
    *   `setpointColor` (Color): The color of the marker that indicates the `setpointValue`.

#### 3.4. Label and Outline

These are object properties that control additional visual elements.

*   `label` (Object): Displays the numeric `processValue` as text next to the indicator.
    *   `label.visible` (Boolean): Set to `true` to display the label. Default is `false`.
    *   `label.format` (String): A format string for the numeric text. Available options are: `#,##0`, `#,##0.0`, `#,##0.00`, `0`, `0.0`, `0.00`, `#,##0%`.
    *   `label.style` (Object): A standard style object to control the appearance (font, color, etc.) of the label text.

*   `sectionOutline` (Object): Controls the border that appears between each colored range.
    *   `sectionOutline.color` (Color): The color of the border lines.
    *   `sectionOutline.width` (Number): The width of the border lines in pixels.

#### 3.5. Other Properties

*   `reverseIndicator` (Boolean): If set to `true`, the `processValue` indicator arrow and its `label` are moved to the opposite side of the scale. This is purely a visual change. Default is `false`.
*   `style` (Object): A standard style object that can be used to apply styles (like background color, borders, etc.) to the component as a whole. You can also specify a style class.

---

## Helpful Tips

*   **Optional Ranges:** To disable an alarm or interlock range, set its corresponding property (e.g., `highHighAlarm`, `lowInterlock`) to `null`. The component will not render a section for that range.

*   **Active vs. Inactive Alarms:** The coloring logic is powerful. Use `inactiveAlarmColor` to show where an alarm *would* occur. Use `level1AlarmColor` and `level2AlarmColor` to make that same section change color and draw attention when the `processValue` actually enters the alarm condition.

*   **Displaying the Exact Value:** The indicator is a visual guide. For precision, it is highly recommended to make the label visible by setting `props.label.visible` to `true`. Use `props.label.format` to control the number of decimal places or add a percent sign as needed.

*   **Visual Separation:** If you have many ranges defined, the indicator bar can look busy. Use the `props.sectionOutline` properties (`color` and `width`) to draw clear lines between the different colored sections, improving readability.

*   **Layout Flexibility:** Remember that the component's orientation is controlled by its aspect ratio. You can choose a horizontal or vertical layout to best fit your screen design. The `reverseIndicator` property provides further layout flexibility by allowing you to choose which side of the bar the pointer appears on.

*   **Setpoint Usage:** The `setpointValue` is a great way to show an operator the target for a process alongside the actual current value. If you don't have a setpoint, ensure the property is `null` to prevent an unwanted marker from appearing.

*   **Bindings and Events:** Like most Perspective components, the properties of the Moving Analog Indicator can be bound to tags or other data sources. Component events can be configured to trigger actions (e.g., scripting, navigation) when a user interacts with the component. For more details, consult the "Bindings in Perspective" and "Component Events and Actions" pages in the Ignition documentation.

# Schema - raw
{"schema":{"type":"object","properties":{"level2AlarmColor":{"format":"color","description":"Color for an active level 2 alarm (high or low)","type":"string","default":""},"highAlarm":{"description":"Value above which is a high alarm","type":["number","null"],"example":90},"indicatorColor":{"format":"color","description":"Color of the process value indicator","type":"string","default":""},"reverseIndicator":{"description":"Put the process value indicator on the other side of the scale","type":"boolean","default":false},"processValue":{"description":"Current value of the process","type":"number","default":50},"inactiveAlarmColor":{"format":"color","description":"Color for an inactive alarm range","type":"string","default":""},"desiredLow":{"description":"Lower limit of 'desired' range","type":"number","example":40},"minValue":{"description":"The minimum value shown on the indicator","type":"number","default":0},"setpointColor":{"format":"color","description":"Color of the setpoint value marker","type":"string","default":""},"highInterlock":{"description":"Value above which an interlock will be activated","type":["number","null"],"example":null},"level1AlarmColor":{"format":"color","description":"Color for an active level 1 alarm (high-high or low-low)","type":"string","default":""},"highHighAlarm":{"description":"Value above which is a high-high alarm","type":["number","null"],"example":null},"defaultRangeColor":{"format":"color","description":"Color of any area not defined as a range","type":"string","default":""},"sectionOutline":{"description":"Border surrounding each range area","type":"object","properties":{"color":{"format":"color","description":"Color for range borders","type":"string","default":""},"width":{"description":"Width for range borders","type":"number","default":2}}},"setpointValue":{"description":"Current value of the setpoint","type":["number","null"],"default":null},"maxValue":{"description":"The maximum value shown on the indicator","type":"number","default":100},"desiredRangeColor":{"format":"color","description":"Color for the area in the 'desired' range","type":"string","default":""},"interlockColor":{"format":"color","description":"Color for interlock range","type":"string","default":""},"label":{"description":"Numeric value displayed as text next to indicator","type":"object","properties":{"visible":{"description":"Whether to display label","type":"boolean","default":false},"format":{"description":"Format of numeric value in label, including commas, decimal places etc.","type":"string","enum":["#,##0","#,##0.0","#,##0.00","0","0.0","0.00","#,##0%"],"default":"#,##0"},"style":{"example":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"desiredHigh":{"description":"Upper limit of 'desired' range","type":"number","example":65},"lowAlarm":{"description":"Value below which is a low alarm","type":["number","null"],"example":10},"lowLowAlarm":{"description":"Value below which is a low-low alarm","type":["number","null"],"example":null},"lowInterlock":{"description":"Value below which an interlock will be activated","type":["number","null"],"example":null},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"MovingAnalogIndicator","name":"Moving Analog Indicator","palette":{"variants":[{"tooltip":"Displays an analog value in context with other information so you can visually see if the value is within the normal range or not.","label":"Moving Analog Indicator"}],"category":"display"},"id":"ia.display.moving-analog-indicator"}