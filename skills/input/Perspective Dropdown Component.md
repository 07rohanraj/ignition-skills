# Perspective Dropdown Component

## Description

These instructions detail the usage and configuration of the Ignition Perspective Dropdown component, explaining how to define the list of selectable options and handle both single and multiple selections. The document also covers implementing features such as search functionality, placeholder text, custom user-created entries, and styling for the component and its dropdown menu.

## Documentation

# Instructions
This document provides instructions for using the **Perspective Dropdown Component** in Ignition.

### Instructions

The Perspective Dropdown component allows you to display a list of choices in a compact space. The user can click on the component to reveal a list of options and make a selection.

#### Basic Configuration

1.  **`options` Property:** This is the most important property. It defines the list of items that will appear in the dropdown.
    *   It is an array of objects.
    *   Each object in the array represents a single option in the dropdown list.
    *   At a minimum, each object **must** have a `value` and a `label` key.
        *   `label`: The text that is displayed to the user for that option (e.g., "Valve 1"). The label can be a string or a number.
        *   `value`: The actual value that the component will hold when that option is selected (e.g., "[default]Dairy/Bldg25/valve1"). The value can be a string, number, boolean, array, or object. **Each option must have a unique value.**
    *   Each option object can also have an `isDisabled` boolean key. If set to `true`, that specific option will be visible but not selectable.

    **Example `options` structure:**
    ```json
    [
      {
        "label": "Valve 1",
        "value": "[default]Dairy/Bldg25/valve1"
      },
      {
        "label": "Valve 2",
        "value": "[default]Dairy/Bldg25/valve2"
      },
      {
        "label": "Valve 3",
        "value": "[default]Dairy/Bldg25/valve3",
        "isDisabled": true
      }
    ]
    ```

2.  **`value` Property:** This property stores the result of the user's selection. Its data type will match the data type of the `value` field from the selected `options` object. When no selection has been made, its value is typically `null` or `""` (empty string).

#### Key Features

*   **Multiple Selections:**
    *   To allow users to select more than one option, set the `multiSelect` property to `true`.
    *   When `multiSelect` is `true`, the `value` property will become an array containing the values of all selected options.
    *   The `wrapMultiSelectValues` property (default `true`) controls whether selected items wrap to a new line or are displayed on a single line.

*   **Search Functionality:**
    *   The `search` property is an object that controls the search behavior within the dropdown.
    *   `search.enabled`: Set to `true` (the default) to allow users to type into the field to filter the options.
    *   `search.matching`: Determines how the search works.
        *   `any` (default): The search term can appear anywhere in the option's label.
        *   `start`: The option's label must begin with the search term.
    *   `search.noResultsText`: The text to display if the user's search term matches no options (e.g., "No results found").
    *   `search.searchParam`: This property holds the text the user is currently searching for.

*   **Placeholder Text:**
    *   The `placeholder` property is an object that defines the content shown when the component's `value` is empty.
    *   `placeholder.text`: The text to display (e.g., "Select an Option...").
    *   `placeholder.color`: Sets the color of the placeholder text.
    *   `placeholder.icon`: An object to configure an icon to appear with the placeholder text, with properties for `path`, `color`, and `style`.

*   **Custom Options:**
    *   Set the `allowCustomOptions` property to `true` to let a user type a value that is not in the `options` list.
    *   When a user types a custom value, a "Create" option will appear in the dropdown. Selecting it sets the component's `value` property to this new custom text.
    *   **Note:** Creating a custom option **does not** add the new option to the `options` property. It only affects the current `value`.

*   **Disabling the Component:**
    *   Set the `enabled` property to `false` to disable the entire component. It will not be interactive.

#### Appearance and Styling

*   **Component Style (`style`):** This object controls the appearance of the main dropdown field itself (the box the user clicks on). You can set font, background color, borders, etc.
*   **Dropdown Option Style (`dropdownOptionStyle`):** This object controls the appearance of the individual options *within the dropdown menu that appears*.
*   **Text Alignment (`textAlign`):** Aligns the text (the selected value or the placeholder) within the main dropdown field. Can be `left`, `center`, or `right`.
*   **Menu Height:**
    *   `minMenuHeight`: The minimum height of the dropdown menu.
    *   `maxMenuHeight`: The maximum height before the menu becomes scrollable.
*   **Clear Icon:**
    *   Set `showClearIcon` to `true` to display an 'x' icon that allows the user to clear the current selection.

#### Events

*   **`onActionPerformed`:** This is the primary event for the Dropdown. It fires when the "action" of the component occurs, which typically means when a selection is made.

### Helpful Tips

*   The `options` and `value` properties are the most fundamental to making the Dropdown component work. Ensure the `options` property is configured correctly.
*   The data type of the `value` property is directly determined by the data type of the `value` field in the selected option. If you select an option where `{ "label": "One", "value": 1 }`, the component's `value` will be the number `1`.
*   To create a dynamic list of options (e.g., from a database), use a binding on the `options` property. You can bind it to a query or an expression.
*   Remember the distinction between `style` and `dropdownOptionStyle`. `style` is for the box itself, while `dropdownOptionStyle` is for the items in the list that pops up.
*   If you allow `multiSelect`, your scripts and bindings connected to the `value` property must be able to handle an array instead of a single value.
*   The `allowCustomOptions` feature is useful for allowing free-text entry while still providing a list of common suggestions. Remember that it doesn't modify your source list in `props.options`.
*   The `enabled` property disables the entire component. The `isDisabled` property (inside an object within the `options` array) disables just a single choice, leaving others selectable.

# Schema - raw
{"schema":{"type":"object","required":["value","options","style"],"properties":{"minMenuHeight":{"description":"Minimum height of the dropdown menu.","type":"number","default":150},"textAlign":{"description":"Aligns the value(s) and/or placeholder text displayed within the dropdown","type":"string","enum":["left","center","right"],"default":"left"},"showClearIcon":{"description":"Whether to render a button allowing user to clear the selection","type":"boolean","default":false},"enabled":{"description":"If set to false, component is disabled. Field will not focus and dropdown is hidden","type":"boolean","default":true},"wrapMultiSelectValues":{"visibleWhen":{"equals":true,"property":"multiSelect"},"description":"Wrap values when true, display values on one line when false","type":"boolean","default":true},"maxMenuHeight":{"description":"Maximum height of the dropdown menu before it becomes scrollable.","type":"number","default":350},"search":{"type":"object","default":{"searchParam":"","noResultsText":"No results found","enabled":true,"matching":"any"},"properties":{"searchParam":{"description":"The text being searched for","type":"string","default":""},"noResultsText":{"description":"Text to display in dropdown when no options match search","type":"string","default":"No results found"},"enabled":{"description":"Whether options are searchable by typing text into the field","type":"boolean","default":true},"matching":{"description":"Whether search string must match from the start or may match any position of an option","type":"string","enum":["start","any"],"default":"any"}}},"dropdownOptionStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"options":{"description":"Configuration objects for each dropdown option. At minimum, 'value' and 'label' are required for each.","type":["array","dataset"],"default":[],"items":{"type":"object","required":["value","label"],"default":{"label":"","value":""},"additionalProperties":false,"properties":{"label":{"description":"Text to display in menu representing this option","type":["string","number"]},"isDisabled":{"description":"Whether this option is currently disabled from selection","type":"boolean","default":false},"value":{"description":"Actual value to be matched by input/selection","type":["string","number","boolean","array","object","null"]}}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"placeholder":{"type":"object","default":{"color":"","icon":{"color":"","path":"","style":{"width":"16px","height":"16px"}},"text":"Select..."},"properties":{"color":{"format":"color","description":"Color of placeholder text","type":"string","default":""},"icon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"text":{"description":"Prompt text to display when no options are selected","type":"string","default":"Select..."}}},"allowCustomOptions":{"description":"Whether user may enter a custom value to be submitted","type":"boolean","default":false},"value":{"description":"The result of current selections (input) after any processing","type":["string","number","boolean","array","object","null"],"default":""},"multiSelect":{"description":"Enable multiple selected values","type":"boolean","default":false}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Dropdown","name":"Dropdown","palette":{"variants":[{"tooltip":"Displays a list of choices when the user clicks on the dropdown button.","label":"Dropdown"},{"tooltip":"Displays a list of choices when the user clicks on the dropdown button.","label":"Single Selection","id":"dropdown-single"},{"tooltip":"Displays a list of choices when the user clicks on the dropdown button.","label":"Multi-Selection","props":{"multiSelect":true},"id":"dropdown-multi"}],"category":"input"},"id":"ia.input.dropdown","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}