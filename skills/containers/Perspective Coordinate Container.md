# Perspective Coordinate Container

## Description

This documentation describes the usage and configuration of the Perspective Coordinate Container, which is used to precisely control the position and size of child components. It explains how to build layouts using either a fixed pixel-based mode for static diagrams or a responsive percentage-based mode for scalable designs. The guide also covers creating complex visuals by layering and rotating components, as well as drawing interactive vector pipes to represent connections.

## Documentation

# Instructions
# Instructions for Perspective Coordinate Container

## Core Concept
The **Perspective Coordinate Container** is a container type in Ignition Perspective that allows you to place child components at specific coordinates within its boundaries. Its primary purpose is to control the exact size and location of its children, allowing for effects like overlapping components (placing one on top of another on the z-axis) or creating complex diagrams where components must maintain a fixed position relative to each other.

The container has two fundamental operating modes that dictate how child components are sized and positioned: **`fixed`** and **`percent`**.

---

## Container Properties (`props`)
These properties belong to the Coordinate Container itself.

### `mode`
This is the most important property of the Coordinate Container. It determines the coordinate system used for all child components.
- **Type**: `string`
- **Options**:
    - **`"fixed"` (Default)**: In this mode, the position (`x`, `y`) and size (`width`, `height`) of child components are defined in absolute pixel values. The layout is static and does not change when the container is resized.
    - **`"percent"`**: In this mode, the position and size of child components are defined as a percentage of the container's total dimensions. This allows components to scale and reposition proportionally as the container is resized.

### `aspectRatio`
This property is **only** used when `mode` is set to `"percent"`. It forces the container to maintain a specific aspect ratio as it resizes.
- **Type**: `string`
- **Format**: A string in `"x:y"` format (e.g., `"16:9"`, `"1:1"`, `"4:3"`).
- **Default**: If the value is missing or invalid, it defaults to `"1:1"`.

### `style`
This property allows you to apply custom CSS styling to the container itself, such as background colors, borders, etc.
- **Type**: `object`

### `pipes`
This property allows you to draw vector-based pipes within the container. Pipes are useful for creating P&ID diagrams or showing connections between components. It is an array of pipe objects.
- **Type**: `array` of `objects`
- **Pipe Object Properties**:
    - **`name`**: A unique name for the pipe, which can be useful for identification in the Project Browser or in scripting.
    - **`appearance`**: Defines the visual style of the pipe. The selected style determines which other properties are available.
        - **`"auto"` (Default)**: Uses the session property `pipes.autoAppearance`. Defaults to `mimic` if not defined.
        - **`"p&id"`**: A style for Process and Instrumentation Diagrams.
        - **`"mimic"`**: A style that mimics a physical pipe.
        - **`"simple"`**: A basic line style.
    - **`origin`**: A `point` object that defines the starting point of the pipe. A `point` object has `x`, `y`, and `connections` properties. The `connections` property is an array of other `point` objects, forming the segments of the pipe.
    - **`width`**: The thickness of the pipe line.
    - **`stroke`**: The color of the pipe's line/outline.
    - **`fill`**: The fill color of the pipe. Only applicable when `appearance` is `mimic`, `simple`, or `auto` resolving to one of them.
    - **`flanges`**: If `true`, displays flanges at the ends and connection points of the pipe. Only applicable when `appearance` is `mimic` or `auto` resolving to it.
    - **`start`**: Draws a decoration (e.g., an arrowhead) at the pipe's origin. Only applicable when `appearance` is `p&id` or `auto` resolving to it.
    - **`end`**: Draws a decoration at the end of terminal pipe segments. Only applicable when `appearance` is `p&id` or `auto` resolving to it.
    - **`lineVariant`**: Changes the line style (e.g., solid, dashed). Only applicable when `appearance` is `p&id` or `auto` resolving to it.

---

## Child Component Position Properties
When you place a component inside a Coordinate Container, it gains the following `position` properties. The interpretation of these properties depends entirely on the parent container's `mode`.

### `x` and `y`
Defines the top-left coordinate of the child component.
- **In `fixed` mode**: An absolute CSS length value (e.g., `100px`, `50px`). This represents the distance from the top-left corner of the container.
- **In `percent` mode**: A relative numeric value from 0 to 1. For example, an `x` of `0.25` means the component's left edge will be positioned at 25% of the container's width.

### `width` and `height`
Defines the size of the child component.
- **In `fixed` mode**: An absolute CSS length value (e.g., `150px`, `75px`). The component's size will not change.
- **In `percent` mode**: A relative numeric value representing a percentage of the container's dimensions. For example, a `width` of `0.5` will make the component half as wide as the container.

### `rotate`
This property allows you to rotate the child component.
- **Type**: `object`
- **Properties**:
    - **`angle`**: The rotation angle in CSS units (e.g., `"45deg"`).
    - **`anchor`**: The point around which the rotation occurs, using CSS percentage strings (e.g., `"50% 50%"` for center).

---

## Events

### `onPipeClicked`
This event is fired when a user clicks on one of the pipes defined in the `props.pipes` array.
- **Event Object Properties**:
    - **`pipeName`**: The `name` of the pipe that was clicked.
    - **`pipeIndex`**: The array index of the clicked pipe within `props.pipes`.
    - **`event`**: A mouse event object containing details about the click, such as coordinates (`clientX`, `clientY`) and key states (`ctrlKey`, `shiftKey`).

---

## Big List of Helpful Tips

*   **Mode is Key**: The single most important setting is the `mode` property. Your choice of `"fixed"` or `"percent"` completely changes how the child `x`, `y`, `width`, and `height` properties are interpreted (pixels vs. percentage).
*   **Overlapping is Easy**: This container is the ideal choice when you need to layer components on top of one another. Just place them at the desired coordinates; components with a higher index in the component tree will appear on top.
*   **Use Case - Static Diagrams**: Use `fixed` mode when building a diagram where the elements are individual components and must not resize or move, such as a process diagram or a map.
*   **Use Case - Scalable Layouts**: Use `percent` mode when you want your entire layout to grow and shrink proportionally with the browser window or parent container. Remember to set the `aspectRatio` property in this mode to prevent distortion.
*   **No Automatic Layout**: Unlike Flex or Column containers, the Coordinate Container does **not** automatically arrange components. You are responsible for setting the size and position for every single child component.
*   **Child Position Units**: Be very mindful of the units you are using for child properties based on the container's mode.
    *   `fixed` mode uses CSS length units like `"100px"`.
    *   `percent` mode uses unitless numbers representing a ratio (e.g., `0.5` for 50%).
*   **Pipes for Visualization**: The `pipes` property is for drawing connections and pathways. They are purely visual but can be made interactive using the `onPipeClicked` event.
*   **Pipe Appearance**: The appearance of a pipe is controlled by the `appearance` property. Other properties like `flanges`, `start`, `end`, and `lineVariant` are only visible when the correct `appearance` is selected.
*   **Rotation**: Rotation is applied directly to the child components inside the container, not to the container itself.



# Schema - raw
{"schema":{"type":"object","required":["mode","aspectRatio","style"],"additionalProperties":false,"definitions":{"point":{"description":"An array of pipes points forming a contiguous pipe segment.","type":"object","required":["x","y"],"additionalProperties":false,"properties":{"x":{"type":"Number","default":0},"y":{"type":"Number","default":0},"connections":{"description":"An Array of Points connected to this Point","type":"array","default":[],"items":{"$ref":"#/definitions/point"}}}}},"properties":{"aspectRatio":{"visibleWhen":{"equals":"percent","property":"mode"},"description":"Only applied in 'percent' mode. Dimensions, in 'x:y' format to maintain container aspect ratio for different sizes. Missing or invalid value will default to '1:1'","type":"string","default":""},"mode":{"description":"Whether child layouts should always be in fixed coordinate space, or should stretch relative to different container sizes","type":"string","enum":["fixed","percent"],"default":"fixed"},"style":{"default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"pipes":{"description":"An array of pipes.","type":"array","default":[],"items":{"type":"object","required":["appearance","width","origin"],"default":{"visible":true,"origin":{"x":0,"y":0,"connections":[]},"start":"none","fill":"","stroke":"","appearance":"auto","flanges":true,"width":10,"end":"none","lineVariant":"solid"},"additionalProperties":false,"properties":{"visible":{"description":"Enables pipe visibility.","type":"boolean","default":true},"origin":{"$ref":"#/definitions/point"},"start":{"visibleWhen":{"equals":["auto","p&id"],"property":"appearance"},"description":"Draws a decoration at the Pipe's origin when appearance is p&id, or when auto and Session Prop pipes.autoAppearance is p&id","type":"string","enum":["none","arrowInward","arrowOutward"]},"fill":{"visibleWhen":{"equals":["auto","mimic","simple"],"property":"appearance"},"format":"color","description":"Fill color when appearance is mimic or simple, or when auto and Session Prop pipes.autoAppearance is mimic or simple","type":"string"},"stroke":{"format":"color","description":"Stroke color","type":"string"},"appearance":{"description":"auto uses the value of the Session Prop pipes.autoAppearance if it exists, default is mimic.","type":"string","enum":["auto","p&id","mimic","simple"]},"flanges":{"visibleWhen":{"equals":["auto","mimic"],"property":"appearance"},"description":"Displays flanges at the ends and mid pipe when the appearance is mimic, or when auto and Session Prop pipes.autoAppearance is mimic","type":"boolean"},"name":{"description":"A name to display in the Designer Project browser","type":["number","string"]},"width":{"description":"The width of the pipe","type":"number"},"end":{"visibleWhen":{"equals":["auto","p&id"],"property":"appearance"},"description":"Draws a decoration at the end of Pipe connections without further connections when appearance is p&id, or when auto and Session Prop pipes.autoAppearance is p&id","type":"string","enum":["none","arrowInward","arrowOutward"]},"lineVariant":{"visibleWhen":{"equals":["auto","p&id"],"property":"appearance"},"description":"Changes the line variant when appearance is p&id, or when auto and Session Prop pipes.autoAppearance is p&id. midArrows are dependent on the direction of the start and end arrows, with start taking precedence except for terminal segments","type":"string","enum":["solid","dashed","midArrow","wavy"]}}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"CoordinateContainer","version":1,"name":"Coordinate Container","palette":{"variants":[{"tooltip":"A container that makes a component's size and location relative to its parent's size and location.","label":"Coordinate"},{"tooltip":"A container that makes a component's size and location relative to its parent's size and location.","label":"Fixed","id":"coord-fixed"},{"tooltip":"A container that makes a component's size and location relative to its parent's size and location.","label":"Percent","props":{"mode":"percent"},"id":"coord-percent"}],"category":"container"},"id":"ia.container.coord","childPositionSchema":{"type":"object","required":["x","y"],"default":{"rotate":{"anchor":"50% 50%","angle":"0deg"},"x":0,"y":0},"additionalProperties":false,"properties":{"rotate":{"$ref":"urn:ignition-schema:schemas/css-rotation.schema.json"},"x":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"width":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"y":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"height":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"}}},"events":[{"schema":{"type":"object","properties":{"pipeIndex":{"description":"The array index of the pipe within props.pipes that was clicked.","type":"number"},"event":{"description":"The event object generated from the mouse click.","type":"object","properties":{"buttons":{"description":"The buttons being depressed when the event was fired.","type":"number"},"clientY":{"description":"The Y coordinate in local coordinates.","type":"number"},"clientX":{"description":"The X coordinate in local coordinates.","type":"number"},"ctrlKey":{"description":"True if the 'ctrl' key was held down when the event was fired.","type":"boolean"},"metaKey":{"description":"True if the 'meta' key was held down when the event was fired.","type":"boolean"},"button":{"description":"The button number that was pressed when the event was fired.","type":"number"},"shiftKey":{"description":"True if the 'shift' key was held down when the event was fired.","type":"boolean"},"altKey":{"description":"True if the 'alt' key was held down when the event was fired.","type":"boolean"},"pageY":{"description":"The Y coordinate relative to the whole document.","type":"number"},"pageX":{"description":"The X coordinate relative to the whole document.","type":"number"},"screenX":{"description":"The X coordinate in global (screen) coordinates.","type":"number"},"screenY":{"description":"The Y coordinate in global (screen) coordinates.","type":"number"}}},"pipeName":{"description":"The name of the pipe that was clicked.","type":"string"}}},"documentationUrl":"https://links.inductiveautomation.com/81-coordinate-container-component-events","description":"Interaction event fired when a pipe is clicked.","name":"onPipeClicked"}]}