# Perspective DateTime Picker Component

## Description

These instructions detail the configuration and usage of the Perspective DateTime Picker component. You will learn how to use its properties to control the picker's type, format the displayed value, constrain the selectable date range, and apply localization. The document also covers the component's primary events for scripting actions and offers best practices for effective implementation.

## Documentation

# Instructions
# Perspective DateTime Picker Component Instructions

## Object Name
Perspective DateTime Picker

## Introduction
The Perspective DateTime Picker is an input component that provides a user-friendly calendar and clock interface for users to select a date, a time, or both. It is highly configurable, allowing for control over the format, selectable range, and localization.

---

## Component Properties

The component's behavior and appearance are controlled by its properties, found in the Property Editor.

| Property | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| **pickerType** | string | Determines whether the component allows the user to select only a date (`date`) or both a date and a time (`datetime`). | `datetime` |
| **value** | date, number, null | The currently selected date and time. This value can be a Date object or a timestamp in milliseconds since the Unix epoch. This property is best for bindings and scripting logic. | `null` |
| **formattedValue** | string, null | A read-only string representation of the `value` property, formatted according to the `format` property. This is ideal for display purposes. | `""` |
| **format** | string | A string that defines the format for the `formattedValue` property. It must use a valid [moment.js](https://momentjs.com/docs/#/displaying/format/) format string. For example, 'MM/DD/YYYY h:mm a'. | `lll` |
| **minDate** | date, number, null | The minimum selectable date/time. Can be a Date object or a timestamp in milliseconds. If not set (`null`), the minimum date defaults to 10 years in the past from the current day. | `null` |
| **maxDate** | date, number, null | The maximum selectable date/time. Can be a Date object or a timestamp in milliseconds. If not set (`null`), the maximum date defaults to 10 years in the future from the current day. | `null` |
| **locale** | string | A code that specifies the language and formatting for the calendar. A dropdown list is available in the designer with numerous options. | `en` |
| **enabled** | boolean | If `true`, the user can interact with the component. If `false`, the component is visually disabled. Note: Even when disabled, component events (like `onActionPerformed`) can still be triggered by user clicks. | `true` |
| **style** | object | An object that allows for extensive styling of the component's appearance, including text, background, borders, and margins. | |

---

## Component Variants

The DateTime Picker has two pre-configured variants available in the Component Palette:

*   **Date and Time:** The default configuration, allowing users to select both a date and a time. The `pickerType` is set to `datetime`.
*   **Date:** A variant configured to allow users to select only a date. The `pickerType` is set to `date`.

---

## User Interface Interactions

The component's user interface allows for intuitive selection:

*   **Year Selector:** Allows the user to choose a specific year.
*   **Month Selector:** Allows the user to choose a specific month.
*   **Day Selector:** Allows the user to choose a specific day from the calendar view.
*   **Time Selector:** Allows the user to choose a specific time (hours and minutes).
*   **AM/PM:** Allows the user to toggle between AM and PM.

---

## Component Events

*   **onActionPerformed:** This is the primary event for this component. It fires when the user makes a selection. You can configure actions, such as running a script, in response to this event.

---

## Helpful Tips & Best Practices

*   **`value` vs. `formattedValue`:** This is a critical distinction.
    *   Use the `value` property for any data manipulation, scripting, or binding to other component properties that expect a date/time object or a numeric timestamp.
    *   Use the `formattedValue` property when you need to display the selected date/time in a human-readable format, such as in a label or table.
*   **Date/Time Formatting:** The `format` property is very powerful. Refer to the moment.js documentation for a complete list of available format specifiers to display the date and time exactly as you need it (e.g., `YYYY-MM-DD` for a database-friendly format or `dddd, MMMM Do YYYY` for a long-form display).
*   **Constraining Dates:** Use the `minDate` and `maxDate` properties to prevent users from selecting dates outside of a valid range. These properties can be bound to other properties or tags to create dynamic date ranges. For example, the `maxDate` of a "Start Date" picker could be bound to the `value` of an "End Date" picker.
*   **Localization (`locale`):** To ensure your application is accessible to a global audience, set the `locale` property appropriately. This will translate month names, day names, and apply the correct local date formatting conventions.
*   **Disabled State:** Be aware that setting `enabled` to `false` does *not* prevent component events from firing. If you want to completely prevent any actions, you should also add logic to your event scripts to check the `enabled` property before executing.
*   **Choosing the Right `pickerType`:** Always choose the appropriate `pickerType` for the required data. If the time of day is not relevant, use the `date` pickerType to simplify the user interface and avoid confusion.

# Schema - raw
{"schema":{"type":"object","properties":{"pickerType":{"description":"Whether to display and enable picker for date only, or both date and time","type":"string","enum":["datetime","date"],"default":"datetime"},"minDate":{"description":"Minimum date/time as a Date object or timestamp in milliseconds. If null, the minimum date is 10 years in the past from today.","type":["date","number","null"],"default":null},"format":{"description":"Template for formatting date display - must be valid moment.js format, e.g. 'MM/DD/YYYY h:mm a'","type":"string","default":"lll"},"locale":{"description":"Code for localization of language and formatting","type":"string","default":"en","suggestions":["en","ar","be","bg","bn","ca","cs","cy","da","de-at","de-ch","de","el","en-au","en-ca","en-gb","en-ie","en-il","en-nz","es-do","es-us","es","et","eu","fi","fr-ca","fr-ch","fr","hi","hu","is","it","ja","ko","lt","lv","mk","ms-my","ms","mt","nb","nn","pl","pt-br","pt","ro","ru","sk","sl","sr-cyrl","sr","sv","sw","th","tr","uk","uz","vi","zh-cn","zh-hk","zh-tw"]},"enabled":{"description":"False will disable any interaction with calendar","type":"boolean","default":true},"formattedValue":{"description":"Date and time in configured format","type":["string","null"],"default":""},"maxDate":{"description":"Maximum date/time as a Date object or timestamp in milliseconds. If null, the maximum date is 10 years in the future from today.","type":["date","number","null"],"default":null},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"value":{"description":"Current date/time as a Date object or timestamp in milliseconds","type":["date","number","null"],"default":null}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"DateTimePicker","name":"DateTime Picker","palette":{"variants":[{"tooltip":"Provides a calendar from which the user can select the date and time.","label":"DateTime Picker"},{"tooltip":"Provides a calendar from which the user can select the date and time.","label":"Date and Time","id":"date-time-picker-datetime"},{"tooltip":"Provides a calendar from which the user can select the date and time.","label":"Date","props":{"pickerType":"date"},"id":"date-time-picker-date"}],"category":"input"},"id":"ia.input.date-time-picker","events":[{"schema":{"type":"object"},"documentationUrl":"https://links.inductiveautomation.com/81-action-performed-event","description":"This event is fired when the 'action' of the component occurs.","name":"onActionPerformed"}]}