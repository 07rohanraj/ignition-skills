# Perspective Tag Browse Tree Component

## Description

This document describes the configuration and usage of the Perspective Tag Browse Tree component. It covers the component's properties for defining the starting tag path, managing user selection, and applying filters. These instructions also explain how to use events and extension functions to script custom actions and advanced filtering logic based on user interactions.

## Documentation

# Instructions
# Name for this set of instructions
Perspective Tag Browse Tree Component

# Instructions
## Introduction
The Perspective Tag Browse Tree component is used to display a hierarchical tree of tags from an Ignition tag provider. It allows users to navigate through the tag structure, select one or multiple tags, and trigger actions based on those selections or interactions. It is visually represented as a folder tree, similar to a file explorer.

## Component Properties
The component's behavior and appearance are configured through its properties, which are organized into logical groups.

### root
This object configures the starting point for the tag tree.
*   **`path` (String):** Specifies the initial path from which the tag structure will be displayed. An empty string (`""`) will start the browse at the root level of the tag providers. To start deeper in the hierarchy, provide a tag path to a specific folder (e.g., `[default]MyFolder/SubFolder`).

### filter
This object configures the built-in text filter for the tree.
*   **`enabled` (Boolean):** If `true`, a text input box will be visible above the tree, allowing users to type and filter the visible nodes. Defaults to `false`.
*   **`text` (String):** The value of the filter text. This property can be bound or written to from a script to programmatically filter the tree.

### selection
This object configures how tags can be selected within the component.
*   **`mode` (String):** Determines the selection behavior.
    *   `"single"`: Allows the user to select only one tag at a time.
    *   `"multiple"`: Allows the user to select multiple tags simultaneously. This is the default.
*   **`values` (Array of Strings):** A read-only list containing the tag paths of the currently selected items. The order of the paths in the array reflects the order in which they were selected. This property is very useful for scripting, as it provides direct access to the user's selection.

### display
This object manages display settings for auxiliary elements of the component.
*   **`refreshIcon` (Object):** Contains properties for the refresh icon.
    *   **`visible` (Boolean):** If `true` (the default), a refresh icon is displayed, allowing the user to manually reload the tag tree.
    *   **`path` (String):** The icon path for the refresh button. Defaults to `"material/refresh"`.
    *   **`style` (Object):** A style object to apply custom CSS styling to the refresh icon.

### style
This is a standard style object that allows you to apply CSS styling to the main component container, affecting properties like background color, border, padding, etc.

## Component Events
These events allow you to execute scripts in response to user interactions with the tree. The event object passed to these scripts contains contextual information about the node that was interacted with.

### onNodeClick
Fires when a user left-clicks on any node (tag or folder) in the tree.
*   **Event Object Properties:**
    *   **`path` (String):** The full tag path of the clicked node.
    *   **`name` (String):** The name of the clicked node.

### onNodeDoubleClick
Fires when a user double-clicks on any node in the tree.
*   **Event Object Properties:**
    *   **`path` (String):** The full tag path of the double-clicked node.
    *   **`name` (String):** The name of the double-clicked node.

### onNodeContextMenu
Fires when a user right-clicks on any node in the tree. This is typically used to open a custom context menu.
*   **Event Object Properties:**
    *   **`path` (String):** The full tag path of the right-clicked node.
    *   **`name` (String):** The name of the right-clicked node.

## Extension Functions
Extension functions provide hooks to inject custom logic into the component's behavior.

### filterBrowseNode(self, node)
This function is called for every single tag and folder before it is displayed in the tree. It gives you the ability to create complex filtering logic beyond the simple text filter.
*   **Parameters:**
    *   **`self`:** A reference to the Tag Browse Tree component itself.
    *   **`node`:** An object (`NodeBrowseInfo`) that represents the tag or folder being evaluated. The most common property to use is `node.name`.
*   **Return Value:**
    *   The function **must** return a Boolean value.
    *   Return `True` to include the node in the tree.
    *   Return `False` to exclude (hide) the node from the tree.

*   **Example Implementation:**
    This script will only show nodes (both tags and folders) that have "Ramp" in their name.
    ```python
    # This example will filter out any nodes (both Tags and folders included) 
    # that do not contain the string "Ramp".
    if "Ramp" in node.name:
        return True
    else:
        return False
    ```

## Helpful Tips
*   **No Component Functions:** This component does not have any built-in scripting functions (like `system.perspective.refresh()`). All scripting is handled via component events or the `filterBrowseNode` extension function.
*   **Two Ways to Filter:**
    1.  Use the `filter.text` property for simple, user-driven text filtering.
    2.  Use the `filterBrowseNode` extension function when you need to implement complex, programmatic filtering logic based on node properties other than just text matching (e.g., tag type, specific naming conventions).
*   **Starting Path:** The `root.path` property is crucial for limiting the scope of the tree, which improves both usability and performance by not loading the entire tag provider. It works well in combination with `filterBrowseNode`.
*   **Accessing Selections:** To act on the tags a user has selected, you will almost always read the `selection.values` array property. For example, you could have a button next to the tree that, when clicked, iterates through this array to trend the selected tags.
*   **Event-Driven Actions:** Use the `onNodeClick` or `onNodeDoubleClick` events to trigger immediate actions when a user interacts with a tag, such as opening a popup or navigating to a different view. The `event.path` property is the key piece of information you'll need from the event object.

# Schema - raw
{"schema":{"type":"object","properties":{"display":{"description":"Display settings for the component.","type":"object","required":["refreshIcon"],"properties":{"refreshIcon":{"description":"Display settings for the refresh icon.","type":"object","required":["visible","path","style"],"properties":{"visible":{"description":"Visibility setting for the refresh icon.","type":"boolean","default":true},"path":{"format":"icon-path","description":"Path to the icon used to represent the \"refresh\" action.","type":"string","default":"material/refresh"},"style":{"description":"Style to apply to the refresh icon.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}}},"filter":{"description":"Tree filtering configuration.","type":"object","properties":{"enabled":{"description":"Enables the visibility of the filter.","type":"boolean","default":false},"text":{"description":"The filter text.","type":["string","number"],"default":""}}},"selection":{"description":"Configuration for the selected tags.","type":"object","required":["mode","values"],"properties":{"values":{"description":"List of the selected tag paths in the order in which selection occurred.","type":"array","default":[]},"mode":{"description":"Mode used when selecting tags.","type":"string","enum":["single","multiple"],"default":"multiple"}}},"root":{"description":"Configuration for the path from which the displaying folder/tag structure will start.","type":"object","required":["path"],"properties":{"path":{"description":"String value representing the \"starting path\" from which the tag structure will begin displaying.","type":"string","default":""}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"TagBrowseTree","name":"Tag Browse Tree","palette":{"variants":[{"tooltip":"Provides the ability to select tags from a tag provider and perform actions on them from the component events.","label":"Tag Browse Tree"}],"category":"display"},"extensionFunctions":[{"defaultImplementation":"return True","description":"Called for each tag before it is displayed in the tag browse tree. Return False to exclude the tag from displayed results.","name":"filterBrowseNode","arguments":[{"description":"The tag returned as type NodeBrowseInfo. See the Ignition JavaDocs for usage.","name":"node"}]}],"id":"ia.display.tag-browse-tree","events":[{"schema":{"type":"object","properties":{"path":{"description":"Tag path of the node that was clicked.","type":"string"},"name":{"description":"Name of the node that was clicked.","type":"string"}}},"description":"This event is fired when a node is clicked in the tree.","name":"onNodeClick"},{"schema":{"type":"object","properties":{"path":{"description":"Tag path of the node that was clicked.","type":"string"},"name":{"description":"Name of the node that was clicked.","type":"string"}}},"description":"This event is fired when a node is double-clicked in the tree.","name":"onNodeDoubleClick"},{"schema":{"type":"object","properties":{"path":{"description":"Tag path of the node that was clicked.","type":"string"},"name":{"description":"Name of the node that was clicked.","type":"string"}}},"description":"This event is fired when a node is right-clicked in the tree.","name":"onNodeContextMenu"}]}