# Perspective Audio Component

## Description

This document describes the usage and configuration of the Perspective Audio component (`ia.display.audio`), which is used to embed and control audio playback within an Ignition Perspective session. The instructions cover the component's properties for managing the audio source, playback state, volume, and player visibility. Additionally, they explain how to use events to trigger scripts in response to playback status changes, such as a track ending or an error occurring.

## Documentation

# Instructions
This document provides instructions for using the Perspective Audio Component in Ignition.

### Object Name
`ia.display.audio`

### Core Concept
The Audio Component is used to play audio files within a Perspective session. Its primary function is to embed sound into a view, which can be controlled through its properties. By default, the component is not visible to the user, allowing it to be used for background audio notifications or sound effects. It can be made visible, in which case it will render the browser's native audio player interface.

### Properties

| Property | Type | Description |
| --- | --- | --- |
| `play` | boolean | Controls the playback state. When set to `true`, the audio begins to play from its current position. When set to `false`, it pauses. This is the primary property for controlling audio playback. |
| `source` | string | The URL path to the audio file that needs to be played. This is a required property for any audio to be heard. |
| `display` | boolean | Determines if the audio player's UI is visible. If `false` (the default), the component is hidden. If `true`, the browser's native audio player is displayed. |
| `volume` | number | A number between 0 and 100 representing the audio volume as a percentage. The default is 100. |
| `playbackRate` | number | A double that sets the playback speed of the audio. `1` is normal speed, `2` is double speed, `0.5` is half speed. Default is `1`. |
| `loop` | boolean | If set to `true`, the audio file will automatically restart from the beginning as soon as it finishes playing. Default is `false`. |
| `allowDownload` | boolean | If set to `true`, the browser's native audio player may show a download button for the media file. This is only relevant if `display` is also `true`. Default is `false`. |
| `style` | object | Standard style properties to control the appearance of the component's container when `display` is `true`. |

### Events

The Audio Component has several events that can trigger scripts:

*   **`onPlay`**: Fires when the audio begins playing.
*   **`onPause`**: Fires when the audio is paused.
*   **`onEnded`**: Fires when the audio track finishes playing naturally (does not fire if `loop` is true, as playback doesn't technically end).
*   **`onError`**: Fires if an error occurs during playback (e.g., the source file cannot be found or is in an unsupported format). It provides an `errorMessage` string in its event object.
*   **`onLoaded`**: Fires once the first frame of the audio media has been loaded and is ready.
*   **`onRateChanged`**: Fires whenever the `playbackRate` property is changed.

### Helpful Tips

*   The most common use case for this component is as a hidden element (`display: false`) to provide audio feedback based on user actions or system events. For example, you can bind the `play` property to a memory tag that gets toggled by a script.
*   **CRITICAL:** The supported audio file formats (e.g., MP3, WAV, OGG) are entirely dependent on the web browser being used to view the Perspective session, not on the Ignition Gateway.
*   Similarly, if you choose to make the component visible by setting `display` to `true`, the appearance and controls of the audio player are determined by the browser (Chrome, Firefox, Safari, etc.) and will look different to different users.
*   The `source` property must contain a valid URL to an audio file. You can use the Webdev module to host audio files directly on the Ignition Gateway or point to an externally hosted file.
*   To play a sound in response to a button click, place an Audio component on the view, set its `source` to the desired audio file URL, and in the button's `onClick` event, use a script to write `true` to the Audio component's `play` property.
*   The `onEnded` event is useful for creating sequential actions. For example, you could use this event to trigger another process or play another sound once the first one has finished.
*   Use the `onError` event to debug issues with audio playback or to notify a user that an audio file could not be played. The `errorMessage` property within the event object can be logged or displayed for diagnostics.
*   For more advanced control, scripting functions are available. See the "Perspective - Audio Scripting" page in the Ignition documentation for more details.

# Schema - raw
{"schema":{"type":"object","properties":{"play":{"description":"The play state of the media file. Toggling the property will start or pause the media file.","type":"boolean","default":false},"display":{"description":"The visible state of the component.","type":"boolean"},"source":{"description":"The source URL of the media file.","type":"string","default":""},"volume":{"description":"The percentage of maximum volume in use (from 0 to 100).","type":"number","default":100},"playbackRate":{"description":"A double that represents the playback rate of the media file.","type":"number","default":1},"loop":{"description":"Determines if the media file should loop when the end is reached.","type":"boolean","default":false},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"allowDownload":{"description":"Determines if the audio player allows downloading of the media file.","type":"boolean","default":false}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Audio","name":"Audio","palette":{"variants":[{"tooltip":"Plays audio tracks supported by the browser.","label":"Audio"}],"category":"display"},"id":"ia.display.audio","events":[{"schema":{"type":"object"},"description":"This event is fired when playback has begun.","name":"onPlay"},{"schema":{"type":"object"},"description":"This event is fired when playback has been paused.","name":"onPause"},{"schema":{"type":"object","properties":{"errorMessage":{"description":"Error message when attempting to play media file.","type":"string"}}},"description":"This event is fired when there is an error attempting to playback.","name":"onError"},{"schema":{"type":"object"},"description":"This event is fired when playback has ended due to reaching end of media.","name":"onEnded"},{"schema":{"type":"object"},"description":"This event is fired when the first frame of the media has loaded.","name":"onLoaded"},{"schema":{"type":"object"},"description":"This event is fired when the playback rate of the media has changed.","name":"onRateChanged"}]}