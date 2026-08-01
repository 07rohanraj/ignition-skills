# Perspective Flex Repeater Component

## Description

The usage and configuration of the Perspective Flex Repeater component, which dynamically generates and arranges multiple instances of a template View based on a provided data set. These instructions detail the process of linking a template, providing instance data, and utilizing flexbox properties to control the layout, alignment, sizing, and styling of the repeated elements.

## Documentation

# Instructions
This document provides a detailed guide for using the Perspective Flex Repeater component in Ignition.

### Core Concept

The Flex Repeater component is a powerful tool for displaying dynamic collections of data. Its primary function is to take a single "template" View and a list of data objects, and then create and display an instance of that template View for each object in the list. It uses a flexbox layout model to arrange these instances, providing a high degree of control over alignment, spacing, and wrapping.

### Instructions for Use

#### 1. Basic Setup

1.  **Create a Template View**: First, design the View that you want to be repeated. This View will serve as the template for each instance. It is crucial to define View Parameters (in the `PARAMS` section of the View editor) on this template View. These parameters will receive data from the Flex Repeater. For example, if you want each repeated instance to show a different name and value, you might create `name` and `value` parameters on your template View.
2.  **Add a Flex Repeater**: Drag a Flex Repeater component from the Component Palette onto your main View.
3.  **Set the Path**: In the Property Editor for the Flex Repeater, set the `path` property to the file path of the template View you created in step 1.
4.  **Provide Instances Data**: The `instances` property is the most important property. It is an array of objects, where each object in the array corresponds to one repeated instance of your template View.
    *   The property names inside each object in the `instances` array should **exactly match** the names of the `PARAMS` you created on your template View. The repeater will automatically pass the values to the corresponding parameters.
    *   **Example**: If your template View has params `name` and `value`, your `instances` property might look like this:
        ```json
        [
          {"name": "Motor 1", "value": 150},
          {"name": "Motor 2", "value": 175},
          {"name": "Motor 3", "value": 162}
        ]
        ```
        This will create three instances of your template View, each with its own `name` and `value`.

#### 2. Layout and Positioning (Flex Properties)

The Flex Repeater uses a flexbox model. This involves a **main axis** and a **cross axis**.

*   `direction`: Defines the main axis.
    *   `row` (default): Main axis is horizontal, left-to-right.
    *   `row-reverse`: Main axis is horizontal, right-to-left.
    *   `column`: Main axis is vertical, top-to-bottom.
    *   `column-reverse`: Main axis is vertical, bottom-to-top.
*   `justify`: Adjusts the spacing and alignment of instances along the **main axis**.
    *   `flex-start` (default): Packs items toward the start of the `direction`.
    *   `flex-end`: Packs items toward the end.
    *   `center`: Packs items toward the center.
    *   `space-between`: Distributes items evenly, with the first item at the start and the last item at the end.
    *   `space-around`: Distributes items evenly with half-sized spaces at each end.
    *   `space-evenly`: Distributes items evenly with equal space between them and at the ends.
*   `alignItems`: Adjusts the alignment of instances along the **cross axis**.
    *   `stretch` (default): Stretches items to fill the container's cross-axis size.
    *   `flex-start`: Aligns items to the start of the cross axis.
    *   `flex-end`: Aligns items to the end of the cross axis.
    *   `center`: Aligns items to the center of the cross axis.
    *   `baseline`: Aligns items based on their text baseline.
*   `wrap`: Determines what happens when the instances run out of space on a single line.
    *   `nowrap` (default): All items are forced onto a single line, potentially overflowing the container.
    *   `wrap`: Items will wrap onto a new line if needed.
    *   `wrap-reverse`: Items will wrap onto a new line in the opposite direction.
*   `alignContent`: When `wrap` is active and there are multiple lines of content, this property aligns the entire block of lines within the container. It has no effect when there is only one line.

#### 3. Sizing the Repeated Instances

There are two primary ways to control the size of the repeated views:

1.  **Using the View's Default Size**:
    *   `useDefaultViewWidth`: (Default: `true`) When `true` and `direction` is `row` or `row-reverse`, the instance will use the width defined in the template View's own properties. Flex sizing properties (`grow`, `shrink`, `basis`) will be ignored.
    *   `useDefaultViewHeight`: (Default: `true`) When `true` and `direction` is `column` or `column-reverse`, the instance will use the height defined in the template View's own properties. Flex sizing properties will be ignored.
    *   **To enable dynamic flex sizing, you must set these properties to `false`.**

2.  **Using Flex Sizing Properties**:
    These properties are configured within the `elementPosition` property (for all instances) or `instancePosition` (for a single instance). This is only effective if `useDefaultViewWidth`/`useDefaultViewHeight` are `false`.
    *   `basis`: The default size of an element before remaining space is distributed.
    *   `grow`: A number defining the ability for an element to grow if there is extra space. A value of `1` means it will take up an equal share of the extra space. A value of `0` means it will not grow.
    *   `shrink`: A number defining the ability for an element to shrink if there is not enough space.

#### 4. Styling

There are three levels of styling, which allows for both uniform and specific styling.

1.  `style`: This styles the Flex Repeater **container itself**. Use this to set properties like the container's border, background color, or overflow behavior.
2.  `elementStyle`: This is a base style applied to **every repeated instance**. Use this to set a common look and feel, like a border or padding for all instances.
3.  `instanceStyle`: This is a style applied to **one specific instance**, overriding any conflicting styles from `elementStyle`. This property is configured *inside* an object in the `instances` array. Use this to highlight a specific instance, for example, by giving it a different background color based on its data.

**Example `instances` with `instanceStyle`:**
```json
[
  {"name": "Motor 1", "value": 150, "instanceStyle": {"backgroundColor": "#C8F7C8"}},
  {"name": "Motor 2", "value": 175, "instanceStyle": {"backgroundColor": "#C8F7C8"}},
  {"name": "Motor 3", "value": 210, "instanceStyle": {"backgroundColor": "#F7C8C8", "border": "2px solid red"}}
]
```

---

### Big List of Helpful Tips

*   **My instances won't resize!** The most common reason for this is the `useDefaultViewWidth` and `useDefaultViewHeight` properties. They are `true` by default. If you want to use flex properties like `grow`, `shrink`, and `basis` to control sizing, you **must set these to `false`**.
*   **Passing Data is Key**: The core pattern is to define `PARAMS` on your template view and then match those param names with property keys in the objects inside the `instances` array.
*   **Dynamic Instances**: The `instances` property can be bound to a database query or a script transform. This allows you to dynamically generate repeated views from any data source. For example, you can run a query to get a list of equipment and bind the result to `instances` to create a status display for each piece of equipment.
*   **Individual Overrides**: To make one specific instance look or behave differently, add `instanceStyle` or `instancePosition` properties to its corresponding object in the `instances` array. This is how you apply unique styles or sizing to a single repeated view.
*   **Main Axis vs. Cross Axis**: Remember that `justify` always applies to the main axis (`direction`), and `alignItems` applies to the cross axis. If you change `direction` from `row` to `column`, the main axis becomes vertical, and the cross axis becomes horizontal.
*   **Spacing Between Items**: Use the `justify` property with values like `space-between`, `space-around`, or `space-evenly` to create space between elements along the main axis. For spacing on the cross-axis, or for more complex spacing, use margins within the `elementStyle` property.
*   **Container Styling vs. Element Styling**: Do not confuse the `style` property (which styles the repeater component itself) with the `elementStyle` property (which styles the repeated views inside).
*   **Performance**: For repeaters with many instances, the `loading.order` property can be useful. The default, `after-parent`, improves the initial load time of the parent View. `with-parent` loads everything at once.
*   **Palette Shortcuts**: When dragging the Flex Repeater onto a view, you can choose the "Row" or "Column" variants, which are shortcuts that pre-configure the `direction` property for you.

# Schema - raw
{"schema":{"type":"object","definitions":{"elementPosition":{"additionalProperties":false,"properties":{"grow":{"type":"number"},"shrink":{"type":"number"},"basis":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"align":{"type":"string","enum":["auto","flex-start","flex-end","center","baseline","stretch"]}}}},"properties":{"alignItems":{"description":"Adjusts placement of repeated views along the cross axis when there is extra space.","type":"string","enum":["flex-start","flex-end","center","baseline","stretch"],"default":"stretch"},"instances":{"description":"List of params for each rendered view. Each instance will contain an instanceStyle and instancePosition property. Changing these properties will override the styling and positioning applied by elementStyle and elementPosition.","type":"array","default":[],"items":{"extension":{"view-params":{"path":"/path"}},"type":"object","additionalProperties":true,"properties":{"instanceStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"instancePosition":{"default":{},"$ref":"#/definitions/elementPosition"}}}},"elementPosition":{"description":"Flex position properties that are applied to all repeated views.","default":{"grow":1,"shrink":1,"basis":0},"$ref":"#/definitions/elementPosition"},"useDefaultViewWidth":{"description":"Use of view's default width instead of adjusting based on the content's width. This will override all flex position properties in the row and row-reverse direction.","type":"boolean","default":true},"loading":{"type":"object","properties":{"order":{"description":"Controls when the embedded views load: after the parent is displayed or combined with the parent view loading","type":"string","enum":["after-parent","with-parent"],"default":"after-parent"}}},"alignContent":{"description":"Adjusts alignment of repeated views when there is free space in the cross axis.","type":"string","enum":["flex-start","flex-end","center","space-between","space-around","stretch"],"default":"stretch"},"path":{"format":"view-path","description":"Path of the view to display","type":"string","default":""},"justify":{"description":"Adjusts placement of repeated views along the main axis when there is extra space, which may be used to fill areas before, after or in-between.","type":"string","enum":["flex-start","flex-end","center","space-between","space-around","space-evenly"],"default":"flex-start"},"elementStyle":{"description":"Style properties that are applied to all repeated views.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"useDefaultViewHeight":{"description":"Use of view's default height instead of adjusting based on the content's height. This will override all flex position properties in the column and column-reverse direction.","type":"boolean","default":true},"style":{"default":{"classes":"","overflow":"auto"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"wrap":{"description":"Whether the container should allow repeated views to wrap to next line if space has run out.","type":"string","enum":["nowrap","wrap","wrap-reverse"],"default":"nowrap"},"direction":{"description":"Direction of layout of repeated views.","type":"string","enum":["row","row-reverse","column","column-reverse"],"default":"row"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"FlexRepeater","name":"Flex Repeater","palette":{"variants":[{"tooltip":"Creates multiple instances of views for display in another view.","label":"Flex Repeater"},{"tooltip":"Creates multiple instances of views for display in another view.","label":"Row","props":{"direction":"row"},"id":"flex-repeater-row"},{"tooltip":"Creates multiple instances of views for display in another view.","label":"Column","props":{"direction":"column"},"id":"flex-repeater-column"}],"category":"embedding"},"id":"ia.display.flex-repeater"}