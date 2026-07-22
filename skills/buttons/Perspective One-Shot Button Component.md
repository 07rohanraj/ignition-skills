# Perspective One-Shot Button Component

## Description

This document describes the usage and configuration of the Perspective One-Shot Button component, which is designed to perform a single action and then enter a disabled state until it is reset by an external process. The instructions explain the component's unique two-state workflow, its properties for customizing the 'ready' and 'writing' appearances, and the critical binding setup required for its operation.

## Documentation

# Instructions
# Perspective One-Shot Button Component

## Object Description
The Perspective One-Shot Button component is a specialized button used to write a value to a tag or property and then enter a "writing" state. It remains in this state until an external mechanism resets the value, at which point it returns to its initial "ready" state. This is ideal for scenarios where an action should only be triggered once, and the UI should reflect the ongoing process until it's confirmed to be complete by the backend system (e.g., a PLC).

The core functionality revolves around the relationship between two properties: `value` and `setValue`.

### The "One-Shot" Workflow:
1.  **Ready State**: The button is initially in its "ready" state, displaying the text, icon, and styling defined in the `readyState` property. In this state, the component's `value` is not equal to its `setValue`.
2.  **Action**: A user clicks the button.
3.  **Write**: The component writes the value from its `setValue` property to the property or tag that is bound to its `value` property. For this to work correctly, the `value` property should have a bidirectional binding to a tag.
4.  **Writing State**: Once the write is successful, the component's `value` becomes equal to its `setValue`. This equality triggers a state change. The button is now in its "writing" state, displaying the configuration from the `writingState` property. While in this state, the button is effectively disabled.
5.  **External Reset**: The button will remain in the "writing" state until some external system (like a PLC script or another process) changes the tag's value. The new value must be different from the `setValue` property.
6.  **Return to Ready**: As soon as the bidirectional binding updates the component's `value` to be different from `setValue`, the button automatically reverts to its "ready" state, ready to be clicked again.

---

## Properties

This component has the following properties:

| Property | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| **value** | `any` | The current value of the component. This property is the key to the component's state and should be bidirectionally bound to a tag or another property that will be externally reset. | `0` |
| **setValue** | `any` | The value that will be written to the `value` property when the button is clicked. When `value` equals `setValue`, the button enters its `writingState`. | `1` |
| **enabled** | `boolean` | If `true`, the user can interact with the button. If `false`, the button is disabled. | `true` |
| **primary** | `boolean` | Toggles the button's visual style between the default `primary` (true) and a `secondary` (false) appearance. | `true` |
| **readyState** | `object` | An object that defines the appearance of the button when `value` is not equal to `setValue`. It contains the following sub-properties: `text`, `icon`, and `style`. | |
| &emsp;`readyState.text` | `string` | The text displayed on the button in its ready state. | "One-Shot Button" |
| &emsp;`readyState.icon` | `object` | An object defining an icon to display on the button. | |
| &emsp;`readyState.style` | `object` | A style object that applies to the button only when it is in the ready state. | |
| **writingState** | `object` | An object that defines the appearance of the button when `value` is equal to `setValue`. It contains the following sub-properties: `text`, `icon`, and `style`. | |
| &emsp;`writingState.text` | `string` | The text displayed on the button in its writing state. | "Writing..." |
| &emsp;`writingState.icon` | `object` | An object defining an icon to display on the button. | |
| &emsp;`writingState.style` | `object` | A style object that applies to the button only when it is in the writing state. | |
| **confirm** | `object` | An object that configures a confirmation dialog that appears when the button is clicked. | |
| &emsp;`confirm.enabled` | `boolean` | If `true`, a confirmation dialog will be shown before the button's action is performed. | `false` |
| &emsp;`confirm.text` | `string` | The message to display in the confirmation dialog. | "Are you sure?" |
| **style** | `object` | The base style object for the component. | |
| **disabledStyle** | `object` | The style object that is applied when the `enabled` property is `false`. | |

---

## Events

The primary event for this component is:

*   **onActionPerformed**: This event fires when the primary action of the component occurs. For the One-Shot button, this happens *after* the user clicks the button (and confirms the action, if `confirm.enabled` is `true`).

---

## Helpful Tips & Best Practices

*   **Crucial Binding**: The `value` property **must** be configured with a **bidirectional** binding to a Tag for the component to function as intended. The button writes a value out, and then listens for that value to be changed externally.
*   **External Logic is Required**: Remember that the One-Shot Button **does not** reset itself. You must have an external process, like a PLC, a gateway script, or another user action, that changes the value of the tag linked to the `value` property.
*   **Confirmation and Scripts**: If you enable the `confirm` property (`confirm.enabled: true`), any scripts or actions you want to run should be configured on the `onActionPerformed` event. This event waits for the user to click "OK" in the confirmation dialog before it executes.
*   **Two Visual States**: The button's appearance is controlled by two distinct property objects: `readyState` (for when `value != setValue`) and `writingState` (for when `value == setValue`). You can customize the text, icon, and styling for each state independently.
*   **Disabled State**: The button is automatically disabled while in its `writingState`. You can also manually disable it at any time by setting the `enabled` property to `false`. The `disabledStyle` property will be applied in this case.
*   **Styling Order**: Be aware that if you are using both `style` classes and the `disabledStyle` properties, CSS rules will be applied in alphabetical order of the class names. A style from a class later in the alphabet could override a style from one earlier in the alphabet.
*   **Component Variants**: The component palette offers pre-configured variants to speed up design:
    *   **Primary/Secondary**: Toggles the `primary` property for a different visual theme.
    *   **Require Confirm**: A button with `confirm.enabled` set to `true` by default.

# Schema - raw
{"schema":{"type":"object","properties":{"enabled":{"description":"Whether user can currently interact with the One-Shot Button","type":"boolean","default":true},"confirm":{"type":"object","properties":{"enabled":{"description":"If true, a confirmation box will be shown.","type":"boolean","default":false},"text":{"description":"Message to show user if confirmation is enabled.","type":"string","default":"Are you sure?"}}},"writingState":{"type":"object","example":{"icon":{"path":"material/hourglass_empty","style":{"width":"2rem","height":"24px"}},"style":{"classes":""},"text":"Writing..."},"properties":{"icon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"The text of the button while it's value is being written.","type":"string"}}},"setValue":{"type":["boolean","null","number","string"],"default":1},"readyState":{"type":"object","example":{"icon":{"path":"","style":{"width":"2rem","height":"24px"}},"style":{"classes":""},"text":"One-Shot Button"},"properties":{"icon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"The text of the button while it's value is not being written.","type":"string"}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"disabledStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"type":["boolean","null","number","string"],"default":0},"primary":{"description":"Toggle between the default primary and secondary button style.","type":"boolean","default":true}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"OneShotButton","name":"One-Shot Button","palette":{"variants":[{"tooltip":"A control button that sets a value and waits for it to be reset by some external mechanism.","label":"One Shot Button"},{"tooltip":"A control button that sets a value and waits for it to be reset by some external mechanism.","label":"Primary","id":"oneshotbutton-primary"},{"tooltip":"A control button that sets a value and waits for it to be reset by some external mechanism.","label":"Secondary","props":{"primary":false},"id":"oneshotbutton-secondary"},{"tooltip":"A control button that sets a value and waits for it to be reset by some external mechanism.","label":"Require Confirm","props":{"confirm":{"enabled":true}},"id":"oneshotbutton-require-confirm"}],"category":"input"},"id":"ia.input.oneshotbutton","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}