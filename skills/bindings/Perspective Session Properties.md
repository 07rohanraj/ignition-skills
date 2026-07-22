# Perspective Session Properties

## Description

This reference details the structure, purpose, and configuration of Perspective Session Properties, which provide global access to information about the authenticated user, device capabilities, gateway connection, and other session-specific states for use in data binding and scripting.

## Documentation

# Instructions
### Name: Perspective Session Properties

### Instructions for LLM

Here is a detailed set of instructions on how to interact with and understand Perspective Session Properties.

#### I. Overview

Perspective Session Properties are a collection of properties that hold information about a user's session. These properties are available globally within a Perspective session and can be accessed for binding or scripting. They provide details about the user, their device, the gateway, and session-specific settings. The properties are organized into a hierarchical structure.

#### II. General Property Concepts

These concepts, derived from how properties work in Perspective, apply to the Session Properties:

*   **Data Types**: All property values are encoded as JSON. They are one of the following:
    *   **Value (primitive)**: A single value, which can be a `boolean` (true/false), `number`, `string`, or `null`.
    *   **Object**: A collection of key-value pairs, where values can be any data type. Indicated by `{}`.
    *   **Array**: An ordered list of values. Indicated by `[]`.
    *   **Date**: A special string format (`YYYY-MM-dd HH:mm:ss`) that is treated as a long integer on the backend.
*   **Read-Only Properties**: Many session properties are marked as "Readonly". You cannot write to these properties. They are updated by the system automatically. Attempting to modify them will have no effect.
*   **Property Access**: While most session properties are readable, some might have restrictions that prevent them from being modified from the browser's developer console for security reasons. Writing to protected properties should be done via gateway-side scripts or bidirectional bindings.

---

### III. Session Property Details

The following is a comprehensive breakdown of all available session properties.

#### **Top-Level Properties**

*   `id` (string, Readonly): A unique string identifier for the current session.
*   `host` (string, Readonly): The remote host (IP address) of the application or browser, as detected by the gateway.
*   `theme` (string): The current theme for the session. Defaults to `"light"`. You can write a new theme name to this property to change the session's theme.
*   `locale` (string): The current locale of the session (e.g., `"en-US"`). Defaults to `""`.
*   `timeZoneId` (string): The ID of the current timezone for the session. Defaults to `""`.
*   `lastActivity` (date/null, Readonly): The gateway timestamp of the last user activity in the session.
*   `googleMapsApiKey` (string): Your Google Maps API Key. This key is required for the Map component to function correctly. Defaults to `""`.

---

#### **`auth` (Object)**
Represents the user's authentication and authorization status for the session.

*   `auth.authenticated` (boolean/null, Readonly): Is `true` if the user is logged in, `false` if they are not, and `null` if the status is unknown.
*   `auth.securityLevels` (Array of SecurityLevel Objects, Readonly): The user's current security levels in a hierarchical structure.
    *   A `SecurityLevel` object has a `name` (string) and `children` (array of `SecurityLevel` objects).
*   **`auth.user` (Object, Readonly)**: Contains information about the logged-in user. All sub-properties will be `null` if the user is not authenticated.
    *   `auth.user.id` (string/null): The Identity Provider's unique ID for the user.
    *   `auth.user.userName` (string/null): The user's username.
    *   `auth.user.firstName` (string/null): The user's first name.
    *   `auth.user.lastName` (string/null): The user's last name.
    *   `auth.user.email` (string/null): The user's email address.
    *   `auth.user.roles` (Array of strings/null): A list of roles assigned to the user by the Identity Provider.
    *   `auth.user.timestamp` (date/null): The timestamp of when the user last logged into this session.

---

#### **`gateway` (Object)**
Information about the connected Ignition Gateway.

*   `gateway.address` (string, Readonly): The remote host address of the gateway.
*   `gateway.timezone` (Object, Readonly): The timezone of the gateway.
    *   `gateway.timezone.id` (string): The timezone ID (e.g., "America/Chicago").
    *   `gateway.timezone.name` (string): The name of the timezone.
    *   `gateway.timezone.utcOffset` (number): The offset from UTC in hours.

---

#### **`device` (Object)**
Information about the device running the session.

*   `device.type` (string, Readonly): The type of device. Can be one of: `"ios"`, `"android"`, `"designer"`, `"browser"`, `"workstation"`. It will be an empty string if the type is unknown or during session loading.
*   `device.identifier` (string, Readonly): A unique ID for the device. **Note:** This is a convenience property and is not suitable for security purposes, as it can change if the app is reinstalled or browser cache is cleared.
*   `device.userAgent` (string, Readonly): The User Agent string from the device's browser or application.
*   `device.timezone` (Object, Readonly): The timezone of the device. Structure is the same as `gateway.timezone`.
*   **`device.settings` (Object)**: Writable settings to control device behavior.
    *   `device.settings.pullToRefresh` (boolean): If `true`, swiping down from the top of the page will refresh the project. Defaults to `true`.
    *   `device.settings.preventSleep` (boolean): If `true`, the device will be prevented from sleeping while the project is being viewed. Defaults to `false`.
*   **`device.accelerometer` (Object, Readonly)**: Provides data from the device's accelerometer.
    *   `device.accelerometer.timestamp` (number): The timestamp of the reading in milliseconds since the Unix epoch.
    *   `device.accelerometer.x` (number): Acceleration force (m/s²) along the x-axis.
    *   `device.accelerometer.y` (number): Acceleration force (m/s²) along the y-axis.
    *   `device.accelerometer.z` (number): Acceleration force (m/s²) along the z-axis.

---

#### **`bluetooth` (Object)**
Provides control and data for device Bluetooth services.

*   `bluetooth.enabled` (boolean): Set to `true` to start listening for Bluetooth advertising packets. Set to `false` to stop. Defaults to `false`.
*   `bluetooth.data` (Array, Readonly): An array containing the most recent Bluetooth packets seen by the device.
*   **`bluetooth.options` (Object)**: Configuration for how Bluetooth data is gathered.
    *   `bluetooth.options.updateInterval` (number): The time in milliseconds to buffer Bluetooth data before sending it to the session. Defaults to `1000`.
    *   `bluetooth.options.limit` (number): The maximum number of packets to report. Packets with a stronger RSSI (signal strength) are prioritized. Defaults to `10`.
    *   **`bluetooth.options.filter` (Object)**: Options to filter which packets are reported.
        *   `bluetooth.options.filter.enabled` (boolean): Set to `true` to enable filtering. Defaults to `false`.
        *   `bluetooth.options.filter.minimumRSSI` (number): The minimum RSSI strength to report. Use `0` to ignore this filter.
        *   You can also filter by beacon type (`altBeacon`, `eddystone`, `iBeacon`) by providing a `uuid` or `namespaceID` and setting `exclusive` to `true` if you only want that type. **Note for iOS:** You *must* specify an iBeacon `uuid` to receive any iBeacon data.

---

#### **`geolocation` (Object)**
Provides control and data for device geolocation services (GPS).

*   `geolocation.enabled` (boolean): Set to `true` to start requesting location data. Set to `false` to stop. This will typically trigger a permission prompt for the user. Defaults to `false`.
*   `geolocation.permissionGranted` (boolean/null, Readonly): Becomes `true` if the user allows location permission, `false` otherwise.
*   **`geolocation.data` (Object, Readonly)**: Holds the location information if `enabled` is `true` and permission is granted. All sub-properties will be `null` if location is not available.
    *   `geolocation.data.latitude` (number/null): Latitude in decimal degrees.
    *   `geolocation.data.longitude` (number/null): Longitude in decimal degrees.
    *   `geolocation.data.altitude` (number/null): Altitude in meters above sea level.
    *   `geolocation.data.accuracy` (number/null): Accuracy of latitude/longitude in meters.
    *   `geolocation.data.altitudeAccuracy` (number/null): Accuracy of altitude in meters.
    *   `geolocation.data.heading` (number/null): Direction of travel in degrees from true north (0-359.9).
    *   `geolocation.data.speed` (number/null): Velocity in meters per second.
    *   `geolocation.data.timestamp` (number/null): Timestamp of the last location update.
*   **`geolocation.options` (Object)**: Configuration for how geolocation data is gathered.
    *   `geolocation.options.accuracy` (string): The desired accuracy mode. Affects battery life.
        *   `"max"`: Highest possible accuracy.
        *   `"high"`: High accuracy (~3m).
        *   `"balanced"`: Balanced accuracy (~100m). **(Default)**
        *   `"low"`: Low accuracy, low power (~3km).
    *   `geolocation.options.timeout` (number): Maximum time in milliseconds to wait for a position. Default is `Infinity`.
    *   `geolocation.options.maximumAge` (number): How old a cached position can be (in milliseconds) before a new one is required. `0` means a fresh position is always required. Default is `0`.

---

#### **Other Properties**

*   **`appBar` (Object)**: Settings for the bottom-docked App Bar.
    *   `appBar.togglePosition` (string): Position of the toggle button. Can be `"left"`, `"right"`, or `"hidden"`. Defaults to `"right"`.
    *   `appBar.about` (Object): Configuration for the "About" modal. You can set an `icon`, `path` to a view, and a `title`.

*   **`pipes` (Object)**: Default appearance settings for Piping components.
    *   `pipes.autoAppearance` (string): Appearance for pipes set to 'auto'. Can be `"p&id"`, `"mimic"`, or `"simple"`. Defaults to `"simple"`.
    *   `pipes.overlapGap` (number): The gap width when P&ID pipes overlap. Defaults to `4`.

*   **`symbols` (Object)**: Default settings for Symbol components.
    *   `symbols.autoAnimationSpeed` (number): Animation speed percentage for symbols set to 'auto'. `0` disables animation. Defaults to `100`.
    *   `symbols.autoAppearance` (string): Appearance for symbols set to 'auto'. Can be `"p&id"`, `"mimic"`, or `"simple"`. Defaults to `"simple"`.

*   **`offline` (Object, Readonly)**: Information about the project's offline status.
    *   `offline.capable` (boolean): `true` if the project is configured for offline mode.
    *   `offline.enabled` (boolean): `true` if the session started and is currently offline.
    *   `offline.lastSynced` (date/string): The last time the project was synchronized for offline use.
    *   `offline.language` (string): The language for offline translations.

---

### IV. Helpful Tips

*   **Checking Authentication**: Before accessing user details under `session.props.auth.user`, always check if `session.props.auth.authenticated` is `true`. Otherwise, all user properties will be `null`.
*   **Device Features and Battery**: Be mindful that enabling features like `geolocation` and `bluetooth` will increase battery consumption on mobile devices. Use the `geolocation.options.accuracy` property to balance precision with battery life. Setting `device.settings.preventSleep` to `true` will also significantly impact battery.
*   **Permissions**: Enabling `geolocation` or `bluetooth` will trigger a permission prompt to the user. The feature will not work if the user denies permission. You can check the `geolocation.permissionGranted` property to see the user's choice.
*   **Read-Only Properties**: Many properties, especially those providing information from the gateway or device (like `id`, `host`, `lastActivity`, `device.type`, `geolocation.data`), are read-only. Their values are set by the system.
*   **Device Identifier**: Do not rely on `session.props.device.identifier` for security-sensitive applications. It is not guaranteed to be permanent and can be changed.
*   **Maps Component**: The `session.props.googleMapsApiKey` must be set with a valid Google Maps API key for the Perspective Map Component to display maps.
*   **Numbers in JavaScript**: Be aware that JavaScript has limitations with very large integers (greater than ~9 quadrillion). If you are working with data that might exceed this, the values could be altered unexpectedly. This is a general JavaScript limitation, not specific to Ignition.

# Schema - raw
{"type":"object","definitions":{"context":{"type":"object","default":{}},"timezone":{"type":"object","description":"Document providing timezone information","properties":{"id":{"type":"string","description":"Timezone identification code"},"name":{"type":"string","description":"Name of the timezone"},"utcOffset":{"type":"number","description":"Offset of the current timezone relative to UTC, in hours","default":0}}},"securityLevel":{"type":"object","description":"A Security Level represents a hierarchical node of access.","properties":{"name":{"type":"string","description":"The name for this security level. Unique amongst its siblings.","default":""},"children":{"type":"array","description":"Security levels which descend from this security level.","items":{"$ref":"#/definitions/securityLevel"},"default":[]}}}},"properties":{"id":{"type":"string","description":"A string identifier unique to this session"},"host":{"type":"string","description":"Remote host of the app or browser, as detected by the gateway"},"theme":{"type":"string","default":"light","description":"Current/initial setting for session theme","extension":{"suggestion-source":"theme-names"}},"locale":{"type":"string","description":"The current locale of this session","default":""},"timeZoneId":{"type":"string","default":""},"lastActivity":{"description":"Gateway date of the last user activity in the Client. Readonly.","type":["date","null"],"default":null},"auth":{"type":"object","description":"Represents the user's authentication and authorization status for this session.","properties":{"authenticated":{"type":["boolean","null"],"description":"true if the user is authenticated. false if the user is not authenticated. null if the user's authentication status is unknown.","default":null},"user":{"type":"object","description":"Contains information about the user if they are authenticated","properties":{"id":{"type":["string","null"],"description":"The Identity Provider's unique identifier for this user. null if the user is not authenticated.","default":null},"userName":{"type":["string","null"],"description":"The user's username. null if the user is not authenticated.","default":null},"firstName":{"type":["string","null"],"description":"The user's first name. null if the user is not authenticated or if the Identity Provider did not provide this attribute or if no mapping was configured for this attribute.","default":null},"lastName":{"type":["string","null"],"description":"The user's last name. null if the user is not authenticated or if the Identity Provider did not provide this attribute or if no mapping was configured for this attribute.","default":null},"email":{"type":["string","null"],"description":"The user's email address. null if the user is not authenticated or if the Identity Provider did not provide this attribute or if no mapping was configured for this attribute.","default":null},"roles":{"type":["array","null"],"description":"The roles that the Identity Provider assigned this user. null if the user is not authenticated or if the Identity Provider did not provide this attribute or if no mapping was configured for this attribute.","items":{"type":"string","description":"The name which uniquely identifies this role","default":""},"default":null},"timestamp":{"description":"The timestamp of when the current user last logged into Perspective from the IdP. null if the user is not authenticated."}}},"securityLevels":{"type":"array","description":"The user's current security levels.","items":{"$ref":"#/definitions/securityLevel"},"default":[]}}},"gateway":{"type":"object","properties":{"address":{"type":"string","description":"Remote host address of the connected gateway.","default":""},"timezone":{"$ref":"#/definitions/timezone"}}},"device":{"type":"object","properties":{"type":{"description":"Type of device that created this session. Readonly. Options: 'ios', 'android', 'designer', 'browser', 'workstation'.  Empty string if device unknown/during loading.","type":"string","enum":["ios","android","designer","browser","workstation",""],"default":""},"identifier":{"description":"A unique ID representing the device. Readonly. Convenience property not intended/suitable for security purposes.  May change via device/application reinstalls, browser cache clears.","type":"string","default":""},"timezone":{"$ref":"#/definitions/timezone"},"userAgent":{"description":"User Agent string of the connected device.","type":"string","default":""},"settings":{"type":"object","properties":{"pullToRefresh":{"description":"If true, swiping down from top of page and holding for two seconds will refresh project.","type":"boolean","default":true},"preventSleep":{"description":"Prevent the device from sleeping while viewing project.","type":"boolean","default":false}}},"accelerometer":{"type":"object","description":"When continuous read mode is active, represents values retrieved from the accelerometer.","properties":{"timestamp":{"type":"number","default":0,"description":"Timestamp represented as standard 'milliseconds since unix epoch'."},"x":{"type":"number","default":0,"description":"Acceleration force (in m/s²) along the x axis (including gravity)."},"y":{"type":"number","default":0,"description":"Acceleration force (in m/s²) along the y axis (including gravity)."},"z":{"type":"number","default":0,"description":"Acceleration force (in m/s²) along the z axis (including gravity)."}}}},"default":{"type":"","identifier":"","userAgent":"","settings":{"pullToRefresh":true,"preventSleep":false},"accelerometer":{"timestamp":0,"x":0,"y":0,"z":0}}},"bluetooth":{"type":"object","description":"Options and data provided by device Bluetooth services.","properties":{"enabled":{"type":"boolean","default":false,"description":"If true, will start listening for Bluetooth advertising packets."},"options":{"type":"object","properties":{"updateInterval":{"type":"number","default":1000,"description":"Duration in ms to buffer Bluetooth data before sending to Perspective."},"limit":{"type":"number","default":10,"description":"Maximum number of packets to display. Packets with stronger RSSI have priority."},"filter":{"type":"object","properties":{"enabled":{"type":"boolean","default":false,"description":"If true, will enable filtering."},"minimumRSSI":{"type":"number","default":0,"description":"Minimum strength of RSSI to return, 0 to ignore."},"altBeacon":{"type":"object","description":"AltBeacon format.","properties":{"exclusive":{"type":"boolean","default":false,"description":"Exclude other beacon types."},"uuid":{"type":"string","default":"","description":"16 byte beacon identifier."}}},"eddystone":{"type":"object","description":"Eddystone open beacon format.","properties":{"exclusive":{"type":"boolean","default":false,"description":"Exclude other beacon types."},"namespaceID":{"type":"string","default":"","description":"Namespace component"}}},"iBeacon":{"type":"object","description":"iBeacon format.","properties":{"exclusive":{"type":"boolean","default":false,"description":"Exclude other beacon types."},"uuid":{"type":"string","default":"","description":"16 byte proximity uuid of iBeacon. On iOS this must be specified in order to receive iBeacon data."}}}}}}},"data":{"type":"array","description":"Most recent packets seen by device.","default":[]}}},"geolocation":{"type":"object","description":"Options and data provided by web or native device geolocation services.","properties":{"enabled":{"type":"boolean","default":false,"description":"If true, will attempt to populate location data into the 'data' property"},"permissionGranted":{"type":["boolean","null"],"default":null,"description":"If geolocation is enabled and a geolocation permission prompt is requested, this field populates true if the user allowed permission.  Otherwise, false.  Readonly."},"options":{"type":"object","properties":{"accuracy":{"type":"string","enum":["max","high","balanced","low"],"default":"balanced","description":"Indicates the mode of accuracy the application uses to receive results. MAX: Maximum accuracy (and highest system battery use).  Accurate to the level allowed by the environment/device.  HIGH: High accuracy (and high system battery use). accuracy resolves ~3m using a more efficient poll rate.  BALANCED: Balanced accuracy - accuracy resolves ~100m (about a city block) using a more efficient poll rate and supplementing with device data. LOW: Low accuracy - typically does not use GPS sensor, but relies on environmental meta data (such as cell tower information, wifi connectivity, etc).  Most efficient, accurate to approximately town/3 kilometers. The default value is balanced."},"timeout":{"type":["number","string"],"description":"Is a positive long value representing the maximum length of time (in milliseconds) the device is allowed to take in order to return a position. The default value is Infinity, meaning that getCurrentPosition() won't return until the position is available."},"maximumAge":{"type":"number","description":"Is a positive long value indicating the maximum age in milliseconds of a possible cached position that is acceptable to return. If set to 0, it means that the device cannot use a cached position and must attempt to retrieve the real current position. If set to Infinity the device must return a cached position regardless of its age. Default: 0.","default":0}}},"data":{"description":"If geolocation is enabled and the device can provide geolocation data, this will hold information about location.","type":"object","properties":{"latitude":{"description":"A floating point value representing the position's latitude in decimal degrees.  null if location disabled.","type":["number","null"],"default":null},"longitude":{"description":"A floating point value representing the position's longitude in decimal degrees. null if location disabled.","type":["number","null"],"default":null},"altitude":{"description":"A double representing the position's altitude in meters, relative to sea level. This value can be null if the implementation cannot provide the data.","type":["number","null"],"default":null},"accuracy":{"description":"A double representing the accuracy of the latitude and longitude properties, expressed in meters.","type":["number","null"],"default":null},"altitudeAccuracy":{"description":"A double representing the accuracy of the altitude expressed in meters. May be null if device fails to provide, or geolocation is disabled.","type":["number","null"],"default":null},"heading":{"description":"Returns a double representing the direction in which the device is traveling. This value, specified in degrees, indicates how far off from heading true north the device is. 0 degrees represents true north, and the direction is determined clockwise (which means that east is 90 degrees and west is 270 degrees). If speed is 0, heading is NaN. If the device is unable to provide heading information, this value is null.","type":["number","null"],"default":null},"speed":{"description":"Returns a double representing the velocity of the device in meters per second. This value can be null.","type":["number","null"],"default":null},"timestamp":{"description":"Time the last location update was received.","type":["number","null"],"default":null}}}}},"appBar":{"type":"object","description":"Settings relevant to the bottom-docked \"App Bar\", which lists gateway information.","properties":{"togglePosition":{"type":"string","enum":["left","right","hidden"],"default":"right","description":"The position of the overlaid toggle button that shows the app bar."},"about":{"type":"object","properties":{"show":{"type":"boolean","deprecated":true,"example":false,"description":"Deprecated. About panel will be shown automatically."},"icon":{"type":"string","default":"","description":"The path of the about button icon.","format":"icon-path"},"path":{"type":"string","default":"","format":"view-path","description":"Path of the view to display in the about modal."},"title":{"type":"string","default":"","description":"The title of the about modal."}}}}},"pipes":{"type":"object","properties":{"autoAppearance":{"type":"string","description":"The appearance to use for Piping with appearance prop set to auto.","enum":["p&id","mimic","simple"],"default":"simple"},"overlapGap":{"type":"number","description":"The width of the gap to draw when P&ID pipes overlap.","default":4}},"default":{"autoAppearance":"simple","overlapGap":4}},"symbols":{"type":"object","properties":{"autoAnimationSpeed":{"type":"number","description":"The speed of animations as a percent to use for Symbols with animationSpeed set to auto. 0 turns off animations.","default":100},"autoAppearance":{"type":"string","description":"The appearance to use for Symbols with appearance prop set to auto.","enum":["p&id","mimic","simple"],"default":"simple"}}},"googleMapsApiKey":{"type":"string","description":"Google Maps API Key","default":""},"offline":{"type":"object","properties":{"capable":{"type":"boolean","description":"True if the project has been configured to work offline.","default":false},"enabled":{"type":"boolean","description":"True if the current session was started offline, and continues to be offline.","default":false},"lastSynced":{"type":["date","string"],"description":"The last time this project was synchronized for offline use.","default":""},"language":{"type":"string","description":"The language for offline translations.","default":""}}}}}