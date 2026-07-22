# Perspective Checkbox Component

## Description

The configuration and use of the Perspective Checkbox component, explaining how to set its binary or three-state selection, customize its text label and icons, and understand its event behavior, particularly that events will still fire when the component is disabled.

## Documentation

# Instructions
# Perspective Checkbox Component

## Instructions for Use

### General
The Perspective Checkbox component is a standard input control that represents a binary state, such as on/off or true/false. It can also be configured to support a third, indeterminate state. Its primary purpose is to allow a user to make a simple selection, which is then reflected in the component's `selected` property.

### Core Properties and Configuration

#### State and Value (`selected` and `triState`)
The most important property of the Checkbox is `selected`, which holds the current state of the component.
- **Binary State**: By default, `triState` is `false`. In this mode, the `selected` property can only be a boolean: `true` (checked) or `false` (unchecked).
- **Ternary (Three-State) Mode**: To enable the third "indeterminate" state, you must set the `triState` property to `true`. When enabled, the `selected` property can be `true`, `false`, or `null`. The `null` value represents the indeterminate state, which is visually distinct. This is useful for scenarios where a selection is neither explicitly on nor off.

#### Labeling (`text` and `textPosition`)
- **Text**: The `text` property contains the string that will be displayed as a label for the checkbox.
- **Text Position**: The `textPosition` property determines where the label appears relative to the checkbox itself. The possible values are:
    - `top`
    - `right` (Default)
    - `bottom`
    - `left`

#### Interactivity (`enabled`)
The `enabled` property is a boolean that controls whether a user can interact with the checkbox.
- If `true` (default), the user can click the checkbox to change its state.
- If `false`, the checkbox will be visually greyed out and will not respond to user clicks to change its state. **However, it is critical to note that any configured events, such as an `onActionPerformed` event, will still fire if the user clicks the disabled component.**

#### Icons (`checkedIcon`, `uncheckedIcon`, `indeterminateIcon`)
You can customize the appearance of the checkbox in each of its possible states by configuring its icon properties. Each of these is an object that contains settings for the icon.

- **`checkedIcon`**: The icon to display when `selected` is `true`. (Default: `material/check_box`)
- **`uncheckedIcon`**: The icon to display when `selected` is `false`. (Default: `material/check_box_outline_blank`)
- **`indeterminateIcon`**: The icon to display when `selected` is `null`. This icon is only used if the `triState` property is set to `true`. (Default: `material/indeterminate_check_box`)

Within each icon object, you can set the following:
- **`path`**: The path to the icon, specified in the format `library/iconName`.
- **`color`**: An object to define the color of the icon in its `enabled` and `disabled` states.
- **`style`**: A standard style object to apply custom styles to the icon.

### Events
The primary event for the Checkbox component is `onActionPerformed`. This event fires whenever the user performs the primary action on the component, which is clicking it to attempt to change its state.

---

## Helpful Tips

*   The `selected` property is the main output of the component. It can be `true`, `false`, or `null`.
*   To use the `null` value (the indeterminate state), you **must** set the `triState` property to `true`. Otherwise, `selected` will only ever be `true` or `false`.
*   **CRITICAL**: A disabled checkbox (`enabled: false`) prevents the user from changing its state, but it **does not** prevent component events from firing. If you have a script on the `onActionPerformed` event, it will still run when a user clicks the disabled checkbox.
*   For a consistent user experience, especially when using `triState`, remember to configure all three icon properties: `checkedIcon`, `uncheckedIcon`, and `indeterminateIcon`.
*   The label text can be edited quickly in the Designer by "deep selecting" the component, which enables inline editing of the `text` property.
*   The Checkbox component is functionally equivalent to the Toggle Switch component, offering a different visual style for the same type of input.
*   The component palette offers pre-configured variants for "Text Right" and "Text Left" to speed up design.

# Schema - raw
{"schema":{"type":"object","definitions":{"icon":{"type":"object","oneOf":[{"required":["path"]},{"required":["library","name"]}],"default":{"color":{"enabled":"","disabled":""},"path":"","style":{}},"properties":{"color":{"type":"object","properties":{"enabled":{"format":"color","description":"Color of the icon when enabled. Can be a named color.","type":"string","default":""},"disabled":{"format":"color","description":"Color of the icon when disabled. Can be a named color.","type":"string","default":""}}},"path":{"description":"Shorthand path to icon source, in format: library/iconName","type":"string","default":""},"library":{"description":"Optional alternative to 'path', name of library where icon is located. Must also supply 'name'.","type":"string"},"name":{"description":"Optional alternative to 'path', name of icon. Must also supply 'library'.","type":"string"},"style":{"default":{},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}},"properties":{"indeterminateIcon":{"description":"Icon to show when in indeterminate or tristate.","default":{"color":{"enabled":"","disabled":""},"path":"material/indeterminate_check_box","style":{}},"$ref":"#/definitions/icon"},"textPosition":{"description":"Where to place label text in relation to checkbox","type":"string","enum":["top","right","bottom","left"],"default":"right"},"triState":{"description":"Whether checkbox supports a third state of 'indeterminate' - effectively 'null' or 'no choice'","type":"boolean","default":false},"uncheckedIcon":{"description":"Icon to show when unchecked.","default":{"color":{"enabled":"","disabled":""},"path":"material/check_box_outline_blank","style":{}},"$ref":"#/definitions/icon"},"enabled":{"description":"Whether user can currently interact with the checkbox","type":"boolean","default":true},"checkedIcon":{"description":"Icon to show when checked.","default":{"color":{"enabled":"","disabled":""},"path":"material/check_box","style":{}},"$ref":"#/definitions/icon"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Label for checkbox","type":"string","default":"text"},"selected":{"description":"Output value for checkbox","type":["boolean","null"],"default":false}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Checkbox","name":"Checkbox","palette":{"variants":[{"tooltip":"Simple component that represents a bit that is either on (checked), off (not checked), or indeterminate.","label":"Checkbox"},{"tooltip":"Simple component that represents a bit that is either on (checked), off (not checked), or indeterminate.","label":"Text Right","id":"checkbox-right"},{"tooltip":"Simple component that represents a bit that is either on (checked), off (not checked), or indeterminate.","label":"Text Left","props":{"textPosition":"left"},"id":"checkbox-left"}],"category":"input"},"id":"ia.input.checkbox","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}