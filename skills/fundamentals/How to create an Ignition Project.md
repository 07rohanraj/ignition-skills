# How to Create an Ignition Project

## Description

This document provides a complete guide for creating an Ignition Perspective project from scratch. It covers the folder structure, required files, configuration files, and how to set up views, page configuration, and session properties. Use this guide when starting a new project or when you need to understand the project file organization.

## Documentation

# How to Create an Ignition Perspective Project

## Overview

An Ignition Perspective project consists of a specific folder structure with configuration files that define the project's behavior, views, navigation, and settings. This guide explains each component and how to create them.

**Project Location:** Ignition projects are created in the gateway's project directory:

```
C:\Program Files\Inductive Automation\Ignition\data\projects\
```

Each project gets its own folder within this directory (e.g., `C:\Program Files\Inductive Automation\Ignition\data\projects\MyProjectName\`).

---

## Project Folder Structure

```
ProjectName/
├── project.json                          # Project metadata
├── com.inductiveautomation.perspective/  # Perspective module
│   ├── page-config/                      # Page and dock configuration
│   │   ├── config.json                   # Page routes and dock settings
│   │   └── resource.json                 # Resource metadata
│   ├── session-props/                    # Session properties
│   │   ├── props.json                    # Session property definitions
│   │   └── resource.json                 # Resource metadata
│   ├── style-classes/                    # Custom CSS style classes
│   │   ├── StyleClassName/
│   │   │   ├── resource.json             # Resource metadata
│   │   │   └── style.css                 # CSS styles
│   │   └── ...
│   ├── stylesheet/                       # Global stylesheet
│   │   ├── resource.json                 # Resource metadata
│   │   └── stylesheet.css                # Global CSS styles
│   └── views/                            # All Perspective views
│       ├── ViewName/                     # Individual view folder
│       │   ├── view.json                 # View JSON configuration
│       │   └── resource.json             # Resource metadata
│       └── SubFolder/                    # Nested view folder
│           ├── ViewName/
│           │   ├── view.json
│           │   └── resource.json
│           └── ...
├── com.inductiveautomation.vision/       # Vision module (optional)
│   └── client-tags/                      # Client tag definitions
│       ├── data.bin                      # Binary tag data
│       └── resource.json                 # Resource metadata
├── ignition/                             # Gateway-level settings
│   ├── global-props/                     # Global properties
│   │   ├── data.bin                      # Binary property data
│   │   └── resource.json                 # Resource metadata
│   ├── named-query/                      # Named queries
│   │   ├── QueryCategory/
│   │   │   ├── QueryName/
│   │   │   │   ├── resource.json         # Resource metadata
│   │   │   │   └── query.py              # Query script
│   │   │   └── ...
│   │   └── ...
│   └── script-python/                    # Python scripts
│       ├── ScriptCategory/
│       │   ├── resource.json             # Resource metadata
│       │   └── code.py                   # Python code
│       └── ...
├── UDT/                                  # User Defined Types (optional)
│   ├── UDTName/
│   │   ├── resource.json                 # Resource metadata
│   │   └── definition.json               # UDT definition
│   └── ...

```

---

## File Definitions

### 1. `project.json` (Root Level)

The project metadata file. Defines project name, description, and inheritance settings.

**Required fields:**

- `title` (string): Display name of the project
- `description` (string): Project description
- `enabled` (boolean): Whether project is active
- `inheritable` (boolean): Whether child projects can inherit from this
- `parent` (string): Parent project name (empty string if root)

**Example:**

```json
{
  "title": "MyProject",
  "description": "Battery monitoring system",
  "enabled": true,
  "inheritable": false,
  "parent": ""
}
```

---

### 2. `com.inductiveautomation.perspective/` (Perspective Module)

Contains all Perspective-specific configuration and views.

#### 2.1 `page-config/` (Page Configuration)

Defines page routes, navigation docks, and page settings.

**`config.json` structure:**

```json
{
  "pages": {
    "/page-route": {
      "title": "Page Title",
      "viewPath": "ViewPath/ViewName",
      "docks": {
        "top": [],
        "left": [],
        "right": [],
        "bottom": []
      }
    }
  },
  "sharedDocks": {
    "cornerPriority": "top-bottom"
  }
}
```

**Dock configuration object:**

```json
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
  "size": 150,
  "viewParams": {},
  "viewPath": "Navigation/Side Dock"
}
```

**Dock properties:**

- `anchor`: `"fixed"` or `"float"` - How dock is positioned
- `autoBreakpoint`: Pixel width to auto-hide dock on small screens
- `content`: `"push"` or `"overlay"` - How dock affects main content
- `handle`: `"hide"` or `"none"` - Show/hide handle
- `modal`: boolean - Whether dock blocks interaction with main content
- `resizable`: boolean - Whether user can resize dock
- `show`: `"visible"`, `"hidden"`, or `"auto"` - Initial visibility
- `size`: number - Dock width/height in pixels
- `viewPath`: string - Path to the dock view (relative to `views/`)
- `viewParams`: object - Parameters to pass to dock view

**`resource.json` structure:**

```json
{
  "scope": "G",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["config.json"],
  "attributes": {}
}
```

---

#### 2.2 `session-props/` (Session Properties)

Defines session-scoped properties available throughout the project.

**`props.json` structure:**

```json
{
  "custom": {},
  "propConfig": {
    "props.propertyName": {
      "access": "PUBLIC|PROTECTED|PRIVATE|SYSTEM",
      "persistent": false
    }
  },
  "props": {
    "propertyName": "defaultValue"
  }
}
```

**Access levels:**

- `PUBLIC`: Read/write from browser scripts
- `PROTECTED`: Read-only from browser, write only from server
- `PRIVATE`: Not accessible from browser
- `SYSTEM`: Built-in system properties (read-only)

**Common system properties:**

- `props.auth`: Authentication info
- `props.device`: Device info (user agent, type, timezone)
- `props.gateway`: Gateway info
- `props.locale`: User locale
- `props.offline`: Offline capability info

---

#### 2.3 `views/` (Perspective Views)

Contains all view JSON files organized in folders.

**Folder structure:**

```
views/
├── RootView/                    # Top-level view
│   ├── view.json
│   └── resource.json
├── SubFolder/                   # Nested folder
│   ├── ChildView/
│   │   ├── view.json
│   │   └── resource.json
│   └── AnotherChild/
│       ├── view.json
│       └── resource.json
└── ...
```

**View path examples:**

- `RootView` → View at `views/RootView/`
- `SubFolder/ChildView` → View at `views/SubFolder/ChildView/`
- `SubFolder/AnotherChild` → View at `views/SubFolder/AnotherChild/`

---

#### 2.4 `style-classes/` (Custom CSS Style Classes)

Contains custom CSS classes that can be applied to components.

**Folder structure:**

```
style-classes/
├── StyleClassName/
│   ├── resource.json
│   └── style.css
└── ...
```

**`resource.json` structure:**

```json
{
  "scope": "A",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["style.css"],
  "attributes": {}
}
```

**`style.css` example:**

```css
.my-custom-class {
  background-color: #f0f0f0;
  border-radius: 8px;
  padding: 16px;
}
```

---

#### 2.5 `stylesheet/` (Global Stylesheet)

Contains project-wide CSS styles applied to all views.

**`resource.json` structure:**

```json
{
  "scope": "A",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["stylesheet.css"],
  "attributes": {}
}
```

**`stylesheet.css` example:**

```css
/* Global project styles */
body {
  font-family: Arial, sans-serif;
}

/* Target a user-created Style Class using the .psc- prefix */
.psc-my-global-style {
  gap: 8px;
}

/* Override a built-in Perspective component selector (verify in DevTools) */
.ia_containerFlexComponent {
  gap: 8px;
}
```

> **Note:** User-created Style Classes use the `.psc-` prefix in CSS. Built-in Perspective classes use `.ia_`. Always verify selectors in browser DevTools (`F12`) before using them. See the `perspective-stylesheet-css` skill for full details.

---

#### 2.6 `ignition/named-query/` (Named Queries)

Contains named queries organized by category. Named queries are reusable SQL queries that can be called from scripts and views.

**Folder structure:**

```
named-query/
├── QueryCategory/
│   ├── QueryName/
│   │   ├── resource.json
│   │   └── query.py
│   └── ...
└── ...
```

**`resource.json` structure:**

```json
{
  "scope": "A",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["query.py"],
  "attributes": {
    "hintScope": 2
  }
}
```

**`query.py` example:**

```python
query = "SELECT * FROM equipment WHERE id = :equipmentId"
result = system.db.runNamedQuery("EquipmentHealth", "Equipment/GetEquipment", {"equipmentId": equipmentId})
```

For more details, see `Ignition Named Query.md`.

---

#### 2.7 `ignition/script-python/` (Python Scripts)

Contains project-level Python scripts organized by category.

**Folder structure:**

```
script-python/
├── ScriptCategory/
│   ├── resource.json
│   └── code.py
└── ...
```

**`resource.json` structure:**

```json
{
  "scope": "A",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["code.py"],
  "attributes": {
    "hintScope": 2
  }
}
```

**`code.py` example:**

```python
def getEquipmentData(equipmentId):
    """
    Retrieve equipment data by ID.

    Args:
        equipmentId (int): The equipment identifier

    Returns:
        dict: Equipment data
    """
    result = system.db.runNamedQuery(
        "EquipmentHealth",
        "Equipment/GetEquipment",
        {"equipmentId": equipmentId}
    )
    return system.util.jsonDecode(result.getValueAt(0, "data"))
```

---

#### 2.8 `com.inductiveautomation.vision/` (Vision Module)

Contains Vision module resources (optional, for legacy or hybrid projects).

**Folder structure:**

```
com.inductiveautomation.vision/
├── client-tags/
│   ├── data.bin
│   └── resource.json
└── ...
```

**Note:** Most new projects should use Perspective instead of Vision. The Vision module is included for backward compatibility or hybrid scenarios.

---

#### 2.9 `skills/` (OpenCode Skills)

Contains documentation and skills for OpenCode AI assistant.

**Folder structure:**

```
skills/
├── perspective/
│   ├── SKILL.md                          # Main skill file
│   ├── How to create an Ignition Project.md
│   ├── How to build a new Perspective View.md
│   ├── Perspective Button Component.md
│   ├── Perspective Table Component.md
│   └── ... (other component docs)
└── ...
```

**`SKILL.md` example:**

```markdown
# Perspective Component Documentation

This skill provides documentation for Ignition Perspective components.

## When to use

Use this skill when working with Perspective views, components, or configurations.

## Documentation files

- How to create an Ignition Project.md
- How to build a new Perspective View.md
- Perspective [Component] Component.md
```

---

#### 2.10 `UDT/` (User Defined Types)

Contains User Defined Type (UDT) definitions that can be used to create reusable tag structures.

**Folder structure:**

```
UDT/
├── UDTName/
│   ├── resource.json
│   └── definition.json
└── ...
```

**`resource.json` structure:**

```json
{
  "scope": "A",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["definition.json"],
  "attributes": {}
}
```

**`definition.json` structure:**

```json
{
  "name": "EquipmentUDT",
  "description": "User Defined Type for equipment",
  "parameters": [
    {
      "name": "EquipmentName",
      "value": "",
      "description": "Name of the equipment"
    }
  ],
  "tags": [
    {
      "name": "Status",
      "tagType": "AtomicTag",
      "dataType": "Boolean",
      "valueSource": "memory"
    }
  ]
}
```

---

#### 2.11 `Project_Instructions/` (Project Documentation)

Contains project-specific documentation and instructions for developers and users.

**Folder structure:**

```
Project_Instructions/
├── README.md                              # Project overview
├── Architecture.md                        # System architecture
├── DevelopmentGuide.md                    # Development guidelines
└── ...
```

**Purpose:**

- Document project requirements
- Describe system architecture
- Provide development guidelines
- Record deployment procedures
- Document API integrations

---

#### 2.12 `opencode.json` (OpenCode Configuration)

Configuration file for OpenCode AI assistant.

**Example structure:**

```json
{
  "name": "ProjectName",
  "description": "Project description",
  "version": "1.0.0"
}
```

---

### 3. View JSON Structure (`view.json`)

Every view has the same top-level structure:

```json
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "children": [],
    "meta": {
      "name": "root"
    },
    "props": {},
    "type": "ia.container.flex"
  }
}
```

**Top-level keys:**

- `custom`: User-defined custom properties for the view
- `params`: Parameters passed into the view from other views
- `props`: View properties (e.g., `defaultSize`)
- `root`: The root container component

**Root container properties:**

- `children`: Array of child components
- `meta.name`: Always `"root"`
- `props`: Container-specific properties
- `type`: Container type (`ia.container.flex`, `ia.container.coord`, etc.)

**View size configuration:**

```json
{
  "props": {
    "defaultSize": {
      "width": 1200,
      "height": 800
    }
  }
}
```

For more details on creating views, see `How to build a new Perspective View.md`.

---

### 4. Resource JSON Structure (`resource.json`)

Every resource folder (view, page-config, session-props, etc.) has a `resource.json` file.

**Standard structure:**

```json
{
  "scope": "G",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["view.json"],
  "attributes": {}
}
```

**Properties:**

- `scope`: `"G"` (Global) or `"A"` (Application)
- `version`: Resource version number
- `restricted`: Whether resource is restricted
- `overridable`: Whether child projects can override
- `files`: Array of files in this resource
- `attributes`: Modification metadata (auto-populated by Ignition)

---

## Step-by-Step: Creating a New Project

### Step 1: Create Project Root Folder

```bash
mkdir ProjectName
cd ProjectName
```

### Step 2: Create `project.json`

```json
{
  "title": "ProjectName",
  "description": "Project description",
  "enabled": true,
  "inheritable": false,
  "parent": ""
}
```

### Step 3: Create Perspective Module Structure

```bash
mkdir -p com.inductiveautomation.perspective/page-config
mkdir -p com.inductiveautomation.perspective/session-props
mkdir -p com.inductiveautomation.perspective/views
mkdir -p com.inductiveautomation.perspective/style-classes
mkdir -p com.inductiveautomation.perspective/stylesheet
```

### Step 3.5: Create Ignition Module Structure (Optional)

```bash
mkdir -p ignition/global-props
mkdir -p ignition/named-query
mkdir -p ignition/script-python
```

### Step 4: Create Page Configuration

**`com.inductiveautomation.perspective/page-config/resource.json`:**

```json
{
  "scope": "G",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["config.json"],
  "attributes": {}
}
```

**`com.inductiveautomation.perspective/page-config/config.json`:**

```json
{
  "pages": {
    "/": {
      "title": "Home",
      "viewPath": "Home",
      "docks": {
        "top": [],
        "left": [],
        "right": [],
        "bottom": []
      }
    }
  },
  "sharedDocks": {
    "cornerPriority": "top-bottom"
  }
}
```

### Step 5: Create Session Properties

**`com.inductiveautomation.perspective/session-props/resource.json`:**

```json
{
  "scope": "G",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["props.json"],
  "attributes": {}
}
```

**`com.inductiveautomation.perspective/session-props/props.json`:**

```json
{
  "custom": {},
  "propConfig": {},
  "props": {}
}
```

### Step 6: Create Views

For each view, create a folder and two files:

**View folder:**

```bash
mkdir -p com.inductiveautomation.perspective/views/ViewName
```

**`view.json`:**

```json
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "children": [],
    "meta": {
      "name": "root"
    },
    "props": {
      "direction": "column"
    },
    "type": "ia.container.flex"
  }
}
```

**`resource.json`:**

```json
{
  "scope": "G",
  "version": 1,
  "restricted": false,
  "overridable": true,
  "files": ["view.json"],
  "attributes": {}
}
```

---

## Common Patterns

### Creating a Navigation Dock

See `Perspective Horizontal Menu Component.md` for menu configuration.

**Top Dock view structure:**

```json
{
  "root": {
    "children": [
      {
        "type": "ia.navigation.horizontalmenu",
        "props": {
          "items": [
            {
              "label": "Home",
              "target": "/",
              "icon": { "path": "material/home" },
              "enabled": true,
              "items": []
            }
          ]
        }
      }
    ],
    "type": "ia.container.flex"
  }
}
```

### Creating a Sidebar Navigation

See `Perspective Link Component.md` for link configuration.

**Side Dock view structure:**

```json
{
  "root": {
    "children": [
      {
        "type": "ia.container.flex",
        "props": {
          "direction": "column"
        },
        "children": [
          {
            "type": "ia.navigation.link",
            "props": {
              "text": "Page Name",
              "url": "/page-route",
              "target": "self"
            }
          }
        ]
      }
    ],
    "type": "ia.container.flex"
  }
}
```

### Embedding Views

See `Perspective Embedded View Component.md` for embedding configuration.

**Embedded View structure:**

```json
{
  "type": "ia.container.embeddedView",
  "props": {
    "view": "Path/To/View",
    "viewParams": {}
  }
}
```

---

## Binary Files

Some Ignition files are binary format and cannot be directly edited:

- **`data.bin`**: Binary property data (global-props, client-tags)
- **`resource.json`**: May contain binary metadata in attributes

**Working with binary files:**

1. Use the Ignition Designer to create/edit binary resources
2. Export resources as JSON for version control
3. Import JSON exports to restore resources

**Example workflow:**

1. Open Ignition Designer
2. Create/edit named query or global property
3. Export the resource
4. The exported files will be in JSON format
5. Commit JSON files to version control

---

## Helpful Tips

1. **View Paths are Relative**: When referencing views in `viewPath` or embedded views, use paths relative to the `views/` folder.

2. **Resource JSON is Required**: Every folder containing Ignition resources must have a `resource.json` file.

3. **Root Container Type**: Most views use `ia.container.flex` as the root. Use `ia.container.coord` for pixel-perfect positioning.

4. **Page Routes**: Page routes in `config.json` start with `/` (e.g., `/dashboard`, `/settings`).

5. **Dock Views**: Dock views are regular views embedded in the page configuration. They should be self-contained and sized appropriately.

6. **Session Properties**: Use `props.custom.*` for user-defined properties. System properties are read-only.

7. **File Encoding**: All JSON files must be UTF-8 encoded.

8. **Designer vs. Files**: While you can create projects entirely through files, it's often easier to use the Ignition Designer for initial setup and then modify files as needed.

---

## Minimal Project Template

Here's a minimal project structure with one page and a basic view:

```
MinimalProject/
├── project.json
├── com.inductiveautomation.perspective/
│   ├── page-config/
│   │   ├── config.json
│   │   └── resource.json
│   ├── session-props/
│   │   ├── props.json
│   │   └── resource.json
│   ├── style-classes/
│   ├── stylesheet/
│   │   ├── resource.json
│   │   └── stylesheet.css
│   └── views/
│       └── Home/
│           ├── view.json
│           └── resource.json
└── ignition/
    ├── global-props/
    │   ├── data.bin
    │   └── resource.json
    ├── named-query/
    └── script-python/
```

**project.json:**

```json
{
  "title": "MinimalProject",
  "description": "A minimal Ignition Perspective project",
  "enabled": true,
  "inheritable": false,
  "parent": ""
}
```

**page-config/config.json:**

```json
{
  "pages": {
    "/": {
      "title": "Home",
      "viewPath": "Home",
      "docks": {
        "top": [],
        "left": [],
        "right": [],
        "bottom": []
      }
    }
  },
  "sharedDocks": {
    "cornerPriority": "top-bottom"
  }
}
```

**views/Home/view.json:**
```json
{
  "custom": {},
  "params": {},
  "props": {},
  "root": {
    "children": [
      {
        "meta": {
          "name": "WelcomeLabel"
        },
        "position": {
          "align": "center"
        },
        "props": {
          "text": "Welcome to My Project",
          "textStyle": {
            "fontSize": "24px",
            "fontWeight": "bold"
          }
        },
        "type": "ia.display.label"
      }
    ],
    "meta": {
      "name": "root"
    },
    "props": {
      "direction": "column",
      "justify": "center",
      "alignItems": "center"
    },
    "type": "ia.container.flex"
  }
}
```

---

## References

- `How to build a new Perspective View.md` - Detailed view creation guide
- `Ignition Named Query.md` - Named query documentation
- `Perspective Flex Container.md` - Flex container layout
- `Perspective Expression Binding.md` - Expression binding guide
- `Perspective Power Chart Component.md` - Power chart configuration
- `Perspective Default Component JSON Configs.md` - Component JSON structure
- `Perspective Container - Child Item Position Properties.md` - Positioning in containers
- `Perspective Horizontal Menu Component.md` - Menu navigation setup
- `Perspective Link Component.md` - Link navigation setup
- `Perspective Embedded View Component.md` - Embedding views
- `Perspective Session Properties.md` - Session property reference
