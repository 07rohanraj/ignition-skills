# Perspective Button Component

## Description

This document details the configuration and usage of the Perspective Button component, explaining how to customize its visual properties, such as text, icons, and styling. It covers how to control the layout of the button's content, manage its interactive state, and configure its events to trigger actions when pressed by a user.

## Documentation

# Instructions
# Perspective Button Component

## Object Description
The Perspective Button component is a standard, versatile input component used to initiate an action when pressed by a user. It is a foundational element for user interaction, commonly used for navigation, submitting data, or triggering scripts and events. The button can display text, an icon, or a combination of both. It comes in two pre-configured visual styles: "Primary" and "Secondary".

## Properties

| Property | Type | Description | Default Value |
| --- | --- | --- | --- |
| **text** | `string` or `number` | The text that will be displayed on the button. | `"Button"` |
| **primary** | `boolean` | Toggles the button's visual style between the default "Primary" and "Secondary" styles. `true` for Primary, `false` for Secondary. | `true` |
| **enabled** | `boolean` | If `true`, the button is interactive. If `false`, the button is visually "greyed out" and cannot be pressed. | `true` |
| **image** | `object` | An object that defines an optional image or icon to be displayed on the button. It contains the following nested properties: | |
| | **image.source** | `string` | The URI for the image. This can be a URL, a path to an image in the Ignition Gateway (e.g., `/system/images/path/to/image.png`), or an embedded image. | `""` |
| | **image.icon** | `object` | Defines an icon to use from the built-in library. | |
| | | **image.icon.path** | `string` | The path to the icon, typically in the format `library/IconName` (e.g., `material/check`). | `""` |
| | | **image.icon.color** | `string` | The color of the icon. | `""` |
| | **image.position** | `string` | The position of the image relative to the text. Enum: `left`, `center`, `right`, `top`, `bottom`. | `"left"` |
| | **image.width** | `number` | The width of the image in pixels. | `24` |
| | **image.height** | `number` | The height of the image in pixels. | `24` |
| | **image.style** | `object` | Style properties applied specifically to the image within the button. | |
| **justify** | `string` | Justifies the text and image along the main axis. If `image.position` is `top` or `bottom`, the main axis is horizontal. Otherwise, the main axis is vertical. Enum: `start`, `center`, `end`, `space-around`, `space-between`, `space-evenly`. | `"center"` |
| **align** | `string` | Aligns the text and image along the cross axis. If `image.position` is `top` or `bottom`, the cross axis is vertical. Otherwise, the cross axis is horizontal. Enum: `start`, `center`, `end`, `stretch`. | `"center"` |
| **style** | `object` | An object containing CSS-like properties to style the button component itself (background, border, etc.). | |
| **textStyle** | `object` | An object containing CSS-like properties applied specifically to the button's text. | |

## Events

*   **onActionPerformed**: This is the primary event for the Button component. It fires when a user clicks or presses the button. Actions, such as running a script, navigating to a new view, or writing to a tag, are configured to execute when this event occurs.

## Helpful Tips & Best Practices

*   **Primary vs. Secondary Style**: The `primary` property is a simple boolean toggle for the button's appearance. Set `primary: true` (the default) for the main call-to-action button, and `primary: false` for less prominent, secondary actions.
*   **Adding an Image/Icon**:
    *   To use a pre-loaded image from the Ignition Gateway, set the `image.source` property to its path, for example: `/system/images/Builtin/icons/48/disk_green.png`.
    *   To use a material design icon, set the `image.icon.path` property, for example: `material/save`. You can also set the `image.icon.color`.
*   **Image and Text Layout**:
    *   The `image.position` property determines the location of the image relative to the text (`top`, `bottom`, `left`, `right`).
    *   Once `image.position` is set, use `justify` and `align` to fine-tune the layout.
    *   `justify` controls the arrangement along the main axis (e.g., `space-between` to push the text and image to opposite ends).
    *   `align` controls the arrangement along the cross axis (e.g., `center` to vertically center text next to an image).
*   **Styling**:
    *   To change the button's background color or border, modify the `style` property (e.g., `style.backgroundColor`, `style.borderStyle`, `style.borderWidth`).
    *   To change only the text's color, font, or weight, modify the `textStyle` property (e.g., `textStyle.color`, `textStyle.fontWeight`).
*   **Disabling the Button**: Set the `enabled` property to `false` to prevent users from clicking the button. This is useful for preventing actions until a condition is met, like filling out all required input fields.
*   **Triggering Actions**: The main purpose of a button is to perform an action. Right-click the component in the designer and select "Configure Events" to add actions to the `onActionPerformed` event handler.

# Schema - raw
{"schema":{"type":"object","properties":{"image":{"description":"An optional image to be embedded in the button","type":"object","default":{"icon":{"color":"","path":""},"source":"","width":24,"style":{"classes":""},"position":"left","height":24},"properties":{"icon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"source":{"format":"image","description":"The image source URI. Could be a URL to an image on the internet or gateway, or could be an embedded image.","type":"string","default":""},"width":{"description":"The width of the button image in pixels","type":"number","default":24},"style":{"description":"Style properties that are applied to the image within the button.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"position":{"description":"The position of the image within the button relative to the text","type":"string","enum":["left","center","right","top","bottom"],"default":"left"},"height":{"description":"The height of the button image in pixels","type":"number","default":24}}},"align":{"description":"Align text and image (if present) along the cross axis. Vertical if imagePosition top or bottom, else horizontal.","type":"string","enum":["start","center","end","stretch"],"default":"center"},"enabled":{"description":"Enables button interaction.","type":"boolean","default":true},"justify":{"description":"Justify text and image (if present) along the main axis. Horizontal if imagePosition top or bottom, else vertical.","type":"string","enum":["start","center","end","space-around","space-between","space-evenly"],"default":"center"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display on button","type":["string","number"],"default":"Button"},"textStyle":{"description":"Style properties that are applied to the text within the button.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"primary":{"description":"Toggle between the default primary and secondary button style.","type":"boolean","default":true}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Button","name":"Button","palette":{"variants":[{"tooltip":"A standard button component commonly used for navigation and control.","label":"Button"},{"tooltip":"A standard button component commonly used for navigation and control.","label":"Primary","id":"button-primary"},{"tooltip":"A standard button component commonly used for navigation and control.","label":"Secondary","props":{"primary":false},"id":"button-secondary"}],"category":"input"},"id":"ia.input.button","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}