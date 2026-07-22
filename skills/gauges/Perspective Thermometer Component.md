# Perspective Thermometer Component

## Description

This document describes the usage and configuration of the Ignition Perspective Thermometer component, explaining how its properties control visual appearance and behavior. It covers setting the component's value and scale, with a focus on using dynamic intervals to change the color based on the current value. Best practices for data binding and styling are also included to help create effective visual displays.

## Documentation

# Instructions
This document provides instructions for using and configuring the **Perspective Thermometer Component** in Ignition.

### Component Overview
The Thermometer component is a visual tool used to display a numerical value, typically a temperature, in the graphical form of a mercury thermometer. It shows a value as a fill level within the thermometer's tube. A key feature is the ability to define different temperature ranges (intervals) that can change the color of the "mercury" based on the current value, providing an immediate visual cue for different states (e.g., cold, normal, hot).

### Property Reference

The component's behavior and appearance are controlled by its properties, which are found in the Perspective Property Editor.

| Property | Type | Description | Default Value |
| --- | --- | --- | --- |
| **value** | Number | The current numerical value to be displayed by the thermometer. The mercury level and the value label will update to reflect this value. | 25 |
| **lowBound** | Number | The lowest value on the thermometer's scale. | 0 |
| **highBound** | Number | The highest value on the thermometer's scale. | 100 |
| **unit** | String | A string that represents the unit of measurement. This is displayed next to the value. The only valid options are "C" (for Celsius) or "F" (for Fahrenheit). | "C" |
| **mercuryColor** | Color | Sets the color of the mercury. This color is used if the current `value` does not fall within any of the defined `intervals`, or if no `intervals` are defined. | "" (empty string) |
| **thermometerColor** | Color | The color of the thermometer's outline and tick marks. | "" (empty string) |
| **strokeWidth** | Number | The width (in pixels) of the lines used to draw the thermometer's outline. | 2 |
| **axisLabelColor** | Color | The color of the labels on the thermometer's Y-axis scale. | "" (empty string) |
| **valueFontColor** | Color | The color of the text label that displays the current `value`. | "" (empty string) |
| **valueFont** | Object | An object that controls the font styling for the current value label. The primary property within this object is `fontSize`. | `{"fontSize": 25}` |
| **intervals** | Array | An array of objects used to change the mercury's color based on the current `value`. Each object in the array defines a specific range and its associated color. | `[{"color":"#47A9E5","high":25,"low":0},{"color":"#B394EF","high":75,"low":25},{"color":"#DB3939","high":100,"low":75}]` |
| **intervals.color** | Color | The color of the mercury when the `value` is within this interval's `low` and `high` bounds. | "" (empty string) |
| **intervals.low** | Number | The low bound for this specific interval. | null |
| **intervals.high** | Number | The high bound for this specific interval. | null |
| **style** | Object | Allows for advanced styling of the component using CSS-like properties or by assigning a pre-configured Style Class. This can control background, margins, borders, and more. | |

---

### Helpful Tips and Best Practices

*   **Understanding Intervals:** The `intervals` property is the most powerful feature for dynamic visualization.
    *   It is an array of objects. Each object *must* contain three properties: `low`, `high`, and `color`.
    *   The component checks the current `value` against each interval. If the `value` falls between an interval's `low` and `high` bounds, the mercury will adopt that interval's `color`.
    *   If the `value` falls outside of all defined intervals, the color will fall back to the base `mercuryColor` property.
    *   Intervals should not have overlapping ranges.

*   **Binding:** Most properties, especially `value`, `lowBound`, and `highBound`, are designed to be bound to data sources like OPC Tags, database queries, or expression tags to create dynamic and live displays.

*   **Units of Measurement:** The `unit` property is a string dropdown that only accepts "C" or "F" as valid inputs. Do not attempt to use other units like "K" for Kelvin, as they will not work.

*   **Color Properties:**
    *   Colors can be set using standard hex codes (e.g., `#FF0000`), color names (`red`), or RGB values (`rgb(255, 0, 0)`).
    *   If `mercuryColor` is not set and no `intervals` match, the mercury may not be visible.
    *   `thermometerColor` affects the "glass" part of the thermometer.
    *   `axisLabelColor` and `valueFontColor` control the text elements.

*   **Font Sizing:** To change the size of the numerical value displayed, you must edit the `fontSize` property within the `valueFont` object.

*   **Component Events:** You can configure actions based on user interaction with the component, such as mouse clicks. Events and actions can be configured from the Component Events and Actions page in the Designer. Note that not all event types are supported by every component.

*   **Styling:** For complex styling that goes beyond the basic properties (e.g., background gradients, complex borders, custom spacing), use the `style` property to either apply ad-hoc styles or link the component to a shared Style Class. This is the standard approach for styling Perspective components.

# Schema - raw
{"schema":{"type":"object","additionalProperties":false,"properties":{"strokeWidth":{"type":"number","default":2},"highBound":{"type":"number","default":100},"mercuryColor":{"format":"color","type":"string","default":""},"thermometerColor":{"format":"color","type":"string","default":""},"valueFontColor":{"format":"color","type":"string","default":""},"axisLabelColor":{"format":"color","type":"string","default":""},"unit":{"type":"string","default":"C"},"intervals":{"type":"array","example":[{"color":"#47A9E5","high":25,"low":0},{"color":"#B394EF","high":75,"low":25},{"color":"#DB3939","high":100,"low":75}],"items":{"type":"object","required":["high","color","low"],"default":{"color":"","high":null,"low":null},"additionalProperties":false,"properties":{"color":{"format":"color","type":"string","default":""},"high":{"type":["number","null"],"default":null},"low":{"type":["number","null"],"default":null}}}},"lowBound":{"type":"number","default":0},"valueFont":{"default":{"fontSize":25},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"type":"number","default":25}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Thermometer","name":"Thermometer","palette":{"variants":[{"tooltip":"Displays a temperature value depicted as a level in a mercury thermometer.","label":"Thermometer"}],"category":"display"},"id":"ia.display.thermometer"}