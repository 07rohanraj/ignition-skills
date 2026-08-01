# Perspective Signature Pad Component

## Description

This document describes the usage and configuration of the Perspective Signature Pad component, detailing its properties for customization, its events for processing captured signature data, and its scripting functions for programmatic control.

## Documentation

# Instructions
This document provides instructions for using the **Perspective Signature Pad Component** in Ignition.

### Object Name
Perspective Signature Pad Component

### Description
The Signature Pad component provides a canvas for users to draw a signature using a mouse or touchscreen. The captured signature can then be submitted, triggering events that allow for further processing, such as saving the signature as an image file or storing it in a database. It includes built-in "Submit" and "Clear" buttons and is highly customizable in appearance and behavior.

### Properties
The component's properties are organized into several categories.

**Top-Level Properties**
| Property | Type | Description | Default |
| --- | --- | --- | --- |
| `enabled` | boolean | If `true`, the entire component (canvas, buttons, and scripting functions) is interactive. If `false`, the component is disabled. | `true` |
| `style` | object | Manages the overall style of the component, including borders, margins, and padding. | - |

**`pad` Properties**
This object contains properties related to the drawing area itself.
| Property | Type | Description | Default |
| --- | --- | --- | --- |
| `pad.canvas.clearColor` | color | Sets the visible background color of the canvas. **Note:** According to documentation examples, this color is for display purposes only and is *not* included in the final submitted signature image, which will have a transparent background. | `transparent` |
| `pad.canvas.style` | object | Style properties specifically for the canvas, such as border or background image. | - |
| `pad.pen.color` | color | The color of the ink used for drawing the signature. Accepts HEX, RGB, or HSL values. | `#000000` |
| `pad.pen.width` | number | The width (in pixels) of the pen's stroke. | `1` |

**`actionBar` Properties**
This object controls the appearance and behavior of the "Submit" and "Clear" buttons.
| Property | Type | Description | Default |
| --- | --- | --- | --- |
| `actionBar.position` | string | Positions the action bar relative to the canvas. Enum: `top`, `bottom`, `left`, `right`. | `bottom` |
| `actionBar.style` | object | Style properties for the action bar container itself. | - |
| `actionBar.submitButton.text` | string | The text displayed on the submit button. | `"Submit"` |
| `actionBar.submitButton.enabled` | boolean | If `true`, the submit button is clickable. This does not affect the `submitSignature()` scripting function. | `true` |
| `actionBar.submitButton.primary` | boolean | If `true`, uses the primary button style. If `false`, uses the secondary style. | `true` |
| `actionBar.submitButton.style` | object | Style properties for the submit button. | - |
| `actionBar.clearButton.text` | string | The text displayed on the clear button. | `"Clear"` |
| `actionBar.clearButton.enabled` | boolean | If `true`, the clear button is clickable. This does not affect the `clearSignature()` scripting function. | `true` |
| `actionBar.clearButton.primary` | boolean | If `true`, uses the primary button style. If `false`, uses the secondary style. | `false` |
| `actionBar.clearButton.style` | object | Style properties for the clear button. | - |

**`status` Properties**
This read-only object provides information about the current state of the pad.
| Property | Type | Description | Default |
| --- | --- | --- | --- |
| `status.touched` | boolean | Becomes `true` as soon as the user starts drawing on the pad. It remains `true` until the signature is cleared. | `false` |

---

### Component Events
You can configure actions for the following component events by right-clicking the component and selecting "Configure Events...".

**`onSignatureSubmitted`**
*   **Description:** This event fires after a signature is successfully submitted, either by clicking the submit button or by calling the `submitSignature()` function. It is the primary event for handling the captured signature data.
*   **Event Object Properties:** When configuring a script action for this event, the `event` object contains the following properties:
    *   `event.signature` (String): A Base64-encoded PNG DataURL of the signature image. Useful for direct display in other components or for embedding.
    *   `event.signatureFile` (Object): An object representing the signature as a file, with the following details and methods:
        *   `name` (String): The name of the signature file.
        *   `size` (Integer): The size of the signature file in bytes.
        *   `getBytes()` (Function): Returns a byte array (`byte[]`) of the image. This is typically used with `system.perspective.download()` to let the user download the file.
        *   `copyTo(filePath)` (Function): Saves the signature file to a specified path on the Gateway's filesystem. The `filePath` argument is a string (e.g., `"C:\\signatures\\user_sig.png"`).
        *   `getString()` (Function): Attempts to parse the file data as a string using UTF-8 encoding. This is generally not useful for image files.

**`onSignatureCleared`**
*   **Description:** Fires after the signature has been cleared, either by the user clicking the "Clear" button or by calling the `clearSignature()` function.
*   **Event Object Properties:** The `event` object for this event is empty (null).

---

### Component Scripting
These functions can be called from other scripts (e.g., from another component's event script) to control the Signature Pad. To call them, you need a reference to the component, for example: `self.getSibling("SignaturePad").clearSignature()`.

*   **`.clearSignature()`**
    *   **Description:** Clears the current signature from the canvas. This is functionally identical to clicking the "Clear" button.
    *   **Parameters:** None
    *   **Returns:** Nothing

*   **`.submitSignature()`**
    *   **Description:** Submits the current signature, which triggers the `onSignatureSubmitted` event. This is functionally identical to clicking the "Submit" button.
    *   **Parameters:** None
    *   **Returns:** Nothing

---

### Helpful Tips
*   **Saving vs. Downloading:** To save the signature to the server (Gateway), use the `onSignatureSubmitted` event with a script that calls `event.signatureFile.copyTo("C:\\path\\on\\server\\signature.png")`. To allow the user to download the signature to their own computer, use a script that calls `system.perspective.download("Signature.png", event.signatureFile.getBytes())`.
*   **Controlling the Pad Externally:** You can create your own custom "Submit" or "Clear" buttons elsewhere on the view. In the script for your custom button's `onActionPerformed` event, call `self.getSibling("SignaturePad").submitSignature()` or `self.getSibling("SignaturePad").clearSignature()`.
*   **Disabling Buttons vs. Component:** Disabling the built-in submit or clear buttons (e.g., `props.actionBar.submitButton.enabled = false`) only affects the UI button. The `submitSignature()` and `clearSignature()` scripting functions will still work. To disable all interaction, set the component's main `props.enabled` property to `false`.
*   **Checking for a Signature:** You can bind a property on another component to the `status.touched` property. This allows you to enable or disable other components (like a save button) based on whether the user has started signing.
*   **Styling the Background:** Use `props.pad.canvas.clearColor` to set a background color for the drawing area that is *not* included in the final image. To have a background color or image that *is* part of the final submitted signature, use the `props.pad.canvas.style.backgroundColor` or `props.pad.canvas.style.backgroundImage` properties instead.
*   **Signature Data Formats:**
    *   `event.signature` provides a Base64 string. This is useful if you need to store the signature as text in a database or display it in an Image component by binding the Image's `source` property to the `event.signature` value.
    *   `event.signatureFile` is an object designed for file operations. Use its methods (`getBytes`, `copyTo`) when you need to treat the signature as a physical file.
*   **Example Download Script:** To configure the component to download the signature when submitted:
    1.  Right-click the Signature Pad and select "Configure Events".
    2.  Select the `onSignatureSubmitted` event.
    3.  Add a "Script" action.
    4.  Enter the following code:
        ```python
        # This script runs in the Gateway scope and downloads the file to the user's browser.
        image_bytes = event.signatureFile.getBytes()
        system.perspective.download("MySignature.png", image_bytes)
        ```
*   **No Extension Functions:** This component does not have any associated extension functions. All scripting is done through the component methods and events listed above.

# Schema - raw
{"schema":{"description":"A component for collecting signatures","type":"object","title":"Signature Pad","additionalProperties":false,"properties":{"actionBar":{"type":"object","additionalProperties":false,"properties":{"submitButton":{"type":"object","additionalProperties":false,"properties":{"enabled":{"description":"Enables submit button interaction. This does not affect the submitSignature component scripting function.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display on button","type":["string","number"],"default":"Submit"},"primary":{"description":"Toggle between the default primary and secondary button style.","type":"boolean","default":true}}},"clearButton":{"type":"object","additionalProperties":false,"properties":{"enabled":{"description":"Enables clear button interaction. This does not affect the clearSignature component scripting function.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display on button","type":["string","number"],"default":"Clear"},"primary":{"description":"Toggle between the default primary and secondary button style.","type":"boolean","default":false}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"position":{"description":"Action Bar position relative to the canvas.","type":"string","enum":["top","bottom","left","right"],"default":"bottom"}}},"enabled":{"description":"When enabled the canvas, clear button, and submit button are interactable, and component scripting functions for clearSignature and submitSignature are enabled.","type":"boolean","default":true},"pad":{"type":"object","additionalProperties":false,"properties":{"canvas":{"type":"object","additionalProperties":false,"properties":{"clearColor":{"format":"color","description":"Visible canvas color which will be submitted as part of the signature image.","type":"string","default":"transparent"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"pen":{"type":"object","properties":{"color":{"format":"color","description":"Color used to draw the lines with the pen.","type":"string","default":"#000000"},"width":{"description":"Width of the lines drawn by the pen.","type":"number","default":1}}}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"status":{"type":"object","properties":{"touched":{"description":"True when the signature pad contains a signature.","type":"boolean","default":false}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"SignaturePad","name":"Signature Pad","palette":{"variants":[{"tooltip":"Enables users to draw a signature and “submit” it.","label":"Signature Pad"}],"category":"input"},"id":"ia.input.signature-pad","events":[{"schema":{"type":"object","properties":{"signature":{"description":"Base64-encoded PNG DataURL of the submitted signature.","type":"string"},"signatureFile":{"type":"object","properties":{"size":{"description":"The size (in bytes) of the submitted signature file.","type":"integer"},"name":{"description":"The name of the submitted signature file.","type":"string"}}}}},"documentationUrl":"https://links.inductiveautomation.com/81-signature-pad-component-events","description":"Fired after the gateway has received a submitted signature.","name":"onSignatureSubmitted"},{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-signature-pad-component-events","description":"Fired after the gateway has received a signal that the signature has been cleared.","name":"onSignatureCleared"}]}