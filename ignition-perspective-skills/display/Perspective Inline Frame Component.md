# Perspective Inline Frame Component

## Description

This document details the usage and configuration of the Perspective Inline Frame component, which embeds external webpages into an Ignition View. It covers the essential properties for setting the source URL, controlling the referrer policy for security, enabling full-screen mode, and applying basic styles to the component's frame.

## Documentation

# Instructions
This document provides instructions for an LLM on how to use and configure the **Perspective Inline Frame** component in Ignition.

### Object Name
Perspective Inline Frame Component

### Object ID
`ia.display.iframe`

---

### Instructions for Use

The Perspective Inline Frame component is used to embed an external webpage directly into a Perspective View. It functions by creating an HTML `<iframe>` element.

To configure the component, you will primarily modify its properties. The configuration is specified as a JSON object.

**1. Specifying the Webpage Source:**

The most critical property is `src`. This property determines which webpage is loaded into the frame.

*   **`src` (string):** Set this property to the full URL of the webpage you wish to embed.
    *   **Example:** To embed the main Ignition documentation page, you would set the `src` property like this:
        ```json
        {
          "type": "ia.display.iframe",
          "props": {
            "src": "https://docs.inductiveautomation.com/display/DOC81"
          }
        }
        ```
*   If the `src` property is left as its default value, an empty string (`""`), the component will render as a blank frame.

**2. Controlling Referrer Information:**

The `referrerPolicy` property controls how much information about the referring page (your Ignition Perspective View) is sent to the server of the embedded webpage. This is an important security and privacy feature.

*   **`referrerPolicy` (string):** This property must be one of the following values:
    *   `"no-referrer"`: (Default) No referrer information is sent.
    *   `"no-referrer-when-downgrade"`: The full URL of the referring page is sent, but only for requests from a secure (HTTPS) origin to another secure origin.
    *   `"origin"`: Only the origin (protocol, host, and port) of the referring page is sent.
    *   `"origin-when-cross-origin"`: The full URL is sent for same-origin requests, but only the origin is sent for cross-origin requests.
    *   `"unsafe-url"`: The full URL is sent with all requests, regardless of security. This can be a security risk.

    *   **Example:** To set the policy to only send the origin:
        ```json
        {
          "type": "ia.display.iframe",
          "props": {
            "src": "https://example.com",
            "referrerPolicy": "origin"
          }
        }
        ```

**3. Enabling Full-Screen Mode:**

Some embedded content, like video players, may have a full-screen feature. You can enable this functionality using the `allowFullScreen` property.

*   **`allowFullScreen` (boolean):** Set this to `true` to allow the content within the iframe to enter full-screen mode. The default is `false`.

    *   **Example:** To enable full-screen for an embedded video:
        ```json
        {
          "type": "ia.display.iframe",
          "props": {
            "src": "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "allowFullScreen": true
          }
        }
        ```

**4. Styling the Frame:**

The frame of the component itself can be styled using the `style` property. This allows you to control aspects like borders and apply CSS classes defined in your project.

*   **`style` (object):** An object containing style properties. You can modify the border, apply classes, and more.

    *   **Example:** To add a 2-pixel solid black border to the iframe:
        ```json
        {
          "type": "ia.display.iframe",
          "props": {
            "src": "https://example.com",
            "style": {
              "border": "2px solid black"
            }
          }
        }
        ```

---

### Helpful Tips

*   **Content May Be Blocked:** Be aware that many websites explicitly prevent themselves from being embedded in iframes. They do this as a security measure using HTTP headers like `X-Frame-Options` or `Content-Security-Policy`. If you set the `src` URL and the frame remains blank or shows an error, it is very likely that the target website is blocking the connection. This is controlled by the external website and cannot be overridden from within Ignition.
*   **Security First:** The `referrerPolicy` is a security feature. The default value of `"no-referrer"` is the most private. Only change this setting if the embedded content requires referrer information to function correctly. Using `"unsafe-url"` can leak potentially sensitive information from your Perspective session's URL to an external site.
*   **Blank by Default:** A new Inline Frame component will be blank because its `src` property is initially an empty string. You must provide a URL for any content to appear.
*   **No Internal Styling:** You can style the iframe element itself (the "box" or "frame"), but you cannot apply styles to the content *inside* the iframe. The styling of the embedded webpage is controlled entirely by that page's own CSS.
*   **No Scripting Interaction:** For security reasons, scripts running in your Perspective View cannot directly interact with the content or scripts of the page inside the Inline Frame, and vice-versa, especially when the content is from a different origin.

# Schema - raw
{"schema":{"type":"object","properties":{"referrerPolicy":{"type":"string","enum":["no-referrer","no-referrer-when-downgrade","origin","origin-when-cross-origin","unsafe-url"],"default":"no-referrer"},"src":{"description":"The source URL of the webpage to embed.","type":"string","default":""},"allowFullScreen":{"type":"boolean","default":false},"style":{"default":{"border":"unset","classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"IFrame","name":"Inline Frame","palette":{"description":"A component that uses the <iframe> tag to embed another webpage.","variants":[{"tooltip":"A component that uses the <iframe> tag to embed another webpage.","label":"Inline Frame"}],"category":"display"},"id":"ia.display.iframe"}