---
name: perspective-master
description: Master routing skill for all 85 Ignition Perspective skills. Use this to determine which skill(s) to load for your current task. Do NOT load all skills — only load the relevant ones.
---

# Perspective Master Skill

---

## CRITICAL RULES — READ BEFORE PROCEEDING

1. **NEVER invent component types, property names, or JSON schemas.** Every component type (e.g., `ia.display.label`, `ia.container.flex`) and every property must come directly from the skill documentation loaded from this package.

2. **NEVER create your own schema or guess property structures.** If a skill file is not loaded, do not attempt to construct the component from memory or assumptions. Load the relevant skill first.

3. **ALWAYS load the relevant skill(s) before generating any Perspective JSON.** The skill files contain the authoritative property definitions, valid enum values, and correct default values.

4. **If unsure which skill to use, consult the category tables below or use the Quick Task Reference at the bottom.**

---

## How to Use
1. Identify what you're building/modifying
2. Find the matching category and skill(s) below
3. Load ONLY the relevant skill(s) using the skill tool
4. Follow that skill's instructions strictly — use only the properties and values documented there

---

## View Construction & Fundamentals
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-build-view` | Creating a new view from scratch | `fundamentals/How to build a new Perspective View.md` |
| `perspective-default-configs` | Need default JSON for any component | `fundamentals/Perspective Default Component JSON Configs.md` |
| `perspective-component-meta` | Setting component name/visibility/tooltip | `fundamentals/Perspective Component Meta Properties.md` |
| `perspective-css-properties` | Styling any component | `fundamentals/Perspective CSS Properties.md` |
| `perspective-container-child-position` | Positioning children in containers | `fundamentals/Perspective Container - Child Item Position Properties.md` |
| `perspective-create-project` | Creating a new Ignition project | `fundamentals/How to create an Ignition Project.md` |
| `perspective-named-query` | Creating/modifying Named Queries | `fundamentals/Ignition Named Query.md` |

---

## Containers
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-flex-container` | Dynamic/responsive layouts | `containers/Perspective Flex Container.md` |
| `perspective-column-container` | Screen-size-aware layouts | `containers/Perspective Column Container.md` |
| `perspective-coordinate-container` | Pixel-perfect positioning | `containers/Perspective Coordinate Container.md` |
| `perspective-breakpoint-container` | Responsive view switching | `containers/Perspective Breakpoint Container.md` |
| `perspective-split-container` | Two-panel resizable layout | `containers/Perspective Split Container.md` |
| `perspective-tab-container` | Tabbed content | `containers/Perspective Tab Container.md` |
| `perspective-carousel-container` | Slideshow/cycling views | `containers/Perspective Carousel Container.md` |
| `perspective-dashboard` | User-arrangeable widgets | `containers/Perspective Dashboard Component.md` |
| `perspective-accordion` | Collapsible sections | `containers/Perspective Accordion Component.md` |
| `perspective-view-canvas` | Coordinate-based multi-view | `containers/Perspective View Canvas Component.md` |

---

## Display Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-label` | Displaying text | `display/Perspective Label Component.md` |
| `perspective-markdown` | Rich text rendering | `display/Perspective Markdown Component.md` |
| `perspective-icon` | SVG icons | `display/Perspective Icon Component.md` |
| `perspective-image` | Displaying images | `display/Perspective Image Component.md` |
| `perspective-led-display` | LED-style readouts | `display/Perspective LED Display Component.md` |
| `perspective-table` | Tabular data display | `display/Perspective Table Component.md` |
| `perspective-tree` | Hierarchical data | `display/Perspective Tree Component.md` |
| `perspective-menu-tree` | Navigation menus | `display/Perspective Menu Tree Component.md` |
| `perspective-tag-browse-tree` | Tag browsing | `display/Perspective Tag Browse Tree Component.md` |
| `perspective-inline-frame` | External web content | `display/Perspective Inline Frame Component.md` |
| `perspective-pdf-viewer` | PDF display | `display/Perspective PDF Viewer Component.md` |
| `perspective-video-player` | Video playback | `display/Perspective Video Player Component.md` |
| `perspective-audio` | Audio playback | `display/Perspective Audio Component.md` |
| `perspective-barcode-display` | Barcode/QR display | `display/Perspective Barcode Display Component.md` |
| `perspective-signature-pad` | Signature capture | `display/Perspective Signature Pad Component.md` |
| `perspective-file-upload` | File upload | `display/Perspective File Upload Component.md` |

---

## Input Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-text-field` | Single-line text input | `input/Perspective Text Field Component.md` |
| `perspective-text-area` | Multi-line text input | `input/Perspective Text Area Component.md` |
| `perspective-numeric-entry` | Numeric input | `input/Perspective Numeric Entry Field Component.md` |
| `perspective-password-field` | Password input | `input/Perspective Password Field Component.md` |
| `perspective-dropdown` | Selection from list | `input/Perspective Dropdown Component.md` |
| `perspective-checkbox` | Boolean/three-state | `input/Perspective Checkbox Component.md` |
| `perspective-radio-group` | Single selection from options | `input/Perspective Radio Group Component.md` |
| `perspective-toggle-switch` | On/off toggle | `input/Perspective Toggle Switch Component.md` |
| `perspective-slider` | Range value selection | `input/Perspective Slider Component.md` |
| `perspective-datetime-input` | Date/time selection | `input/Perspective DateTime Input Component.md` |
| `perspective-datetime-picker` | Full date/time picker | `input/Perspective DateTime Picker Component.md` |
| `perspective-barcode-scanner` | Barcode scanning | `input/Perspective Barcode Scanner Input Component.md` |
| `perspective-google-map` | Geographic display | `input/Perspective Google Map Component.md` |

---

## Button & Navigation Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-button` | Action button | `buttons/Perspective Button Component.md` |
| `perspective-one-shot-button` | Single-trigger button | `buttons/Perspective One-Shot Button Component.md` |
| `perspective-multi-state-button` | Equipment mode control | `buttons/Perspective Multi-State Button Component.md` |
| `perspective-horizontal-menu` | Top navigation | `buttons/Perspective Horizontal Menu Component.md` |
| `perspective-link` | Hyperlink | `buttons/Perspective Link Component.md` |

---

## Gauge & Indicator Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-gauge` | Dial/arc value display | `gauges/Perspective Gauge Component.md` |
| `perspective-simple-gauge` | Modern arc gauge | `gauges/Perspective Simple Gauge Component.md` |
| `perspective-thermometer` | Temperature display | `gauges/Perspective Thermometer Component.md` |
| `perspective-linear-scale` | Linear axis display | `gauges/Perspective Linear Scale Component.md` |
| `perspective-moving-analog` | Colored scale indicator | `gauges/Perspective Moving Analog Indicator.md` |
| `perspective-progress-indicator` | Progress bar | `gauges/Perspective Progress Indicator Component.md` |

---

## Chart Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-time-series-chart` | Time-based data | `charts/Perspective Time Series Chart Component.md` |
| `perspective-power-chart` | Advanced time-series | `charts/Perspective Power Chart Component.md` |
| `perspective-pie-chart` | Proportional data | `charts/Perspective Pie Chart Component.md` |
| `perspective-xy-chart` | XY scatter/line/column | `charts/Perspective XY Chart Component.md` |
| `perspective-sparkline-chart` | Compact trend | `charts/Perspective Sparkline Chart Component.md` |
| `perspective-chart-range-selector` | Time range selection | `charts/Perspective Chart Range Selector Component.md` |

---

## Industrial Symbol Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-motor-symbol` | Motor visualization | `industrial/Perspective Motor Symbol Component.md` |
| `perspective-pump-symbol` | Pump visualization | `industrial/Perspective Pump Symbol Component.md` |
| `perspective-valve-symbol` | Valve visualization | `industrial/Perspective Valve Symbol Component.md` |
| `perspective-vessel-symbol` | Tank/vessel visualization | `industrial/Perspective Vessel Symbol Component.md` |
| `perspective-sensor-symbol` | Sensor visualization | `industrial/Perspective Sensor Symbol Component.md` |
| `perspective-cylindrical-tank` | 3D tank fill | `industrial/Perspective Cylindrical Tank Component.md` |

---

## Alarm Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-alarm-status-table` | Real-time alarms | `alarms/Perspective Alarm Status Table Component.md` |
| `perspective-alarm-journal-table` | Historical alarms | `alarms/Perspective Alarm Journal Table Component.md` |

---

## Form & Schedule Components
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-form-config` | Building forms | `forms/Perspective Form Component Property Configuration.md` |
| `perspective-equipment-schedule` | Time-based scheduling | `forms/Perspective Equipment Schedule Component.md` |

---

## Embedded Views & Repeaters
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-embedded-view` | Including sub-views | `embedded/Perspective Embedded View Component.md` |
| `perspective-flex-repeater` | Repeating templates | `embedded/Perspective Flex Repeater Component.md` |

---

## Bindings (Data Connections)
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-property-binding` | Connect to other components | `bindings/Perspective Property Binding.md` |
| `perspective-tag-binding` | Connect to Ignition tags | `bindings/Perspective Tag Binding.md` |
| `perspective-expression-binding` | Calculate from expressions | `bindings/Perspective Expression Binding.md` |
| `perspective-expression-structure-binding` | Build object from expressions | `bindings/Perspective Expression Structure Binding.md` |
| `perspective-query-binding` | Connect to database | `bindings/Perspective Query Binding.md` |
| `perspective-http-binding` | Connect to REST APIs | `bindings/Perspective HTTP Binding.md` |
| `perspective-tag-history-binding` | Historical tag data | `bindings/Perspective Tag History Binding.md` |
| `perspective-session-properties` | Access session/user info | `bindings/Perspective Session Properties.md` |

---

## Transforms (Data Manipulation)
| Skill ID | When to Use | File Path |
|----------|-------------|-----------|
| `perspective-expression-transform` | Calculate with expressions | `transforms/Perspective Expression Transform.md` |
| `perspective-script-transform` | Calculate with Python | `transforms/Perspective Script Transform.md` |
| `perspective-format-transform` | Format display | `transforms/Perspective Format Transform.md` |
| `perspective-map-transform` | Map values to outputs | `transforms/Perspective Map Transform.md` |

---

## Quick Task Reference

| Task | Load These Skills |
|------|-------------------|
| Create a new view | `perspective-build-view`, `perspective-default-configs` |
| Style a component | `perspective-css-properties` |
| Add a table with data | `perspective-table`, `perspective-tag-binding` or `perspective-query-binding` |
| Create a form | `perspective-form-config`, relevant input skills |
| Display a chart | `perspective-time-series-chart` / `perspective-pie-chart` / `perspective-xy-chart` |
| Show industrial graphics | `perspective-motor-symbol` / `perspective-pump-symbol` / `perspective-valve-symbol` etc. |
| Connect to tags | `perspective-tag-binding` |
| Connect to database | `perspective-query-binding` |
| Connect to API | `perspective-http-binding` |
| Transform data | `perspective-expression-transform` / `perspective-script-transform` |
| Build responsive layout | `perspective-flex-container`, `perspective-column-container` |
| Add navigation | `perspective-horizontal-menu`, `perspective-link`, `perspective-menu-tree` |
| Embed sub-views | `perspective-embedded-view`, `perspective-flex-repeater` |
| Display alarms | `perspective-alarm-status-table` / `perspective-alarm-journal-table` |

---

*This is the master skill — load only the specific skill(s) you need for your current task.*
