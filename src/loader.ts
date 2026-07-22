import * as fs from 'fs';
import * as path from 'path';
import { SkillMetadata, SkillContent, SkillCategory, LoadOptions } from './types';

const SKILLS_DIR = path.join(__dirname, '..', 'skills');

const SKILL_REGISTRY: Record<string, SkillMetadata> = {
  // Fundamentals
  'perspective-build-view': {
    id: 'perspective-build-view',
    name: 'How to build a new Perspective View',
    category: 'fundamentals',
    description: 'Step by step guide on how to construct the basic JSON configuration for a new Perspective View.',
    filePath: 'fundamentals/How to build a new Perspective View.md',
    tags: ['view', 'json', 'construction', 'starter']
  },
  'perspective-default-configs': {
    id: 'perspective-default-configs',
    name: 'Perspective Default Component JSON Configs',
    category: 'fundamentals',
    description: 'JSON configuration schema for Ignition Perspective Views.',
    filePath: 'fundamentals/Perspective Default Component JSON Configs.md',
    tags: ['json', 'schema', 'configuration']
  },
  'perspective-component-meta': {
    id: 'perspective-component-meta',
    name: 'Perspective Component Meta Properties',
    category: 'fundamentals',
    description: 'Configuration and usage of component meta properties.',
    filePath: 'fundamentals/Perspective Component Meta Properties.md',
    tags: ['meta', 'name', 'visibility', 'tooltip']
  },
  'perspective-css-properties': {
    id: 'perspective-css-properties',
    name: 'Perspective CSS Properties',
    category: 'fundamentals',
    description: 'How to apply visual styles to components.',
    filePath: 'fundamentals/Perspective CSS Properties.md',
    tags: ['css', 'style', 'styling']
  },
  'perspective-container-child-position': {
    id: 'perspective-container-child-position',
    name: 'Perspective Container Child Item Position Properties',
    category: 'fundamentals',
    description: 'Position properties for child items in containers.',
    filePath: 'fundamentals/Perspective Container - Child Item Position Properties.md',
    tags: ['position', 'layout', 'containers']
  },
  'perspective-create-project': {
    id: 'perspective-create-project',
    name: 'How to create an Ignition Project',
    category: 'fundamentals',
    description: 'Complete guide for creating an Ignition Perspective project from scratch.',
    filePath: 'fundamentals/How to create an Ignition Project.md',
    tags: ['project', 'structure', 'folder', 'configuration']
  },

  // Containers
  'perspective-flex-container': {
    id: 'perspective-flex-container',
    name: 'Perspective Flex Container',
    category: 'containers',
    description: 'Creating dynamic and responsive layouts.',
    filePath: 'containers/Perspective Flex Container.md',
    tags: ['flex', 'layout', 'responsive']
  },
  'perspective-column-container': {
    id: 'perspective-column-container',
    name: 'Perspective Column Container',
    category: 'containers',
    description: 'Screen-size-aware layouts with 12-column grid.',
    filePath: 'containers/Perspective Column Container.md',
    tags: ['column', 'grid', 'responsive']
  },
  'perspective-coordinate-container': {
    id: 'perspective-coordinate-container',
    name: 'Perspective Coordinate Container',
    category: 'containers',
    description: 'Pixel-perfect positioning.',
    filePath: 'containers/Perspective Coordinate Container.md',
    tags: ['coordinate', 'position', 'pixel']
  },
  'perspective-breakpoint-container': {
    id: 'perspective-breakpoint-container',
    name: 'Perspective Breakpoint Container',
    category: 'containers',
    description: 'Responsive view switching.',
    filePath: 'containers/Perspective Breakpoint Container.md',
    tags: ['breakpoint', 'responsive', 'switching']
  },
  'perspective-split-container': {
    id: 'perspective-split-container',
    name: 'Perspective Split Container',
    category: 'containers',
    description: 'Two-panel resizable layout.',
    filePath: 'containers/Perspective Split Container.md',
    tags: ['split', 'resizable', 'panels']
  },
  'perspective-tab-container': {
    id: 'perspective-tab-container',
    name: 'Perspective Tab Container',
    category: 'containers',
    description: 'Tabbed content organization.',
    filePath: 'containers/Perspective Tab Container.md',
    tags: ['tab', 'tabs', 'organization']
  },
  'perspective-carousel-container': {
    id: 'perspective-carousel-container',
    name: 'Perspective Carousel Container',
    category: 'containers',
    description: 'Slideshow/cycling views.',
    filePath: 'containers/Perspective Carousel Container.md',
    tags: ['carousel', 'slideshow', 'cycling']
  },
  'perspective-dashboard': {
    id: 'perspective-dashboard',
    name: 'Perspective Dashboard Component',
    category: 'containers',
    description: 'User-arrangeable widgets.',
    filePath: 'containers/Perspective Dashboard Component.md',
    tags: ['dashboard', 'widgets', 'arrangeable']
  },
  'perspective-accordion': {
    id: 'perspective-accordion',
    name: 'Perspective Accordion Component',
    category: 'containers',
    description: 'Collapsible sections.',
    filePath: 'containers/Perspective Accordion Component.md',
    tags: ['accordion', 'collapsible', 'sections']
  },
  'perspective-view-canvas': {
    id: 'perspective-view-canvas',
    name: 'Perspective View Canvas Component',
    category: 'containers',
    description: 'Coordinate-based multi-view layout.',
    filePath: 'containers/Perspective View Canvas Component.md',
    tags: ['canvas', 'coordinate', 'multi-view']
  },

  // Display
  'perspective-label': {
    id: 'perspective-label',
    name: 'Perspective Label Component',
    category: 'display',
    description: 'Displaying text.',
    filePath: 'display/Perspective Label Component.md',
    tags: ['label', 'text', 'display']
  },
  'perspective-markdown': {
    id: 'perspective-markdown',
    name: 'Perspective Markdown Component',
    category: 'display',
    description: 'Rich text rendering.',
    filePath: 'display/Perspective Markdown Component.md',
    tags: ['markdown', 'rich-text', 'html']
  },
  'perspective-icon': {
    id: 'perspective-icon',
    name: 'Perspective Icon Component',
    category: 'display',
    description: 'SVG icons.',
    filePath: 'display/Perspective Icon Component.md',
    tags: ['icon', 'svg', 'material']
  },
  'perspective-image': {
    id: 'perspective-image',
    name: 'Perspective Image Component',
    category: 'display',
    description: 'Displaying images.',
    filePath: 'display/Perspective Image Component.md',
    tags: ['image', 'picture', 'photo']
  },
  'perspective-led-display': {
    id: 'perspective-led-display',
    name: 'Perspective LED Display Component',
    category: 'display',
    description: 'LED-style readouts.',
    filePath: 'display/Perspective LED Display Component.md',
    tags: ['led', 'display', 'digital']
  },
  'perspective-table': {
    id: 'perspective-table',
    name: 'Perspective Table Component',
    category: 'display',
    description: 'Tabular data display.',
    filePath: 'display/Perspective Table Component.md',
    tags: ['table', 'data', 'grid', 'rows']
  },
  'perspective-tree': {
    id: 'perspective-tree',
    name: 'Perspective Tree Component',
    category: 'display',
    description: 'Hierarchical data.',
    filePath: 'display/Perspective Tree Component.md',
    tags: ['tree', 'hierarchy', 'nested']
  },
  'perspective-menu-tree': {
    id: 'perspective-menu-tree',
    name: 'Perspective Menu Tree Component',
    category: 'display',
    description: 'Navigation menus.',
    filePath: 'display/Perspective Menu Tree Component.md',
    tags: ['menu', 'tree', 'navigation']
  },
  'perspective-tag-browse-tree': {
    id: 'perspective-tag-browse-tree',
    name: 'Perspective Tag Browse Tree Component',
    category: 'display',
    description: 'Tag browsing.',
    filePath: 'display/Perspective Tag Browse Tree Component.md',
    tags: ['tag', 'browse', 'tree']
  },
  'perspective-inline-frame': {
    id: 'perspective-inline-frame',
    name: 'Perspective Inline Frame Component',
    category: 'display',
    description: 'External web content.',
    filePath: 'display/Perspective Inline Frame Component.md',
    tags: ['iframe', 'web', 'external']
  },
  'perspective-pdf-viewer': {
    id: 'perspective-pdf-viewer',
    name: 'Perspective PDF Viewer Component',
    category: 'display',
    description: 'PDF display.',
    filePath: 'display/Perspective PDF Viewer Component.md',
    tags: ['pdf', 'viewer', 'document']
  },
  'perspective-video-player': {
    id: 'perspective-video-player',
    name: 'Perspective Video Player Component',
    category: 'display',
    description: 'Video playback.',
    filePath: 'display/Perspective Video Player Component.md',
    tags: ['video', 'player', 'media']
  },
  'perspective-audio': {
    id: 'perspective-audio',
    name: 'Perspective Audio Component',
    category: 'display',
    description: 'Audio playback.',
    filePath: 'display/Perspective Audio Component.md',
    tags: ['audio', 'sound', 'media']
  },
  'perspective-barcode-display': {
    id: 'perspective-barcode-display',
    name: 'Perspective Barcode Display Component',
    category: 'display',
    description: 'Barcode/QR display.',
    filePath: 'display/Perspective Barcode Display Component.md',
    tags: ['barcode', 'qr', 'code']
  },
  'perspective-signature-pad': {
    id: 'perspective-signature-pad',
    name: 'Perspective Signature Pad Component',
    category: 'display',
    description: 'Signature capture.',
    filePath: 'display/Perspective Signature Pad Component.md',
    tags: ['signature', 'draw', 'capture']
  },
  'perspective-file-upload': {
    id: 'perspective-file-upload',
    name: 'Perspective File Upload Component',
    category: 'display',
    description: 'File upload.',
    filePath: 'display/Perspective File Upload Component.md',
    tags: ['file', 'upload', 'transfer']
  },

  // Input
  'perspective-text-field': {
    id: 'perspective-text-field',
    name: 'Perspective Text Field Component',
    category: 'input',
    description: 'Single-line text input.',
    filePath: 'input/Perspective Text Field Component.md',
    tags: ['text', 'input', 'field']
  },
  'perspective-text-area': {
    id: 'perspective-text-area',
    name: 'Perspective Text Area Component',
    category: 'input',
    description: 'Multi-line text input.',
    filePath: 'input/Perspective Text Area Component.md',
    tags: ['text', 'area', 'multiline']
  },
  'perspective-numeric-entry': {
    id: 'perspective-numeric-entry',
    name: 'Perspective Numeric Entry Field Component',
    category: 'input',
    description: 'Numeric input.',
    filePath: 'input/Perspective Numeric Entry Field Component.md',
    tags: ['numeric', 'number', 'input']
  },
  'perspective-password-field': {
    id: 'perspective-password-field',
    name: 'Perspective Password Field Component',
    category: 'input',
    description: 'Password input.',
    filePath: 'input/Perspective Password Field Component.md',
    tags: ['password', 'secure', 'input']
  },
  'perspective-dropdown': {
    id: 'perspective-dropdown',
    name: 'Perspective Dropdown Component',
    category: 'input',
    description: 'Selection from list.',
    filePath: 'input/Perspective Dropdown Component.md',
    tags: ['dropdown', 'select', 'list']
  },
  'perspective-checkbox': {
    id: 'perspective-checkbox',
    name: 'Perspective Checkbox Component',
    category: 'input',
    description: 'Boolean/three-state.',
    filePath: 'input/Perspective Checkbox Component.md',
    tags: ['checkbox', 'boolean', 'toggle']
  },
  'perspective-radio-group': {
    id: 'perspective-radio-group',
    name: 'Perspective Radio Group Component',
    category: 'input',
    description: 'Single selection from options.',
    filePath: 'input/Perspective Radio Group Component.md',
    tags: ['radio', 'group', 'selection']
  },
  'perspective-toggle-switch': {
    id: 'perspective-toggle-switch',
    name: 'Perspective Toggle Switch Component',
    category: 'input',
    description: 'On/off toggle.',
    filePath: 'input/Perspective Toggle Switch Component.md',
    tags: ['toggle', 'switch', 'on-off']
  },
  'perspective-slider': {
    id: 'perspective-slider',
    name: 'Perspective Slider Component',
    category: 'input',
    description: 'Range value selection.',
    filePath: 'input/Perspective Slider Component.md',
    tags: ['slider', 'range', 'value']
  },
  'perspective-datetime-input': {
    id: 'perspective-datetime-input',
    name: 'Perspective DateTime Input Component',
    category: 'input',
    description: 'Date/time selection.',
    filePath: 'input/Perspective DateTime Input Component.md',
    tags: ['date', 'time', 'input']
  },
  'perspective-datetime-picker': {
    id: 'perspective-datetime-picker',
    name: 'Perspective DateTime Picker Component',
    category: 'input',
    description: 'Full date/time picker.',
    filePath: 'input/Perspective DateTime Picker Component.md',
    tags: ['date', 'time', 'picker']
  },
  'perspective-barcode-scanner': {
    id: 'perspective-barcode-scanner',
    name: 'Perspective Barcode Scanner Input Component',
    category: 'input',
    description: 'Barcode scanning.',
    filePath: 'input/Perspective Barcode Scanner Input Component.md',
    tags: ['barcode', 'scanner', 'input']
  },
  'perspective-google-map': {
    id: 'perspective-google-map',
    name: 'Perspective Google Map Component',
    category: 'input',
    description: 'Geographic display.',
    filePath: 'input/Perspective Google Map Component.md',
    tags: ['map', 'google', 'geographic']
  },

  // Buttons
  'perspective-button': {
    id: 'perspective-button',
    name: 'Perspective Button Component',
    category: 'buttons',
    description: 'Action button.',
    filePath: 'buttons/Perspective Button Component.md',
    tags: ['button', 'action', 'click']
  },
  'perspective-one-shot-button': {
    id: 'perspective-one-shot-button',
    name: 'Perspective One-Shot Button Component',
    category: 'buttons',
    description: 'Single-trigger button.',
    filePath: 'buttons/Perspective One-Shot Button Component.md',
    tags: ['button', 'one-shot', 'single']
  },
  'perspective-multi-state-button': {
    id: 'perspective-multi-state-button',
    name: 'Perspective Multi-State Button Component',
    category: 'buttons',
    description: 'Equipment mode control.',
    filePath: 'buttons/Perspective Multi-State Button Component.md',
    tags: ['button', 'multi-state', 'mode']
  },
  'perspective-horizontal-menu': {
    id: 'perspective-horizontal-menu',
    name: 'Perspective Horizontal Menu Component',
    category: 'buttons',
    description: 'Top navigation.',
    filePath: 'buttons/Perspective Horizontal Menu Component.md',
    tags: ['menu', 'horizontal', 'navigation']
  },
  'perspective-link': {
    id: 'perspective-link',
    name: 'Perspective Link Component',
    category: 'buttons',
    description: 'Hyperlink.',
    filePath: 'buttons/Perspective Link Component.md',
    tags: ['link', 'hyperlink', 'navigation']
  },

  // Gauges
  'perspective-gauge': {
    id: 'perspective-gauge',
    name: 'Perspective Gauge Component',
    category: 'gauges',
    description: 'Dial/arc value display.',
    filePath: 'gauges/Perspective Gauge Component.md',
    tags: ['gauge', 'dial', 'arc']
  },
  'perspective-simple-gauge': {
    id: 'perspective-simple-gauge',
    name: 'Perspective Simple Gauge Component',
    category: 'gauges',
    description: 'Modern arc gauge.',
    filePath: 'gauges/Perspective Simple Gauge Component.md',
    tags: ['gauge', 'simple', 'arc']
  },
  'perspective-thermometer': {
    id: 'perspective-thermometer',
    name: 'Perspective Thermometer Component',
    category: 'gauges',
    description: 'Temperature display.',
    filePath: 'gauges/Perspective Thermometer Component.md',
    tags: ['thermometer', 'temperature', 'display']
  },
  'perspective-linear-scale': {
    id: 'perspective-linear-scale',
    name: 'Perspective Linear Scale Component',
    category: 'gauges',
    description: 'Linear axis display.',
    filePath: 'gauges/Perspective Linear Scale Component.md',
    tags: ['linear', 'scale', 'axis']
  },
  'perspective-moving-analog': {
    id: 'perspective-moving-analog',
    name: 'Perspective Moving Analog Indicator',
    category: 'gauges',
    description: 'Colored scale indicator.',
    filePath: 'gauges/Perspective Moving Analog Indicator.md',
    tags: ['analog', 'indicator', 'scale']
  },
  'perspective-progress-indicator': {
    id: 'perspective-progress-indicator',
    name: 'Perspective Progress Indicator Component',
    category: 'gauges',
    description: 'Progress bar.',
    filePath: 'gauges/Perspective Progress Indicator Component.md',
    tags: ['progress', 'bar', 'indicator']
  },

  // Charts
  'perspective-time-series-chart': {
    id: 'perspective-time-series-chart',
    name: 'Perspective Time Series Chart Component',
    category: 'charts',
    description: 'Time-based data.',
    filePath: 'charts/Perspective Time Series Chart Component.md',
    tags: ['chart', 'time-series', 'trend']
  },
  'perspective-power-chart': {
    id: 'perspective-power-chart',
    name: 'Perspective Power Chart Component',
    category: 'charts',
    description: 'Advanced time-series.',
    filePath: 'charts/Perspective Power Chart Component.md',
    tags: ['chart', 'power', 'advanced']
  },
  'perspective-pie-chart': {
    id: 'perspective-pie-chart',
    name: 'Perspective Pie Chart Component',
    category: 'charts',
    description: 'Proportional data.',
    filePath: 'charts/Perspective Pie Chart Component.md',
    tags: ['chart', 'pie', 'proportional']
  },
  'perspective-xy-chart': {
    id: 'perspective-xy-chart',
    name: 'Perspective XY Chart Component',
    category: 'charts',
    description: 'XY scatter/line/column.',
    filePath: 'charts/Perspective XY Chart Component.md',
    tags: ['chart', 'xy', 'scatter', 'line']
  },
  'perspective-sparkline-chart': {
    id: 'perspective-sparkline-chart',
    name: 'Perspective Sparkline Chart Component',
    category: 'charts',
    description: 'Compact trend.',
    filePath: 'charts/Perspective Sparkline Chart Component.md',
    tags: ['chart', 'sparkline', 'compact']
  },
  'perspective-chart-range-selector': {
    id: 'perspective-chart-range-selector',
    name: 'Perspective Chart Range Selector Component',
    category: 'charts',
    description: 'Time range selection.',
    filePath: 'charts/Perspective Chart Range Selector Component.md',
    tags: ['chart', 'range', 'selector']
  },

  // Industrial
  'perspective-motor-symbol': {
    id: 'perspective-motor-symbol',
    name: 'Perspective Motor Symbol Component',
    category: 'industrial',
    description: 'Motor visualization.',
    filePath: 'industrial/Perspective Motor Symbol Component.md',
    tags: ['motor', 'symbol', 'industrial']
  },
  'perspective-pump-symbol': {
    id: 'perspective-pump-symbol',
    name: 'Perspective Pump Symbol Component',
    category: 'industrial',
    description: 'Pump visualization.',
    filePath: 'industrial/Perspective Pump Symbol Component.md',
    tags: ['pump', 'symbol', 'industrial']
  },
  'perspective-valve-symbol': {
    id: 'perspective-valve-symbol',
    name: 'Perspective Valve Symbol Component',
    category: 'industrial',
    description: 'Valve visualization.',
    filePath: 'industrial/Perspective Valve Symbol Component.md',
    tags: ['valve', 'symbol', 'industrial']
  },
  'perspective-vessel-symbol': {
    id: 'perspective-vessel-symbol',
    name: 'Perspective Vessel Symbol Component',
    category: 'industrial',
    description: 'Tank/vessel visualization.',
    filePath: 'industrial/Perspective Vessel Symbol Component.md',
    tags: ['vessel', 'tank', 'symbol']
  },
  'perspective-sensor-symbol': {
    id: 'perspective-sensor-symbol',
    name: 'Perspective Sensor Symbol Component',
    category: 'industrial',
    description: 'Sensor visualization.',
    filePath: 'industrial/Perspective Sensor Symbol Component.md',
    tags: ['sensor', 'symbol', 'industrial']
  },
  'perspective-cylindrical-tank': {
    id: 'perspective-cylindrical-tank',
    name: 'Perspective Cylindrical Tank Component',
    category: 'industrial',
    description: '3D tank fill.',
    filePath: 'industrial/Perspective Cylindrical Tank Component.md',
    tags: ['tank', 'cylindrical', 'fill']
  },

  // Alarms
  'perspective-alarm-status-table': {
    id: 'perspective-alarm-status-table',
    name: 'Perspective Alarm Status Table Component',
    category: 'alarms',
    description: 'Real-time alarms.',
    filePath: 'alarms/Perspective Alarm Status Table Component.md',
    tags: ['alarm', 'status', 'real-time']
  },
  'perspective-alarm-journal-table': {
    id: 'perspective-alarm-journal-table',
    name: 'Perspective Alarm Journal Table Component',
    category: 'alarms',
    description: 'Historical alarms.',
    filePath: 'alarms/Perspective Alarm Journal Table Component.md',
    tags: ['alarm', 'journal', 'historical']
  },

  // Forms
  'perspective-form-config': {
    id: 'perspective-form-config',
    name: 'Perspective Form Component Property Configuration',
    category: 'forms',
    description: 'Building forms.',
    filePath: 'forms/Perspective Form Component Property Configuration.md',
    tags: ['form', 'configuration', 'input']
  },
  'perspective-equipment-schedule': {
    id: 'perspective-equipment-schedule',
    name: 'Perspective Equipment Schedule Component',
    category: 'forms',
    description: 'Time-based scheduling.',
    filePath: 'forms/Perspective Equipment Schedule Component.md',
    tags: ['schedule', 'equipment', 'time']
  },

  // Embedded
  'perspective-embedded-view': {
    id: 'perspective-embedded-view',
    name: 'Perspective Embedded View Component',
    category: 'embedded',
    description: 'Including sub-views.',
    filePath: 'embedded/Perspective Embedded View Component.md',
    tags: ['embedded', 'view', 'sub-view']
  },
  'perspective-flex-repeater': {
    id: 'perspective-flex-repeater',
    name: 'Perspective Flex Repeater Component',
    category: 'embedded',
    description: 'Repeating templates.',
    filePath: 'embedded/Perspective Flex Repeater Component.md',
    tags: ['repeater', 'flex', 'template']
  },

  // Bindings
  'perspective-property-binding': {
    id: 'perspective-property-binding',
    name: 'Perspective Property Binding',
    category: 'bindings',
    description: 'Connect to other components.',
    filePath: 'bindings/Perspective Property Binding.md',
    tags: ['property', 'binding', 'component']
  },
  'perspective-tag-binding': {
    id: 'perspective-tag-binding',
    name: 'Perspective Tag Binding',
    category: 'bindings',
    description: 'Connect to Ignition tags.',
    filePath: 'bindings/Perspective Tag Binding.md',
    tags: ['tag', 'binding', 'ignition']
  },
  'perspective-expression-binding': {
    id: 'perspective-expression-binding',
    name: 'Perspective Expression Binding',
    category: 'bindings',
    description: 'Calculate from expressions.',
    filePath: 'bindings/Perspective Expression Binding.md',
    tags: ['expression', 'binding', 'calculate']
  },
  'perspective-expression-structure-binding': {
    id: 'perspective-expression-structure-binding',
    name: 'Perspective Expression Structure Binding',
    category: 'bindings',
    description: 'Build object from expressions.',
    filePath: 'bindings/Perspective Expression Structure Binding.md',
    tags: ['expression', 'structure', 'object']
  },
  'perspective-query-binding': {
    id: 'perspective-query-binding',
    name: 'Perspective Query Binding',
    category: 'bindings',
    description: 'Connect to database.',
    filePath: 'bindings/Perspective Query Binding.md',
    tags: ['query', 'database', 'sql']
  },
  'perspective-http-binding': {
    id: 'perspective-http-binding',
    name: 'Perspective HTTP Binding',
    category: 'bindings',
    description: 'Connect to REST APIs.',
    filePath: 'bindings/Perspective HTTP Binding.md',
    tags: ['http', 'rest', 'api']
  },
  'perspective-tag-history-binding': {
    id: 'perspective-tag-history-binding',
    name: 'Perspective Tag History Binding',
    category: 'bindings',
    description: 'Historical tag data.',
    filePath: 'bindings/Perspective Tag History Binding.md',
    tags: ['tag', 'history', 'historical']
  },
  'perspective-session-properties': {
    id: 'perspective-session-properties',
    name: 'Perspective Session Properties',
    category: 'bindings',
    description: 'Access session/user info.',
    filePath: 'bindings/Perspective Session Properties.md',
    tags: ['session', 'properties', 'user']
  },

  // Transforms
  'perspective-expression-transform': {
    id: 'perspective-expression-transform',
    name: 'Perspective Expression Transform',
    category: 'transforms',
    description: 'Calculate with expressions.',
    filePath: 'transforms/Perspective Expression Transform.md',
    tags: ['expression', 'transform', 'calculate']
  },
  'perspective-script-transform': {
    id: 'perspective-script-transform',
    name: 'Perspective Script Transform',
    category: 'transforms',
    description: 'Calculate with Python.',
    filePath: 'transforms/Perspective Script Transform.md',
    tags: ['script', 'transform', 'python']
  },
  'perspective-format-transform': {
    id: 'perspective-format-transform',
    name: 'Perspective Format Transform',
    category: 'transforms',
    description: 'Format display.',
    filePath: 'transforms/Perspective Format Transform.md',
    tags: ['format', 'transform', 'display']
  },
  'perspective-map-transform': {
    id: 'perspective-map-transform',
    name: 'Perspective Map Transform',
    category: 'transforms',
    description: 'Map values to outputs.',
    filePath: 'transforms/Perspective Map Transform.md',
    tags: ['map', 'transform', 'values']
  }
};

export function getSkillMetadata(skillId: string): SkillMetadata | undefined {
  return SKILL_REGISTRY[skillId];
}

export function getSkillsByCategory(category: SkillCategory): SkillMetadata[] {
  return Object.values(SKILL_REGISTRY).filter(skill => skill.category === category);
}

export function getAllSkills(): SkillMetadata[] {
  return Object.values(SKILL_REGISTRY);
}

export function searchSkills(query: string): SkillMetadata[] {
  const lowerQuery = query.toLowerCase();
  return Object.values(SKILL_REGISTRY).filter(skill =>
    skill.name.toLowerCase().includes(lowerQuery) ||
    skill.description.toLowerCase().includes(lowerQuery) ||
    skill.tags.some(tag => tag.toLowerCase().includes(lowerQuery))
  );
}

export function loadSkillContent(skillId: string, basePath?: string): SkillContent | null {
  const metadata = SKILL_REGISTRY[skillId];
  if (!metadata) return null;

  const skillsDir = basePath || SKILLS_DIR;
  const filePath = path.join(skillsDir, metadata.filePath);

  try {
    const raw = fs.readFileSync(filePath, 'utf-8');
    const { description, documentation, schema } = parseSkillMarkdown(raw);

    return {
      metadata,
      raw,
      description,
      documentation,
      schema
    };
  } catch {
    return null;
  }
}

function parseSkillMarkdown(content: string): {
  description: string;
  documentation: string;
  schema?: string;
} {
  const descriptionMatch = content.match(/## Description\s*\n([\s\S]*?)(?=\n## |\n# |$)/);
  const documentationMatch = content.match(/## Documentation\s*\n([\s\S]*?)(?=\n# Schema|$)/);
  const schemaMatch = content.match(/# Schema - raw\s*\n([\s\S]*?)$/);

  return {
    description: descriptionMatch?.[1]?.trim() || '',
    documentation: documentationMatch?.[1]?.trim() || '',
    schema: schemaMatch?.[1]?.trim()
  };
}
