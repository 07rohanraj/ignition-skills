export {
  SkillMetadata,
  SkillContent,
  SkillCategory,
  SkillRoute,
  SkillCategoryInfo,
  LoadOptions,
  ValidationResult
} from './types';

export {
  getSkillMetadata,
  getSkillsByCategory,
  getAllSkills,
  searchSkills,
  loadSkillContent
} from './loader';

export {
  validateSkillFile,
  validateAllSkills,
  validateSkillRegistry
} from './validator';

import { SkillCategory } from './types';
import { getSkillsByCategory } from './loader';

export const CATEGORIES: Record<SkillCategory, { name: string; description: string }> = {
  fundamentals: {
    name: 'View Construction & Fundamentals',
    description: 'Core concepts for building Perspective views'
  },
  containers: {
    name: 'Containers',
    description: 'Layout and container components'
  },
  display: {
    name: 'Display Components',
    description: 'Components for displaying data and content'
  },
  input: {
    name: 'Input Components',
    description: 'Components for user input'
  },
  buttons: {
    name: 'Button & Navigation Components',
    description: 'Buttons and navigation elements'
  },
  gauges: {
    name: 'Gauge & Indicator Components',
    description: 'Visual indicators and gauges'
  },
  charts: {
    name: 'Chart Components',
    description: 'Data visualization charts'
  },
  industrial: {
    name: 'Industrial Symbol Components',
    description: 'Industrial equipment symbols'
  },
  alarms: {
    name: 'Alarm Components',
    description: 'Alarm display and management'
  },
  forms: {
    name: 'Form & Schedule Components',
    description: 'Forms and scheduling components'
  },
  embedded: {
    name: 'Embedded Views & Repeaters',
    description: 'View embedding and repetition'
  },
  bindings: {
    name: 'Bindings (Data Connections)',
    description: 'Data binding configurations'
  },
  transforms: {
    name: 'Transforms (Data Manipulation)',
    description: 'Data transformation operations'
  }
};

export function getCategoryInfo(category: SkillCategory) {
  return CATEGORIES[category];
}

export function getSkillsForTask(task: string): string[] {
  const taskLower = task.toLowerCase();

  const taskSkillMap: Record<string, string[]> = {
    'create view': ['perspective-build-view', 'perspective-default-configs'],
    'style component': ['perspective-css-properties'],
    'add table': ['perspective-table', 'perspective-tag-binding'],
    'create form': ['perspective-form-config'],
    'display chart': ['perspective-time-series-chart', 'perspective-pie-chart'],
    'industrial graphics': ['perspective-motor-symbol', 'perspective-pump-symbol'],
    'connect tags': ['perspective-tag-binding'],
    'connect database': ['perspective-query-binding'],
    'connect api': ['perspective-http-binding'],
    'transform data': ['perspective-expression-transform', 'perspective-script-transform'],
    'responsive layout': ['perspective-flex-container', 'perspective-column-container'],
    'add navigation': ['perspective-horizontal-menu', 'perspective-link'],
    'embed views': ['perspective-embedded-view', 'perspective-flex-repeater'],
    'display alarms': ['perspective-alarm-status-table', 'perspective-alarm-journal-table']
  };

  for (const [key, skills] of Object.entries(taskSkillMap)) {
    if (taskLower.includes(key.toLowerCase())) {
      return skills;
    }
  }

  return [];
}
