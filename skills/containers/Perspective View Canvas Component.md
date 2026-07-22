# Perspective View Canvas Component

## Description

These instructions explain the usage and configuration of the Perspective View Canvas component, a container for displaying multiple Views in a dynamic, coordinate-based layout. The document details how to place, size, and layer individual View instances by manipulating the `props.instances` array, and it covers how to apply animated transitions and handle user interaction through scripting.

## Documentation

# Instructions
### Instructions for using the Perspective View Canvas Component

The Perspective View Canvas is a container component used to display multiple Perspective Views within a single, coordinate-based layout. It allows for precise placement, sizing, and layering of individual View instances, and supports animated transitions when their properties change.

#### Core Concepts

The primary configuration of the View Canvas is done through its `props.instances` property. This property is an array of objects, where each object represents a single "instance" of a View displayed on the canvas. To add, remove, or modify the Views on the canvas, you must manipulate the objects within this array.

#### Configuring Instances

Each object within the `props.instances` array has the following key properties:

*   **`viewPath`**: (String) The path to the Perspective View you want to display in this instance (e.g., "MyProject/MyView").
*   **`viewParams`**: (Object) A dictionary of parameters to pass into the View instance. This allows you to make your embedded Views dynamic.
*   **`position`**: (String) Determines how the instance is positioned. It has two possible values:
    *   `"absolute"`: The instance is positioned relative to the top-left corner of the View Canvas component itself, based on the `top`, `left`, `right`, and `bottom` properties. Absolute instances do not affect the positioning of other instances.
    *   `"relative"`: The instance is positioned in the normal document flow. It will appear after the preceding instance. The `top`, `left`, `right`, and `bottom` properties will act as offsets from this default position.
*   **`left`, `top`, `right`, `bottom`**: (String) These properties define the position of the instance. Values must be a string including CSS units (e.g., `"10px"`, `"50%"`).
    *   **Positioning Precedence**:
        *   If `left` and `right` are both set on an `absolute` positioned instance with an unrestricted width, `left` will take precedence.
        *   If `top` and `bottom` are both set on an `absolute` positioned instance with an unrestricted height, `top` will take precedence.
*   **`width`, `height`**: (String) The dimensions of the instance. Values must be a string including CSS units (e.g., `"200px"`, `"auto"`).
*   **`zIndex`**: (Integer | String) Controls the stacking order of instances. An instance with a higher `zIndex` will appear in front of an instance with a lower `zIndex`. Can be a number or the string `"auto"`.
*   **`style`**: (Object) An object for applying specific CSS styles to this individual instance. These styles will override any styles defined in `props.defaultStyle`.

#### Global Component Properties

*   **`useDefaultViewWidth` / `useDefaultViewHeight`**: (Boolean) If set to `true`, these properties force all instances to use the default width/height defined within their respective View files, overriding any `width` or `height` set on the instance itself.
*   **`defaultStyle`**: (Object) A style object that is applied to every instance on the canvas. Individual instance styles can override these defaults.
*   **`style`**: (Object) A style object applied to the View Canvas component itself, not the instances within it.

#### Transitions and Animations

The View Canvas can automatically animate instances when their position or z-index changes.

*   **`enableTransitions`**: (Boolean) A master switch to turn all animations on or off. Defaults to `true`.
*   **`transitionSettings`**: (Object) An object that defines the animation's behavior.
    *   **`duration`**: (String) The time it takes for the transition to complete (e.g., `"1s"`, `"250ms"`).
    *   **`timingFunction`**: (String) The acceleration curve of the animation. Common values include `"linear"`, `"ease"`, `"ease-in"`, `"ease-out"`, and `"ease-in-out"`.
    *   **`delay`**: (String) An optional delay before the transition begins (e.g., `"500ms"`).

Transitions are applied **only** when the `top`, `left`, `bottom`, `right`, or `zIndex` properties of an instance are changed.

#### Events

The View Canvas has one primary event:

*   **`onInstanceClicked`**: This event fires when a user clicks on any View instance within the canvas.
    *   The `event` object provides contextual information about the clicked instance, including:
        *   `event.index`: The index of the clicked instance within the `props.instances` array.
        *   `event.path`: The view path of the instance.
        *   `event.params`: The view parameters of the instance.
        *   `event.position`: An object containing the `{top, left, bottom, right}` position values.
        *   `event.size`: An object containing the `{width, height}` of the instance.

#### Scripting

*   The View Canvas component has **NO** built-in component functions or extension functions for adding, removing, or modifying instances.
*   All modifications must be done by scripting changes to the `props.instances` array directly. For example, to add a new view, you must append a new instance object to the array. To remove one, you must remove the corresponding object from the array.

### Helpful Tips & Best Practices

*   **Manipulate the Array:** Remember that all changes to the canvas content are done by modifying the `self.props.instances` array in a script. There are no functions like `self.addInstance()`. Use standard array manipulation methods.
*   **Positioning is Key:** Understanding the difference between `position: "absolute"` and `position: "relative"` is critical for achieving your desired layout. Most free-form canvas layouts will primarily use `absolute` positioning.
*   **Mind the Precedence:** When positioning, `left` takes precedence over `right`, and `top` takes precedence over `bottom` if the instance size is not fixed. If your `right` or `bottom` properties seem to be ignored, check the `width`/`height` and `left`/`top` properties.
*   **CSS Units are Mandatory:** All position and size properties (`top`, `left`, `width`, `height`, etc.) require a string with a unit, such as `"100px"` or `"10rem"`. A raw number like `100` will not work.
*   **Styling Hierarchy:** Remember the style precedence: `instance.style` (most specific) overrides `props.defaultStyle`, which is applied to all instances. The main `props.style` property styles the canvas container itself.
*   **Global Size Override:** Be aware that `props.useDefaultViewWidth` and `props.useDefaultViewHeight` are global settings that will override any `width` and `height` you have set on individual instances.
*   **Animated Properties:** Transitions only apply to changes in `top`, `left`, `bottom`, `right`, and `zIndex`. Changing other properties like `viewPath` or `style` will happen instantly without animation.
*   **Leverage `onInstanceClicked`:** The `onInstanceClicked` event is your primary tool for interactivity. You can get the `event.index` of a clicked instance and use that index to target it in a script to modify its properties (e.g., `self.props.instances[event.index].width = "300px"`).

# Schema - raw
{"schema":{"type":"object","properties":{"instances":{"type":"array","items":{"type":"object","default":{"bottom":"auto","right":"auto","viewPath":"","top":"0px","left":"0px","width":"auto","style":{"classes":""},"position":"absolute","viewParams":{},"height":"auto","zIndex":"auto"},"additionalProperties":false,"properties":{"bottom":{"description":"Bottom position of this instance. If top and bottom are set, both are honored if position is absolute and height is not restricted (auto or 100%); otherwise, top takes precedence and bottom is ignored.","$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"right":{"description":"Right position of this instance. If left and right are set, both are honored if position is absolute and width is not restricted (auto or 100%); otherwise, left takes precedence and bottom is ignored.","$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"viewPath":{"format":"view-path","description":"View path of this instance","type":"string"},"top":{"description":"Top position of this instance","$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"left":{"description":"Left position of this instance","$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"width":{"description":"Width of this instance","$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"position":{"description":"Determines how the instance is positioned in the canvas. Absolute: final position is offset from origin of View Canvas by declared top, left, bottom, right properties. Relative: final position is offset from bottom left of previous relative instance by declared top, left, bottom, right properties, or the origin of the View Canvas if this is the first relative instance.","type":"string","enum":["relative","absolute"]},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"description":"Parameters for this instance","type":"object"},"zIndex":{"pattern":"^(auto|0)$|^[-]?[1-9]+[0-9]*","description":"Z-index position of this instance","type":["string","number"]},"height":{"description":"Height of this instance","$ref":"urn:ignition-schema:schemas/css-length.schema.json"}}}},"defaultStyle":{"description":"Default style applied to all view instances","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"useDefaultViewWidth":{"description":"Use of view's default width instead of adjusting based on the content's width. This will override any width settings defined on an instance.","type":"boolean","default":true},"transitionSettings":{"type":"object","example":{"timingFunction":"linear","duration":"1s"},"default":{},"additionalProperties":false,"properties":{"timingFunction":{"description":"Mathematical function that describes how fast one-dimensional values change","type":"string"},"duration":{"description":"Duration of the transition","$ref":"urn:ignition-schema:schemas/css-time.schema.json"},"delay":{"description":"Delay of the transition before it begins","$ref":"urn:ignition-schema:schemas/css-time.schema.json"}}},"enableTransitions":{"description":"Determines whether transitions should play when transitions are defined","type":"boolean","default":true},"useDefaultViewHeight":{"description":"Use of view's default height instead of adjusting based on the content's height. This will override any height settings defined on an instance.","type":"boolean","default":true},"style":{"default":{"classes":"","overflow":"auto"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"ViewCanvas","name":"View Canvas","palette":{"variants":[{"tooltip":"Display multiple Perspective views, each positioned on a coordinate based system.","label":"View Canvas"}],"category":"embedding"},"id":"ia.display.viewcanvas","events":[{"schema":{"description":"This event is fired when the user clicks on a view instance.","type":"object","properties":{"index":{"description":"The index of the view instance.","type":"integer"},"params":{"description":"The current view parameters of the instance.","type":"object"},"path":{"description":"The path of the view that is embedded in the instance.","type":"string"},"size":{"description":"The size of the view instance.","type":"object","properties":{"width":{"description":"Width of the view instance.","type":"number"},"height":{"description":"Height of the view instance.","type":"number"}}},"position":{"description":"The position of the view instance in relation to the canvas.","type":"object","properties":{"bottom":{"description":"Bottom position of the view instance.","type":"number"},"right":{"description":"Bottom position of the view instance.","type":"number"},"top":{"description":"Bottom position of the view instance.","type":"number"},"left":{"description":"Left position of the view instance.","type":"number"}}}}},"documentationUrl":"https://links.inductiveautomation.com/81-view-canvas-component-events","name":"onInstanceClicked"}]}