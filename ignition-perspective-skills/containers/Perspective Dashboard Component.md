# Perspective Dashboard Component

## Description

These instructions describe how to configure the Perspective Dashboard component by defining its grid layout and creating a library of available widgets. This process enables end-users to dynamically add, arrange, resize, and remove these widgets in a live session, allowing them to build and customize their own interactive layouts.

## Documentation

# Instructions
Here are the instructions for the Perspective Dashboard Component.

### **How to Use the Perspective Dashboard Component**

The Dashboard component is a powerful tool for creating user-customizable layouts in a Perspective session. It acts as a container that allows end-users to add, remove, and arrange pre-configured "widgets" on a grid. Your primary task as a designer is to define the grid system and create a library of `availableWidgets` that users can place on the dashboard.

#### **1. Initial Setup: The Grid**

First, you must decide on the layout mode for the dashboard grid. This is controlled by the `grid` property.

*   **`grid`**: Sets the layout mode.
    *   **`"stretch"` (default):** The grid will fill the available space of the Dashboard component. The number of rows and columns is fixed, but their size will grow or shrink with the component. This is the most common mode for responsive designs.
    *   **`"fixed"`:** Each cell in the grid has a fixed pixel size. The total size of the dashboard will depend on the number of rows/columns and the `cellSize`.

#### **2. Configuring the Grid Mode**

Based on your choice for the `grid` property, you will configure either the `stretch` object or the `fixed` object.

*   **If `grid` is `"stretch"`:**
    *   Use the `stretch` property to define the grid structure.
    *   `stretch.columnCount`: The number of columns in the grid (e.g., `8`).
    *   `stretch.rowCount`: The number of rows in the grid (e.g., `8`).
    *   `stretch.columnGutterSize`: The spacing in pixels between columns (e.g., `6`).
    *   `stretch.rowGutterSize`: The spacing in pixels between rows (e.g., `6`).

*   **If `grid` is `"fixed"`:**
    *   Use the `fixed` property to define the grid structure.
    *   `fixed.cellSize`: The width and height of each grid cell in pixels (e.g., `100`).
    *   `fixed.columnCount`: The number of columns in the grid (e.g., `10`).
    *   `fixed.rowCount`: The number of rows in the grid (e.g., `10`).
    *   `fixed.columnGutterSize`: The spacing in pixels between columns (e.g., `6`).
    *   `fixed.rowGutterSize`: The spacing in pixels between rows (e.g., `6`).

#### **3. Creating Available Widgets**

This is the most important step. You need to create a list of widgets that the user can choose from. This is done by adding objects to the `availableWidgets` array property. Each object in this array defines a widget template.

For each widget you want to make available, add an object to the `availableWidgets` array with the following properties:

*   **`name`**: A unique and descriptive name for the widget (e.g., "Motor Status" or "Tank Level Indicator"). This is shown to the user in the "Add Widget" dialog.
*   **`viewPath`**: The path to the Perspective View that this widget will display (e.g., "Widgets/MotorDetails").
*   **`viewParams`**: An object containing parameters to pass to the View specified in `viewPath`. The keys of this object **must** exactly match the names of the parameters defined in the target View.
*   **`defaultSize`**: An object defining the initial size of the widget when added to the dashboard.
    *   `columnSpan`: The number of columns the widget should occupy by default (e.g., `2`).
    *   `rowSpan`: The number of rows the widget should occupy by default (e.g., `2`).
*   **`minSize`**: An object defining the minimum size the user can resize the widget to.
    *   `columnSpan`: The minimum number of columns (e.g., `1`).
    *   `rowSpan`: The minimum number of rows (e.g., `1`).
*   **`header`**: An object to configure the widget's header bar.
    *   `enabled`: Set to `true` to show the header, `false` to hide it.
    *   `title`: The default title displayed in the header. The user can often edit this at runtime.
*   **`isConfigurable`**: If `true`, a configuration toggle icon appears when the user selects the widget. When clicked, a session parameter named `configuring` on the widget's view will be set to `true`. This allows you to create a View that has both a display state and a configuration state.
*   **`category`**: A string to group similar widgets together in the "Add Widget" dialog (e.g., "Motors", "Tanks").

#### **4. Runtime Properties and Behavior**

These properties control the user's interaction with the dashboard in a live session.

*   **`editingToggle`**: If `true`, a master "Edit" / "Done" button is shown on the dashboard, allowing users to enter and exit edit mode.
*   **`isEditing`**: This property reflects the current mode. `true` means the user is in edit mode and can move, resize, or remove widgets. You can bind this property to other components to show or hide elements based on the dashboard's mode.
*   **`pack`**: If `true` (default), the dashboard will automatically rearrange widgets to prevent empty spaces and overlaps, creating a compact layout. If `false`, widgets can be placed anywhere, even on top of each other, and will not be automatically rearranged.
*   **`widgets`**: This property holds the array of widgets *currently displayed* on the dashboard. It is usually populated and modified by the user at runtime. While `availableWidgets` is the design-time library, `widgets` is the runtime instance state. You generally do not configure this property directly in the Designer unless you want to define a default, non-empty layout.

---

### **Helpful Tips**

*   **`availableWidgets` vs. `widgets`**: Remember the distinction. You, the designer, set up the *templates* in `availableWidgets`. The end-user, in the session, uses these templates to add *instances* to the `widgets` array.
*   **`viewParams` are Critical**: The keys in the `viewParams` object (in both `availableWidgets` and `widgets`) must perfectly match the parameter names on the View being loaded into the widget. If they don't match, the parameters will not be passed correctly.
*   **Configuring Widget Views**: The `isConfigurable` property is very powerful. You can design a single View that uses an internal parameter (e.g., `self.view.params.configuring`). When this parameter is true, you can show configuration controls (like a dropdown to select a machine) and hide the normal display. When it's false, you show the display (like the machine's status).
*   **Sizing and Spans**: The size and position of widgets are defined in terms of grid units, not pixels. A widget with `columnSpan: 2` and `rowSpan: 3` will take up a 2x3 block of grid cells.
*   **`pack` for Automatic Layouts**: For a classic dashboard experience where widgets neatly tile themselves, keep `pack` set to `true`. If you need a free-form layout where the user has pixel-perfect control over placement (and can create overlaps), set `pack` to `false`.
*   **Responsive Design**: The `stretch` grid mode is generally better for responsive designs that need to work on various screen sizes, as it adapts to the available space. The `fixed` mode is better when you need a consistent, pixel-perfect layout where the visual scale is always the same.
*   **Styling**: You can apply styles at multiple levels. The main `style` property affects the entire Dashboard component. You can also define a `style` object for each widget template in `availableWidgets`, and even separately for the widget's `header` and `body`.
*   **Default Layout**: If you want the dashboard to start with a specific set of widgets already in place, you can pre-populate the `widgets` array in the Designer. This defines the default state for a new session. The user can then modify this layout if `editingToggle` is enabled.

# Schema - raw
{"schema":{"type":"object","properties":{"isEditing":{"description":"Whether the dashboard is in runtime edit mode.","type":"boolean","default":false},"widgets":{"description":"Widgets currently in dashboard display.","type":"array","default":[],"items":{"type":"object","properties":{"isConfigurable":{"description":"If enabled, provides a toggle that becomes available when a widget is selected which is used to configure the widgets view. When the toggled on, the configuring view parameter will be true.","type":"boolean","default":false},"body":{"description":"Widget body configuration.","type":"object","properties":{"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"viewPath":{"format":"view-path","description":"The current configured view path of the widget.","type":"string","default":""},"name":{"description":"The unique widget name.","type":"string","default":""},"header":{"description":"Widget header configuration.","type":"object","properties":{"title":{"description":"The header title.","type":"string","default":""},"enabled":{"description":"Whether the widget header should show.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"minSize":{"description":"This widgets minimum size used when determining widget layout.","type":"object","properties":{"columnSpan":{"description":"The minimum allowable columns that this widget may span.","type":"number","default":1},"rowSpan":{"description":"The minimum allowable rows that this widget may span.","type":"number","default":1}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"position":{"description":"The widgets position in the dashboard.","type":"object","required":["rowStart","rowEnd","columnStart","columnEnd"],"properties":{"columnEnd":{"type":"number","default":2},"columnStart":{"type":"number","default":1},"rowStart":{"type":"number","default":1},"rowEnd":{"type":"number","default":2}}},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"description":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","type":"object","default":{}}}}},"pack":{"description":"Enables widget packing algorithm. When disabled, widgets can be placed anywhere on the Dashboard and the component will not try to rearrange them in an optimal layout.","type":"boolean","default":true},"editingToggle":{"description":"Whether to display the dashboard editing toggle.","type":"boolean","default":true},"stretch":{"visibleWhen":{"equals":"stretch","property":"grid"},"description":"Stretch configuration used when dashboard mode is stretch.","type":"object","required":["rowCount","columnCount"],"properties":{"rowGutterSize":{"description":"The size of the grid gaps or gutters between rows in pixels.","type":"number","default":6},"columnCount":{"description":"The number of columns in the grid","type":"number","default":8},"rowCount":{"description":"The number of rows in the grid","type":"number","default":8},"columnGutterSize":{"description":"The size of the grid gaps or gutters between columns in pixels.","type":"number","default":6}}},"availableWidgets":{"type":"array","default":[],"items":{"type":"object","properties":{"isConfigurable":{"description":"If enabled, provides a toggle that becomes available when a widget is selected which is used to configure the widgets view. When the toggled on, the configuring view parameter will be true.","type":"boolean","default":false},"body":{"description":"Widget body configuration.","type":"object","properties":{"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"viewPath":{"format":"view-path","description":"The primary view path of the widget.","type":"string","default":""},"defaultSize":{"type":"object","properties":{"columnSpan":{"type":"number","default":2},"rowSpan":{"type":"number","default":2}}},"name":{"description":"A unique name to provide this widget.  This is used in the add widget modal.","type":["string","number"],"default":""},"header":{"description":"Widget header configuration","type":"object","properties":{"title":{"description":"The header title.","type":"string","default":""},"enabled":{"description":"Whether the widget header should show.","type":"boolean","default":true},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"minSize":{"description":"This widgets minimum size used when determining widget layout.","type":"object","properties":{"columnSpan":{"description":"The minimum allowable columns that this widget may span.","type":"number","default":1},"rowSpan":{"description":"The minimum allowable rows that this widget may span.","type":"number","default":1}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"type":"object","descriptions":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","default":{}},"category":{"description":"A category in which to group this widget when displayed in the add widgets modal.","type":["string","number"],"default":""}}}},"grid":{"description":"The grids layout mode.","type":"string","enum":["fixed","stretch"],"default":"stretch"},"fixed":{"visibleWhen":{"equals":"fixed","property":"grid"},"description":"Fixed configuration used when dashboard mode is fixed.","type":"object","required":["cellSize","rowCount","columnCount"],"properties":{"rowGutterSize":{"description":"The size of the grid gaps or gutters between rows in pixels.","type":"number","default":6},"columnCount":{"description":"The number of columns in the grid","type":"number","default":10},"cellSize":{"description":"Grid cell size in pixels.","type":"number","default":100},"rowCount":{"description":"The number of rows in the grid","type":"number","default":10},"columnGutterSize":{"description":"The size of the grid gaps or gutters between columns in pixels.","type":"number","default":6}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Dashboard","name":"Dashboard","palette":{"variants":[{"tooltip":"Exposes layout capabilities to end users in a Perspective Session. Widgets are configured in the Designer by designers and made available to Perspective Session users.","label":"Dashboard"}],"category":"display"},"id":"ia.display.dashboard"}