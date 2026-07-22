# Perspective Text Area Component

## Description

This document details the usage and configuration of the Perspective Text Area component, designed for displaying and editing multiple lines of text. It explains the various properties that control the component's behavior and appearance, such as text handling, data update timing, user interaction, and styling. These instructions will help a user effectively implement and customize the component for various data entry and display applications.

## Documentation

# Instructions
# Perspective Text Area Component Instructions

## Introduction
The Text Area component is used for displaying and editing multiple lines of text. It is suitable for scenarios where users need to input or view text that spans more than one line, such as comments, descriptions, or logs. The component can scroll vertically when the text content exceeds the available space.

---

## Properties

Here is a detailed list of the properties available for the Text Area component.

| Property | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| **text** | String / Number | The text content to be displayed and edited within the component. | `""` |
| **placeholder** | String / Number | The placeholder text that appears when the `text` property is empty. This is typically used to give the user a hint about what to enter. | `""` |
| **enabled** | Boolean | If `true`, the user can interact with the component and edit the text. If `false`, the component is read-only. | `true` |
| **deferUpdates** | Boolean | If `true`, any changes to the `text` property will only be sent to the server after the user clicks away from the component (loses focus). If `false`, updates are sent on every keystroke. | `true` |
| **rejectUpdatesWhileFocused** | Boolean | If `true`, the `text` property will not accept updates from external sources (like a binding) while the user has the component focused (i.e., they are typing in it). This prevents the user's input from being overwritten. | `true` |
| **resize** | String | Determines if and how the user can resize the Text Area in the session. The options are: `none`, `both`, `horizontal`, or `vertical`. | `none` |
| **wrap** | String | Specifies how the text should wrap within the component. The options are: `soft` (text wraps to fit the component's width, but the actual `text` value does not contain line breaks), `hard` (text wraps and line break characters are inserted into the `text` value), or `off` (text does not wrap and horizontal scrolling will appear if needed). | `soft` |
| **spellcheck** | Boolean | If `true`, the browser's built-in spell checker will be enabled, highlighting potential spelling errors as the user types. | `true` |
| **style** | Object | This property allows for custom styling of the component. You can configure styles for text, background, margins, padding, borders, and more, or assign a pre-configured Style Class. | |

---

## Component Events

Component events, such as `onFocus` or `onBlur`, can be configured to trigger actions or run scripts. Configuration for these events is handled in the Component Events and Actions section of the Property Editor. For a complete list of all possible event types and how to configure them, refer to the official documentation on Component Events and Actions and the Perspective Event Types Reference.

---

## Helpful Tips

*   **Input Handling**: The `deferUpdates` and `rejectUpdatesWhileFocused` properties are crucial for managing user input. For most data entry scenarios, keeping both set to `true` provides the best user experience, preventing data loss and unnecessary updates while the user is typing.
*   **Text Wrapping**:
    *   `soft`: The most common setting. The text appears to wrap within the component for easy reading, but the underlying `text` property value remains free of artificial line breaks.
    *   `hard`: Use this when the line breaks themselves are meaningful and need to be saved as part of the string data.
    *   `off`: Best for displaying pre-formatted text or code where line integrity is important. This will enable horizontal scrolling if a line exceeds the component's width.
*   **Placeholder vs. Text**: The `placeholder` is only visible when the `text` property is an empty string (`""`). It is not a default value for the `text` property itself.
*   **Scrollbars**: The Text Area will automatically display a vertical scrollbar if the content is taller than the component's height. A horizontal scrollbar will only appear if `wrap` is set to `off` and a line of text is wider than the component's width.
*   **Dynamic Sizing**: If you want the user to be able to resize the component, set the `resize` property to `vertical`, `horizontal`, or `both`.
*   **Spell Checking Nuances**: Be aware that the behavior and dictionary of the `spellcheck` feature can vary slightly from one web browser to another (e.g., Chrome vs. Firefox vs. Safari).
*   **Bindings**: Most properties are bindable. You can bind the `text` property to a database tag or another component property to create dynamic and interactive views.

# Schema - raw
{"schema":{"type":"object","properties":{"rejectUpdatesWhileFocused":{"description":"When true, props.text will not accept updates from external sources while focused.","type":"boolean","default":true},"enabled":{"description":"If user should be allowed to alter text.","type":"boolean","default":true},"spellcheck":{"description":"When true, the component will highlight potential spelling errors while text is being edited.","type":"boolean","default":true},"resize":{"description":"Sets whether text area is resizable, and if so, in which direction(s).","type":"string","enum":["none","both","horizontal","vertical"],"default":"none"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display.","type":["string","number"],"default":""},"placeholder":{"description":"Text displayed when text is empty.","type":["string","number"],"default":""},"wrap":{"description":"Specifies how to wrap text.","type":"string","enum":["hard","soft","off"],"default":"soft"},"deferUpdates":{"description":"When true, updates to props.text will be deferred until focus is lost.","type":"boolean","default":true}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"TextArea","name":"Text Area","palette":{"variants":[{"tooltip":"Enables display and editing of multiple lines of text.","label":"Text Area"}],"category":"input"},"id":"ia.input.text-area"}