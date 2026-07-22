# Perspective Accordion Component

## Description

This document details the configuration and usage of the Perspective Accordion component. It explains how to build the component's structure by defining each expandable section's header and body content, control expansion behavior, and utilize events to create dynamic, interactive lists.

## Documentation

# Instructions
# Object Name
Perspective Accordion Component

# Object Purpose
The Perspective Accordion component is a container used to display a list of items in an expandable/collapsible manner. Each item has a header and a body. Clicking or tapping the header toggles the visibility of the body content. This component is ideal for organizing and presenting large amounts of information in a compact space, allowing users to focus on one section at a time or view multiple sections as needed. The content for both the header and the body is typically a separate Ignition Perspective View.

# How to Use This Object
The fundamental structure of the Accordion component is configured through its `items` property, which is an array of objects. Each object in the array represents one collapsible section of the Accordion.

### Basic Configuration
1.  **Add Items**: To create sections in the Accordion, you need to add objects to the `items` array property. Each object you add will create a new header/body pair.
2.  **Configure Each Item**: For each item in the array, you must configure its `header` and `body`.

### Configuring the `body`
The `body` of an accordion item is where the main content is displayed when the item is expanded. The content of a body is always an embedded Perspective View.
*   **`body.viewPath`**: This is a **required** property. You must provide the path to the View you want to embed in the body section (e.g., `MyProject/MyBodyView`).
*   **`body.viewParams`**: If the View specified in `viewPath` has parameters, you can pass values to them using this object. The keys in the `viewParams` object must exactly match the names of the parameters defined in the target View.
*   **`body.height`**: Controls the height of the body area. It can be set to `"auto"` to resize based on content, or a specific value (e.g., `"200px"`).
*   **`body.style`**: Apply specific CSS styles to the body's container.

### Configuring the `header`
The `header` is the clickable area that toggles the visibility of the `body`. It can contain either simple text or an embedded View.
*   **`header.content.type`**: Determines the content of the header. Set to `"text"` for simple text or `"view"` to embed a View.
    *   If `type` is `"text"`, set the **`header.content.text`** property to the string you want to display.
    *   If `type` is `"view"`, set the **`header.content.viewPath`** property to the path of the View to use as the header. You can also pass parameters via **`header.content.viewParams`**.
*   **`header.toggle`**: This object configures the expand/collapse icon.
    *   **`toggle.enabled`**: A boolean that shows or hides the toggle icon.
    *   **`toggle.expandedIcon`** and **`toggle.collapsedIcon`**: Configure the icon to display for each state. You can change the `path`, `color`, and `style` of the icon.
*   **`header.reverse`**: A boolean that, when true, reverses the order of the header content and the toggle icon, placing the icon on the left.
*   **`header.height`**: Sets the height of the header.

### Controlling Expansion Behavior
*   **`expansionMode`**: This top-level property controls how many items can be expanded at once.
    *   `"multiple"` (default): Allows users to have any number of items expanded simultaneously.
    *   `"single"`: Only one item can be expanded at a time. Expanding a new item will automatically collapse the previously expanded one.
*   **`items.expanded`**: This boolean property exists on each individual item object.
    *   It controls whether an item is currently expanded or collapsed.
    *   It is a read/write property. You can bind it to a tag or another property to control the state of the item programmatically, or you can read its value to know if an item is open.

### Events
The Accordion component has two main events that you can use to trigger scripts:
*   **`onItemExpanded`**: Fires when an item's body is expanded.
*   **`onItemCollapsed`**: Fires when an item's body is collapsed.
*   Both events provide an `index` property in the event object (`event.index`), which tells you the zero-based index of the item that was acted upon.

# Important Tips and Best Practices
*   **Primary Configuration**: Remember that almost all configuration happens within the `items` property array. The Accordion's functionality is defined by the list of item objects within it.
*   **View Paths are Crucial**: Always double-check your View paths in `body.viewPath` and `header.content.viewPath`. An incorrect path will result in the View not loading.
*   **Dynamic Content with `viewParams`**: To make your embedded Views reusable and dynamic, define parameters on them and pass data using the `viewParams` object in the Accordion's item configuration. The keys used in the `viewParams` object must be identical to the parameter names on the target View.
*   **Programmatic Control**: Use the `items.expanded` property for each item to control its state. For example, you could have a button outside the Accordion that sets `items[0].expanded` to `true` to open the first item.
*   **Dynamic Accordions**: The entire `items` property can be bound to a property or a script transform. This is a powerful technique for creating Accordions with a variable number of items based on a database query or other data source. For example, you can use a script transform to build the array of item objects from a list of equipment.
*   **Choose the Right `expansionMode`**: Use `"single"` mode when you want the user to only focus on one piece of content at a time. Use `"multiple"` mode when comparing or viewing information from several sections at once is useful.
*   **Leverage Events**: Use the `onItemExpanded` and `onItemCollapsed` events to perform actions in response to user interaction. For example, you could use `onItemExpanded` to trigger a script that logs the action or queries a database for fresh data to display in the item's View. Remember to use `event.index` to identify which item was affected.
*   **Flexible Headers**: Don't forget that a header can be a View itself. This allows for very rich headers that can include their own graphics, data points, and buttons, rather than just simple text.
*   **Styling Granularity**: Style properties (`style`) are available at multiple levels: on the main Accordion component, on each item's `header`, and on each item's `body`. This allows for precise control over the component's appearance.

# Schema - raw
{"schema":{"type":"object","required":["expansionMode","items"],"properties":{"expansionMode":{"type":"string","enum":["single","multiple"],"default":"multiple"},"unusedSpaceStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"items":{"description":"Accordion items.","type":"array","items":{"type":"object","required":["expanded","header","body"],"properties":{"body":{"type":"object","required":["viewPath"],"default":{"useDefaultViewWidth":false,"viewPath":"","useDefaultViewHeight":false,"style":{"margin":"16px","classes":""},"viewParams":{},"height":"auto"},"properties":{"useDefaultViewWidth":{"description":"Use of view's default width instead of adjusting based on the content's width.","type":"boolean"},"viewPath":{"format":"view-path","description":"Path of view to display","type":"string"},"useDefaultViewHeight":{"description":"Use of view's default height instead of adjusting based on the content's height.","type":"boolean"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"description":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","type":"object"},"height":{"description":"The height of the body.","oneOf":[{"pattern":"^(auto|0)$|^[+-]?[0-9]+.?([0-9]+)?(px|em|ex|%|in|cm|mm|pt|pc|rem)$","type":"string"},{"type":"number"}]}}},"expanded":{"description":"Is the accordion body expanded.  This property is both read and written to.","type":"boolean","default":false},"header":{"description":"Accordion header configuration.","type":"object","required":["toggle","content"],"default":{"toggle":{"enabled":true,"collapsedIcon":{"color":"","path":"material/expand_more","style":{"classes":""}},"expandedIcon":{"color":"","path":"material/expand_less","style":{"classes":""}}},"reverse":false,"content":{"useDefaultViewWidth":false,"type":"text","viewPath":"","useDefaultViewHeight":false,"style":{"classes":""},"text":"","viewParams":{}},"style":{"classes":""},"height":"40px"},"properties":{"toggle":{"description":"Toggle configuration","type":"object","required":["enabled"],"properties":{"enabled":{"description":"Enables the collapse and expand toggle.","type":"boolean"},"collapsedIcon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"expandedIcon":{"$ref":"urn:ignition-schema:schemas/icon-schema.json"}}},"reverse":{"description":"Reverses the order of the toggle and header content.","type":"boolean"},"content":{"type":"object","required":["viewPath"],"additionalProperties":false,"properties":{"useDefaultViewWidth":{"visibleWhen":{"equals":"view","property":"type"},"description":"Use of view's default width instead of adjusting based on the content's width.","type":"boolean"},"type":{"description":"Whether text or a view will be rendered in this accordion header","type":"string","enum":["text","view"],"default":"view"},"viewPath":{"visibleWhen":{"equals":"view","property":"type"},"format":"view-path","description":"Path to view to render in this accordion header","type":"string"},"useDefaultViewHeight":{"visibleWhen":{"equals":"view","property":"type"},"description":"Use of view's default height instead of adjusting based on the content's height.","type":"boolean"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"visibleWhen":{"equals":"text","property":"type"},"description":"Text to display for this accordion header","type":["string","number"]},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"visibleWhen":{"equals":"view","property":"type"},"description":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","type":"object"}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"height":{"description":"The height of the header.","oneOf":[{"pattern":"^(auto|0)$|^[+-]?[0-9]+.?([0-9]+)?(px|em|ex|%|in|cm|mm|pt|pc|rem)$","type":"string"},{"type":"number"}]}}}}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Accordion","name":"Accordion","palette":{"variants":[{"tooltip":"Enables the embedding of expandable/collapsible views that can be toggled with a click or a tap of their headers.","label":"Accordion"}],"category":"embedding"},"id":"ia.display.accordion","events":[{"schema":{"type":"object","properties":{"index":{"description":"The index of the item that was expanded.","type":"number"}}},"documentationUrl":"https://links.inductiveautomation.com/81-accordion-component-events","description":"This event is fired when an item is expanded.","name":"onItemExpanded"},{"schema":{"type":"object","properties":{"index":{"description":"The index of the item that was expanded.","type":"number"}}},"documentationUrl":"https://links.inductiveautomation.com/81-accordion-component-events","description":"This event is fired when an item is collapsed.","name":"onItemCollapsed"}]}