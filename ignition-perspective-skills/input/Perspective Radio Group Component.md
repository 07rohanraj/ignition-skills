# Perspective Radio Group Component

## Description

This document outlines the usage and configuration of the Perspective Radio Group component, detailing how to define the set of radio button options, read the user's selection, customize the layout and visual appearance, and respond to user interaction events.

## Documentation

# Instructions
Here are the instructions for the Perspective Radio Group Component.

### **Component: Perspective Radio Group**

The Perspective Radio Group component is used to display a set of radio buttons, allowing a user to select only one option from the group. It is ideal for scenarios requiring a single, mutually exclusive choice from a visible set of options.

---

### **Instructions**

#### **1. Basic Configuration**

The core of the Radio Group is the `radios` property, which is an array of objects. Each object in this array defines a single radio button within the group.

To configure the radio buttons, you must modify the `radios` property. Each object in the `radios` array has the following properties:
*   `text`: (String | Number) The label displayed next to the radio button.
*   `value`: The value associated with the radio button. When this button is selected, the component's main `value` property will be updated to this value.
*   `selected`: (Boolean) If `true`, this radio button will be the selected one in the group. Only one item in the array should have `selected: true`.

**Example:** To create a group with three options:

```json
[
  {"text": "Option 1", "value": "opt1", "selected": true},
  {"text": "Option 2", "value": "opt2", "selected": false},
  {"text": "Option 3", "value": "opt3", "selected": false}
]
```

#### **2. Reading the Selected Value**

There are two primary properties to determine which radio button is currently selected:

*   **`value`**: This property holds the `value` of the selected radio button from the `radios` array. In the example above, the component's `value` would be `"opt1"`.
*   **`index`**: This property holds the numerical index of the selected radio button within the `radios` array. In the example above, the `index` would be `0`.

Changing either the `value` or `index` property will update the component's selection.

#### **3. Layout and Orientation**

You can control the arrangement and alignment of the radio buttons using the following properties:

*   **`orientation`**: Determines the direction the buttons are laid out.
    *   `"row"` (default): Arranges buttons horizontally.
    *   `"column"`: Arranges buttons vertically.
*   **`textPosition`**: Sets the position of the label text relative to the radio button icon.
    *   Options: `"top"`, `"right"` (default), `"bottom"`, `"left"`.
*   **`justify`**: Aligns the buttons along the main axis (`row` or `column`).
    *   Options: `"start"` (default), `"center"`, `"end"`, `"space-around"`, `"space-between"`, `"space-evenly"`.
*   **`align`**: Aligns the buttons along the cross axis (the axis perpendicular to the `orientation`).
    *   Options: `"start"`, `"center"` (default), `"end"`.

#### **4. Customizing Icons**

You can change the default radio button icons for both selected and unselected states.

*   **`selectedIcon`**: Defines the icon for the selected radio button.
    *   `path`: The path to the icon, typically in the format `"material/icon_name"`. The default is `"material/radio_button_checked"`.
    *   `color`: An object to set the icon color for `enabled` and `disabled` states.
    *   `style`: Apply a style class or inline styling to the icon.
*   **`unselectedIcon`**: Defines the icon for unselected radio buttons.
    *   `path`: The path to the icon. The default is `"material/radio_button_unchecked"`.
    *   `color`: An object to set the icon color for `enabled` and `disabled` states.
    *   `style`: Apply a style class or inline styling to the icon.

#### **5. Styling**

There are two distinct style properties:

*   **`style`**: Applies styles to the entire component container (e.g., border, background color of the whole group).
*   **`radioStyle`**: Applies styles to the individual radio buttons within the group.

#### **6. Events**

*   **`onActionPerformed`**: This event is the primary event for this component. It fires whenever the user clicks to select a different radio button. Use this event to trigger scripts or actions based on the user's selection.

---

### **Helpful Tips**

*   **Mutually Exclusive Selection:** Remember that only one radio button can be selected at a time. If you programmatically set `selected: true` on multiple objects within the `radios` array, only the last one in the array with that setting will be honored.
*   **`value` vs. `radios.value`:** Do not confuse the top-level `value` property of the component with the `value` property inside each object in the `radios` array. The top-level `value` is a read/write property that reflects the `value` of whichever radio is currently selected.
*   **Data Binding:** The `radios` property is often bound to a database query or a tag to dynamically generate the list of options. The `value` property is often bound to another tag to write the user's selection back to the PLC or a database.
*   **Layout Behavior:**
    *   When `orientation` is `"row"`, `justify` controls horizontal alignment and `align` controls vertical alignment.
    *   When `orientation` is `"column"`, `justify` controls vertical alignment and `align` controls horizontal alignment.
*   **Disabled State:** Setting the component's `enabled` property to `false` will prevent users from changing the selection. However, any scripts configured on events (like `onActionPerformed`) can still be triggered by user clicks, even in a disabled state.
*   **Component Choice:** Use the Radio Group for a small, finite set of options where all choices should be visible to the user. For a large number of options, consider using a `Dropdown` component to save space. If multiple selections are required, use multiple `Checkbox` components.
*   **Variants:** For quick setup, you can use the pre-configured variants from the Component Palette:
    *   **Text Right**: Default configuration.
    *   **Text Left**: Pre-sets `textPosition` to `"left"`.
    *   **Multiple**: Starts with three pre-configured radio buttons in the `radios` array.

# Schema - raw
{"schema":{"type":"object","definitions":{"icon":{"type":"object","oneOf":[{"required":["path"]},{"required":["library","name"]}],"default":{"color":{"enabled":"","disabled":""},"radioStyle":{"classes":""},"path":"","style":{"classes":""}},"properties":{"color":{"type":"object","properties":{"enabled":{"format":"color","description":"Color of the icon when enabled. Can be a named color.","type":"string","default":""},"disabled":{"format":"color","description":"Color of the icon when disabled. Can be a named color.","type":"string","default":""}}},"path":{"description":"Shorthand path to icon source, in format: library/iconName","type":"string","default":""},"library":{"description":"Optional alternative to 'path', name of library where icon is located. Must also supply 'name'.","type":"string"},"name":{"description":"Optional alternative to 'path', name of icon. Must also supply 'library'.","type":"string"},"style":{"style":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}},"properties":{"orientation":{"description":"The orientation or flex direction of radios.","type":"string","enum":["column","row"],"default":"row"},"textPosition":{"description":"Where to place label text in relation to radio button","type":"string","enum":["top","right","bottom","left"],"default":"right"},"index":{"description":"The index of the selected radio.","type":"number","default":0},"align":{"description":"Align radios along the cross axis. Vertical if orientation is set to row, horizontal if orientation is set to column.","type":"string","default":"center","suggestions":["start","center","end"]},"enabled":{"description":"If user should be allowed to select a radio.","type":"boolean","default":true},"radioStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"selectedIcon":{"description":"Icon to show when selected.","default":{"color":{"enabled":"","disabled":""},"path":"material/radio_button_checked","style":{"classes":""}},"$ref":"#/definitions/icon"},"radios":{"description":"List of radios that make up this group.","type":"array","default":[{"text":"Radio button","value":"Radio button","selected":true}],"items":{"type":"object","required":["value","text","selected"],"default":{"text":"Radio button","value":"","selected":false},"additionalProperties":false,"properties":{"text":{"description":"Text to pair with this radio.","type":["string","number"],"default":""},"value":{"description":"The value of the radio to be evaluated when selected.","default":""},"selected":{"description":"If true, this radio is selected.","type":"boolean","default":false}}}},"justify":{"description":"Justify radios along the main axis. Horizontal if orientation is set to row, vertical if orientation is set to column.","type":"string","default":"start","suggestions":["start","center","end","space-around","space-between","space-evenly"]},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"unselectedIcon":{"description":"Icon to show when unselected.","default":{"color":{"enabled":"","disabled":""},"path":"material/radio_button_unchecked","style":{"classes":""}},"$ref":"#/definitions/icon"},"value":{"description":"The value of the selected radio.","default":"Radio button"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"RadioGroup","name":"Radio Group","palette":{"variants":[{"tooltip":"A radio button group that allows mutually exclusive selection between it and its siblings.","label":"Radio Group"},{"tooltip":"A radio button group that allows mutually exclusive selection between it and its siblings.","label":"Text Right","id":"radio-group-right"},{"tooltip":"A radio button group that allows mutually exclusive selection between it and its siblings.","label":"Text Left","props":{"textPosition":"left"},"id":"radio-group-left"},{"tooltip":"A radio button group that allows mutually exclusive selection between it and its siblings.","label":"Multiple","props":{"radios":[{"text":"Radio button","value":"Radio button","selected":true},{"text":"Radio button","value":"Radio button","selected":false},{"text":"Radio button","value":"Radio button","selected":false}]},"id":"radio-group-multiple"}],"category":"input"},"id":"ia.input.radio-group","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}