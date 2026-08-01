# Perspective Menu Tree Component

## Description

This document outlines the configuration and usage of the Perspective Menu Tree component, detailing how to build a hierarchical navigation menu by defining the structure within the core `items` property. The instructions cover customizing the appearance of the component and its individual items, defining navigation targets, and implementing custom logic using the `onItemClicked` event.

## Documentation

# Instructions
# Perspective Menu Tree Component Instructions

## 1. Overview and Purpose

The Perspective Menu Tree component is used to create hierarchical navigation menus. It displays a list of items, which can contain sub-items, forming a tree-like structure. Users can click on items to either navigate to a different View or URL, or to expand a branch of the tree, revealing its sub-items. This component is ideal for organizing complex navigation structures in a compact and intuitive way.

## 2. Core Concept: The `items` Property

The entire structure of the Menu Tree is defined within the `props.items` property. This property is an array of "ConfigItem" objects. Each object in the array represents a top-level menu item.

The key to creating a hierarchical menu is that each ConfigItem object can, itself, contain an `items` array. This nesting of `items` arrays allows you to build out the branches and leaves of your menu tree.

-   An item with a non-empty `items` array acts as a **branch**. When clicked, it will display its sub-items.
-   An item with an empty `items` array acts as a **leaf**. When clicked, it will attempt to navigate to the location specified in its `target` property.

### Example `items` structure:

```json
[
  {
    "label": {"text": "HMI"},
    "navIcon": {"path": "material/chevron_right"},
    "items": [
      {"label": {"text": "Overview"}, "target": "/overview", "items": []},
      {"label": {"text": "Lines"}, "target": "/lines", "items": []}
    ]
  },
  {
    "label": {"text": "Administration"},
    "navIcon": {"path": "material/chevron_right"},
    "items": [
      {"label": {"text": "Edit Users"}, "target": "/userEdit", "items": []}
    ]
  }
]
```

## 3. Component Properties (props)

These properties are configured on the root of the Menu Tree component.

| Property          | Type   | Description                                                                                                                              |
| ----------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `items`           | array  | An array of ConfigItem objects that define the top-level items of the menu. This is the primary property used to build the menu structure. |
| `layoutAlignment` | string | Specifies which side the root menu is aligned to. Submenus will slide in from the opposite side. Can be "left" or "right". Default: "left". |
| `enabled`         | boolean| If `true`, the entire component is enabled and can be interacted with. Default: `true`.                                                   |
| `style`           | object | Sets the style for the component's container (e.g., background, border, padding).                                                        |
| `itemStyle`       | object | A style object that is applied to all individual items in the menu. Can be overridden by an item's specific `style` property.            |
| `headerStyle`     | object | A style object applied to the header text that appears when a submenu is opened.                                                         |
| `backActionStyle` | object | A style object applied to the "back" button that appears in submenus.                                                                    |
| `backActionText`  | string | Text to display for the action that takes the user back to the previous menu level. This can be overridden by an item's `backActionText`.    |

## 4. Item Properties (ConfigItem)

These properties are configured for each individual object within an `items` array.

| Property         | Type    | Description                                                                                                                                                                                             |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `label`          | object  | An object containing the text and optional icon for the item's label.                                                                                                                                     |
| `items`          | array   | An array of nested ConfigItem objects. If this array is not empty, clicking the item will reveal these sub-items. If it is empty, clicking navigates to the `target`.                                        |
| `target`         | string  | A URL (e.g. `https://example.com`) or a mounted page path (e.g., `/my/page`). Navigation only occurs if the `items` property is an empty array.                                                          |
| `navIcon`        | object  | An icon displayed on the right side of the menu item, typically used to indicate that the item has a submenu (e.g., a chevron).                                                                           |
| `enabled`        | boolean | If `true`, this specific item can be interacted with. If `false`, it will be visually disabled. Default: `true`.                                                                                           |
| `visible`        | boolean | If `true`, the item will be displayed in the menu. Default: `true`.                                                                                                                                     |
| `showHeader`     | boolean | If `true`, this item's `label.text` will be displayed as a header/title for its own submenu. Default: `true`.                                                                                                |
| `style`          | object  | A style object applied specifically to this item, overriding any styles set by the component's `itemStyle` property.                                                                                      |
| `resetOnClick`   | boolean | If `true`, clicking this item will cause the entire Menu Tree to reset back to its root level. Useful for quick navigation back to the start. Default: `false`.                                            |
| `backActionText` | string  | Overrides the component's root `backActionText` property for this item's specific submenu, providing custom text for the back action. If blank, the root text is used.                                      |

### 4.1. `label` Object Properties

| Property | Type   | Description                                                                               |
| -------- | ------ | ----------------------------------------------------------------------------------------- |
| `text`   | string | The text to display for the menu item.                                                    |
| `icon`   | object | An object defining the icon to display to the *left* of the label text. See `icon` below. |

### 4.2. `navIcon` and `label.icon` Object Properties

| Property | Type   | Description                                                                                                                   |
| -------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `path`   | string | The path to the icon, e.g., `material/list`. The Material Icons library is the primary source.                                  |
| `color`  | string | The color of the icon, specified as a hex code (e.g., `#FF0000`) or standard color name. This can also be set via a style class. |

## 5. Events

### `onItemClicked`

This is the primary event for the Menu Tree. It fires whenever any item in the tree is clicked.

The `event` object passed to this event script contains the following properties:

| Property  | Type    | Description                                                                 |
| --------- | ------- | --------------------------------------------------------------------------- |
| `label`   | string  | The `label.text` of the item that was clicked.                              |
| `target`  | string  | The `target` of the item that was clicked.                                  |
| `enabled` | boolean | A boolean indicating if the clicked item was enabled.                       |
| `path`    | array   | A list of integers representing the indexes to the clicked item in the tree |
|           |         | (e.g., `[0, 2]` would be the 3rd sub-item of the 1st top-level item).       |

## 6. Scripting

The Menu Tree component **does not have any component-specific or extension functions**. All interaction scripting must be done through the `onItemClicked` event handler. You can use the properties of the `event` object within this handler to build custom logic.

## 7. Helpful Tips & Best Practices

*   **Icons:** Remember the distinction: `label.icon` appears on the left of the text, while `navIcon` appears on the right. `navIcon` is commonly used to indicate a submenu exists (e.g., `material/chevron_right`).
*   **Navigation Logic:** An item only navigates to its `target` if its `items` array is empty (`[]`). If `items` is not empty, clicking the item will always open the submenu, regardless of what is in the `target` property.
*   **Dynamic Menus:** The `items` property can be bound to a query or a script transform. This allows for creating dynamic menus based on user roles, system state, or database content.
*   **Styling Priority:** Styles are applied in the following order of increasing priority: Component `itemStyle` -> Item-specific `style`. An item's own style will always override the general style.
*   **Root Reset:** Use the `resetOnClick` property on key navigation items to provide a simple way for users to get back to the main menu without repeatedly clicking the "back" action.
*   **Complex Structure:** For very complex or deeply nested menus, it is often easier to edit the `items` property directly as JSON. You can copy the entire JSON structure, edit it in a text editor, and paste it back into the property editor.
*   **Finding Icons:** The documentation mentions the Material Icons library (`https://fonts.google.com/icons?selected=Material+Icons`) as the primary source for icon paths. The path format is `material/IconName`.

# Schema - raw
{"schema":{"type":"object","example":{"backActionText":"","itemStyle":{"classes":""},"backActionStyle":{"classes":""},"headerStyle":{"classes":""},"layoutAlignment":"left","style":{"classes":""},"items":[{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"color":"","path":"material/chevron_right"},"label":{"icon":{"path":"material/list"},"text":"Menu Item 1"},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"path":""},"label":{"icon":{"path":""},"text":"Submenu item 1"},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[]},{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"path":""},"label":{"icon":{"path":""},"text":"Submenu item 2"},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[]}]},{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"color":"","path":"material/chevron_right"},"label":{"icon":{"path":"material/list"},"text":"Menu Item 2"},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"path":""},"label":{"icon":{"path":""},"text":"Submenu item 1"},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[]},{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"path":""},"label":{"icon":{"path":""},"text":"Submenu item 2"},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[]}]}]},"additionalProperties":false,"definitions":{"ConfigItem":{"type":"object","default":{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"color":"","path":"material/chevron_right"},"label":{"icon":{"path":""},"text":""},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[]},"additionalProperties":false,"properties":{"visible":{"description":"Whether this option should be displayed in menu tree","type":"boolean","default":true},"backActionText":{"description":"Text to display in prompt to go back to the previous menu","type":"string","default":""},"showHeader":{"description":"Whether to display this option's text as a header/title for its submenu","type":"boolean","default":true},"navIcon":{"description":"Icon to convey action associated with this option","default":{"color":"","path":"material/chevron_right"},"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"label":{"type":"object","properties":{"icon":{"description":"Icon to accompany text in this option's label","default":{"path":""},"$ref":"urn:ignition-schema:schemas/icon-schema.json"},"text":{"description":"Text to display for this option","type":"string","default":""}}},"enabled":{"description":"Whether this option is currently enabled to perform its action or render its submenu","type":"boolean","default":true},"target":{"description":"A url (external) or a mounted path to a page. If 'items' is empty (no subtree for this option) this will navigate to that location","type":"string","default":""},"resetOnClick":{"description":"Whether to navigate back to the root of the menu tree when selected","type":"boolean","default":false},"style":{"description":"Style to apply just to this menu item.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"items":{"description":"Config items representing nodes in a subtree from this option. If defined, a submenu will branch from here with these options.","type":"array","default":[],"items":{"type":"object","default":{"visible":true,"backActionText":"","showHeader":true,"navIcon":{"path":""},"label":{"icon":{"path":""},"text":""},"enabled":true,"target":"","resetOnClick":false,"style":{"classes":""},"items":[]},"$ref":"#/definitions/ConfigItem"}}}}},"properties":{"backActionText":{"description":"Text to display in prompt to go back to the previous menu","type":"string","default":""},"itemStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"enabled":{"description":"Whether this option is currently enabled to perform its action or render its submenu","type":"boolean","default":true},"backActionStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"headerStyle":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"layoutAlignment":{"description":"Which side root menu is aligned to. Submenu slides in from other side.","type":"string","enum":["left","right"],"default":"left"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"items":{"description":"Config items representing nodes in a subtree from this option. If defined, a submenu will branch from here with these options.","type":"array","default":[],"items":{"$ref":"#/definitions/ConfigItem"}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"name":"Menu Tree","palette":{"variants":[{"tooltip":"Provides a hierarchical view of information that can be configured to expand submenu branches and menu items.","defaultName":"MenuTree"}],"category":"navigation"},"id":"ia.navigation.menutree","events":[{"schema":{"type":"object","properties":{"label":{"description":"Text to display for this option.","type":"string"},"enabled":{"description":"Whether the item interacted with is enabled.","type":"boolean"},"target":{"description":"A url (external) or a mounted path to a page.","type":"string"},"path":{"description":"A list containing the item indexes leading to the item that was clicked.","type":"array"}}},"documentationUrl":"https://links.inductiveautomation.com/81-menu-tree-component-events","description":"Fired whenever an item is clicked on this menu.","name":"onItemClicked"}]}