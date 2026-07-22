# Perspective Embedded View Component

## Description

This document details the configuration and usage of the Perspective Embedded View component, an essential tool for creating modular and reusable user interfaces. It explains how to embed a separate, pre-existing view within another, pass dynamic data to it using parameters, and manage its sizing, styling, and loading behavior for optimal performance.

## Documentation

# Instructions
# Perspective Embedded View Component

## Core Functionality

The Embedded View component is a fundamental tool for creating modular and reusable user interfaces in Perspective. Its primary function is to display an entire, separate view within the boundary of the component. This allows for the creation of "template" views that can be reused in multiple locations. For example, you could design a detailed view for a single motor, and then use the Embedded View component to place several instances of that motor view onto a larger plant overview screen.

Data can be passed from the parent view into the embedded view through parameters, making each instance of the embedded view dynamic and unique.

## Key Properties

### `path`
*   **Type:** String
*   **Description:** This is the most critical property. It holds the path to the Perspective View you want to embed. The path must be valid and point to an existing view in the project.
*   **Usage:** Set this property to the full path of the view to be displayed. For example: `MyViews/MotorTemplate`.

### `params`
*   **Type:** Object
*   **Description:** An object containing key-value pairs that are passed into the embedded view. For this to work, the embedded view must have corresponding parameters defined in its own `view.params` section. The keys in this `params` object **must** match the keys of the parameters on the target view.
*   **Usage:** To pass a motor number to an embedded view, if the target view has a parameter named `motorId`, you would configure this property as `{"motorId": 123}`.

### `useDefaultViewWidth` and `useDefaultViewHeight`
*   **Type:** Boolean
*   **Description:** These properties determine how the Embedded View component sizes itself.
    *   If `false` (the default), the component will attempt to adjust its size based on the content of the view it is embedding.
    *   If `true`, the component will use the default width/height defined on the root of the embedded view itself.

### `loading.order`
*   **Type:** String
*   **Description:** Controls the loading behavior of the embedded view relative to its parent view.
    *   `after-parent` (Default): The parent view will load and display first, and then the embedded view will begin to load. This can make the application *feel* faster to the user because the main interface appears more quickly, even if the total load time is slightly longer.
    *   `with-parent`: The embedded view loads simultaneously with the parent view. This is generally more efficient for the browser but can make the initial display of the parent view feel slower if the embedded view is complex.

### `style`
*   **Type:** Object
*   **Description:** Allows for standard CSS styling of the component's container, such as setting a background color, border, padding, or margins.

---

## Helpful Tips & Best Practices

*   **Performance Warning:** Be cautious about performance. Over-saturating a single view with a large number of Embedded Views, or creating deeply nested chains of them (e.g., a view embedded in a view embedded in another view), can lead to slow load times and a sluggish user experience. Potential "race conditions" from passing parameters between many embedded views can also degrade performance.

*   **When to Use an Embedded View vs. a Container:**
    *   Use the **Embedded View** when you want to display a *separate, pre-existing view* and potentially reuse it in multiple places. It's ideal for templating.
    *   Use a **Container** component (like a Flex Container or Coordinate Container) when you want to group and arrange a set of components *directly within the current view*. You cannot add or remove components from an embedded view from the parent; you can only do so with a container.

*   **Parameters are Essential for Dynamic Content:** The true power of the Embedded View is realized through the `params` property. Always ensure that the parameter keys you define on the Embedded View component instance perfectly match the parameter names defined on the view you are embedding.

*   **Styling Affects the Container:** The `style` property of the Embedded View component applies to the component's container itself, not the content of the view being embedded. For example, `props.style.backgroundColor` will change the background of the Embedded View component's area, which can be seen if the embedded view itself has no background or has margins.

*   **Navigating in the Designer:** When a valid view `path` is entered in the Property Editor in the Ignition Designer, a small "Open View" icon will appear next to the property. Clicking this icon is a convenient shortcut to open and edit the embedded view directly.

*   **Adding Parameters in the Designer:** The Ignition Designer provides a helpful UI for adding parameters to the `params` object. When you click the "Add Object Member" icon, a dropdown will often suggest available parameters from the target view specified in the `path` property, which helps prevent typos.

# Schema - raw
{"schema":{"type":"object","properties":{"useDefaultViewWidth":{"description":"Use of view's default width instead of adjusting based on the content's width.","type":"boolean","default":false},"params":{"extension":{"view-params":{"path":"/path"}},"description":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","type":"object","default":{}},"loading":{"type":"object","properties":{"order":{"description":"Controls when the embedded view loads: after the parent is displayed or combined with the parent view loading","type":"string","enum":["after-parent","with-parent"],"default":"after-parent"}}},"path":{"format":"view-path","description":"Path of embedded view to display","type":"string","default":""},"useDefaultViewHeight":{"description":"Use of view's default height instead of adjusting based on the content's height.","type":"boolean","default":false},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"EmbeddedView","name":"Embedded View","palette":{"variants":[{"tooltip":"Enables an entire view to be embedded within another view.","label":"Embedded View"}],"category":"embedding"},"id":"ia.display.view"}