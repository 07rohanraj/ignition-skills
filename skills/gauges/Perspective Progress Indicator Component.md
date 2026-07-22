# Perspective Progress Indicator Component

## Description

These instructions detail the configuration and usage of the Perspective Progress Indicator Component. This component allows for the visual representation of a task's progress, which can be configured for either known durations (determinate) or unknown durations (indeterminate). The documentation outlines the extensive properties available for customizing the appearance of the progress bar, its track, and an optional text overlay for the current value.

## Documentation

# Instructions
# Perspective Progress Indicator Component

## Description
The Perspective Progress Indicator Component provides a visual indication of the progress of a task. It is used to display any value that has a defined minimum and maximum bound. The component can operate in two modes: "determinate", which shows progress as a percentage of completion from a known start and end point, and "indeterminate", which is used for tasks of unknown duration, showing a continuous animation instead of a specific progress value.

The appearance of the progress bar, its track, and an optional value display can be extensively customized through various properties and styles.

## Properties

### Top-Level Properties
*   **`value`** (Number): The current value representing the progress. This value should be between the `min` and `max` properties. Default is `50`.
*   **`min`** (Number): The minimum value of the progress indicator. When `value` is equal to `min`, the progress indicator will be empty. It must be less than `max`. Default is `0`.
*   **`max`** (Number): The maximum value of the progress indicator. When `value` is equal to `max`, the progress indicator will be completely filled. It must be greater than `min`. Default is `100`.
*   **`mode`** (String): Defines the operational mode of the component.
    *   `determinate`: Shows the progress of the `value` property relative to the `min` and `max` properties.
    *   `indeterminate`: Shows a continuous loading animation, used when the duration or progress of a task is not known.
*   **`style`** (Object): An object that defines the overall style for the component. A full menu of style options is available for text, background, margin and padding, border, shape, and miscellaneous settings. You can also specify a style class.

---

### `bar` Properties
This object contains settings for the progress bar itself (the part that fills up).

*   **`bar.color`** (String - Color): A convenience property for setting the base color of the bar. This can also be set via `bar.style.backgroundColor`.
*   **`bar.style`** (Object): Sets a style for the bar. A full menu of style options is available.
*   **`bar.determinate`** (Object): Contains configuration properties that apply only when the `mode` is "determinate".
    *   **`bar.determinate.color`** (String - Color): A convenience property for setting the bar's color specifically in "determinate" mode.
    *   **`bar.determinate.style`** (Object): Sets a style for the bar specifically in "determinate" mode.
*   **`bar.indeterminate`** (Object): Contains configuration properties that apply only when the `mode` is "indeterminate".
    *   **`bar.indeterminate.color`** (String - Color): A convenience property for setting the bar's color specifically in "indeterminate" mode.
    *   **`bar.indeterminate.style`** (Object): Sets a style for the bar specifically in "indeterminate" mode.

---

### `track` Properties
This object contains settings for the track of the progress bar (the background).

*   **`track.color`** (String - Color): A convenience property for setting the base color of the track. This can also be set via `track.style.backgroundColor`.
*   **`track.style`** (Object): Sets a style for the track. A full menu of style options is available.
*   **`track.determinate`** (Object): Contains configuration properties that apply only when the `mode` is "determinate".
    *   **`track.determinate.color`** (String - Color): A convenience property for setting the track's color specifically in "determinate" mode.
    *   **`track.determinate.style`** (Object): Sets a style for the track specifically in "determinate" mode.
*   **`track.indeterminate`** (Object): Contains configuration properties that apply only when the `mode` is "indeterminate".
    *   **`track.indeterminate.color`** (String - Color): A convenience property for setting the track's color specifically in "indeterminate" mode.
    *   **`track.indeterminate.style`** (Object): Sets a style for the track specifically in "indeterminate" mode.

---

### `valueDisplay` Properties
This object configures a text overlay that is rendered on top of the progress bar to display the current value.

*   **`valueDisplay.enabled`** (Boolean): If `true`, the value display overlay is shown. Default is `false`.
*   **`valueDisplay.format`** (String): A format string to apply to the `value` for display. Common options include:
    *   `0,0`: Integer (e.g., 100)
    *   `0,0.##`: Number with decimals (e.g., 50.25)
    *   `0.##%`: Percent (e.g., 50.25%)
    *   `$0,0.00`: Currency (e.g., $1,000.12)
    *   `00:00:00`: Duration (e.g., 24:01:00)
    *   `none`: No formatting.
*   **`valueDisplay.justify`** (String): Sets the horizontal alignment of the displayed value.
    *   `left`
    *   `center` (default)
    *   `right`
*   **`valueDisplay.style`** (Object): An object that defines the style for the value display text. A full menu of style options is available.

---

## Helpful Tips
*   **Choosing a Mode**: Use `determinate` mode when you can track the progress of an operation (e.g., processing records, file transfers). Use `indeterminate` mode for operations where the completion time is unknown (e.g., waiting for a server response).
*   **Styling Precedence**: The most specific style or color property will be applied. For example, if `mode` is "determinate", the `bar.determinate.color` property will be used for the bar's color over the more general `bar.color` property. The same logic applies to the `style` objects.
*   **Data Binding**: For a `determinate` progress bar to be effective, its `value` property should be bound to a data source that updates over time, such as a Tag or the output of a script.
*   **Value Display Formatting**: The `valueDisplay.format` property is very flexible. For a progress bar with a `min` of 0 and a `max` of 100, setting the format to `0'%'` will display the value as a percentage (e.g., "75%").
*   **Convenience vs. Style**: The `bar.color` and `track.color` properties are shortcuts. For more advanced styling, like gradients or borders, use the corresponding `style` objects (e.g., `bar.style`, `track.style`).
*   **Example Configuration**: To create a customized progress bar, you can set multiple properties. For instance, to create an orange bar on a light orange track with rounded corners and a bold percentage display in the center:
    *   `value`: `56`
    *   `mode`: `determinate`
    *   `bar.color`: `#FFAC47`
    *   `track.color`: `#FFE8CC`
    *   `track.style.borderStyle`: `solid`
    *   `track.style.borderWidth`: `2px`
    *   `track.style.borderRadius`: `15px`
    *   `track.style.borderColor`: `#A45324`
    *   `valueDisplay.enabled`: `true`
    *   `valueDisplay.format`: `0'%'`
    *   `valueDisplay.justify`: `center`
    *   `valueDisplay.style.fontWeight`: `bold`
    *   `valueDisplay.style.fontFamily`: `Merriweather`

# Schema - raw
{"schema":{"type":"object","properties":{"max":{"description":"The maximum value of the progress indicator. If the value reaches the max, the progress indicator will be completely filled. Must be greater than min.","type":"number","default":100},"mode":{"description":"","type":"string","enum":["determinate","indeterminate"],"default":"determinate"},"valueDisplay":{"description":"Value display configuration.  Renders and styles a value overlay above the progress bar.","type":"object","properties":{"format":{"description":"Format to apply to value which is then used and the value display.","type":["string","number"],"default":"0,0.##","suggestions":{"integer [1,200]":"0,0","none":"none","percent [10.12%]":"0.##%","currency [$1,000.12]":"$0,0.00","duration [24:01:00]":"00:00:00"}},"enabled":{"description":"If true, will show the value display overlay","type":"boolean","default":false},"justify":{"description":"Horizontal alignment of displayed value","type":"string","enum":["left","center","right"],"default":"center"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"bar":{"type":"object","properties":{"color":{"format":"color","description":"A convenience property for setting the base color of the bar, can also be accomplished via style by setting backgroundColor.","type":"string","default":""},"indeterminate":{"description":"Indeterminate bar configuration.","type":"object","properties":{"color":{"format":"color","description":"A convenience property for setting the color of the bar when mode is indeterminate, can also be accomplished via style by setting backgroundColor.","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"determinate":{"description":"Determinate bar configuration.","type":"object","properties":{"color":{"format":"color","description":"A convenience property for setting the background color of the bar when mode is determinate, can also be accomplished via style by setting backgroundColor.","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"min":{"description":"The minimum value of the progress indicator. If the value reaches the min, the progress indicator will be completely empty. Must be less than max.","type":"number","default":0},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"track":{"type":"object","properties":{"color":{"format":"color","description":"A convenience property for setting the base color of the track, can also be accomplished via style by setting backgroundColor.","type":"string","default":""},"indeterminate":{"description":"Indeterminate track configuration.","type":"object","properties":{"color":{"format":"color","description":"A convenience property for setting the color of the track when mode is indeterminate, can also be accomplished via style by setting backgroundColor.","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"determinate":{"description":"Determinate track configuration.","type":"object","properties":{"color":{"format":"color","description":"A convenience property for setting the color of the track when mode is determinate, can also be accomplished via style by setting backgroundColor.","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"value":{"description":"The current value representing the current progress. Must be greater than 0.0 and less than max.","type":"number","default":50}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Progress","name":"Progress","palette":{"variants":[{"tooltip":"Provides a visual indication of the progress of a task.","label":"Progress"}],"category":"display"},"id":"ia.display.progress"}