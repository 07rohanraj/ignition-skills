# Perspective Carousel Container

## Description

These instructions detail the usage and configuration of the Perspective Carousel component, which displays a series of Views as a cycling slideshow. The document explains how to define slides, configure automatic playback, and customize the component's visual appearance and interactive behavior, including navigation controls and transition effects.

## Documentation

# Instructions
This document provides instructions for using and configuring the Perspective Carousel component in Ignition.

## Object Name
Perspective Carousel Container

### Description
The Perspective Carousel Container is a component that displays one or more Views as "slides" in a continuous loop. It can be configured to cycle through these slides automatically at a set interval or allow users to navigate them manually using arrows and dots. It is found in the "Embedding" category of the Perspective Component Palette.

### Instructions

#### Basic Configuration
The core of the Carousel is the `views` property, which is an array of objects. Each object in this array defines a slide to be displayed.

To add slides to the Carousel, you must add objects to the `views` array. Each object must have a `viewPath` property, which is a string specifying the path to the View you want to display for that slide.

**Example `views` configuration:**
```json
[
  {
    "viewPath": "path/to/my/FirstView"
  },
  {
    "viewPath": "path/to/my/SecondView"
  }
]
```

#### Slide View Configuration
For each slide object within the `views` array, you can configure the following properties:
*   **`viewPath`**: (Required) The path to the View to be rendered in the slide.
*   **`viewParams`**: An object containing parameters to pass to the View. The keys in this object must match the names of the parameters defined on the target View itself.
*   **Layout Properties**: These properties control the positioning of the View within the slide's container.
    *   **`direction`**: The layout direction of the child components. Can be 'row' (default) or 'column'.
    *   **`justify`**: Adjusts the View's placement along the main axis. Can be 'flex-start' (default), 'flex-end', or 'center'.
    *   **`alignItems`**: Adjusts the View's placement along the cross axis. Can be 'flex-start' (default), 'flex-end', or 'center'.

#### Autoplay
To make the Carousel cycle through slides automatically, configure the `autoplay` properties:
*   **`autoplay.enabled`**: Set to `true` to enable automatic scrolling.
*   **`autoplay.transitionDelay`**: The time in milliseconds (ms) between slide transitions. The default is 2500ms.
*   You can also configure the Carousel to pause when the user interacts with it:
    *   **`autoplay.pauseOnHover`**: Pauses when the user's mouse is over a slide.
    *   **`autoplay.pauseOnDotHover`**: Pauses when the user's mouse is over a navigation dot.
    *   **`autoplay.pauseOnFocus`**: Pauses when the Carousel is in focus.

#### Appearance
You can customize the look and feel of the Carousel using the `appearance` properties.
*   **`slidesToShow`**: Sets the number of slides to display at one time on the carousel page. Defaults to 1. This property is only available when `behavior.fade` is set to `false`.
*   **`slidePadding`**: The amount of padding, in pixels, between slides. Defaults to 20.
*   **`reverse`**: Set to `true` to reverse the order of the slides.
*   **`useDefaultViewWidth` / `useDefaultViewHeight`**: If `true`, the carousel will use the default width/height of the embedded view instead of dynamically adjusting it based on available space.

**Navigation Elements (Arrows and Dots):**
*   **Arrows (`appearance.arrows`)**:
    *   **`enabled`**: Set to `true` to show the 'previous' and 'next' navigation arrows.
    *   **`iconPath`**: You can provide a path to a custom icon for the `next` and `previous` arrows.
    *   **`fillColor`**: Sets the color of the arrow icons.
    *   **`style`**: Apply additional CSS styles to the arrows.
*   **Dots (`appearance.dots`)**:
    *   **`enabled`**: Set to `true` to show the navigation dots at the bottom of the component.
    *   **`iconPath`**: Provide a path to a custom icon to be used for the dots.
    *   **`styles`**: Configure the appearance of the dots for active and inactive states.
        *   `active.fillColor`: The color of the dot for the currently displayed slide.
        *   `inactive.fillColor`: The color of the dots for all other slides.

#### Behavior
Control the interaction and transition behavior using the `behavior` properties.
*   **`activePane`**: A numeric, 0-based index that determines which slide is currently active. This can be read to find the current slide or written to change the slide.
*   **`transitionSpeed`**: The speed of the animation in milliseconds (ms) when transitioning between slides. Default is 500ms.
*   **`fade`**: Set to `true` to make slides fade in and out instead of sliding. Note that setting this to `true` disables the `slidesToShow` property.
*   **`desktopDraggable`**: If `true`, users on a desktop can change slides by clicking and dragging.
*   **`mobileSwipeable`**: If `true`, users on a mobile device can change slides by swiping.
*   **`swipeThreshold`**: The maximum pixel distance a user can drag before a slide transition is initiated. The minimum value is 50. The actual threshold will be the lesser of this value or half the width of the slide pane.

#### Other Properties
*   **`lazyLoad`**: When `true` (the default), views are loaded progressively or on-demand as they are needed, which can improve performance.

### Helpful Tips
*   **Performance:** For best performance, avoid embedding performance-intensive components like the Video Player or Map component within a Carousel.
*   **Nested Carousels:** Avoid embedding a View that contains a Carousel inside another Carousel, as this can be confusing for the user.
*   **iFrames:** Avoid embedding Views that contain iFrame components. Content within an iFrame can steal focus from other components and negatively impact performance.
*   **Drag Transition Limitations:** The "swipe" or drag-to-transition feature only works if the Carousel component has a standard rotation (0, 90, 180, or 270 degrees). If the component is rotated to any other angle, drag transitions will be disabled.
*   **Fade vs. `slidesToShow`**: The `appearance.slidesToShow` property, which allows multiple slides to be visible at once, only works when `behavior.fade` is `false`. If `fade` is `true`, only one slide will be shown at a time.
*   **`activePane` Index**: The `activePane` property is a 0-based index that corresponds to the order of the slide objects in the `views` array.
*   **Delay vs. Speed**: `autoplay.transitionDelay` is the time the carousel *waits* on a slide before automatically moving to the next one. `behavior.transitionSpeed` is the duration of the *animation* when changing slides.
*   **View Parameters**: When using the `viewParams` property for a slide, ensure the parameter names you provide exactly match the parameter names defined within the target View specified in `viewPath`.

# Schema - raw
{"schema":{"description":"A component which displays one or more Views as slides in a loop, optionally in automated fashion.","type":"object","title":"Carousel","additionalProperties":false,"properties":{"lazyLoad":{"description":"Load views on demand or progressively.","type":"boolean","default":true},"autoplay":{"type":"object","title":"Auto Play","properties":{"pauseOnDotHover":{"description":"Pause autoplay on dot mouse over.","type":"boolean","title":"Pause on Dot Hover","default":false},"enabled":{"description":"If true, the carousel will automatically scroll through the views according to the transitionDelay.","type":"boolean","default":false},"transitionDelay":{"description":"Delay (in ms) at which slides scroll through the carousel when autoplay is true.","type":"number","title":"Transition Delay","default":2500},"pauseOnHover":{"description":"Pause autoplay on mouse over.","type":"boolean","title":"Pause on Hover","default":false},"pauseOnFocus":{"description":"Pause autoplay on focus.","type":"boolean","title":"Pause on Focus","default":false}}},"appearance":{"description":"Appearance related carousel options.","type":"object","title":"Appearance","properties":{"slidePadding":{"description":"Applies padding between slides.","type":"number","title":"Slide Padding","default":20},"dots":{"description":"Carousel dots configuration.","type":"object","title":"Dots","properties":{"enabled":{"description":"Enable dots.","type":"boolean","default":true},"styles":{"description":"Configure active and inactive styles for the dot icon.","type":"object","title":"Dot Styles","properties":{"active":{"description":"Styles to apply when the dot icon is active.","type":"object","properties":{"fillColor":{"format":"color","description":"The active icon color or fill, enabled when the current slide's index matches the dot's index.","type":"string","default":"#51BAFC"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}},"inactive":{"description":"Styles to apply when the dot icon is inactive.","type":"object","properties":{"fillColor":{"format":"color","description":"The inactive icon color or fill, enabled when the current slide's index does not match the dot's index.","type":"string","default":"#E2E4E6"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"}}}}},"iconPath":{"description":"Path to an icon that will be used if provided.","type":"string","default":""}}},"arrows":{"description":"Carousel arrows configuration.","type":"object","title":"Arrows","properties":{"next":{"description":"Next arrow icon configuration.","type":"object","properties":{"fillColor":{"format":"color","description":"Fill color to apply to icon.","type":"string","default":"#51BAFC"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"iconPath":{"description":"Path to an icon that will be used for the next arrow if provided.","type":"string","default":""}}},"previous":{"description":"Previous arrow icon configuration.","type":"object","properties":{"fillColor":{"format":"color","description":"Fill color to apply to icon.","type":"string","default":"#51BAFC"},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"iconPath":{"description":"Path to an icon that will be used for the previous arrow if provided.","type":"string","default":""}}},"enabled":{"description":"Enable arrows.","type":"boolean","default":true}}},"useDefaultViewWidth":{"description":"Enables the use of view default width instead of dynamically adjusting based on the available width.","type":"boolean","default":false},"reverse":{"description":"Reverses the slide order.","type":"boolean","title":"Reverse","default":false},"useDefaultViewHeight":{"description":"Enables the use of view default height instead of dynamically adjusting based on the available height.","type":"boolean","default":false},"slidesToShow":{"visibleWhen":{"equals":false,"property":"../behavior/fade"},"description":"Number of slides to show on each carousel page.","type":"number","title":"Slides to Show","default":1}}},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"activePane":{"description":"Active pane being displayed.","type":"number","default":0},"behavior":{"description":"Behavior and interaction related carousel options.","type":"object","title":"Behavior","properties":{"transitionSpeed":{"description":"The speed (in ms) at which the carousel transitions between slides.","type":"number","title":"Transition Speed","default":500},"mobileSwipeable":{"description":"Enables swiping on mobile to change slides.","type":"boolean","title":"Mobile Swipeable","default":true},"fade":{"description":"Enables slides to fade in and out of view on transition.","type":"boolean","title":"Fade","default":false},"swipeThreshold":{"description":"The maximum length of a drag, in pixels, to allow before initiating a slide transition.  Minimum of 50 pixels. Actual threshold will be either the provided value, or half the width of the slide pane, whichever is smaller.","type":"number","title":"Swipe threshold","default":200,"min":50},"desktopDraggable":{"description":"Enables scrolling via drag on desktop.","type":"boolean","title":"Desktop Draggable","default":true}}},"views":{"title":"Views","type":"array","items":{"type":"object","required":["viewPath"],"additionalProperties":false,"properties":{"alignItems":{"description":"Adjusts placement of view along the cross axis.","type":"string","enum":["flex-start","flex-end","center"],"default":"flex-start"},"viewPath":{"format":"view-path","description":"The path of the view to render in the carousel.","type":"string","title":"View Path","default":""},"justify":{"description":"Adjusts placement of view along the main axis.","type":"string","enum":["flex-start","flex-end","center"],"default":"flex-start"},"viewParams":{"extension":{"view-params":{"path":"../viewPath"}},"description":"Parameters for the view. If passing parameters into the embedded view, the names here must match the parameters on that view.","type":"object","title":"View Parameters","default":{}},"direction":{"description":"Direction of child layout.","type":"string","enum":["row","column"],"default":"row"}}}}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"Carousel","name":"Carousel","palette":{"variants":[{"tooltip":"Enables you to cycle through a selection of views at a defined rate.","label":"Carousel"}],"category":"embedding"},"id":"ia.display.carousel"}