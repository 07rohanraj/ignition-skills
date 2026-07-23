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
- Logo/branding (with click event for navigation)
- Application title
- DateTime display
- User information
- Notification icons
- **Hamburger menu icon** (opens/toggles side menu)

**Custom Properties:**
```json
{
  "custom": {
    "desktop": true,       // Desktop mode flag
    "display": "visible"   // Display state: "visible" or "hidden"
  }
}
```

**Event Flow:**
1. Logo click → Script checks `desktop` flag → Toggles `display` → Navigates to page
2. Hamburger click → `dock` event opens/toggles side menu

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

### 2. Menu Dock (Side Navigation)

**Default Configuration:**
- **Position:** Left side of screen
- **Anchor:** `fixed`
- **Size:** `{"width": 80}` (collapsed), expands to `200` on hover
- **Handles:** `left: "show"`, others: `"hide"`
- **Modal:** `false` (allows interaction with main content)
- **View Path:** `Docks/Menu`

**Custom Properties:**
```json
{
  "custom": {
    "expanded": false   // Controls label visibility
  }
}
```

**Hover Expand/Collapse Behavior:**

The menu uses `onMouseOver` and `onMouseOut` events on the root container to expand/collapse:

```json
{
  "events": {
    "dom": {
      "onMouseOver": [
        {
          "config": {
            "anchor": "fixed",
            "autoBreakpoint": 480,
            "content": "cover",
            "display": "visible",
            "handle": "hide",
            "id": "deskMenu",
            "modal": false,
            "size": 200,
            "view": "Docks/Menu"
          },
          "scope": "C",
          "type": "alter-dock"
        },
        {
          "config": {
            "script": "\tself.view.custom.expanded = True"
          },
          "scope": "G",
          "type": "script"
        }
      ],
      "onMouseOut": [
        {
          "config": {
            "anchor": "fixed",
            "autoBreakpoint": 480,
            "content": "cover",
            "display": "visible",
            "handle": "hide",
            "id": "deskMenu",
            "modal": true,
            "size": 80,
            "view": "Docks/Menu"
          },
          "scope": "C",
          "type": "alter-dock"
        },
        {
          "config": {
            "script": "\tself.view.custom.expanded = False"
          },
          "scope": "G",
          "type": "script"
        }
      ]
    }
  }
}
```

**Menu Item Click Behavior:**

Each icon in the menu triggers **three actions**:
1. **Navigate** to the target page (`nav` event)
2. **Open** the expanded menu dock (`dock` event)
3. **Send message** to unselect other items (`script` event)

```json
{
  "events": {
    "dom": {
      "onClick": [
        {
          "config": { "page": "/TargetPage" },
          "scope": "C",
          "type": "nav"
        },
        {
          "config": { "id": "BigMenu", "type": "open" },
          "scope": "C",
          "type": "dock"
        },
        {
          "config": {
            "script": "\tsystem.perspective.sendMessage('unselect', {'selectMenu': self.meta.name})"
          },
          "scope": "G",
          "type": "script"
        }
      ]
    }
  }
}
```

**Icon Styling:**

Icons use tint colors for visual feedback:
- Default color: `#2699FB` (blue)
- Active/selected color: `#D42C67` (red/pink)

```json
{
  "props": {
    "tint": {
      "color": "#2699FB",
      "enabled": true
    },
    "style": {
      "cursor": "pointer",
      "marginBottom": "10px",
      "paddingLeft": "28px",
      "paddingRight": "28px"
    }
  }
}
```

**Tooltip on Hover:**

Each icon has a tooltip for accessibility:
```json
{
  "meta": {
    "name": "MenuItem",
    "tooltip": {
      "enabled": true,
      "location": "center-right",
      "text": "Menu Item Label"
    }
  }
}
```

**Hamburger Icon at Bottom:**

The menu typically has a hamburger icon at the bottom to open the expanded menu:
```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": { "id": "MaxDock", "type": "open" },
        "scope": "C",
        "type": "dock"
      }
    }
  },
  "meta": { "name": "MenuIcon" },
  "position": { "basis": "40px", "shrink": 0 },
  "props": {
    "path": "material/dehaze",
    "style": {
      "cursor": "pointer",
      "marginBottom": "20px",
      "marginLeft": "22.5px",
      "marginRight": "22.5px",
      "marginTop": "82.5px"
    }
  },
  "type": "ia.display.icon"
}
```

**Menu Structure:**
```
┌─────────────┐
│   Logo      │  ← Click navigates to home
├─────────────┤
│   📊 Icon   │  ← Click navigates + opens BigMenu
│   📈 Icon   │  ← Tooltip shows on hover
│   ⚙️ Icon   │  ← Tint color changes on selection
│   👤 Icon   │
├─────────────┤
│   (spacer)  │
├─────────────┤
│   ☰ Hamburger│  ← Opens BigMenu (expanded menu)
└─────────────┘
```

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

## How the Hamburger Menu Opens the Side Menubar

The hamburger menu icon (typically `material/dehaze`) in the header dock triggers a **dock event** to open the expanded side menu.

### Header Dock Hamburger Behavior

**Two Common Patterns:**

**Pattern 1: Open Specific Dock (COP_TSDPL style)**
```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": {
          "id": "BigMenu",
          "type": "open"
        },
        "scope": "C",
        "type": "dock"
      }
    }
  },
  "meta": { "name": "MenuIcon" },
  "props": {
    "path": "material/dehaze",
    "style": {
      "cursor": "pointer",
      "marginLeft": "10px"
    }
  },
  "type": "ia.display.icon"
}
```

**Pattern 2: Toggle Dock (WCS style)**
```json
{
  "events": {
    "dom": {
      "onClick": {
        "config": {
          "id": "deskMenu",
          "type": "toggle"
        },
        "scope": "C",
        "type": "dock"
      }
    }
  },
  "meta": { "name": "MenuIcon" },
  "props": {
    "path": "material/dehaze",
    "style": { "cursor": "pointer" }
  },
  "type": "ia.display.icon"
}
```

### Header Display Mode Toggle

The header also controls its own visibility mode for responsive design using **custom properties** and **script events**:

```json
{
  "custom": {
    "desktop": true,
    "display": "visible"
  }
}
```

**Logo Click with Display Mode Toggle:**
```json
{
  "events": {
    "dom": {
      "onClick": [
        {
          "config": {
            "script": "\tif self.view.custom.desktop:\n\t\tsystem.perspective.sendMessage('show', {'header': self.view.custom.display})\n\t\tself.view.custom.display = 'visible'\n\telse:\n\t\tself.view.custom.display = 'hidden'\n\t\tsystem.perspective.sendMessage('hide', {'header': self.view.custom.display})\n\tsystem.perspective.navigate('/')"
          },
          "scope": "G",
          "type": "script"
        }
      ]
    }
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

| Type | Description | Use Case |
|------|-------------|----------|
| `"open"` | Opens the specified dock | Hamburger opens menu |
| `"close"` | Closes the specified dock | Close button closes menu |
| `"toggle"` | Toggles dock open/close state | Hamburger toggle behavior |

**Example: Toggle between two docks (Close minDock, Open maxDock):**

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

**Example: Close expanded menu when clicking a menu item:**

```json
{
  "events": {
    "dom": {
      "onClick": [
        {
          "config": { "page": "/targetPage" },
          "scope": "C",
          "type": "nav"
        },
        {
          "config": { "id": "BigMenu", "type": "open" },
          "scope": "C",
          "type": "dock"
        },
        {
          "config": {
            "script": "\tsystem.perspective.sendMessage('unselect', {'selectMenu': self.meta.name})"
          },
          "scope": "G",
          "type": "script"
        }
      ]
    }
  }
}
```

### Alter-Dock (Dynamic Dock Modification)

The `alter-dock` event type dynamically modifies dock properties at runtime:

```json
{
  "config": {
    "anchor": "fixed",
    "autoBreakpoint": 480,
    "content": "cover",
    "display": "visible",
    "handle": "hide",
    "id": "deskMenu",
    "modal": false,
    "size": 200,
    "view": "Docks/Menu"
  },
  "scope": "C",
  "type": "alter-dock"
}
```

**Use Case: Hover Expand/Collapse on Menu Dock:**
```json
{
  "events": {
    "dom": {
      "onMouseOver": [
        {
          "config": {
            "anchor": "fixed",
            "autoBreakpoint": 480,
            "content": "cover",
            "display": "visible",
            "handle": "hide",
            "id": "deskMenu",
            "modal": false,
            "size": 200,
            "view": "Docks/Menu"
          },
          "scope": "C",
          "type": "alter-dock"
        },
        {
          "config": {
            "script": "\tself.view.custom.expanded = True"
          },
          "scope": "G",
          "type": "script"
        }
      ],
      "onMouseOut": [
        {
          "config": {
            "anchor": "fixed",
            "autoBreakpoint": 480,
            "content": "cover",
            "display": "visible",
            "handle": "hide",
            "id": "deskMenu",
            "modal": true,
            "size": 80,
            "view": "Docks/Menu"
          },
          "scope": "C",
          "type": "alter-dock"
        },
        {
          "config": {
            "script": "\tself.view.custom.expanded = False"
          },
          "scope": "G",
          "type": "script"
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

### The "unselect" Message Pattern

The most common message pattern in dock navigation is the **"unselect"** message, which manages selection state across menu items.

**How it works:**
1. When a menu icon is clicked, it sends an "unselect" message with its name
2. The Flex Repeater receives this message and updates selection state
3. Only the clicked item remains selected; all others are deselected

**Message Handler on Flex Repeater:**

```json
{
  "scripts": {
    "messageHandlers": [
      {
        "messageType": "unselect",
        "pageScope": true,
        "script": "selectedMenu = payload['selectMenu']\nfor item in self.props.instances:\n    for childItem in item['child']:\n        try:\n            childItem['subSelect'] = False\n        except:\n            continue\n    if item['headerLabel'] != selectedMenu:\n        item['selected'] = False\n    else:\n        if item['selected'] == True:\n            item['selected'] = False\n        else:\n            item['selected'] = True\n        system.perspective.openDock('mainDock')",
        "sessionScope": true,
        "viewScope": true
      }
    ]
  }
}
```

**Script Breakdown:**
```python
# Get the name of the clicked menu item
selectedMenu = payload['selectMenu']

# Loop through all menu categories
for item in self.props.instances:
    # Reset all child items' subSelect to False
    for childItem in item['child']:
        try:
            childItem['subSelect'] = False
        except:
            continue
    
    # If this category is NOT the selected one, deselect it
    if item['headerLabel'] != selectedMenu:
        item['selected'] = False
    else:
        # Toggle selection state for the clicked category
        if item['selected'] == True:
            item['selected'] = False
        else:
            item['selected'] = True
        # Open the expanded menu dock
        system.perspective.openDock('mainDock')
```

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

**Scope Properties:**

| Property | Description |
|----------|-------------|
| `pageScope` | Message is scoped to the current page |
| `sessionScope` | Message is scoped to the entire session |
| `viewScope` | Message is scoped to the current view |

### Sending Messages

```python
# From a script event - send unselect message
system.perspective.sendMessage("unselect", {"selectMenu": self.meta.name})

# From a script event - send show/hide message
system.perspective.sendMessage("show", {"header": self.view.custom.display})

# From a script event - send hide message
system.perspective.sendMessage("hide", {"header": self.view.custom.display})
```

### Common Message Patterns

**Show Header:**
```python
system.perspective.sendMessage('show', {'header': self.view.custom.display})
```

**Hide Header:**
```python
system.perspective.sendMessage('hide', {'header': self.view.custom.display})
```

**Unselect Menu Items:**
```python
system.perspective.sendMessage('unselect', {'selectMenu': self.meta.name})
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

**Instance Properties Reference:**

| Property | Type | Description |
|----------|------|-------------|
| `child` | array | Array of sub-menu items |
| `display` | boolean | Whether instance is visible |
| `headerIcon` | string | Icon for the category header (base64 or URL) |
| `headerLabel` | string | Label for the category header |
| `headerTarget` | string | Navigation target for the header |
| `selected` | boolean | Whether category is expanded/selected |

**Child Item Properties:**

| Property | Type | Description |
|----------|------|-------------|
| `display` | boolean | Whether sub-item is visible |
| `label` | string | Sub-item label text |
| `nav` | boolean | Whether clicking navigates |
| `path` | boolean | Whether item has a path |
| `subSelect` | boolean | Whether sub-item is selected |
| `target` | string | Navigation target page |

### SingleMenu View

The SingleMenu view is a child view that renders each menu category. It typically contains:
- A header container with icon and label
- A list of sub-items that expand when selected

**SingleMenu View Structure:**

```json
{
  "custom": {},
  "params": {
    "child": [],
    "display": true,
    "headerIcon": "",
    "headerLabel": "",
    "headerTarget": "",
    "selected": false
  },
  "propConfig": {
    "params.child": { "paramDirection": "input" },
    "params.display": { "paramDirection": "input" },
    "params.headerIcon": { "paramDirection": "input" },
    "params.headerLabel": { "paramDirection": "input" },
    "params.headerTarget": { "paramDirection": "input" },
    "params.selected": { "paramDirection": "input" }
  },
  "root": {
    "children": [
      {
        "meta": { "name": "HeaderContainer" },
        "position": { "shrink": 0 },
        "props": {
          "direction": "row",
          "style": { "padding": "10px" }
        },
        "type": "ia.container.flex"
      },
      {
        "meta": { "name": "SubItemsContainer" },
        "position": { "grow": 1 },
        "props": {
          "direction": "column"
        },
        "type": "ia.container.flex"
      }
    ],
    "type": "ia.container.flex"
  }
}
```

### Flex Repeater Configuration

```json
{
  "meta": { "name": "FlexRepeater" },
  "position": { "basis": "700px", "grow": 1 },
  "props": {
    "direction": "column",
    "elementPosition": { "basis": "auto", "grow": 0, "shrink": 0 },
    "instances": [...],
    "path": "Docks/MenuBar/SingleMenu",
    "useDefaultViewHeight": false,
    "useDefaultViewWidth": false
  },
  "type": "ia.display.flex-repeater"
}
```

---

## Best Practices

1. **Use Unique IDs**: Every dock must have a unique `id` for programmatic access.

2. **Organize Dock Views**: Keep dock views in a `Docks/` folder under `views/`.

3. **Consistent Styling**: Use CSS variables for consistent theming across docks.

4. **Responsive Design**: Set appropriate `autoBreakpoint` values for mobile responsiveness.

5. **Message Handling**: Use message handlers for dock-to-dock communication.

6. **Thumbnail Images**: Include `thumbnail.png` files for visual identification in the Designer.

7. **Default Sizes**: Set reasonable `defaultSize` values in dock views for proper rendering.

8. **Hover Expand/Collapse**: Use `onMouseOver`/`onMouseOut` with `alter-dock` for menu expansion.

9. **Selection State**: Use the "unselect" message pattern to manage menu item selection.

10. **Icon Tinting**: Use `tint` property to visually indicate selected/active menu items.

11. **Tooltip Support**: Add tooltips to icons for better accessibility and usability.

12. **Event Chaining**: Chain multiple events (nav + dock + script) for complex interactions.

13. **Custom Properties**: Use custom properties for state management (expanded, display, desktop).

14. **Modal vs Non-Modal**: Set `modal: false` for side menus to allow main content interaction.

15. **Content Mode**: Use `content: "cover"` for menus that overlay, `content: "push"` for headers.

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

---

## Comparison: COP_TSDPL vs WCS Menu Approaches

### COP_TSDPL Approach (Two-Dock System)

**Structure:**
- `Menu` dock (80px) - Icons only
- `BigMenu` dock (200-300px) - Expanded menu with labels

**Behavior:**
1. Hover over Menu dock → Labels appear (uses `alter-dock` to expand)
2. Click icon → Navigates to page + Opens BigMenu dock
3. Click hamburger in Menu dock → Opens BigMenu dock
4. BigMenu dock has close button that collapses back to Menu

**Key Files:**
- `views/Docks/Menu/view.json` - Icon-only menu
- `views/Docks/BigMenu/view.json` - Expanded menu

### WCS Approach (Single Dock with Hover)

**Structure:**
- `deskMenu` dock (80px default, 200px on hover)

**Behavior:**
1. Hover over dock → Expands to 200px (uses `onMouseOver` + `alter-dock`)
2. Mouse out → Collapses to 80px (uses `onMouseOut` + `alter-dock`)
3. Custom property `expanded` controls label visibility
4. Uses Flex Repeater for menu items

**Key Files:**
- `views/Docks/Menu/view.json` - Single menu with hover expand

### Which to Use?

| Scenario | Recommended Approach |
|----------|---------------------|
| Need separate icon and expanded views | COP_TSDPL (Two-Dock) |
| Simple hover expand/collapse | WCS (Single Dock) |
| Complex menu with categories | COP_TSDPL with MenuBar |
| Mobile-friendly design | WCS with autoBreakpoint |

---

## Quick Reference

### Dock Event Types
| Type | Description |
|------|-------------|
| `dock` | Open, close, or toggle docks |
| `nav` | Navigate to a page |
| `script` | Execute custom script |
| `popup` | Open a popup window |
| `alter-dock` | Dynamically modify dock properties |

### Common Dock IDs
| ID | Purpose |
|----|---------|
| `BigMenu` | Expanded menu (200-300px) |
| `maxDock` | Maximum/expanded dock |
| `minDock` | Minimum/collapsed dock |
| `deskMenu` | Desktop menu dock |
| `mainDock` | Main navigation dock |

### Common Messages
| Message | Payload | Purpose |
|---------|---------|---------|
| `unselect` | `{"selectMenu": "name"}` | Deselect all menu items except named |
| `show` | `{"header": "visible"}` | Show header |
| `hide` | `{"header": "hidden"}` | Hide header |

### Dock Sizes
| Dock Type | Typical Size |
|-----------|--------------|
| Header | 40-80px height |
| Menu (collapsed) | 80px width |
| Menu (expanded) | 200-300px width |
| MenuBar | 250-350px width |
