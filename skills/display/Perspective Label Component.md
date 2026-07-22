# Perspective Label Component

## Description

This document details the configuration and usage of the Perspective Label Component for displaying text. It covers the available properties for setting the text content, adjusting vertical alignment, and applying distinct styling to both the text and the component's container.

## Documentation

# Instructions
# Perspective Label Component

## Introduction
The Perspective Label Component is a fundamental tool used for displaying text on a screen. It can render various types of data as text, including strings, numbers, and booleans. Its appearance is highly customizable through styling properties.

## Object Properties
The Label component has the following properties:

| Property | Type | Description | Default Value |
|---|---|---|---|
| `text` | `string`, `number`, `boolean`, `null`, `object`, `array` | The content you want the label to display. If an object or array is provided, it will be displayed as a string representation (e.g., JSON format). | `""` (empty string) |
| `alignVertical` | `string` | Determines how the text is vertically aligned within the component's boundaries. | `"center"` |
| `style` | `object` | An object that defines the CSS styling for the entire Label component's container (e.g., background color, border, padding). | (empty style object) |
| `textStyle` | `object` | An object that defines the CSS styling specifically for the text itself (e.g., font color, font size, font weight). | (empty style object) |

### `alignVertical` Options
*   `"top"`: Aligns the text to the top of the component.
*   `"center"`: Aligns the text to the vertical center of the component.
*   `"bottom"`: Aligns the text to the bottom of the component.

## Helpful Tips
*   **Primary Function:** Use the Label component whenever you need to display static or dynamic text.
*   **Data Binding:** The `text` property is often bound to other properties or tags to display dynamic information. For example, you can bind it to a Tag to show a real-time value from a PLC.
*   **Styling Distinction:** It is important to understand the difference between the `style` and `textStyle` properties.
    *   The `style` property block affects the entire component. You would use it to change the `backgroundColor`, `border`, or `padding` of the label's container.
    *   The `textStyle` property block affects only the text within the component. You would use it to change the text's `color`, `fontSize`, `fontWeight`, `textAlign`, etc.
*   **Horizontal Alignment:** To align the text horizontally (left, center, right), you must use the `textAlign` property within the `textStyle` object. For example: `props.textStyle.textAlign = "right"`.
*   **Displaying Non-Text Data:** While the `text` property accepts various data types like objects and arrays, be aware that they will be converted to a string for display. For example, an object will be shown in its JSON string format.
*   **Combining Styles:** You can use both `style` and `textStyle` together. For instance, you could give the component a dark background using `style.backgroundColor` and make the text light-colored using `textStyle.color` to ensure readability.

# Schema - raw
{"schema":{"type":"object","properties":{"alignVertical":{"description":"How to vertically align the text in the dimensions of the component","type":"string","enum":["top","center","bottom"],"default":"center"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display","type":["string","number","boolean","null","object","array"],"example":"Label","default":""},"textStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Label","name":"Label","palette":{"variants":[{"tooltip":"A simple component for displaying text.","label":"Label"}],"category":"display"},"id":"ia.display.label"}