# Perspective Tab Container

## Description

These instructions describe the usage and configuration of the Perspective Tab Container, a component designed to organize content into a selectable series of tabs. The guide covers how to create and manage the tabs themselves, how to place other components into the content area for each specific tab, and how to customize the container's visual appearance and behavior through its various styling and operational properties.

## Documentation

# Instructions
Here are the instructions for the Perspective Tab Container.

### **Object Name:**
`Perspective Tab Container`

### **Instructions for LLM:**

The Perspective Tab Container is a component used to organize content into a series of selectable tabs. When a user clicks on a tab, a different view or component associated with that tab is displayed in the main content area. Only the content for the currently selected tab is visible at any time.

There are two main visual styles, or variants, determined by the `menuType` property:
*   **Classic:** A traditional layout with distinct boxes for each tab.
*   **Modern:** A more contemporary layout where tabs are not boxed, and the selected tab is indicated by an underline.

#### **Core Concepts:**

*   **Tab Management:** Tabs are defined and configured through the `tabs` property, which is an array of objects. Each object in the array represents one tab.
*   **Content Display:** To display content *inside* a tab, you must add a component as a child of the Tab Container. You then associate that child component with a specific tab by setting the child's `position.tabIndex` property to the corresponding index of the tab in the `tabs` array.
*   **Active Tab:** The `currentTabIndex` property, a zero-based integer, determines which tab is currently active and visible.

---

### **Property Breakdown & Usage:**

#### **`tabs`**
This is an array that defines the tabs in the menu. Each element in the array configures a single tab. You can add, remove, or reorder tabs by manipulating this array. An element can be a simple string (for text-only tabs) or a more detailed object.

*   **Simple Tab (String):**
    *   If you just need a tab with a text label, you can provide a simple string.
    *   Example: `{"tabs": ["Overview", "Details", "Settings"]}` creates three tabs with these labels.

*   **Advanced Tab (Object):**
    For more control, use an object with the following properties:
    *   `text` (string): The text to display on the tab.
    *   `disabled` (boolean): If `true`, the tab is visible but cannot be selected by the user.
    *   `runWhileHidden` (boolean): When `true`, the content (view/components) of the tab will remain loaded in the background even when another tab is selected. This improves performance when switching back to complex tabs but consumes more memory. If `false` (the default), the content is loaded when the tab is first activated and destroyed when the user navigates away.
    *   `viewPath` (string): Path to a Perspective View. This will render the specified View *inside the tab header itself*, replacing the `text`. This is for creating complex, dynamic tab headers, not for defining the main content of the tab.
    *   `viewParams` (object): If using `viewPath`, this object passes parameters to the View being rendered in the tab header.
    *   `width` (number): Sets a specific width for this individual tab, overriding the default `tabSize.width`.

#### **`currentTabIndex`**
A number representing the index of the currently active tab. This is **zero-indexed**, so the first tab is at index `0`. To change which tab is displayed, you modify this value. For example, to programmatically switch to the third tab, you would set `currentTabIndex` to `2`.

#### **`childPositionSchema` (`position.tabIndex`)**
This is not a property of the Tab Container itself, but rather a property that must be set on each **child component** placed within it.
*   To place a component (like a Flex Container, a Chart, or a Label) into a specific tab's content area, you must set that component's `position.tabIndex` property.
*   The value of `position.tabIndex` must correspond to the index of the desired tab in the `tabs` array.
*   **Only one component can be displayed in each tab's content area.** If you need multiple components in one tab, you should place them inside a container component (like a Column Container or Flex Container) and then place that single container into the tab.

#### **Styling Properties**
*   `style`: Applies CSS styles to the entire Tab Container component.
*   `menuType` (enum): Sets the overall look.
    *   `"classic"`: Traditional boxed tabs.
    *   `"modern"`: Tabs with an underline for the selected state.
*   `tabSize`: An object defining the default `width` and `height` for all tabs.
    *   `width` (number): Default width in pixels.
    *   `height` (number): Default height in pixels.
*   `menuStyle`: Styles the menu bar area that contains the tabs.
*   `contentStyle`: Styles the content area below the tabs where the child components are displayed.
*   `tabStyle`: An object that allows you to apply specific styles to tabs based on their state. This is useful for creating distinct visual feedback for user interaction.
    *   `active`: Styles applied only to the `currentTabIndex`.
    *   `inactive`: Styles applied to all tabs that are not active or disabled.
    *   `disabled`: Styles applied to any tab where `disabled` is set to `true` in the `tabs` array.

---

### **Helpful Tips:**

*   **Zero-Indexing is Key:** Remember that both `tabs` and `currentTabIndex` are zero-indexed. The first tab is `0`, the second is `1`, and so on. This is a common source of errors.
*   **Content vs. Tab Header:** Do not confuse adding content *to* a tab with embedding a view *in* a tab.
    *   To put something **inside the main content area** of a tab, add a component to the Tab Container and set its `position.tabIndex`.
    *   To change the **appearance of the tab button itself**, use the `tabs[i].viewPath` property.
*   **Adding/Deleting Tabs:** To add a new tab, append a new object or string to the `tabs` array. To delete a tab, remove its corresponding element from the `tabs` array. Remember that removing a tab will shift the indices of all subsequent tabs, so you may need to update the `position.tabIndex` of child components.
*   **One Child Per Tab:** You can only assign one child component to any given `tabIndex`. If you need to display multiple components, first place them into a parent container (like a Column or Flex container) and then place that single container inside the tab.
*   **Styling Precedence:** Styles defined in `tabStyle` (e.g., `active`, `inactive`) will generally override the more general styles in `menuStyle`.
*   **Performance:** For tabs with very complex content that is slow to load, set `runWhileHidden: true` on that tab's configuration object. This keeps the tab's content in memory for faster switching, but be mindful of the increased memory usage.
*   **User Interaction:** To add a component to a tab from the Designer, a user would typically deep-select the Tab Container and then drag a component onto it. This automatically adds the component as a child. The user then needs to set the `position.tabIndex` on the new component.

# Schema - raw
{"schema":{"type":"object","required":["tabs","currentTabIndex","menuType","tabSize","menuStyle","tabStyle","style"],"additionalProperties":false,"properties":{"menuStyle":{"description":"Styles for the menu area. For 'modern' menuType, this is the whole menu. For 'classic', the portion not filled by tabs.","default":{"backgroundColor":"transparent"},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"tabs":{"description":"Content to display in the menu as tabs. Each tab in this array may be either a string to display as the tab text or an object with viewPath and optionally viewParams. If the latter, a view will render as the tab in place of text.","type":"array","default":[""],"items":{"oneOf":[{"description":"Text to display for this tab","type":"string","default":""},{"type":"object","required":["text"],"default":{"runWhileHidden":false,"disabled":false,"text":""},"additionalProperties":false,"properties":{"runWhileHidden":{"description":"When true the contents of this tab will load once their tab is first activated, and will persist in the background when the currentTabIndex changes","type":"boolean"},"disabled":{"description":"When true the tab is disabled","type":"boolean"},"text":{"type":"string"}}},{"type":"object","required":["viewPath"],"default":{"viewPath":"","runWhileHidden":false,"disabled":false,"viewParams":{}},"additionalProperties":false,"properties":{"viewPath":{"format":"view-path","description":"Path to view to render in place of tab text","type":"string","default":""},"runWhileHidden":{"description":"When true the contents of this tab will load once their tab is first activated, and will persist in the background when the currentTabIndex changes","type":"boolean"},"width":{"description":"Individual width for this view tab","type":"number"},"disabled":{"description":"When true the tab is disabled","type":"boolean"},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"description":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","type":"object","default":{}}}}]}},"tabSize":{"description":"Default size allotted to a single tab. If container width does not allow, tab width will shrink from this size accordingly.","type":"object","required":["height","width"],"default":{"width":96,"height":36},"additionalProperties":false,"properties":{"width":{"type":"number","default":96},"height":{"type":"number","default":36}}},"contentStyle":{"description":"Styles for the tab container content frame.","$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"menuType":{"description":"If the type is 'classic', a traditional menu with boxed tabs is shown. 'modern' has no borders around each tab and shows selection with an underline.","type":"string","enum":["classic","modern"],"default":"classic"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"tabStyle":{"description":"Additional styling to apply to all tabs depending on active (selected), inactive or disabled state","type":"object","required":["active","inactive","disabled"],"default":{"active":{},"inactive":{},"disabled":{}},"additionalProperties":false,"properties":{"active":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"inactive":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"disabled":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"currentTabIndex":{"description":"Which index in tabs array is currently active","type":"number","default":0}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"TabContainer","name":"Tab Container","palette":{"variants":[{"tooltip":"Container with tabs as navigation buttons arranged together with the selected tab highlighted.","label":"Tab"},{"tooltip":"Container with tabs as navigation buttons arranged together with the selected tab highlighted.","label":"Classic","id":"tab-classic"},{"tooltip":"Container with tabs as navigation buttons arranged together with the selected tab highlighted.","label":"Modern","props":{"menuType":"modern"},"id":"tab-modern"}],"category":"container"},"id":"ia.container.tab","childPositionSchema":{"type":"object","required":["tabIndex"],"additionalProperties":false,"properties":{"tabIndex":{"type":"number","default":0}}}}