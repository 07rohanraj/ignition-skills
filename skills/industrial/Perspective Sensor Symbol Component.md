# Perspective Sensor Symbol Component

## Description

The usage and configuration of the Perspective Sensor Symbol component, detailing the properties for customizing its visual appearance, animation, orientation, and dynamic state. These instructions cover how to manage the display and styling of the component's label and value text to create an informative industrial symbol.

## Documentation

# Instructions
Here are the instructions for the **Perspective Sensor Symbol Component**:

### Instruction
This document provides instructions for using the Perspective Sensor Symbol component in Ignition.

**High-Level Description**

The Sensor Symbol is an animated component that visually represents a sensor, commonly used in industrial HMIs and SCADA dashboards. It is highly customizable, allowing for different appearances, states, and orientations. It can display a label and a value, each with its own positioning and styling options.

**Component Properties**

Here is a detailed breakdown of the component's properties, which are found in the "Props" section of the Ignition Designer's Property Editor.

| Property | Description | Type | Default Value | Allowed Values/Notes |
| :--- | :--- | :--- | :--- | :--- |
| **appearance** | Controls the visual style of the component. If set to 'auto', the appearance is determined by the session property `symbols.appearance`. | String | "auto" | "auto", "p&id", "mimic", "simple" |
| **animationSpeed** | Sets the speed of the animation as a percentage. A value of 0 disables the animation. If set to 'auto', the speed is determined by the session property `symbols.autoAnimationSpeed`. | String or Number | "auto" | A numeric value (e.g., 100 for 100%) or "auto". |
| **state** | Represents the current state of the sensor, which affects its animation and appearance. New states can be defined in the Project Properties > Symbols section of the Ignition Designer. | String | "default" | Built-in states: "default", "running", "stopped", "faulted". Also accepts custom-defined states. |
| **orientation** | Determines the direction the sensor is facing. The schema and documentation have conflicting default values; the schema's default is "bottom". | String | "bottom" | "top", "bottom", "left", "right" |
| **label** | An object containing properties for the sensor's label. | Object | - | This object has its own set of properties detailed below. |
| **label.text** | The text to be displayed for the label. | String, Number, etc. | "Sensor" | Can be bound to any data type. |
| **label.location** | The position of the label relative to the sensor symbol. | String | "inside" | "top", "bottom", "left", "right", "inside", "hidden" |
| **label.justify** | The horizontal alignment of the label's text. This property is only visible and applicable when `label.location` is set to "top", "bottom", "left", or "right". | String | "center" | "left", "center", "right", "auto" |
| **label.style** | A style object that allows for detailed styling of the label's text, background, border, etc. | Object | - | See the Style Properties documentation for all available options. |
| **value** | An object containing properties for the sensor's value display. | Object | - | This object has its own set of properties detailed below. |
| **value.text** | The text to be displayed for the value. Typically bound to a sensor's process value. | String, Number, etc. | "100%" | Can be bound to any data type. |
| **value.location** | The position of the value text relative to the sensor symbol. | String | "inside" | "top", "bottom", "left", "right", "inside", "hidden" |
| **value.justify** | The horizontal alignment of the value's text. This property is only visible and applicable when `value.location` is set to "top", "bottom", "left", or "right". | String | "center" | "left", "center", "right" |
| **value.style** | A style object that allows for detailed styling of the value's text, background, border, etc. | Object | - | See the Style Properties documentation for all available options. |
| **style** | A style object for the main sensor component itself. The documentation for this property incorrectly refers to the component as a "cylindrical tank", but it applies to the sensor. | Object | - | See the Style Properties documentation for all available options. |

**Component Events**

User interactions, such as mouse clicks or property changes, are handled through Component Events. These are configured separately from the properties in the Ignition Designer and are not detailed in the properties list above.

### helpful_tips
Here is a list of helpful tips for working with the Sensor Symbol component.

*   **Dynamic States:** The `state` property is one of the most powerful features. You can bind it to a tag's value or quality to automatically change the sensor's appearance (e.g., from "running" to "faulted"). Remember that you can create your own custom states in `Project Properties > Symbols` to match the specific states of your process.
*   **Global Appearance Control:** Use the `appearance` and `animationSpeed` properties set to their default of "auto" if you want to control the look and feel of all symbols in your project consistently from the Session Properties.
*   **Independent Labels and Values:** The `label` and `value` are two separate objects. This means you can position them independently. For example, you can place the `label` on top of the sensor and the `value` on the bottom. You can also hide one by setting its `location` to "hidden".
*   **Conditional Justification:** The `justify` property for both `label` and `value` only has an effect when the `location` is set to one of the outside positions (`top`, `bottom`, `left`, `right`). When the location is `inside`, the text is always centered.
*   **Styling Everything:** You have three distinct places to apply styles: the main component body (`style`), the label (`label.style`), and the value (`value.style`). This allows for granular control over the component's appearance.
*   **Bindings are Essential:** For the component to be useful, you will almost always bind the `value.text` property to a PLC tag or other data source. Similarly, binding the `state` property makes the component dynamic.
*   **Turn off Animation:** If you don't need the animation, set the `animationSpeed` property to `0`. This can improve performance in views with a very large number of symbols.
*   **Interactivity:** To make the sensor interactive (e.g., open a popup on click), use the Component Events configuration panel in the Designer. You would add an `onClick` event and configure an action, such as a Navigation or Script action.

# Schema - raw
{"schema":{"type":"object","properties":{"orientation":{"type":"string","enum":["top","bottom","left","right"],"default":"bottom"},"label":{"type":"object","properties":{"justify":{"visibleWhen":{"equals":["top","bottom","left","right"],"property":"location"},"description":"Horizontal text alignment.","type":"string","enum":["left","center","right","auto"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","inside","hidden"],"default":"inside"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Label to display as text","type":["string","number","boolean","null","object","array"],"example":"Sensor","default":"Sensor"}}},"animationSpeed":{"description":"The speed of animations as a percent. 0 turns off animations.","type":["string","number"],"default":"auto"},"appearance":{"description":"auto uses the value of the Session Prop symbols.appearance if it exists, default is mimic.","type":"string","enum":["auto","p&id","mimic","simple"],"default":"auto"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"state":{"format":"symbol-states","type":"string","default":"default"},"value":{"type":"object","properties":{"justify":{"visibleWhen":{"equals":["top","bottom","left","right"],"property":"location"},"description":"Horizontal text alignment.","type":"string","enum":["left","center","right"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","inside","hidden"],"default":"inside"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Value to display as text","type":["string","number","boolean","null","object","array"],"example":"100%","default":"100%"}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Sensor","name":"Sensor","palette":{"variants":[{"tooltip":"A component that looks like a sensor.","label":"Sensor"}],"category":"symbols"},"id":"ia.symbol.sensor"}