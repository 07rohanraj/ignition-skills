# Perspective Column Container

## Description

These instructions describe the configuration and use of the Perspective Column Container for creating responsive, screen-size-aware layouts. It explains how to organize child components into a dynamic 12-column grid by defining width-based breakpoints on the container and then configuring each child's specific size and position to adapt automatically at each of those breakpoints.

## Documentation

# Instructions
### Instructions for the LLM

#### Object Name
Perspective Column Container

#### Core Functionality
The Perspective Column Container is a responsive container that organizes child components into a 12-column grid. Its primary feature is the ability to automatically change the layout of its children based on its own width. This is achieved using "breakpoints," which are specific width thresholds. For each breakpoint, you can define a unique size and position for every child component, allowing you to create dynamic and screen-size-aware designs.

---

### Container Properties (`props`)

These properties are configured on the Column Container component itself.

1.  **`breakpoints`**:
    *   **Purpose**: This is the most important property. It defines the different width thresholds that will trigger layout changes.
    *   **Type**: An array of objects.
    *   **Default**: The container comes with three default breakpoints:
        *   `{ "name": "sm", "minWidth": 0 }`
        *   `{ "name": "md", "minWidth": 480 }`
        *   `{ "name": "lg", "minWidth": 996 }`
    *   **How it Works**: The container checks its current width against the `minWidth` of each breakpoint. It will apply the layout rules associated with the largest breakpoint whose `minWidth` is less than or equal to the container's current width.
        *   For example, with the default settings:
            *   If the container width is `0px` to `479px`, the `sm` breakpoint is active.
            *   If the container width is `480px` to `995px`, the `md` breakpoint is active.
            *   If the container width is `996px` or more, the `lg` breakpoint is active.
    *   **Configuration**: Each object in the array must have two keys:
        *   `name` (string): A unique identifier for the breakpoint (e.g., "small", "tablet", "desktop"). This name is used to link child component settings to a specific breakpoint.
        *   `minWidth` (number): The minimum width, in pixels, at which this breakpoint becomes active.

2.  **`gutters`**:
    *   **Purpose**: Defines the amount of empty space between the child components within the container.
    *   **Type**: An object with two properties.
    *   **Default**: `{ "vertical": 10, "horizontal": 10 }`
    *   **Configuration**:
        *   `vertical` (number): The space in pixels above and below each component.
        *   `horizontal` (number): The space in pixels to the left and right of each component.

3.  **`style`**:
    *   **Purpose**: Standard Perspective styling properties for the container itself (e.g., background color, border).

---

### Child Component Properties (`position`)

When a component is placed inside a Column Container, it gains a new set of `position` properties. This is where you define how that specific child should behave at each of the container's breakpoints.

1.  **`breakpoints`**:
    *   **Purpose**: This property on the child holds all the layout rules for that child.
    *   **Type**: An array of objects.
    *   **Configuration**: You must create one object in this array for *each breakpoint* defined on the parent container. Each object specifies the child's layout for that corresponding breakpoint.
        *   `name` (string): **CRITICAL:** This must exactly match the `name` of a breakpoint from the parent container's `props.breakpoints` array.
        *   `span` (number): The number of columns (out of 12) that the component will occupy. This determines the component's width.
        *   `rowIndex` (number): The row (starting from 0) in which to place the component. All components with the same `rowIndex` are considered part of the same row.
        *   `colIndex` (number): The column number (starting from 0) where the component will begin.
        *   `order` (number): Controls the placement order of components *within the same row*. Lower numbers appear first (to the left). This is for fine-tuning the visual order of siblings in a row.

2.  **`height`**:
    *   **Purpose**: Defines the height of the child component. The row's height will automatically adjust to accommodate the tallest component within it.
    *   **Type**: A string representing a CSS length.
    *   **Examples**: `"100px"`, `"50%"`, or `"auto"`. Using `"auto"` is common, as it allows the component's content (like text) to determine its height.

---

### Helpful Tips & Best Practices

*   **Match Breakpoint Names**: The `name` value in a child's `position.breakpoints` object *must* be identical to a `name` in the container's `props.breakpoints` array. A mismatch will cause the layout rules for that breakpoint to be ignored for that child.
*   **Configure All Breakpoints**: For the most predictable and reliable responsive behavior, ensure every child component has a defined configuration object for every single breakpoint set on the container.
*   **The 12-Column Rule**: The total `span` of all components within the same `rowIndex` should ideally add up to 12 or less. If the total span exceeds 12, components will wrap onto a new line within that same logical row.
*   **Use `rowIndex` for Structure**: To create distinct rows that do not interact with each other's layout, assign different `rowIndex` values to your components.
*   **`colIndex` Starts at 0**: Remember that the grid is 0-indexed, so the first column is `colIndex: 0` and the last is `colIndex: 11`.
*   **`order` for Reordering**: The `order` property is useful when you want to change the visual sequence of components at different breakpoints without changing their `colIndex`. For example, two components could be `A | B` on a large screen but `B | A` on a small screen.
*   **`auto` Height is Powerful**: Setting a child's `height` to `"auto"` is very useful for components whose content size might change, like labels or text areas. The row will grow vertically to prevent the content from being cut off.
*   **Gutters are Global**: The `gutters` property on the container applies uniformly to all children. You cannot specify different gutters for different components.

# Schema - raw
{"schema":{"type":"object","required":["breakpoints","gutters","style"],"additionalProperties":false,"properties":{"gutters":{"description":"Amount of space, in pixels, to place between child components","type":"object","required":["vertical","horizontal"],"default":{"vertical":10,"horizontal":10},"additionalProperties":false,"properties":{"vertical":{"type":"number"},"horizontal":{"type":"number"}}},"style":{"default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"breakpoints":{"description":"Width breakpoints declarations for child layouts. When container is sized below minWidth, child position rules will fall back to the next set breakpoint rules","type":"array","default":[{"minWidth":0,"name":"sm"},{"minWidth":480,"name":"md"},{"minWidth":996,"name":"lg"}],"items":{"type":"object","required":["name","minWidth"],"default":{"minWidth":0,"name":""},"additionalProperties":false,"properties":{"minWidth":{"type":"number"},"name":{"type":"string"}}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"ColumnContainer","name":"Column Container","palette":{"variants":[{"tooltip":"A 12 column grid layout in which components can be organized. The columns that alter their layout depending on screen viewport size.","label":"Column"}],"category":"container"},"id":"ia.container.column","childPositionSchema":{"type":"object","required":["breakpoints"],"additionalProperties":false,"properties":{"breakpoints":{"type":"array","default":[],"items":{"type":"object","required":["name","span","rowIndex","colIndex","order"],"additionalProperties":false,"properties":{"name":{"description":"Name of a breakpoint defined in container. If this matches the currently applied breakpoint, these rules determine child layout.","type":"string"},"colIndex":{"description":"Column number upon which the child's span should begin unless forced to wrap.","type":"number","default":0},"rowIndex":{"description":"Row index (starting from 0) in which to place child. Children may wrap lines within a row. Children in separate rows don't affect each other's layout","type":"number","default":0},"span":{"description":"Number of columns the child's width will span.","type":"number"},"order":{"description":"Where component is placed among its siblings within its row. Ordering is independent per row.","type":"number"}}}},"height":{"description":"Component height. Rows adjust height to accommodate components. Use 'auto' to let component content (such as text) dictate height.","$ref":"urn:ignition-schema:schemas/css-length.schema.json"}}}}