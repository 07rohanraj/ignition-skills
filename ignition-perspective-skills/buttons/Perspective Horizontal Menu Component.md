# Perspective Horizontal Menu Component

## Description

This guide details the configuration of the Perspective Horizontal Menu component for creating primary navigation. It covers how to define the menu's structure with items and nested submenus, set navigation targets for internal or external pages, and apply custom styles. Furthermore, it explains how to use the `onItemClicked` event to trigger scripts in response to user selections.

## Documentation

# Instructions
# Perspective Horizontal Menu Component

## Instructions for Use

The Horizontal Menu component is a primary navigation tool in Ignition Perspective. It is designed to create a horizontal bar of menu options that can be used to navigate between different views within your project or to link to external websites.

### Core Configuration

The primary configuration for the Horizontal Menu is done through the `items` property. This property is an array of objects, where each object represents a single menu item at the top level of the menu.

Each menu item object has the following key properties:

*   **`label` (string):** The text that will be displayed for the menu item.
*   **`target` (string):** The destination for navigation when the item is clicked. This is only used if the item does not have a submenu (i.e., its own `items` array is empty).
    *   For navigation to a page within the Perspective project, use the Page URL (e.g., `/path/to/my-page`).
    *   For navigation to an external website, use the full URL (e.g., `https://example.com`).
*   **`enabled` (boolean):** Determines if the menu item is clickable. If `false`, the item will be visible but greyed out and non-interactive.
*   **`icon` (object):** An object to define an icon that appears to the left of the label.
    *   **`path` (string):** The path to the icon. The Material Design icon library is commonly used, with a format like `material/icon_name` (e.g., `material/home`).
    *   **`color` (string):** The color of the icon, which can be a hex code (e.g., `#FF0000`) or a named color.
*   **`style` (object):** An object for applying specific CSS styles to this individual menu item. This will override styles defined in the component's `itemStyle` property.
*   **`items` (array):** An array of menu item objects that will serve as a submenu. If this array contains items, a dropdown will appear when the user interacts with the parent item. **A parent item with a submenu should not have a `target` property set.**

### Submenus

To create a dropdown submenu, you define a nested structure. For a given menu item, instead of providing a `target`, you populate its `items` array with more menu item objects. Each of these child objects can then have its own `label`, `target`, `icon`, etc.

**Example Structure:**
```json
[
  {
    "label": "Home",
    "target": "/home",
    "icon": { "path": "material/home" }
  },
  {
    "label": "Offices",
    "icon": { "path": "material/landscape" },
    "items": [
      {
        "label": "Reservoir",
        "target": "/reservoir_page",
        "icon": { "path": "material/rowing" }
      },
      {
        "label": "Warehouse",
        "target": "/warehouse_page",
        "icon": { "path": "material/local_shipping" }
      }
    ]
  },
  {
    "label": "External Link",
    "target": "http://www.inductiveautomation.com/",
    "icon": { "path": "material/link" }
  }
]
```

### Styling

There are three levels of styling available:

1.  **`props.style`:** Applies CSS styles to the entire component container, such as the border around the whole menu bar.
2.  **`props.itemStyle`:** Applies a consistent style to *every* individual menu item. This is useful for setting a uniform look and feel.
3.  **`props.items[n].style`:** Applies a style to a *single, specific* menu item. This overrides any conflicting styles from `props.itemStyle` for that item only. For example, you could use this to highlight a specific menu option.

### Events

The main event for this component is `onItemClicked`.

*   **`onItemClicked`**: This event fires whenever any clickable menu item is selected by the user. It provides an `event` object with useful information about the clicked item:
    *   **`event.label` (string):** The label of the item that was clicked.
    *   **`event.target` (string):** The target URL or path of the clicked item.
    *   **`event.enabled` (boolean):** The enabled state of the clicked item.
    *   **`event.path` (array):** A list of numerical indexes representing the path to the clicked item. For a top-level item, it might be `[2]`. For a nested item, it would be `[2, 0]`, indicating the first item in the submenu of the third top-level item.

This event can be used to run scripts for actions other than simple navigation.

---

### Big List of Helpful Tips

*   **Submenu Parent Items Have No Target:** If a menu item is meant to open a submenu, make sure its `target` property is empty. Populate its `items` array instead. If you set a `target`, the submenu will not be accessible.
*   **Internal vs. External Navigation:** Always use a leading slash `/` for internal page URLs (e.g., `/my-view`) and the full protocol `http://` or `https://` for external websites.
*   **Icon Paths:** The standard format for icon paths is `library_name/icon_name`. The most common library is `material`.
*   **No Component Functions:** This component **does not have any component-specific or extension scripting functions**. All custom logic should be handled through the `onItemClicked` event. Do not attempt to call functions like `refresh()` or `setItems()` on this component.
*   **Styling Precedence:** Remember the styling hierarchy: component `style` is for the container, `itemStyle` is for all items, and an individual item's `style` property is for that one item and overrides `itemStyle`.
*   **Automatic Scrolling:** If the number of top-level menu items exceeds the horizontal width of the component, navigation arrows will automatically appear to allow the user to scroll through the items.
*   **Component vs. Item `enabled`:** The `props.enabled` property will disable the entire component. The `enabled` property within an item object will disable only that specific item and its potential submenu.
*   **Event `path` is Key:** When using the `onItemClicked` event for scripting, the `event.path` array is the most reliable way to programmatically identify which specific item was clicked, especially in menus with nested sub-items.

# Schema - raw
{"schema":{"type":"object","required":["items"],"example":{"itemStyle":{"classes":""},"enabled":true,"style":{"classes":""},"items":[{"icon":{"path":""},"label":"Menu Item","enabled":true,"target":"","style":{"classes":""},"items":[{"icon":{"color":"","path":"material/link"},"label":"Link to Google","enabled":true,"target":"http://www.google.com","style":{"classes":""},"items":[]}]},{"icon":{"color":"","path":"material/link"},"label":"Link to Google","enabled":true,"target":"http://www.google.com","style":{"classes":""},"items":[]},{"icon":{"path":""},"label":"Disabled Menu Item","enabled":false,"target":"","style":{"classes":""},"items":[]},{"icon":{"path":""},"label":"Last Menu Item","enabled":true,"target":"","style":{"classes":""},"items":[]}]},"additionalProperties":false,"definitions":{"ConfigItem":{"type":"object","default":{"icon":{"path":""},"label":"Menu Item","enabled":true,"target":"","style":{"classes":""},"items":[]},"additionalProperties":false,"properties":{"icon":{"description":"Path to an icon repository containing the icon to be used in the menu item.","default":{},"$ref":"urn:ignition-schema:schemas/optional-icon-schema.json"},"label":{"description":"Text to display for this menu item.","type":"string"},"enabled":{"description":"The enabled state of the menu item.  Allows it to perform its action or render its submenu.","type":"boolean","default":true},"target":{"description":"A url (external) or a mounted path to a page. If 'items' is empty (no children for this item) this will navigate to that location.","type":"string","default":""},"style":{"description":"Style to apply just to this menu item.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"items":{"description":"Config items representing child menu items from this option. If defined, a submenu will branch from here with these options.","type":"array","default":[],"items":{"$ref":"#/definitions/ConfigItem"}}}}},"properties":{"itemStyle":{"description":"Style to apply to the individual menu items.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"enabled":{"description":"The enabled state of the component.","type":"boolean","default":true},"style":{"description":"Style to apply to apply to the entire component.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"items":{"description":"Config items representing the main menu items.","type":"array","default":[],"items":{"$ref":"#/definitions/ConfigItem"}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"HorizontalMenu","name":"Horizontal Menu","palette":{"variants":[{"tooltip":"Enables you to build a menu structure for navigation by setting up multiple links to different page URLs from the component.","label":"Horizontal Menu"}],"category":"navigation"},"id":"ia.navigation.horizontalmenu","events":[{"schema":{"type":"object","default":"\t# if event.enabled:\n\t\t# add your action handling code\n","properties":{"label":{"description":"The label of the item that was selected.","type":"string"},"enabled":{"description":"Whether the item interacted with is enabled.","type":"boolean"},"target":{"description":"A url (external) or a mounted path to a page.","type":"string"},"path":{"description":"A list containing the item indexes leading to the item that was clicked.","type":"array"}}},"documentationUrl":"https://links.inductiveautomation.com/81-horizontal-menu-events","description":"Fired whenever an item is clicked on this menu.","name":"onItemClicked"}]}