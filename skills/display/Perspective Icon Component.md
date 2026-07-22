# Perspective Icon Component

## Description

These instructions detail the configuration and usage of the Perspective Icon Component. The document covers the primary methods for selecting an icon, applying simple color or complex CSS styling, and adjusting the icon's visible area for cropping and panning effects.

## Documentation

# Instructions
# Instructions for the LLM

You are an expert in configuring and using the **Perspective Icon Component** in Ignition. Your purpose is to display vector-based SVG icons.

## Object Definition

The Icon component is used to display an icon from a library. It is a simple and efficient way to add visual cues to your Perspective Views. The icon itself is rendered as an SVG image, allowing for scalable and high-quality graphics that can be colored and styled.

---

## Property Instructions

Here is a detailed breakdown of the component's properties and how to configure them.

### Identifying the Icon

There are two mutually exclusive ways to specify which icon to display. You must use one of the following methods:

**Method 1: Using the `path` Property (Recommended)**

*   The `path` property is a single string that combines the icon library and the icon name.
*   **Format:** The format must be `library_name/icon_name`.
*   **Example:** To use the `insert_emoticon` icon from the `material` library, you would set the `path` property to `"material/insert_emoticon"`.
*   This is the most common and convenient way to select an icon.

**Method 2: Using `library` and `name` Properties**

*   Alternatively, you can specify the icon by providing the `library` and `name` properties separately.
*   **`library` (string):** The name of the icon library where the desired icon is located.
*   **`name` (string):** The name of the specific icon you want to display.
*   **Usage:** You must provide a value for **both** `library` and `name` if you choose this method. You cannot use `path` at the same time.

### Styling the Icon

**`color` Property**

*   This property sets the color of the icon.
*   **Type:** String, representing a color. This can be a hex code (e.g., `#FF0000`), a color name (e.g., `red`), or an RGB value (e.g., `rgb(255, 0, 0)`).
*   **Convenience:** This is a quick and easy way to color the icon. For more advanced color control, use the `style` property.

**`style` Property**

*   This is an object that allows for applying complex CSS styling to the icon.
*   You can set any valid CSS properties here. For coloring the icon, you would typically set the `fill` property within the style object.
*   **Example:** To set the color to blue with a red outline, you might configure the style object like this: `{"fill": "blue", "stroke": "red"}`.

### Adjusting the Icon's Viewport

**`viewBox` Property**

*   The `viewBox` is an object that allows you to crop or pan the SVG image within its frame. It defines a specific rectangular region of the icon to display.
*   This is useful if you only want to show a portion of an icon or if the icon has extra whitespace you want to trim.
*   The `viewBox` object has four properties:
    *   **`x` (number):** The starting x-coordinate of the viewable rectangle. A positive value will effectively pan the icon to the left.
    *   **`y` (number):** The starting y-coordinate of the viewable rectangle. A positive value will effectively pan the icon upwards.
    *   **`width` (number):** The width of the viewable rectangle. A smaller value will zoom into the icon, effectively cropping the right side.
    *   **`height` (number):** The height of the viewable rectangle. A smaller value will zoom into the icon, effectively cropping the bottom.

---

## Helpful Tips

*   **Primary Identification:** Always prefer using the `path` property for its simplicity and clarity unless you have a specific reason to define `library` and `name` separately.
*   **Choose One Method:** You **must** define the icon using *either* the `path` property *or* the `library` and `name` properties. You cannot mix them. The component's schema requires one of these two methods to be satisfied.
*   **Coloring:** For simple color changes, the top-level `color` property is sufficient. For more complex styling, like gradients, outlines (`stroke`), or opacity, use the `style` property. The `color` property is a convenient shortcut for setting the `fill` style.
*   **`viewBox` for Cropping:** The `viewBox` property does not resize the component itself, but rather the visible area *of the icon* within the component. Think of it as a window or a magnifying glass over the source SVG.
*   **Default State:** If no properties are set, the component will be empty, as it requires a `path` or `library`/`name` to render an icon.
*   **Vector Benefits:** Remember that because these are SVG icons, they will scale to any size without losing quality. Their appearance is controlled by styling properties, not a pre-rendered image file.

# Schema - raw
{"schema":{"type":"object","oneOf":[{"required":["path"]},{"required":["library","name"]}],"properties":{"color":{"format":"color","description":"Color of the icon. Here for convenience, may instead assign 'fill' in the styles prop.","type":"string","default":""},"path":{"format":"icon-path","description":"Shorthand path to icon source, in format: library/iconName","type":"string","example":"material/insert_emoticon","default":""},"library":{"description":"Optional alternative to 'path', name of library where icon is located. Must also supply 'name'.","type":"string"},"viewBox":{"description":"Properties to assign to the 'viewBox' portion of the SVG that displays the icon.","type":"object","properties":{"x":{"description":"The x value (amount to crop from the X axis) assigned to the 'viewBox' portion of the SVG that displays the icon.","type":"number"},"width":{"description":"The width assigned to the 'viewBox' portion of the SVG that displays the icon.","type":"number"},"y":{"description":"The y value (amount to crop from the Y axis) assigned to the 'viewBox' portion of the SVG that displays the icon.","type":"number"},"height":{"description":"The height assigned to the 'viewBox' portion of the SVG that displays the icon.","type":"number"}}},"name":{"description":"Optional alternative to 'path', name of icon. Must also supply 'library'.","type":"string"},"style":{"default":{},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Icon","name":"Icon","palette":{"variants":[{"tooltip":"An image path to an icon, commonly used to augment a label or text property of a component by placing the icon next to it.","label":"Icon"}],"category":"display"},"id":"ia.display.icon"}