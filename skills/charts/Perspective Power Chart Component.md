# Perspective Power Chart Component

## Description

These instructions describe the configuration and runtime use of the Perspective Power Chart component to create highly interactive visualizations of time-series data. The document covers the detailed setup of the component's properties, including its pens, axes, and plots, as well as the various user interaction modes for panning, zooming, and analyzing data within a live session.

## Documentation

# Instructions
This document provides instructions for using the Perspective Power Chart component in Ignition.

## Overview

The Perspective Power Chart is a powerful and flexible component designed to collect and display time-series data. Its primary function is to visualize data based on "pens," which represent historical data sources, typically from Ignition's Tag Historian. The chart is highly customizable from within a running Perspective session, allowing users to modify its appearance, add or remove pens, and interact with the data in various ways.

**Critical Note:** The Power Chart component requires the **Tag Historian module** to be installed and licensed, as it relies on its functionality to query and display data.

## Component Anatomy

The Power Chart is composed of several key areas that provide distinct functionality:

*   **Trending Area:** The main part of the component where data is visually plotted.
*   **Browse Tags Panel:** A panel that allows users to browse for any available historical data (from any Tag Historian provider) and add it to the chart as a new pen. You can add tags by selecting them and clicking the "Add Selected Tags" button or by dragging and dropping them onto a plot.
*   **Pen Control Table:** A table that lists all the pens currently on the chart. It displays aggregate data for each pen based on the current time range and provides controls for hiding, coloring, or removing the pen.
*   **Chart Settings Panel:** Accessible via the "Settings" icon, this panel allows runtime configuration of the chart's Axes, Pens, Plots, and the data columns shown in the Pen Control table.

## User Interaction and Modes

The Power Chart has several built-in tools and interaction modes, accessible from its toolbar. The primary user interaction mode is controlled by the `interaction.mode` property.

*   **Date Range Selector:** Allows switching between **Realtime** and **Historical** modes.
    *   **Realtime:** Shows the most recent data for a specified timeframe (e.g., "the last 8 hours").
    *   **Historical:** Shows data between a specific start and end date/time. In this mode, a secondary time axis (the range selector) appears at the bottom, which can be used to zoom and pan within the selected historical range.
*   **Pan and Zoom (`panAndZoom`):** The default interaction mode.
    *   **Desktop:** Click and drag to pan through time. Use the mouse wheel to zoom in and out.
    *   **Mobile:** Tap and drag to pan. Use pinch and spread gestures to zoom.
    *   A "Zoom Reset" icon appears when zoomed in to return to the default view.
*   **X-Trace (`xTrace`):** Click on the chart to place a vertical line that shows the interpolated value for each pen at that specific point in time. X-Trace values appear in an info box and in the Pen Control table.
*   **Range Brush (`rangeBrush`):** Allows you to click and drag to select a specific range of time on the chart. When a range is selected, the Pen Control table updates to show aggregate summaries (min, max, average, etc.) for that specific range. Multiple range brushes can be created.
*   **Annotation (`annotation`):** Allows you to click near a data point to add an annotation. Annotations are stored in the Tag Historian (`sqlth_annotations` table) and can be edited or deleted directly from the chart.
*   **Full Screen:** Toggles a full-screen view of the chart.
*   **Settings:** Opens the Chart Settings panel.
*   **More Menu:** Provides additional options:
    *   **Export:** Exports the visible data points to a CSV file.
    *   **Print:** Opens a print dialog to print the chart.
    *   **Clear X Traces:** Removes all X-Traces from the chart.
    *   **Clear Range Brushes:** Removes all range brush selections.

## Properties

Below is a detailed description of the Power Chart's properties.

### `config`

Configuration for the data source and general behavior of the chart.

*   `mode` (String): The query mode.
    *   `"realtime"` (Default): Queries the most recent data.
    *   `"historical"`: Queries data between a start and end date.
*   `startDate` (Date): The start date for a historical query. Only visible when `config.mode` is `"historical"`. Default is `null`.
*   `endDate` (Date): The end date for a historical query. Only visible when `config.mode` is `"historical"`. Default is `null`.
*   `unitOfTime` (Number): The number of time units to show in a realtime query. Default is `8`.
*   `measureOfTime` (String): The measurement of time for a realtime query. e.g., `"seconds"`, `"minutes"`, `"hours"`. Default is `"hours"`.
*   `refreshRate` (Number): The rate in milliseconds at which data is refreshed in realtime mode. Default is `1000`.
*   `pointCount` (Number): The number of data points to return for the selected time range. Default is `300`. **Note:** Setting this to `-1` retrieves the raw, "as stored" data from the database.
*   `tagBrowserStartPath` (String): Sets a starting path for the "Browse Tags" panel. The format is a series of key-value pairs.
    *   **Format:** `histprov:<ProviderName>:/drv:<GatewayName>:<TagProviderName>:/tag:<PathToFolder>`
    *   **Example:** `histprov:Sample_SQLite_Database:/drv:My_Gateway:DefaultHistorical:/tag:Ramp`
*   `penNamePathDepth` (Number): Sets the depth of the tag path to include in a pen's name when added from the tag browser. A value of `1` (default) uses only the tag's name. A value of `2` would include the parent folder, e.g., `realistic/realistic0`.
*   `rangeStartDate` (Date): **(Read-Only)** The start date of the visible chart area after a user has panned or zoomed.
*   `rangeEndDate` (Date): **(Read-Only)** The end date of the visible chart area after a user has panned or zoomed.
*   `responsiveDesignWidth` (Number): The pixel width at which the chart switches to its mobile-optimized view. Default is `750`.
*   `visibility` (Object): Controls the visibility of UI elements.
    *   `showTagBrowser` (Boolean): Toggles visibility of the Tag Browser panel. Default `false`.
    *   `showDateRangeSelector` (Boolean): Toggles visibility of the Realtime/Historical selector. Default `true`.
    *   `showPenControlDisplay` (Boolean): Toggles visibility of the Pen Control table. Default `true`.
    *   `buttons` (Object): An object with boolean properties to show/hide individual toolbar buttons (e.g., `showPanZoomButton`, `showXTraceButton`, etc.). All are `true` by default.
*   `export` (Object): Controls the format of exported data.
    *   `dateFormat` (String): The date format for the exported CSV file, using a MomentJS string.
    *   `timeFormat` (String): The time format for the exported CSV file, using a MomentJS string.

### `pens`

An array of objects, where each object defines a pen on the chart.

*   `name` (String): The name of the pen, displayed in the legend and Pen Control table.
*   `data` (Object): Defines the data source for the pen.
    *   `source` (String): The historical tag path to the data. **Note:** Non-historical tag paths will be automatically converted to the historical format (e.g., `histprov:default:/tag:path/to/tag`). NOTE - this should be a string to the tag's path. This is not an OBJECT.
    *   `aggregateMode` (String): The aggregation mode to use for the query. Default is `"default"` (which uses Min/Max). Other options include `Average`, `Sum`, `Minimum`, `Maximum`, etc.
*   `axis` (String): The `name` of an axis from the `axes` array to plot this pen against. If blank, a default axis is created.
*   `plot` (Number): The zero-based index of the plot (from the `plots` array) this pen belongs to. Default is `0`.
*   `visible` (Boolean): If `true` (default), the pen is visible on the chart.
*   `enabled` (Boolean): If `true` (default), the pen is available on the chart and in the configuration panel.
*   `selectable` (Boolean): If `true` (default), the pen can be selected by the user.
*   `display` (Object): Defines the visual appearance of the pen.
    *   `type` (String): The chart type. Can be `"line"` (default), `"area"`, `"bar"`, or `"scatter"`.
    *   `interpolation` (String): The curve style used to draw the line (e.g., `"curveLinear"`, `"curveStepAfter"`). Applicable to `line` and `area` types.
    *   `breakLine` (Boolean): If `true` (default), gaps will appear in the line for bad or missing data. If `false`, points are connected across gaps.
    *   `radius` (Number): The radius of points for a `scatter` chart. Default is `3`.
    *   `styles` (Object): Contains style objects for the pen's different states: `normal`, `highlighted`, `selected`, `muted`. Each state object has `fill` and `stroke` objects to define color and opacity.

### `axes`

An array of objects, where each object defines a Y-axis.

*   `name` (String): A unique name for the axis. This is used by pens (`pen.axis`) and markers (`marker.axis`) to associate with this axis.
*   `position` (String): The side of the chart to draw the axis on. `"left"` (default) or `"right"`.
*   `label` (Object): Configuration for the axis title.
    *   `text` (String): The text to display for the axis label.
*   `range` (Object): Configuration for the axis value range.
    *   `auto` (Boolean): If `true` (default), the min/max values are calculated automatically from the pen data.
    *   `min` (Number): A fixed minimum value for the axis. Used when `auto` is `false`.
    *   `max` (Number): A fixed maximum value for the axis. Used when `auto` is `false`.
*   `tick` (Object): Configuration for the axis tick marks and labels.
    *   `label.format` (String): A D3 format string for the tick labels (e.g., `",.2f"` for a comma-separated number with two decimal places). Default is `"Auto"`.
*   `grid` (Object): Configuration for gridlines associated with this axis.
    *   `visible` (Boolean): If `true`, shows gridlines. Default is `false`.
    *   `color` (String): The color of the gridlines.
*   `width` (Number): The width of the axis in pixels. Default is `60`.
*   `color` (String): The color of the axis line and ticks. Default `#757A7F`.
*   `dataFormat` (String): A Numeral.js format for displaying data associated with this axis in the Pen Control table (e.g., `"0,0.00"`).

### `plots`

An array of objects, where each object defines a plot area. Plots are stacked vertically and can contain multiple pens.

*   `relativeWeight` (Number): The ratio of vertical space this plot takes up relative to other plots. Default is `1`.
*   `color` (String): Background color of the plot. Default is `#FFFFFF`.
*   `markers` (Array): An array of marker objects to display on the plot.
    *   `type` (String): The type of marker, either `"line"` (default) or `"band"`.
    *   `axis` (String): The `name` of the axis to draw the marker against. **This is required for the marker to appear.**
    *   `value` (Number): The value at which to draw a `"line"` marker.
    *   `min` (Number): The lower value for a `"band"` marker.
    *   `max` (Number): The upper value for a `"band"` marker.
    *   `display` (Object): Configuration for the marker's appearance (color, width, opacity, label, etc.).

### `interaction`

Configuration for the user interaction modes.

*   `mode` (String): The current interaction mode. Can be `"panAndZoom"` (default), `"xTrace"`, `"rangeBrush"`, or `"annotation"`.
*   `fullscreen` (Boolean): If `true`, the chart is in fullscreen mode. Default is `false`.
*   `chartZoomLevel` (Number): **(Read-Only)** The current zoom level of the main chart.
*   `rangeZoomLevel` (Number): **(Read-Only)** The current zoom level of the range brush (in historical mode).
*   `xTrace` (Object): Configuration for the X-Trace display. Contains objects to style the `line` and the `infoBox`.
*   `rangeBrush` (Object): Configuration for the Range Brush display. Contains style objects for the `active` and `inactive` brush states.
*   `annotation` (Object): Configuration for the Annotation display. Contains objects to style the `dot`, `line`, and `infoBox`.
*   `panAndZoom` (Object):
    *   `freeRange` (Boolean): If `true`, panning and zooming will update the `config.startDate` and `config.endDate` properties, effectively changing the time range of the historical query. Default is `false`.

### `timeAxis`

Configuration for the time axis (X-axis).

*   `visible` (Boolean): Whether the time axis is visible. Default `true`.
*   `height` (Number): The height of the axis in pixels. Default is `35`.
*   `tickCount` (Number/String): The number of ticks to display. Setting to `0` enables automatic scaling of ticks based on zoom level. Default is `"auto"`.
*   `tick` (Object): Configuration for the time axis tick labels.
    *   `label.format` (String): The date/time format for the labels, using a MomentJS string (e.g., `"YYYY-MM-DD HH:mm:ss"`). Default is `"Auto"`.
*   `grid` (Object): Configuration for vertical gridlines extending from the time axis.
    *   `visible` (Boolean): If `true`, shows gridlines. Default is `false`.

---

## Helpful Tips and Best Practices

*   **Data Source:** Always ensure that `pens.data.source` points to a valid historical tag path. The component will attempt to convert standard tag paths, but it's best to use the historical format for reliability.
*   **As-Stored Data:** To retrieve raw data without aggregation, set `config.pointCount` to `-1`. This is useful for seeing every value change as it was recorded by the historian.
*   **Dynamic Date Ranges:** The Power Chart can be driven by other components. Bind the `config.startDate` and `config.endDate` properties to Date Picker components to create a custom date range selector.
*   **Markers Require an Axis:** For a marker in `plots.markers` to be visible, its `axis` property **must** be set to the `name` of a valid axis in the `axes` array.
*   **Performance:** Displaying a very large number of points or pens with raw data (`pointCount: -1`) can impact performance. Use appropriate aggregation (`pens.data.aggregateMode`) and a reasonable `pointCount` for faster load times.
*   **`tagBrowserStartPath` Syntax:** The syntax for this path is specific. Use `histprov:`, `drv:`, and `tag:` prefixes correctly. For example: `histprov:MyDB:/drv:IgnitionGateway:default:/tag:Motors/Motor1`.
*   **Read-Only Properties:** Properties like `rangeStartDate`, `rangeEndDate`, `chartZoomLevel`, and `rangeZoomLevel` are read-only. They reflect the user's interaction with the chart but cannot be written to to control the chart. To control the chart's range via scripting, modify `config.startDate` and `config.endDate`.
*   **Free-Range Panning:** For a truly exploratory chart where users can pan and zoom freely through history, set `config.mode` to `historical` and `interaction.panAndZoom.freeRange` to `true`. You may want to bind `config.startDate` and `config.endDate` to tags or session properties to save the user's state.
*   **Default Time Range** If no time range is given to you, then assume a default of realtime mode and the last 5 minutes.
*   **Artifact Creation** For an artifact of this, provide only the "props" portion of the schema, and only the relevant parts (the parts you are changing).
*   **Plot background** Set the plot background (the "color" property) to transparent (#FFFFFF00) for all cases unless the user requests otherwise.


** EXAMPLE STARTER **
{
  "config": {
    "mode": "realtime",
    "unitOfTime": 8,
    "measureOfTime": "hours"
  },
  "pens": [
    {
      "name": "Motor RPM",
      "data": {
        "source": "histprov:default:/tag:Motor RPM",
        "aggregateMode": "default"
      },
      "axis": "DefaultAxis",
      "plot": 0,
      "visible": true,
      "enabled": true,
      "selectable": true,
      "display": {
        "type": "line",
        "interpolation": "curveLinear",
        "breakLine": true,
        "styles": {
          "normal": {
            "fill": {
              "color": "#63BEA2",
              "opacity": 0.8
            },
            "stroke": {
              "color": "#63BEA2",
              "width": 1,
              "dashArray": 0,
              "opacity": 0.8
            }
          }
        }
      }
    }
  ],
  "axes": [
    {
      "name": "DefaultAxis",
      "position": "left",
      "label": {
        "text": "RPM"
      },
      "range": {
        "auto": true
      }
    }
  ]
}


<< CRITICAL NOTE - THIS IS NOT A VALID "data" property structure; note that "source" must be the path itself, and not "tag" with a separate "tag" object.
        "data": {
            "source": "tag",
            "tag": {
                "path": "[default]Motor RPM"
            }
        },
<< END CRITICAL NOTE

# Schema - raw
{"schema":{"type":"object","additionalProperties":false,"definitions":{"fill":{"type":"object","properties":{"color":{"format":"color","type":"string","default":"#FAFAFB"},"opacity":{"type":["number","string"],"default":0.9}}},"stroke":{"type":"object","properties":{"color":{"format":"color","type":"string","default":"#757A7F"},"width":{"type":["number","string"],"default":1},"opacity":{"type":["number","string"],"default":0.9},"dashArray":{"type":["number","string"],"default":0}}},"grid":{"description":"Configuration for gridlines to display on this axis.","type":"object","properties":{"visible":{"description":"Visible state of the gridlines. Gridlines are shown only for axes that connect directly to the chart. Any satellite axes will display their tick configurations instead of gridlines.","type":"boolean","default":false},"color":{"format":"color","description":"Color of the gridlines.","type":"string","default":""},"style":{"description":"Style properties to be applied to the axis gridlines.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"Opacity of the gridlines.","type":"number","default":0.9},"dashArray":{"description":"Dashed appearance of the gridlines.","type":"number","default":0}}},"font":{"type":"object","properties":{"color":{"format":"color","description":"The text color of the info box label and datetime text.","type":"string","default":""},"size":{"description":"The font size of the info box label and datetime text.","type":["number","string"],"default":11},"style":{"description":"Style properties to be applied to the text of the info box.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}},"properties":{"dataColumns":{"description":"Configuration for the data columns that can be shown in tabular displays throughout the chart.","type":"object","additionalProperties":false,"properties":{"rangeSelection":{"description":"Configuration for the data columns that can display for the range brush.","type":"object","additionalProperties":false,"properties":{"average":{"description":"Show the \"Average\" column for the pen based on the time range.","type":"boolean","default":true},"last":{"description":"Show the \"Last\" column for the pen based on the time range.","type":"boolean","default":true},"delta":{"description":"Show the \"Delta\" column for the pen based on the time range.","type":"boolean","default":true},"sum":{"description":"Show the \"Sum\" column for the pen based on the time range.","type":"boolean","default":true},"median":{"description":"Show the \"Median\" column for the pen based on the time range.","type":"boolean","default":true},"lcl":{"description":"Show the \"LCL\" column for the pen based on the time range.","type":"boolean","default":true},"maximum":{"description":"Show the \"Maximum\" column for the pen based on the time range.","type":"boolean","default":true},"minimum":{"description":"Show the \"Minimum\" column for the pen based on the time range.","type":"boolean","default":true},"first":{"description":"Show the \"First\" column for the pen based on the time range.","type":"boolean","default":true},"standardDeviation":{"description":"Show the \"Standard Deviation\" column for the pen based on the time range.","type":"boolean","default":true},"ucl":{"description":"Show the \"UCL\" column for the pen based on the time range.","type":"boolean","default":true}}},"penControl":{"description":"Configuration for the data columns that can display for pens.","type":"object","additionalProperties":false,"properties":{"average":{"description":"Show the \"Average\" column for the pen based on the time range.","type":"boolean","default":true},"axis":{"description":"Show the \"Axis\" column for the pen.","type":"boolean","default":true},"plot":{"description":"Show the \"Plot\" column for the pen.","type":"boolean","default":true},"xTrace":{"description":"Show the \"X Trace\" column for the pen.","type":"boolean","default":true},"maximum":{"description":"Show the \"Maximum\" column for the pen based on the time range.","type":"boolean","default":true},"minimum":{"description":"Show the \"Minimum\" column for the pen based on the time range.","type":"boolean","default":true},"currentValue":{"description":"Show the \"Current Value\" column for the pen based on the time range.","type":"boolean","default":true}}}}},"legend":{"description":"Configuration for the display of the legend for the chart.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the legend.","type":"boolean","default":false}}},"axes":{"description":"Collection of predefined axes against which the data visualizations can be drawn.","type":"array","default":[],"items":{"type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The color of the Y axis vertical bar.","type":"string","default":"#757A7F"},"dataFormat":{"description":"A numeral.js data format for displaying the data for this axis. See http://numeraljs.com/ for formats.","type":"string","default":"0,0.##","suggestions":{"integer [1,200]":"0,0","number [1,000.12]":"0,0.##","percent [10.12%]":"0.##%","currency [$1,000.12]":"$0,0.00","currency (rounded) [$1,012]":"$0,0","accounting [$ (1,000.12)]":"$ (0,0.00)","financial [(1,000.12)]":"(0,0.00)","duration [24:01:00]":"00:00:00","scientific [1.01E+03]":"0.00e+0","ordinal [100th]":"0o","abbreviation [1.2k]":"0.0a","four decimal precision [1.1200]":"0,0.0000"}},"range":{"description":"Configuration for the upper and lower limits of the axis.","type":"object","additionalProperties":false,"properties":{"auto":{"description":"If true, the minimum and maximum displaying values for the axis will be auto calculated.","type":"boolean","default":true},"max":{"visibleWhen":{"equals":false,"property":"auto"},"description":"Maximum range value. If no value is provided, a maximum value will be calculated from the data bound to this axis.","type":["number","string","null"],"default":""},"min":{"visibleWhen":{"equals":false,"property":"auto"},"description":"Minimum range value. If no value is provided, a minimum value will be calculated from the data bound to this axis.","type":["number","string","null"],"default":""}}},"label":{"description":"Y axis label configuration.","type":"object","additionalProperties":false,"properties":{"offset":{"description":"Offset the Y axis label from its default position. This allows you to fine tune the label location, which may be necessary depending on the scale and how much room the tick labels take up. Maybe positive or negative.","type":"number","default":0},"style":{"description":"Style properties to be applied to the Y axis label. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"The text of the Y axis label.","type":"string","default":""},"font":{"description":"Y axis label font configuration.","type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The color of the Y axis label text.","type":"string","default":"#757A7F"},"size":{"description":"The size of the Y axis label text.","type":["number","string"],"default":10}}}}},"tick":{"description":"Tick configuration. When the grid is displaying, ticks will be hidden.","type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The color of the ticks.","type":"string","default":"#757A7F"},"count":{"description":"The number of ticks. If \"Auto\" is used, the ticks will be determined by available space in the interface.","type":["number","string"],"default":"Auto","suggestions":{"2":2,"4":4,"6":6,"8":8,"10":10,"Auto":"Auto"}},"label":{"description":"Tick label configuration.","type":"object","additionalProperties":false,"properties":{"format":{"description":"Data format displayed by each tick using a D3 format string (https://github.com/d3/d3-format).","type":"string","default":"Auto","suggestions":{"Currency [$1,234.00]":"$,.2f","2 Decimal Points [1234.00]":".2f","Percentage [123400%]":".0%","Comma-Separated Integer [1,234]":",.0f","Hexadecimal (lowercase) [4d2]":"x","4 Decimal Points [1234.0000]":".4f","Auto":"Auto","Integer [1234]":"d","Binary [10011010010]":"b","Hexadecimal (uppercase) [4D2]":"X","Octal [2322]":"o","Comma-Separated w/ 2 Decimal Points [1,234.00]":",.2f","Exponential [1.234000e+3]":"e"}},"style":{"description":"Style properties to be applied to the tick labels. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"font":{"description":"Label font configuration.","type":"object","properties":{"color":{"format":"color","description":"The color of the label text.","type":"string","default":"#757A7F"},"size":{"description":"The size of the label text.","type":["number","string"],"default":10}}}}},"style":{"description":"Style properties to be applied to the ticks. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"grid":{"$ref":"#/definitions/grid"},"name":{"description":"The name of the axis.","type":"string","default":""},"width":{"description":"The width of the axis.","type":"number","default":60},"style":{"description":"Style properties to be applied to the axis line. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"position":{"description":"The side of the plot upon which the axis should be drawn.","type":"string","enum":["left","right"],"default":"left"}}}},"timeAxis":{"description":"Configuration for the time axis (X axis) of the chart.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the time axis.","type":"boolean","default":true},"color":{"format":"color","description":"The color of the axis.","type":"string","default":"#757A7F"},"tick":{"description":"Tick configuration. When the grid is displaying, ticks will be hidden.","type":"object","properties":{"color":{"format":"color","description":"The color of the ticks.","type":"string","default":"#757A7F"},"label":{"description":"Tick label configuration.","type":"object","properties":{"format":{"description":"Date/time format displayed by each tick using a MomentJS date string (https://momentjs.com/).","type":"string","default":"Auto","suggestions":{"[2020-3-2 8:15:35]":"YYYY-M-D h:mm:ss","Day of Week, Month, and Hour [Monday 2nd, 08 AM]":"dddd Do, hh A","Unix Timestamp [1563464737]":"X","Full Month [January]":"MMMM","Abbreviated Month and Day of Month [Jan 2nd]":"MMM Do","Auto":"Auto","Hour Minute [8:15]":"h:mm","Abbreviated Month and Year [Jan 20]":"MMM YY","Unix Millisecond Timestamp [1563464737269]":"x","Millisecond [638]":"SSS","Second [35]":":ss","Full Year [2020]":"YYYY","Hour with Meridiem [8 AM]":"h A","[3-2-2020 8:15:35]":"M-D-YYYY h:mm:ss","Abbreviated Day of Week and Month [Mon 2nd]":"ddd Do"}},"angled":{"description":"A flag to toggle the angled state of the tick labels.","type":"boolean","default":false},"style":{"description":"Style properties to be applied to the timeAxis labels. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"font":{"description":"Tick label font configuration.","type":"object","properties":{"color":{"format":"color","description":"The color of the tick label text.","type":"string","default":"#757A7F"},"size":{"description":"The size of the tick label text.","type":["number","string"],"default":10}}}}},"style":{"description":"Style properties to be applied to the ticks. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"tickCount":{"description":"The number of ticks.","type":["number","string"],"default":"auto"},"grid":{"$ref":"#/definitions/grid"},"style":{"description":"Style properties to be applied to the horizontal line of the axis. Any property that would apply to an SVG line element can be used here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"height":{"description":"The height of the time axis.","type":"number","default":35}}},"title":{"description":"Configuration for the title of the chart.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the title.","type":"boolean","default":false},"style":{"description":"A style object that is used to add visual style to the title. Style that can be applied to an SVG text element can be used here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"The text of the title.","type":"string","default":""},"font":{"description":"Title font configuration.","type":"object","properties":{"color":{"format":"color","description":"The color of the title text.","type":"string","default":"#222222"},"size":{"description":"The size of the title text.","type":["number","string"],"default":12}}}}},"pens":{"description":"Visual representation of each active data item.","type":"array","default":[],"items":{"type":"object","additionalProperties":false,"properties":{"visible":{"description":"Visible state of the pen on the chart.","type":"boolean","default":true},"data":{"description":"Configuration that defines the data structure for the pen.","type":"object","additionalProperties":false,"properties":{"source":{"description":"Source of the data behind the pen.","type":"string","default":""},"aggregateMode":{"description":"Mode used to group the data.","type":"string","enum":["default","Average","MinMax","LastValue","SimpleAverage","Sum","Minimum","Maximum","DurationOn","DurationOff","CountOn","CountOff","Count","Range","Variance","StdDev","PctGood","PctBad"],"default":"default"}}},"selectable":{"description":"Flag to allow the pen to be responsive to user selection.","type":"boolean","default":true},"display":{"description":"Configuration that drives the display of the pen.","type":"object","additionalProperties":false,"properties":{"breakLine":{"visibleWhen":{"equals":"line","property":"type"},"description":"If true, the line will be broken on either side of bad/missing data values. If false, bad/missing data values are removed and the adjoining points are connected.","type":"boolean","default":true},"type":{"description":"The type of chart to be built.","type":"string","enum":["line","area","bar","scatter"],"default":"line"},"interpolation":{"visibleWhen":{"equals":["line","area"],"property":"type"},"description":"Type of curve that should be used to draw the line portion of the chart.","type":"string","enum":["curveBasis","curveBasisOpen","curveCardinal","curveCardinalOpen","curveCatmullRom","curveCatmullRomOpen","curveLinear","curveMonotoneX","curveMonotoneY","curveNatural","curveStep","curveStepAfter","curveStepBefore"],"default":"curveLinear"},"styles":{"description":"If provided, the default styles to apply to the column.","default":{"normal":{"fill":{"color":"#63BEA2","opacity":0.8},"stroke":{"color":"#63BEA2","width":1,"dashArray":0,"opacity":0.8}},"highlighted":{"fill":{"color":"#63BEA2","opacity":1},"stroke":{"color":"#63BEA2","width":1,"dashArray":0,"opacity":1}},"muted":{"fill":{"color":"#63BEA2","opacity":0.4},"stroke":{"color":"#63BEA2","width":1,"dashArray":0,"opacity":0.4}},"selected":{"fill":{"color":"#63BEA2","opacity":1},"stroke":{"color":"#63BEA2","width":1,"dashArray":0,"opacity":1}}},"$ref":"urn:ignition-schema:schemas/trend-style.schema.json"},"radius":{"visibleWhen":{"equals":"scatter","property":"type"},"description":"The radius of the points.","type":"number","default":3}}},"axis":{"dynamicSuggestions":"../../../axes/*/name","description":"Name of an axis in the \"axes\" array to plot against. If left blank, a default axis will be created based on data values.","type":"string","default":""},"enabled":{"description":"Availability of the pen on the chart and pen configuration panel.","type":"boolean","default":true},"plot":{"description":"The plot to which this pen is bound.","type":"number","default":0},"name":{"description":"Name of the pen.","type":"string","default":""}}}},"plots":{"description":"A plot represents a row containing one or more pens.","type":"array","items":{"type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The background color of the plot.","type":"string","default":"#FFFFFF"},"relativeWeight":{"description":"Ratio between all plots.","type":"number","default":1},"style":{"description":"Style properties to be applied to the plot. Any style that applies to an SVG box element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"markers":{"description":"A collection of markers that can be added on the plot to better visualize the data being displayed.","type":"array","default":[],"items":{"description":"Marker that can be added on the plot to better visualize the data being displayed.","type":"object","additionalProperties":false,"properties":{"max":{"visibleWhen":{"equals":"band","property":"type"},"description":"Upper value where the band should end.","type":"number","default":0},"display":{"description":"Configuration for the display of the marker.","type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"Color of the marker.","type":"string","default":"#757A7F"},"label":{"description":"Configuration for the label of the marker.","type":"object","additionalProperties":false,"properties":{"style":{"description":"Style properties to be applied to the marker label. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"The label drawn on the chart for the line.","type":"string","default":""},"position":{"description":"The position of the label relative to the line.","type":"string","enum":["left","right"],"default":"right"},"font":{"description":"Label font configuration.","type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The color of the label text.","type":"string","default":"#757A7F"},"size":{"description":"The size of the label text.","type":["number","string"],"default":10}}}}},"width":{"visibleWhen":{"equals":"line","property":"../type"},"description":"Width of the line.","type":["number","string"],"default":1},"style":{"description":"Style properties to be applied to the marker line. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"Opacity of the marker.","type":["number","string"],"default":0.5},"dashArray":{"visibleWhen":{"equals":"line","property":"../type"},"description":"Dashed appearance of the marker.","type":["number","string"],"default":0}}},"type":{"description":"Type of marker to add to the plot.","type":"string","enum":["line","band"],"default":"line"},"axis":{"dynamicSuggestions":"../../../../../axes/*/name","description":"Name of the axis against which the marker should be drawn. This must be specified for the marker to be drawn.","type":"string","default":""},"min":{"visibleWhen":{"equals":"band","property":"type"},"description":"Lower value where the band should start.","type":"number","default":0},"value":{"visibleWhen":{"equals":"line","property":"type"},"description":"Value where the line marker should be drawn.","type":"number","default":0}}}}}}},"interaction":{"description":"Configuration for the presentation of, and interaction with, chart data.","type":"object","additionalProperties":false,"properties":{"annotation":{"visibleWhen":{"equals":["annotation"],"property":"mode"},"description":"Configuration to build the annotation display.","type":"object","additionalProperties":false,"properties":{"line":{"description":"Configuration to build the connecting line portion of the annotation display.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the line.","type":"boolean","default":true},"color":{"format":"color","description":"The color of the line.","type":"string","default":"#757A7F"},"width":{"description":"The width of the line.","type":["number","string"],"default":1},"style":{"description":"Style properties to be applied to the annotation line. Any style properties that can be applied to a 'line' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"The opacity of the line.","type":["number","string"],"default":0.9},"dashArray":{"description":"The dashed appearance of the line.","type":["number","string"],"default":0}}},"dot":{"description":"Configuration to build the dot portion of the annotation display.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the dot.","type":"boolean","default":true},"color":{"format":"color","description":"The color of the dot.","type":"string","default":"#757A7F"},"style":{"description":"Style properties to be applied to the annotation dot. Any style properties that can be applied to a 'circle' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"radius":{"description":"The radius of the dot.","type":"number","default":3},"opacity":{"description":"The opacity of the dot.","type":["number","string"],"default":1}}},"infoBox":{"description":"Configuration to build the box portion of the annotation display.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the box.","type":"boolean","default":true},"dateFormat":{"description":"The date format of the date/time display using a MomentJS date string (https://momentjs.com/).","type":"string","default":"YYYY/MM/DD","suggestions":{"[2020-3-10]":"YYYY-M-D","[Mar 10th 20]":"MMM Do YY","[03/10/2020]":"MM/DD/YYYY","none":"None","[3-10-2020]":"M-D-YYYY","[2020/03/10]":"YYYY/MM/DD","[March 10th 2020]":"MMMM Do YYYY"}},"showTime":{"description":"The visible state of the time value above the box.","type":"boolean","default":true},"icon":{"description":"The configuration applied to the icons within the annotation's infoBox.","type":"object","default":{"fill":{"color":"#929597","opacity":1},"stroke":{"color":"#929597","width":0,"opacity":0,"dashArray":0},"style":{"classes":""}},"additionalProperties":false,"properties":{"fill":{"$ref":"#/definitions/fill"},"stroke":{"$ref":"#/definitions/stroke"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"fill":{"$ref":"#/definitions/fill"},"stroke":{"$ref":"#/definitions/stroke"},"timeFormat":{"description":"The time format of the date/time display using a MomentJS time string (https://momentjs.com/).","type":"string","default":"h:mm A","suggestions":{"12 Hour w/ Meridiem and Seconds [8:41:56 AM]":"h:mm:ss A","Unix Timestamp [1563464737]":"X","none":"None","24 Hour w/ Milliseconds [08:41:06:269]":"HH:mm:ss:SSS","Unix Millisecond Timestamp [1563464737269]":"x","12 Hour [8:41]":"h:mm","12 Hour w/ Meridiem [8:41 AM]":"h:mm A","24 Hour w/ Seconds [08:41:06]":"HH:mm:ss"}},"width":{"description":"The width of the box.","type":["number","string"],"default":"auto"},"style":{"description":"Style properties to be applied to the annotation info box. Any style properties that can be applied to a 'rect' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"font":{"$ref":"#/definitions/font"}}}}},"chartZoomLevel":{"description":"READ-ONLY: The zoom level displayed on the chart.","type":"number"},"rangeZoomLevel":{"description":"READ-ONLY: The zoom level displayed on the range brush in Historical mode.","type":"number"},"panAndZoom":{"visibleWhen":{"equals":["panAndZoom"],"property":"mode"},"description":"Configuration to use when panning and zooming.","type":"object","additionalProperties":false,"properties":{"freeRange":{"description":"When enabled, this allows panning and zooming to dictate the time range used for the chart display.","type":"boolean","default":false}}},"rangeBrush":{"visibleWhen":{"equals":["rangeBrush"],"property":"mode"},"description":"Configuration to build the range brush display.","type":"object","additionalProperties":false,"properties":{"values":{"description":"An array of config objects used to build each range brush.","type":"array","default":[],"items":{"description":"An object containing the start and end timestamps for each range brush.","type":"object","additionalProperties":false,"properties":{"start":{"description":"The start timestamp position.","type":["date","string"],"default":""},"plot":{"description":"The plot into which this range brush will be added.","type":"number"},"end":{"description":"The end timestamp position.","type":["date","string"],"default":""},"id":{"description":"The ID of the brush.","type":"string"}}}},"active":{"description":"Configuration to build the active range brush display.","type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The color of the active range brush.","type":"string","default":"#0C7BB3"},"style":{"description":"Additional style properties to be applied to the active range brush. Any style properties that can be applied to a 'rect' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"The opacity of the active range brush.","type":["number","string"],"default":0.3}}},"inactive":{"description":"Configuration to build the inactive range brush displays.","type":"object","additionalProperties":false,"properties":{"color":{"format":"color","description":"The color of the range brush.","type":"string","default":"#757A7F"},"style":{"description":"Style properties to be applied to the range brush. Any style properties that can be applied to a 'rect' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"The opacity of the range brush.","type":["number","string"],"default":0.3}}}}},"mode":{"description":"Current user interaction mode of the chart.","type":"string","enum":["panAndZoom","xTrace","rangeBrush","annotation"],"default":"panAndZoom"},"fullscreen":{"description":"Flag representing the fullscreen presentation mode of the chart.","type":"boolean","default":false},"xTrace":{"visibleWhen":{"equals":["xTrace"],"property":"mode"},"description":"Configuration to build the x-trace display.","type":"object","additionalProperties":false,"properties":{"line":{"description":"Configuration to build the vertical line portion of the x-trace display.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the line.","type":"boolean","default":true},"color":{"format":"color","description":"The color of the line.","type":"string","default":"#757A7F"},"width":{"description":"The width of the line.","type":["number","string"],"default":1},"style":{"description":"Style properties to be applied to the X-Trace tracking line. Any style properties that can be applied to a 'line' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"The opacity of the line.","type":["number","string"],"default":0.5},"dashArray":{"description":"The dashed appearance of the line.","type":["number","string"],"default":0}}},"values":{"description":"An array of timestamp or numeric values representing the visible x-trace positions. In \"historical\" interaction mode, a timestamp representing an x-trace position. In \"realtime\" interaction mode, a number representing the percentage of the distance to the end of the chart where the x-trace will be positioned.","type":"array","default":[],"items":{"description":"In \"historical\" interaction mode, a timestamp representing an x-trace position. In \"realtime\" interaction mode, a number representing the percentage of the distance to the end of the chart where the x-trace will be positioned.","type":["date","number"]}},"infoBox":{"description":"Configuration to build the box portion of the x-trace display.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the box.","type":"boolean","default":true},"dateFormat":{"description":"The date format of the date/time display using a MomentJS date string (https://momentjs.com/).","type":"string","default":"YYYY/MM/DD","suggestions":{"[2020-3-10]":"YYYY-M-D","[Mar 10th 20]":"MMM Do YY","[03/10/2020]":"MM/DD/YYYY","none":"None","[3-10-2020]":"M-D-YYYY","[2020/03/10]":"YYYY/MM/DD","[March 10th 2020]":"MMMM Do YYYY"}},"dataFormat":{"description":"A numeral.js data format for displaying the data. See http://numeraljs.com/ for formats.","type":"string","default":"0,0.##","suggestions":{"integer [1,200]":"0,0","number [1,000.12]":"0,0.##","percent [10.12%]":"0.##%","currency [$1,000.12]":"$0,0.00","currency (rounded) [$1,012]":"$0,0","accounting [$ (1,000.12)]":"$ (0,0.00)","financial [(1,000.12)]":"(0,0.00)","duration [24:01:00]":"00:00:00","scientific [1.01E+03]":"0.00e+0","ordinal [100th]":"0o","abbreviation [1.2k]":"0.0a","four decimal precision [1.1200]":"0,0.0000"}},"showTime":{"description":"The visible state of the time value above the box.","type":"boolean","default":true},"fill":{"$ref":"#/definitions/fill"},"stroke":{"$ref":"#/definitions/stroke"},"timeFormat":{"description":"The time format of the date/time display using a MomentJS time string (https://momentjs.com/).","type":"string","default":"h:mm A","suggestions":{"12 Hour w/ Meridiem and Seconds [8:41:56 AM]":"h:mm:ss A","Unix Timestamp [1563464737]":"X","none":"None","24 Hour w/ Milliseconds [08:41:06:269]":"HH:mm:ss:SSS","Unix Millisecond Timestamp [1563464737269]":"x","12 Hour [8:41]":"h:mm","12 Hour w/ Meridiem [8:41 AM]":"h:mm A","24 Hour w/ Seconds [08:41:06]":"HH:mm:ss"}},"width":{"description":"The width of the box.","type":["number","string"],"default":"auto"},"style":{"description":"Style properties to be applied to the X-Trace info box. Any style properties that can be applied to a 'rect' SVG shape can be applied here.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"font":{"$ref":"#/definitions/font"}}}}}}},"style":{"description":"Style properties to be applied to the base chart component.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"config":{"description":"Configuration for the data feeding the chart.","type":"object","additionalProperties":false,"properties":{"tagBrowserStartPath":{"description":"A path to a nested Tag History provider structure from which browsing will start.","type":"string","default":""},"responsiveDesignWidth":{"description":"A number (in pixels) that will be used as the switch over width to the responsive design for the chart.","type":"number","default":750},"visibility":{"description":"Settings to show/hide elements within the component interface.","type":"object","additionalProperties":false,"properties":{"showTagBrowser":{"description":"Flag representing the visible state of the tag browser.","type":"boolean","default":false},"buttons":{"description":"Settings to show/hide the buttons used in the interface.","type":"object","additionalProperties":false,"properties":{"showPanZoomButton":{"description":"Flag representing the visible state of the \"Pan and Zoom\" mode button.","type":"boolean","default":true},"showSettingsButton":{"description":"Flag representing the visible state of the \"Settings\" menu button.","type":"boolean","default":true},"showFullscreenButton":{"description":"Flag representing the visible state of the \"Fullscreen\" presentation mode button.","type":"boolean","default":true},"showRangeBrushButton":{"description":"Flag representing the visible state of the \"Range Brush\" mode button.","type":"boolean","default":true},"showTagBrowserButton":{"description":"Flag representing the visible state of the \"Open Tag Browser\" and \"Close Tag Browser\" buttons.","type":"boolean","default":true},"showMoreButton":{"description":"Flag representing the visible state of the \"More\" menu button.","type":"boolean","default":true},"showXTraceButton":{"description":"Flag representing the visible state of the \"X Trace\" mode button.","type":"boolean","default":true},"showAnnotationButton":{"description":"Flag representing the visible state of the \"Annotation\" mode button.","type":"boolean","default":true}}},"showDateRangeSelector":{"description":"Flag representing the visible state of the realtime/historical date range selector.","type":"boolean","default":true},"showPenControlDisplay":{"description":"Flag representing the visible state of the pen data table and pen legend.","type":"boolean","default":true}}},"endDate":{"visibleWhen":{"equals":["historical"],"property":"mode"},"description":"End date for a historical data query.","type":["date","null"],"default":null},"dateFormat":{"visibleWhen":{"equals":["historical"],"property":"mode"},"description":"The date format displayed when in historical mode using a MomentJS date string (https://momentjs.com/).","type":"string","default":"YYYY/MM/DD","suggestions":{"[2020-3-10]":"YYYY-M-D","[Mar 10th 20]":"MMM Do YY","[03/10/2020]":"MM/DD/YYYY","none":"None","[3-10-2020]":"M-D-YYYY","[2020/03/10]":"YYYY/MM/DD","[March 10th 2020]":"MMMM Do YYYY"}},"penNamePathDepth":{"description":"Depth of the tag path to include in the pen name.","type":"number","default":1},"rangeSelectorPen":{"visibleWhen":{"equals":["historical"],"property":"mode"},"dynamicSuggestions":"../../pens/*/data/source","description":"The pen that will drive the data display of the range selector in Historical mode.","type":"string","default":""},"rangeStartDate":{"description":"READ-ONLY: Start date for the modified chart data range that the user has selected either with the range brush or by panning/zooming.","type":["date","null"],"default":null},"mode":{"description":"The type of query that is being made against the data source.","type":"string","enum":["realtime","historical"],"default":"realtime"},"pointCount":{"description":"Number of data points returned for the selected time range.","type":"number","default":300},"unitOfTime":{"visibleWhen":{"equals":["realtime"],"property":"mode"},"description":"Time unit used for a realtime data query.","type":"number","default":8},"refreshRate":{"visibleWhen":{"equals":["realtime"],"property":"mode"},"description":"Duration (in milliseconds) that data will be queried for updated results.","type":"number","default":1000},"timeFormat":{"visibleWhen":{"equals":["historical"],"property":"mode"},"description":"The time format displayed when in historical mode using a MomentJS time string (https://momentjs.com/).","type":"string","default":"h:mm A","suggestions":{"12 Hour w/ Meridiem and Seconds [8:41:56 AM]":"h:mm:ss A","Unix Timestamp [1563464737]":"X","none":"None","24 Hour w/ Milliseconds [08:41:06:269]":"HH:mm:ss:SSS","Unix Millisecond Timestamp [1563464737269]":"x","12 Hour [8:41]":"h:mm","12 Hour w/ Meridiem [8:41 AM]":"h:mm A","24 Hour w/ Seconds [08:41:06]":"HH:mm:ss"}},"measureOfTime":{"visibleWhen":{"equals":["realtime"],"property":"mode"},"description":"Time measurement used for a realtime data query.","type":"string","enum":["seconds","minutes","hours","days","weeks","months","years"],"default":"hours"},"rangeEndDate":{"description":"READ-ONLY: End date for the modified chart data range that the user has selected either with the range brush or by panning/zooming.","type":["date","null"],"default":null},"export":{"description":"Settings to control the format of the data exported from the chart.","type":"object","additionalProperties":false,"properties":{"dateFormat":{"description":"The date format of the exported data using a MomentJS date string (https://momentjs.com/).","type":"string","default":"None","suggestions":{"[2020-3-10]":"YYYY-M-D","[Mar 10th 20]":"MMM Do YY","[03/10/2020]":"MM/DD/YYYY","none":"None","[3-10-2020]":"M-D-YYYY","[2020/03/10]":"YYYY/MM/DD","[March 10th 2020]":"MMMM Do YYYY"}},"timeFormat":{"description":"The time format of the exported data using a MomentJS time string (https://momentjs.com/).","type":"string","default":"x","suggestions":{"12 Hour w/ Meridiem and Seconds [8:41:56 AM]":"h:mm:ss A","Unix Timestamp [1563464737]":"X","none":"None","24 Hour w/ Milliseconds [08:41:06:269]":"HH:mm:ss:SSS","Unix Millisecond Timestamp [1563464737269]":"x","12 Hour [8:41]":"h:mm","12 Hour w/ Meridiem [8:41 AM]":"h:mm A","24 Hour w/ Seconds [08:41:06]":"HH:mm:ss"}}}},"startDate":{"visibleWhen":{"equals":["historical"],"property":"mode"},"description":"Start date for a historical data query.","type":["date","null"],"default":null}}}}},"resources":[{"type":"js","dependencies":["perspective-components-js"],"path":"/res/perspective/js/PerspectiveTimeseriesCharts.js","name":"perspective-react-timeseries-js"},{"type":"css","dependencies":["perspective-components-css"],"path":"/res/perspective/css/PerspectiveTimeseriesCharts.css","name":"perspective-react-timeseries-css"}],"defaultMetaName":"PowerChart","name":"Power Chart","palette":{"variants":[{"tooltip":"A flexible chart designed to visualize time series data and provide full configuration from a running session.","label":"Power Chart"}],"category":"chart"},"id":"ia.chart.powerchart"}

Trend Style Schema
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Trend Style Schema",
  "type": "object",
  "properties": {
    "colorScheme": {
      "type": "string",
      "enum": [
        "Spectral", "RdYlGn", "RdBu", "PiYG", "PRGn",
        "RdYlBu", "BrBG", "RdGy", "PuOr", "Set2",
        "Accent", "Set1", "Set3", "Dark2", "Paired",
        "Pastel2", "Pastel1", "OrRd", "PuBu", "BuPu",
        "Oranges", "BuGn", "YlOrBr", "YlGn", "Reds",
        "RdPu", "Greens", "YlGnBu", "Purples", "GnBu",
        "Greys", "YlOrRd", "PuRd", "Blues", "PuBuGn"
      ],
      "description": "Specifies a Color Brewer color scheme to use on the series (http://colorbrewer2.org/)."
    },
    "colors": {
      "type": "array",
      "description": "If provided, the colors listed here will override the colors used in the colorScheme.",
      "items": {
        "type": "string",
        "format": "color"
      }
    },
    "normal": {
      "$ref": "#/definitions/styleConfig",
      "description": "The style applied to the default state of the trend."
    },
    "highlighted": {
      "$ref": "#/definitions/styleConfig",
      "description": "The style applied to the highlighted state of the trend."
    },
    "selected": {
      "$ref": "#/definitions/styleConfig",
      "description": "The style applied to the selected state of the trend."
    },
    "muted": {
      "$ref": "#/definitions/styleConfig",
      "description": "The style applied to the muted (unselected) state of the trend."
    }
  },
  "definitions": {
    "styleConfig": {
      "properties": {
        "stroke": {
          "type": "object",
          "properties": {
            "color": {
              "type": "string",
              "format": "color",
              "description": "The color to apply to the line stroke, if applicable."
            },
            "width": {
              "type": [ "number", "null" ],
              "description": "The width to apply to the line stroke, if applicable."
            },
            "opacity": {
              "type": [ "number", "null" ],
              "description": "The opacity to apply to the line stroke, if applicable."
            },
            "dashArray": {
              "type": [ "number", "null" ],
              "description": "The spacing to apply between dashes of the line stroke, if applicable."
            }
          }
        },
        "fill": {
          "type": "object",
          "properties": {
            "color": {
              "type": "string",
              "format": "color",
              "description": "The color to apply to the trend fill, if applicable."
            },
            "opacity": {
              "type": [ "number", "null" ],
              "description": "The opacity to apply to the trend fill, if applicable."
            }
          }
        }
      }
    }
  }
}