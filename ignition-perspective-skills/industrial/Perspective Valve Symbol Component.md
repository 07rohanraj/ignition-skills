# Perspective Valve Symbol Component

## Description

This document describes the properties and configuration options for the Perspective Valve Symbol component. It explains how to customize the valve's visual appearance, orientation, and dynamic states, as well as how to control animations and display associated labels and process values to accurately represent industrial equipment.

## Documentation

# Instructions
# Perspective Valve Symbol Component

## About the Perspective Valve Component
The Valve Symbol is a Perspective component used to visually represent a valve in an industrial process. It provides various appearances, states, and orientations to accurately reflect the real-world equipment. It can display a label and a value, and includes animations for state transitions and flow.

## Properties

### `appearance`
- **Description**: Determines the overall visual style of the valve. The `auto` setting allows for a centralized control over the appearance of all symbols in a session.
- **Type**: `String`
- **Accepted Values**: `auto`, `p&id`, `mimic`, `simple`
- **Default Value**: `auto`
- **Notes**: When set to `auto`, the component will use the `symbols.appearance` property from the Session Properties.

### `animationSpeed`
- **Description**: Controls the speed of the valve's animations, specified as a percentage. Setting this to 0 will disable animations entirely. The `auto` setting allows for a centralized control over the animation speed of all symbols in a session.
- **Type**: `String` or `Number`
- **Default Value**: `auto`
- **Notes**: When set to `auto`, the component will use the `symbols.autoAnimationSpeed` property from the Session Properties.

### `state`
- **Description**: Represents the current state of the valve, which typically affects its color and animation. In addition to the built-in states, custom states can be defined.
- **Type**: `String`
- **Accepted Values**: The built-in states are `default`, `open`, `failedToOpen`, `partiallyClosed`, `closed`, and `failedToClose`.
- **Default Value**: `default`
- **Notes**: Custom states can be configured globally for the project under the Project Properties > Symbols page. This property is commonly bound to a tag representing the valve's status.

### `valve`
- **Description**: Controls the orientation of the valve's actuator/handle.
- **Type**: `String`
- **Accepted Values**: `top`, `bottom`, `left`, `right`
- **Default Value**: `top`

### `reverseFlow`
- **Description**: Reverses the direction of the flow animation within the valve body.
- **Type**: `Boolean`
- **Accepted Values**: `true`, `false`
- **Default Value**: `false`

### `label`
- **Description**: An object containing properties for the text label associated with the valve. This is typically used for a static identifier.
- **Type**: `Object`
- **Properties**:
    - **`text`** (`String`): The text to display for the label (e.g., "HV-101").
    - **`location`** (`String`): The position of the label relative to the valve. Can be `top`, `bottom`, `left`, `right`, or `hidden`. Default is `bottom`.
    - **`justify`** (`String`): The horizontal alignment of the label text. Can be `left`, `center`, `right`, or `auto`. Default is `center`.
    - **`style`** (`Object`): Style object for the label's text, allowing for customization of font, color, etc.

### `value`
- **Description**: An object containing properties for the value text associated with the valve. This is typically used to display dynamic process data.
- **Type**: `Object`
- **Properties**:
    - **`text`** (`String` | `Number`): The value to display as text (e.g., a flow rate or percentage).
    - **`location`** (`String`): The position of the value text relative to the valve. Can be `top`, `bottom`, `left`, or `right`. Default is `bottom`.
    - **`justify`** (`String`): The horizontal alignment of the value text. Can be `left`, `center`, or `right`. Default is `center`.
    - **`style`** (`Object`): Style object for the value's text, allowing for customization of font, color, etc.

### `style`
- **Description**: The styling properties for the main component container. This can be used to apply styles like borders, background colors, and margins to the entire valve component.
- **Type**: `Object`

---

## Configuration Tips
- **Dynamic Control via State**: The `state` property is the most important property for dynamic control. Bind the `state` property to a tag representing the equipment's status to automatically update the valve's appearance (e.g., color) based on its real-world state.
- **Custom States**: You are not limited to the default states. You can define new states (e.g., "maintenance", "standby") in the `Project Properties > Symbols` section. These custom states can then be used in the `state` property of the component.
- **Displaying Process Data**: Use the `value.text` property to display dynamic data from a PLC or other source. Bind this property to a relevant tag, such as flow rate, pressure, or valve position.
- **Static Identifiers**: Use the `label.text` property for static identifiers, such as the valve's equipment name (e.g., "V-102").
- **Hiding Labels/Values**: If you don't need a label or a value display, set the corresponding `location` property to `hidden`.
- **Consistent Project Appearance**: For a consistent look and feel across your project, set the `appearance` and `animationSpeed` properties to `auto`. Then, configure the desired appearance and speed in the Session Properties (`symbols.appearance` and `symbols.autoAnimationSpeed`). This allows you to change the style of all symbols in your application from a single location.
- **Styling Granularity**: Understand the difference between the three style properties:
    - `style`: Applies to the entire component's container.
    - `label.style`: Applies *only* to the label's text.
    - `value.style`: Applies *only* to the value's text.
- **Flow Animation**: The `state` property can trigger flow animations (e.g., in the 'open' state). Use the `reverseFlow` property if the default animation direction does not match your process flow diagram.
- **Bindings**: Almost all properties can be bound. Use property bindings to make the component dynamic and responsive to your system's state. For more information, refer to the documentation on "Bindings in Perspective".

# Schema - raw
{"schema":{"type":"object","properties":{"label":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right","auto"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Label to display as text","type":["string","number","boolean","null","object","array"],"example":"Valve","default":"Valve"}}},"animationSpeed":{"description":"The speed of animations as a percent. 0 turns off animations.","type":["string","number"],"default":"auto"},"appearance":{"description":"auto uses the value of the Session Prop symbols.appearance if it exists, default is mimic.","type":"string","enum":["auto","p&id","mimic","simple"],"default":"auto"},"reverseFlow":{"type":"boolean","default":false},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"state":{"format":"symbol-states","type":"string","default":"default"},"valve":{"type":"string","enum":["top","bottom","left","right"],"default":"top"},"value":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Value to display as text","type":["string","number","boolean","null","object","array"],"example":"100%","default":"100%"}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Valve","name":"Valve","palette":{"variants":[{"tooltip":"A component that looks like a valve.","label":"Valve"}],"category":"symbols"},"id":"ia.symbol.valve"}