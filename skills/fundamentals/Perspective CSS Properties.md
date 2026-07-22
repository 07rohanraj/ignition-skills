# Perspective CSS Properties

## Description

This guide explains how to apply visual styles to components in Ignition's Perspective module by configuring the `style` property object or creating Style Classes. It outlines the available camelCase CSS properties, categorized into groups such as text, layout, and background, and includes essential tips for proper implementation and best practices.

## Documentation

# Instructions
Here are the instructions for the LLM on how to use Perspective CSS Properties.

# Perspective CSS Properties

## Instructions

You are to use these instructions to apply styling to components within Ignition's Perspective module. Styling is accomplished by modifying a component's `style` property, which is an object that directly corresponds to CSS properties. These properties can also be used when creating Style Classes.

All property names use camelCase (e.g., `backgroundColor`) instead of the traditional kebab-case (`background-color`) found in CSS.

### 1. General Usage

To apply a style, you will modify the target component's `style` object. For example, to change a Label's text color to red and its font size to 20 pixels, you would configure its `style` property as follows:

```json
{
  "color": "#FF0000",
  "fontSize": 20
}
```

### 2. Main Style Property Groups

The available style properties can be broken down into the following logical groups:

#### Text and Font Styling
These properties control the appearance of text.

*   **`color`**: Sets the color of the text. Can be a HEX, RGB, or HSL value.
*   **`fontFamily`**: Specifies the font (e.g., "Arial", "Monospace").
*   **`fontSize`**: Sets the size of the font. If a number is provided, it is assumed to be in pixels (`px`). You can also provide a string with a unit (e.g., "1.2em", "90%").
*   **`fontWeight`**: Sets the thickness of the font. Common values are `"normal"`, `"bold"`, `"lighter"`, and `"bolder"`, or a numeric value from `"100"` to `"900"`.
*   **`fontStyle`**: Used to make text italic (`"italic"`) or oblique (`"oblique"`).
*   **`textAlign`**: Specifies the horizontal alignment of text. Values include `"left"`, `"right"`, `"center"`, and `"justify"`.
*   **`textDecorationLine`**: Adds a decorative line to text, such as `"underline"`, `"overline"`, or `"line-through"`.
*   **`textTransform`**: Changes the capitalization of text, with values like `"uppercase"`, `"lowercase"`, or `"capitalize"`.
*   **`lineHeight`**: Specifies the height of a line of text.
*   **`letterSpacing`**: Increases or decreases the space between characters.
*   **`wordSpacing`**: Increases or decreases the space between words.

#### Background
These properties control the background of a component.

*   **`backgroundColor`**: Sets the background color of the component.
*   **`backgroundImage`**: Sets a background image using a URL (e.g., `url("http://example.com/image.png")`). Can also be used to create linear or radial gradients.
*   **`backgroundRepeat`**: Defines if/how a background image should be repeated (e.g., `"no-repeat"`, `"repeat-x"`).
*   **`backgroundSize`**: Sets the size of the background image.
*   **`backgroundPosition`**: Sets the starting position of a background image.

#### Sizing, Spacing, and Layout
These properties control the dimensions, spacing, and positioning of components.

*   **Margin (`marginTop`, `marginRight`, `marginBottom`, `marginLeft`)**: Sets the space *outside* of a component's border.
*   **Padding (`paddingTop`, `paddingRight`, `paddingBottom`, `paddingLeft`)**: Sets the space *inside* a component's border, between the border and the content.
*   **`position`**: Specifies the positioning method. Common values are `"static"`, `"relative"`, `"absolute"`, and `"fixed"`.
*   **`display`**: Specifies the display behavior of a component (e.g., `"block"`, `"inline"`, `"flex"`, `"none"`).
*   **`overflow`**, **`overflowX`**, **`overflowY`**: Defines what happens when content overflows its container. Values can be `"visible"`, `"hidden"`, `"scroll"`, or `"auto"`.
*   **`boxSizing`**: Defines how the total width and height of an element is calculated. Can be `"content-box"` (default) or `"border-box"`.

#### Borders and Outlines
These properties control the component's borders.

*   **`borderStyle`**: Sets the style for all four borders (e.g., `"solid"`, `"dotted"`, `"dashed"`). You can also set styles for individual sides (`borderStyleTop`, etc.).
*   **`borderWidth`**: Sets the width of the border. Assumed to be in pixels if only a number is provided.
*   **`borderColor`**: Sets the color of the border.
*   **`borderRadius`**: Used to create rounded corners. You can also set the radius for individual corners (`borderTopLeftRadius`, etc.).
*   **`outlineStyle`**: Specifies the style of an outline drawn around a component, outside the border edge.

#### Flex Container Properties
When a container's `display` property is set to `"flex"`, you can use these properties on the container to control the alignment and distribution of its children.

*   **`flexDirection`**: Defines the direction of the main axis (`"row"`, `"column"`).
*   **`justifyContent`**: Aligns flex items along the main axis (`"flex-start"`, `"center"`, `"space-between"`).
*   **`alignItems`**: Aligns flex items along the cross axis (`"stretch"`, `"center"`, `"flex-start"`).
*   **`flexWrap`**: Specifies whether flex items should wrap onto multiple lines (`"nowrap"`, `"wrap"`).

#### Miscellaneous Properties
*   **`opacity`**: Sets the transparency level of a component, from `1` (fully opaque) to `0` (fully transparent).
*   **`cursor`**: Specifies the mouse cursor to display when hovering over the component (e.g., `"pointer"`, `"wait"`, `"text"`).
*   **`visibility`**: Can show (`"visible"`) or hide (`"hidden"`) an element. Note that a hidden element still takes up space in the layout.
*   **`pointerEvents`**: Can disable mouse interactions on an element by setting it to `"none"`.

## Helpful Tips

*   **Units**: For any property that accepts a length (e.g., `fontSize`, `padding`, `margin`, `borderWidth`), if you provide just a number, it will be interpreted as pixels (`px`). To use other units like percentages (`%`), em (`em`), or seconds (`s`), you must provide the value as a string (e.g., `fontSize: "1.5em"`).
*   **Color Theme Variables**: Perspective has built-in themes (`light`, `dark`, etc.) that provide a palette of CSS color variables. These variables (e.g., `--callToAction`, `--neutral-90`, `--error`) can be used to ensure your application has a consistent look and feel that adapts to the selected theme.
*   **Using Theme Variables**:
    *   When applying a style directly to a component's `style` object, you can just use the variable name as a string: `backgroundColor: "--callToAction"`.
    *   When defining a style within a **Style Class**, you **must** wrap the variable name in the `var()` function: `backgroundColor: "var(--callToAction)"`.
*   **Overflow Behavior**: For the `textOverflow: "ellipsis"` property to work and show "...", the element's content must actually be overflowing. This typically requires you to also set `overflow: "hidden"` and `white-space: "nowrap"` on the same style object.
*   **Individual Border Sides**: You can style all four borders at once using properties like `borderStyle` and `borderColor`. To style each side individually, use the more specific properties like `borderStyleTop`, `borderColorTop`, etc.
*   **`display: "none"` vs. `visibility: "hidden"`**: Use `display: "none"` to completely remove a component from the view and the document flow (it will not take up any space). Use `visibility: "hidden"` to hide a component but have it retain its space in the layout.
*   **Modifying Built-in Themes**: Avoid making changes directly to the built-in theme files. These changes can be lost on a Gateway restart or upgrade. For custom, persistent theme changes, create your own custom theme files.
*   **External CSS Documentation**: These style properties are based on standard CSS. For more in-depth examples and explanations of what a specific property does, refer to the MDN CSS Reference documentation online, keeping in mind that property names are in camelCase.

# Schema - raw
{"$schema":"http://json-schema.org/draft-04/schema#","title":"Perspective CSS Properties","definitions":{"css-length-unit":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"length":{"type":"object","properties":{"value":{"type":"integer","default":"2"},"unit":{"type":"string","enum":["px","em","%"],"default":"px"}}},"time":{"type":"object","properties":{"value":{"type":"integer","default":"2"},"unit":{"type":"string","enum":["s","ms"],"default":"s"}}},"overflow":{"type":"string","enum":["visible","scroll","hidden","auto"]},"borderStyle":{"enum":["none","hidden","dotted","dashed","solid","double","groove","ridge","inset","outset"],"type":"string"}},"type":"object","format":"inline-style","default":{},"properties":{"alignContent":{"enum":["stretch","space-between","space-around","flex-start","flex-end","center"],"required":true,"type":"string"},"alignItems":{"enum":["stretch","flex-start","flex-end","center","baseline"],"required":true,"type":"string"},"alignSelf":{"enum":["auto","stretch","flex-start","flex-end","center","baseline"],"required":true,"type":"string"},"all":{"enum":["initial","unset","inherit"],"required":true,"type":"string"},"animationDelay":{"$ref":"#/definitions/time"},"animationDirection":{"enum":["normal","reverse","alternate-reverse","alternate"],"required":true,"type":"string"},"animationDuration":{"$ref":"#/definitions/time"},"animationFillMode":{"enum":["none","forwards","both","backwards"],"required":true,"type":"string"},"animationPlayMode":{"enum":["running","paused"],"required":true,"type":"string"},"backfaceVisibility":{"enum":["visible","hidden"],"required":true,"type":"string"},"backgroundAttachment":{"enum":["scroll","local","fixed"],"required":true,"type":"string"},"backgroundClip":{"enum":["border-box","padding-box","content-box"],"required":true,"type":"string"},"backgroundColor":{"default":"#ffa500","format":"color","title":"background-color","type":"string"},"backgroundOrigin":{"enum":["padding-box","content-box","border-box"],"required":true,"type":"string"},"backgroundRepeat":{"enum":["repeat","space","round","repeat-y","repeat-x","repeat no-repeat","no-repeat"],"required":true,"type":"string"},"backgroundSize":{"required":true,"type":"string"},"borderCollapse":{"enum":["separate","collapse"],"required":true,"type":"string"},"borderStyle":{"$ref":"#/definitions/borderStyle"},"borderStyleTop":{"$ref":"#/definitions/borderStyle"},"borderImageRepeat":{"enum":["stretch","space","round","repeat"],"required":true,"type":"string"},"boxDecorationBreak":{"enum":["slice","clone"],"required":true,"type":"string"},"boxSizing":{"enum":["content-box","padding-box","border-box"],"required":true,"type":"string"},"breakAfter":{"enum":["auto","right","page","left","column","avoid-page","avoid-column","avoid","always"],"required":true,"type":"string"},"breakBefore":{"enum":["auto","right","page","left","column","avoid-page","avoid-column","avoid","always"],"required":true,"type":"string"},"breakInside":{"enum":["auto","avoid-page","avoid-column","avoid"],"required":true,"type":"string"},"captionSide":{"enum":["top","bottom"],"required":true,"type":"string"},"clear":{"enum":["none","right","left","both"],"required":true,"type":"string"},"clearAfter":{"enum":["none","top","start","right","outside","left","inside","end","descendants","bottom","both"],"required":true,"type":"string"},"color":{"default":"#ffa500","format":"color","title":"color","type":"string"},"columnFill":{"enum":["balance","auto"],"required":true,"type":"string"},"columnRuleStyle":{"enum":["none","solid","ridge","outset","inset","hidden","groove","double","dotted","dashed"],"required":true,"type":"string"},"columnSpan":{"enum":["none","all"],"required":true,"type":"string"},"display":{"enum":["inline","table-row-group","table-row","table-header-group","table-footer-group","table-column-group","table-column","table-cell","table-caption","table","run-in","none","list-item","inline-table","inline-flex","inline-block","flex","compact","block"],"required":true,"type":"string"},"emptyCells":{"enum":["show","hide"],"required":true,"type":"string"},"flexDirection":{"enum":["row","row-reverse","column-reverse","column"],"required":true,"type":"string"},"flexWrap":{"enum":["nowrap","wrap-reverse","wrap"],"required":true,"type":"string"},"float":{"enum":["none","right","left"],"required":true,"type":"string"},"fontFamily":{"title":"font-family","type":"string"},"fontKerning":{"enum":["auto","normal","none"],"required":true,"type":"string"},"fontSize":{"required":false,"type":["string","number"]},"fontStretch":{"enum":["normal","ultra-expanded","ultra-condensed","semi-expanded","semi-condensed","extra-expanded","extra-condensed","expanded","condensed"],"required":true,"type":"string"},"fontStyle":{"enum":["normal","oblique","italic"],"required":true,"type":"string"},"fontSynthesis":{"enum":["weight style","weight","style","none"],"required":true,"type":"string"},"fontVariant":{"enum":["normal","unicase","titling-caps","small-caps","petite-caps","all-small-caps","all-petite-caps"],"required":true,"type":"string"},"fontVariantCaps":{"enum":["normal","unicase","titling-caps","small-caps","petite-caps","all-small-caps","all-petite-caps"],"required":true,"type":"string"},"fontWeight":{"enum":["normal","lighter","bolder","bold","900","800","700","600","500","400","300","200","100"],"required":true,"type":"string"},"hangingPunctuation":{"enum":["none","last force-end","last allow-end","last","force-end","first force-end","first allow-end","first","allow-end"],"required":true,"type":"string"},"hyphens":{"enum":["manual","none","auto"],"required":true,"type":"string"},"imageResolution":{"enum":["1dppx","from-image"],"required":true,"type":"string"},"justifyContent":{"enum":["flex-start","space-between","space-around","flex-end","center"],"required":true,"type":"string"},"lineBreak":{"enum":["auto","strict","normal","loose"],"required":true,"type":"string"},"listStylePosition":{"enum":["outside","inside"],"required":true,"type":"string"},"listStyleType":{"enum":["disc","upper-roman","upper-latin","upper-alpha","square","none","lower-roman","lower-latin","lower-greek","lower-alpha","georgian","decimal-leading-zero","decimal","circle","armenian"],"required":true,"type":"string"},"marginBottom":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"marginLeft":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"marginRight":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"marginTop":{"$ref":"urn:ignition-schema:schemas/css-length.schema.json"},"objectFit":{"enum":["fill","scale-down","none","cover","contain"],"required":true,"type":"string"},"outlineStyle":{"enum":["none","solid","ridge","outset","inset","groove","double","dotted","dashed","auto"],"required":true,"type":"string"},"overflow":{"$ref":"#/definitions/overflow"},"overflowWrap":{"enum":["normal","break-word"],"required":true,"type":"string"},"overflowX":{"$ref":"#/definitions/overflow"},"overflowY":{"$ref":"#/definitions/overflow"},"paddingBottom":{"$ref":"#/definitions/css-length-unit"},"paddingLeft":{"$ref":"#/definitions/css-length-unit"},"paddingRight":{"$ref":"#/definitions/css-length-unit"},"paddingTop":{"$ref":"#/definitions/css-length-unit"},"pageBreakAfter":{"enum":["auto","right","left","avoid","always"],"required":true,"type":"string"},"pageBreakBefore":{"enum":["auto","right","left","avoid","always"],"required":true,"type":"string"},"pageBreakInside":{"enum":["auto","avoid"],"required":true,"type":"string"},"pointerEvents":{"enum":["auto","none"],"required":true,"type":"string"},"position":{"enum":["static","sticky  ","relative","page","fixed","center","absolute"],"required":true,"type":"string"},"resize":{"enum":["none","vertical","horizontal","both"],"required":true,"type":"string"},"tableLayout":{"enum":["auto","fixed"],"required":true,"type":"string"},"textAlignLast":{"enum":["auto","start","right","left","justify","end","center"],"required":true,"type":"string"},"textDecorationLine":{"enum":["none","underline","overline","line-through","blink"],"required":true,"type":"string"},"textDecorationPosition":{"enum":["auto","under right","under left","under","right","left"],"required":true,"type":"string"},"textDecorationSkip":{"enum":["none","spaces","objects","ink","edges","box-decoration"],"required":true,"type":"string"},"textDecorationStyle":{"enum":["solid","wavy","double","dotted","dashed"],"required":true,"type":"string"},"textEmphasisPosition":{"enum":["over right","over left","below right","below left"],"required":true,"type":"string"},"textJustify":{"enum":["auto","none","inter-word","distribute"],"required":true,"type":"string"},"textOrientation":{"enum":["mixed","use-glyph-orientation","upright","sideways-right","sideways-left","sideways"],"required":true,"type":"string"},"textTransform":{"enum":["none","uppercase","lowercase","full-width","capitalize"],"required":true,"type":"string"},"transformStyle":{"enum":["flat","preserve-3d"],"required":true,"type":"string"},"unicodeBidi":{"enum":["normal","embed","bidi-override"],"required":true,"type":"string"},"visibility":{"enum":["visible","hidden","collapse"],"required":true,"type":"string"},"whiteSpace":{"enum":["normal","pre-wrap","pre-line","pre","nowrap"],"required":true,"type":"string"},"wordBreak":{"enum":["normal","keep-all","break-all"],"required":true,"type":"string"},"wordWrap":{"enum":["normal","break-word"],"required":true,"type":"string"},"writingMode":{"enum":["horizontal-tb","vertical-rl","vertical-lr"],"required":true,"type":"string"}}}