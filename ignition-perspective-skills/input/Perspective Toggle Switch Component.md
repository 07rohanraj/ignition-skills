# Perspective Toggle Switch Component

## Description

This documentation describes the configuration and usage of the Perspective Toggle Switch component, a UI element that represents a binary on/off state. It covers how to customize the component's appearance, such as its colors and label, manage its `selected` state, and handle user interaction via the `onActionPerformed` event.

## Documentation

# Instructions
# Perspective Toggle Switch Component

## General Description
The Perspective Toggle Switch component represents a binary state, typically a bit that is either on (selected) or off (not selected). It functions very similarly to a Checkbox but provides a different visual representation. When a user interacts with the switch, it toggles its `selected` state. By default, the switch is blue when selected and gray when not selected.

The component is highly customizable, allowing for changes to its colors, the addition of a label, and control over its enabled state.

## Component Events
### onActionPerformed
This is the primary event for the Toggle Switch. It fires whenever the user interacts with the component, causing a change in its state (i.e., when the switch is toggled). You can configure actions, such as running a script, in response to this event.

## Component Properties

### `selected`
This is the most critical property of the Toggle Switch. It holds the current state of the component.
*   **Type:** `boolean`
*   **Default:** `false`
*   **Usage:** A value of `true` indicates the switch is in the "on" or "selected" state. A value of `false` indicates the "off" or "unselected" state. This property is often bound to a tag or another property.

### `label`
This property is an object that contains settings for the text label associated with the toggle switch.
*   **Type:** `object`
*   **Properties:**
    *   **`text`**:
        *   **Description:** The text to be displayed for the label.
        *   **Type:** `string`
        *   **Default:** `""` (empty string)
        *   **Note:** You can edit this text directly in the Designer by deep-selecting the component.
    *   **`position`**:
        *   **Description:** Determines the position of the label relative to the switch.
        *   **Type:** `string`
        *   **Accepted Values:** `"left"`, `"right"`
        *   **Default:** `"right"`
    *   **`style`**:
        *   **Description:** An object for applying inline CSS styles specifically to the label's text. This allows you to control the font, color, and other text-specific styles independently of the main component's style.
        *   **Type:** `object`
        *   **Default:** `{}`

### `color`
This property is an object that allows for customizing the colors of the toggle switch slider for both of its states.
*   **Type:** `object`
*   **Properties:**
    *   **`selected`**:
        *   **Description:** The color of the switch's slider when the component's `selected` property is `true`.
        *   **Type:** `string` (color format)
        *   **Default:** `""` (defaults to blue)
    *   **`unselected`**:
        *   **Description:** The color of the switch's slider when the component's `selected` property is `false`.
        *   **Type:** `string` (color format)
        *   **Default:** `""` (defaults to gray)

### `enabled`
This property controls whether the user can interact with the component.
*   **Type:** `boolean`
*   **Default:** `true`
*   **Usage:** When `true`, the user can click or tap the switch to change its state. When `false`, the switch is visually "grayed out" and does not respond to user input.
*   **Critical Note:** Disabling the component via this property (`enabled: false`) only prevents the user from *altering its state*. Any configured events, such as an `onActionPerformed` script, will still execute if the user clicks on the disabled component.

### `style`
This property allows you to apply inline CSS styles to the main component container.
*   **Type:** `object` (`Style Properties`)
*   **Usage:** Use this to control aspects like the background, margin, padding, border, and shape of the entire Toggle Switch component. This is distinct from `label.style`, which only affects the text.

## Palette Variants
When dragging a Toggle Switch onto a View from the Component Palette, you have several pre-configured variants:
*   **Toggle Switch (No Text):** The default variant with no label text.
*   **Text Right:** A Toggle Switch with placeholder text positioned to the right of the switch.
*   **Text Left:** A Toggle Switch with placeholder text positioned to the left of the switch.

## Helpful Tips
*   The `selected` property is the main data property. Bind this to a bidirectional Tag to control and monitor the state of a device or a value in the PLC.
*   To handle user interaction, configure an action on the `onActionPerformed` event. This is the standard way to trigger scripts or other actions when the switch is toggled.
*   Remember the distinction between the two `style` properties: `props.style` for the entire component and `props.label.style` for the label text only.
*   If the Toggle Switch appears unresponsive to clicks, check that the `enabled` property is set to `true`.
*   Even if `enabled` is `false`, `onClick` events and other configured events will still fire. The `enabled` property only prevents the `selected` state from changing through direct user interaction.
*   You can set colors using various formats, including hex codes (e.g., `#FF0000`), RGB values, or by using the built-in Color Selector in the Designer.
*   If you don't specify colors under `props.color`, the component will use its default theme colors (typically blue for selected, gray for unselected).
*   For quick edits to the label, you can double-click (or deep-select) the component in the design space to edit the `label.text` property inline.

# Schema - raw
{"schema":{"type":"object","properties":{"color":{"type":"object","default":{"unselected":"","selected":""},"properties":{"unselected":{"format":"color","description":"Color of the slider when the toggle switch is selected.","type":"string","default":""},"selected":{"format":"color","description":"Color of the slider when the toggle switch is selected.","type":"string","default":""}}},"label":{"type":"object","default":{"style":{},"text":"","position":"right"},"properties":{"style":{"description":"Inline style for the text element.","default":{},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text for the toggle switch.","type":"string","default":""},"position":{"description":"Text position relative to the toggle switch.","type":"string","enum":["left","right"],"default":"right"}}},"enabled":{"description":"Whether the user should be allowed to alter the toggle switch's selected state.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"selected":{"description":"The selected state of the toggle switch.","type":"boolean","default":false}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"ToggleSwitch","name":"Toggle Switch","palette":{"variants":[{"tooltip":"A switch component that represents a bit that can be toggled on (selected) or off (not selected).","label":"Toggle Switch"},{"tooltip":"A switch component that represents a bit that can be toggled on (selected) or off (not selected).","label":"No Text","id":"toggle-switch-no-text"},{"tooltip":"A switch component that represents a bit that can be toggled on (selected) or off (not selected).","label":"Text Right","props":{"label":{"text":"text"}},"id":"toggle-switch-text-right"},{"tooltip":"A switch component that represents a bit that can be toggled on (selected) or off (not selected).","label":"Text Left","props":{"label":{"text":"text","position":"left"}},"id":"toggle-switch-text-left"}],"category":"input"},"id":"ia.input.toggle-switch","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}