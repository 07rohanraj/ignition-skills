# Perspective Video Player Component

## Description

This document details the configuration and usage of the Perspective Video Player component for embedding and controlling video files or live camera feeds. It explains the properties used to set a video source, manage playback, and monitor status, while also outlining crucial considerations such as platform-specific behaviors, video codec limitations, and browser compatibility.

## Documentation

# Instructions
# Perspective Video Player Component

## Instructions

### I. Overview

The Video Player component is used to embed video files or live camera feeds into a Perspective view. It can display content from a URL, including video files hosted on the web or served through Ignition's WebDev module, as well as live feeds from IP cameras. The component provides a customizable control bar for interacting with video files and adapts its behavior for live streams.

### II. Component Properties

#### General Properties

*   **`source` (String):** This is the most critical property. It must be set to the URL of the video file or live feed you want to display.
    *   Example for a video file: `"https://example.com/path/to/myvideo.mp4"`
    *   Example for a local file served by WebDev: `"/system/webdev/ProjectName/video.mp4"`
*   **`liveFeed` (Boolean):**
    *   Set to `false` (default) if the `source` is a pre-recorded video file. This will make video-specific properties like `controls`, `status`, and `poster` available.
    *   Set to `true` if the `source` is a live camera feed. This will hide properties that are not applicable to live streams (`controls`, `status`, `poster`, `autohideControls`).
*   **`poster` (String):** The URL for an image to display as a placeholder before the video loads or is played. This is only visible if `liveFeed` is `false`.
*   **`autohideControls` (Boolean):** If `true`, the video control bar will only appear when the user's mouse is hovering over the video. If `false`, the controls are always visible. This is only applicable when `liveFeed` is `false`.

#### Controls Properties (`controls`)

This object contains properties for programmatically controlling the playback of a video file. These properties are only available when `liveFeed` is `false`.

*   **`play` (Boolean):** Sets the playback state. `true` for play, `false` for pause.
*   **`mute` (Boolean):** Sets the audio state. `true` to mute the audio, `false` to unmute.
*   **`seek` (Number):** Jumps the video to a specific time, measured in seconds. For example, a value of `30` will start playback 30 seconds into the video.
*   **`autoplay` (Boolean):** If `true`, the video will attempt to play automatically as soon as it's loaded. **Note:** On many platforms, autoplay will only work if the video is also muted (`controls.mute` is `true`).
*   **`playRate` (Number):** Sets the playback speed. `1` is normal speed, `0.5` is half-speed, and `2` is double-speed.
*   **`volume` (Number):** Sets the audio volume as a percentage, from `0` to `100`.
*   **`loop` (Boolean):** If `true`, the video will automatically restart from the beginning after it finishes.

#### Status Properties (`status`)

This is a **read-only** object that provides information about the current state of the video player. You can bind to these properties to monitor the player's status. These properties are only available when `liveFeed` is `false`.

*   **`paused` (Boolean):** `true` when the video is currently paused.
*   **`playing` (Boolean):** `true` when the video is actively playing.
*   **`ended` (Boolean):** `true` when the video has reached its end.
*   **`progress` (Number):** The current playback time in seconds.
*   **`waiting` (Boolean):** `true` if playback has stopped temporarily due to a lack of data (buffering).
*   **`loadedData` (Boolean):** `true` once the first frame of the video has loaded.
*   **`seeking` (Boolean):** `true` while a seek operation is in progress.
*   **`seeked` (Number):** The time in seconds where the most recent seek operation completed.
*   **`rateChanged` (Number):** The current playback rate.

#### Style Properties

*   **`style` (Object):** Used to apply CSS styles to the main component container.
*   **`controlStyle` (Object):** Used to apply CSS styles specifically to the control bar and its elements (buttons, menus, etc.). This is only available when `liveFeed` is `false`.

### III. Big List of Helpful Tips

*   **Critical: Video Codec Limitations in the Designer.** The Ignition Designer uses an embedded JxBrowser (based on the open-source Chromium project) to render views. Chromium does not support certain proprietary video codecs by default due to licensing restrictions. Google Chrome, however, does support them. This means a video might fail to play in the Designer but work perfectly fine in a client session running in a Chrome browser.
    *   **Codecs NOT supported in the Designer by default:** H.264, HEVC, AAC.
    *   **Codecs supported in the Designer:** VP8, VP9, Vorbis, Opus, Theora, FLAC, WAV, MP3.
    *   If your video uses an unsupported codec, it will not play within the Designer environment.

*   **Platform-Specific Restrictions are Important.** The component's behavior can change significantly based on the user's operating system and browser.
    *   **iOS (iPhone/iPad):**
        *   User interaction (a click or touch) is **required** to start video playback. The `controls.play` property will not work to programmatically start the video.
        *   The component will always use the native iOS video player. Custom styles applied via `controlStyle` will be ignored.
    *   **Android and iOS Tablets:**
        *   When `controls.autoplay` is set to `true`, you **must** also set `controls.mute` to `true` for it to work, due to platform security restrictions.
    *   **Fullscreen Mode (All Platforms):**
        *   When the video enters fullscreen, it will use the browser's native video player.
        *   This means custom `controlStyle` settings will not be visible in fullscreen.
        *   Programmatic control via `controls.play` will not work while in fullscreen; the user must use the native controls.

*   **Read-Only vs. Writable Properties:** Remember the distinction between the `controls` and `status` objects.
    *   Use `controls` (e.g., `controls.play`, `controls.seek`) to *tell the video what to do*. These are writable properties.
    *   Use `status` (e.g., `status.playing`, `status.progress`) to *get information about what the video is doing*. These are read-only properties. Do not attempt to write to them.

*   **Live Feed Mode Simplifies the Component:** Setting `liveFeed` to `true` correctly configures the component for streaming. It automatically hides the `poster`, `controls`, `status`, and `autohideControls` properties, as they are irrelevant for a live stream that has no duration, timeline, or defined start/end.

*   **Browser Incompatibility:** Be aware that some older browsers may not support this component. The documentation specifically notes that Sessions running in **Safari 14** will not be able to play video on this component.

*   **Source URL:** The `source` property can be a standard URL to a video on the internet or a URL pointing to a file within your Ignition Gateway. To serve local files, place them in a folder accessible by the **WebDev** module and use a URL like `/system/webdev/<ProjectName>/<path>/<to>/<file.mp4>`.

# Schema - raw
{"schema":{"type":"object","properties":{"controls":{"visibleWhen":{"equals":false,"property":"liveFeed"},"type":"object","properties":{"play":{"description":"The play state of the video.","type":"boolean","default":false},"mute":{"description":"The muted state of the video's audio track.","type":"boolean","default":false},"seek":{"description":"The time (in seconds) from which the video should start playing.","type":"number","default":0},"autoplay":{"description":"Should the video play by default once loaded. NOTE: The video will be muted when initially playing when this is enabled.","type":"boolean","default":false},"playRate":{"description":"The speed at which the video will be played (where 1 is normal speed, .5 is half speed, 2 is double speed, etc.).","type":"number","default":1},"volume":{"description":"The percentage of maximum volume in use (from 0 to 100).","type":"number","default":75},"loop":{"description":"Should the video play continuously.","type":"boolean","default":false}}},"source":{"description":"The location of the video source.","type":"string","default":""},"controlStyle":{"visibleWhen":{"equals":false,"property":"liveFeed"},"description":"The styles to apply to the individual controls.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"liveFeed":{"description":"This should be set to true if the source of the video is a live camera feed.","type":"boolean","default":false},"autohideControls":{"visibleWhen":{"equals":false,"property":"liveFeed"},"description":"The visible state of the video controls. If set to true, controls will auto-hide when the cursor is not hovering the video.","type":"boolean","default":false},"style":{"description":"The styles to apply to the component.","default":{"classes":""},"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"poster":{"visibleWhen":{"equals":false,"property":"liveFeed"},"description":"The location of the poster image to use as the background while the video is loading and before it has been played.","type":"string","default":""},"status":{"visibleWhen":{"equals":false,"property":"liveFeed"},"type":"object","properties":{"paused":{"description":"True when playback has been paused.","type":"boolean","default":false},"waiting":{"description":"True when playback has stopped because of a temporary lack of data.","type":"boolean","default":false},"loadedData":{"description":"True when the current playback position of the media has finished loading; often the first frame.","type":"boolean","default":false},"seeked":{"description":"Number representing the time (in seconds) where the seek action was completed.","type":"number","default":0},"seeking":{"description":"True when a seek operation is in progress.","type":"boolean","default":false},"ended":{"description":"True when playback has stopped because the end of the media was reached.","type":"boolean","default":false},"progress":{"description":"Number representing the time (in seconds) where playback has occurred.","type":"number","default":0},"playing":{"description":"True when playback is ready to start after having been paused or delayed due to lack of data.","type":"boolean","default":false},"rateChanged":{"description":"Number representing the current playback rate (1 being normal speed).","type":"number","default":1}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"VideoPlayer","name":"Video Player","palette":{"variants":[{"tooltip":"Enables you to embed video or a live feed in a Perspective view.","label":"Video Player"}],"category":"display"},"id":"ia.display.video-player"}