# Perspective Slider Component

## Description

This document details the usage and configuration of the Perspective Slider component, a graphical control for selecting a numerical value within a defined range. It covers the component's core properties, such as value, range, orientation, and step increments, as well as options for customizing its appearance with labels and colors. The instructions also provide best practices for implementation, including property binding and event handling.

## Documentation

# Instructions
# Perspective Slider Component

## 1. Introduction
The Perspective Slider component provides a graphical way for users to select a numerical value from a defined range. It consists of a handle that can be dragged along a track (or rail). The component can be oriented either horizontally or vertically and can be customized with labels and colors to improve user experience.

## 2. Core Functionality & Configuration
The primary purpose of the Slider is to control a single numerical value. This value is stored in the `props.value` property. The range of the slider is determined by the `props.min` and `props.max` properties.

### Properties

| Property | Type | Description |
| --- | --- | --- |
| **value** | number | **(Primary Property)** The current numerical value represented by the slider handle's position. This is the property you will most often bind to a Tag or another component property. Default: `0`. |
| **min** | number | The minimum value for the slider scale (the far left or bottom of the track). Default: `0`. |
| **max** | number | The maximum value for the slider scale (the far right or top of the track). Default: `100`. |
| **step** | number | The interval the value will snap to when a user drags the handle. For example, a step of 5 will only allow the user to select values in increments of 5. **Note:** This does not restrict the `value` property when it is changed programmatically via a script or a binding. Default: `1`. |
| **orientation** | string | Determines the alignment of the slider track. Can be set to `"horizontal"` (default) or `"vertical"`. |
| **enabled** | boolean | If `true`, the user can interact with and drag the slider handle. If `false`, interaction is disabled. Default: `true`. |
| **labels** | object | An object containing properties for displaying numerical labels along the track. |
| &nbsp;&nbsp;&nbsp;labels.show | boolean | If `true`, labels are displayed along the track. If `false`, they are hidden. Default: `false`. |
| &nbsp;&nbsp;&nbsp;labels.interval | number | The numerical interval at which to display labels. For example, if `min` is 0 and `max` is 100, an interval of 20 will show labels at 0, 20, 40, 60, 80, and 100. Default: `20`. |
| **handleColor** | string | The color of the slider's draggable handle. This can be a hex code, RGB, or HSL value (e.g., `"#8AFF8A"`). |
| **trackColor** | string | The color of the portion of the track that indicates the current value (i.e., the space between `min` and the handle). |
| **railColor** | string | The color of the slider's background rail. |
| **style** | object | Allows for advanced CSS styling of the component, affecting aspects like background, margin, padding, border, and shape. |

### Events

| Event | Description |
| --- | --- |
| **onActionPerformed** | This event is fired when the user performs the primary action of the component. For the Slider, this typically occurs when the user changes the value by dragging the handle and releasing the mouse button. |

---

## 3. Helpful Tips & Best Practices

*   **Binding the `value` Property:** The most common use case for the Slider is to bidirectionally bind `props.value` to a Tag. This allows the slider to both display and control the Tag's value.
*   **Understanding the `step` Property:** Remember that the `step` property only affects user interaction. A binding or script can write any value to `props.value`, even if it doesn't align with the step interval. The slider handle will correctly display this non-step value.
*   **User-Friendly Labels:** To make the slider intuitive, it's highly recommended to enable labels. Set `props.labels.show` to `true` and choose a `props.labels.interval` that makes sense for your `min`/`max` range.
*   **Disabled State:** While setting `enabled` to `false` prevents the user from dragging the handle, other component events (like `onClick`) can still be configured to fire scripts.
*   **Color Customization:** Use `handleColor`, `trackColor`, and `railColor` for basic and quick color changes to match your application's theme. For more complex styling (e.g., changing border radius or adding a box shadow), use the `style` property.
*   **Orientation:** The default orientation is `"horizontal"`. To make the slider run from top to bottom, set the `orientation` property to `"vertical"`.

### Example Configuration

Here is an example of a vertical slider with customized colors and labels, as seen in the documentation:
*   `props.value`: `65`
*   `props.orientation`: `"vertical"`
*   `props.min`: `0` (default)
*   `props.max`: `100` (default)
*   `props.step`: `5`
*   `props.labels.show`: `true`
*   `props.labels.interval`: `10`
*   `props.handleColor`: `"#8AFF8A"`
*   `props.trackColor`: `"#CCFFFF"`

# Schema - raw
{"schema":{"type":"object","properties":{"orientation":{"description":"Whether slider track is aligned vertically or horizontally","type":"string","enum":["horizontal","vertical"],"default":"horizontal"},"handleColor":{"format":"color","description":"Color of slider handle","type":"string","default":""},"max":{"description":"Maximum value for slider scale","type":"number","default":100},"enabled":{"description":"Whether slider interaction is currently active","type":"boolean","default":true},"trackColor":{"format":"color","description":"Color of slider track","type":"string","default":""},"labels":{"type":"object","properties":{"show":{"description":"Whether to display labels at periodic values along track","type":"boolean","default":false},"interval":{"description":"Interval at which to display periodic labels along track","type":"number","default":20}}},"min":{"description":"Minimum value for slider scale","type":"number","default":0},"railColor":{"format":"color","description":"Color of slider rail","type":"string","default":""},"step":{"description":"Intervals along track at which value may be set","type":"number","default":1},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"description":"Value represented by slider handle","type":"number","default":0}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Slider","name":"Slider","palette":{"variants":[{"tooltip":"Enables a user to drag an indicator along a scale to choose a value in a range.","label":"Slider"}],"category":"input"},"id":"ia.input.slider","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}