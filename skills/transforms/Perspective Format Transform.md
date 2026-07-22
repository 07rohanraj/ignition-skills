# Perspective Format Transform

## Description

The usage and configuration of the Perspective Format Transform, which is used to change the display format of bound data without altering the underlying value. These instructions detail how to format numeric values as currency, percentages, or with specific decimal precision, and how to convert date/time values into various human-readable string formats using predefined styles or custom patterns.

## Documentation

# Instructions
This document provides instructions for using the Perspective Format Transform in Ignition.

### Overview

The Format Transform is used within a component binding to alter the display format of a bound value. It does not change the underlying value itself, but rather how it is presented. This is particularly useful for formatting numbers (e.g., adding currency symbols, controlling decimal places) and dates/times (e.g., converting a raw timestamp into a human-readable string). The transform takes the raw value from the binding (like a number, a float, or a Unix timestamp) and outputs a formatted string.

The primary configuration property is `formatType`, which determines whether you are formatting a number or a date/time.

---

### Configuration Instructions

#### 1. `formatType: "numeric"`

This mode is for formatting numerical values.

**Properties:**

*   **`formatType`**: Must be set to `"numeric"`.
*   **`formatValue`**: (Required) This defines the formatting style. It can be one of two types:
    *   **A Predefined Format String:**
        *   `"integer"`: Rounds a floating-point number to the nearest integer.
        *   `"number"`: Formats the number according to the specified `locale`, which typically includes adding group separators (e.g., commas in "1,234.5").
        *   `"percent"`: Multiplies the input value by 100 and appends a percent sign. For example, an input of `0.123` would become `12.3%`.
        *   `"currency"`: Formats the number as a currency value according to the specified `locale`.
    *   **A Custom Pattern String:**
        *   A user-defined pattern that follows Java's `DecimalFormat` rules. Use `#` for optional digits and `0` for mandatory digits.
        *   **Example**: The pattern `#.00` will format a number to always show exactly two decimal places. An input of `45.970097` would be formatted as `"45.97"`.
*   **`locale`**: (Optional) A string that specifies the locale to use for formatting. This affects things like the currency symbol and number separators. If set to `"auto"` (the default), the client's locale will be used.

#### 2. `formatType: "datetime"`

This mode is for formatting date and time values. The input is typically a timestamp (e.g., a Unix timestamp with milliseconds).

**Properties:**

*   **`formatType`**: Must be set to `"datetime"`.
*   **`formatValue`**: (Required) This defines the date/time formatting. It can be one of two types:
    *   **A Custom Pattern String:**
        *   A user-defined pattern string that follows Java's `SimpleDateFormat` rules.
        *   **Example**: `"yyyy-MM-dd h:mm:ss aa"` will format a timestamp into a string like `"2023-10-27 4:30:00 PM"`.
    *   **A Format Object:**
        *   An object containing a `date` and/or a `time` property. At least one of the two must be present.
        *   **`date`**: Specifies the format for the date part. Can be one of:
            *   `"full"` (e.g., "Monday, March 18, 2019")
            *   `"long"` (e.g., "March 18, 2019")
            *   `"medium"` (e.g., "Mar 18, 2019")
            *   `"short"` (e.g., "3/18/19")
        *   **`time`**: Specifies the format for the time part. Can be one of:
            *   `"full"` (e.g., "2:02:46 PM Pacific Standard Time")
            *   `"long"` (e.g., "2:02:46 PM PST")
            *   `"medium"` (e.g., "2:02:46 PM")
            *   `"short"` (e.g., "2:02 PM")
*   **`locale`**: (Optional) A string that specifies the locale to use for formatting month names, day names, etc. If set to `"auto"` (the default), the client's locale will be used.
*   **`timezone`**: (Optional) A string that specifies the timezone to apply to the date/time. If set to `"auto"` (the default), the client's timezone will be used. This is useful for displaying a stored UTC timestamp in a specific local time.
    *   **Example**: An input of `1551823366022` with the timezone set to `"Japan"` would be formatted as `"3/6/19, 7:02 AM"`.

---

### Helpful Tips

*   The default configuration for a new Format Transform is `{"formatType":"datetime","formatValue":"yyyy-MM-dd h:mm:ss aa"}`.
*   Transforms are executed in order from top to bottom when multiple are applied to a single binding. The Format Transform will operate on the value that is passed into it from the binding or the preceding transform.
*   The input to the transform is the raw binding value; the output is always a formatted string.
*   For numeric patterns, use `0` to represent a digit that must be present (even if it's a leading or trailing zero) and `#` to represent a digit that will not be displayed if it's a leading or trailing zero.
*   When using the object format for `datetime`, you can show just the date (by only providing the `date` property), just the time (by only providing the `time` property), or both.
*   The `locale` and `timezone` properties with a value of `"auto"` provide formatting that is localized to the end-user's system (the Perspective client), which is generally recommended for user-facing displays.
*   Custom numeric format strings follow the pattern rules of Java's `DecimalFormat`.
*   Custom date-time format strings follow the pattern rules of Java's `SimpleDateFormat`.

# Schema - raw
{"definitions":{"date-time-format-value":{"anyOf":[{"type":"object","description":"Common date-time formats. See Java's DateFormat#get*Instance where * can be replaced with Date, Time, or DateTime based on the presence of the respective properties in the instance of this definition","properties":{"date":{"$ref":"#/definitions/date-time-enum"},"time":{"$ref":"#/definitions/date-time-enum"}},"anyOf":[{"required":["date"]},{"required":["time"]}]},{"type":"string","description":"Custom user-defined date-time format string which follows the pattern rules of Java's SimpleDateFormat"}]},"date-time-enum":{"type":"string","enum":["full","long","medium","short"]}},"type":"object","description":"JSON Schema for the Format Transform","format":"format","anyOf":[{"properties":{"formatType":{"type":"string","constant":"datetime"},"formatValue":{"$ref":"#/definitions/date-time-format-value"},"locale":{"type":"string"},"timezone":{"type":"string"}}},{"properties":{"formatType":{"type":"string","constant":"numeric"},"formatValue":{"anyOf":[{"type":"string","description":"Common numeric formats. See Java's NumberFormat#get*Instance where * can be replaced with one of the enum values in this definition","enum":["currency","integer","number","percent"]},{"type":"string","description":"Custom user-defined numeric format string which follows the pattern rules of Java's DecimalFormat"}]},"locale":{"type":"string"}}}],"required":["formatType","formatValue"],"default":{"formatType":"datetime","formatValue":"yyyy-MM-dd h:mm:ss aa"}}