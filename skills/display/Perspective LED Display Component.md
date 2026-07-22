# Perspective LED Display Component

## Description

These instructions describe the configuration and use of the Perspective LED Display component. The document explains how to display numeric or alphanumeric data by customizing properties such as the visual style, color scheme, and value formatting to create a stylized, digital LED-like label.

## Documentation

# Instructions
# Perspective LED Display Component Instructions

## Object Description
The Perspective LED Display component is a stylized label that mimics the appearance of a segmented Light Emitting Diode (LED) display. It's used to show numeric or alphanumeric values. The component is visually configurable, offering two main styles: a 7-segment display, typically used for numbers, and a 14-segment display, which can represent a wider range of letters and numbers.

## Properties
Below is a detailed list of the component's properties.

| Property | Type | Description |
| :--- | :--- | :--- |
| `value` | `number` or `string` | This is the primary content to be shown on the display. It can accept both numerical and text values. |
| `segmentFormat` | `string` | Determines the visual style of the characters. It has two possible options: <br> - **`7 segment`**: A classic display style suitable for digits. <br> - **`14 segment`**: A more complex style that allows for better representation of alphanumeric characters. This is the default setting. |
| `numberFormat` | `string` | A format string that dictates how numeric values are displayed, including the use of commas, decimal points, and percentage signs. This property only affects the display when the `value` is a number. The available formats are: `"#,##0"`, `"#,##0.0"`, `"#,##0.00"`, `"0"`, `"0.0"`, `"0.00"`, `"#,##0.00;(#,##0.00)"`, `"#,##0%"`, `"0.###E0"`. The default is `"#,##0.00"`. |
| `backgroundColor` | `color` | Sets the background color of the display surface itself. The default is a dark gray (`#161616`). |
| `diodeOnColor` | `color` | Sets the color of the individual segments when they are lit up or "on". The default is a bright green (`#1EC963`). |
| `diodeOffColor` | `color` | Sets the color of the individual segments when they are "off". For a realistic analog look, this should be a color that is distinct from the `backgroundColor` but much less prominent than the `diodeOnColor`. |
| `locale` | `string` | A localization code (e.g., "en-US", "de-DE") that defines the rules for formatting numbers, such as which character to use for decimal points versus thousands separators. The default is "en-US". |
| `style` | `object` | An object that holds various style properties for the component, allowing for customization of its appearance, including text styles, background, margins, padding, borders, and shape. You can also assign a pre-defined style class. |

## Component Variants
When dragging the LED Display onto a view, you have these pre-configured options:
*   **LED Display**: The default variant, which uses the `14 segment` format.
*   **14 Segment**: Identical to the default variant.
*   **7 Segment**: A variant where the `segmentFormat` property is pre-set to `7 segment`.

---
## Helpful Tips
*   **Alphanumeric Characters**: If you need to display text (alphanumeric characters), you must use the `14 segment` format. The `7 segment` format is not designed to render all letters intelligibly.
*   **Numeric Formatting**: The `numberFormat` property will have no effect if the `value` you provide is a string, even if that string contains a number (e.g., "123.45"). For formatting to apply, the `value` must be a numeric type.
*   **Aesthetic Customization**: The combination of `backgroundColor`, `diodeOnColor`, and `diodeOffColor` is key to the component's appearance. To create a realistic effect where unlit segments are still faintly visible, make the `diodeOffColor` slightly different from the `backgroundColor`. If you set `diodeOffColor` and `backgroundColor` to the same color, the unlit segments will be completely invisible.
*   **Styling with Borders and Padding**: Use the `style` property to add finishing touches. For example, you can set `props.style.borderStyle` to `"groove"` to give the component a 3D-style border, or set `props.style.padding` to `"2px"` to add some space between the display content and the border.
*   **Dynamic Data**: Most properties, especially the `value` property, can be bound to data sources like Tags. This allows you to create a dynamic display that updates in real-time with process values.
*   **Localization**: Remember to set the `locale` property if the application will be used in different regions. This ensures that numbers like `1,234.56` are displayed correctly according to local conventions.
*   **Component Events**: Like other Perspective components, the LED Display can trigger actions based on user interaction events (e.g., mouse clicks). These are configured via the Component Events and Actions interface in the designer.

# Schema - raw
{"schema":{"type":"object","properties":{"backgroundColor":{"format":"color","description":"Color of display surface","type":"string","default":""},"locale":{"description":"Localization code that determines rules for commas, decimals, etc.","type":"string","default":"en-US"},"diodeOffColor":{"format":"color","description":"Color of segments when switched off - generally different from display background color to preserve analogue look","type":"string","default":""},"numberFormat":{"description":"Format of display for numeric values, including commas, decimal places etc.","type":"string","enum":["#,##0","#,##0.0","#,##0.00","0","0.0","0.00","#,##0.00;(#,##0.00)","#,##0%","0.###E0"],"default":"#,##0.00"},"diodeOnColor":{"format":"color","description":"Color of segments when switched on","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"description":"Value to be displayed","type":["number","string"],"default":0},"segmentFormat":{"description":"Style of each character/digit - number of segments that compose the character","type":"string","enum":["7 segment","14 segment"],"default":"14 segment"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"LedDisplay","name":"LED Display","palette":{"variants":[{"tooltip":"A stylized numeric and/or alphanumeric label styled like a segmented LED and capable of 7-segments or 14-segments.","label":"LED Display"},{"tooltip":"A stylized numeric and/or alphanumeric label styled like a segmented LED and capable of 7-segments or 14-segments.","label":"14 Segment","id":"led-display-14"},{"tooltip":"A stylized numeric and/or alphanumeric label styled like a segmented LED and capable of 7-segments or 14-segments.","label":"7 Segment","props":{"segmentFormat":"7 segment"},"id":"led-display-7"}],"category":"display"},"id":"ia.display.led-display"}