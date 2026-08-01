# Perspective Vessel Symbol Component

## Description

These instructions detail the configuration and customization of the Perspective Vessel Symbol component. The guide covers how to set its fill level and orientation, style its visual appearance, control the visibility of parts like the agitator, and manage the display of data, animations, and states.

## Documentation

# Instructions
# Perspective Vessel Symbol Component

## Object Description
The Perspective Vessel Symbol is an animated graphical component that represents a tank or vessel, commonly used in industrial HMIs. It is designed to visually display the level of a substance within the vessel, along with other states and information. Its appearance is highly customizable, with options to show or hide various parts like an agitator and stand, control the liquid's color and opacity, and configure labels and value displays.

---

## Instructions for Use

### **1. Basic Configuration**
*   **Value and Capacity:** To display the fill level, set the `value.value` property to the current level of the liquid and the `value.capacity` property to the maximum capacity of the vessel. By default, `value.displayValueAsPercent` is true, so the component will show the value as a percentage.
*   **Orientation:** You can orient the vessel vertically or horizontally using the `orientation` property.
    *   If `orientation` is set to `"vertical"`, you can specify the shape of the vessel's bottom using the `bottom` property (`"flat"`, `"conical"`, or `"rounded"`).
*   **Labeling:** To label the vessel, set the `label.text` property. You can control its position relative to the vessel with `label.location` (`"top"`, `"bottom"`, `"left"`, `"right"`, or `"hidden"`) and its horizontal alignment with `label.justify`.

### **2. Appearance and Styling**
*   **Overall Look:** The `appearance` property changes the fundamental style of the vessel. Options are `"auto"`, `"p&id"`, `"mimic"`, and `"simple"`. `"auto"` will use the session's `symbols.appearance` property.
*   **Liquid Appearance:**
    *   Use `liquidColor` to set the color of the liquid inside the vessel.
    *   Use `liquidWarningColor` to set the color the liquid should display in a warning state.
    *   The `liquidOpacity` property controls the transparency of the liquid, accepting a value from 0 (completely transparent) to 1 (completely opaque).
*   **Component Visibility:**
    *   To show or hide the agitator inside the vessel, set the `displayAgitator` property (`true` or `false`).
    *   To show or hide the stand the vessel sits on, set the `displayStand` property. Note that the stand is only visible when the `appearance` is set to `"mimic"` or `"simple"`.
    *   To show or hide the liquid fill level graphic, set `displayFillLevel` to `true` or `false`.
*   **Styling:**
    *   Use the `style` property to apply custom styles to the main component.
    *   To style the label's text (e.g., font weight, color), modify the `label.style` object.
    *   To style the value display's text, modify the `value.style` object.

### **3. Animation and State**
*   **State:** The `state` property controls the visual state of the component. Built-in states are `"default"`, `"running"`, `"stopped"`, and `"faulted"`. This can affect the component's appearance based on style configurations.
*   **Animation Speed:** The `animationSpeed` property controls the speed of animations, such as the agitator. It is a percentage. Setting it to `0` disables animations. `"auto"` will use the session's `symbols.autoAnimationSpeed` property.

### **4. Value Display**
*   **Displaying the Value:** The numerical value inside the vessel is configured via the `value` object.
    *   `value.value`: The raw value to display.
    *   `value.displayValueAsPercent`: Set to `false` to show the raw `value.value` instead of a percentage.
    *   `value.location`: Position the value display relative to the vessel (`"top"`, `"bottom"`, `"left"`, `"right"`, or `"hidden"`).
    *   `value.justify`: Justify the text for the value (`"left"`, `"center"`, or `"right"`).

---

## Helpful Tips
*   To create a vertical vessel with a rounded bottom, set `orientation` to `"vertical"` and `bottom` to `"rounded"`.
*   If the vessel stand is not appearing, check that the `displayStand` property is `true` AND the `appearance` property is set to either `"mimic"` or `"simple"`.
*   To display the exact value (e.g., 87 liters) instead of a percentage, you must set `value.displayValueAsPercent` to `false`. The text for this display can then be set via the `value.value` property.
*   If you don't want to see the label or the value text, set their respective `location` properties to `"hidden"`. For example, to hide the label, set `label.location` to `"hidden"`.
*   The `state` property is powerful when combined with styles. You can define custom styles for states like "running" or "faulted" to change the vessel's appearance dynamically.
*   The `liquidColor` and `liquidWarningColor` properties should be set to valid color strings, such as hex codes (`#00ACAC`) or RGB values.
*   To make the liquid completely solid and not transparent, set `liquidOpacity` to `1`.
*   For advanced styling, you can assign a style class to the main `style` property or to the `label.style` and `value.style` properties.
*   If the agitator animation is distracting, you can either hide the agitator completely by setting `displayAgitator` to `false`, or you can stop the animation by setting `animationSpeed` to `0`.

# Schema - raw
{"schema":{"type":"object","properties":{"orientation":{"type":"string","enum":["horizontal","vertical"],"default":"vertical"},"displayFillLevel":{"type":"boolean","default":true},"bottom":{"visibleWhen":{"equals":"vertical","property":"orientation"},"type":"string","enum":["flat","conical","rounded"],"default":"flat"},"displayStand":{"visibleWhen":{"equals":["mimic","simple"],"property":"appearance"},"type":"boolean","default":true},"label":{"type":"object","properties":{"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right","auto"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Label to display as text","type":["string","number","boolean","null","object","array"],"example":"Vessel","default":"Vessel"}}},"animationSpeed":{"description":"The speed of animations as a percent. 0 turns off animations.","type":["string","number"],"default":"auto"},"liquidOpacity":{"type":"number","default":0.7,"maximum":1,"minimum":0},"appearance":{"description":"auto uses the value of the Session Prop symbols.appearance if it exists, default is mimic.","type":"string","enum":["auto","p&id","mimic","simple"],"default":"auto"},"liquidColor":{"format":"color","description":"The color used to render the filled part of the tank.","type":"string","default":""},"liquidWarningColor":{"format":"color","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"state":{"format":"symbol-states","type":"string","default":"default"},"displayAgitator":{"type":"boolean","default":true},"value":{"type":"object","properties":{"displayValueAsPercent":{"type":"boolean","default":true},"capacity":{"type":"number","default":100},"justify":{"description":"Horizontal text alignment.","type":"string","enum":["left","center","right"],"default":"center"},"location":{"type":"string","enum":["top","bottom","left","right","hidden"],"default":"bottom"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"type":"number","default":0}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Vessel","name":"Vessel","palette":{"variants":[{"tooltip":"An animated component that looks like a tank or vessel.","label":"Vessel"}],"category":"symbols"},"id":"ia.symbol.vessel"}