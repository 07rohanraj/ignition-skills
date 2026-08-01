# Perspective Pump Symbol Component

## Description

These instructions detail the configuration of the Perspective Pump Symbol component's properties, enabling users to customize its visual appearance, control its animation and operational state, and display associated labels and process values.

## Documentation

# Instructions
This document provides instructions for using the Perspective Pump Symbol component in Ignition.

### Object Overview

The Perspective Pump Symbol is an animated graphical component used to represent a pump, such as those found in industrial processes. It is visually configurable and can be bound to process values to display the state and operating parameters of a real-world pump. It has several built-in appearance styles, variants, and states to accurately depict the equipment it represents.

### Property Instructions

Here is a detailed breakdown of the component's properties:

**Core Appearance & Type**

*   **`variant`**: Determines the type of pump to display.
    *   `centrifugal` (Default): Shows a standard centrifugal pump.
    *   `vacuum`: Shows a vacuum pump.
*   **`appearance`**: Sets the visual style of the pump.
    *   `auto` (Default): The component's appearance is determined by the session property `symbols.appearance`. If that property doesn't exist, the default is `mimic`.
    *   `p&id`: A simplified style, suitable for Piping and Instrumentation Diagrams.
    *   `mimic`: A more detailed and colorful representation.
    *   `simple`: A less detailed, "flat" style.
*   **`orientation`**: Controls the direction the pump's output is facing.
    *   Values: `top`, `bottom`, `left`, `right` (Default).
*   **`feet`**: Sets the position of the pump's mounting feet. This property is only visible when the `appearance` is set to `mimic`, `simple`, or `auto`.
    *   Values: `top`, `bottom` (Default), `left`, `right`, `none`.

**State & Animation**

*   **`state`**: Represents the operational state of the pump, which can affect its visual appearance (e.g., color).
    *   `default` (Default): The default state.
    *   Built-in states include `running`, `stopped`, and `faulted`.
    *   Custom states can be configured in the project properties (`Project Properties > Symbols`) and then assigned to this property.
*   **`animationSpeed`**: Controls the speed of the pump's animation as a percentage.
    *   A value of `"0"` will disable the animation entirely.
    *   `auto` (Default): The animation speed is determined by the session property `animationSpeed`.

**Text & Value Displays**

The pump component has two areas for displaying text, `label` and `value`, each with identical configuration properties.

*   **`label`**: An object for configuring the pump's descriptive label.
    *   `text`: The text to display (e.g., "Pump-101"). Defaults to "Pump".
    *   `location`: The position of the label relative to the pump. Can be `top`, `bottom` (Default), `left`, `right`, or `hidden`.
    *   `justify`: The horizontal alignment of the text. Can be `left`, `center` (Default), `right`, or `auto`.
    *   `style`: A standard style object for applying custom styles (color, font, etc.) specifically to the label text.
*   **`value`**: An object for configuring a text display for a process value.
    *   `text`: The text to display (e.g., a speed or flow rate). Defaults to "100%".
    *   `location`: The position of the value text relative to the pump. Can be `top`, `bottom` (Default), `left`, `right`, or `hidden`.
    *   `justify`: The horizontal alignment of the text. Can be `left`, `center` (Default), or `right`.
    *   `style`: A standard style object for applying custom styles specifically to the value text.

**General Styling**

*   **`style`**: A standard style object that applies to the entire pump component. This can be used to set background colors, borders, margins, etc.

### Helpful Tips

*   To create a dynamic symbol, bind the `state` property to a tag representing the pump's status. You can also bind the `label.text` and `value.text` properties to relevant tags for identification and process values.
*   The `animationSpeed` can be bound to a tag representing motor speed to make the animation reflect the actual operational speed. Set it to `"0"` via a binding when the pump is off.
*   Use the `auto` setting for `appearance` and `animationSpeed` to maintain a consistent look and feel across all symbols in a project by controlling them from the session properties.
*   If you don't want to show a `label` or `value`, set its `location` property to `hidden`.
*   The `feet` property is not available when `appearance` is set to `p&id`. If you need to show feet, use the `mimic` or `simple` appearance.
*   For more complex state representations beyond the defaults (e.g., 'cleaning', 'overloaded'), define new states in `Project Properties > Symbols` and apply them to the `state` property.
*   You can apply styles at multiple levels. Use the main `style` property for the component's container (e.g., border, background). Use the `label.style` and `value.style` properties for specific text styling.

# Schema - raw
{"schema":{"type":"object","properties":{"feet":{"visibleWhen":{"equals":["mimic","simple","auto"],"property":"appearance"},"type":"string","enum":["top","bottom","left","right","none"],"default":"bottom"},"orientation":{"type":"string","enum":["top","bottom","left","right"],"default":"right"},"label":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right","auto"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Label to display as text","type":["string","number","boolean","null","object","array"],"example":"Pump","default":"Pump"}}},"animationSpeed":{"description":"The speed of animations as a percent. 0 turns off animations.","type":["string","number"],"default":"auto"},"appearance":{"description":"auto uses the value of the Session Prop symbols.appearance if it exists, default is mimic.","type":"string","enum":["auto","p&id","mimic","simple"],"default":"auto"},"variant":{"type":"string","enum":["centrifugal","vacuum"],"default":"centrifugal"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"state":{"format":"symbol-states","type":"string","default":"default"},"value":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Value to display as text","type":["string","number","boolean","null","object","array"],"example":"100%","default":"100%"}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Pump","name":"Pump","palette":{"variants":[{"tooltip":"An animated component that looks like a pump.","label":"Pump"},{"tooltip":"Devices that utilize pressure to transfer fluids from one location to another.","label":"Centrifugal","id":"pump-centrifugal"},{"tooltip":"Devices that utilize pressure to transfer fluids from one location to another.","label":"Vacuum","props":{"variant":"vacuum"},"id":"pump-vacuum"}],"category":"symbols"},"id":"ia.symbol.pump"}