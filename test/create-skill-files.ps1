$ErrorActionPreference = 'Stop'
$base = '.opencode/skills/ignition-perspective-skills'

$skills = @(
  @{ cat = 'fundamentals'; src = 'How to build a new Perspective View.md'; name = 'perspective-build-view'; desc = 'Building a new Perspective view from scratch (view.json, root container, params, propConfig). Use when creating a new view or starting a Perspective view build.' },
  @{ cat = 'fundamentals'; src = 'Perspective Default Component JSON Configs.md'; name = 'perspective-default-configs'; desc = 'Default JSON configs for any Perspective component. Use when you need a component default view.json schema or default property values.' },
  @{ cat = 'fundamentals'; src = 'Ignition Named Query.md'; name = 'perspective-named-query'; desc = 'Creating, editing, and using Ignition Named Queries (SQL, parameters, resource.json, dataset/json/scalar returns). Use when creating or modifying Named Queries for Query bindings or system.db.runNamedQuery.' },
  @{ cat = 'fundamentals'; src = 'Perspective Docks.md'; name = 'perspective-docks'; desc = 'Perspective Docks (header, footer, left, right, page-config, navigation). Use when creating or modifying docks or implementing navigation with docks.' },
  @{ cat = 'fundamentals'; src = 'Perspective CSS Properties.md'; name = 'perspective-css-properties'; desc = 'Perspective CSS properties (style objects, classes, stylesheet.css, selectors). Use when styling components or writing stylesheet CSS.' },
  @{ cat = 'fundamentals'; src = 'Perspective Component Meta Properties.md'; name = 'perspective-component-meta'; desc = 'Perspective component meta properties (name, visible, tooltip, hotkey, styleClass, meta). Use when setting component meta properties or locating the component tree in view.json.' },
  @{ cat = 'fundamentals'; src = 'Perspective Container - Child Item Position Properties.md'; name = 'perspective-container-child-position'; desc = 'Perspective container child item position properties (x, y, width, height, margin, coordinate container). Use when positioning children inside a container.' },

  @{ cat = 'bindings'; src = 'Perspective Query Binding.md'; name = 'perspective-query-binding'; desc = 'Perspective Query Binding that executes a Named Query. Use when binding a component property to database results via queryPath, parameters, polling, and returnFormat.' },
  @{ cat = 'bindings'; src = 'Perspective Tag Binding.md'; name = 'perspective-tag-binding'; desc = 'Perspective Tag Binding to Ignition tags. Use when binding a component property to a tag value via tagPath.' },
  @{ cat = 'bindings'; src = 'Perspective Expression Binding.md'; name = 'perspective-expression-binding'; desc = 'Perspective Expression Binding. Use when binding a property to a computed expression string using functions, operators, and property references.' },
  @{ cat = 'bindings'; src = 'Perspective Property Binding.md'; name = 'perspective-property-binding'; desc = 'Perspective Property Binding linking properties. Use when binding one component property to another component or view property.' },
  @{ cat = 'bindings'; src = 'Perspective Tag History Binding.md'; name = 'perspective-tag-history-binding'; desc = 'Perspective Tag History Binding. Use when binding to historical tag data over a time range (tagPath, date range, aggregation).' },

  @{ cat = 'transforms'; src = 'Perspective Script Transform.md'; name = 'perspective-script-transform'; desc = 'Perspective Script Transform using Jython 2.7. Use when transforming a binding value with script code (return value).' },
  @{ cat = 'transforms'; src = 'Perspective Expression Transform.md'; name = 'perspective-expression-transform'; desc = 'Perspective Expression Transform. Use when transforming a binding value with an expression.' },
  @{ cat = 'transforms'; src = 'Perspective Format Transform.md'; name = 'perspective-format-transform'; desc = 'Perspective Format Transform. Use when formatting binding values (numbers, dates, strings) for display.' },
  @{ cat = 'transforms'; src = 'Perspective Map Transform.md'; name = 'perspective-map-transform'; desc = 'Perspective Map Transform. Use when mapping input values to output values (input/output map, default value).' },

  @{ cat = 'containers'; src = 'Perspective Flex Container.md'; name = 'perspective-flex-container'; desc = 'Perspective Flex Container (ia.container.flex). Use when building responsive/dynamic layouts with flex children.' },
  @{ cat = 'containers'; src = 'Perspective Column Container.md'; name = 'perspective-column-container'; desc = 'Perspective Column Container (ia.container.column). Use when building responsive column layouts.' },

  @{ cat = 'charts'; src = 'Perspective Time Series Chart Component.md'; name = 'perspective-time-series-chart'; desc = 'Perspective Time Series Chart (ia.chart.timeseries) for time-based data. Use when charting OEE, KPI, or trends over time with series and trends.' },
  @{ cat = 'charts'; src = 'Perspective XY Chart Component.md'; name = 'perspective-xy-chart'; desc = 'Perspective XY Chart (ia.chart.xy) for scatter, line, and column plots. Use when plotting x/y data with dataSources and axes.' },
  @{ cat = 'charts'; src = 'Perspective Power Chart Component.md'; name = 'perspective-power-chart'; desc = 'Perspective Power Chart (ia.chart.power) advanced time-series. Use when you need pan, zoom, tooltips, and aggregated historical charting.' },

  @{ cat = 'display'; src = 'Perspective Label Component.md'; name = 'perspective-label'; desc = 'Perspective Label component (ia.display.label) for displaying text. Use when showing text, numbers, or values on screen.' },
  @{ cat = 'display'; src = 'Perspective Table Component.md'; name = 'perspective-table'; desc = 'Perspective Table component (ia.display.table) for tabular data. Use when displaying datasets or query results in rows and columns.' },
  @{ cat = 'display'; src = 'Perspective Icon Component.md'; name = 'perspective-icon'; desc = 'Perspective Icon component (ia.display.icon) for SVG or URL icons. Use when displaying an icon or image glyph.' },

  @{ cat = 'input'; src = 'Perspective Text Field Component.md'; name = 'perspective-text-field'; desc = 'Perspective Text Field (ia.input.text-field) for single-line text input. Use when collecting text entry.' },
  @{ cat = 'input'; src = 'Perspective Text Area Component.md'; name = 'perspective-text-area'; desc = 'Perspective Text Area (ia.input.text-area) for multi-line text input. Use when collecting longer text entry.' },
  @{ cat = 'input'; src = 'Perspective Numeric Entry Field Component.md'; name = 'perspective-numeric-entry'; desc = 'Perspective Numeric Entry Field (ia.input.numeric-field) for numeric input. Use when collecting numbers.' },
  @{ cat = 'input'; src = 'Perspective Dropdown Component.md'; name = 'perspective-dropdown'; desc = 'Perspective Dropdown (ia.input.dropdown) for selecting one option from a list. Use when binding options, value, and placeholder.' },
  @{ cat = 'input'; src = 'Perspective DateTime Picker Component.md'; name = 'perspective-datetime-picker'; desc = 'Perspective DateTime Picker (ia.input.date-time-picker) for date and time selection. Use when collecting a date or timestamp.' },
  @{ cat = 'input'; src = 'Perspective Checkbox Component.md'; name = 'perspective-checkbox'; desc = 'Perspective Checkbox (ia.input.checkbox) for boolean or three-state input. Use when collecting true/false values.' },

  @{ cat = 'buttons'; src = 'Perspective Button Component.md'; name = 'perspective-button'; desc = 'Perspective Button (ia.input.button) for actions and events. Use when adding a button and handling onActionPerformed events.' }
)

foreach ($s in $skills) {
  $srcFile = Join-Path $base (Join-Path $s.cat $s.src)
  if (-not (Test-Path -LiteralPath $srcFile)) { Write-Error "MISSING: $srcFile"; continue }
  $dir = Join-Path $base (Join-Path $s.cat $s.name)
  New-Item -ItemType Directory -Path $dir -Force | Out-Null
  $content = Get-Content -LiteralPath $srcFile -Raw
  $fm = "---`nname: $($s.name)`ndescription: $($s.desc)`n---`n`n"
  Set-Content -LiteralPath (Join-Path $dir 'SKILL.md') -Value ($fm + $content) -Encoding utf8
  Remove-Item -LiteralPath $srcFile
  Write-Output "CREATED: $($s.cat)/$($s.name)/SKILL.md  (removed $($s.src))"
}
