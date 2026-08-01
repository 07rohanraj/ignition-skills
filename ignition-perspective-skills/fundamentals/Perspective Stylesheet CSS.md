---
name: perspective-stylesheet-css
description: Writing correct CSS for Ignition Perspective — covers stylesheet.css, style-classes/style.css, the psc- and ia- selector prefixes, and how to target generated DOM elements reliably.
---

# Perspective Stylesheet CSS

## Description

This guide explains how to write correct, reliable CSS for Ignition Perspective components. It covers the two types of CSS resources (global `stylesheet.css` and per-style-class `style.css`), the selector prefix conventions (`psc-` for user Style Classes, `ia_` for built-in Perspective classes), how to discover real DOM selectors, and common pitfalls to avoid.

## Documentation

---

## 1. Where CSS Lives in a Perspective Project

Perspective projects have two places where custom CSS can be authored:

```
com.inductiveautomation.perspective/
├── stylesheet/                    # Global project-wide CSS
│   ├── resource.json
│   └── stylesheet.css             # Applied to ALL views
└── style-classes/                 # Per-style-class CSS
    └── StyleClassName/
        ├── resource.json
        └── style.css              # Applied when the class is assigned
```

| Resource | Scope | Use Case |
|----------|-------|----------|
| `stylesheet/stylesheet.css` | Global — affects every view in the project | Project-wide resets, base typography, global overrides of built-in component styles |
| `style-classes/Name/style.css` | Scoped — only applies when the Style Class is assigned to a component | Reusable, targeted style bundles (e.g., a "card" style, a "status-badge" style) |

### resource.json for style-classes

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

### resource.json for stylesheet

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

---

## 2. Selector Prefix Conventions

Perspective uses two distinct CSS class prefix conventions. Using the wrong one is the most common source of CSS that "doesn't work."

### 2.1 User Style Classes → `.psc-` prefix

When you create a Style Class in the Designer (e.g., named `card`), Perspective renders it in the DOM with the prefix `psc-`. In your CSS, you **must** use this prefix:

| Style Class Name (Designer) | Correct CSS Selector | Incorrect Selector |
|-----------------------------|---------------------|-------------------|
| `card` | `.psc-card` | `.card` |
| `header` | `.psc-header` | `.header` |
| `chart-title` | `.psc-chart-title` | `.chart-title` |
| `my-custom-style` | `.psc-my-custom-style` | `.my-custom-style` |
| `CSS/MyFolder/MyStyle` | `.psc-CSS\/MyFolder\/MyStyle` | `.CSS/MyFolder/MyStyle` |

**Rules:**
- Always prefix with `.psc-` when targeting a user-created Style Class in CSS
- The Style Class name entered in the Designer is used **without** the prefix in the Property Editor's `style.classes` field
- Folder separators (`/`) in Style Class names are escaped as `\/` in the CSS selector

### 2.2 Built-in Perspective Classes → `.ia_` prefix

Perspective's internal component styles use the `.ia_` prefix with an ABEM (Atomic Block Element Modifier) naming convention. These classes are applied by Perspective automatically — you do not assign them in the Property Editor.

**Naming pattern:**
```
ia_componentName__element--modifier
```

**Common built-in selectors (verify each in browser DevTools):**

| Component | Common Selectors | Purpose |
|-----------|-----------------|---------|
| Label | `.ia_labelComponent` | Outer label wrapper |
| Button | `.ia_buttonComponent`, `.ia_button--primary` | Button wrapper, primary variant |
| Flex Container | `.ia_containerFlexComponent` | Flex container wrapper |
| Coordinate Container | `.ia_containerCoordinateComponent` | Coordinate container wrapper |
| Column Container | `.ia_containerColumnComponent` | Column container wrapper |
| Text Field | `.ia_inputTextFieldComponent` | Text field wrapper |
| Dropdown | `.ia_inputDropdownComponent` | Dropdown wrapper |
| Checkbox | `.ia_inputCheckboxComponent` | Checkbox wrapper |
| Toggle Switch | `.ia_toggleSwitch__thumb`, `.ia_toggleSwitch__thumb--selected` | Toggle thumb, selected state |
| Table | `.ia_displayTableComponent`, `.t`, `.tc` | Table wrapper, row, cell |
| Cylindrical Tank | `.ia_cylindricalTankComponent__liquid--animation` | Liquid animation element |

> **CRITICAL:** The `ia_` prefix is **reserved** for Perspective's built-in classes. Never create user Style Classes with the `ia_` prefix — it may cause unintended behavior and will be overwritten on upgrades.

### 2.3 Selector Priority (Cascading Order)

CSS applied in Perspective follows this priority (highest wins):

1. **Inline styles** on the component (`style` object in Property Editor)
2. **User Style Classes** (`.psc-*`) — applied in alphabetical order; later classes override earlier ones
3. **Global stylesheet** (`stylesheet.css`)
4. **Built-in theme styles** (`.ia_*` classes from the active theme)

---

## 3. Writing Correct CSS

### 3.1 Targeting a Style Class Applied to a Component

If you create a Style Class named `status-badge` and apply it to a Label:

**In the Designer Property Editor:**
```
style.classes = "status-badge"
```

**In your CSS (stylesheet.css or style.css):**
```css
/* CORRECT: .psc- prefix */
.psc-status-badge {
  background-color: #e0f7fa;
  border-radius: 12px;
  padding: 4px 12px;
  font-size: 12px;
}
```

### 3.2 Overriding Built-in Component Styles

To override a built-in Perspective component's internal styling, target its `.ia_` class:

```css
/* Override all primary buttons globally */
.ia_button--primary {
  background-color: var(--callToAction);
  border-radius: 20px;
}

/* Override the toggle switch thumb when selected */
.ia_toggleSwitch__thumb--selected {
  background-color: #4caf50;
}
```

### 3.3 Targeting a Style Class Scope Within Built-in Elements

To style a built-in component element **only** when a specific Style Class is applied:

```css
/* Style the toggle thumb ONLY inside a component with "my-toggle" style class */
.psc-my-toggle .ia_toggleSwitch__thumb--selected {
  background-color: #ff5722;
}
```

This pattern scopes overrides to specific instances without affecting all components globally.

### 3.4 Using CSS Variables (Theme-Aware Colors)

Perspective themes expose CSS custom properties. Use them for theme-consistent styling:

```css
.psc-card {
  background-color: var(--neutral-5);
  border: 1px solid var(--neutral-20);
  color: var(--neutral-90);
}

.psc-status-ok {
  color: var(--success);
}

.psc-status-alarm {
  color: var(--error);
}
```

Common theme variables: `--callToAction`, `--neutral-5` through `--neutral-90`, `--error`, `--success`, `--warning`, `--info`.

### 3.5 Media Queries for Responsive Styles

```css
.psc-responsive-card {
  padding: 16px;
}

@media (max-width: 600px) {
  .psc-responsive-card {
    padding: 8px;
    font-size: 12px;
  }
}
```

### 3.6 Hover and Element State Pseudo-Classes

```css
.psc-clickable-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  cursor: pointer;
}

.psc-clickable-card:active {
  transform: scale(0.98);
}
```

---

## 4. How to Discover the Correct Selectors

**Never guess selectors.** Always verify them using browser DevTools:

1. Open your Perspective Session in Chrome
2. Press `F12` to open DevTools
3. Use `Ctrl+Shift+C` (Inspect Element mode) and click on the component
4. In the Elements panel, examine the DOM to find the actual CSS class names applied
5. In the Styles panel, test your CSS live before committing it to a file

**Tips:**
- Perspective components are wrapped in multiple `<div>` layers — the outermost div carries the component's class
- Style Classes you assign appear directly on the component's wrapper element as `psc-{name}`
- Built-in `.ia_` classes appear on inner wrapper elements
- Table components do NOT use standard HTML `<td>` elements — use `.t` and `.tc` classes instead

---

## 5. Common Pitfalls and How to Avoid Them

### ❌ Wrong: Using `.card` instead of `.psc-card`
```css
/* WRONG — this targets nothing in Perspective */
.card {
  background: white;
}

/* CORRECT */
.psc-card {
  background: white;
}
```

### ❌ Wrong: Using `ia_` prefix for user Style Classes
```css
/* WRONG — ia_ is reserved for built-in classes */
.ia_my-custom-style {
  color: red;
}

/* CORRECT — use psc- for user-created Style Classes */
.psc-my-custom-style {
  color: red;
}
```

### ❌ Wrong: Targeting HTML elements directly
```css
/* WRONG — Perspective doesn't use standard HTML table elements */
td {
  padding: 8px;
}

/* CORRECT — use Perspective's actual table classes */
.t {
  /* row styling */
}
.tc {
  /* cell styling */
}
```

### ❌ Wrong: Using unescaped folder separators
```css
/* WRONG — folder separators must be escaped */
.psc-CSS/MyFolder/MyStyle {
  color: blue;
}

/* CORRECT — escape / as \/ */
.psc-CSS\/MyFolder\/MyStyle {
  color: blue;
}
```

### ❌ Wrong: Assuming selectors without verifying
```css
/* WRONG — .ia_label is NOT a valid selector */
.ia_label {
  font-size: 20px;
}

/* CORRECT — verify in DevTools first; the actual selector is likely .ia_labelComponent */
.ia_labelComponent {
  font-size: 20px;
}
```

---

## 6. Complete Examples

### Example: Global Stylesheet (stylesheet.css)

```css
/* Project-wide base styles */
body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
}

/* Override all flex containers to have consistent gap */
.ia_containerFlexComponent {
  gap: 8px;
}

/* Global card style */
.psc-card {
  background-color: var(--neutral-5);
  border: 1px solid var(--neutral-20);
  border-radius: 8px;
  padding: 16px;
}

/* Status indicator styles */
.psc-status-ok {
  color: var(--success);
  font-weight: bold;
}

.psc-status-warning {
  color: var(--warning);
  font-weight: bold;
}

.psc-status-alarm {
  color: var(--error);
  font-weight: bold;
}

/* Custom button override */
.ia_button--primary {
  border-radius: 20px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
```

### Example: Per-Style-Class CSS (style-classes/Card/style.css)

```css
.psc-Card {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: box-shadow 0.2s ease;
}

.psc-Card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Style child elements that also have a specific class */
.psc-Card .psc-card-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 8px;
  color: var(--neutral-90);
}

.psc-Card .psc-card-body {
  font-size: 14px;
  color: var(--neutral-70);
  line-height: 1.5;
}
```

### Example: Scoped Component Override (stylesheet.css)

```css
/* Only override toggle switch inside a component with "custom-toggle" style */
.psc-custom-toggle .ia_toggleSwitch__thumb--selected {
  background-color: #4caf50;
}

/* Only override button styling inside a "toolbar" container */
.psc-toolbar .ia_button--primary {
  background-color: #1976d2;
  border-radius: 4px;
}
```

---

## 7. Quick Reference Table

| What You Want to Do | CSS Selector Pattern | Where to Put It |
|---------------------|---------------------|-----------------|
| Style all components with Style Class "card" | `.psc-card { ... }` | stylesheet.css or Card/style.css |
| Style a built-in button variant | `.ia_button--primary { ... }` | stylesheet.css |
| Style a Style Class's children | `.psc-card .psc-card-title { ... }` | Card/style.css |
| Override built-in only when Style Class present | `.psc-my-class .ia_buttonComponent { ... }` | stylesheet.css |
| Use theme-aware colors | `color: var(--callToAction)` | Any CSS file |
| Responsive breakpoint | `@media (max-width: 600px) { ... }` | stylesheet.css or style.css |
| Hover state on a Style Class | `.psc-card:hover { ... }` | Card/style.css |

---

## 8. Key Rules Summary

1. **Always use `.psc-` prefix** for user-created Style Classes in CSS selectors
2. **Always use `.ia_` prefix** for built-in Perspective component classes (never for user classes)
3. **Never guess selectors** — verify them in browser DevTools (`F12` → Inspect)
4. **Escape `/` as `\/`** in Style Class names that use folders
5. **Do not target raw HTML elements** (e.g., `td`, `div`) — Perspective uses custom class-based wrappers
6. **Prefer scoped overrides** (`.psc-myClass .ia_component`) over global overrides to avoid side effects
7. **Use CSS variables** (`var(--name)`) for theme-consistent colors
8. **Check selector existence** before using it — if you can't find it in DevTools, it's likely not a valid selector
