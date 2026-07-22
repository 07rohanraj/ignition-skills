# Perspective Split Container

## Description

These instructions detail the usage and configuration of the Perspective Split Container, a component designed to create a two-paneled layout with a resizable divider. The documentation explains how to set the container's orientation, define the initial position and appearance of the split, and control user interactions like draggability. It also covers best practices for creating both responsive and fixed layouts using the container's properties and events.

## Documentation

# Instructions
# Perspective Split Container Instructions

## 1. Core Concept

The **Perspective Split Container** is a specialized container designed to hold exactly **two** child components. These two components are separated by a divider, known as the "split". The container can be oriented either horizontally or vertically. In a running session, an end-user can typically drag the split to resize the two child components relative to each other. It is ideal for creating layouts like master-detail screens, side-by-side comparisons, or any view that requires two distinct, resizable areas.

## 2. Configuration & Properties

The behavior and appearance of the Split Container are controlled by its properties.

### Primary Properties

| Property      | Type             | Description                                                                                                                                                                                                                         |
| :------------ | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `orientation` | `string`         | **Required**. Determines the layout direction of the two child components. <br/>- **`"horizontal"` (Default):** The split is vertical, creating a left pane and a right pane. The user drags the split left and right. <br/>- **`"vertical"`:** The split is horizontal, creating a top pane and a bottom pane. The user drags the split up and down. |
| `split`       | `object`         | A container for all properties related to the draggable split bar itself.                                                                                                                                                           |

### Split Properties

These properties are nested under the main `split` property (e.g., `split.position`).

| Property      | Type             | Description                                                                                                                                                                                                                         |
| :------------ | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `position`    | `number` or `string` | Sets the initial position of the split bar and thus the size of the first child component. This value is bidirectional. <br/>- **As a `string`:** Use a percentage value (e.g., `"50%"`). This is responsive and will adapt to the container's total size. <br/>- **As a `number`:** Use a pixel value (e.g., `300`). This creates a fixed-size pane. <br/>The default is `"50%"`. |
| `draggable`   | `boolean`        | If `true` (the default), users can drag the split bar to resize the panes. If `false`, the split position is fixed.                                                                                                                   |
| `visible`     | `boolean`        | If `true` (the default), the split bar is visible as a distinct element. If `false`, the bar is not rendered, but the space it occupies still exists, and it may still be draggable if `draggable` is `true`. |
| `size`        | `number`         | The thickness of the split bar in pixels. This is also the size of the "grab" area for dragging. The default is `16`.                                                                                                          |

### Child Component Properties

When a component is placed inside of a Split container, it will inherit the position property listed below.
| Property	| Description	| Data Type
| position	| Indicates which side of the split bar the child component is located on. Expected values include "left", "right", "top", and "bottom"	| value: string

## 3. Events

The Split Container has events that can be used to trigger actions.

*   `onMinBoundReached`: This event fires when the user drags the split handle to its minimum possible position (e.g., all the way to the left in a horizontal container).
*   `onMaxBoundReached`: This event fires when the user drags the split handle to its maximum possible position (e.g., all the way to the right in a horizontal container).

## 4. Scripting

The full list of scripting functions available for this component can be found on the `Perspective - Split Container Scripting` page in the user manual.

## 5. Helpful Tips & Best Practices

*   **Two-Child Limit:** Always remember that the Split Container is designed for **exactly two** children. If you need to display more than two components in one of the panes, you must first place another container (like a Flex Container or Column Container) into that pane and then add your components to it.
*   **Responsive vs. Fixed Panes:**
    *   For a layout that should adapt gracefully to different screen sizes, set `split.position` to a percentage string (e.g., `"33%"`).
    *   To create a fixed-size sidebar or header, set `split.position` to a numeric pixel value (e.g., `250`).
*   **Creating a Fixed Layout:** To create a two-panel layout that the user cannot change, set the `split.draggable` property to `false`.
*   **Invisible Dividers:** For a seamless two-panel layout with no visible divider, set `split.visible` to `false`. If you also set `split.draggable` to `false`, the division will be completely static and invisible.
*   **Event-Driven Actions:** Use the `onMinBoundReached` and `onMaxBoundReached` events to create dynamic user experiences. For example, you could use these events to hide or show other components on the view, or to collapse a navigation menu completely.
*   **Orientation is Key:** The `orientation` property is the most fundamental setting. A **`horizontal`** orientation means the components are arranged side-by-side (left/right). A **`vertical`** orientation means they are stacked (top/bottom).

# Schema - raw
{"schema":{"type":"object","required":["orientation"],"additionalProperties":false,"properties":{"orientation":{"description":"The orientation in which the container's split is fixed. Horizontal will allow the user to adjust the container from left to right, while Vertical will allow the user to adjust it from top to bottom.","type":"string","enum":["horizontal","vertical"],"default":"horizontal"},"split":{"description":"Split bar option configuration","type":"object","required":["position","size","visible"],"properties":{"visible":{"description":"Determines if the split bar should be visible.","type":"boolean","default":true},"size":{"description":"The size of the split bar in pixels.","type":"number","default":16},"draggable":{"description":"Determines if the split bar should be draggable.","type":"boolean","default":true},"position":{"description":"Bidirectionally represents the position of the split bar. Numeric values written here will be used as pixels.","type":["number","string"],"default":"50%"}}},"style":{"default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"SplitContainer","name":"Split Container","palette":{"variants":[{"tooltip":"A container that has two children and can be oriented in either a horizontal or vertical position with a draggable split bar that separates and resizes the two accordingly.","label":"Split"},{"tooltip":"A container that has two children and can be oriented in either a horizontal or vertical position with a draggable split bar that separates and resizes the two accordingly.","label":"Horizontal","id":"split-horizontal"},{"tooltip":"A container that has two children and can be oriented in either a horizontal or vertical position with a draggable split bar that separates and resizes the two accordingly.","label":"Vertical","props":{"orientation":"vertical"},"id":"split-vertical"}],"category":"container"},"id":"ia.container.split","childPositionSchema":{"type":"object","default":{}},"events":[{"schema":{"type":"object"},"description":"This event is fired when the minimum bound on the container is reached by the handle","name":"onMinBoundReached"},{"schema":{"type":"object"},"description":"This event is fired when the maximum bound on the container is reached by the handle","name":"onMaxBoundReached"}]}