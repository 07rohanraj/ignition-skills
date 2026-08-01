# Perspective Markdown Component

## Description

These instructions detail the usage and configuration of the Ignition Perspective Markdown component, a tool for displaying text formatted with Markdown and HTML. The document outlines its core properties and the settings for its rendering engine, enabling users to control how content is parsed and displayed. This includes managing security options for raw HTML, customizing spacing, and selectively allowing or disallowing specific formatting elements such as headings, lists, and tables.

## Documentation

# Instructions
### Perspective Markdown Component Instructions

This document provides detailed instructions for interacting with and configuring the **Perspective Markdown Component** in Ignition.

#### Object Description
The Markdown component is a display tool in Perspective used to render text formatted with Markdown, a lightweight and easy-to-read markup language. It is designed to take plain text with simple formatting cues (like `*italic*` or `# Heading`) and display it as styled HTML. The component also supports rendering raw HTML for more complex styling, providing a flexible way to display formatted text content.

---

### Core Properties

#### `source`
-   **Type:** `String`
-   **Description:** This is the primary property of the component. It holds the string of text to be rendered. The text should be formatted using Markdown syntax. It can also contain HTML code, which will be rendered if configured correctly.
-   **Example:**
    ```markdown
    # Main Title

    This is a paragraph with some _italic_ and **bold** text.

    - List Item 1
    - List Item 2
    ```

#### `sectionSpacing`
-   **Type:** `Number`
-   **Description:** Defines the amount of vertical space, in pixels, between distinct sections of the rendered markdown, such as between a heading and a paragraph, or between two paragraphs.
-   **Default Value:** `24`

#### `style`
-   **Type:** `Object`
-   **Description:** This property allows for standard CSS styling of the component's container, such as setting the background color, border, padding, and margins. Note that this styles the component as a whole and does not affect the styling of the individual markdown elements within. To style the rendered content itself (e.g., text color), you should use HTML within the `source` property.

---

### Markdown Rendering Engine (`props.markdown`)

This object contains a set of properties that control how the string in the `props.source` property is parsed and rendered.

#### `escapeHtml`
-   **Type:** `Boolean`
-   **Description:** This is a critical security feature. By default, it is `true`, which causes any HTML found in the `source` property to be treated as plain text (e.g., `<b>` appears as the literal text `<b>` instead of making text bold). When set to `false`, the component will render the HTML.
-   **Default Value:** `true`
-   **CRITICAL NOTE:** Setting this property to `false` can create a security vulnerability if the text in the `source` property is supplied by a user. Malicious code could be injected. Only set to `false` when the source content is trusted and controlled.

#### `skipHtml`
-   **Type:** `Boolean`
-   **Description:** When set to `true`, the component will completely ignore and skip all inline and block-level HTML found in the `source` property.
-   **Default Value:** `false`

#### `disallowedTypes`
-   **Type:** `Array` of `String`
-   **Description:** Provides a "blacklist" of Markdown node types to prevent from rendering. Any node type included in this array will be ignored. This is useful for restricting the formatting options available.
-   **Default Value:** `[]` (empty array)
-   **Available Types:** `root`, `text`, `break`, `paragraph`, `emphasis`, `strong`, `thematicBreak`, `blockquote`, `delete`, `link`, `image`, `linkReference`, `imageReference`, `table`, `tableHead`, `tableBody`, `tableRow`, `tableCell`, `list`, `listItem`, `definition`, `heading`, `inlineCode`, `code`, `html`.

#### `allowedTypes`
-   **Type:** `Array` of `String`
-   **Description:** Provides a "whitelist" of Markdown node types to allow for rendering. Only node types included in this array will be rendered. All others will be ignored.
-   **Default Value:** An array containing all available types.

#### `unwrapDisallowed`
-   **Type:** `Boolean`
-   **Description:** This property modifies the behavior of `disallowedTypes`. When `false` (the default), if a node type is disallowed, both the node and its content are removed. When `true`, the disallowed node's container is removed, but its content (child nodes/text) is preserved and rendered.
-   **Default Value:** `false`
-   **Example:** Given the source `Some **bold** text.` and `disallowedTypes: ["strong"]`:
    -   If `unwrapDisallowed` is `false`, the output is "Some text.".
    -   If `unwrapDisallowed` is `true`, the output is "Some bold text.".

#### `sourcePos`
-   **Type:** `Boolean`
-   **Description:** A debugging tool. If set to `true`, the component will keep track of and log the source position of rendered elements.
-   **Default Value:** `false`

---

### Helpful Tips

1.  **Enabling HTML:** To use any HTML for formatting (like `<br>` for line breaks, `<b>` for bold, or `<p style="...">` for styling), you **must** set `props.markdown.escapeHtml` to `false`.

2.  **Security First:** Always be cautious when setting `props.markdown.escapeHtml` to `false`. If the content of the `source` property can be influenced by users, you risk cross-site scripting (XSS) attacks.

3.  **Adding Line Breaks:**
    *   **HTML Method:** The most reliable way to force a line break is to set `props.markdown.escapeHtml: false` and use the `<br>` tag in your `source` text.
    *   **Markdown List Method:** Within a list, you can create a line break within a single list item by ending the line with two spaces. For example, `* Item 1 line 1  \n  Item 1 line 2` will render the text on two lines within the same bullet point.

4.  **Applying Custom Colors:** To change the color or other styles of the text itself, use inline HTML styles within the `source` property. You must set `props.markdown.escapeHtml` to `false`.
    *   **Example:** To make a paragraph purple and bold:
        *   `props.source`: `<p style="color:#AC00AC;"><b>Adding Color to your Text</b></p>`
        *   `props.markdown.escapeHtml`: `false`

5.  **Controlling Allowed Formatting:** Use the `disallowedTypes` array to restrict formatting. For example, to prevent users from creating tables or inserting images, set `props.markdown.disallowedTypes` to `["table", "image"]`.

6.  **Preserving Text from Disallowed Elements:** If you want to strip formatting but keep the text, use `unwrapDisallowed: true`. For example, if you don't want to allow headings but also don't want to lose the heading text, add `"heading"` to `disallowedTypes` and set `unwrapDisallowed` to `true`. The heading text will appear as a normal paragraph.

7.  **Forcing Extra Spaces:** Standard markdown collapses multiple spaces. To force the inclusion of non-breaking spaces, set `escapeHtml: false` and use the HTML entity `&nbsp;`.

# Schema - raw
{"schema":{"type":"object","properties":{"sectionSpacing":{"description":"Number of pixels of vertical space between each section or header","type":"number","default":24},"source":{"description":"Text annotated with markdown syntax to display.","type":"string","example":"Welcome to _Markdown_"},"markdown":{"type":"object","title":"Markdown rendering properties","required":["sourcePos","escapeHtml","skipHtml","disallowedTypes","unwrapDisallowed"],"default":{"disallowedTypes":[],"skipHtml":false,"escapeHtml":true,"renderers":{},"unwrapDisallowed":false,"sourcePos":false},"allowAdditionalProperties":false,"properties":{"allowedTypes":{"description":"Defines which types of nodes should be allowed (rendered).","type":"array","default":["root","text","break","paragraph","emphasis","strong","thematicBreak","blockquote","delete","link","image","linkReference","imageReference","table","tableHead","tableBody","tableRow","tableCell","list","listItem","definition","heading","inlineCode","code","html"],"items":{"type":"string","enum":["root","text","break","paragraph","emphasis","strong","thematicBreak","blockquote","delete","link","image","linkReference","imageReference","table","tableHead","tableBody","tableRow","tableCell","list","listItem","definition","heading","inlineCode","code","html"]}},"disallowedTypes":{"description":"Defines which types of nodes should be disallowed (not rendered).","type":"array","default":[],"items":{"type":"string","enum":["root","text","break","paragraph","emphasis","strong","thematicBreak","blockquote","delete","link","image","linkReference","imageReference","table","tableHead","tableBody","tableRow","tableCell","list","listItem","definition","heading","inlineCode","code","html"]}},"skipHtml":{"description":"Setting to true will skip inlined and blocks of HTML","type":"boolean","default":false},"escapeHtml":{"description":"Setting to false will cause HTML to be rendered. Be aware that setting this to false might cause security issues if the input is user-generated. Use at your own risk.","type":"boolean","default":true},"unwrapDisallowed":{"description":"Setting to true will try to extract/unwrap the children of disallowed nodes. For instance, if disallowing Strong, the default behaviour is to simply skip the text within the strong altogether, while the behaviour some might want is to simply have the text returned without the strong wrapping it.","type":"boolean","default":false},"sourcePos":{"description":"If true, will keep track and log source positioning for debugging purposes.","type":"boolean","default":false}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Markdown","name":"Markdown","palette":{"variants":[{"tooltip":"Enables you to format text with a lightweight formatting language that is easy to write and easy to read.","label":"Markdown"}],"category":"display"},"id":"ia.display.markdown"}