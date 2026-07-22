# Perspective Tag Binding

## Description

The usage and configuration of the Perspective Tag Binding, which links component properties to Ignition tags for live data updates. These instructions detail the binding's JSON structure, including its various modes for direct, indirect, and expression-based tag paths, as well as the option for bidirectional data flow.

## Documentation

# Instructions
Here are the instructions and tips for using the Perspective Tag Binding in Ignition.

### Object Name
Perspective Tag Binding

### Instructions for Use

A Perspective Tag Binding is used to link a component property to a tag in the Ignition Tag system. This creates a live subscription, where any changes to the tag's value are automatically pushed to the component's property.

You must configure the binding using a JSON object with the following properties:

**`tagPath` (string):** This is a required property that specifies the path to the tag. The interpretation of this path depends on the selected `mode`.
*   If you are binding to a specific property of a tag (e.g., its quality or timestamp), you must include it in the path (e.g., `[default]MyTag.Quality`).
*   If you only provide the path to the tag itself (e.g., `[default]MyTag`), the binding will default to the tag's `Value` property.

**`mode` (string):** This property determines how the binding operates. It can be one of three values:
1.  **`direct` (Default):** This is the simplest mode. The `tagPath` is a static, complete string path to a single tag.
2.  **`indirect`:** This mode allows you to build a `tagPath` dynamically. The `tagPath` string contains one or more placeholders enclosed in braces, such as `{1}` or `{motor_number}`. You must then provide a `references` object to resolve these placeholders.
3.  **`expression`:** In this mode, the `tagPath` property contains an Ignition expression that must evaluate to a string. This resulting string is then used as the full path to the tag. This allows for complex conditional logic to determine which tag to bind to.

**`bidirectional` (boolean):**
*   If `false` (the default), the binding is read-only. Changes to the tag update the property, but changes to the property do not affect the tag.
*   If `true`, the binding becomes read/write. Any change to the bound property's value will be written back to the tag, provided the tag has the necessary security permissions to allow writes.

**`references` (object):**
*   This property is **only used when the `mode` is `indirect`**.ZIt is ignored in `direct` and `expression` modes.
*   It is a dictionary (JSON object) where each key corresponds to a placeholder in the `tagPath` string (without the braces), and the value is a binding to another property or parameter that will supply the dynamic part of the path.
*   For example, if `tagPath` is `"[default]Motors/Motor {num}/Amps"`, the `references` object should look like `{"num": <binding_to_property_with_motor_number>}`.

#### Mode-Specific Examples:

*   **Direct Mode Example:**
    To bind directly to the value of a tag named `Tank_1_Level`, you would use:
    ```json
    {
        "mode": "direct",
        "tagPath": "[default]Tanks/Tank_1_Level"
    }
    ```

*   **Indirect Mode Example:**
    To create a binding that can point to the `Amps` tag of different motors based on a Dropdown component's selected value, you could use:
    ```json
    {
        "mode": "indirect",
        "tagPath": "[default]Motors/Motor {1}/Amps",
        "references": {
            "1": {
                "type": "property",
                "path": "props.parent.getChild('Dropdown').props.value"
            }
        },
        "bidirectional": false
    }
    ```
    In this case, the placeholder `{1}` in the `tagPath` is resolved by the value of the 'Dropdown' component.

*   **Expression Mode Example:**
    To switch between 'Tag A' and 'Tag B' based on a view parameter named `tagToShow`, you would use:
    ```json
    {
        "mode": "expression",
        "tagPath": "if({view.params.tagToShow} = 'Tag A', '[default]Z_Other_Tags/Tag A', '[default]Z_Other_Tags/Tag B')",
        "bidirectional": true
    }
    ```
    Here, the entire `tagPath` field is an expression that returns one of two complete tag path strings.

### Helpful Tips

*   **`bidirectional` requires Tag Security:** For a `bidirectional` binding to successfully write a value back to a tag, the tag itself must be configured with security settings that permit write operations from the session.
*   **`indirect` vs. `expression` Mode:**
    *   Use **`indirect`** mode when you are swapping out known pieces of a structured tag path (e.g., an equipment number or area name). It is simpler for dynamic path segments.
    *   Use **`expression`** mode when you need complex logic or need to choose between fundamentally different tag path structures, not just swapping a segment.
*   **Don't Confuse Tag Expression with Expression Binding:** A "Tag Binding" in `expression` mode is different from a standard "Expression Binding". The Tag Expression *must* resolve to a string that is a valid tag path. A regular Expression Binding can perform calculations, run functions, and combine multiple values.
*   **Default Tag Property:** If your `tagPath` does not specify a property (like `.Value` or `.Quality`), the binding will automatically default to the tag's `.Value` property.
*   **`references` for Indirect Mode:** The `references` object is crucial for `indirect` mode. The keys in this object must exactly match the names of the placeholders in your `tagPath` (e.g., for `{motorNum}`, the key is `"motorNum"`). The values for these keys must be bindings to other properties that will provide the substitution values.
*   **Automatic Binding with `dropConfig`:** Be aware that Tag Bindings can be created automatically in the Designer. A View can have a `dropConfig` property that associates it with a specific UDT (User Defined Type) or a tag data type. When a matching tag is dragged onto another View, an instance of the configured View is created, and the `dropConfig`'s `action` property may automatically create a Tag Binding to one of its View Parameters.
*   **Handling Initial Values:** A binding may initially receive a `null` value with an "Uncertain" quality as the view loads. To prevent a component overlay from briefly appearing, you can configure the binding to "Publish Initial Uncertain Value" (this setting is in the UI, not the schema).
*   **Quality Overlays:** Components can visually indicate a bad tag quality (e.g., disconnected, error) with an overlay. This behavior can be disabled for a specific binding by enabling "Overlay Opt-Out" in the binding configuration UI.

# Schema - raw
{"type":"object","properties":{"tagPath":{"type":"string","description":"The tag path","default":""},"mode":{"type":"string","description":"The mode in which the tag binding will operate. Three modes: Direct, Indirect, and Expression. See documentation for details.","enum":["direct","indirect","expression"],"default":"direct"},"bidirectional":{"type":"boolean","description":"Whether or not changes to the bound property should write back to the tag.","default":false},"references":{"type":"object","description":"The references map for indirect mode. Ignored if the mode is not set to Indirect.","default":{},"additionalProperties":true}},"required":["tagPath"],"default":{"tagPath":"","mode":"direct","bidirectional":false},"additionalProperties":false}