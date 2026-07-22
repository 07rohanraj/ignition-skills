# Perspective Cylindrical Tank Component

## Description

This document details the usage and configuration of the Perspective Cylindrical Tank component, explaining how to visually represent a numeric value as a tank's fill level. The instructions cover customizing the appearance of the tank and liquid, configuring the text overlay to display the value with custom formatting and units, and setting up a visual warning state that triggers when the fill level exceeds a defined threshold.

## Documentation

# Instructions
# Perspective Cylindrical Tank Component Instructions

This document provides detailed instructions for an LLM on how to interact with and configure the **Perspective Cylindrical Tank Component** in Ignition.

## Description

The Cylindrical Tank is a visual component that resembles a 3D cylindrical tank containing a liquid. Its primary purpose is to display a value, such as the volume level of a tank or vessel, in a graphical way. The component is configured so that the "liquid" inside rises and falls as the `value` property changes relative to the `capacity` property. It offers a range of styling options for the tank, the liquid, and a text overlay that can display the current value.

---

## Core Functionality

The visual fill level of the tank is determined by the ratio of the `value` property to the `capacity` property.
-   If `value` is `50` and `capacity` is `100`, the tank will appear 50% full.
-   If `value` is `25` and `capacity` is `200`, the tank will appear 12.5% full.

The component also has a built-in warning system. When the fill level (value as a percentage of capacity) exceeds the `warningThreshold`, the colors of the tank and the liquid can be changed to indicate a warning state.

---

## Properties

### Main Properties

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **`value`** | `number` | `0` | The current value or fill level of the tank. This is the primary property that determines how full the tank appears. |
| **`capacity`** | `number` | `100` | The maximum capacity of the tank. This is used in conjunction with the `value` property to calculate the fill percentage. |
| **`warningThreshold`**| `number`| `100` | When the value (as a percentage of the capacity) exceeds this threshold, the warning appearance is applied. |
| **`liquidColor`** | `string` (color) | `""` | The color of the liquid when the component is in its normal state. |
| **`liquidWarningColor`**| `string` (color) | `""` | The color of the liquid when the component is in a warning state. |
| **`liquidOpacity`** | `number`| `0.7` | The opacity of the liquid, where `0` is fully transparent and `1` is fully opaque. The value must be between `0` and `1`. |
| **`tankColor`** | `string` (color) | `""` | The color of the tank itself when in its normal state. |
| **`tankWarningColor`**| `string` (color) | `""` | The color of the tank itself when in a warning state. |
| **`strokeWidth`** | `number`| `2` | The width of the tank's outline stroke. Must be `0` or greater. |
| **`style`** | `object` | | An object that allows for extensive styling of the component, including background, margin, padding, border, and shape. |

### `valueDisplay` Properties

This object controls the text overlay that displays the tank's current value.

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **`enabled`** | `boolean` | `true` | If `true`, the value display overlay is shown. If `false`, it is hidden. |
| **`format`** | `string` or `number` | `"0%"` | A format string that dictates how the `value` is displayed. Suggestions include `0,0` (integer), `$0,0.00` (currency), and `0%` (percent). |
| **`style`** | `object` | | An object that allows for styling of the value display text itself. |

#### `valueDisplay.unit` Properties

This nested object controls the unit displayed next to the value.

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **`enabled`** | `boolean` | `false` | If `true`, a unit will be displayed with the value. |
| **`value`** | `string` | `""` | The actual text of the unit to be displayed (e.g., "Gallons", "Liters"). |
| **`fix`** | `string` | `"post"` | Determines the placement of the unit. Can be set to `"pre"` for a prefix or `"post"` for a postfix. |

---

## Component Events

Component events and actions can be configured for this component. Scripting can be accessed from the component's menubar or by right-clicking on the component. The specific events supported are documented on the "Perspective Event Types Reference" page.

---

## Helpful Tips for the LLM

*   **Primary Function:** The main purpose of this component is to visualize a numeric `value` against a `capacity`. The fill percentage is always `(value / capacity) * 100`.
*   **Enabling the Warning State:** The warning state is purely visual. It is triggered when `(value / capacity) * 100` is greater than the `warningThreshold`. To make the warning state visible, you must define the `liquidWarningColor` and/or `tankWarningColor` properties. If these are not set, nothing will visually change.
*   **Displaying the Value:** To show the numeric value on the tank, ensure the `valueDisplay.enabled` property is set to `true`.
*   **Formatting the Displayed Value:** You can format the number shown on the tank using the `valueDisplay.format` property. For example, to show a value of `75.5` as "75.50", you might use a format string like `"0.00"`. To show it as a percentage of capacity, use the default `"0%"` format.
*   **Adding Units:** To display a unit like "gal" next to the value, you must set `valueDisplay.unit.enabled` to `true` and then provide the unit text in `valueDisplay.unit.value`. You can place it before or after the number using the `valueDisplay.unit.fix` property.
*   **Color Properties:** All color properties (`liquidColor`, `tankColor`, etc.) should be valid color strings (e.g., hex codes like `#FF0000`, color names like `red`, or `rgb()` functions). If a color property is left as an empty string (`""`), a default color scheme is likely used.
*   **Styling:** Deep customization of the component's appearance (fonts, borders, backgrounds) is available through the `style` object property. Similarly, the text of the value display can be styled using its own nested `valueDisplay.style` object.
*   **Bindings:** Most properties support bindings, which is a key feature for making the component dynamic. For example, you would typically bind the `value` property to a PLC tag or a database query to show real-time data.

# Schema - raw
{"schema":{"type":"object","required":["value","capacity"],"additionalProperties":false,"properties":{"strokeWidth":{"type":"number","default":2,"minimum":0},"tankColor":{"format":"color","type":"string","default":""},"warningThreshold":{"description":"The warning appearance will be applied when value as a percentage of the capacity exceeds this value.","type":"number","default":100},"tankWarningColor":{"format":"color","type":"string","default":""},"capacity":{"type":"number","default":100},"liquidOpacity":{"type":"number","default":0.7,"maximum":1,"minimum":0},"valueDisplay":{"type":"object","properties":{"format":{"description":"Format to apply to value which is then used as the display value.","type":["string","number"],"default":"0%","suggestions":{"integer [1,200]":"0,0","none":"none","currency [$1,000.12]":"$0,0.00","percent [10%]":"0%"}},"enabled":{"description":"If true, will show the value display overlay.","type":"boolean","default":true},"unit":{"description":"Unit value to display on value overlay","type":"object","properties":{"enabled":{"description":"If true, will show either a prefixed or postfixed unit","type":"boolean","default":false},"fix":{"description":"Direction in which to place the unit. Either as a prefix or a postfix.","type":"string","enum":["pre","post"],"default":"post"},"value":{"description":"Unit value to display","type":"string","default":""}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"liquidColor":{"format":"color","description":"The color used to render the filled part of the tank.","type":"string","default":""},"liquidWarningColor":{"format":"color","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"type":"number","default":0}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"CylindricalTank","name":"Cylindrical Tank","palette":{"variants":[{"tooltip":"Displays the volume level of a tank or vessel.","label":"Cylindrical Tank"}],"category":"display"},"id":"ia.display.cylindrical-tank"}