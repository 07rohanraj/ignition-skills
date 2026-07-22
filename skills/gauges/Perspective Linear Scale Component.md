# Perspective Linear Scale Component

## Description

The usage and configuration of the Perspective Linear Scale component, detailing how to define its value range and orientation, customize its tick marks and numeric labels, and add various indicators to mark specific values or highlight ranges on the scale.

## Documentation

# Instructions
This document provides instructions for an LLM on how to use and configure the **Perspective Linear Scale** component in Ignition.

### Functionality

The Perspective Linear Scale component is a visual element used to display a range of values between a specified minimum and maximum. It is primarily used to visualize data points, thresholds, and value ranges along a linear axis. This is accomplished by using a combination of tick marks (major, minor, and fine), numeric labels, and special indicators. The component is highly customizable, allowing for different visual styles, orientations, and data representations.

### Properties

The component's behavior and appearance are controlled by its properties, which are organized into several categories.

#### General Properties

| Property | Type | Description |
| :--- | :--- | :--- |
| **minValue** | number | The minimum value shown on the scale. Default: `0`. |
| **maxValue** | number | The maximum value shown on the scale. Default: `100`. |
| **mirror** | boolean | If `true`, the scale is aligned to the opposite side of the component. Default: `false`. |
| **reverse** | boolean | If `true`, the order of the scale values is inverted, so the maximum value is at the start and the minimum value is at the end. Default: `false`. |
| **style** | object | Applies a style to the component, including options for background, border, and shape. |

---

#### Tick Properties (`majorTicks`, `minorTicks`, `fineTicks`)

These properties control the three levels of tick marks on the scale. Each is an object with the same set of child properties, but with different default values to represent different levels of granularity.

| Property | Type | Description |
| :--- | :--- | :--- |
| **span** | number | The distance between each tick mark of this type. For example, a `span` of 20 on a 0-100 scale would place major ticks at 0, 20, 40, 60, 80, and 100. |
| **length** | number | The length of the tick mark in pixels. |
| **color** | string | The color of the tick mark. Can be a hex code, RGB, or HSL value. |
| **stroke** | number | The width (thickness) of the tick mark in pixels. |

---

#### Label Properties (`labels`)

This object controls the appearance of the numeric labels that correspond to the `majorTicks`.

| Property | Type | Description |
| :--- | :--- | :--- |
| **angle** | number | The rotational angle of the numeric labels. Default: `0`. |
| **style** | object | A standard style object that can be used to change the font, color, and other text properties of the labels. |

---

#### Indicator Properties (`indicators`)

This is an array of objects used to place markers for specific values or ranges on the scale. Each object in the array represents a single indicator.

| Property | Type | Description |
| :--- | :--- | :--- |
| **value** | number | **(Required)** The value along the scale where the indicator is placed (or where it starts). |
| **indicatorStyle** | string | The visual style of the indicator. Options are `'line'`, `'wedge'`, or `'range'`. Default: `'line'`. |
| **label** | string | The text to display with the indicator. |
| **color** | string | The color of the indicator or the area making up the indicator. |
| **labelColor** | string | The color of the indicator's label text. |
| **labelAngle** | number | The rotational angle of the indicator's label. Default: `0`. |
| **opacity** | number | The opacity of the indicator, where `0` is fully transparent and `1` is fully opaque. Default: `1`. |
| **length** | number | The length of the indicator in pixels, as measured by its x-value within the scale. Default: `25`. |
| **stroke** | number | The width of the indicator in pixels. This applies only when `indicatorStyle` is set to `'line'` or `'wedge'`. Default: `1`. |
| **extent** | number | The distance along the scale that the indicator covers. This applies only when `indicatorStyle` is set to `'range'`. For example, an indicator with `value: 85` and `extent: 15` will create a range covering values from 85 to 100. Default: `2`. |

### Helpful Tips

*   **Tick Hierarchy:** The component has three types of ticks: `majorTicks`, `minorTicks`, and `fineTicks`. Use them to create a clear visual hierarchy. `majorTicks` are the most prominent, `minorTicks` are secondary, and `fineTicks` are for the finest level of detail. All three share the same configuration properties (`span`, `length`, `color`, `stroke`).
*   **Understanding `span` vs. `length`:** Do not confuse these two properties. `span` defines the value-based interval *between* ticks, while `length` defines the visual pixel size *of* a tick.
*   **Configuring Indicators:** The `indicators` property is an array. To add or modify indicators, you must work with the array elements. Each element is an object that defines a single indicator.
*   **Indicator Styles:**
    *   `'line'`: Creates a simple line marker. Its thickness is controlled by the `stroke` property.
    *   `'wedge'`: Creates a triangular marker. Its border width is controlled by the `stroke` property.
    *   `'range'`: Creates a rectangular block along the scale. The starting point is set by `value` and its size along the scale is set by `extent`. This is useful for highlighting an operational range or a deadband.
*   **Labels vs. Indicator Labels:** The top-level `labels` property styles the numeric markings on the scale itself (e.g., "0", "20", "40"). The `label` property *inside an indicator's object* is for the text associated with that specific marker (e.g., "High Setpoint").
*   **Orientation Control:** Use the `mirror` (boolean) and `reverse` (boolean) properties to control the scale's orientation. `mirror` flips it horizontally, and `reverse` inverts the direction of the values (e.g., from `max` to `min`).
*   **Data Types:** Pay close attention to the data types. Colors should be strings (e.g., `'#FF0000'`), boolean properties should be `true` or `false`, and all other values are numeric.
*   **Example Indicator Configuration:** To create a red range indicator that starts at 95 and extends for 25 units, and a blue wedge indicator at a value of 74, you would structure the `indicators` property as follows:
    ```json
    [
      {
        "value": 95,
        "indicatorStyle": "range",
        "color": "#D90000",
        "extent": 25
      },
      {
        "value": 74,
        "indicatorStyle": "wedge",
        "color": "#0000D9"
      }
    ]
    ```

# Schema - raw
{"schema":{"type":"object","definitions":{"TickConfig":{"type":"object","properties":{"color":{"format":"color","description":"Color of the tick","type":"string","default":""},"length":{"description":"Length of the tick","type":"number","default":20},"stroke":{"description":"Width of the tick","type":"number","default":1},"span":{"description":"Distance between each tick mark of this type","type":"number","default":20}}},"IndicatorConfig":{"type":"object","required":["value"],"additionalProperties":false,"properties":{"extent":{"description":"If indicatorStyle is 'range', the extent along the scale this indicator is placed (starting at 'value')","type":"number","default":2},"color":{"format":"color","description":"Color of this indicator, or of the area making up this indicator","type":"string","default":""},"length":{"description":"Length of this indicator, as measured by its x value within the scale","type":"number","default":25},"label":{"description":"Text to display along with this indicator","type":"string","default":""},"stroke":{"description":"If type 'line' or 'wedge', the width of this indicator","type":"number","default":1},"labelColor":{"format":"color","description":"Color of this indicator label","type":"string","default":""},"indicatorStyle":{"description":"'line' displays similar to a tick mark, 'wedge' displays a triangle shape, and 'range' displays a rectilinear range along the scale as measured by the property 'extent'","type":"string","enum":["line","wedge","range"],"default":"line"},"labelAngle":{"description":"Rotational angle of this indicator label","type":"number","default":0},"opacity":{"description":"Opacity of this indicator","type":"number","default":1},"value":{"description":"Value along the scale at which point this indicator is placed (or is started)","type":"number","default":0}}}},"properties":{"majorTicks":{"description":"The most prominent tick marks indicating periodic scale values","default":{"color":"","length":20,"stroke":1,"span":20},"$ref":"#/definitions/TickConfig"},"mirror":{"description":"Aligns the scale to the opposite side of the component","type":"boolean","default":false},"minorTicks":{"description":"Secondary tick marks indicating periodic scale values","default":{"color":"","length":10,"stroke":1,"span":5},"$ref":"#/definitions/TickConfig"},"maxValue":{"description":"The maximum value shown on the scale","type":"number","default":100},"fineTicks":{"description":"Smallest tick marks indicating periodic scale values, useful for very short spans","default":{"color":"","length":5,"stroke":1,"span":1},"$ref":"#/definitions/TickConfig"},"indicators":{"description":"Markers of special significance to place along the scale","type":"array","example":[{"extent":15,"color":"","length":25,"label":"High","stroke":1.5,"labelColor":"","indicatorStyle":"range","labelAngle":270,"opacity":0.4,"value":85},{"extent":2,"color":"","length":25,"label":"Low","stroke":2,"labelColor":"","indicatorStyle":"wedge","labelAngle":270,"opacity":1,"value":20}],"items":{"$ref":"#/definitions/IndicatorConfig"}},"reverse":{"description":"Inverts the order of scale values, so min to max is ordered in reverse","type":"boolean","default":false},"labels":{"description":"Displays of the numeric values of major tick marks","type":"object","properties":{"angle":{"description":"Rotation of the numeric labels","type":"number","default":0},"style":{"default":{"classes":"","fill":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"minValue":{"description":"The minimum value shown on the scale","type":"number","default":0},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"LinearScale","name":"Linear Scale","palette":{"variants":[{"tooltip":"A level indicator component that displays tick marks and labels.","label":"Linear Scale"}],"category":"display"},"id":"ia.display.linear-scale"}