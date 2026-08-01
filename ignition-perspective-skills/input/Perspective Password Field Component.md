# Perspective Password Field Component

## Description

This guide covers the configuration and usage of the Perspective Password Field component, a secure input for entering passwords. It explains the component's core properties, such as text masking and a reveal option, along with key scripting events and best practices for implementing user authentication.

## Documentation

# Instructions
### INSTRUCTIONS FOR THE PERSPECTIVE PASSWORD FIELD COMPONENT

#### Introduction
The Password Field component is a specialized text input field designed for securely entering passwords. It visually masks the characters as they are typed. It is functionally similar to a standard Text Field but includes specific features for handling sensitive password data, such as a reveal option.

---

### Core Concepts

*   **Password Masking**: By default, any text entered into the field is visually obscured by dots or asterisks to prevent shoulder-surfing. The actual password value is stored in the `text` property.
*   **Placeholder Text**: When the `text` property is empty, you can display a helpful prompt or placeholder (e.g., "Enter your password") to the user. This is configured via the `placeholder` property.
*   **Reveal Functionality**: You can provide the user with an icon to temporarily unmask the password, allowing them to verify what they've typed. This behavior is controlled by the `allowReveal` property.

---

### Properties

Below is a detailed list of the component's properties.

| Property Name | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| **`text`** | `string` | This is the most important property. It holds the actual password value entered by the user. You will bind this property or use its value in scripts for authentication. | `""` |
| **`placeholder`** | `string` | The text that is displayed inside the input field when the `text` property is empty. This is used to provide guidance to the user. | `""` |
| **`enabled`** | `boolean` | Determines if the user can interact with and enter text into the component. If `false`, the field is visually "greyed out" and cannot be edited by the user. | `true` |
| **`allowReveal`** | `boolean` | If `true`, a small icon appears in the field that allows the user to click and hold to temporarily reveal the password text. If `false`, this icon is hidden. | `true` |
| **`style`** | `object` | An object containing various style properties for the component. This allows you to customize the appearance, including text styles, background color, borders, margins, and more. You can also assign a named Style Class. | |

---

### Component Events

While the component supports the standard set of Perspective component events, here are some key considerations:

*   **`onActionPerformed`**: This event is commonly used. It fires when the user presses the "Enter" or "Return" key while the component is focused. This is ideal for triggering a login script without requiring a separate button.
*   **User Interaction Events (`onClick`, `onFocusReceived`, `onFocusLost`, etc.)**: These events will **not** fire if the component's `enabled` property is set to `false`.
*   **System Events (`onStartup`, `onShutdown`)**: These events will execute their scripts regardless of the `enabled` property's state. For example, an `onStartup` script on a disabled Password Field will still run when the view loads.

---

### Helpful Tips & Best Practices

*   **Binding the `text` Property**: For login forms, you should typically have a bi-directional binding on the `props.text` property to a component custom property or a memory tag. This makes it easy to access the password from a button's script action. **Do not** bind the password text to a database tag or any tag that would store the raw password insecurely.
*   **Using `placeholder`**: Always use the `placeholder` property to guide users. It improves the user experience by making the form more intuitive.
*   **Leverage `allowReveal`**: For better usability, it is recommended to keep `allowReveal` set to `true`. This helps users avoid typing errors when entering complex passwords.
*   **Providing User Feedback with `style`**: You can dynamically change the component's style to provide feedback. For example, after a failed login attempt, you could change the `style.borderColor` to red and `style.borderStyle` to 'solid' to indicate an error, as shown in the documentation example.
*   **Login Scripting**: The common use case is to pair this component with a Button. The button's `onActionPerformed` event would trigger a script that takes the `text` value from the Password Field and uses it in an authentication script (e.g., `system.security.login`).
*   **Clearing the Field**: After a login attempt (successful or not), it is good practice to clear the `props.text` property for security reasons.
*   **Disabled State Nuance**: Remember that even if `enabled` is `false`, scripts on system events like `onStartup` will still run. This is important to know if you have any logic configured on those events.

# Schema - raw
{"schema":{"type":"object","properties":{"allowReveal":{"description":"Describes whether the user has the ability to temporarily remove the password mask, revealing the password.","type":"boolean","default":true},"enabled":{"description":"If user should be allowed to alter password text.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Password text.","type":"string","default":""},"placeholder":{"description":"Text displayed when password text is empty.","type":["string","number"],"default":""}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"PasswordField","name":"Password Field","palette":{"variants":[{"tooltip":"A text field designed to be used for password entry. It does not display the text that is being entered.","label":"Password Field"}],"category":"input"},"id":"ia.input.password-field"}