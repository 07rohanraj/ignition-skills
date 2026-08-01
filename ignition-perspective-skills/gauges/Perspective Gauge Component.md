# Perspective Gauge Component

## Description

The usage and configuration of the Perspective Gauge component, a visual element for displaying one or two real-time values on a customizable dial or arc. These instructions detail the properties available for controlling the gauge's shape, colors, and behavior, including the setup of its axes, needles, and colored range indicators.

## Documentation

# Instructions
# Perspective Gauge Component

## General Instructions

The Perspective Gauge component is used to display one or two real-time values within a specified range. It's visually represented as a dial or arc with a needle indicating the current value. The component is highly customizable, allowing for control over its appearance, including colors, angles, axes, and needle styles.

### Core Functionality

The gauge operates by mapping a numerical input (`value` and an optional `secondaryValue`) to a position on a circular axis. You can define the start and end angles of this axis to create different shapes, such as a semi-circle, a full circle, or a 3/4 arc.

The gauge can have two distinct axes: an `outerAxis` and an `innerAxis`. Each axis can be independently configured to display either the primary `value` or the `secondaryValue`, and each can have its own scale, colors, and appearance.

### Component Properties

Here is a detailed breakdown of the component's properties.

#### **Primary Configuration**

| Property | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `value` | number | The primary numeric value for the gauge to display. | 0 |
| `secondaryValue` | number | An optional secondary numeric value that can be displayed on a second axis. | 0 |
| `startAngle` | number | The radial position (in degrees) where the gauge's axis begins. | 180 |
| `endAngle` | number | The radial position (in degrees) where the gauge's axis ends. | 360 |
| `backgroundColor` | color | The background color within the gauge's arc. | |
| `animate` | boolean | If true, the needle will animate with a sweeping motion when the value changes. | `false` |
| `reverseScale` | boolean | If true, the gauge reverses the direction of the scale from `minValue` to `maxValue`. | `false` |
| `style` | object | An object for applying custom CSS styles to the component. | |

---

### Axis Configuration (`outerAxis` and `innerAxis`)

The `outerAxis` and `innerAxis` properties are objects that define the two possible axes on the gauge. They share the exact same set of configuration properties. By default, the `outerAxis` is visible and the `innerAxis` is hidden.

| Property | Type | Description | Default (Outer) | Default (Inner) |
| :--- | :--- | :--- | :--- | :--- |
| `show` | boolean | Determines whether this axis is displayed. | `true` | `false` |
| `data` | string | Specifies which value this axis should display. Must be either "value" or "secondaryValue". | "value" | "secondaryValue" |
| `minValue` | number | The minimum value for this axis's scale. | 0 | 0 |
| `maxValue` | number | The maximum value for this axis's scale. | 120 | 80 |
| `width` | number | The width of the axis arc, in pixels. | 1 | 1 |
| `color` | color | The color of the axis arc. | | |
| `percentRadius` | number | The radius of this axis as a percentage of the total available chart radius. Use a smaller value for the `innerAxis` to prevent overlap. | 100 | 85 |
| `ranges` | array | An array of objects to define colored zones or bands along the axis. | (see below) | `[]` |
| `needle` | object | An object containing properties to configure the needle for this axis. | (see below) | (see below) |
| `tickMarks` | object | An object containing properties to configure the tick marks for this axis. | (see below) | (see below) |

#### **Axis Sub-Properties**

##### `ranges` Array Object Properties
The `ranges` property is an array of objects, where each object defines a colored band on the axis dial.

| Property | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `start` | number | The value at which this colored range begins. | 0 |
| `end` | number | The value at which this colored range ends. | 0 |
| `width` | number | The width of this specific range band, in pixels. | 0 |
| `color` | color | The color to apply to this range. | "#77b6d8" |

##### `needle` Object Properties

| Property | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `origin` | number | The distance from the gauge's center where the needle begins, as a percentage of the radius. A value of 0 starts the needle at the very center. | 0 |
| `reach` | number | How far the needle extends from the center, as a percentage of the radius. A value of 100 means the needle extends to the outer edge of its own axis. | 100 |
| `color` | color | The color of the needle. | |

##### `tickMarks` Object Properties

| Property | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `color` | color | The color of the tick marks. | |
| `thickness` | number | The thickness of the tick marks, in pixels. | 1 |
| `length` | number | The length of the tick marks, in pixels. | 10 |

---

## Helpful Tips

*   **Dual Axis Display**: To show two different values, make sure both `outerAxis.show` and `innerAxis.show` are set to `true`. Then, set `outerAxis.data` to "value" and `innerAxis.data` to "secondaryValue" (or vice-versa). You must also provide data to both the `value` and `secondaryValue` properties of the gauge.
*   **Preventing Axis Overlap**: When using both axes, ensure the `innerAxis.percentRadius` is smaller than the `outerAxis.percentRadius` to create a visible gap between them. For example, set `outerAxis.percentRadius` to 100 and `innerAxis.percentRadius` to 85.
*   **Gauge Shape Variants**: The Gauge component comes with several pre-configured variants that provide a good starting point:
    *   **Half-Circle (Default)**: `startAngle: 180`, `endAngle: 360`
    *   **3/4 Circle**: `startAngle: 90`
    *   **Full Axis**: `startAngle: 135`, `endAngle: 405`
    You can create any arc shape by modifying these two angle properties.
*   **Creating Colored Status Zones**: The `ranges` property is ideal for creating visual status indicators (e.g., green for normal, yellow for warning, red for critical). You define each colored zone as an object in the `ranges` array, specifying its `start` and `end` values and a unique `color`.
*   **Independent Scales**: The `innerAxis` and `outerAxis` can have completely different scales. For example, the `outerAxis` could have `minValue: 0` and `maxValue: 100` to show a percentage, while the `innerAxis` has `minValue: 0` and `maxValue: 2500` to show RPM.
*   **Needle Appearance**: You can create different needle styles using the `origin` and `reach` properties. A needle with `origin: 0` and `reach: 100` will be a simple line from the center to the edge. A needle with `origin: 80` and `reach: 100` will be a shorter line that appears only near the edge of the dial.
*   **Hiding an Axis Line**: If you want to show a needle and tick marks but not the solid arc line of the axis itself, you can set the `width` of that axis to 0.

# Schema - raw
{"schema":{"description":"A Gauge component","type":"object","title":"Gauge","required":["value","secondaryValue","startAngle","endAngle","outerAxis","innerAxis","backgroundColor","animate","reverseScale","style"],"example":{"backgroundColor":"","startAngle":180,"secondaryValue":0,"endAngle":360,"innerAxis":{"tickMarks":{"color":"","thickness":1,"length":10},"data":"secondaryValue","color":"","ranges":[],"maxValue":80,"show":false,"minValue":0,"width":1,"percentRadius":85,"needle":{"color":"","reach":100,"origin":0}},"animate":false,"reverseScale":false,"outerAxis":{"tickMarks":{"color":"","thickness":1,"length":10},"data":"value","color":"","ranges":[{"color":"#77B6D8","start":0,"width":8,"end":80},{"color":"#6E94D7","start":80,"width":12,"end":105},{"color":"#7A6BD5","start":105,"width":16,"end":120}],"maxValue":120,"show":true,"minValue":0,"width":1,"percentRadius":100,"needle":{"color":"","reach":100,"origin":0}},"value":0},"additionalProperties":false,"definitions":{"AxisConfig":{"type":"object","required":["data","show","minValue","maxValue","width","color","percentRadius","ranges","needle","tickMarks"],"additionalProperties":false,"properties":{"tickMarks":{"type":"object","required":["color","thickness","length"],"additionalProperties":false,"properties":{"color":{"format":"color","description":"Color of tick marks for this axis","type":"string","default":""},"thickness":{"description":"Thickness of tick marks for this axis","type":"number","default":1},"length":{"description":"Length of tick marks for this axis","type":"number","default":10}}},"data":{"description":"Which value this axis and its needle should display","type":"string","enum":["value","secondaryValue"]},"color":{"format":"color","description":"Color of this axis arc","type":"string","default":""},"ranges":{"description":"Zones defined in dial band with a unique color","type":"array","example":[{"color":"#77B6D8","start":0,"width":10,"end":50},{"color":"#6E94D7","start":50,"width":15,"end":80},{"color":"#7A6BD5","start":80,"width":20,"end":100}],"items":{"type":"object","required":["start","end","width","color"],"additionalProperties":false,"properties":{"color":{"format":"color","description":"Color to apply to this range on the dial","type":"string","default":"#77b6d8"},"start":{"description":"Value at which this range starts","type":"number","default":0},"width":{"description":"Width of this axis, in pixels","type":"number","default":0},"end":{"description":"Value at which this range starts","type":"number","default":0}}}},"maxValue":{"description":"Maximum gauge value for this axis","type":"number","default":100},"show":{"description":"Whether this axis is displayed","type":"boolean"},"minValue":{"description":"Minimum gauge value for this axis","type":"number","default":0},"width":{"description":"Width of this axis, in pixels","type":"number","default":2},"percentRadius":{"description":"Radius of this axis, as a percentage of total chart radius","type":"number"},"needle":{"type":"object","required":["origin","reach","color"],"additionalProperties":false,"properties":{"color":{"format":"color","description":"Color of gauge's needle","type":"string","default":""},"reach":{"description":"How far needle reaches from the center of the gauge towards the outer dial, as a percentage of the radius","type":"number","default":100},"origin":{"description":"Distance from gauge's center the needle starts, as a percentage of the radius","type":"number","default":0}}}}}},"properties":{"backgroundColor":{"format":"color","description":"Color to apply as background within the gauge","type":"string"},"startAngle":{"description":"Radial position for start of gauge's axis","type":"number","default":180},"secondaryValue":{"description":"Optional secondary value for gauge to display on a second axis","type":"number","default":0},"endAngle":{"description":"Radial position for end of gauge's axis","type":"number","default":360},"innerAxis":{"type":"object","$ref":"#/definitions/AxisConfig"},"animate":{"description":"Whether needle should be animated in a sweeping motion when value changes","type":"boolean","default":false},"reverseScale":{"description":"If true, gauge will reverse the direction from minValue to maxValue on its dial","type":"boolean","default":false},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"outerAxis":{"type":"object","$ref":"#/definitions/AxisConfig"},"value":{"description":"Numeric value for gauge to display","type":"number","default":0}}},"resources":[{"type":"js","path":"/res/perspective/js/PerspectiveAmCharts.js","name":"perspective-amcharts-js"},{"type":"css","path":"/res/perspective/css/PerspectiveAmCharts.css","name":"perspective-amcharts-css"}],"defaultMetaName":"Gauge","name":"Gauge","palette":{"variants":[{"tooltip":"A needle gauge component that shows real time values in a range as they change.","label":"Gauge"},{"tooltip":"A needle gauge component that shows real time values in a range as they change.","label":"Half-Circle","id":"gauge-half-circle"},{"tooltip":"A needle gauge component that shows real time values in a range as they change.","label":"3/4 Circle","props":{"startAngle":90},"id":"gauge-34-circle"},{"tooltip":"A needle gauge component that shows real time values in a range as they change.","label":"Full Axis","props":{"startAngle":135,"endAngle":405},"id":"gauge-full-axis"}],"category":"chart"},"id":"ia.chart.gauge"}