---
name: ignition-perspective-skills
description: Master routing skill for all Ignition skills including Perspective views and Tag management. Use this to determine which skill(s) to load for your current task. Do NOT load all skills — only load the relevant ones.
---

# Ignition Perspective Skills

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

## Individual Skills (loaded via the skill tool)

Each of these has its own `SKILL.md` and is loaded directly by name.

### View Construction & Fundamentals
| Skill Name | When to Use |
|------------|-------------|
| `perspective-build-view` | Creating a new view from scratch |
| `perspective-default-configs` | Need default JSON for any component |
| `perspective-component-meta` | Setting component name/visibility/tooltip |
| `perspective-css-properties` | Styling any component |
| `perspective-container-child-position` | Positioning children in containers |
| `perspective-named-query` | Creating/modifying Named Queries |
| `perspective-docks` | Creating/configuring docks (headers, menus, sidebars) |

### Containers
| Skill Name | When to Use |
|------------|-------------|
| `perspective-flex-container` | Dynamic/responsive layouts |
| `perspective-column-container` | Screen-size-aware layouts |

### Display Components
| Skill Name | When to Use |
|------------|-------------|
| `perspective-label` | Displaying text |
| `perspective-table` | Tabular data display |
| `perspective-icon` | SVG icons |

### Input Components
| Skill Name | When to Use |
|------------|-------------|
| `perspective-text-field` | Single-line text input |
| `perspective-text-area` | Multi-line text input |
| `perspective-numeric-entry` | Numeric input |
| `perspective-dropdown` | Selection from list |
| `perspective-datetime-picker` | Full date/time picker |
| `perspective-checkbox` | Boolean/three-state |

### Button & Navigation Components
| Skill Name | When to Use |
|------------|-------------|
| `perspective-button` | Action button |

### Chart Components
| Skill Name | When to Use |
|------------|-------------|
| `perspective-time-series-chart` | Time-based data |
| `perspective-power-chart` | Advanced time-series |
| `perspective-xy-chart` | XY scatter/line/column |

### Bindings (Data Connections)
| Skill Name | When to Use |
|------------|-------------|
| `perspective-property-binding` | Connect to other components |
| `perspective-tag-binding` | Connect to Ignition tags |
| `perspective-expression-binding` | Calculate from expressions |
| `perspective-query-binding` | Connect to database |
| `perspective-tag-history-binding` | Historical tag data |

### Transforms (Data Manipulation)
| Skill Name | When to Use |
|------------|-------------|
| `perspective-expression-transform` | Calculate with expressions |
| `perspective-script-transform` | Calculate with Python |
| `perspective-format-transform` | Format display |
| `perspective-map-transform` | Map values to outputs |

### Ignition Tags (Gateway REST API)
| Skill Name | When to Use |
|------------|-------------|
| `ignition-tags` | Creating, importing, and exporting tags via REST API |

---

## Shared Category Skills (loaded via the skill tool, then read the specific file)

Each category folder has a single `SKILL.md` covering the remaining components. Load the category skill, then use the `Read` tool to open the specific component file it points to.

| Skill Name | Covers | File Location |
|------------|--------|---------------|
| `alarms` | Alarm Status Table, Alarm Journal Table | `alarms/` |
| `bindings` | HTTP Binding, Session Properties, Expression Structure Binding | `bindings/` |
| `buttons` | Horizontal Menu, Link, Multi-State Button, One-Shot Button | `buttons/` |
| `charts` | Pie Chart, Sparkline Chart, Chart Range Selector | `charts/` |
| `containers` | Accordion, Breakpoint, Carousel, Coordinate, Dashboard, Split, Tab, View Canvas | `containers/` |
| `display` | Audio, Barcode Display, File Upload, Image, Inline Frame, LED Display, Markdown, Menu Tree, PDF Viewer, Signature Pad, Tag Browse Tree, Tree, Video Player | `display/` |
| `embedded` | Embedded View, Flex Repeater | `embedded/` |
| `forms` | Form Configuration, Equipment Schedule | `forms/` |
| `fundamentals` | Create an Ignition Project, Stylesheet CSS | `fundamentals/` |
| `gauges` | Gauge, Simple Gauge, Thermometer, Linear Scale, Moving Analog Indicator, Progress Indicator | `gauges/` |
| `industrial` | Motor, Pump, Valve, Vessel, Sensor Symbol, Cylindrical Tank | `industrial/` |
| `input` | Barcode Scanner, DateTime Input, Google Map, Password Field, Radio Group, Slider, Toggle Switch | `input/` |

---

## Quick Task Reference

| Task | Load These Skills |
|------|-------------------|
| Create a new view | `perspective-build-view`, `perspective-default-configs` |
| Style a component | `perspective-css-properties` |
| Write stylesheet.css / CSS selectors | `fundamentals` (Perspective Stylesheet CSS) |
| Add a table with data | `perspective-table`, `perspective-tag-binding` or `perspective-query-binding` |
| Create a form | `forms`, relevant input skills |
| Display a chart | `perspective-time-series-chart` / `perspective-xy-chart` / `perspective-power-chart` |
| Show industrial graphics | `industrial` |
| Connect to tags | `perspective-tag-binding` |
| Connect to database | `perspective-query-binding` |
| Connect to API | `bindings` (Perspective HTTP Binding) |
| Transform data | `perspective-expression-transform` / `perspective-script-transform` |
| Build responsive layout | `perspective-flex-container`, `perspective-column-container` |
| Add navigation | `buttons` (Horizontal Menu, Link) |
| Create docks/navigation | `perspective-docks` |
| Embed sub-views | `embedded` |
| Display alarms | `alarms` |
| Create memory tags | `ignition-tags` |
| Create expression tags | `ignition-tags` |
| Create OPC tags from PLC | `ignition-tags` |
| Create SQL query tags | `ignition-tags` |
| Create tag folders | `ignition-tags` |
| Create UDT definitions | `ignition-tags` |
| Create UDT instances | `ignition-tags` |
| Bulk create tags | `ignition-tags` |
| Export existing tags | `ignition-tags` |
| Import tags | `ignition-tags` |

---

*This is the master skill — load only the specific skill(s) you need for your current task. For Perspective views, use the perspective-* skills. For tag management, use the ignition-tags skill.*
