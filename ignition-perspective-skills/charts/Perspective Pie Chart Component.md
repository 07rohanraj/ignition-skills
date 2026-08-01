# Perspective Pie Chart Component

## Description

The configuration and usage of the Perspective Pie Chart component, detailing how to bind data and extensively customize its appearance and behavior. This includes altering the visual style to a pie, donut, or 3D chart, modifying colors, and managing the display of labels, the legend, and tooltips. The instructions also cover formatting numeric values and enabling user interactivity through slice selection.

## Documentation

# Instructions
Here are the instructions for the **Perspective Pie Chart Component** in Ignition.

### Component Overview
The Perspective Pie Chart component is used to display a list of named items, where each item's value contributes to a total. It visually represents these items as wedges of a pie, with the size of each wedge proportional to its value relative to the sum of all values. The component is highly customizable, allowing for modifications to its colors, labels, legend, and overall appearance. It can be configured to display as a traditional pie chart, a ring/donut chart, or a 3D pie chart.

### Properties

| Property | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| **data** | array / dataset | The data source for the chart. This is an array of objects, where each object defines a slice of the pie. Each object should contain a key for the name (label) and a key for the numeric value. For example: `[{"flavor":"Pumpkin","count":36}, {"label":"Pecan","value":17}]`. | `[]` |
| **colors** | array | An array of color strings (e.g., Hex, RGB) that correspond to each section in the `data` property, in the same order. If there are more data sections than colors, the colors will repeat. | `[]` |
| **title** | string | The main title displayed above the chart. | `""` |
| **titleColor** | color | The color for the chart's title text. | `""` |
| **showLabels** | boolean | If true, labels are displayed for each section of the pie. | `true` |
| **labels** | object | An object containing properties to configure the appearance of the section labels. | |
| `labels.showName` | boolean | If true, the name of the section is shown in the label. | `true` |
| `labels.showValue` | boolean | If true, the value of the section is shown in the label. Hiding this will disable value formatting. | `true` |
| `labels.color` | color | The color of the label text. | `""` |
| `labels.bent` | boolean | If true, labels will bend around the curve of the pie slices. Enabling this will disable the `align` and `wrap` properties. | `false` |
| `labels.align` | boolean | If true, the labels are aligned in vertical columns. This is disabled if `labels.bent` is true. | `true` |
| `labels.inside` | object | An object to configure labels to appear inside the chart slices. Displaying labels inside disables the `bent` and `align` properties. | |
| `labels.inside.enabled` | boolean | If true, labels will be placed inside the chart slices, provided the slice's percentage is below the `percentLimit`. | `false` |
| `labels.inside.color` | color | The color of the label text when it is displayed inside a slice. | `"#FFFFFF"` |
| `labels.inside.radius` | number | The distance of the label from the center, as a percentage (0-100). 0 is the outside edge, 100 is the center. | `80` |
| `labels.inside.percentLimit` | number | A slice's value percentage must be below this threshold to have its label placed inside the chart. | `10` |
| `labels.wrap` | object | An object to configure label text wrapping for long labels. This is disabled if `labels.bent` is true. | |
| `labels.wrap.enabled` | boolean | If true, long label text will wrap to a new line. | `false` |
| `labels.wrap.maxWidth` | number | The maximum width in pixels for a label before it wraps. | `200` |
| **showLegend** | boolean | If true, a legend is displayed for the chart. | `true` |
| **legend** | object | An object containing properties to configure the legend. | |
| `legend.position` | string | Sets the position of the legend relative to the chart. Enum: `"left"`, `"top"`, `"right"`, `"bottom"`. | `"bottom"` |
| `legend.fontSize` | number | The font size for the text in the legend. | `16` |
| `legend.icon` | object | An object to configure the color key icons in the legend. | |
| `legend.icon.enabled`| boolean | If true, the color key icons are shown in the legend. | `true` |
| `legend.icon.width` | number | The width of the legend icons in pixels. | `25` |
| `legend.icon.height`| number | The height of the legend icons in pixels. | `25` |
| **legendLabelColor** | color | The color for the legend's label text. | `""` |
| **cutoutRadius** | number | The percentage (0-99) of the chart's radius to cut out from the center. A value greater than 0 creates a ring/donut chart. | `0` |
| **sectionOutline** | object | An object to configure the border around each pie section. | |
| `sectionOutline.width`| number | The width of the border in pixels. | `0` |
| `sectionOutline.color`| color | The color of the border. | `""` |
| `sectionOutline.opacity`| number | The opacity of the border, from 0 (transparent) to 1 (opaque). | `1` |
| **valueFormat** | object | An object to configure the format of numeric values in labels and the legend. | |
| `valueFormat.showValueAsPercent`| boolean | If true, shows the section's value as a percentage of the total. If false, shows the raw value. | `true` |
| `valueFormat.showPercentSymbol`| boolean | If true, a '%' symbol is displayed next to the value (only applies when `showValueAsPercent` is true). | `true` |
| **tooltipFormat** | string | A format string for the tooltip that appears on hover. It uses placeholders and special formatting. | `"{category} : {value.percent.formatNumber('#.0')}%"` |
| **enableTransitions**| boolean | If true, the chart will animate when its data changes. | `true` |
| **threeDimensional** | boolean | If true, the chart is rendered with a 3D effect. | `false` |
| **selection** | object | An object containing properties related to slice selection. | |
| `selection.enabled` | boolean | If true, users can click on pie slices to select them. | `false` |
| `selection.data` | array | A read-only array containing the data of the currently selected slice(s). | `[]` |
| **style** | object | An object for applying standard component styling (background, border, etc.). | |

---

### `tooltipFormat` Details

The `tooltipFormat` property is a powerful string that allows for rich, custom tooltips. It recognizes special placeholders and formatting blocks.

**Placeholders (wrapped in `{}`):**
*   `{category}`: Displays the name/label of the pie slice (e.g., "Pumpkin").
*   `{value}`: Displays the raw numeric value of the slice.
*   `{value.percent}`: Displays the percentage value of the slice.
*   You can also apply formatting functions directly, for example: `{value.percent.formatNumber('#.0')}` to format the percentage to one decimal place.

**Formatting Blocks (wrapped in `[]`):**
You can apply styling to parts of your tooltip text. The styling applies until the end of the string or until a closing block `[/]` is found.
*   **Bold:** `[bold]My Text[/]`
*   **Color:** `[red]Important[/]` or `[#FF0000]Important[/]`
*   **Inline CSS:** `[font-size: 20px]Large Text[/]`
*   **Combined:** `[bold red font-size: 20px]Important[/]`

**Example:**
A `tooltipFormat` string of `"[bold]{category}[/]\nValue: {value.value}\nPercent: {value.percent.formatNumber('#.0')}%"` would produce a tooltip like:
> **Pumpkin**
> Value: 36
> Percent: 27.5%

---

### Helpful Tips & Best Practices

*   **Data is Key:** The most important property is `data`. It must be an array of objects. Each object needs one string key for the label and one numeric key for the value. The property names in the objects can be anything (e.g., `flavor`/`count` or `label`/`value`), as long as they are consistent across all objects in the array. Numeric values can be passed as numbers or as strings (e.g., `50` or `"50"`).
*   **Creating a Donut Chart:** To change the Pie Chart into a Donut (or Ring) Chart, simply set the `cutoutRadius` property to a number greater than 0. A value of `50` is a good starting point.
*   **Pre-configured Variants:** When dragging the component from the palette, you have three options:
    1.  **Pie Chart / Flat Chart:** The standard, default appearance.
    2.  **Three Dimensional:** A chart with the `threeDimensional` property preset to `true`.
*   **Color Mapping:** The `colors` array maps to the `data` array by index. `colors[0]` applies to `data[0]`, `colors[1]` applies to `data[1]`, and so on. If you have fewer colors than data entries, the colors will repeat.
*   **Label Management:**
    *   To prevent long labels from overlapping, you can enable `labels.wrap.enabled` and set a `labels.wrap.maxWidth`.
    *   For a more stylized look, try setting `labels.bent` to `true`. Note that this will disable `align` and `wrap`.
    *   To de-clutter the chart, you can move labels for small slices inside the slices themselves using the `labels.inside` properties. Set `labels.inside.enabled` to `true` and adjust the `percentLimit`. Note that enabling `inside` labels disables `bent` and `align`.
*   **Interactive Slices:** To get the data from a slice when a user clicks it, set `selection.enabled` to `true`. The data for the selected slice will then appear in the read-only `selection.data` property, which you can use in a property binding.
*   **Custom Tooltips:** Use the `tooltipFormat` property to create detailed tooltips. You can combine placeholders like `{category}` and `{value}` with formatting blocks like `[bold]` and color names to provide more context to the user on hover.
*   **Showing Raw Values vs. Percentages:** Use the `valueFormat.showValueAsPercent` property to toggle between displaying percentages (the default) or the raw numeric values from your dataset in the labels and legend.

# Schema - raw
{"schema":{"description":"A Pie Chart component","type":"object","title":"Pie Chart","required":["data","colors","title","showLabels","showLegend","cutoutRadius","sectionOutline","enableTransitions","threeDimensional","style"],"additionalProperties":false,"properties":{"sectionOutline":{"type":"object","required":["width","color","opacity"],"additionalProperties":false,"properties":{"color":{"format":"color","description":"Color of border around each pie section","type":"string","default":""},"width":{"description":"Thickness of border around each pie section","type":"number","default":0},"opacity":{"description":"Opacity of border around each pie section. 0 is fully transparent, 1 is fully opaque.","type":"number","exclusiveMaximum":false,"default":1,"maximum":1,"minimum":0}}},"data":{"description":"Data source for this chart. Each object within array defines the name and value for a single pie section.","type":["array","dataset"],"example":[{"count":36,"flavor":"Pumpkin"},{"count":17,"flavor":"Pecan"},{"count":14,"flavor":"Apple"},{"count":10,"flavor":"Sweet Potato"},{"count":9,"flavor":"Chocolate"}],"items":{"type":"object","properties":{"label":{"description":"Name of subject of current pie section","type":"string"},"value":{"description":"Value which determines percentage of chart current pie section occupies","type":"number"}}}},"cutoutRadius":{"description":"Percent of total radius to cut out of center of chart. If greater than zero, chart becomes ring-style instead of pie.","type":"number","exclusiveMaximum":true,"default":0,"maximum":100,"minimum":0},"legend":{"type":"object","properties":{"icon":{"type":"object","properties":{"enabled":{"description":"Value that determines whether to show the legend icons or hide them","type":"boolean","default":true},"width":{"visibleWhen":{"equals":true,"property":"enabled"},"description":"Width value of legend icon","type":"number","default":25},"height":{"visibleWhen":{"equals":true,"property":"enabled"},"description":"Height value of legend icon","type":"number","default":25}}},"fontSize":{"description":"Font size for legend labels","type":"number","default":16},"position":{"description":"Aligns legend to specified direction","type":"string","enum":["left","top","right","bottom"],"default":"bottom"}}},"valueFormat":{"description":"Label and legend value format configuration","type":"object","default":{"showPercentSymbol":true,"showValueAsPercent":true},"properties":{"showPercentSymbol":{"visibleWhen":{"equals":true,"property":"showValueAsPercent"},"description":"Whether to show the percent symbol next to the percent value","type":"boolean","default":true},"showValueAsPercent":{"description":"Whether to show the value as a percent of total or the raw value","type":"boolean","default":true}}},"showLegend":{"description":"Value that determines whether to show a legend for this chart or hide it","type":"boolean","default":true},"title":{"description":"Name to display for this chart","type":"string","example":"Favorite Pie Flavors","default":""},"colors":{"description":"Colors that correspond to each pie section, respective of order in data","type":"array","example":["#3366CC","#EC4B3D","#4FC86C","#00A9C6","#E69300"],"items":{"format":"color","description":"Color for a single pie section","type":"string"}},"enableTransitions":{"description":"Whether chart has visual transition effects for changes in chart data","type":"boolean","default":true},"labels":{"type":"object","properties":{"showName":{"description":"Whether to show the name on the label","type":"boolean","default":true},"color":{"format":"color","description":"The color of the labels","type":"string","default":""},"bent":{"description":"Bend labels around slices. Bending labels will disable the align and wrap properties","type":"boolean","default":false},"align":{"visibleWhen":{"equals":false,"property":"bent"},"description":"Whether the labels should be aligned in vertical columns","type":"boolean","default":true},"inside":{"type":"object","properties":{"percentLimit":{"description":"Value that determines at what value percentage to place label on outside of chart instead of inside","type":"number","default":10},"color":{"format":"color","description":"Label color for labels while they are displayed inside the chart","type":"string","default":"#FFFFFF"},"enabled":{"description":"Whether the labels should show inside of the chart slices, based on if the value percentage is below the percentLimit threshold. Displaying labels inside the chart will disable bent and align properties","type":"boolean","default":false},"radius":{"description":"Distance in percentage towards center of pie chart while inside is enabled. 0 represents outside edge while 100 would be directly in the middle","type":"number","default":80}}},"showValue":{"description":"Whether to show the value on the label. Hiding values will disable any value formats set","type":"boolean","default":true},"wrap":{"visibleWhen":{"equals":false,"property":"bent"},"description":"Label text wrapping configuration.","type":"object","properties":{"enabled":{"description":"Enables label text wrapping.","type":"boolean","default":false},"maxWidth":{"description":"The max allowable label width.","type":"number","default":200}}}}},"titleColor":{"format":"color","description":"The color of the title","type":"string","default":""},"showLabels":{"description":"Whether to show labels for each section of this chart","type":"boolean","default":true},"selection":{"description":"An object that contains selection related properties.","type":"object","properties":{"data":{"description":"A read-only list of currently selected pie chart slice","type":"array","default":[]},"enabled":{"description":"Enables selection of pie chart slices.","type":"boolean","default":false}}},"threeDimensional":{"description":"Whether chart has a depth effect to look three-dimensional","type":"boolean","default":false},"legendLabelColor":{"format":"color","description":"The color of the legend labels","type":"string","default":""},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"tooltipFormat":{"description":"Value that determines the format of the tooltips.","type":"string","default":"{category} : {value.percent.formatNumber('#.0')}%","suggestions":["{category}","{value.value}","{category}: {value.value}","{category} : {value.percent.formatNumber('#.0')}%","[bold]{category}[/] : [font-size: 30px red]{value.value}[/]"]}}},"resources":[{"type":"js","path":"/res/perspective/js/PerspectiveAmCharts.js","name":"perspective-amcharts-js"},{"type":"css","path":"/res/perspective/css/PerspectiveAmCharts.css","name":"perspective-amcharts-css"}],"defaultMetaName":"PieChart","name":"Pie","palette":{"variants":[{"tooltip":"A standard pie chart that displays a list of items, each of which has a value that is part (percentage) of the total.","label":"Pie Chart"},{"tooltip":"A standard pie chart that displays a list of items, each of which has a value that is part (percentage) of the total.","label":"Flat Chart","id":"pie-flat"},{"tooltip":"A standard pie chart that displays a list of items, each of which has a value that is part (percentage) of the total.","label":"Three Dimensional","props":{"threeDimensional":true},"id":"pie-3d"}],"category":"chart"},"id":"ia.chart.pie"}