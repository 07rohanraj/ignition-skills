# Perspective Tag History Binding

## Description

This document explains how to configure and use a Perspective Tag History Binding to query historical data from the Ignition Tag Historian. It covers defining the target tags and time range, controlling the data's return format and sampling size, and setting aggregation and polling behaviors to retrieve customized datasets for display or manipulation within Perspective components.

## Documentation

# Instructions
This document provides instructions for an LLM on how to configure and use a **Perspective Tag History Binding** in Ignition.

### Object Name
Perspective Tag History Binding

### Instructions

A Tag History Binding is used to query the Tag Historian module to retrieve historical data for one or more Ignition tags. This data can then be displayed or manipulated by a Perspective component. The configuration of the binding determines which tags are queried, over what time period, and in what format the data is returned.

**1. Define the Tags to Query (`tags`)**

This is a **required** property that specifies the tags you want to retrieve history for. You have two methods for this:

*   **As an Array of Tag Objects (Directly):**
    Provide a list of JSON objects, where each object represents a tag.
    *   `path` (string, required): The full path to the tag. Example: `"[default]Path/To/MyTag"`
    *   `alias` (string, optional): A friendly name for the tag. If provided, the resulting data column will use this alias instead of the full tag path. This is highly recommended for readability.
    *   `aggregate` (string, optional): An aggregation mode specific to this tag, which will override the binding's default `aggregate` property.

    *Example:*
    ```json
    [
        {"path": "[default]Sinusoid/Sine0", "alias": "Sine Wave 0"},
        {"path": "[default]Sinusoid/Sine2", "alias": "Sine Wave 2", "aggregate": "MinMax"}
    ]
    ```

*   **As a String Expression:**
    Provide a string that is a property binding path to another property on the view (like a custom property) that contains the array of tag objects as described above. This allows for dynamic tag selection.

    *Example:*
    If you have a custom property `view.custom.myTags` that holds the JSON array from the previous example, you would set the `tags` property to the string `"view.custom.myTags"`.

**2. Specify the Time Range (`dateRange`)**

This is a **required** property that defines the time period for the historical query. There are two types of time ranges:

*   **Real-time / Most Recent:** Fetches data from a recent period up to the current moment. This configuration will poll for new data.
    *   `mostRecent` (string or number): The amount of time to look back.
    *   `mostRecentUnits` (string): The units for `mostRecent`. Must be one of: `"sec"`, `"min"`, `"hour"`, `"day"`, `"week"`, `"month"`.

    *Example (for the last 10 minutes):*
    ```json
    {"mostRecent": "10", "mostRecentUnits": "min"}
    ```

*   **Historical:** Fetches data between a fixed start and end date. This configuration will not poll unless polling is explicitly enabled.
    *   `startDate` (string or number): The start of the time range. Can be a date string (e.g., `"2023-10-27 10:00:00"`) or an expression.
    *   `endDate` (string or number): The end of the time range. Can be a date string or an expression (e.g., `now()`).

    *Example:*
    ```json
    {"startDate": "2023-10-27 10:00:00", "endDate": "2023-10-27 11:00:00"}
    ```

**3. Set the Return Data Format (`returnFormat`)**

This property determines the structure of the resulting dataset.

*   `"wide"` (default): Returns a dataset where the first column is the timestamp (`t_stamp`), and each subsequent column represents a single tag, identified by its path or alias.
*   `"tall"`: Returns a "normalized" dataset with four columns: `Path`, `Value`, `Quality`, and `Timestamp`. Each row represents a single data point for a single tag.
*   `"calculations"`: Does not return a time-series dataset. Instead, it performs the aggregate functions specified in the `calculations` property on each tag over the entire `dateRange` and returns a single row of results.

**4. Control the Number of Returned Rows (`returnSize`)**

This property dictates the sampling or granulation of the data.

*   `{"type": "raw"}` (default): Returns the data points as they were stored in the database.
*   `{"type": "natural"}`: Returns points at the "natural" rate of the underlying data.
*   `{"type": "fixed", "numRows": <integer>}`: Returns a fixed number of rows, evenly distributed across the specified `dateRange`.
*   `{"type": "interval", "delay": <integer>, "delayUnits": "<unit>"}`: Returns one data point per interval. For example, `{"type": "interval", "delay": 5, "delayUnits": "sec"}` will return one point every 5 seconds.

**5. Configure the Default Aggregation Mode (`aggregate`)**

This property sets the default aggregation mode for all tags in the query. It dictates how multiple raw values within a single time slice are combined into one representative value. This can be overridden on a per-tag basis (see step 1). The default is `"Average"`. See the list of available modes in the tips section.

**6. Configure Polling (`polling`)**

This object controls whether the binding periodically re-executes.
*   `enabled` (boolean): If `true`, the binding will poll. If `false` (default), it runs once, and then only again if one of its parameters changes. Real-time date ranges will poll by default.
*   `rate` (number or string): The polling frequency in seconds. Default is 5.

### Helpful Tips

*   **Use Aliases:** Always use the `alias` property when defining tags. It makes the resulting dataset columns much easier to work with, especially when using the `"wide"` return format.
*   **Understand Aggregation Modes:** The choice of aggregation mode is critical for displaying meaningful data.
    *   **Average:** Time-weighted average of values in the time slice.
    *   **MinMax:** Returns two rows for the time slice: the minimum and maximum values.
    *   **LastValue:** The value closest to the end time of the slice.
    *   **SimpleAverage:** The mathematical average (sum / count).
    *   **Sum:** The sum of all values.
    *   **Minimum / Maximum:** The single minimum or maximum value.
    *   **DurationOn / DurationOff:** Time in seconds the value was non-zero / zero.
    *   **CountOn / CountOff:** Number of times the value changed from zero to non-zero / non-zero to zero.
    *   **Count:** The total number of data points recorded.
    *   **Range:** The difference between the highest and lowest value. Returns 0 if the value was static.
    *   **StdDev / Variance:** Statistical standard deviation or variance.
    *   **PctGood / PctBad:** Time-weighted percentage of good or bad quality data.
*   **Historical Query End Date Warning:** A historical query is inclusive of its end date. If you query from 10:00 to 11:00 in 1-minute intervals, you may get an extra interval for 11:00-11:01 which will likely contain no data or an interpolated zero. To avoid this, set your end date just before the next interval begins (e.g., end at `10:59:59` instead of `11:00:00`).
*   **Wide vs. Tall Format:** Use `"wide"` format for components like the Power Chart that expect a column per data series. Use `"tall"` format for Tables where you might want to sort or filter by tag path, or for more complex scripting manipulations.
*   **Calculations Format:** Use the `"calculations"` format when you don't need a trend but rather a single aggregated value over a period, such as "what was the average temperature over the last 8 hours?". The specific calculations to perform are passed in the `calculations` array property.
*   **Data Quality:** Set `ignoreBadQuality` to `true` to ensure your dataset contains only values logged with "Good" data quality.
*   **Interpolation:** The system will "fill in the gaps" by default to provide evenly spaced data points. Set `preventInterpolation` to `true` to disable this, which means you will only receive data for time slices where a raw value was actually recorded.
*   **Document vs. Dataset:** The `valueFormat` property can be set to `"document"` to return the result as a list of JSON objects instead of the standard Ignition Dataset object. This can be more convenient for certain scripting or component models.

# Schema - raw
{"definitions":{"aggregate":{"type":"string","description":"Dictates how multiple history values are \"aggregated\" together in order to form a result for a given time slice.","default":"Average","suggestions":["Average","MinMax","LastValue","SimpleAverage","Sum","Minimum","Maximum","DurationOn","DurationOff","CountOn","CountOff","Count","Range","Variance","StdDev","PctGood","PctBad"]}},"type":"object","properties":{"dateRange":{"oneOf":[{"type":"object","properties":{"startDate":{"type":["number","string"],"description":"A start date expression"},"endDate":{"type":["number","string"],"description":"An end date expression"}},"required":["startDate","endDate"]},{"type":"object","properties":{"mostRecent":{"type":["number","string"],"description":"An expression which emits the most recent real-time data to pull in milliseconds"},"mostRecentUnits":{"type":"string","enum":["sec","min","hour","day","week","month"]}},"required":["mostRecent","mostRecentUnits"]}]},"tags":{"oneOf":[{"type":"array","items":{"type":"object","properties":{"path":{"type":"string","default":""},"alias":{"type":"string","default":""},"aggregate":{"type":"string","default":""}},"default":{"path":""},"required":["path"]}},{"type":"string","default":""}]},"returnFormat":{"type":"string","enum":["wide","tall","calculations"],"default":"wide"},"returnSize":{"type":"object","anyOf":[{"properties":{"type":{"type":"string","constant":"raw"}},"required":["type"]},{"properties":{"type":{"type":"string","constant":"natural"}},"required":["type"]},{"properties":{"type":{"type":"string","constant":"fixed"},"numRows":{"type":"integer"}},"required":["type","numRows"]},{"properties":{"type":{"type":"string","constant":"interval"},"delay":{"type":"integer"},"delayUnits":{"type":"string","enum":["sec","min","hour"]}},"required":["type","delay","delayUnits"]}],"default":{"type":"raw"}},"polling":{"type":"object","properties":{"enabled":{"type":"boolean","description":"If true, the query will polled: that is, executed repeatedly at an interval. If false, the query will only run once on startup and again as parameter values change.","default":false},"rate":{"type":["number","string"],"description":"The rate at which the query will be executed. If numeric, this rate will be interpreted as the number of seconds between executions. If a string, the string will be interpreted as an expression whose result will be the poll rate. If the rate is not positive, polling will be disabled.","default":5}},"required":["enabled","rate"],"default":{"enabled":false,"rate":5}},"aggregate":{"$ref":"#/definitions/aggregate","description":"Default aggregation mode used by a column in case the column does not override it"},"valueFormat":{"type":"string","enum":["dataset","document"],"default":"dataset"},"ignoreBadQuality":{"type":"boolean","default":false},"preventInterpolation":{"type":"boolean","default":false},"avoidScanClassValidation":{"type":"boolean","default":false},"calculations":{"type":"array","items":{"$ref":"#/definitions/aggregate"}}},"required":["dateRange","tags"],"default":{"tags":[{"path":""}],"dateRange":{"mostRecent":"10","mostRecentUnits":"min"}}}