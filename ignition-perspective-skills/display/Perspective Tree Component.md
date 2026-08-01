# Perspective Tree Component

## Description

This documentation describes the configuration and usage of the Perspective Tree component, detailing how its properties are used to define the hierarchical data structure, customize the visual appearance and icons, and manage interactive behaviors like selection and node expansion. It also covers how to capture and respond to user interactions through component events to build dynamic functionality.

## Documentation

# Instructions
# Perspective Tree Component Instructions

## Object Description
The Perspective Tree component is an interactive component used to display data in a hierarchical, tree-like structure. It is built from a nested array of objects, where each object represents a "node" or "branch" in the tree. Users can expand and collapse nodes to navigate the hierarchy. The component is highly customizable, allowing for different icons, styles, and behaviors based on user interaction.

## Property Instructions

### `items`
This is the most critical property. It is an array of objects that defines the structure and content of the tree. Each object in the array is a top-level node (a "root" branch).

**Each node object has the following structure:**
*   **`label` (string, required):** The text that will be displayed for the node.
*   **`expanded` (boolean, required):** Determines if the node is shown in an expanded (`true`) or collapsed (`false`) state by default.
*   **`items` (array, required):** An array of other node objects, representing the children of the current node. If a node has no children, this should be an empty array `[]`. This nested structure is what creates the tree hierarchy.
*   **`data` (any, optional):** A property to hold extra, non-displayed information about the node. This can be a string, number, object, or array. This data is accessible through scripting, for example, when a user clicks on the item.
*   **`icon` (object, optional):** An object to define a custom icon for this specific node, overriding the default icons set in `appearance.defaultNodeIcons`.
    *   `path` (string): Path to the icon, e.g., `"material/folder"`.
    *   `color` (string): A color for the icon, e.g., `"#FF0000"`.
    *   `style` (object): Style rules to apply to the icon.

**Example of an `items` structure:**
```json
[
  {
    "label": "Item 1",
    "expanded": true,
    "items": [
      {
        "label": "Child 1",
        "expanded": false,
        "items": [],
        "data": {"info": "This is a child node"}
      }
    ],
    "data": "Root Node Data"
  },
  {
    "label": "Item 2",
    "expanded": false,
    "items": [],
    "data": 123
  }
]
```

### `selection` and `selectionData`
These two properties manage user selections in the tree.
*   **`selection` (array of strings):** A read/write array containing the "item path" of the currently selected node(s). The item path is a string representation of the indexes that lead to the item. For example, `"0.1"` refers to the second child of the first top-level node. You can programmatically select a node by writing its path to this property.
*   **`selectionData` (array of objects):** A read-only array that provides detailed information about the currently selected nodes. Each object in the array contains:
    *   `itemPath` (string): The index path to the selected item.
    *   `value`: The content of the `data` property for the selected item.

### `interactable`
*   A boolean property. If `true` (default), users can interact with the tree (expand, collapse, select). If `false`, the tree is visible but cannot be interacted with.

### `branchNodeSelectable`
*   A boolean property. If `true` (default), users can select any node in the tree, including those that have children (branch nodes). If `false`, only terminal nodes (nodes with an empty `items` array) can be selected.

### `appearance`
An object that controls the visual look of the tree.
*   **`rowHeight` (number):** The height of each row in pixels. The default is `24`.
*   **`textOverflow` (string):** Controls how text that is too long for the component's width is handled.
    *   `"scroll"` (default): The tree will become horizontally scrollable.
    *   `"truncate"`: The text will be cut off and an ellipsis (...) will be shown.
*   **`expandIcons` (object):** Defines the icons used for expanding and collapsing nodes. It has three sub-properties, each an icon object (`path`, `color`, `style`):
    *   `expanded`: Icon for a node whose children are visible. Default is `material/arrow_drop_down`.
    *   `collapsed`: Icon for a node whose children are hidden. Default is `material/arrow_right`.
    *   `empty`: Icon for a terminal node (no children). Default is an empty path.
*   **`defaultNodeIcons` (object):** Defines the default icons displayed next to the node's label. It has three sub-properties for different node states, each an icon object (`path`, `color`, `style`):
    *   `expanded`: For an expanded node. Default is `material/folder_open`.
    *   `collapsed`: For a collapsed node. Default is `material/folder`.
    *   `empty`: For a terminal node (no children). Default is `material/stop`.
*   **`selectedStyle` (object):** Style object applied to a node when it is selected. You can define a style class via the `classes` property.
*   **`unselectedStyle` (object):** Style object applied to unselected nodes. You can define a style class via the `classes` property.

### `style`
*   An object that defines the overall style for the component, including background, border, padding, etc. You can also assign a style class.

## Event Instructions

### `onItemClicked`
This is the primary event for the Tree component. It fires whenever any node in the tree is clicked. The event object contains the following properties:
*   **`event.data`:** The value of the `data` property from the clicked node. This is how you access the hidden contextual information you stored.
*   **`event.label` (string):** The `label` text of the clicked node.
*   **`event.itemPath` (array):** An array of numbers representing the index path to the clicked item. For example, `[0, 1]` refers to the second child of the first top-level node.

## Scripting and Functions
*   **Component Functions:** This component has no component-specific scripting functions.
*   **Extension Functions:** This component has no extension functions.

## Helpful Tips
*   The `items` property is recursive. The structure of a child node inside the `items` array is identical to the structure of a parent node.
*   The `data` property in each item is extremely useful for storing identifiers, raw data, or any context that your scripts might need when an item is clicked, without cluttering the display.
*   Remember the difference between `selection` and `selectionData`. Use `selection` if you need to know *which* item is selected (by its path) or if you want to *set* the selection. Use `selectionData` if you need to get the `data` from the selected item(s).
*   Icon paths typically use the Material Design Icon library. The format is `material/icon_name`.
*   To create a tree with no items initially, set the `items` property to an empty array `[]`.
*   The `itemPath` in the `onItemClicked` event is an array of integers, which is ideal for programmatic access, while the `selection` property uses a string representation of that path (e.g., `"0.1.2"`).

# Schema - raw
{"schema":{"description":"An interactive tree component.","type":"object","title":"Tree","example":{"appearance":{"unselectedStyle":{"classes":""},"defaultNodeIcons":{"collapsed":{"color":"","path":"material/folder"},"empty":{"color":"","path":"material/stop"},"expanded":{"color":"","path":"material/folder_open"}},"expandIcons":{"collapsed":{"color":"","path":"material/arrow_right"},"empty":{"color":"","path":""},"expanded":{"color":"","path":"material/arrow_drop_down"}},"textOverflow":"scroll","selectedStyle":{"classes":""},"rowHeight":24},"selection":[],"style":{"classes":""},"selectionData":[],"interactable":true,"items":[{"data":"I am string data for Item 1","label":"Item 1","expanded":true,"items":[{"data":{"someKey":"Information here."},"label":"Child 1","expanded":false,"items":[{"data":{"things":["one potato","two potato","three potato","four","boilem, mash em, put em in a stew"]},"icon":{"color":"#869DB1","path":"material/arrow_right","style":{}},"label":"Grandchild 1","expanded":false,"items":[]},{"data":3.14159265359,"label":"Grandchild 2","expanded":false,"items":[]}]}]},{"data":[1,2,77,89,123],"label":"Item 2","expanded":false,"items":[{"label":"Child of Item 2","expanded":false,"items":[{"label":"Different Grandchild 1","expanded":false,"items":[]}]}]}]},"additionalProperties":false,"definitions":{"TreeNode":{"description":"Configuration for a single node of a tree.","title":"Tree Node","type":"object","required":["label","items","expanded"],"default":{"data":{},"label":"Item","expanded":false,"items":[]},"additionalProperties":false,"properties":{"data":{"description":"Extra contextual information about this tree node."},"icon":{"description":"Optional custom icon to override default for this node","$ref":"urn:ignition-schema:schemas/icon-schema.json"},"label":{"description":"Text displayed for this item.","type":"string"},"expanded":{"description":"Whether this node is currently expanded in the tree.","type":"boolean"},"items":{"description":"An array of TreeNode objects, each of which represents a node in the tree.","type":"array","items":{"$ref":"#/definitions/TreeNode"}}}}},"properties":{"branchNodeSelectable":{"description":"If false, only terminal nodes without children will be selectable.","type":"boolean","default":true},"appearance":{"type":"object","properties":{"unselectedStyle":{"description":"Styles to apply to all unselected nodes","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"defaultNodeIcons":{"type":"object","properties":{"collapsed":{"description":"Default icon displayed next to each collapsed tree node's label","$ref":"urn:ignition-schema:schemas/icon-schema.json"},"empty":{"description":"Default icon displayed next to each empty (terminal) tree node's label","$ref":"urn:ignition-schema:schemas/icon-schema.json"},"expanded":{"description":"Default icon displayed next to each expanded tree node's label","$ref":"urn:ignition-schema:schemas/icon-schema.json"}}},"expandIcons":{"type":"object","properties":{"collapsed":{"description":"Configuration for the tree icon used to represent a collapsed parent node.","$ref":"urn:ignition-schema:schemas/icon-schema.json"},"empty":{"description":"Configuration for the tree icon used to represent a childless (terminal) node.","$ref":"urn:ignition-schema:schemas/icon-schema.json"},"expanded":{"description":"Configuration for the tree icon used to represent a node with children displayed.","$ref":"urn:ignition-schema:schemas/icon-schema.json"}}},"textOverflow":{"description":"Whether overflowing text should cause entire tree to scroll horizontally or to truncate text with an ellipsis","type":"string","enum":["scroll","truncate"],"default":"scroll"},"selectedStyle":{"description":"Styles to apply to all selected nodes","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"rowHeight":{"description":"Height, in pixels, of each row/node in the tree","type":"number","default":24}}},"selection":{"description":"Holds the item index paths of the current selection.","type":"array","default":[],"items":{"pattern":"","type":"string"}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"interactable":{"description":"If false, tree is displayed but may not be interacted with.","type":"boolean","default":true},"selectionData":{"description":"Array of objects containing the data and index path for all currently selected items.","type":"array","default":[],"items":{"type":"object","additionalProperties":false,"properties":{"itemPath":{"type":"string"},"value":{}}}},"items":{"description":"An array of objects, each representing a distinct node in the tree.","type":"array","default":[],"items":{"type":"object","$ref":"#/definitions/TreeNode"}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Tree","name":"Tree","palette":{"variants":[{"tooltip":"Displays a dataset in a tree hierarchy.","label":"Tree"}],"category":"display"},"id":"ia.display.tree","events":[{"schema":{"type":"object","properties":{"data":{"description":"The value of the contextual 'data' object on the clicked node"},"label":{"description":"Text to display for this option.","type":"string"},"itemPath":{"description":"A list containing the item indexes leading to the item that was clicked.","type":"array"}}},"documentationUrl":"https://links.inductiveautomation.com/81-tree-component-events","description":"Fired whenever an item is clicked on this tree.","name":"onItemClicked"}]}