# Perspective Component Meta Properties

## Description

This guide covers the configuration and usage of a Perspective component's universal `meta` properties. These instructions explain how to define a component's name and visibility, as well as how to create and customize interactive features like hover-over tooltips and complex right-click context menus. It also details how these properties are used to set a component's DOM ID for automated testing and tab index for accessibility.

## Documentation

# Instructions
This document provides instructions for using the `meta` properties of a Perspective component. These properties are common to all components and are used to configure metadata and other non-style-related aspects of a component's appearance and behavior.

### `meta` Object Properties:

The `meta` object contains several properties that control the component's name, visibility, and interactive features like tooltips and context menus.

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of the component. This name is used when navigating component tree paths, such as in property bindings or scripts. |
| `visible` | `boolean` | If `true`, the component is visible. If `false`, it is hidden. Defaults to `true`. |
| `tooltip` | `object` | An object that configures a tooltip to be displayed when the user hovers over the component. |
| `contextMenu` | `object` | An object that configures a context menu (right-click menu) for the component. |
| `domId` | `string` | A hidden-by-default property. When added, its value becomes the DOM `id` of the output HTML element. This is primarily intended for use with testing frameworks like Selenium. |
| `tabIndex` | `number` | A hidden-by-default property. When added, it allows you to set an integer value to establish the sequence in which each component will receive focus when a user tabs through the page. |

---

### `tooltip` Object:

The `tooltip` object configures a hover-over tooltip for the component.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | `boolean` | `false` | If `true`, the tooltip will display on hover or when requested by a script. |
| `width` | `number` or `string` | `"auto"` | The display width of the tooltip. Can be a number (pixels) or a string (e.g., "60px", "100pt", "auto"). |
| `text` | `string` | `""` | The message to display in the tooltip. |
| `style` | `object` | | A standard style object to customize the tooltip's appearance. |
| `delay` | `number` | `500` | The time in milliseconds to wait before displaying the tooltip after a hover starts. A value of 0 is immediate. |
| `sustain` | `number` | `10000` | The time in milliseconds the tooltip remains visible. A value of 0 means it stays until the mouse leaves the component. |
| `location` | `string` | `"mouse"` | Where the tooltip appears relative to the component. Valid values: `"mouse"`, `"top"`, `"top-right"`, `"top-left"`, `"center"`, `"center-right"`, `"center-left"`, `"bottom"`, `"bottom-right"`, `"bottom-left"`. |
| `tail` | `boolean` | `true` | If `true`, a decorative triangle points from the tooltip to the component. This is ignored if `location` is `"mouse"`. |

---

### `contextMenu` Object:

The `contextMenu` object configures a menu that appears when the component is right-clicked.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | `boolean` | `false` | If `true`, the context menu is active. |
| `items` | `array` | `[]` | An array of item objects to display in the menu. |
| `style` | `object` | | A standard style object for the context menu itself. |

#### `contextMenu.items` Array:

This is an array of objects, where each object defines an item in the context menu.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `string` | `"menu-item"` | The text to display for the menu item. Not applicable for the `separator` type. |
| `icon` | `object` | | An icon to display next to the text. Not applicable for the `separator` type. See `icon` object details below. |
| `style` | `object` | | A standard style object for this specific menu item. |
| `type` | `string` | `"link"` | The type of menu item. Determines its function. Valid values: `"submenu"`, `"link"`, `"method"`, `"message"`, `"separator"`. |
| `children` | `array` | `[]` | *Visible only when `type` is `"submenu"`*. An array of other context menu item objects that form the submenu. |
| `link` | `object` | | *Visible only when `type` is `"link"`*. Configures the hyperlink. See `link` object details below. |
| `method` | `object` | | *Visible only when `type` is `"method"`*. Configures the component method to call. See `method` object details below. |
| `message` | `object` | | *Visible only when `type` is `"message"`*. Configures the message to dispatch. See `message` object details below. |

---

#### `icon` Object:

Used within `contextMenu.items` to define an icon.

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `string` | `""` | Shorthand path to the icon, in the format `library/iconName`. |
| `library` | `string` | | The name of the icon library. Must be used with `name`. |
| `name` | `string` | | The name of the icon. Must be used with `library`. |
| `color` | `string` | `""` | The color of the icon. Can also be set via the `fill` property in `style`. |
| `style` | `object` | `{}` | A standard style object for the icon. |

---

#### `contextMenu` Item Type Details:

##### `link` Object (`type: "link"`):

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `url` | `string` | `""` | The URL to navigate to. For internal project pages, use the configured URL path (e.g., `/my-view/my-page`). |
| `target` | `string` | `"self"` | Determines where to open the link. `"self"` opens in the current context; `"tab"` opens in a new browser tab. |

##### `method` Object (`type: "method"`):

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `string` | `""` | The name of the custom method (defined on the component) to invoke when clicked. |
| `params` | `object` | `{}` | An object of parameters to pass to the method. Positional arguments are not supported. |

##### `message` Object (`type: "message"`):

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | `string` | `""` | The message type (string identifier) that will trigger component message handlers with the same type value. |
| `payload` | `object` | `{}` | The payload object to pass to the message handlers. |
| `scope` | `string` | `"page"` | Defines the scope the message will be sent on. Valid values: `"session"`, `"page"`, `"view"`. |

---

### Helpful Tips & General Knowledge

*   **Meta Properties are Universal:** The `meta` properties described here are available on every Perspective component.
*   **Creating Multi-Line Tooltips:** To make a tooltip display on multiple lines:
    1.  Set the `meta.tooltip.style.white-space` property to `"pre"`.
    2.  In the `meta.tooltip.text` property, use the newline character `\n` to separate lines. For example, in an expression binding: `"Line 1" + "\n" + "Line 2"`.
*   **`domId` for Testing:** The primary use for the `meta.domId` property is to assign a predictable HTML `id` to a component's element, making it easier to select and interact with in automated testing tools.
*   **`tabIndex` for Accessibility:** Use `meta.tabIndex` to define a logical navigation order for users who rely on the `Tab` key to move through the interactive elements on a page.
*   **Context Menu Behavior:** Once opened with a right-click, a context menu will remain visible until the user clicks somewhere else on the view.
*   **Context Menu Item Types:**
    *   **`submenu`**: Creates a nested menu. An arrow icon `>` appears automatically if the `children` array is not empty.
    *   **`link`**: Creates a hyperlink. To link to a page within the same Ignition project, use the page's configured URL (e.g., `/path/to/page`).
    *   **`method`**: Calls a custom script method defined on the same component that the context menu belongs to.
    *   **`message`**: Dispatches a Perspective message. This is useful for communicating with other components or parts of the application using message handlers.
    *   **`separator`**: Displays a non-interactive horizontal line, useful for visually grouping related items in the menu.

# Schema - raw
{"title":"Perspective Component Meta Properties","definitions":{"css-length-unit":{"oneOf":[{"type":"string","pattern":"^(auto|0)$|^[+-]?[0-9]+.?([0-9]+)?(px|em|ex|%|in|cm|mm|pt|pc|rem)$"},{"type":"number"}]},"length":{"type":"object","properties":{"value":{"type":"integer","default":"2"},"unit":{"type":"string","enum":["px","em","%"],"default":"px"}}},"time":{"type":"object","properties":{"value":{"type":"integer","default":"2"},"unit":{"type":"string","enum":["s","ms"],"default":"s"}}},"overflow":{"type":"string","enum":["visible","scroll","hidden","auto"]},"borderStyle":{"enum":["none","hidden","dotted","dashed","solid","double","groove","ridge","inset","outset"],"type":"string"},"style":{"type":"object","format":"inline-style","default":{"classes":""},"properties":{"classes":{"type":["array","string"],"format":"style-list","title":"Style Class Names","description":"Styles defined in the project to be applied to this component","default":""},"alignContent":{"enum":["stretch","space-between","space-around","flex-start","flex-end","center"],"required":true,"type":"string"},"alignItems":{"enum":["stretch","flex-start","flex-end","center","baseline"],"required":true,"type":"string"},"alignSelf":{"enum":["auto","stretch","flex-start","flex-end","center","baseline"],"required":true,"type":"string"},"all":{"enum":["initial","unset","inherit"],"required":true,"type":"string"},"animationDelay":{"$ref":"#/definitions/time"},"animationDirection":{"enum":["normal","reverse","alternate-reverse","alternate"],"required":true,"type":"string"},"animationDuration":{"type":"string"},"animationFillMode":{"enum":["none","forwards","both","backwards"],"required":true,"type":"string"},"animationPlayMode":{"enum":["running","paused"],"required":true,"type":"string"},"backfaceVisibility":{"enum":["visible","hidden"],"required":true,"type":"string"},"backgroundAttachment":{"enum":["scroll","local","fixed"],"required":true,"type":"string"},"backgroundClip":{"enum":["border-box","padding-box","content-box"],"required":true,"type":"string"},"backgroundColor":{"default":"#ffa500","format":"color","title":"background-color","type":"string"},"backgroundOrigin":{"enum":["padding-box","content-box","border-box"],"required":true,"type":"string"},"backgroundRepeat":{"enum":["repeat","space","round","repeat-y","repeat-x","repeat no-repeat","no-repeat"],"required":true,"type":"string"},"backgroundSize":{"required":true,"type":"string"},"borderCollapse":{"enum":["separate","collapse"],"required":true,"type":"string"},"borderStyle":{"$ref":"#/definitions/borderStyle"},"borderStyleTop":{"$ref":"#/definitions/borderStyle"},"borderImageRepeat":{"enum":["stretch","space","round","repeat"],"required":true,"type":"string"},"boxDecorationBreak":{"enum":["slice","clone"],"required":true,"type":"string"},"boxSizing":{"enum":["content-box","padding-box","border-box"],"required":true,"type":"string"},"breakAfter":{"enum":["auto","right","page","left","column","avoid-page","avoid-column","avoid","always"],"required":true,"type":"string"},"breakBefore":{"enum":["auto","right","page","left","column","avoid-page","avoid-column","avoid","always"],"required":true,"type":"string"},"breakInside":{"enum":["auto","avoid-page","avoid-column","avoid"],"required":true,"type":"string"},"captionSide":{"enum":["top","bottom"],"required":true,"type":"string"},"clear":{"enum":["none","right","left","both"],"required":true,"type":"string"},"clearAfter":{"enum":["none","top","start","right","outside","left","inside","end","descendants","bottom","both"],"required":true,"type":"string"},"color":{"default":"#ffa500","format":"color","title":"color","type":"string"},"columnFill":{"enum":["balance","auto"],"required":true,"type":"string"},"columnRuleStyle":{"enum":["none","solid","ridge","outset","inset","hidden","groove","double","dotted","dashed"],"required":true,"type":"string"},"columnSpan":{"enum":["none","all"],"required":true,"type":"string"},"display":{"enum":["inline","table-row-group","table-row","table-header-group","table-footer-group","table-column-group","table-column","table-cell","table-caption","table","run-in","none","list-item","inline-table","inline-flex","inline-block","flex","compact","block"],"required":true,"type":"string"},"emptyCells":{"enum":["show","hide"],"required":true,"type":"string"},"fill":{"format":"color","title":"fill","type":"string"},"flexDirection":{"enum":["row","row-reverse","column-reverse","column"],"required":true,"type":"string"},"flexWrap":{"enum":["nowrap","wrap-reverse","wrap"],"required":true,"type":"string"},"float":{"enum":["none","right","left"],"required":true,"type":"string"},"fontFamily":{"title":"font-family","type":"string"},"fontKerning":{"enum":["auto","normal","none"],"required":true,"type":"string"},"fontSize":{"required":false,"type":["string","number"]},"fontStretch":{"enum":["normal","ultra-expanded","ultra-condensed","semi-expanded","semi-condensed","extra-expanded","extra-condensed","expanded","condensed"],"required":true,"type":"string"},"fontStyle":{"enum":["normal","oblique","italic"],"required":true,"type":"string"},"fontSynthesis":{"enum":["weight style","weight","style","none"],"required":true,"type":"string"},"fontVariant":{"enum":["normal","unicase","titling-caps","small-caps","petite-caps","all-small-caps","all-petite-caps"],"required":true,"type":"string"},"fontVariantCaps":{"enum":["normal","unicase","titling-caps","small-caps","petite-caps","all-small-caps","all-petite-caps"],"required":true,"type":"string"},"fontWeight":{"enum":["normal","lighter","bolder","bold","900","800","700","600","500","400","300","200","100"],"required":true,"type":"string"},"hangingPunctuation":{"enum":["none","last force-end","last allow-end","last","force-end","first force-end","first allow-end","first","allow-end"],"required":true,"type":"string"},"hyphens":{"enum":["manual","none","auto"],"required":true,"type":"string"},"imageResolution":{"enum":["1dppx","from-image"],"required":true,"type":"string"},"justifyContent":{"enum":["flex-start","space-between","space-around","flex-end","center"],"required":true,"type":"string"},"lineBreak":{"enum":["auto","strict","normal","loose"],"required":true,"type":"string"},"listStylePosition":{"enum":["outside","inside"],"required":true,"type":"string"},"listStyleType":{"enum":["disc","upper-roman","upper-latin","upper-alpha","square","none","lower-roman","lower-latin","lower-greek","lower-alpha","georgian","decimal-leading-zero","decimal","circle","armenian"],"required":true,"type":"string"},"marginBottom":{"$ref":"#/definitions/css-length-unit"},"marginLeft":{"$ref":"#/definitions/css-length-unit"},"marginRight":{"$ref":"#/definitions/css-length-unit"},"marginTop":{"$ref":"#/definitions/css-length-unit"},"objectFit":{"enum":["fill","scale-down","none","cover","contain"],"required":true,"type":"string"},"opacity":{"type":["number","string"]},"outlineStyle":{"enum":["none","solid","ridge","outset","inset","groove","double","dotted","dashed","auto"],"required":true,"type":"string"},"overflow":{"$ref":"#/definitions/overflow"},"overflowWrap":{"enum":["normal","break-word"],"required":true,"type":"string"},"overflowX":{"$ref":"#/definitions/overflow"},"overflowY":{"$ref":"#/definitions/overflow"},"paddingBottom":{"$ref":"#/definitions/css-length-unit"},"paddingLeft":{"$ref":"#/definitions/css-length-unit"},"paddingRight":{"$ref":"#/definitions/css-length-unit"},"paddingTop":{"$ref":"#/definitions/css-length-unit"},"pageBreakAfter":{"enum":["auto","right","left","avoid","always"],"required":true,"type":"string"},"pageBreakBefore":{"enum":["auto","right","left","avoid","always"],"required":true,"type":"string"},"pageBreakInside":{"enum":["auto","avoid"],"required":true,"type":"string"},"pointerEvents":{"enum":["auto","none"],"required":true,"type":"string"},"position":{"enum":["static","sticky  ","relative","page","fixed","center","absolute"],"required":true,"type":"string"},"resize":{"enum":["none","vertical","horizontal","both"],"required":true,"type":"string"},"tableLayout":{"enum":["auto","fixed"],"required":true,"type":"string"},"textAlignLast":{"enum":["auto","start","right","left","justify","end","center"],"required":true,"type":"string"},"textDecorationLine":{"enum":["none","underline","overline","line-through","blink"],"required":true,"type":"string"},"textDecorationPosition":{"enum":["auto","under right","under left","under","right","left"],"required":true,"type":"string"},"textDecorationSkip":{"enum":["none","spaces","objects","ink","edges","box-decoration"],"required":true,"type":"string"},"textDecorationStyle":{"enum":["solid","wavy","double","dotted","dashed"],"required":true,"type":"string"},"textEmphasisPosition":{"enum":["over right","over left","below right","below left"],"required":true,"type":"string"},"textJustify":{"enum":["auto","none","inter-word","distribute"],"required":true,"type":"string"},"textOrientation":{"enum":["mixed","use-glyph-orientation","upright","sideways-right","sideways-left","sideways"],"required":true,"type":"string"},"textTransform":{"enum":["none","uppercase","lowercase","full-width","capitalize"],"required":true,"type":"string"},"transformStyle":{"enum":["flat","preserve-3d"],"required":true,"type":"string"},"unicodeBidi":{"enum":["normal","embed","bidi-override"],"required":true,"type":"string"},"visibility":{"enum":["visible","hidden","collapse"],"required":true,"type":"string"},"whiteSpace":{"enum":["normal","pre-wrap","pre-line","pre","nowrap"],"required":true,"type":"string"},"wordBreak":{"enum":["normal","keep-all","break-all"],"required":true,"type":"string"},"wordWrap":{"enum":["normal","break-word"],"required":true,"type":"string"},"writingMode":{"enum":["horizontal-tb","vertical-rl","vertical-lr"],"required":true,"type":"string"}}}},"type":"object","properties":{"name":{"type":"string","pattern":"^[a-zA-Z_][a-zA-Z_ ()\\-0-9]*$","description":"The name of the component, used when navigating component tree paths by name (such as during Property Bindings)."},"visible":{"description":"Whether or not this component should be visible.","type":"boolean","default":true},"tooltip":{"description":"Tooltip configuration to display for currently selected component.","type":"object","properties":{"enabled":{"type":"boolean","description":"Whether the tooltip should display on hover and when requested.","default":false},"width":{"type":["number","string"],"description":"The display width of the tooltip. Defaults to a value of 'auto'.","default":"auto"},"text":{"type":"string","default":"","description":"The message to display in the component tooltip."},"style":{"$ref":"#/definitions/style"},"delay":{"type":"number","default":500,"description":"Time, in milliseconds, to wait before the tooltip is displayed when requested or when component is hovered over. A value of 0 results in immediate display."},"sustain":{"type":"number","default":10000,"description":"Time, in milliseconds, to display tooltip before removing it. A value of 0 results in the tooltip displaying until the mouse exits the component."},"location":{"type":"string","description":"The location of where to display tooltip.","enum":["mouse","top","top-right","top-left","center","center-right","center-left","bottom","bottom-right","bottom-left"],"default":"mouse"},"tail":{"type":"boolean","description":"Enables a decorative triangle on the tooltip that points to the tooltip owner. Ignored when location uses a value of 'mouse'.","default":true}}},"contextMenu":{"description":"Context Menu configuration to display for currently selected component.","type":"object","properties":{"enabled":{"type":"boolean","default":false,"description":"Determines if the context menu for this component is on or off."},"items":{"type":"array","description":"Items of configuration for context menu","items":{"type":"object","description":"A context menu item configuration object.","properties":{"text":{"type":"string","description":"Text to display on the context menu item.","default":"menu-item","visibleWhen":{"property":"type","equals":["submenu","link","method","message"]}},"icon":{"type":"object","description":"Icon configuration for context menu item.","properties":{"path":{"type":"string","default":"","description":"Shorthand path to icon source, in format: library/iconName","format":"icon-path"},"library":{"type":"string","description":"Optional alternative to 'path', name of library where icon is located. Must also supply 'name'."},"name":{"type":"string","description":"Optional alternative to 'path', name of icon. Must also supply 'library'."},"color":{"type":"string","format":"color","default":"","description":"Color of the icon. Here for convenience, may instead assign 'fill' in the styles prop."},"style":{"$ref":"#/definitions/style","default":{}}},"oneOf":[{"required":["path"]},{"required":["library","name"]}],"default":{"path":"","color":"","style":{}},"visibleWhen":{"property":"type","equals":["link","message","method","submenu"]}},"style":{"description":"Style configuration for context menu item.","$ref":"#/definitions/style"},"type":{"type":"string","description":"Type of context menu item to display.","enum":["submenu","link","method","message","separator"],"default":"link"},"children":{"type":"array","description":"Array of children items to display from the configured submenu.","items":{"$ref":"#/properties/contextMenu/properties/items/items"},"default":[],"visibleWhen":{"property":"type","equals":["submenu"]}},"link":{"type":"object","description":"Link context menu item configuration.","visibleWhen":{"property":"type","equals":"link"},"properties":{"url":{"type":"string","default":"","description":"Url to be used for the configured link menu item."},"target":{"type":"string","enum":["self","tab"],"default":"self","description":"Target attribute to give the link menu item that determines in which context the link will be opened when clicked."}}},"method":{"type":"object","description":"Method context menu item configuration.","visibleWhen":{"property":"type","equals":["method"]},"properties":{"name":{"type":"string","default":"","description":"Name of method to be invoked when this menu item is clicked."},"params":{"type":"object","description":"Object of params to pass to the method that is invoked when this menu item is clicked.","default":{}}}},"message":{"type":"object","description":"Message context menu item configuration.","visibleWhen":{"property":"type","equals":["message"]},"properties":{"type":{"type":"string","default":"","description":"Defines the message type that will trigger all component message handlers with the same type value"},"payload":{"type":"object","default":{},"description":"Payload object used to pass defined payload for message handlers"},"scope":{"type":"string","default":"page","enum":["session","page","view"],"description":"Defines the scope that the message will be sent on."}}}}},"default":[]},"style":{"$ref":"#/definitions/style"}}},"domId":{"description":"If specified, the value of this property will become the DOM 'id' of the output element.","type":"string"},"tabIndex":{"description":"Determines relative ordering for sequential focus navigation.","type":["null","number"]}}}