# Perspective Text Field Component

## Description

A guide to the usage and configuration of the Perspective Text Field component, a control designed to accept a single line of text from a user. These instructions cover its core properties for managing the text value and placeholder hints, along with critical settings for controlling data update behavior. It also explains how to trigger actions based on user interaction and distinguish its use from multi-line or numeric-only input fields.

## Documentation

# Instructions
# Perspective Text Field Component Instructions

## Role

You are an expert technical writer for Inductive Automation's Ignition platform. Your task is to provide a comprehensive guide for an LLM on how to understand and use the Perspective Text Field component. You will synthesize information from the provided component schema and documentation to create a detailed set of instructions and helpful tips. You must not include any information that is not present in the provided context.

---

## General Functionality

The Perspective Text Field component is a fundamental input control used to accept a single line of any alpha-numeric text from a user. It is the standard choice for simple, one-line text entries.

It is important to distinguish the Text Field from similar components:
*   For text input that requires **multiple lines**, use the **Text Area** component.
*   For input that should be restricted to **numbers**, use the **Numeric Entry Field** component.

## User Interaction

In a running Perspective session, a user interacts with the Text Field in the following ways:
*   **Editing:** To begin editing, the user must either double-click the field or select it and press the "Enter" key.
*   **Committing Changes:** To confirm the entered text and push the value to the `props.text` property, the user must either press "Enter" again or click/focus away from the component (lose focus).
*   **Disabled State:** If the `props.enabled` property is set to `false`, the user cannot interact with or edit the text in the field, even if it is selected.

---

## Properties

The following properties are available for the Text Field component and can be configured in the Perspective Property Editor.

| Property                    | Type             | Description                                                                                                                                                             | Default Value |
| --------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `text`                      | `string`         | The text content to display inside the field. This property is typically bound to a database tag or another component property to display and/or receive data.                | `""`          |
| `placeholder`               | `string`         | The hint text that is displayed inside the field whenever the `props.text` property is empty. This is useful for prompting the user on the expected input.                    | `""`          |
| `enabled`                   | `boolean`        | If `true`, the user can interact with and alter the text in the field. If `false`, the field is read-only.                                                                 | `true`        |
| `deferUpdates`              | `boolean`        | If `true`, any changes a user makes to the text are only sent to the `props.text` property after the user either presses "Enter" or the component loses focus.                 | `true`        |
| `rejectUpdatesWhileFocused` | `boolean`        | If `true`, the component will ignore any external updates to the `props.text` property (e.g., from a property binding) while the user is actively editing the field (i.e., while it is focused). This prevents the user's input from being overwritten mid-edit. | `true`        |
| `spellcheck`                | `boolean`        | If `true`, the user's web browser will perform its native spell-checking on the text as it is being edited, typically underlining potential errors in red. Behavior may vary slightly between different web browsers. | `true`        |
| `style`                     | `object`         | An object that holds all the style configurations for the component, such as text color, background, borders, and margins. You can also assign a pre-configured Style Class. | N/A           |

---

## Component Events

You can configure actions to be triggered by user interactions with the Text Field component. This is done through the Component Events system in the Perspective Designer. For example, you could run a script when the user presses "Enter" after typing in the field.

A full list of all possible event types and detailed instructions on how to configure them are available on the "Perspective Event Types Reference" and "Component Events and Actions" pages in the official documentation.

---

## Helpful Tips for the LLM

*   **Choosing the Right Component:** Always clarify if the user needs a single-line input, multi-line input (Text Area), or numeric input (Numeric Entry Field) to ensure you suggest the correct component.
*   **Guiding the User:** Advise using the `placeholder` property to provide a clear example or instruction of what should be typed into the field, such as "Enter your name" or "Scan barcode here".
*   **Controlling Data Flow:** The `deferUpdates` and `rejectUpdatesWhileFocused` properties are critical for creating a stable user experience, especially when the `text` property is bound to a tag that might change frequently.
    *   Use `deferUpdates` (set to `true`) to prevent the component from writing a new value on every single keystroke, which can be inefficient.
    *   Use `rejectUpdatesWhileFocused` (set to `true`) to prevent a user's typing from being erased or overwritten by an incoming data change from a binding.
*   **Enabling and Disabling Input:** You can dynamically control the `enabled` property. For example, you can bind it to a Checkbox component to allow a user to lock/unlock the Text Field.
*   **Styling:** For consistent styling across multiple Text Fields or other components, recommend the use of Style Classes over individual styling configurations.
*   **Triggering Actions:** When a user needs to perform an action after entering text (like submitting data or running a query), configure a script on a relevant component event, such as `onActionPerformed` (fired when Enter is pressed) or `onFocusLost`.

# Schema - raw
{"schema":{"type":"object","properties":{"rejectUpdatesWhileFocused":{"description":"When true, props.text will not accept updates from external sources while focused.","type":"boolean","default":true},"enabled":{"description":"If user should be allowed to alter text.","type":"boolean","default":true},"spellcheck":{"description":"When true, the component will highlight potential spelling errors while text is being edited.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display","type":"string","default":""},"placeholder":{"description":"Text displayed when text is empty","type":["string","number"],"default":""},"deferUpdates":{"description":"When true, updates to props.text will be deferred until focus is lost or enter is pressed.","type":"boolean","default":true}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"TextField","name":"Text Field","palette":{"variants":[{"tooltip":"Used for input of a single line of text.","label":"Text Field"}],"category":"input"},"id":"ia.input.text-field"}