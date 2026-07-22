# Perspective Multi-State Button Component

## Description

This describes the configuration and usage of the Perspective Multi-State Button, a component for representing and controlling a numeric state through a series of buttons. The instructions explain how to define each button's state, appearance, and value using the `states` property, and detail the critical binding between the `indicatorValue` and `controlValue` properties to achieve interactive control.

## Documentation

# Instructions
Here are the instructions for the LLM on how to use the Perspective Multi-State Button Component in Ignition.

### Object Name
Perspective Multi-State Button

### Instructions for LLM
The Perspective Multi-State Button is a component that displays a series of two or more buttons, arranged either in a row or a column. Each button corresponds to a specific numeric state. When a user clicks a button, the component's value changes to that button's assigned state value. This is commonly used to control or represent the state of a piece of equipment, such as "Off", "On", "Auto", or "Manual".

#### Core Concepts
*   **Control vs. Indicator:** The component has two key properties for managing its state: `controlValue` and `indicatorValue`.
    *   `indicatorValue`: This property determines which button *appears* selected. Its value is compared against the `value` property of each state in the `states` array.
    *   `controlValue`: When a user clicks a button, that button's state `value` is written to this property.
    *   In most use cases, `controlValue` and `indicatorValue` should be bound together (often to the same Tag), creating a seamless link between the visual state and the underlying control value.

*   **States Array (`states`):** This is the most critical property. It is an array of objects, where each object defines a single button within the component.
    *   Each object in the array must have a unique `value` (number) and `text` (string).
    *   Each state object also has `selectedStyle` and `unselectedStyle` properties to define its appearance based on whether it is the active state or not.

#### Key Properties
*   **`states`**: An array of objects defining the buttons. To configure the component, you must edit this array.
    *   **`text`**: The text displayed on the button.
    *   **`value`**: The numeric value associated with this state. This value must be unique among all states.
    *   **`selectedStyle`**: A style object defining the appearance of the button when the `indicatorValue` matches this state's `value`. You can set properties like `backgroundColor`, `color`, `border`, etc.
    *   **`unselectedStyle`**: A style object defining the appearance of the button when it is not the selected state.
    *   **`tooltipText`**: An optional string that appears in a tooltip when a user hovers over the button. This property must be added manually to the state object if desired.
*   **`indicatorValue`**: A numeric property that controls which state is visually selected. Bind this to the Tag or property that represents the current state.
*   **`controlValue`**: A numeric property that gets updated when a user clicks a button. Bind this to the Tag you wish to write the new state to.
*   **`orientation`**: Determines the layout of the buttons. Can be set to `"row"` (horizontal) or `"column"` (vertical).
*   **`buttonGap`**: The amount of space, in pixels, between each button.
*   **`endButtonCornerRadius`**: Defines the corner radius for the first and last buttons in the series, allowing you to create a "pill" or "rounded tab" effect.
*   **`defaultSelectedStyle` / `defaultUnselectedStyle`**: These are fallback style objects. If a specific state does not have its own `selectedStyle` or `unselectedStyle` defined, these default styles will be used instead.
*   **`enabled`**: A boolean that, when `false`, prevents users from interacting with the buttons.
*   **`primary`**: A boolean toggle that switches between the default primary and secondary button styles of the theme.

#### Events
*   **`onActionPerformed`**: This event is fired whenever a user clicks any of the buttons in the component. You can configure actions, such as running a script, to respond to this event.

### Helpful Tips
*   **Critical Binding:** For the component to function as an interactive control, you **must** bind the `controlValue` and `indicatorValue` properties. Typically, they are both bound to the same Tag or session property, often with a bidirectional binding to allow both reading the current state and writing a new one.
*   **Unique State Values:** The `value` property for each object inside the `states` array must be a unique number. The component will not function correctly if there are duplicate values.
*   **Button Order:** The visual order of the buttons in the component is determined by the order of the state objects in the `states` array. The first object in the array will be the first button, and so on.
*   **Styling Hierarchy:** Styles defined directly on a state (e.g., `states[0].selectedStyle`) will always override the component-level default styles (`defaultSelectedStyle`).
*   **Adding Tooltips:** The `tooltipText` property does not exist on state objects by default. To add a tooltip to a specific button, you must manually add the `tooltipText` key to that state's object within the `states` array.
*   **Minimum States:** The Multi-State Button requires a minimum of two states to be configured.

# Schema - raw
{"schema":{"type":"object","properties":{"orientation":{"type":"string","enum":["column","row"],"default":"column"},"defaultUnselectedStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"controlValue":{"example":0},"enabled":{"description":"Whether user is able to currently interact with buttons","type":"boolean","default":true},"states":{"type":"array","example":[{"unselectedStyle":{"classes":""},"text":"Hand","value":2,"selectedStyle":{"backgroundColor":"#FFF275","classes":""}},{"unselectedStyle":{"classes":""},"text":"Off","value":0,"selectedStyle":{"backgroundColor":"#F84553","classes":""}},{"unselectedStyle":{"classes":""},"text":"Auto","value":1,"selectedStyle":{"backgroundColor":"#7CEA9C","classes":""}}],"minItems":2,"uniqueItems":true,"items":{"type":"object","required":["text","value","selectedStyle","unselectedStyle"],"additionalProperties":false,"properties":{"unselectedStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"tooltipText":{"description":"Mousing over this button will show a tooltip with this text, if present","type":"string"},"text":{"type":"string","default":""},"value":{"type":"number","default":""},"selectedStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}},"buttonGap":{"description":"Space (pixels) between each button in group","type":"number","default":4},"endButtonCornerRadius":{"description":"Amount to round the end corners of the first and last button","type":["number","string"],"default":""},"defaultSelectedStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"indicatorValue":{"example":0},"primary":{"description":"Toggle between the default primary and secondary button style.","type":"boolean","default":false}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"MultiStateButton","name":"Multi-State Button","palette":{"variants":[{"tooltip":"A column or row of buttons that acts as a multi-state control button.","label":"Multi-State Button"},{"tooltip":"A column or row of buttons that acts as a multi-state control button.","label":"Column","id":"multi-state-button-vertical"},{"tooltip":"A column or row of buttons that acts as a multi-state control button.","label":"Row","props":{"orientation":"row"},"id":"multi-state-button-horizontal"}],"category":"input"},"id":"ia.input.multi-state-button","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}