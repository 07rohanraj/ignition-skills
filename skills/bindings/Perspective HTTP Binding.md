# Perspective HTTP Binding

## Description

This document details the configuration and usage of the Perspective HTTP Binding for interacting with web servers and APIs. It explains how to construct and send HTTP requests by defining parameters like the URL, method, headers, and authentication. The instructions also cover how to manage the binding's execution through polling settings and leverage its ability to automatically parse JSON responses to populate component properties.

## Documentation

# Instructions
This document provides instructions for an LLM on how to configure and use the Perspective HTTP Binding in Ignition.

### Object Name
Perspective HTTP Binding

### Instructions

The HTTP Binding is used to interact with web servers and APIs. Its primary function is to make HTTP requests (like GET, POST, etc.) to a specified URL and use the response to populate the bound property. It is exceptionally useful for fetching JSON data from an endpoint, as the binding can automatically create a property structure that mirrors the received JSON document.

#### Configuration Properties:

The binding is configured through a single JSON object with the following properties:

**`request` (Object):** This contains all the details for the HTTP request itself.

*   **`url` (String, Required):** An expression that evaluates to the target URL for the request. If you are using a static URL, it must be enclosed in quotation marks (e.g., `"https://api.example.com/data"`). You can also build dynamic URLs by referencing other properties, for example: `"/api/data/" + {view.params.id}`.
*   **`method` (String, Required, Default: "GET"):** The HTTP method to be used for the request. Common methods include:
    *   **GET:** Retrieves information from the URL. This is the default method.
    *   **POST:** Sends data to the URL to create a new resource. Often used with a `body`.
    *   **PUT:** Sends data to the URL to update or replace an existing resource. Often used with a `body`.
    *   **DELETE:** Requests the deletion of the resource at the URL.
    *   **HEAD:** Same as GET, but the server does not return a message body in the response.
    *   Other available methods include `PATCH`, `OPTIONS`, `TRACE`, and `CONNECT`.
*   **`header` (Array of Objects):** Allows you to pass key/value pairs in the header of the HTTP request. Each object in the array represents one header and has the following structure:
    *   **`key` (String):** The header key (e.g., "Content-Type", "Accept").
    *   **`value` (String):** An expression that evaluates to the header's value.
*   **`body` (Any):** The body of the HTTP request.
    *   This property should be **removed** for methods that do not expect a body (e.g., GET, HEAD).
    *   If the value is a string, it is treated as an expression that evaluates to the body's content.
    *   If the value is any other valid JSON type (null, boolean, number, array, or object), it will be converted to a JSON string and sent as the body. This is typically paired with a "Content-Type" header of "application/json".
*   **`auth` (Object):** Defines the authentication for the request. This is a more convenient alternative to manually adding an `Authorization` header.
    *   **`type` (String, Default: "none"):** The authentication type. Options are `none`, `basic`, `bearer`, or `digest`.
    *   **`value` (String):** An expression that evaluates to the credential or token. For example, for "Basic" auth, if the final header should be `Authorization: Basic aWduaXRpb246cGFzc3dvcmQ=`, the `type` should be `"basic"` and the `value` should be an expression that results in the string `"aWduaXRpb246cGFzc3dvcmQ="`.

**`polling` (Object):** Controls how often the binding executes.

*   **`enabled` (Boolean, Default: `false`):**
    *   If `true`, the HTTP request will poll, meaning it will execute repeatedly at a specified interval.
    *   If `false`, the request will only run once when the component first loads, and then again only if any properties used in expression fields (like `url` or `header.value`) change.
*   **`rate` (Number or String, Default: 5):** The polling frequency.
    *   If numeric, it is interpreted as the number of seconds between executions.
    *   If a string, it is interpreted as an expression that must evaluate to the poll rate in seconds.
    *   If the rate is zero or negative, polling is disabled.

**`enableCookies` (Boolean, Default: `true`):** If `true`, the binding will automatically handle cookies. It will read `Set-Cookie` headers from the server's response and send them back in a `Cookie` header on subsequent requests to that domain. Cookies are stored for the life of the component instance.

**`connectTimeout` (Integer, Default: 30000):** The time in milliseconds to wait for a connection to be established with the server. A value of 0 means an infinite timeout.

**`socketTimeout` (Integer, Default: 30000):** The time in milliseconds to wait for data to be received after a connection has been established (i.e., the maximum time between consecutive data packets). A value of 0 means an infinite timeout.

### Helpful Tips

*   **JSON Integration:** The biggest advantage of the HTTP Binding is its ability to handle JSON responses. If an API returns a JSON object or array, the binding will automatically parse it and create a corresponding structure in the property tree. This allows you to directly bind component properties to fields in the JSON response (e.g., `prop.data.results[0].name`).
*   **Expressions are Key:** Many fields (`url`, `header.value`, `body`, `auth.value`, `polling.rate`) are expressions. This allows you to make your bindings dynamic by referencing other properties on the View, such as `view.params`, `session.props`, or other component properties.
*   **Body with No Body:** Remember to completely remove the `body` property from the `request` object if you are using a method like `GET` or `DELETE` that does not have a request body.
*   **Authentication:** Using the `auth` object is the recommended way to handle authentication. It simplifies the process compared to manually constructing an `Authorization` header.
*   **Polling vs. On-Change:** Use polling (`polling.enabled: true`) when you need to refresh data from an endpoint at a regular interval. Use on-change execution (`polling.enabled: false`) when the request only needs to be made once at startup or when a parameter it depends on changes.
*   **Performance with "Cache & Share":** The binding utilizes a shared polling engine for identical requests across all running Perspective sessions. It polls once, caches the result, and delivers it to all consumers. The cache duration matches the poll rate (or 250ms if polling is disabled). This is a powerful optimization that reduces the load on the Gateway and the target endpoint. You can opt-out of this on the component, but it's enabled by default and generally recommended.
*   **Timeouts:** Understanding the two timeout settings is crucial for reliability. `connectTimeout` applies to making the initial connection, while `socketTimeout` applies to waiting for data during the download. Adjust these based on the expected performance of the remote API.

# Schema - raw
{"type":"object","properties":{"request":{"type":"object","description":"The HTTP Request Configuration","properties":{"url":{"type":"string","description":"An expression which evaluates to a URL target for the HTTP Request","default":""},"method":{"type":"string","description":"The HTTP Request Method","suggestions":["GET","DELETE","HEAD","OPTIONS","PATCH","POST","PUT"],"default":"GET"},"header":{"type":"array","description":"An array of HTTP request header key / value pairs.","items":{"type":"object","description":"Static HTTP Request Header Key / Value Pairs","properties":{"key":{"type":"string","description":"The header key.","suggestions":["Accept","Accept-Charset","Accept-Datetime","Accept-Encoding","Accept-Language","Access-Control-Request-Headers","Access-Control-Request-Method","Authorization","Cache-Control","Connection","Content-Length","Content-MD5","Content-Type","Cookie","Date","Forwarded","From","Host","If-Match","If-Modified-Since","If-None-Match","If-Range","If-Unmodified-Since","Max-Forwards","Origin","Pragma","Proxy-Authorization","Range","Referer","TE","User-Agent","Upgrade","Via","Warning"],"default":""},"value":{"type":"string","description":"An expression which evaluates to the header value.","default":""}},"required":["key","value"],"default":{"key":"","value":""},"additionalProperties":false}},"body":{"description":"The body of the HTTP request. This property should be removed for an HTTP request whose method does not expect a body (such as GET). Can be any valid JSON type. Nulls, booleans, numbers, arrays, and objects will be sent as their JSON-stringified values. Strings will be interpreted as an expression which evaluates to the body's value.","default":""},"auth":{"type":"object","description":"The authorization type and value for the request.","properties":{"type":{"type":"string","description":"The type of authorization for the request.","suggestions":["none","basic","bearer","digest"],"default":"none"},"value":{"type":"string","description":"An expression which evaluates to an authorization credential (i.e. a password or token).","default":""}},"required":["type","value"],"default":{"type":"none","value":""},"additionalProperties":false}},"required":["url","method"],"default":{"url":"","method":"GET","header":[],"auth":{"type":"none","value":""}},"additionalProperties":false},"enableCookies":{"type":"boolean","description":"Automatic Cookie handling for reading Set-Cookie: headers from the server and sending them back out in a Cookie: header when appropriate. True (enabled) by default. Cookies are scoped to the life of the component instance.","default":true},"connectTimeout":{"type":"integer","description":"Determines the timeout in milliseconds until a connection is established. A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default).","default":30000},"socketTimeout":{"type":"integer","description":"Defines the socket timeout (SO_TIMEOUT) in milliseconds, which is the timeout for waiting for data or, put differently, a maximum period inactivity between two consecutive data packets). A timeout value of zero is interpreted as an infinite timeout. A negative value is interpreted as undefined (system default).","default":30000},"polling":{"type":"object","properties":{"enabled":{"type":"boolean","description":"If true, the HTTP request will poll: that is, execute repeatedly at an interval. If false, the HTTP request will only run once on startup and again as parameter values change.","default":false},"rate":{"type":["number","string"],"description":"The rate at which the query will be executed. If numeric, this rate will be interpreted as the number of seconds between executions. If a string, the string will be interpreted as an expression whose result will be the poll rate. If the rate is not positive, polling will be disabled.","default":5}},"default":{"enabled":false,"rate":5},"additionalProperties":false}},"required":["request"],"default":{"request":{"url":"","method":"GET","header":[],"auth":{"type":"none","value":""}},"polling":{"enabled":false,"rate":5}},"additionalProperties":false}