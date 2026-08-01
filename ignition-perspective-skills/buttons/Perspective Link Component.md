# Perspective Link Component

## Description

This document describes the usage and configuration of the Perspective Link component. It details how to create clickable hyperlinks for navigating to both internal project pages and external websites, or for initiating a file download. The instructions also cover key properties for controlling the link's target destination, such as opening in a new tab, and for customizing its visual appearance through styling.

## Documentation

# Instructions
### Perspective Link Component Instructions

#### Objective
The primary function of the Perspective Link component is to create a clickable hyperlink for navigation within a Perspective session or to an external web resource. It can also be configured to initiate a file download.

---

### Instructions

**1. Component Identification:**
*   The component is identified by its `name`, which is "Link". The default name assigned to new instances is also "Link".
*   It is located in the "Navigation" category of the component palette.

**2. Basic Configuration (Navigation):**
To create a simple navigation link, you must configure the `text` and `url` properties.
*   **`text` (string):** This is the visible text that the user will click on. For example, "Go to Homepage".
*   **`url` (string):** This is the destination. It can be one of the following:
    *   **An external URL:** A full web address, e.g., `http://inductiveautomation.com`.
    *   **An internal Page Path:** To link to another View mounted within the project, specify the mount path starting with a `/`. For example, if a View is mounted at `/dashboard`, set the `url` to `"/dashboard"`. The Page URL for a page can be found in the Page Configuration settings of the project.
    *   **A URL Fragment:** A fragment of a URL.

**3. Configuring Link Target:**
The `target` property determines where the linked content will be displayed.
*   **`target` (string):**
    *   `'self'`: (Default) Opens the link in the current tab and context.
    *   `'tab'` or `'blank'`: Opens the link in a new browser tab.
    *   `'parent'`: Opens the link in the parent frame.
    *   `'top'`: Opens the link in the full body of the window.
    *   Other standard W3C anchor link target attributes are also supported.

**4. Configuring for File Download:**
Instead of navigating, the component can be used to download a file when clicked.
*   **`download` (string):** To enable this functionality, provide a string value to this property. The string will be used as the default filename for the downloaded resource. When this property is set, clicking the link will prompt a download instead of navigating.

**5. Styling:**
The visual appearance of the link can be customized.
*   **`style` (object):** This object allows for detailed styling. You can set properties for text, background, margins, padding, borders, and more. You can also assign a pre-configured style class by setting `style.classes`.

**6. Advanced Properties:**
*   **`rel` (string):** Specifies the relationship between the current document and the linked one. Suggestions include: `""`, `alternate`, `author`, `bookmark`, `external`, `help`, `license`, `next`, `nofollow`, `noreferrer`, `noopener`, `prev`, `search`, `tag`.
*   **`referrerPolicy` (string):** Controls which referrer information is sent with the request. Suggestions include: `no-referrer`, `no-referrer-when-downgrade`, `origin`, `origin-when-cross-origin`, `unsafe-url`.

---

### Helpful Tips
*   **Appearance:** By default, Link components are visually distinct from regular text, often with a different color and an underline that appears on hover.
*   **Bindings:** Most properties on the Link component, including `url` and `text`, can be bound to other data sources for dynamic behavior. For more details, see "Types of Bindings in Perspective".
*   **Events:** The Link component supports component events (e.g., `onClick`). These events can be configured to run actions or scripts. The configuration of these events is handled on the component itself in the designer, as described on the "Component Events and Actions" page, and is separate from the properties listed here.
*   **Internal vs. External Links:** Remember to prefix internal page paths with a forward slash (`/`), e.g., `/my-page`. Full URLs for external sites should include the protocol, e.g., `http://` or `https://`.

---

### Examples

**1. Link to an External Website in a New Tab:**
```json
{
  "text": "Visit Inductive Automation",
  "url": "http://inductiveautomation.com",
  "target": "blank"
}
```

**2. Link to an Internal View in the Same Tab:**
```json
{
  "text": "Go to Status Dashboard",
  "url": "/status",
  "target": "self"
}
```

**3. Link that Downloads a File:**
```json
{
  "text": "Download Report",
  "url": "/system/webdev/myProject/data/report.pdf",
  "download": "monthly_report.pdf"
}
```

**4. Styled Link:**
```json
{
  "text": "Critical Alert",
  "url": "/alerts/critical",
  "style": {
    "classes": "alert-style-red"
  }
}
```

# Schema - raw
{"schema":{"description":"A component that provides navigation ability.","type":"object","example":{"url":"http://inductiveautomation.com","target":"self","style":{"classes":""},"text":"Link"},"properties":{"referrerPolicy":{"description":"Indicates which referrer to send when fetching the resource at the given URL","type":"string","suggestions":["no-referrer","no-referrer-when-downgrade","origin","origin-when-cross-origin","unsafe-url"]},"url":{"description":"A a URL, URL fragment, or Page that the hyperlink points to. destination, resource, or mount path to navigate to.  If the target is another mounted view, simply specify the mount path, starting with a '/' character.  For instance, if a view is mounted at data/perspective/client/MyProjectName/status, setting the target to '/status' will properly navigate to the status mount when clicked.","type":"string","example":"http://inductiveautomation.com","default":""},"target":{"description":"Specifies where to display the linked URL.  Common values such as 'self' for the current tab/context, 'tab' or 'blank' for a new tab, 'parent' for the parent frame tab/context, or 'top' for the full body of the window.  Otherwise supports standard w3c values for anchor link target attributes.","type":"string","suggestions":["self","tab","blank","parent","top"]},"download":{"description":"Specifies the target filename that will be downloaded when a user clicks on the hyperlink","type":"string"},"rel":{"description":"Specifies the relationship between the current document and the document linked by this component.","type":"string","suggestions":["","alternate","author","bookmark","external","help","license","next","nofollow","noreferrer","noopener","prev","search","tag"]},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"text":{"description":"Text to display in the link","type":"string","example":"link","default":""}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Link","name":"Link","palette":{"variants":[{"tooltip":"Provides a hyperlink that points to a destination such as a page, view, resource, or mount path.","label":"Link"}],"category":"navigation"},"id":"ia.navigation.link"}