# Perspective Property Binding

## Description

This document describes the usage and configuration of a Perspective Property Binding to dynamically link component properties within the same View. These instructions explain how to create both one-way and bidirectional (two-way) data bindings between components, covering the necessary parameters and the critical limitations of this mechanism.

## Documentation

# Instructions
### Instructions for LLM on: Perspective Property Binding

#### Object Description
A Perspective Property Binding is a fundamental mechanism used to link a property of one component to a property of another component *within the same View*. This creates a dynamic relationship where the target property (the one with the binding) automatically updates whenever the source property (the one specified in the path) changes. It is the simplest type of binding in Perspective.

---

#### Parameter Breakdown

1.  **`path` (string, required)**
    *   **Purpose:** This parameter specifies the full path to the source property that will drive the binding. The value of the property at this path will be pushed to the property that holds this binding.
    *   **Syntax:** The path typically follows a relative structure from the location of the binding. It often includes references to parent containers (`../`), the component's name, the property group (`props`), and the specific property name.
    *   **Example:** To bind a Label's `text` property to a Slider's `value` property, where both components are siblings in the same container, the path on the Label's binding would be `../Slider.props.value`.

2.  **`bidirectional` (boolean, optional)**
    *   **Purpose:** When set to `true`, this parameter creates a two-way binding. Not only will the target property update when the source changes, but any change to the target property will also be written back to the source property at the specified `path`.
    *   **Default:** `false` (the binding is one-way).
    *   **Use Case:** This is useful for synchronizing the state of two input components. For example, if two text fields should always display the same value, you can bind one to the other bidirectionally. Typing in either field will update the other.

---

### Instructions for Use

1.  **Identify Target and Source:** Determine which property you want to control (the target) and which property will control it (the source). Both components must exist within the same View.

2.  **Standard One-Way Binding:**
    *   To make a target property reflect the value of a source property, create a binding on the target property.
    *   Set the `path` to the location of the source property.
    *   Leave `bidirectional` as `false` or omit it.
    *   **Example:** You have a Cylindrical Tank and a Slider. To make the tank's `value` reflect the slider's `value`, you would apply the following binding to the `CylindricalTank.props.value` property:
        ```json
        {
          "path": "../Slider.props.value"
        }
        ```

3.  **Two-Way (Bidirectional) Binding:**
    *   To synchronize two properties so they always have the same value, create a binding on one of them.
    *   Set the `path` to the other property.
    *   Set `bidirectional` to `true`.
    *   **Example:** You have two Text Field components (`TextField1` and `TextField2`). To ensure that editing the text in one immediately updates the other, apply the following binding to the `TextField1.props.text` property:
        ```json
        {
          "path": "../TextField2.props.text",
          "bidirectional": true
        }
        ```

---

### Helpful Tips & Critical Gotchas

*   **Same-View Limitation:** A Property Binding can **ONLY** link properties of components that are within the same View. You **cannot** create a direct property binding to a component in a different View, or to a component inside an Embedded View.
*   **Communicating Across Views:** The *only* way to pass property values between different Views is by using an **Embedded View** component and **View Parameters**.
    *   You can create a custom parameter (e.g., `myValue`) on the View you intend to embed.
    *   Inside that View, you can use a Property Binding to link a component's property to that View Parameter (e.g., bind `Slider.props.value` to `view.params.myValue` bidirectionally).
    *   In the parent View, you can then bind a property or tag to the `props.params.myValue` property of the Embedded View instance.
*   **Property Path Syntax:** The `path` string is crucial. It uses a relative pathing system. `../` typically moves up one level in the component hierarchy. Refer to the component tree in the Designer to determine the correct relative path from your target property to your source property.
*   **Bidirectional Loops:** Be cautious when creating complex bidirectional bindings. While powerful, it's possible to create a setup where two components are constantly updating each other, which could lead to performance issues, though this is rare.
*   **Global Values:** If you need a value to be shared across many different Views or even across different user sessions, a Property Binding is the wrong tool. For this "global state" requirement, you should use a **Tag Binding**, typically to a Memory Tag. This forces all sessions to see the same value and can be made bidirectional to allow components to write back to the global tag.

# Schema - raw
{"type":"object","properties":{"path":{"type":"string","description":"Path to the property that drives this binding.","default":""},"bidirectional":{"type":"boolean","default":false}},"required":["path"],"additionalProperties":false}