# Perspective Expression Binding

## Description

The usage and configuration of the Perspective Expression Binding, which dynamically calculates a property's value based on a custom expression. This binding allows you to combine tag values, component properties, operators, and functions to transform, format, or compute data, creating a value that updates automatically whenever its dependencies change.

## Documentation

# Instructions
# Name
Perspective Expression Binding

# Instructions
An Expression Binding is a powerful binding type that uses Ignition's expression language to calculate a value for a component property. It is used when data from one or more sources needs to be manipulated, transformed, combined, or computed before being applied to a property.

The binding configuration consists of a single property, `expression`, which is a string that holds the expression to be evaluated.

### Expression Components
The `expression` string can contain a combination of the following:

1.  **Tag References**: You can reference Tag values directly within the expression. The syntax for a Tag reference is `{TagName}`. The value of the Tag will be substituted into the expression when it is evaluated.
2.  **Property References**: You can reference other component properties. The syntax for a property reference is `{path.to.property}`. The value of that property will be used in the expression.
3.  **Operators**: Standard mathematical (`+`, `-`, `*`, `/`), logical, and comparison operators can be used to perform calculations.
4.  **Functions**: A large library of built-in expression functions are available to perform a wide variety of tasks, such as mathematical calculations (`abs`, `round`), date/time manipulation (`now`, `dateFormat`), type casting (`toInt`, `toString`), and conditional logic (`if`).

### How it Works
The Expression Binding will execute and update its value based on the components used within the expression:
*   **Event-Driven**: The binding will re-evaluate automatically whenever any of its dependencies change. For example, if the expression references a Tag, the expression will re-run every time that Tag's value changes. If it references another component's property, it will re-run when that property changes.
*   **Polling**: Certain functions, such as `now()`, cause the expression to execute on a fixed schedule. For example, `now(1000)` will cause the expression to re-evaluate every 1000 milliseconds (every second).

### Configuration
To configure an Expression Binding, you must provide a valid expression string for the `expression` property.

**Example 1: Combining two Tag values**
This expression adds the values of two Tags together.

```json
{
  "expression": "{path/to/Ramp0} + {path/to/Ramp1}"
}
```

**Example 2: Using a function on a Tag value**
This expression takes the absolute value of a Memory Tag.

```json
{
  "expression": "abs({path/to/MemoryTag})"
}
```

**Example 3: Conditional Logic**
This expression checks the value of a Tag and returns one of two strings.

```json
{
  "expression": "if({path/to/Motor/Amps} > 10, 'High Current', 'Normal')"
}
```

# Tips
*   An Expression binding is ideal for any situation where you need to transform, format, or calculate a value. If you only need to display a direct Tag or property value without modification, use a Tag Binding or Property Binding instead.
*   The expression must be a single string.
*   The data type of the value returned by the expression should match the data type of the property you are binding to. For example, if you are binding to a `text` property, your expression should return a string. If you are binding to a `value` property that expects a number, ensure your expression returns a number. Use type casting functions like `toInt()`, `toFloat()`, or `toString()` if necessary.
*   Always enclose Tag and Property references in curly braces `{}`.
*   You can perform string concatenation. For example: `"The temperature is " + {path/to/thermostat/temperature} + " degrees."`
*   The `now()` function is useful for creating displays that update regularly, such as a clock (`dateFormat(now(1000), "hh:mm:ss a")`).
*   Refer to the Expression Functions documentation for a full list of available functions and their usage.
*   The binding automatically updates when a dependency changes, so there is no need to configure polling unless you are using a poll-rate-based function like `now()`.

# Schema - raw
{"type":"object","properties":{"expression":{"type":"string","description":"The source of the expression to execute for this binding."}},"required":["expression"],"additionalProperties":false}