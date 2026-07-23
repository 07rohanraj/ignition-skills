# Perspective Docks

**When to Use:** Creating, modifying, or understanding Docks in an Ignition Perspective project. This covers dock configuration in page-config, dock view structure, common patterns (Header, Menu, MenuBar), and how to implement navigation with docks.

---

## Overview

Docks are persistent UI panels that appear alongside the main page content. They are used for navigation headers, side menus, footers, and other persistent elements. Docks are defined in the page configuration and implemented as regular Perspective views.

---

## Dock Configuration

Docks are configured in `com.inductiveautomation.perspective/page-config/config.json` under the `sharedDocks` key (for global docks) or within individual page definitions (for page-specific docks).

### Shared Docks Structure

```json
{
  "pages": {
    "/page-route": {
      "title": "Page Title",
      "viewPath": "ViewPath/ViewName"
    }
  },
  "sharedDocks": {
    "cornerPriority": "left-right",
    "top": [],
    "left": [],
    "right": [],
    "bottom": []
  }
}
```

### Dock Configuration Object

Each dock entry in the array has this structure:

```json
{
  "anchor": "fixed",
  "autoBreakpoint": 480,
  "content": "push",
  "handle": "hide",
  "iconUrl": "",
  "id": "DockId",
  "modal": false,
  "resizable": false,
  "show": "visible",
  "size": 80,
  "viewParams": {},
  "viewPath": "Docks/DockViewName"
}
```

### Dock Properties Reference

| Property | Type | Values | Description |
|----------|------|--------|-------------|
| `anchor` | string | `"fixed"`, `"float"` | How dock is positioned |
| `autoBreakpoint` | number | pixels | Width to auto-hide on small screens |
| `content` | string | `"push"`, `"cover"`, `"overlay"` | How dock affects main content |
| `handle` | string | `"hide"`, `"none"`, `"autoHide"` | Show/hide handle |
| `iconUrl` | string | URL or `""` | Icon for collapsed dock |
| `id` | string | unique identifier | Used to open/close docks programmatically |
| `modal` | boolean | `true`, `false` | Whether dock blocks main content |
| `resizable` | boolean | `true`, `false` | Whether user can resize dock |
| `show` | string | `"visible"`, `"hidden"`, `"onDemand"` | Initial visibility |
| `size` | number | pixels | Dock width/height |
| `viewParams` | object | key-value pairs | Parameters passed to dock view |
| `viewPath` | string | view path | Path to dock view (relative to `views/`) |

### Corner Priority

The `cornerPriority` property determines which docks take precedence at corners:

```json
"cornerPriority": "left-right"  // Left docks take priority over top/bottom
"cornerPriority": "top-bottom"  // Top docks take priority over left/right
```

### Page-Specific Docks

Docks can be defined per-page instead of globally:

```json
{
  "pages": {
    "/special-page": {
      "title": "Special Page",
      "viewPath": "Pages/SpecialPage",
      "docks": {
        "top": [
          {
            "anchor": "fixed",
            "autoBreakpoint": 480,
            "content": "push",
            "handle": "hide",
            "iconUrl": "",
            "id": "specialHeader",
            "modal": false,
            "resizable": false,
            "show": "visible",
            "size": 80,
            "viewParams": {},
            "viewPath": "Docks/SpecialHeader"
          }
        ],
        "left": [],
        "right": [],
        "bottom": []
      }
    }
  }
}
```

---

## Dock View Structure

Dock views are regular Perspective views stored in the `views/Docks/` folder.

### Folder Structure

```
com.inductiveautomation.perspective/
└── views/
    └── Docks/
        ├── Header/
        │   ├── view.json
        │   ├── resource.json
        │   └── thumbnail.png
        ├── Menu/
        │   ├── view.json
        │   ├── resource.json
        │   └── thumbnail.png
        └── MenuBar/
            ├── MenuBar/
            │   ├── view.json
            │   ├── resource.json
            │   └── thumbnail.png
            └── SingleMenu/
                ├── view.json
                ├── resource.json
                └── thumbnail.png
```

### resource.json Structure

```json
{
  "scope": "G",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["view.json", "thumbnail.png"],
  "attributes": {
    "lastModification": {
      "actor": "admin",
      "timestamp": "2025-01-01T00:00:00Z"
    },
    "lastModificationSignature": "abc123..."
  }
}
```

---

## Common Dock Patterns

### 1. Header Dock (Top Navigation)

A header dock typically contains:
- Logo/branding
- Application title
- DateTime display
- User information
- Notification icons

**Basic Header Structure:**

```json
{
  "custom": {},
  "params": {},
  "props": {
    "defaultSize": {
      "height": 80,
      "width": 1200
    }
  },
  "root": {
    "children": [
      {
        "children": [
          {
            "meta": { "name": "logo" },
            "position": { "basis": "180px", "shrink": 0 },
            "props": {
              "fit": { "mode": "fill" },
              "source": "data:image/png;base64,..."
            },
            "type": "ia.display.image"
          },
          {
            "meta": { "name": "lblTitle" },
            "position": { "basis": "50px", "grow": 1 },
            "props": {
              "text": "Application Title",
              "textStyle": {
                "fontSize": "24px",
                "fontWeight": 600,
                "paddingLeft": "1rem"
              }
            },
            "type": "ia.display.label"
          }
        ],
        "meta": { "name": "fcLogo" },
        "position": { "basis": "306px", "shrink": 0 },
        "type": "ia.container.flex"
      },
      {
        "children": [
          {
            "meta": { "name": "lblDateTime" },
            "position": { "shrink": 0 },
            "propConfig": {
              "props.text": {
                "binding": {
                  "config": {
                    "tagPath": "[System]Client/System/CurrentDateTime"
                  },
                  "transforms": [
                    {
                      "formatType": "datetime",
                      "formatValue": "dd-MMM-YYYY hh:mm aaa",
                      "type": "format"
                    }
                  ],
                  "type": "tag"
                }
              }
            },
            "props": {
              "textStyle": { "textAlign": "right" }
            },
            "type": "ia.display.label"
          },
          {
            "meta": { "name": "User" },
            "position": { "basis": "30px", "shrink": 0 },
            "props": {
              "color": "var(--primary-color1)",
              "path": "material/account_circle"
            },
            "type": "ia.display.icon"
          }
        ],
        "meta": { "name": "fcIcons" },
        "position": { "basis": "200px", "grow": 1, "shrink": 0 },
        "props": { "justify": "flex-end" },
        "type": "ia.container.flex"
      }
    ],
    "meta": { "name": "root" },
    "props": {
      "justify": "space-between",
      "style": {
        "backgroundColor": "var(--primary-color4)",
        "borderBottom": "3px solid var(--primary-color1)"
      }
    },
    "type": "ia.container.flex"
  }
}
```

---

### 2. Menu Dock (Left Sidebar Icons)

A menu dock displays icons for navigation. When clicked, it navigates to a page and optionally opens an expanded menu.

**Basic Menu Structure:**

```json
{
  "custom": {},
  "params": {},
  "props": {
    "defaultSize": { "width": 80 }
  },
  "root": {
    "children": [
      {
        "events": {
          "dom": {
            "onClick": [
              {
                "config": { "page": "/target-page" },
                "scope": "C",
                "type": "nav"
              },
              {
                "config": { "id": "BigMenu", "type": "open" },
                "scope": "C",
                "type": "dock"
              }
            ]
          }
        },
        "meta": {
          "name": "MenuItem",
          "tooltip": {
            "enabled": true,
            "location": "center-right",
            "text": "Menu Item"
          }
        },
        "position": { "basis": "50px", "shrink": 0 },
        "props": {
          "fit": { "mode": "contain" },
          "source": "data:image/svg+xml;base64,..."
        },
        "type": "ia.display.image"
      },
      {
        "meta": { "name": "Label" },
        "position": { "basis": "420px" },
        "type": "ia.display.label"
      },
      {
        "events": {
          "dom": {
            "onClick": {
              "config": { "id": "BigMenu", "type": "open" },
              "scope": "C",
              "type": "dock"
            }
          }
        },
        "meta": { "name": "MenuIcon" },
        "position": { "basis": "40px", "shrink": 0 },
        "props": {
          "path": "material/dehaze",
          "style": { "cursor": "pointer" }
        },
        "type": "ia.display.icon"
      }
    ],
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": {
        "backgroundColor": "#FFFFFF",
        "borderRight": "2px solid #E5E7EB"
      }
    },
    "type": "ia.container.flex"
  }
}
```

---

### 3. MenuBar Dock (Expanded Menu)

A MenuBar dock displays categorized navigation with expandable sections. It typically uses a Flex Repeater component.

**Key Components:**
- Flex Repeater with menu categories
- Each category has a header (icon + label) and children (sub-items)
- Message handlers for selection state

**Basic MenuBar Structure:**

```json
{
  "custom": {},
  "events": {
    "system": {
      "onStartup": {
        "config": {
          "script": "self.getChild(\"root\").getChild(\"FlexRepeater\").props.instances[0].selected=False"
        },
        "scope": "G",
        "type": "script"
      }
    }
  },
  "params": {
    "display": true,
    "selected": ""
  },
  "propConfig": {
    "params.display": {
      "paramDirection": "input",
      "persistent": true
    },
    "params.selected": {
      "paramDirection": "input",
      "persistent": true
    }
  },
  "props": {
    "defaultSize": { "height": 1080, "width": 347 }
  },
  "root": {
    "children": [
      {
        "meta": { "name": "FlexRepeater" },
        "position": { "basis": "700px", "grow": 1 },
        "props": {
          "direction": "column",
          "elementPosition": { "basis": "auto", "grow": 0, "shrink": 0 },
          "instances": [
            {
              "child": [
                {
                  "display": true,
                  "instancePosition": {},
                  "instanceStyle": { "classes": "" },
                  "label": "Sub Item 1",
                  "nav": true,
                  "path": true,
                  "subSelect": false,
                  "target": "/page1"
                },
                {
                  "display": true,
                  "instancePosition": {},
                  "instanceStyle": { "classes": "" },
                  "label": "Sub Item 2",
                  "nav": true,
                  "path": true,
                  "subSelect": false,
                  "target": "/page2"
                }
              ],
              "display": true,
              "dropAvailable": true,
              "headerIcon": "data:image/svg+xml;base64,...",
              "headerLabel": "Category Name",
              "headerTarget": "",
              "instancePosition": {},
              "instanceStyle": { "classes": "" },
              "selected": false
            }
          ],
          "path": "Docks/MenuBar/SingleMenu",
          "useDefaultViewHeight": false,
          "useDefaultViewWidth": false
        },
        "scripts": {
          "customMethods": [],
          "extensionFunctions": null,
          "messageHandlers": [
            {
              "messageType": "unselect",
              "pageScope": true,
              "script": "selectedMenu = payload['selectMenu']\nfor item in self.props.instances:\n    for childItem in item['child']:\n        try:\n            childItem['subSelect'] = False\n        except:\n            continue\n    if item['headerLabel']!=selectedMenu:\n        item['selected'] = False\n    else:\n        if item['selected'] == True:\n            item['selected'] = False\n        else:\n            item['selected'] = True\n        system.perspective.openDock('mainDock')",
              "sessionScope": true,
              "viewScope": true
            }
          ]
        },
        "type": "ia.display.flex-repeater"
      },
      {
        "children": [
          {
            "meta": { "name": "MenuIcon" },
            "position": { "basis": "30px", "shrink": 0 },
            "props": {
              "color": "var(--primary-color1)",
              "path": "material/close"
            },
            "type": "ia.display.icon"
          },
          {
            "meta": { "name": "Label" },
            "position": { "basis": "140px", "shrink": 0 },
            "props": {
              "text": "Close Menu",
              "textStyle": { "fontSize": "18px", "fontWeight": "bold" }
            },
            "type": "ia.display.label"
          }
        ],
        "events": {
          "dom": {
            "onClick": {
              "config": { "id": "MinDock", "type": "open" },
              "scope": "C",
              "type": "dock"
            }
          }
        },
        "meta": { "name": "fcClose" },
        "position": { "shrink": 0 },
        "props": {
          "style": {
            "cursor": "pointer",
            "marginTop": "20px",
            "paddingLeft": "20px"
          }
        },
        "type": "ia.container.flex"
      }
    ],
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": {
        "backgroundColor": "var(--primary-color4)",
        "borderRight": "2px solid #E5E7EB"
      }
    },
    "type": "ia.container.flex"
  }
}
```

---

## Dock Events and Interactions

### Opening/Closing Docks

Use the `dock` event type to open, close, or toggle docks:

```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": {
          "id": "DockId",
          "type": "open"
        },
        "scope": "C",
        "type": "dock"
      }
    }
  }
}
```

**Dock Event Types:**

| Type | Description |
|------|-------------|
| `"open"` | Opens the specified dock |
| `"close"` | Closes the specified dock |
| `"toggle"` | Toggles dock open/close state |

**Example: Toggle between two docks:**

```json
{
  "events": {
    "dom": {
      "onClick": [
        {
          "config": { "id": "minDock", "type": "close" },
          "scope": "C",
          "type": "dock"
        },
        {
          "config": { "id": "maxDock", "type": "open" },
          "scope": "C",
          "type": "dock"
        }
      ]
    }
  }
}
```

### Page Navigation

Use the `nav` event type to navigate to pages:

```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": {
          "page": "/target-page"
        },
        "scope": "C",
        "type": "nav"
      }
    }
  }
}
```

### Script Execution

Use the `script` event type for custom logic:

```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": {
          "script": "system.perspective.sendMessage('selection', {'selected': True})"
        },
        "scope": "G",
        "type": "script"
      }
    }
  }
}
```

### Popup Windows

Use the `popup` event type for user popups:

```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": {
          "draggable": false,
          "id": "PopupId",
          "modal": true,
          "overlayDismiss": true,
          "position": { "relativeLocation": "bottom" },
          "positionType": "relative",
          "resizable": false,
          "showCloseIcon": false,
          "type": "toggle",
          "viewParams": { "UserName": "{session.custom.UserName}" },
          "viewPath": "Templates/UserLogin/SignOut",
          "viewportBound": true
        },
        "scope": "C",
        "type": "popup"
      }
    }
  }
}
```

---

## Message Handlers

Message handlers allow docks to communicate with each other and respond to events.

### Defining Message Handlers

```json
{
  "scripts": {
    "customMethods": [],
    "extensionFunctions": null,
    "messageHandlers": [
      {
        "messageType": "messageName",
        "pageScope": true,
        "script": "self.view.custom.property = payload['key']",
        "sessionScope": false,
        "viewScope": false
      }
    ]
  }
}
```

### Sending Messages

```python
# From a script event
system.perspective.sendMessage("messageName", {"key": "value"})
```

### Common Message Patterns

**Selection State Management:**

```python
# Unselect message handler
selectedMenu = payload['selectMenu']
for item in self.props.instances:
    for childItem in item['child']:
        try:
            childItem['subSelect'] = False
        except:
            continue
    if item['headerLabel'] != selectedMenu:
        item['selected'] = False
    else:
        if item['selected'] == True:
            item['selected'] = False
        else:
            item['selected'] = True
    system.perspective.openDock('maxDock')
```

---

## Flex Repeater for Menu Items

The Flex Repeater component (`ia.display.flex-repeater`) is commonly used for dynamic menu items.

### Instance Properties

Each instance in the Flex Repeater has:

```json
{
  "child": [
    {
      "display": true,
      "instancePosition": {},
      "instanceStyle": { "classes": "" },
      "label": "Sub Item Label",
      "nav": true,
      "path": true,
      "subSelect": false,
      "target": "/page-route"
    }
  ],
  "display": true,
  "dropAvailable": true,
  "headerIcon": "data:image/svg+xml;base64,...",
  "headerLabel": "Category Label",
  "headerTarget": "",
  "instancePosition": {},
  "instanceStyle": { "classes": "" },
  "selected": false
}
```

### SingleMenu View

The SingleMenu view is a child view that renders each menu category. It typically contains:
- A header container with icon and label
- A list of sub-items that expand when selected

---

## Best Practices

1. **Use Unique IDs**: Every dock must have a unique `id` for programmatic access.

2. **Organize Dock Views**: Keep dock views in a `Docks/` folder under `views/`.

3. **Consistent Styling**: Use CSS variables for consistent theming across docks.

4. **Responsive Design**: Set appropriate `autoBreakpoint` values for mobile responsiveness.

5. **Message Handling**: Use message handlers for dock-to-dock communication.

6. **Thumbnail Images**: Include `thumbnail.png` files for visual identification in the Designer.

7. **Default Sizes**: Set reasonable `defaultSize` values in dock views for proper rendering.

---

## Complete Example: Two-Dock Navigation System

This example shows a complete two-dock navigation system with a collapsed menu (icons) and expanded menu (categories).

### config.json

```json
{
  "pages": {
    "/": { "title": "Home", "viewPath": "Pages/Dashboard" },
    "/page1": { "title": "Page 1", "viewPath": "Pages/Page1" },
    "/page2": { "title": "Page 2", "viewPath": "Pages/Page2" }
  },
  "sharedDocks": {
    "cornerPriority": "left-right",
    "left": [
      {
        "anchor": "fixed",
        "autoBreakpoint": 480,
        "content": "cover",
        "handle": "hide",
        "iconUrl": "",
        "id": "minDock",
        "modal": false,
        "resizable": false,
        "show": "visible",
        "size": 80,
        "viewParams": {},
        "viewPath": "Docks/Menu"
      },
      {
        "anchor": "fixed",
        "autoBreakpoint": 480,
        "content": "cover",
        "handle": "hide",
        "iconUrl": "",
        "id": "maxDock",
        "modal": false,
        "resizable": false,
        "show": "onDemand",
        "size": 250,
        "viewParams": {},
        "viewPath": "Docks/MenuBar/MenuBar"
      }
    ],
    "top": [
      {
        "anchor": "fixed",
        "autoBreakpoint": 480,
        "content": "push",
        "handle": "hide",
        "iconUrl": "",
        "id": "",
        "modal": false,
        "resizable": false,
        "show": "visible",
        "size": 80,
        "viewParams": {},
        "viewPath": "Docks/Header"
      }
    ]
  }
}
```

### Menu Dock View (views/Docks/Menu/view.json)

```json
{
  "custom": {},
  "params": {},
  "props": {
    "defaultSize": { "width": 80 }
  },
  "root": {
    "children": [
      {
        "events": {
          "dom": {
            "onClick": [
              { "config": { "page": "/" }, "scope": "C", "type": "nav" },
              { "config": { "id": "maxDock", "type": "open" }, "scope": "C", "type": "dock" }
            ]
          }
        },
        "meta": { "name": "Home", "tooltip": { "enabled": true, "text": "Home" } },
        "position": { "basis": "50px", "shrink": 0 },
        "props": {
          "fit": { "mode": "contain" },
          "source": "data:image/svg+xml;base64,..."
        },
        "type": "ia.display.image"
      },
      {
        "events": {
          "dom": {
            "onClick": [
              { "config": { "page": "/page1" }, "scope": "C", "type": "nav" },
              { "config": { "id": "maxDock", "type": "open" }, "scope": "C", "type": "dock" }
            ]
          }
        },
        "meta": { "name": "Page 1", "tooltip": { "enabled": true, "text": "Page 1" } },
        "position": { "basis": "50px", "shrink": 0 },
        "props": {
          "fit": { "mode": "contain" },
          "source": "data:image/svg+xml;base64,..."
        },
        "type": "ia.display.image"
      }
    ],
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": {
        "backgroundColor": "#FFFFFF",
        "borderRight": "2px solid #E5E7EB"
      }
    },
    "type": "ia.container.flex"
  }
}
```

---

## References

- `How to create an Ignition Project.md` - Project structure overview
- `Perspective Flex Container.md` - Container layout
- `Perspective Flex Repeater Component.md` - Dynamic component repetition
- `Perspective Horizontal Menu Component.md` - Alternative menu implementation
- `Perspective Link Component.md` - Navigation links
- `Perspective Expression Binding.md` - Dynamic property binding
- `Perspective Script Transform.md` - Data transformation
