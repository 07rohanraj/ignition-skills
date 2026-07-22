# Perspective Simple Gauge Component

## Description

These instructions detail the configuration and use of the Perspective Simple Gauge component, explaining how to modify its properties to control the value range, visual appearance, and label formatting. The document covers customizing the gauge's arc shape and color, binding its value to real-time data sources, and implementing user interactivity.

## Documentation

# Instructions
# Perspective Simple Gauge Component Instructions

## Object Description
The Perspective Simple Gauge component is a modern, web-style gauge used to display a single real-time numeric value within a defined range. It is a simplified version of the standard Gauge component, featuring a single axis and a highly customizable, easy-to-configure appearance. The gauge represents the value as a colored arc against a background track.

### Variants
The Simple Gauge comes with several pre-configured variants available in the component palette:
*   **Simple Gauge (Default):** A standard half-circle gauge.
*   **Half-Circle:** Same as the default layout.
*   **3/4 Circle:** A gauge with an arc spanning 270 degrees.
*   **Full Axis:** A gauge that wraps around almost a full circle.

## Properties

| Property | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| **value** | number | The numeric value the gauge will display. | `0` |
| **minValue** | number | The minimum value of the gauge's range. | `0` |
| **maxValue** | number | The maximum value of the gauge's range. | `100` |
| **startAngle** | number | The radial position (in degrees) where the gauge's arc begins. `0` degrees is at the 3 o'clock position. | `180` |
| **endAngle** | number | The radial position (in degrees) where the gauge's arc ends. | `360` |
| **animate** | boolean | If true, the gauge will animate with a sweeping motion when its value changes. | `false` |
| **arc** | object | An object that defines the appearance of the radial band representing the gauge's value. | |
| `arc.width` | number | The width of the value arc in pixels. | `20` |
| `arc.color` | string | The color of the value arc. Accepts standard color formats (e.g., `#RRGGBB`, `rgb(r,g,b)`). | `"#77B6D8"` |
| `arc.cornerRadius` | number | The amount to round the edges of the value arc, creating a smoother appearance. | `0` |
| **arcBackground** | object | An object that defines the appearance of the background or 'track' for the gauge's arc. | |
| `arcBackground.color`| string | The color of the background arc. | `"#77B6D8"` |
| `arcBackground.opacity`| number | The opacity of the background arc, from `0` (transparent) to `1` (opaque). | `0.2` |
| **label** | object | An object that configures the text label displaying the gauge's value. | |
| `label.visible` | boolean | If true, the value label is shown in the center of the gauge. | `true` |
| `label.size` | number | The font size of the label text. | `25` |
| `label.color` | string | The color of the label text. | `"#697077"` |
| `label.units` | string | A string to be appended to the value in the label (e.g., "psi", "%"). | `""` |
| `label.maxDecimal` | number / null | The maximum number of decimal places to display. If `null`, the full value is shown. | `4` |
| `label.offsetX` | number | The horizontal offset of the label in pixels, relative to the center of the gauge. | `0` |
| `label.offsetY` | number | The vertical offset of the label in pixels, relative to the bottom of the label. | `0` |
| **style** | object | An object that allows for advanced CSS-based styling of the component's container. | |


## Helpful Tips
*   **Bindings:** Nearly all properties of the Simple Gauge can be bound to other sources, like tags or database queries. This is essential for making the gauge dynamic. For example, bind the `value` property to a PLC tag to show real-time machine data.
*   **Configuring the Arc Shape:**
    *   The `startAngle` and `endAngle` properties define the shape of your gauge. The angles are measured in degrees, with 0° at the 3 o'clock position, 90° at 6 o'clock, 180° at 9 o'clock, and 270° at 12 o'clock.
    *   The default `startAngle: 180` and `endAngle: 360` creates a half-circle or "semi-circle" gauge that fills the bottom half.
    *   To create a 3/4 circle gauge, you could use `startAngle: 135` and `endAngle: 405`.
    *   To create a full circle gauge, you could use `startAngle: 0` and `endAngle: 360`, though the "Full Axis" variant uses `startAngle: 135` and `endAngle: 405` for a slightly different aesthetic.
*   **Customizing Appearance:**
    *   You can create a "track" effect by setting the `arc.color` and `arcBackground.color` to different colors.
    *   The `arcBackground.opacity` property is useful for making the track less prominent than the value arc. A lower value like `0.2` makes it subtle.
    *   Use `arc.cornerRadius` to give the value arc a modern, rounded look. A higher value will result in more rounded ends.
*   **Label Formatting:**
    *   Always add units to the label via the `label.units` property for clarity (e.g., "°C", "PSI", "RPM").
    *   Use `label.maxDecimal` to control the precision of the displayed value. To show an integer value, set this to `0`. If you need to show the raw value from your data source without rounding, set it to `null`.
    *   If the label doesn't appear perfectly centered in custom gauge shapes (like the 3/4 circle), use `label.offsetX` and `label.offsetY` to adjust its position.
*   **Example Configuration:**
    To create a dark orange gauge for pressure readings with a limited precision, you could apply the following properties:
    *   `value`: `32.4567` (or bind this to a tag)
    *   `props.arc.width`: `15`
    *   `props.arc.cornerRadius`: `25`
    *   `props.arc.color`: `"#FF8C00"`
    *   `props.arcBackground.opacity`: `0.4`
    *   `props.label.units`: `"psi"`
    *   `props.label.maxDecimal`: `1`
    This will result in the gauge displaying a value of "32.5 psi".
*   **Component Events:** You can configure actions based on component events, such as `onClick`. This allows you to add interactivity, for example, clicking the gauge could open a popup with more detailed information. Scripting can also be accessed by right-clicking the component.

# Schema - raw
{"schema":{"description":"A simple, modern web style Gauge component","type":"object","title":"Simple Gauge","required":["value","minValue","maxValue","startAngle","endAngle","arc","arcBackground","label","animate","style"],"example":{"startAngle":180,"maxValue":100,"endAngle":360,"label":{"visible":true,"color":"#697077","units":"","offsetX":0,"offsetY":0,"size":25},"animate":false,"minValue":0,"arc":{"color":"#77B6D8","cornerRadius":0,"width":20},"arcBackground":{"color":"#77B6D8","opacity":0.2},"value":0},"additionalProperties":false,"properties":{"startAngle":{"description":"Radial position for start of gauge's arc","type":"number","default":180},"maxValue":{"description":"Maximum gauge value","type":"number","default":100},"endAngle":{"description":"Radial position for end of gauge's arc","type":"number","default":360},"label":{"description":"Displays the value as text, with optional units","type":"object","required":["visible","size","units","maxDecimal"],"additionalProperties":true,"properties":{"visible":{"description":"Whether to show label","type":"boolean","default":true},"color":{"format":"color","description":"The color of the text to display.","type":"string","default":"#697077"},"maxDecimal":{"description":"Maximum number of digits after decimal to display in the label. If null, full value will display.","type":["number","null"],"default":4},"units":{"description":"Any unit information to append to the value on the label","type":"string","default":""},"offsetX":{"description":"The x offset relative to the middle of the label.","type":"number","default":0},"offsetY":{"description":"The y offset relative to the bottom of the label.","type":"number","default":0},"size":{"description":"Font size to display label text","type":"number","default":25}}},"animate":{"description":"Whether gauge should be animated in a sweeping motion when value changes","type":"boolean","default":false},"minValue":{"description":"Minimum gauge value","type":"number","default":0},"arc":{"description":"Radial band that displays gauge's value","type":"object","required":["width","color","cornerRadius"],"additionalProperties":false,"properties":{"color":{"format":"color","description":"Color of the arc showing gauge's value","type":"string","default":"#77B6D8"},"cornerRadius":{"description":"Amount to round the edges of the arc","type":"number","default":0},"width":{"description":"Width of the arc showing gauge's value","type":"number","default":20}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"arcBackground":{"description":"Background or 'track' for gauge arc. Shows shape and total potential value behind the arc.","type":"object","required":["color","opacity"],"additionalProperties":false,"properties":{"color":{"format":"color","description":"Color of the arc background","type":"string","default":"#77B6D8"},"opacity":{"description":"Opacity of the arc background, as a number ranged 0 to 1","type":"number","default":0.2}}},"value":{"description":"Numeric value for gauge to display","type":"number","default":0}}},"resources":[{"type":"js","path":"/res/perspective/js/PerspectiveAmCharts.js","name":"perspective-amcharts-js"},{"type":"css","path":"/res/perspective/css/PerspectiveAmCharts.css","name":"perspective-amcharts-css"}],"defaultMetaName":"SimpleGauge","name":"Simple Gauge","palette":{"variants":[{"tooltip":"A simple needle gauge component with just one axis.","label":"Simple Gauge"},{"tooltip":"A simple needle gauge component with just one axis.","label":"Half-Circle","id":"simple-gauge-half-circle"},{"tooltip":"A simple needle gauge component with just one axis.","label":"3/4 Circle","props":{"startAngle":90,"label":{"offsetY":22}},"id":"simple-gauge-34-circle"},{"tooltip":"A simple needle gauge component with just one axis.","label":"Full Axis","props":{"startAngle":135,"endAngle":405,"label":{"offsetY":12}},"id":"simple-gauge-full-axis"}],"category":"chart"},"id":"ia.chart.simple-gauge"}