# Perspective DateTime Input Component

## Description

The usage and configuration of the Perspective DateTime Input component. These instructions detail the component's properties and events, explaining how to control the picker type, format the displayed value, restrict the selectable range, customize its visual style, and respond to user selections.

## Documentation

# Instructions
# Perspective DateTime Input Component Instructions

## Object Description
The Perspective DateTime Input component provides a user-friendly interface for selecting a date, a time, or both from a popup calendar or time selector. It is designed to be compact, taking up less screen space than the DateTime Picker. The component displays the selected date and/or time in a text field, which, when clicked, reveals the selection interface.

There are three main variants of this component, determined by the `pickerType` property:
*   **DateTime Input:** The default variant, which allows users to select both a date and a time.
*   **Date and Time:** Functionally identical to the default DateTime Input.
*   **Time:** A variant that only allows users to select a time via up and down arrows.

## Properties

Below is a detailed list of the component's properties.

### General Properties
| Property | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| **value** | `Date`, `number`, `null` | The currently selected date/time. This can be a Date object or a timestamp in milliseconds since the Unix epoch. Setting this property updates the component's selection. | `null` |
| **formattedValue** | `string`, `null` | A read-only string representation of the selected date and time, formatted according to the `format` property. | `""` |
| **pickerType** | `string` | Determines which picker interface is shown. Can be "datetime" (default), "date", or "time". | `"datetime"` |
| **format** | `string` | A `moment.js` format string that defines how the selected date/time is displayed in the input field (e.g., 'MM/DD/YYYY h:mm a'). The default is 'lll'. | `"lll"` |
| **placeholder** | `string` | The text that appears in the input field when no value is selected. | `"Select date"` |
| **enabled** | `boolean` | If `false`, the component is visually greyed out and all user interaction is disabled. However, scripts on events like `onStartup` can still execute. | `true` |
| **locale** | `string` | The localization code for language and date/time formatting. A dropdown list of available locales is provided in the designer. | `"en"` |
| **dismissOnSelect** | `boolean` | If `true`, the calendar/time picker modal will close automatically as soon as the user selects a date. | `true` |

### Date Range Properties
| Property | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| **minDate** | `Date`, `number`, `null` | The earliest selectable date/time. If `null`, the minimum is set to 10 years in the past from the current day. | `null` |
| **maxDate** | `Date`, `number`, `null` | The latest selectable date/time. If `null`, the maximum is set to 10 years in the future from the current day. | `null` |

### Style and Appearance Properties
| Property | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| **style** | `object` | An object containing CSS styles to be applied to the main component container. Style classes can also be specified here. | |
| **modalStyle** | `object` | An object containing CSS styles to be applied specifically to the popup modal (the calendar/picker). This is only visible when `pickerType` is "datetime" or "date". | `{"classes":""}` |
| **inputProps** | `object` | An object for passing properties to the underlying input element, primarily used for applying CSS styles directly to the text input field itself. The `disabled` and `value` properties here are ignored in favor of the top-level `enabled` and `value` properties. | `{"style":{}}` |


## Events
*   **onActionPerformed**: This event is fired when the user makes a selection in the component. For example, clicking a date in the calendar popup will trigger this event.

---

## Helpful Tips for the LLM

*   **Core Functionality**: Your main purpose is to configure this component to allow users to select a date, time, or both. The most important property to achieve this is `pickerType`.
*   **`value` vs. `formattedValue`**: The `value` property holds the raw selected date as a millisecond timestamp or Date object, which is useful for bindings and scripting. The `formattedValue` is a read-only string, useful for display purposes, that is derived from `value` and the `format` property. You will typically bind `props.value` bidirectionally to a Tag or other property.
*   **Date/Time Formatting**: The `format` property is key for controlling how the date and time are displayed to the user. You must use valid [moment.js](https://momentjs.com/docs/#/displaying/format/) format strings. For example, to show a date like "25/12/2024", you would set `format` to `"DD/MM/YYYY"`.
*   **Restricting Dates**: Use `minDate` and `maxDate` to limit the selectable date range. You can bind these properties to other date components or expressions to create dynamic date ranges (e.g., the end date cannot be before the start date).
*   **Styling**:
    *   To style the text input field (e.g., its border, background color), modify `props.inputProps.style`.
    *   To style the popup calendar itself, modify `props.modalStyle`.
    *   To style the overall component container, use `props.style`.
*   **Placeholders**: The `placeholder` property provides a helpful cue to the user when no value has been selected yet.
*   **Internationalization**: Use the `locale` property to adapt the component's language and date formatting conventions for different regions. For example, setting `locale` to `"fr"` will display calendar month and day names in French.
*   **Events**: Use the `onActionPerformed` event to trigger actions (like running a script or refreshing a query) immediately after a user selects a date/time.
*   **Disabled State**: Remember that setting `enabled` to `false` only prevents user interaction. Component events that are not user-initiated, like an `onStartup` event, will still run.
*   **Component Variants**: The "Date and Time" and "Time" variants found in the Component Palette are simply pre-configured versions of the base DateTime Input component. "Time" has its `pickerType` property set to `"time"`.

# Schema - raw
{"schema":{"type":"object","properties":{"pickerType":{"description":"Whether to display and enable picker for date only, or both date and time","type":"string","enum":["datetime","date","time"],"default":"datetime"},"minDate":{"description":"Minimum date/time as a Date object or timestamp in milliseconds. If null, the minimum date is 10 years in the past from today.","type":["date","number","null"],"default":null},"dismissOnSelect":{"description":"Determines if the date picker should be dismissed when a date is selected.","type":"boolean","default":true},"format":{"description":"Template for formatting date display - must be valid moment.js format, e.g. 'MM/DD/YYYY h:mm a'","type":"string","default":"lll"},"locale":{"description":"Code for localization of language and formatting","type":"string","default":"en","suggestions":["en","ar","be","bg","bn","ca","cs","cy","da","de-at","de-ch","de","el","en-au","en-ca","en-gb","en-ie","en-il","en-nz","es-do","es-us","es","et","eu","fi","fr-ca","fr-ch","fr","hi","hu","is","it","ja","ko","lt","lv","mk","ms-my","ms","mt","nb","nn","pl","pt-br","pt","ro","ru","sk","sl","sr-cyrl","sr","sv","sw","th","tr","uk","uz","vi","zh-cn","zh-hk","zh-tw"]},"enabled":{"description":"False will disable any interaction with calendar","type":"boolean","default":true},"modalStyle":{"visibleWhen":{"equals":["datetime","date"],"property":"pickerType"},"description":"Style applied to the date picker modal.","type":"object","default":{"classes":""},"properties":{"classes":{"format":"style-list","description":"Styles defined in the project to be applied to this component","type":["array","string"],"title":"Style Class Names","default":""},"style":{"$ref":"urn:ignition-schema:schemas/css-props.schema.json"}}},"inputProps":{"description":"Props to pass to the input group. disabled and value will be ignored in favor of the top-level props on this component.","type":"object","default":{"style":{}},"properties":{"style":{"$ref":"urn:ignition-schema:schemas/css-props.schema.json"}}},"formattedValue":{"description":"Date and time in configured format","type":["string","null"],"default":""},"maxDate":{"description":"Maximum date/time as a Date object or timestamp in milliseconds. If null, the maximum date is 10 years in the future from today.","type":["date","number","null"],"default":null},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"placeholder":{"description":"Text for input field to display when no date/time is selected","type":"string","default":"Select date"},"value":{"description":"Current date/time as a Date object or timestamp in milliseconds","type":["date","number","null"],"default":null}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"DateTimeInput","name":"DateTime Input","palette":{"variants":[{"tooltip":"Provides a way to select a date from a popup calendar.","label":"DateTime Input"},{"tooltip":"Provides a way to select a date from a popup calendar.","label":"Date and Time","id":"date-time-input-datetime"},{"tooltip":"Provides a way to select a date from a popup calendar.","label":"Time","props":{"pickerType":"time"},"id":"date-time-input-time"}],"category":"input"},"id":"ia.input.date-time-input","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}