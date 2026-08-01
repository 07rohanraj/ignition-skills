# Perspective Motor Symbol Component

## Description

This document describes the properties and configuration of the Perspective Motor Symbol component. It explains how to customize the motor's visual appearance, orientation, and animation to represent its operational state. The instructions also cover how to display associated information using configurable labels for static identifiers and dynamic values for real-time process data.

## Documentation

# Instructions
# Perspective Motor Symbol Component

## Object Description
The Perspective Motor Symbol is an animated graphical component used to represent a motor in an industrial process visualization. It provides various options to display the motor's state, orientation, and associated data like a label and a dynamic value. Its appearance can be customized from a realistic "mimic" style to a simpler "P&ID" (Piping and Instrumentation Diagram) look.

## Properties

### `appearance`
*   **Description**: Controls the overall visual style of the motor. The 'auto' option will inherit the style from the Session Property `symbols.appearance`; otherwise, it defaults to 'mimic'.
*   **Type**: `string`
*   **Accepted Values**: `auto`, `p&id`, `mimic`, `simple`
*   **Default Value**: `auto`

### `animationSpeed`
*   **Description**: Determines the speed of the motor's animation, expressed as a percentage. A value of 0 will disable the animation entirely. The 'auto' option will inherit the speed from the Session Property `symbols.autoAnimationSpeed`.
*   **Type**: `string` or `number`
*   **Default Value**: `auto`

### `state`
*   **Description**: Represents the operational state of the motor, which typically affects its color and animation. There are built-in states, but custom states can be configured in the Project Properties under the Symbols section.
*   **Type**: `string`
*   **Accepted Values**: `default`, `running`, `stopped`, `faulted` (and any custom-defined states).
*   **Default Value**: `default`

### `orientation`
*   **Description**: Sets the physical orientation of the motor component in the view.
*   **Type**: `string`
*   **Accepted Values**: `top`, `bottom`, `left`, `right`
*   **Default Value**: `right`

### `feet`
*   **Description**: Controls the visibility and position of the motor's mounting feet. This property is only visible and applicable when the `appearance` is set to `mimic`, `simple`, or `auto`.
*   **Type**: `string`
*   **Accepted Values**: `top`, `bottom`, `left`, `right`, `none`
*   **Default Value**: `bottom`

### `label`
*   **Description**: An object for configuring a text label associated with the motor.
*   **Type**: `object`
*   **Properties**:
    *   `text`: The actual text to display for the label (e.g., "Motor 15").
        *   **Type**: `string`, `number`, `boolean`, `null`, `object`, `array`
        *   **Default Value**: "Motor"
    *   `location`: The position of the label relative to the motor graphic.
        *   **Type**: `string`
        *   **Accepted Values**: `top`, `bottom`, `left`, `right`, `hidden`
        *   **Default Value**: `bottom`
    *   `justify`: The horizontal alignment of the label text.
        *   **Type**: `string`
        *   **Accepted Values**: `left`, `center`, `right`, `auto`
        *   **Default Value**: `center`
    *   `style`: An object for applying CSS styles to the label's text, background, border, etc.

### `value`
*   **Description**: An object for configuring a dynamic value display associated with the motor. This is often used to show real-time data like speed, temperature, or load.
*   **Type**: `object`
*   **Properties**:
    *   `text`: The value to be displayed as text (e.g., "100%").
        *   **Type**: `string`, `number`, `boolean`, `null`, `object`, `array`
        *   **Default Value**: "100%"
    *   `location`: The position of the value text relative to the motor graphic.
        *   **Type**: `string`
        *   **Accepted Values**: `top`, `bottom`, `left`, `right`, `hidden`
        *   **Default Value**: `bottom`
    *   `justify`: The horizontal alignment of the value text.
        *   **Type**: `string`
        *   **Accepted Values**: `left`, `center`, `right`
        *   **Default Value**: `center`
    *   `style`: An object for applying CSS styles to the value's text, background, border, etc.

### `style`
*   **Description**: An object that sets the overall style for the motor component, including properties like fill color. Styles can be applied directly or by referencing a Style Class. Note that the component has two pre-configured variants.
*   **Type**: `object`

---

## Helpful Tips
*   **State-Driven Animation and Color**: The `state` property is the most common way to dynamically change the motor's appearance. By binding this property to a PLC tag or expression, you can make the motor appear to be `running` (green, animated), `stopped` (gray, static), or `faulted` (red, static).
*   **Custom States**: Don't forget that you can define your own states beyond the defaults. Navigate to `Project Properties > Symbols` to create new states with custom colors and animation settings. This is useful for representing conditions like 'Overload' or 'Maintenance Required'.
*   **Dynamic Data Display**: Use the `label` for static identification (e.g., the motor's name or asset ID) and bind the `value.text` property to a tag to show dynamic information like RPM, current draw, or temperature.
*   **Controlling Animation**: The `animationSpeed` property can be bound to a tag. Setting it to "0" is a great way to stop the animation to indicate a 'stopped' condition without changing the motor's color via the `state` property.
*   **Bindings are Key**: Most properties on the Motor component are bindable. Use property bindings to link its appearance, state, and displayed values to your underlying process data for a fully dynamic visualization.
*   **Styling Granularity**: You have three levels of style control:
    1.  The main `style` property affects the entire component.
    2.  The `label.style` property targets only the label text.
    3.  The `value.style` property targets only the value text.
    Use Style Classes for consistent styling across multiple motors.
*   **Component Events**: The Motor component can trigger actions. Right-click the component and select "Configure Events" to set up actions like navigating to a different view or opening a popup on a `click` event. This is useful for creating a details popup for the specific motor.
*   **Appearance Toggles**: The `appearance` property allows you to switch between a detailed `mimic` graphic and a simpler `p&id` or `simple` symbol, which can be useful for creating different levels of detail in your HMI screens.

# Schema - raw
{"schema":{"type":"object","properties":{"feet":{"visibleWhen":{"equals":["mimic","simple","auto"],"property":"appearance"},"type":"string","enum":["top","bottom","left","right","none"],"default":"bottom"},"orientation":{"type":"string","enum":["top","bottom","left","right"],"default":"right"},"label":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right","auto"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Label to display as text","type":["string","number","boolean","null","object","array"],"example":"Motor","default":"Motor"}}},"animationSpeed":{"description":"The speed of animations as a percent. 0 turns off animations.","type":["string","number"],"default":"auto"},"appearance":{"description":"auto uses the value of the Session Prop symbols.appearance if it exists, default is mimic.","type":"string","enum":["auto","p&id","mimic","simple"],"default":"auto"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"state":{"format":"symbol-states","type":"string","default":"default"},"value":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Value to display as text","type":["string","number","boolean","null","object","array"],"example":"100%","default":"100%"}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Motor","name":"Motor","palette":{"variants":[{"tooltip":"An animated component that looks like a motor.","label":"Motor"}],"category":"symbols"},"id":"ia.symbol.motor"}