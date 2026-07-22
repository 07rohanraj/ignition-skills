# Perspective Numeric Entry Field Component

## Description

This guide describes the configuration and usage of the Perspective Numeric Entry Field component. It details how to control its core features, including user interaction modes, numeric display formatting, custom styling, and input validation rules. The instructions enable a user to effectively implement the component for accepting and managing numeric input.

## Documentation

# Instructions
Here are the instructions and helpful tips for using the Perspective Numeric Entry Field component in Ignition.

### **Goal**

To provide a comprehensive guide for an LLM to understand and utilize the **Perspective Numeric Entry Field** component. This component is designed to accept numeric input from a user in a Perspective session.

### **Component Overview**

The Numeric Entry Field is a specialized input component, similar to a standard Text Field, but tailored specifically for handling numbers. It allows users to view and, when enabled, edit a numeric value. The component offers several modes of interaction to control how users edit the value, extensive formatting options for displaying the number, and built-in validation to ensure the input is within specified bounds.

---

### **Core Concepts**

*   **Modes of Interaction (`mode`):** This is a critical property that defines the user experience for editing the value.
    *   **`direct`:** The default mode. A single click on the field makes it editable. This is best for forms or screens where rapid data entry is expected.
    *   **`protected`:** Requires a double-click or a long press to enter edit mode. This is useful for preventing accidental changes to important values.
    *   **`button`:** Displays an "Edit" icon next to the value. Clicking this icon opens a popup where the user can enter the new value or cancel the edit. The value can *only* be changed through this popup.

*   **Value Formatting (`format`):** The `format` property allows you to control the visual representation of the numeric value. You can use predefined format strings to display numbers as currency, percentages, integers, and more. The component supports locale-specific formatting, which automatically adjusts the number's appearance based on the session's locale settings after the primary format is applied.

*   **Styling (`style` vs. `containerStyle`):** Understanding the two style properties is key to customizing the component's appearance.
    *   **`containerStyle`:** Applies styles to the outermost element of the component. Use this for properties that affect the entire component, such as adding a border, setting margins around the component, or adding padding between the border and the inner input area.
    *   **`style`:** Applies styles directly to the inner element that displays the numeric value. Use this for properties like changing the font color, font size, background color of the text area, or text alignment.

*   **Input Validation (`inputBounds`):** This property allows you to enforce limits on the user's input.
    *   You can define a `minimum` and a `maximum` allowable value.
    *   If the user enters a value outside these bounds, the style defined in the `invalidStyle` property will be applied, providing immediate visual feedback that the input is not valid.

---

### **Component Properties**

| Property | Type | Description |
| :--- | :--- | :--- |
| **`value`** | Number / String | The numeric value to be displayed. It can be bound to a tag or a database query. Note that values larger than JavaScript's maximum safe integer (9,007,199,254,740,991) may lead to unpredictable behavior. |
| **`format`** | String | A formatting string that dictates how the `value` is displayed. A list of suggested formats includes options for currency (`$0,0.00`), percentages (`0.##%`), integers (`0,0`), scientific notation (`0.00e+0`), and others. The documentation mentions that a full list of format specifiers can be found at `http://numeraljs.com/#format`. |
| **`mode`** | String | Determines the interaction required to edit the value. Can be set to `direct`, `protected`, or `button`. |
| **`enabled`** | Boolean | If `true` (default), the user is allowed to interact with and alter the value. If `false`, the component is read-only. User interaction events (like clicks) will not fire, but system events (like onStartup) can still execute scripts. |
| **`align`** | String | Aligns the displayed value to the `left` or `right` (default) within the input area. |
| **`placeholder`** | String | Text that appears in the component when its `value` is null or an empty string. This is useful for providing guidance to the user, such as "Enter Setpoint". |
| **`tooltipText`** | String | Text that appears in a small popup when the user's mouse hovers over the component. |
| **`inputBounds`** | Object | An object containing properties to configure input validation. |
| `inputBounds.minimum` | Number | The minimum allowable value for the input. |
| `inputBounds.maximum` | Number | The maximum allowable value for the input. |
| `inputBounds.invalidStyle` | Style Object | The style applied to the component when the entered value is outside the `minimum` and `maximum` bounds. |
| **`spinner`** | Object | An object containing properties to configure the increment/decrement spinner buttons. |
| `spinner.enabled` | Boolean | If `true` (default), up and down arrow buttons (a "spinner") will be displayed on the component, allowing the user to increment or decrement the value. |
| `spinner.increment` | Number | The amount the value should change by each time a spinner button is clicked. Defaults to `1`. |
| **`style`** | Style Object | Defines the style for the inner numeric display/input area. Use this for text color, background color, etc. |
| **`containerStyle`** | Style Object | Defines the style for the outer container of the component. Use this for borders, margins, etc. |

---

### **Component Events**

*   **`onActionPerformed`**: This is the primary event for the Numeric Entry Field. It fires when the "action" of the component occurs. This typically means when a user confirms their new value, either by pressing the "Enter" key while editing or when the component loses focus after the value has been changed. You can configure actions (e.g., run a script, write to a tag) to be triggered by this event.

---

### **Big List of Helpful Tips**

*   **Choosing the Right Mode:** Match the `mode` to the use case. Use `direct` for fast-paced data entry forms. Use `protected` for critical setpoints on an HMI to prevent accidental changes. Use `button` when you want a more explicit, guided editing process, as it provides a clear "commit" or "cancel" choice in its popup.
*   **Palette Variants are Shortcuts:** The "Direct", "Protected", and "Button" variants in the Component Palette are simply pre-configured versions of the Numeric Entry Field with the `mode` property already set accordingly.
*   **Clear User Guidance:** Use the `placeholder` property to inform users what kind of input is expected when the field is empty (e.g., "Enter a value between 0-100").
*   **Provide Context with `tooltipText`:** Use the `tooltipText` property to give more detailed information about the value or its purpose when the user hovers over the component.
*   **Visual Feedback is Key:** Combine `inputBounds` with a distinct `invalidStyle`. For example, set the `invalidStyle` to have a light red background color and a red border. This gives the user immediate and unambiguous feedback if their entry is out of the acceptable range.
*   **Style vs. `containerStyle`:** Remember the distinction. To change the font color of the number, use `style.color`. To put a border around the entire component, use `containerStyle.border`.
*   **Using the Spinner:** The `spinner` is a great way to improve usability for small, precise adjustments. Enable it when users are likely to increment or decrement a value by a fixed step.
*   **Handling Nulls:** The component will show the `placeholder` text if its `value` property is `null`. This is useful for distinguishing between a value of `0` and no value at all.
*   **Formatting for Readability:** Use the `format` property to make values easier to read. For example, use `"0,0"` to add a thousands separator to large numbers, or `"$0,0.00"` to clearly indicate a currency value.
*   **Binding the `value`:** The `value` property will almost always be bound to a Tag, a database query, or another component property to make it dynamic.
*   **`onActionPerformed` for Actions:** This event is where you should trigger any logic that needs to run after a user submits a new value, such as writing the value back to a PLC tag or saving it to a database.

# Schema - raw
{"schema":{"type":"object","properties":{"inputBounds":{"description":"Max and min input value bounds configuration.","type":"object","properties":{"maximum":{"description":"The max allowable input value.","type":["number","null"],"default":null},"invalidStyle":{"description":"Style applied to input when input value does not meet bounds.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"minimum":{"description":"The min allowable input value.","type":["number","null"],"default":null}}},"tooltipText":{"description":"Mousing over this button will show a tooltip with this text, if present","type":"string","default":""},"containerStyle":{"description":"Applies style to the root element of the component which contains the input and edit button. Use the style prop to apply style to the input element directly","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"format":{"description":"Format to apply to number.","type":["string","number"],"default":"0,0.##","suggestions":{"integer [1,200]":"0,0","none":"none","number [1,000.12]":"0,0.##","percent [10.12%]":"0.##%","currency [$1,000.12]":"$0,0.00","currency (rounded) [$1,012]":"$0,0","accounting [$ (1,000.12)]":"$ (0,0.00)","financial [(1,000.12)]":"(0,0.00)","duration [24:01:00]":"00:00:00","scientific [1.01E+03]":"0.00e+0","ordinal [100th]":"0o","abbreviation [1.2k]":"0.0a","four decimal precision [1.1200]":"0,0.0000"}},"align":{"description":"Aligns the input's value right or left.","type":"string","enum":["right","left"],"default":"right"},"enabled":{"description":"If user should be allowed to alter the value.","type":"boolean","default":true},"mode":{"description":"Can be direct, protected, or button. Direct mode requires no special action to enter into edit mode. Protected requires double click or long-press to enter edit mode. Button requires that the user click the button to enter edit mode.","type":"string","enum":["direct","protected","button"],"default":"direct"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"placeholder":{"description":"Text displayed when value is empty.","type":"string","default":""},"value":{"description":"Value as a number or numeric string. Values larger than 9,007,199,254,740,991 (JavaScript's max safe integer) will behave unpredictably.","type":["string","number"],"default":""},"spinner":{"description":"Provides buttons for incrementing & decrementing the value","type":"object","properties":{"increment":{"description":"The amount to increment or decrement the value when the spinner's buttons are clicked.","type":"number","default":1},"enabled":{"description":"The spinner will be displayed when enabled.","type":"boolean","default":true}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"NumericEntryField","name":"Numeric Entry Field","palette":{"variants":[{"tooltip":"A text field that is specialized for use with numbers only.","label":"Numeric Entry Field"},{"tooltip":"A text field that is specialized for use with numbers only.","label":"Direct","props":{"mode":"direct"},"id":"numeric-entry-field-direct"},{"tooltip":"A text field that is specialized for use with numbers only.","label":"Protected","props":{"mode":"protected"},"id":"numeric-entry-field-protected"},{"tooltip":"A text field that is specialized for use with numbers only.","label":"Button","props":{"mode":"button"},"id":"numeric-entry-field-button"}],"category":"input"},"id":"ia.input.numeric-entry-field","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}