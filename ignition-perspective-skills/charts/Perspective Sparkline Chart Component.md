# Perspective Sparkline Chart Component

## Description

These instructions explain the configuration and usage of the Perspective Sparkline Chart component to create a compact, minimalistic visualization of a data point's trend. It details how to supply data and customize the chart's appearance, including styling the line, defining a desired operating range with a visual band, and applying markers to highlight key values.

## Documentation

# Instructions
# Perspective Sparkline Chart Component Instructions for LLM

## Introduction
The Sparkline Chart is a minimalistic chart component designed to display a line-chart history for a single data point. The primary purpose of a Sparkline is to provide a quick, contextual overview of a data point's recent trend (e.g., rising, falling, oscillating) in a very compact space. It is not meant to be a full-featured chart with axes and legends. Instead of axes, it can display a colored band to indicate a desired operating range, making it immediately obvious if the value is within, above, or below its expected range.

To use the Sparkline, you typically bind its `points` property to a data source, such as a Tag Historian realtime query or a database query. The component automatically adjusts its internal scale based on the data provided.

## Component Properties

Below are the properties available for the Sparkline Chart component.

### Primary Properties

| Property | Type | Description |
| :--- | :--- | :--- |
| `points` | array, string, or dataset | The data points to be plotted. This is the most important property. See the **Data Formatting for 'points' Property** section below for detailed formatting options. |
| `width` | number | The thickness of the main chart line in pixels. Default is `0.75`. |
| `color` | color | The color of the main chart line. Can be any valid color string (e.g., `#FF0000`, `rgb(255,0,0)`). |
| `opacity` | number | The opacity of the main chart line, ranging from 0.0 (fully transparent) to 1.0 (fully opaque). Default is `1`. |
| `dashArray`| string or number | Defines the pattern of dashes and gaps for the line. It is a comma-separated or space-separated list of lengths. For example, `5,3,2` would create a repeating pattern of a 5px dash, 3px gap, 2px dash, 5px gap, 3px dash, 2px gap, and so on. |
| `style` | object | Standard Perspective style object. Allows for configuration of background color, borders, margins, padding, etc. |

### `range` Object Properties
This object allows you to set fixed vertical boundaries for the chart. If not set, the chart scales automatically based on the data in the `points` property.

| Property | Type | Description |
| :--- | :--- | :--- |
| `range.high`| number or string | A fixed numeric value for the upper edge (top) of the chart. |
| `range.low` | number or string | A fixed numeric value for the lower edge (bottom) of the chart. |

### `desired` Object Properties
This object configures the "desired operating range," which is displayed as a colored band in the background of the chart.

| Property | Type | Description |
| :--- | :--- | :--- |
| `desired.high`| number or string | The high value of the desired operating range. |
| `desired.low` | number or string | The low value of the desired operating range. |
| `desired.fill`| object | An object that defines the appearance of the fill for the desired range band. It contains `color` and `opacity` properties. The default opacity is `0.1`. |
| `desired.stroke`| object | An object that defines the appearance of the border lines at the high and low edges of the desired range. It contains `color`, `width`, `opacity`, and `dashArray` properties. |

### `marker` Object Properties
This object allows you to configure markers for specific points on the chart: the first, last, highest, and lowest points.

| Property | Type | Description |
| :--- | :--- | :--- |
| `marker.first`| object | Configures the marker for the first data point. |
| `marker.last` | object | Configures the marker for the last data point. |
| `marker.high` | object | Configures the marker for the highest data point. |
| `marker.low` | object | Configures the marker for the lowest data point. |

#### Marker Child Properties
Each of the `marker` objects (`first`, `last`, `high`, `low`) has the following child properties:

| Property | Type | Description |
| :--- | :--- | :--- |
| `shape` | string | The shape of the marker. Enum: `circle`, `square`, `triangle`. |
| `size` | number or string| The size of the marker in pixels. Default is `5`. |
| `fill` | object | An object defining the marker's fill, containing `color` and `opacity` properties. |
| `stroke` | object | An object defining the marker's stroke (outline), containing `color`, `width`, `opacity`, and `dashArray` properties. |
| `style` | object | A Perspective style object for applying custom styles to the marker. |

### Deprecated Properties
The following properties are deprecated. While they may still work, you should use their modern equivalents to ensure future compatibility.

| Deprecated Property | Use Instead |
| :--- | :--- |
| `strokeWidth` | `width` |
| `stroke` (at the root level) | `color` (at the root level) |

---

## Helpful Tips & Best Practices

### Data Formatting for `points` Property
The `points` property is flexible. Be sure your data source is formatted in one of these supported ways:
*   **Simple Array of Numbers:** An array of numbers will be treated as the Y-values. The X-values will be inferred as the index of the array (`0, 1, 2, ...`).
    *   Example: `[59, 80, 81, 75, 68]`
*   **Array of Objects:** An array where each object has `x` and `y` numeric properties. This is useful for non-uniform spacing on the x-axis.
    *   Example: `[{"x": 0, "y": 9}, {"x": 5, "y": 12}, {"x": 8, "y": 10}]`
*   **Space-Delimited String:** A string of points where each point is `x,y` and points are separated by spaces.
    *   Example: `'0,20 1,35 2,15'`
*   **Dataset:**
    *   **Single Column:** A dataset with a single numeric column will be treated as the Y-values, similar to the simple array of numbers.
    *   **Two Columns:** A dataset with two columns. The first column is the X-value, and the second is the Y-value. The first column can be a number, date, or timestamp. **The dataset must be sorted by the first column in ascending order.**

### General Usage
*   **Purpose:** Remember that Sparklines are for showing trends at a glance. They are intentionally minimalistic. Do not try to use them for detailed chart analysis.
*   **Data Binding:** The most common way to use a Sparkline is to bind the `points` property to a Tag History query or a database query that returns time-series data.
*   **Time-Series Data:** When using time-series data (like from a Tag History binding), ensure your data is sorted chronologically (oldest to newest). The component expects time-ordered data to draw the line correctly from left to right.
*   **Desired Range:** The `desired` property is a key feature. Use `desired.high` and `desired.low` to visually represent the normal or acceptable operating range for the data point. This is more effective than trying to add axis labels.
*   **Markers:** Use markers to highlight important points. `marker.last` is very useful for showing the most current value, while `marker.high` and `marker.low` can draw attention to extremes within the displayed period.
*   **`dashArray`:** To use `dashArray`, provide a list of numbers representing the length of a dash followed by the length of a gap. The pattern repeats. For example, `dashArray: "10 5"` creates a line with a 10px dash followed by a 5px gap. If you provide an odd number of values, the list is repeated to make it even. For example, `"5,3,2"` is treated as `"5,3,2,5,3,2"`.

# Schema - raw
{"schema":{"type":"object","definitions":{"fill":{"type":"object","default":{"color":"","opacity":1},"properties":{"color":{"format":"color","description":"Fill color.","type":"string","default":""},"opacity":{"description":"Fill opacity.","type":"number","default":1}}},"stroke":{"type":"object","default":{"color":"","width":0.5,"opacity":1,"dashArray":""},"properties":{"color":{"format":"color","description":"Stroke color.","type":"string","default":""},"width":{"description":"Stroke width.","type":"number","default":0.5},"opacity":{"description":"Stroke opacity.","type":"number","default":1},"dashArray":{"description":"Pattern of dashes and gaps used to paint stroke.","type":["string","number"],"default":""}}},"marker":{"type":"object","default":{"shape":"circle","fill":{"color":"","opacity":1},"stroke":{"color":"","width":0.5,"opacity":1,"dashArray":""},"size":5,"style":{"classes":""}},"properties":{"shape":{"type":"string","enum":["square","circle","triangle"],"default":"circle"},"fill":{"$ref":"#/definitions/fill"},"stroke":{"$ref":"#/definitions/stroke"},"size":{"type":["number","string"],"default":5},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}},"properties":{"strokeWidth":{"description":"Thickness of the line in px. DEPRECATED: renamed to width.","type":"number"},"color":{"format":"color","description":"Stroke color.","type":"string","default":""},"range":{"type":"object","properties":{"high":{"description":"A fixed value for the upper edge of the chart as a number.","type":["number","string"],"default":""},"low":{"description":"A fixed value for the lower edge of the chart as a number.","type":["number","string"],"default":""}}},"stroke":{"format":"color","description":"Color of the line. DEPRECATED: renamed to color.","type":"string"},"points":{"anyOf":[{"type":"array","items":{"anyOf":[{"type":"number"},{"type":"object","properties":{"x":{"type":"number"},"y":{"type":"number"}}}]}},{"type":"string"},{"type":"dataset"}],"description":"Data points to plot. May be a dataset, or an array of values or objects containing x and y coordinates ([{x: 0, y: 9}]). Also may be a string formatted with x and y values separated by comma ('x,y x,y').","example":[59,80,80,100,68,62,87,72,42,49,58,53,57,51,42,32,37,30,24,38,57,29,18,32,38,24,24,24,20,21,29,32,26,18,32,36,30,36,29,32,29,28,41,20,28,58,18,24,16,2,22,17,22,21,12,22,14,13,11,20,16,16,18,12,28,28,32,16,16,24,16,20,14,18,12,26,17,11,30,16,9,20,42,13,13,24,17,13,20,12,14,13,14,71,82,20,16,20,22,17,5]},"desired":{"description":"The desired operating range.","type":"object","properties":{"fill":{"default":{"color":"","opacity":0.1},"$ref":"#/definitions/fill"},"stroke":{"default":{"color":"","width":1,"opacity":1,"dashArray":4},"$ref":"#/definitions/stroke"},"high":{"description":"The high value of the desired operating range as a number.","type":["number","string"],"default":""},"low":{"description":"The low value of the desired operating range as a number.","type":["number","string"],"default":""}}},"marker":{"type":"object","properties":{"last":{"default":{"shape":"circle","fill":{"color":"","opacity":1},"stroke":{"color":"","width":0.5,"opacity":1,"dashArray":""},"size":5,"style":{"classes":""}},"$ref":"#/definitions/marker"},"high":{"default":{"shape":"square","fill":{"color":"","opacity":1},"stroke":{"color":"","width":0.5,"opacity":1,"dashArray":""},"size":5,"style":{"classes":""}},"$ref":"#/definitions/marker"},"low":{"default":{"shape":"square","fill":{"color":"","opacity":1},"stroke":{"color":"","width":0.5,"opacity":1,"dashArray":""},"size":5,"style":{"classes":""}},"$ref":"#/definitions/marker"},"first":{"default":{"shape":"circle","fill":{"color":"","opacity":1},"stroke":{"color":"","width":0.5,"opacity":1,"dashArray":""},"size":5,"style":{"classes":""}},"$ref":"#/definitions/marker"}}},"width":{"description":"Stroke width.","type":"number","default":0.75},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"Stroke opacity.","type":"number","default":1},"dashArray":{"description":"Pattern of dashes and gaps used to paint stroke.","type":["string","number"],"default":""}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Sparkline","name":"Sparkline","palette":{"variants":[{"tooltip":"A minimalistic chart component that displays a line-chart history for a single datapoint.","label":"Sparkline"}],"category":"display"},"id":"ia.display.sparkline"}