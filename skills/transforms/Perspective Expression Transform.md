# Perspective Expression Transform

## Description

This document describes how to use a Perspective Expression Transform to manipulate a value from an existing property binding. It explains how to apply the Ignition Expression language to the incoming value, referenced as `{value}`, in order to perform calculations, reformat data, or execute conditional logic. This transform acts upon a value provided by another binding, distinguishing it from an Expression Binding which originates a value.

## Documentation

# Instructions
### Instructions for Perspective Expression Transform

An Expression Transform is used to manipulate the value of a binding by applying an Ignition Expression. It takes the incoming value from the binding, allows you to operate on it using the expression language, and then outputs the result.

**Core Concept**

The primary purpose of an Expression Transform is to modify or act upon the value provided by the binding it is attached to. The incoming value from the binding is accessible within the expression using the special keyword `{value}`. The transform will return the result of the evaluated expression.

**Configuration**

The Expression Transform has a single property:

*   **`expression`**: A string containing the Ignition Expression code to be executed.

**Functionality**

The expression you provide can leverage the full power of the Ignition Expression Language:

1.  **Accessing the Incoming Value**: To use the value from the binding, you must enclose the word `value` in curly braces, like this: `{value}`.
2.  **Operators**: You can use mathematical (`+`, `-`, `*`, `/`), logical (`&&`, `||`, `!`), and bitwise operators to manipulate the `{value}`.
3.  **Functions**: A large library of built-in expression functions is available. For example, you can use `toHex()` to convert a number to a hexadecimal string, `concat()` to join strings, or `len()` to find the length of a string.
4.  **Referencing Other Data**: The expression is not limited to just the `{value}`. You can also browse and include other data sources:
    *   **Tags**: Reference other Tags in the system.
    *   **Properties**: Reference other component properties within the same View or Session properties.

**Example**

Here is an example of an expression that converts an incoming integer value into a zero-padded 4-character hexadecimal string:

```
//Convert an integer to a Hexadecimal and put in leading 0's
switch(
    len(toHex({value})),            // determine length of string
    0,1,2,3,                        // possible lengths
    'n/a',                          // 0 - results to display
    concat('000', toHex({value})),  // 1 - results to display
    concat('00', toHex({value})),   // 2 - results to display
    concat('0', toHex({value})) ,   // 3 - results to display
    toHex({value})                  // Failover if length is 4 or more
)
```

In this example:
*   `{value}` is the integer coming from the binding.
*   `toHex({value})` converts the integer to a hex string.
*   `len()` checks the length of the resulting string.
*   `switch()` and `concat()` are used to apply the correct padding.

### Helpful Tips

*   **Always use `{value}`** to refer to the output of the binding that the transform is attached to. This is the input for your expression.
*   An Expression Transform is particularly useful when you have a simple binding to a source (like a Tag or another property) and need to apply logic or a calculation to it without creating a full, potentially complex, Expression Binding.
*   Transforms can be chained together. The output of one transform becomes the `{value}` for the next transform in the chain. They are executed in order from top to bottom. For example, you could have a Map Transform that outputs a number, and then an Expression Transform that performs a calculation on that number.
*   The Expression Transform is a distinct feature from an Expression Binding. An Expression *Binding* is the source of the value. An Expression *Transform* modifies a value that comes from another binding type (e.g., Tag Binding, Property Binding, Query Binding).

# Schema - raw
{"type":"object","properties":{"expression":{"type":"string","description":"The expression source code."}},"required":["expression"],"additionalProperties":false}