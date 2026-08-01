# Perspective Chart Range Selector Component

## Description

These instructions detail the usage and configuration of the Perspective Chart Range Selector component. They explain how to use this component to provide a user-driven time range selection that can filter the data displayed in other charts. The document also provides a complete reference for configuring the component's properties, including data binding, axis formatting, visual styling, and user interaction controls.

## Documentation

# Instructions
This document provides instructions for using the **Perspective Chart Range Selector** component in Ignition.

### Object Description

The Perspective Chart Range Selector is a specialized chart component designed to facilitate the selection of a specific time range from a larger dataset. It displays a small overview of the data, and users can interact with it by "brushing" (clicking and dragging) to highlight a period. This selection then outputs a start and end time, which can be used to control the data displayed in other components, most commonly a Time Series Chart. It supports panning, zooming, and customizable styling for its various visual elements.

### How to Use the Chart Range Selector

The primary use case for the Chart Range Selector is to control the time range of a main chart, like the Time Series Chart.

**Setup Example:**

1.  **Place Components:** Add a **Chart Range Selector** and a **Time Series Chart** to your View.
2.  **Configure Chart Range Selector Data:**
    *   Select the Chart Range Selector component.
    *   Bind its `props.data` property to a data source that contains a wide range of historical data. A common method is to use a **Tag History Binding** set to a "Historical" time range (e.g., "Last 8 hours"). This binding will populate the selector with the overall data view.
3.  **Configure Time Series Chart Data:**
    *   Select the Time Series Chart component.
    *   Bind its primary data property (e.g., `props.series[0].data`) to the same data source (e.g., a Tag History Binding).
4.  **Link the Components:** This is the most critical step.
    *   In the Time Series Chart's Tag History binding configuration, set the Time Range to "Historical".
    *   Bind the **Start Date** of the binding to the `props.selectedRange.start` property of the Chart Range Selector.
    *   Bind the **End Date** of the binding to the `props.selectedRange.end` property of the Chart Range Selector.

Now, when a user interacts with the brush on the Chart Range Selector, the `selectedRange.start` and `selectedRange.end` properties will update, causing the Time Series Chart's binding to re-query with the new date range and display the selected slice of data.

### Property Reference

#### **`data`**
*   **Description**: The dataset that the chart will visualize. This is the source data for the component.
*   **Data Formats**:
    1.  **Array of Objects**: `[{"time": 1560469431423, "Temperature": 52}, {"time": 1560469432423, "Temperature": 18}]`
    2.  **Array of Arrays**: `[[1560469431423, 52], [1560469432423, 18]]` (Timestamp must be the first element).
    3.  **Dataset Object**: An object with `columns` and `rowCount` properties, where the first column is the timestamp. This is the format returned by Tag History bindings.
*   **Type**: `array` or `object`

#### **`selectedRange`**
*   **Description**: An object representing the start and end of the user's selection (the "brush"). This is a read-only property that is updated by user interaction. You bind *from* this property, not *to* it.
*   **Properties**:
    *   `start`: The start timestamp of the selection in Unix milliseconds.
    *   `end`: The end timestamp of the selection in Unix milliseconds.
*   **Type**: `object`

#### **`timeAxis`** (X-axis)
*   **Description**: An object for configuring the bottom time axis.
*   **Properties**:
    *   `visible`: Toggles the visibility of the axis.
    *   `color`: Sets the color of the axis line.
    *   `height`: The height of the axis area in pixels.
    *   `tickCount`: The desired number of ticks to display on the axis.
    *   `tick`: An object to configure the ticks.
        *   `color`: Color of the tick marks.
        *   `label`: An object to configure the tick labels.
            *   `format`: A **MomentJS** format string (e.g., `"YYYY-M-D h:mm:ss"`) to define how the date/time is displayed. `"Auto"` is the default.
            *   `angled`: If `true`, text is displayed at an angle.
            *   `font`: Contains `color` and `size` properties for the label text.
            *   `style`: Style object for the tick labels.
    *   `grid`: An object to configure gridlines that extend from this axis.
        *   `visible`: Toggles gridline visibility. **Note:** When the grid is visible, ticks are hidden.
        *   `color`, `opacity`, `dashArray`: Styling for the gridlines.

#### **`yAxis`** (Y-axis)
*   **Description**: An object for configuring the vertical value axis.
*   **Properties**:
    *   `visible`: Toggles the visibility of the axis.
    *   `color`: Sets the color of the axis line.
    *   `width`: The width of the axis area in pixels.
    *   `label`: An object to configure the axis title.
        *   `visible`: Toggles the label's visibility.
        *   `text`: The text to display for the axis label (e.g., "Temperature").
        *   `offset`: A numeric value to adjust the label's position.
        *   `font`: Contains `color` and `size` properties for the label text.
    *   `tick`: An object to configure the ticks.
        *   `count`: The number of ticks. `"Auto"` is default.
        *   `label`: An object to configure the tick labels.
            *   `format`: A **D3 format string** (e.g., `",.2f"`) to define how numeric values are displayed. `"Auto"` is the default.
            *   `font`: Contains `color` and `size` properties for the label text.
    *   `grid`: An object to configure gridlines. (Same properties as `timeAxis.grid`).

#### **`brushRange`**
*   **Description**: Controls the visibility and format of the date/time range text displayed below the chart, which shows the current brush selection.
*   **Properties**:
    *   `visible`: Toggles the visibility of this text.
    *   `dateFormat`: A **MomentJS** format string for the date portion (e.g., `"MM-DD-YYYY"`).
    *   `timeFormat`: A **MomentJS** format string for the time portion (e.g., `"HH:mm:ss"`).

#### **`areaStyles`**
*   **Description**: Defines the default styling for the data trends shown on the chart.
*   **Properties**:
    *   `colorScheme`: A ColorBrewer scheme name (e.g., `"RdBu"`) to automatically color the trends.
    *   `colors`: An array of color strings (e.g., `["#FF0000", "#0000FF"]`). If provided, this list will override the `colorScheme`.

#### **`enablePanZoom`**
*   **Description**: A boolean that, when `true`, allows the user to pan and zoom the chart's view using the mouse wheel or pinch-to-zoom on mobile.

### Helpful Tips & Best Practices

*   **Complementary Component**: The Chart Range Selector is almost always used in conjunction with another component, like the Time Series Chart, to filter its data.
*   **Read `selectedRange`**: Remember that `props.selectedRange` is an **output** property. The component updates it for you. You should only create bindings that read *from* this property.
*   **User Interaction**:
    *   **Zoom**: Use the mouse wheel or pinch-zoom (on mobile).
    *   **Pan**: Click and drag the chart background.
    *   **Select/Brush**: Click and drag within the chart to create a selection.
    *   **Move Selection**: Click and drag the existing selection (the "brush") to move it.
*   **Formatting Syntax**: Be aware of the different formatting languages required:
    *   **MomentJS**: Used for `timeAxis.tick.label.format`, `brushRange.dateFormat`, and `brushRange.timeFormat`.
    *   **D3**: Used for `yAxis.tick.label.format`.
*   **Grid vs. Ticks**: For a given axis, the gridlines and tick marks are mutually exclusive. If `grid.visible` is true, the `tick` marks will be hidden.
*   **Mobile Usage**: On mobile devices, a single touch-and-drag creates or moves a brush. A multi-touch gesture (like pinching) is used for zooming.
*   **Data Volume**: The component needs to load and render all the data passed to its `props.data` property. For extremely large time ranges or high-density data, be mindful of potential performance impacts on the client.

# Schema - raw
{"schema":{"type":"object","additionalProperties":false,"definitions":{"grid":{"description":"Configuration for gridlines to display on this axis.","type":"object","properties":{"visible":{"description":"Visible state of the gridlines. Gridlines are shown only for axes that connect directly to the chart. Any satellite axes will display their tick configurations instead of gridlines.","type":"boolean","default":false},"color":{"format":"color","description":"Color of the gridlines.","type":"string","default":""},"style":{"description":"Style properties to be applied to the axis gridlines.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"opacity":{"description":"Opacity of the gridlines.","type":"number","default":0.9},"dashArray":{"description":"Dashed appearance of the gridlines.","type":"number","default":0}}}},"properties":{"data":{"description":"The raw data used to build the chart.","example":[{"Temperature":52,"time":1560469431423},{"Temperature":18,"time":1560469432423},{"Temperature":26,"time":1560469433423},{"Temperature":63,"time":1560469434423},{"Temperature":65,"time":1560469435423},{"Temperature":12,"time":1560469436423},{"Temperature":61,"time":1560469437423},{"Temperature":60,"time":1560469438423},{"Temperature":58,"time":1560469439423},{"Temperature":1,"time":1560469440423}],"oneOf":[{"description":"Data are an object containing a 'time' entry and value entries. Each value entry must be labeled with the column name that it corresponds to.","type":"array","items":{"type":"object","required":["time"],"properties":{"time":{"description":"The timestamp when the data values were captured.","type":["string","number"]}}}},{"description":"Data are an array containing value entries. Each value entry consists of a timestamp (which must be the FIRST value) and one or more values that were captured at that time.","type":"array","items":{"description":"The first entry corresponds to the first column (timestamp), and each successive entry corresponds to the remaining column labels.","type":"array","items":{"type":["number","string"]}}},{"description":"Data are in the form of a dataset where the timestamp is the FIRST value per entry in the dataset.","type":"object","properties":{"columns":{"type":"array"},"rowCount":{"type":"number"}}}],"default":[]},"timeAxis":{"description":"Configuration for the time axis (X axis) of the chart.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the time axis.","type":"boolean","default":true},"color":{"format":"color","description":"The color of the axis.","type":"string","default":""},"tick":{"description":"Tick configuration. When the grid is displaying, ticks will be hidden.","type":"object","properties":{"color":{"format":"color","description":"The color of the ticks.","type":"string","default":""},"label":{"description":"Tick label configuration.","type":"object","properties":{"format":{"description":"The date/time format displayed by each tick using a MomentJS date string (https://momentjs.com/).","type":"string","default":"Auto","suggestions":{"[2020-3-2 8:15:35]":"YYYY-M-D h:mm:ss","Day of Week, Month, and Hour [Monday 2nd, 08 AM]":"dddd Do, hh A","Unix Timestamp [1563464737]":"X","Full Month [January]":"MMMM","Abbreviated Month and Day of Month [Jan 2nd]":"MMM Do","Auto":"Auto","Hour Minute [8:15]":"h:mm","Abbreviated Month and Year [Jan 20]":"MMM YY","Unix Millisecond Timestamp [1563464737269]":"x","Millisecond [638]":"SSS","Full Year [2020]":"YYYY","Hour with Meridiem [8 AM]":"h A","[3-2-2020 8:15:35]":"M-D-YYYY h:mm:ss","Second [:35]":":ss","Abbreviated Day of Week and Month [Mon 2nd]":"ddd Do"}},"angled":{"description":"A flag to toggle the angled state of the tick labels.","type":"boolean","default":false},"style":{"description":"Style properties to be applied to the tick labels. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"font":{"description":"Tick label font configuration.","type":"object","properties":{"color":{"format":"color","description":"The color of the tick label text.","type":"string","default":""},"size":{"description":"The size of the tick label text.","type":["number","string"],"default":10}}}}},"style":{"description":"Style properties to be applied to the ticks. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"tickCount":{"description":"The number of ticks.","type":"number","default":5},"grid":{"$ref":"#/definitions/grid"},"style":{"description":"Style properties to be applied to the axis. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"height":{"description":"The height of the time axis.","type":"number","default":35}}},"yAxis":{"description":"Configuration for the Y axis of the chart.","type":"object","additionalProperties":false,"properties":{"visible":{"description":"The visible state of the Y axis.","type":"boolean","default":true},"label":{"description":"Y axis label configuration.","type":"object","properties":{"visible":{"description":"The visible state of the Y axis label.","type":"boolean","default":true},"offset":{"description":"Offset the Y axis label from its default position. This allows you to fine tune the label location, which may be necessary depending on the scale and how much room the tick labels take up. Maybe positive or negative.","type":"number","default":0},"style":{"description":"Style properties to be applied to the axis label. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"The text of the Y axis label.","type":"string","default":""},"font":{"description":"Y axis label font configuration.","type":"object","properties":{"color":{"format":"color","description":"The color of the Y axis label text.","type":"string","default":""},"size":{"description":"The size of the Y axis label text.","type":["number","string"],"default":10}}}}},"tick":{"description":"Tick configuration. When the grid is displaying, ticks will be hidden.","type":"object","properties":{"color":{"format":"color","description":"The color of the ticks.","type":"string","default":""},"count":{"description":"The number of ticks. If \"Auto\" is used, the ticks will be determined by available space in the interface.","type":["number","string"],"default":"Auto","suggestions":{"2":2,"4":4,"6":6,"8":8,"10":10,"Auto":"Auto"}},"label":{"description":"Tick label configuration.","type":"object","properties":{"format":{"description":"Data format displayed by each tick using a D3 format string (https://github.com/d3/d3-format).","type":"string","default":"Auto","suggestions":{"Currency [$1,234.00]":"$,.2f","2 Decimal Points [1234.00]":".2f","Percentage [123400%]":".0%","Comma-Separated Integer [1,234]":",.0f","Hexadecimal (lowercase) [4d2]":"x","4 Decimal Points [1234.0000]":".4f","Auto":"Auto","Integer [1234]":"d","Binary [10011010010]":"b","Hexadecimal (uppercase) [4D2]":"X","Octal [2322]":"o","Comma-Separated w/ 2 Decimal Points [1,234.00]":",.2f","Exponential [1.234000e+3]":"e"}},"style":{"description":"Style properties to be applied to the tick labels. Any style that applies to an SVG text element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"font":{"description":"Label font configuration.","type":"object","properties":{"color":{"format":"color","description":"The color of the label text.","type":"string","default":""},"size":{"description":"The size of the label text.","type":["number","string"],"default":10}}}}},"style":{"description":"Style properties to be applied to the ticks. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"grid":{"$ref":"#/definitions/grid"},"width":{"description":"The width of the Y axis.","type":"number","default":60},"style":{"description":"Style properties to be applied to the axis. Any style that applies to an SVG line element can be used.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"areaStyles":{"description":"The default styles to apply to the chart.","default":{"colors":[],"colorScheme":"RdBu"},"$ref":"urn:ignition-schema:schemas/trend-style.schema.json"},"selectedRange":{"description":"The start and end points of the range selection.","type":"object","required":["start","end"],"additionalProperties":false,"properties":{"start":{"description":"A Date or timestamp in milliseconds.","type":["date","number"],"default":-1},"end":{"description":"A Date or timestamp in milliseconds.","type":["date","number"],"default":-1}}},"brushRange":{"description":"Properties to govern the display of the date/time range below the chart.","type":"object","required":["visible","dateFormat","timeFormat"],"additionalProperties":false,"properties":{"visible":{"description":"Show the brush data range below the chart.","type":"boolean","default":true},"dateFormat":{"description":"The date format of the range using a MomentJS date string (https://momentjs.com/).","type":"string","default":"M-D-YYYY","suggestions":{"[Jul 18th 19]":"MMM Do YY","none":"None","[2019-7-18]":"YYYY-M-D","[7-18-2019]":"M-D-YYYY","[07-18-2019]":"MM-DD-YYYY","[2019-07-18]":"YYYY-MM-DD","[July 18th 2019]":"MMMM Do YYYY"}},"timeFormat":{"description":"The time format of the range using a MomentJS time string (https://momentjs.com/).","type":"string","default":"h:mm:ss","suggestions":{"24 hour w/ milliseconds [08:41:06:269]":"HH:mm:ss:SSS","Unix Timestamp [1563464737]":"X","none":"None","12 hour [8:41:06]":"h:mm:ss","12 hour w/ period [8:41:06 AM]":"h:mm:ss A","24 hour [08:41:06]":"HH:mm:ss","Unix Millisecond Timestamp [1563464737269]":"x"}}}},"style":{"description":"Style properties to be applied to the base component.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"enablePanZoom":{"description":"Allow the chart to be panned and zoomed.","type":"boolean","default":true}}},"resources":[{"type":"js","dependencies":["perspective-components-js"],"path":"/res/perspective/js/PerspectiveTimeseriesCharts.js","name":"perspective-react-timeseries-js"},{"type":"css","dependencies":["perspective-components-css"],"path":"/res/perspective/css/PerspectiveTimeseriesCharts.css","name":"perspective-react-timeseries-css"}],"defaultMetaName":"ChartRangeSelector","name":"Chart Range Selector","palette":{"variants":[{"tooltip":"A small chart used to select a time range of data. Complements the Time Series Chart.","label":"Chart Range Selector"}],"category":"chart"},"id":"ia.chart.chartrangeselector"}