# Perspective Breakpoint Container

## Description

This guide explains how to add a Perspective Breakpoint Container, configure its pixel breakpoint and dimension determinant, assign two independent child views (small for below the threshold and large for at/above it), and use styling, bindings, and scripting to create a responsive layout that swaps entirely different content based on viewport size.

## Documentation

# Instructions
## Perspective Breakpoint Container  
*A responsive container that swaps between two completely independent child views based on a pixel breakpoint.*

---

### 1.  Overview

| Feature | Description |
|---------|-------------|
| **Purpose** | To show *one* child view when the viewport (or parent) is **below** a pixel threshold, and *another* view when it is **at or above** that threshold. |
| **Ideal Use‑Case** | Mobile vs desktop content where the components in each view must be entirely separate. |
| **Comparison** | Unlike a Flex or Column container, the child content is *different*, not just laid out differently. |

---

### 2.  Schema & Default Values  

```json
{
  "type": "object",
  "required": ["breakpoint","style"],
  "properties": {
    "breakpoint": {
      "description":"Width (in pixels) below which container will display small child, and at/above which will display large child",
      "type":"number",
      "default":640
    },
    "style": { "$ref":"urn:ignition-schema:schemas/style-properties.schema.json" },
    "determinant": {
      "description":"Dimension in which to break",
      "type":"string",
      "enum":["width","height"],
      "default":"width"
    }
  }
}
```

| Property | What it Controls | Default |
|----------|-----------------|---------|
| `breakpoint` | Pixel threshold for swapping views | **640** |
| `determinant` | Which dimension drives the break (`width` or `height`) | **width** |
| `style` | CSS‑style overrides for the container (refer to the `style-properties` schema) | None – style‑free unless you bind or set it |

---

### 3.  Child Position Schema

Each direct child of a Breakpoint Container receives a *position* property that decides which view it is in:

```json
{
  "type": "object",
  "required": ["size"],
  "properties": {
    "size": {
      "type":"string",
      "enum":["small","large"],
      "default":"small"
    }
  }
}
```

* `small` – shown when **viewport < breakpoint**  
* `large` – shown when **viewport ≥ breakpoint**

> **Tip:** The first child you add will be `small` by default, the second will be `large`. If you need to reorder or change a child’s position, adjust its `size` property in the inspector or via binding.

---

### 4.  Resources

| Type | Path | Notes |
|------|------|-------|
| CSS | `/res/perspective/css/PerspectiveComponents.css` | Provides shared component styles |
| JS  | `/res/perspective/js/PerspectiveComponents.js`  | Provides core JS behavior for all Perspective components |

These resources are automatically loaded when a Breakpoint Container is used; you don’t need to include them manually.

---

### 5.  How to Create a Breakpoint Container

1. **Drag & Drop**  
   * Open the **Container Palette** → **Breakpoint** (tooltip: *A simple container whose purpose is to swap subcontainers based on a ‘breakpoint’ in pixels.*) → drop onto your view.

2. **Set Basic Properties**  
   * In the **Properties Inspector**:  
     * **Breakpoint** – choose or bind a pixel value (default 640).  
     * **Determinant** – leave as `width` unless you specifically want to break on height.  
     * **Style** – bind or set any custom CSS (e.g., background color).  

3. **Add Two Child Views**  
   * Inside the Breakpoint Container, drag two containers (e.g., a `Flex` or `Coordinate` container) – one for mobile, one for desktop.  
   * In each child’s **Properties Inspector**, set `size` to `small` or `large` as appropriate.  

4. **Design Each View Separately**  
   * Add components, layout, bindings, scripts *inside* each child – they are completely independent of one another.

5. **Test Responsiveness**  
   * In Perspective view mode, resize the browser or use the device emulator to confirm the swap occurs at the breakpoint.

---

### 6.  Advanced Usage & Tips

| Scenario | Recommendation |
|----------|----------------|
| **Dynamic Breakpoint** | Bind `breakpoint` to an expression (e.g., `system.getProperty("my.breakpoint")`). The view will update automatically if the property changes. |
| **Break on Height** | Set `determinant` to `height`. This is rarely used but can be useful for portrait vs landscape on mobile. |
| **Nested Breakpoints** | You can nest a Breakpoint Container inside another. The inner container’s breakpoint applies relative to its own parent container’s size, *not* the viewport. Example in the documentation: a root container that swaps at 800px, with an inner one swapping at 700px. |
| **Styling** | Because the container inherits a `style` property, you can apply CSS transitions to the container itself for a smooth fade between views. |
| **Script Access** | All scripting functions for the Breakpoint Container are documented in *Perspective – Breakpoint Container Scripting*. Refer there for methods like `isSmall()` or `isLarge()`. |
| **Performance** | Since the two child views are completely separate component trees, they are fully constructed only when visible. Avoid putting heavy operations in a child that will never be shown in a particular breakpoint. |
| **Accessibility** | Ensure each child view has appropriate ARIA roles and labels. When switching, the focus should move to the newly visible child. |
| **Debugging** | In the browser console, inspect the Breakpoint Container’s `clientWidth` and `clientHeight` to confirm the breakpoint is being evaluated correctly. |
| **Design Consistency** | If you need similar layout but different content, consider a Flex or Column container instead; use Breakpoint only when the *components themselves* differ. |
| **Property Binding** | Every property (`breakpoint`, `determinant`, `style`, child `size`) supports binding. Use bindings to change layout in response to other application state (e.g., user role). |
| **Cross‑Browser** | The Breakpoint Container works across all modern browsers supported by Ignition. No special handling required. |
| **Testing** | Use Ignition’s **Preview** mode with the *Responsive* toolbar. It allows you to simulate different widths instantly. |

---

### 7.  Common Mistakes to Avoid

| Mistake | Why It Happens | Fix |
|---------|----------------|-----|
| **Adding more than two children** | Only the first two children are recognized (`small` and `large`). Extra children will be ignored. | Keep the Breakpoint Container to exactly two children. |
| **Using the wrong `size` on a child** | If both children are set to `small` (or both to `large`), the container will only display one of them. | Ensure one child is `small`, the other is `large`. |
| **Mis‑understanding the breakpoint direction** | Setting `breakpoint` to 640 means *small* view appears when width < 640, *large* when ≥ 640. | Remember the `<` vs `≥` logic. |
| **Binding to a non‑numeric value** | `breakpoint` must be a number. | Validate bindings or expressions return a number. |
| **Changing `determinant` after design** | If you switch from width to height, the layout will break because the breakpoint calculation changes. | Set `determinant` early; avoid changing it mid‑design. |

---

### 8.  Quick Reference Cheat‑Sheet

| Action | What to do |
|--------|------------|
| **Add Breakpoint** | Palette → Breakpoint → drop |
| **Set Breakpoint Value** | Inspector → `breakpoint` |
| **Set Determinant** | Inspector → `determinant` |
| **Assign Small/Large** | Child inspector → `size` |
| **Add Custom Style** | Inspector → `style` |
| **Bind a Property** | Right‑click property → Bind → choose source |
| **Check Current View** | Console: `component.getComponent('myBreakpoint').isSmall()` |
| **Toggle View Programmatically** | `component.getComponent('myBreakpoint').setSize('large')` (method example from scripting docs) |

---

### 9.  Suggested Workflow for a Responsive Page

1. **Plan Layout** – decide what components differ between mobile and desktop.  
2. **Create Two Containers** – design each view in its own container.  
3. **Wrap in Breakpoint Container** – set breakpoint threshold.  
4. **Bind Styling if Needed** – e.g., different background colors per view.  
5. **Test with Nested Breakpoints** – if you need multi‑layered responsiveness.  
6. **Publish & Verify** – ensure no unintended content leaks or styling glitches.

---

### 10.  Resources to Review

* **User Manual** – *Perspective – Breakpoint Container* page (already provided in the scrape).  
* **Scripting** – *Perspective - Breakpoint Container Scripting* for programmatic control.  
* **Binding Overview** – *Types of Bindings in Perspective* for dynamic property handling.  

These references contain the full list of scripting functions and binding options that you may need.

---

### 11.  Final Note

The Breakpoint Container is a straightforward but powerful tool for building truly responsive Perspective applications. Keep your two child views simple, use bindings where possible, and test thoroughly across device sizes. With the guidance above, you should be able to implement and maintain breakpoint‑based layouts without surprises.

# Schema - raw
{"schema":{"type":"object","required":["breakpoint","style"],"additionalProperties":false,"properties":{"breakpoint":{"description":"Width (in pixels) below which container will display small child, and at and above which will display large child","type":"number","default":640},"style":{"$ref":"urn:ignition-schema:schemas/style-properties.schema.json"},"determinant":{"description":"The dimension in which to break.","type":"string","enum":["width","height"],"default":"width"}}},"resources":[{"type":"css","path":"/res/perspective/css/PerspectiveComponents.css","name":"perspective-components-css"},{"type":"js","path":"/res/perspective/js/PerspectiveComponents.js","name":"perspective-components-js"}],"defaultMetaName":"BreakpointContainer","name":"Breakpoint Container","palette":{"variants":[{"tooltip":"A simple container whose purpose is to swap subcontainers based on a ‘breakpoint’ in pixels.","label":"Breakpoint"}],"category":"container"},"id":"ia.container.breakpt","childPositionSchema":{"type":"object","required":["size"],"additionalProperties":false,"properties":{"size":{"type":"string","enum":["small","large"],"default":"small"}}}}