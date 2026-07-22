# Perspective Expression Structure Binding

## Description

The Perspective Expression Structure Binding constructs a single object by evaluating a collection of individual expressions. Each key in the resulting object is paired with its own unique expression, enabling the dynamic creation of complex data structures or the configuration of multiple parameters from various sources within a single, organized binding.

## Documentation

# Instructions
# Perspective Expression Structure Binding

An Expression Structure Binding is a binding type that produces an object as its output. Unlike a standard Expression Binding which evaluates a single expression to return a single value, the Expression Structure Binding allows you to construct an object where each key's value is determined by its own independent expression.

This is particularly useful for two main scenarios:
1.  **Creating Complex Objects**: When a component property expects an object with a specific structure, this binding can be used to build that object piece by piece, with each piece coming from a different expression.
2.  **Configuring Parameters**: It's an ideal way to gather and structure multiple values to be passed as parameters into a [Script Transform](https://docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/transforms/) or to a View's `params` property.

The binding will construct an object based on the configuration provided in the `struct` property.

### Properties

| Property    | Type    | Description                                                                                                                                                                                                                         |
| :---------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `struct`    | Object  | The main configuration object. The keys of this object become the keys of the output object. The value for each key must be a string that will be evaluated as an Ignition expression.                                                 |
| `waitOnAll` | Boolean | If `true` (the default), the binding will not return a value until every expression inside the `struct` has successfully evaluated and returned a value. If `false`, each key-value pair in the output object will update individually as its corresponding expression resolves. |

### Helpful Tips

*   The output of this binding is always a single object. The structure of this output object is defined by the `struct` parameter.
*   Each value within the `struct` object is an independent expression. For example, one value can be a static string, another can be a reference to a Tag, and a third can be a mathematical calculation.
*   The keys you define in the `struct` object must match the names expected by the property you are binding to. For example, if you are binding to a View's `params` property to pass parameters named `iconPath` and `labelText`, your `struct` object must contain keys named `iconPath` and `labelText`.
*   The `waitOnAll` property is `true` by default. This is generally the desired behavior as it ensures that the target property receives a complete, fully-formed object all at once, preventing visual inconsistencies where parts of a component update at different times.
*   This binding type is powerful when used to configure the parameters for a child view within a component like the Carousel or Embedded View. You can build the entire `viewParams` object in a single binding.
*   When debugging, if the binding is not producing the expected output, verify each individual expression within the `struct` object for errors. An error in one expression can prevent the entire binding from updating, especially when `waitOnAll` is set to `true`.

# Schema - raw
{"type":"object","properties":{"struct":{"type":"object","description":"The structure whose string values (or children's string values) will be interpreted as expression sources"},"waitOnAll":{"type":"boolean","description":"If set to true, the binding will not emit a value until all expressions in the structure have emitted at least one value. This value is true by default."}},"required":["struct"],"default":{"struct":{},"waitOnAll":true},"additionalProperties":false}