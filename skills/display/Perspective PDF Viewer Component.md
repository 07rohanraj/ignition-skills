# Perspective PDF Viewer Component

## Description

This document describes the configuration and usage of the Perspective PDF Viewer component, detailing its properties for setting a document source and navigating pages, as well as the scripting methods available for implementing custom controls.

## Documentation

# Instructions
# Perspective PDF Viewer Component

## Instructions for Use

The Perspective PDF Viewer component is designed to display a PDF document within a Perspective View. The component renders one page of the specified PDF at a time.

### Configuration and Properties

To use the PDF Viewer, you must configure its properties. The key properties are found in the Property Editor in the Ignition Designer.

1.  **`source`**:
    *   This property defines which PDF to display.
    *   It requires a URL that points to a PDF file. Direct local file paths are not supported.
    *   A recommended method for hosting the PDF is to use the Ignition Web Dev module. You can create a File Resource or a Mounted Folder within the Web Dev module to make your PDF available via a URL. The component's `source` property would then be set to that resource's URL.
    *   **Default Value**: `"/res/perspective/documents/pdf-sample.pdf"`

2.  **`page`**:
    *   This numeric property determines which page of the PDF is currently displayed. It is a 1-based index, meaning the first page is `1`.
    *   You can change this property's value through bindings or scripts to navigate through the document. For example, you can bind this property to a Number Input component to allow users to type in a page number, or use buttons with scripts to increment or decrement the page number.

3.  **`showPageNumber`**:
    *   This is a boolean property that controls the visibility of a page number display at the bottom of the component.
    *   When set to `true`, the component will show text like "Page X of Y", where X is the current page and Y is the total page count.
    *   When `false`, this information is hidden.
    *   **Default Value**: `false`

4.  **`pageCount`**:
    *   This is a **read-only** numeric property that indicates the total number of pages in the PDF document specified by the `source` property.
    *   This property is useful for building custom navigation logic. For example, you can use it to determine the upper limit for the `page` property, preventing users from trying to navigate to a page that doesn't exist.
    *   **Default Value**: `0`

5.  **`style`**:
    *   This property allows for custom styling of the component using standard CSS-based properties, such as borders, margins, padding, and background color. You can also assign a style class to it.

### Scripting

The PDF Viewer component has a specific scripting function available. Scripts can be configured on component events or other events within the View.

*   **`reload()`**
    *   **Description**: This function forces the component to reload the PDF from its `source` URL. This is useful in scenarios where the PDF file at the source URL might be updated, and you want to display the latest version without requiring the user to refresh the entire page.
    *   **Parameters**: None.
    *   **Returns**: Nothing.
    *   **Example**: `self.getSibling("PDFViewer").reload()`

**Note**: The PDF Viewer component does not have any specific extension functions or component events beyond the standard ones available to most Perspective components.

---

## Helpful Tips

*   **URL Requirement**: It is critical to remember that the `source` property must be a URL. The component cannot render a PDF from a local file system path (e.g., `C:\Users\MyUser\Documents\report.pdf`). The PDF must be hosted on a web server accessible by the client's browser.
*   **Hosting PDFs**: The easiest way to host a PDF for use with this component is by leveraging the **Web Dev module** in Ignition. You can add the PDF as a File Resource, and Ignition will provide a URL to it that you can then paste into the `source` property.
*   **One Page at a Time**: The component is designed to show only a single page at a time. To see other pages, you must change the value of the `page` property.
*   **Custom Navigation**: To create a user-friendly PDF viewing experience, you will likely need to build custom navigation controls.
    *   Use Button components for "Next Page" and "Previous Page" functionality.
    *   The script for a "Next Page" button might look like this (assuming the PDF viewer is named "PDFViewer"):
        ```python
        viewer = self.getSibling("PDFViewer")
        if viewer.props.page < viewer.props.pageCount:
            viewer.props.page += 1
        ```
    *   The script for a "Previous Page" button might look like this:
        ```python
        viewer = self.getSibling("PDFViewer")
        if viewer.props.page > 1:
            viewer.props.page -= 1
        ```
*   **Read-Only Page Count**: You cannot write to the `pageCount` property. It is automatically populated after the PDF from the `source` property is successfully loaded. Use this property in your navigation logic to know the maximum page number.
*   **Dynamic PDF Source**: You can dynamically change the `source` property via a binding or script. If you change the `source` to a new URL, the component will load the new PDF. After the new PDF loads, the `pageCount` property will update accordingly.

# Schema - raw
{"schema":{"description":"A component which displays a PDF document, showing one page at a time.","type":"object","title":"PDF Viewer","properties":{"pageCount":{"description":"Number of pages the pdf contains. Readonly.","title":"Page Count","type":"number","default":0},"showPageNumber":{"description":"Whether to show current page number and total page count at the bottom of the component.","type":"boolean","default":false},"source":{"title":"PDF Source","type":"string","default":"/res/perspective/documents/pdf-sample.pdf"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"page":{"description":"The current page being displayed","title":"Current Page","type":"number","example":1}}},"resources":[{"type":"js","path":"/res/perspective/js/PerspectivePdfViewer.js","name":"perspective-pdf-viewer-js"},{"type":"css","path":"/res/perspective/css/PerspectivePdfViewer.css","name":"perspective-pdf-viewer-css"}],"defaultMetaName":"PDFViewer","name":"PDF Viewer","palette":{"variants":[{"tooltip":"Displays a PDF that's hosted on a web server.","label":"PDF Viewer"}],"category":"display"},"id":"ia.display.pdf-viewer"}