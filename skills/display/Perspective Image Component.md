# Perspective Image Component

## Description

These instructions explain the usage and configuration of the Perspective Image Component. They detail the properties that control the image's source, accessibility text, color tinting, and scaling behavior, including how it fits, stretches, or scrolls within its container.

## Documentation

# Instructions
Here are the instructions for the **Perspective Image Component**.

# General Instructions for the LLM

This document provides a detailed guide to understanding and using the **Perspective Image Component** in Ignition. Your primary goal is to assist users in configuring this component by manipulating its properties based on their requests.

The Image component is used to display raster images (like `jpeg`, `gif`, `png`) or vector graphics (`svg`). Its appearance and behavior are controlled by a set of properties that you can modify.

---

## Component Properties

Here is a detailed breakdown of the JSON schema for the Perspective Image Component.

### `source`
*   **Type:** `string`
*   **Description:** This is the most critical property. It defines the actual image to be displayed. The value must be a URI (Uniform Resource Identifier).
*   **Usage:**
    *   It can be a URL pointing to an image on the internet (e.g., `https://some_website.com/image.png`).
    *   It can be a path to an image stored within the Ignition Gateway.
    *   It can be a path to an embedded image.

### `altText`
*   **Type:** `string`
*   **Description:** This property provides alternative text for the image. It's crucial for accessibility and error handling.
*   **Usage:** The `altText` is displayed if the image fails to load due to a broken link, slow connection, or other errors. It is also used by screen readers for visually impaired users. You should encourage users to set this to a descriptive value.
*   **Default:** `""` (empty string)

### `tint`
*   **Type:** `object`
*   **Description:** This property allows you to apply a uniform color tint to the entire image. It consists of two sub-properties.
*   **Sub-Properties:**
    *   `enabled` (boolean): Set to `true` to activate the tint and `false` to disable it.
    *   `color` (string): A color string (e.g., `#FF0000` for red) that will be used for the tint when `enabled` is `true`.
*   **Default:** `{ "enabled": false, "color": "#CCCCCC" }`

### `fit`
*   **Type:** `object`
*   **Description:** This property controls how the image scales and fits within the component's boundaries. It is a complex object with several sub-properties that determine the final appearance.
*   **Sub-Properties:**
    *   `mode` (string): This is the most important sub-property of `fit`. It dictates the scaling strategy.
        *   `none`: The image is displayed at its original size. If it's larger than the component, it will be cropped.
        *   `fill`: The image is stretched and resized to completely fill the component's width and height. **This may distort the image's original aspect ratio.**
        *   `contain`: The image is scaled down or up to fit entirely within the component's boundaries while **preserving its aspect ratio**. This may result in empty space (letterboxing) inside the component if the aspect ratios don't match.
        *   `cover`: The image is scaled to completely cover the component's area while **preserving its aspect ratio**. If the aspect ratios of the image and component differ, the image will be cropped to fit.
        *   `percent`: The image's size is set as a percentage of the component's dimensions. The `width` and `height` properties are used to specify these percentages.
        *   `absolute`: The image is resized to an absolute pixel value. The `width` and `height` properties are used to specify these pixel dimensions.
    *   `width` (number): Used only when `mode` is `percent` or `absolute`. It defines the target width of the image.
    *   `height` (number): Used only when `mode` is `percent` or `absolute`. It defines the target height of the image.
    *   `scroll` (boolean): If the image is larger than the component's bounds (e.g., in `none` or `absolute` mode), setting this to `true` will show scrollbars, allowing the user to pan across the image.
*   **Default:** `{ "mode": "none", "width": 100, "height": 100, "scroll": false }`

### `style`
*   **Type:** `object`
*   **Description:** This property is used to apply CSS-based styling to the component. It references a standard set of style properties available for many Perspective components.

---

## Helpful Tips for the LLM

*   **Prioritize the Source:** The component is useless without a valid `source`. Always confirm the user has a path or URL for the image they want to display.
*   **Always Suggest `altText`:** For good practice, whenever a user sets an image `source`, suggest they also provide descriptive `altText` for accessibility and robustness.
*   **Clarify `fit.mode`:** The `fit.mode` property is the most complex. When a user asks to "make an image fit," you must clarify *how* they want it to fit.
    *   "Should it stretch to fill the whole box, even if it looks distorted?" -> Use `fill`.
    *   "Should the whole image be visible without any cropping, even if there's blank space?" -> Use `contain`.
    *   "Should it completely cover the box without any blank space, even if parts of the image get cut off?" -> Use `cover`.
*   **Tinting for Status:** The `tint` property is excellent for providing visual feedback. For example, you can suggest tinting an image of a motor green when it's running and red when it's faulted by binding the `tint.color` and `tint.enabled` properties to system tags.
*   **Responsive vs. Fixed Sizing:**
    *   For responsive designs that adapt to screen size, the `percent` mode is generally preferred.
    *   For designs where an image must be a specific size regardless of the container, use the `absolute` mode.
*   **Image Overflow and Scrolling:** If an image is larger than its container, it will be cropped by default. Remind the user that if they want to see the rest of the image, they need to set `fit.scroll` to `true`. This is most relevant when `fit.mode` is `none` or `absolute`.
*   **Supported Formats:** The component supports common web image formats, including `jpeg`, `gif`, `png`, and `svg`.

# Schema - raw
{"schema":{"type":"object","properties":{"altText":{"description":"An alternate text for the image, if the image cannot be displayed (because of a slow connection, an error in the src attribute, if the user uses a screen reader, or some other reason).","type":"string","default":""},"source":{"format":"image","description":"The image source URI. Could be a URL to an image on the internet or gateway, or could be an embedded image.","type":"string","default":""},"tint":{"description":"Tint the entire image a color.","type":"object","default":{"color":"#CCCCCC","enabled":false},"properties":{"color":{"format":"color","description":"If the Tint Filter is on, this is the color of the tint.","type":"string","default":"#CCCCCC"},"enabled":{"description":"Turn tint on (true) and off (false).","type":"boolean","default":false}}},"fit":{"description":"Whether or not the image will size to fit. When in percent mode, the parameters are used to fit based on the % of the width and height. When in absolute mode, the image will fit the width and height sizes in pixels.","type":"object","default":{"scroll":false,"mode":"none","width":100,"height":100},"properties":{"scroll":{"type":"boolean","default":false},"mode":{"type":"string","enum":["none","fill","contain","cover","percent","absolute"],"default":"none"},"width":{"type":"number","default":100},"height":{"type":"number","default":100}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Image","name":"Image","palette":{"description":"Displays a vector or raster image, such as jpeg, gif, png, or svg","variants":[{"tooltip":"Displays a vector or raster image, such as jpeg, gif, png, or svg","label":"Image"}],"category":"display"},"id":"ia.display.image"}