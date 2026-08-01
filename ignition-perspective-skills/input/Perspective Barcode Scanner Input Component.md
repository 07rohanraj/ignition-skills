# Perspective Barcode Scanner Input Component

## Description

The configuration and usage of the Perspective Barcode Scanner Input component, a specialized tool for capturing data from a keyboard wedge scanner without requiring page focus. It operates by either identifying scans bracketed by a defined prefix and suffix, or by using a JavaScript regular expression to extract a specific pattern from the input stream. Upon a successful scan, the captured value is added to a data property and an event is triggered to allow for immediate processing of the new information.

## Documentation

# Instructions
# Perspective Barcode Scanner Input Component Instructions

## Overview
The Perspective Barcode Scanner Input component is a specialized input field designed to capture data from a keyboard wedge barcode scanner. Unlike a standard text field, this component does not need to have focus on the page to receive input. It is always listening for character input that matches its configured pattern, making it ideal for dedicated scanning stations. When a valid scan is detected, the component adds the captured barcode value to its `data` property.

The component has two primary modes of operation for detecting a valid scan: **Prefix/Suffix Mode** and **Regex Mode**.

---

## Modes of Operation

### 1. Prefix/Suffix Mode
This is the primary and simplest mode of operation. You define a specific `prefix` and/or `suffix` string that your barcode scanner sends before and after the actual barcode data.

- The component listens for the `prefix` string.
- Once the prefix is detected, it starts capturing all subsequent characters.
- When the `suffix` string is detected, the capture ends.
- The captured text, **excluding the prefix and suffix**, is then added as a new string to the `data` property array.

**CRITICAL:** If either the `prefix` or `suffix` property is set to a non-empty string, **the `regex` property will be completely ignored.**

### 2. Regex Mode
This mode is used when the `prefix` and `suffix` properties are both empty strings. It allows for more complex pattern matching to identify and extract barcode data from a stream of characters.

- The component maintains a buffer of the most recent characters entered. The size of this buffer is determined by the `window` property.
- It continuously tries to match the JavaScript `regex` pattern against the text in the buffer.
- If a match is found, the value from the **first capture group** `(...)` of the regular expression is extracted.
- This extracted value is then added as a new string to the `data` property array.

**CRITICAL:** The regular expression provided **must** use JavaScript regex syntax. It is also crucial that the expression contains at least one capture group `(...)`, as only the content of the first capture group is used for the data.

---

## Properties

### Data Properties
| Property | Type | Description |
| :--- | :--- | :--- |
| **`data`** | `array` of `string` | This read-only property holds the barcode scans returned from the scanner. Each successful scan adds a new string element to this array. |

### General Properties
| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **`prefix`** | `string` | `""` | A string that marks the beginning of a barcode scan. If this property is not an empty string, `regex` mode is disabled. |
| **`suffix`** | `string` | `""` | A string that marks the end of a barcode scan. If this property is not an empty string, `regex` mode is disabled. |
| **`regex`** | `string` | `""` | A JavaScript regular expression used to describe the format of a scan. This is only used if `prefix` and `suffix` are both empty. The **first capture group** of the regex is used as the barcode value. |
| **`window`** | `number` | `20` | The length of the character buffer to monitor for a `regex` match. Only relevant when in Regex Mode. |
| **`captureMode`** | `string` (enum) | `keypress` | Specifies which key event the component will listen for. Options are: `keyup`, `keydown`, `keypress`. |

### Style Properties
| Property | Type | Description |
| :--- | :--- | :--- |
| **`dataStyle`** | `Style Object` | Defines the style for the data returned to the component. Affects properties like text color, background color, margins, etc. |
| **`style`** | `Style Object` | Defines the style for the component itself, which is typically not visible. Styles can be set before a value is scanned. |

---

## Events

| Event | Description |
| :--- | :--- |
| **`onActionPerformed`** | This event fires when a valid barcode is successfully scanned and added to the `data` property. This is the primary event to configure actions or scripts that should run after a scan, such as looking up the scanned value in a database or moving it to another component. |

---

## Helpful Tips & Best Practices

*   **No Focus Required:** Remember that the Barcode Scanner Input component is always listening globally on the page. It does not need to be clicked on or have focus to start capturing input. This means you can place it on a view and it will work in the background.
*   **Prefix/Suffix Precedence:** Always remember that if you provide any value to the `prefix` or `suffix` properties, the `regex` property will be ignored. To use regex, ensure both `prefix` and `suffix` are empty strings.
*   **Data is an Array:** The `data` property is an array that accumulates scans. A new scan is appended to the end of the array. If you only care about the most recent scan, you might use an expression like `props.data[len(props.data)-1]` or handle new data in the `onActionPerformed` event and then clear the array.
*   **Regex Capture Groups are Essential:** When using `regex` mode, a common mistake is forgetting to include a capture group `(...)` in your pattern. A regex like `[A-Z]{2}[0-9]{4}` might match "AB1234", but nothing will be captured. You must write it as `([A-Z]{2}[0-9]{4})` to capture "AB1234". If the pattern were `([A-Z]{2})([0-9]{4})`, only the content of the first group, "AB", would be captured.
*   **Prefix/Suffix are Excluded:** The `prefix` and `suffix` values are used only to identify the start and end of the scan. They are automatically stripped from the result and will not appear in the `data` property.
*   **Choosing `captureMode`:** The default `keypress` works for most scenarios. Some scanner hardware might behave differently, requiring you to use `keydown` or `keyup` to capture scans reliably. Test with your specific hardware.
*   **Processing Scans:** The most common way to use the captured data is to add a script to the `onActionPerformed` event. This event provides a clean and reliable trigger to run logic every time a new scan is completed.
*   **JavaScript Regex:** Be aware that the `regex` property uses JavaScript's flavor of regular expressions, which may have slight differences from regex engines in other environments like Python or Java.

# Schema - raw
{"schema":{"type":"object","properties":{"data":{"description":"Barcode scans returned from scanner","type":"array","items":{"type":"string"}},"prefix":{"description":"String that marks the start of barcode scan capture.","type":"string","default":""},"dataStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"suffix":{"description":"String that marks the end of barcode scan capture.","type":"string","default":""},"regex":{"description":"Regex describing format of scans. The first capture will be used as barcode.","type":"string","default":""},"captureMode":{"description":"Key capture mode used for specifying key event to listen for.","type":"string","enum":["keyup","keydown","keypress"],"default":"keypress"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"window":{"description":"Length of buffer to monitor for regex match.","type":"number","default":20}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"BarcodeScannerInput","name":"Barcode Scanner Input","palette":{"variants":[{"tooltip":"Enables users to scan a barcode directly from a device's built-in camera.","label":"Barcode Scanner Input"}],"category":"input"},"id":"ia.input.barcodescannerinput","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}