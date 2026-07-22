# Perspective Query Binding

## Description

The configuration of a Perspective Query Binding to dynamically link a component property to a database by executing a pre-defined Named Query. These instructions cover specifying the query path, providing expression-based parameters, and setting the data return format. Additionally, they explain how to control the data refresh rate through polling and manage performance using caching options.

## Documentation

# Instructions
Here are the instructions for the **Perspective Query Binding**:

A Perspective Query Binding is used to execute a Named Query and use the results to drive a property on a component. This binding type links a component property directly to a database query, allowing for dynamic data display.

### Instructions

1.  **Specify the Named Query Path**:
    *   You MUST provide a `queryPath`, which is a string that points to an existing Named Query in the Ignition project.
    *   You CANNOT write a raw SQL query directly within this binding. The query must be pre-defined as a Named Query.

2.  **Provide Query Parameters**:
    *   If the specified Named Query has parameters, you will provide their values in the `parameters` object.
    *   The `parameters` object consists of key-value pairs, where the key is the exact name of the parameter in the Named Query.
    *   **CRITICAL**: The value for each parameter is treated as an **expression**.
        *   For a static string, you must wrap it in quotes: `{"myParam": "'some_string'"}`
        *   For a number, use the numeric literal: `{"myParam": "123"}`
        *   To bind the parameter to another property, use the property binding syntax: `{"myParam": "{view.props.someValue}"}`

3.  **Configure Polling (Refresh Rate)**:
    *   The `polling` object controls how often the query is executed.
    *   If `polling.enabled` is `false` (the default), the query will execute once when the view loads, and will automatically re-execute only if the value of one of its `parameters` changes.
    *   If `polling.enabled` is `true`, the query will execute repeatedly at a specified interval.
    *   The `polling.rate` defines this interval in seconds. The default is 5 seconds. This can be a static number (e.g., `10`) or an expression string that resolves to a number (e.g., `"{view.custom.dynamicPollRate}"`). A rate less than or equal to zero will disable polling.

4.  **Set the Return Format**:
    *   Use the `returnFormat` property to specify the data format for the query results.
    *   `auto`: (Default) Returns the data in the database's native format, which is typically a dataset.
    *   `dataset`: Explicitly returns the results as a dataset.
    *   `json`: Returns the results as a JSON object. Each row is an object in an array.
    *   `scalar`: Returns only the value from the first column of the first row of the result set. This is ideal when you expect only a single value.

5.  **Control Caching and Performance**:
    *   `bypassCache`: By default (`false`), the query binding uses a shared, cached polling engine. The query is run once at the poll rate, and the results are cached and distributed to all components using that same query. This is highly efficient. If polling is off, the cache lasts for 250 milliseconds.
    *   Set `bypassCache` to `true` to force this specific binding to execute the query against the database every time it updates, bypassing the shared cache. Use this only when you have a specific need to ignore potentially cached values.
    *   `designerUseLimit`: By default (`true`), the query will respect the row limit settings defined in the Named Query when executed within the Designer. This improves designer performance by preventing large datasets from being loaded.

### Helpful Tips
*   **Parameter Values are Expressions**: This is the most common point of error. Always remember that parameter values are evaluated as expressions. A string literal `'Completed'` is a valid expression, but `Completed` is not (unless it's a reference to something else).
*   **Polling is Not Always Necessary**: If your query depends on parameters that change based on user interaction (like selecting an item in a list), you often do not need to enable polling. The binding will automatically update when the parameter value changes.
*   **Use `scalar` for Single Values**: When you need to display a single piece of data (e.g., a count, a name, a status) in a component like a Label or a Text Field, set `returnFormat` to `scalar`. This simplifies the binding by directly returning the value instead of a dataset that you would then need to parse.
*   **Dynamic Poll Rate**: Because the `polling.rate` can be an expression, you can make the polling frequency dynamic. For example, you could bind it to a slider component to allow a user to control the refresh rate.
*   **Transforms**: The documentation mentions that transforms can be added to a Query Binding to further manipulate the results (e.g., sort, filter, or re-shape the data) before it is applied to the property.
*   **Check the Named Query**: Since you cannot see the query's text directly, you must refer to the project's Named Queries section to understand what the `queryPath` is referencing, what parameters it expects, and what columns it returns.

# Schema - raw
{"type":"object","properties":{"queryPath":{"type":"string","description":"Path to the named query this binding will execute"},"returnFormat":{"type":"string","description":"The format to use for the results of the query execution","enum":["auto","json","dataset","scalar"],"default":"auto"},"parameters":{"type":"object","description":"Parameter values to be passed to the query. Values are expressions.","default":{}},"polling":{"type":"object","properties":{"enabled":{"type":"boolean","description":"If true, the query will polled: that is, executed repeatedly at an interval. If false, the query will only run once on startup and again as parameter values change.","default":false},"rate":{"type":["number","string"],"description":"The rate at which the query will be executed. If numeric, this rate will be interpreted as the number of seconds between executions. If a string, the string will be interpreted as an expression whose result will be the poll rate. If the rate is not positive, polling will be disabled.","default":5}},"additionalProperties":false},"designerUseLimit":{"type":"boolean","description":"If true, this query will use the query's limit settings when executed in the designer.","default":true},"bypassCache":{"type":"boolean","description":"If true, this binding will bypass the query's cache built-in result cache.","default":false}},"required":["queryPath"],"additionalProperties":false}