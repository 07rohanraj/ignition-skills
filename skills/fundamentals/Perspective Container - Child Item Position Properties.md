# Perspective Container - Child Item Position Properties

## Description

This set of instructions provides an overview of position properties for child items placed within the various container types.

## Documentation

All child items will have a 'position' property as part of its root schema (alongside 'props', 'custom', 'meta', etc).
{
  /* 1. Breakpoint Container ------------------------------------- */
  "BreakpointChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {
      "size": "small"                                   // string: "small" | "large"
    },
    "props": { /* component specific properties */ }
  },

  /* 2. Coordinate Container -------------------------------------- */
  "CoordinateChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {
      "x": 100,                                         // number (pixels or 0‑1 if mode:"percent")
      "y": 50,                                          // number
      "width": 200,                                     // number
      "height": 150,                                    // number
      "rotate": {                                       // object (optional)
        "angle": 45,                                    // number (degrees)
        "anchor": "center"                              // string: "top-left" | "top-right" | ... | "center"
      }
    },
    "props": { /* component specific properties */ }
  },

  /* 3. Split Container ------------------------------------------- */
  "SplitChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {
      "position": "left"                                    // string: for horizontal mode "left" | "right" OR for vertical mode "top" | "bottom"
    },
    "props": { /* component specific properties */ }
  },

  /* 4. Flex Container --------------------------------------------- */
  "FlexChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {
      "basis": "200px",                                 // string (size) or number (px)
      "grow": 1,                                       // number
      "shrink": 1,                                     // number
      "align": "center",                               // string: "start" | "center" | "end" | "stretch"
      "display": true                                   // boolean (true = show, false = hide)
    },
    "props": { /* component specific properties */ }
  },

  /* 5. Tab Container ---------------------------------------------- */
  "TabChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {
      "tabIndex": 0                                     // number (zero‑based index)
    },
    "props": { /* component specific properties */ }
  },

  /* 6. Column Container -------------------------------------------- */
  "ColumnChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {
      "height": "auto",                                 // string: "auto" or number (px)
      "breakpoints": [                                 // array – one entry per breakpoint
        {
          "name": "small",                             // string (must match a breakpoint defined on the parent)
          "span": 6,                                  // number (1‑12)
          "rowIndex": 0,                              // number
          "colIndex": 0,                              // number (0‑11)
          "order": 1                                  // number (visual order within the row)
        }
      ]
    },
    "props": { /* component specific properties */ }
  },

  /* 7. Carousel Container ------------------------------------------ */
  "CarouselChild": {
    "meta": { "name": "SomeComponent" },                 // string
    "position": {},                                     // no position – slides are configured in the parent
    "props": { /* component specific properties */ }
  }
}