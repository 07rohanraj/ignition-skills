# ignition-skills

Comprehensive Perspective component documentation and skills for Ignition SCADA development.

## Overview

This package provides detailed documentation for all Ignition Perspective components, organized into categories for easy reference. Each skill includes:

- Component description and purpose
- Property configurations with types and defaults
- Event handling and scripting
- Best practices and helpful tips
- Raw JSON schema definitions

## Installation

```bash
npm install ignition-skills
```

## Usage

### Programmatic Access

```typescript
import {
  getAllSkills,
  getSkillsByCategory,
  loadSkillContent,
  searchSkills,
  getSkillsForTask
} from 'ignition-skills';

// Get all available skills
const allSkills = getAllSkills();

// Get skills by category
const containerSkills = getSkillsByCategory('containers');

// Search for skills
const results = searchSkills('table');

// Get skills for a specific task
const viewSkills = getSkillsForTask('create view');

// Load a specific skill's content
const skillContent = loadSkillContent('perspective-button');
if (skillContent) {
  console.log(skillContent.description);
  console.log(skillContent.documentation);
}
```

### Direct File Access

Skills are also available as markdown files in the `skills/` directory:

```
skills/
├── SKILL.md                    # Master routing document
├── fundamentals/               # View construction basics
├── containers/                 # Layout components
├── display/                    # Display components
├── input/                      # Input components
├── buttons/                    # Button & navigation
├── gauges/                     # Gauges & indicators
├── charts/                     # Chart components
├── industrial/                 # Industrial symbols
├── alarms/                     # Alarm components
├── forms/                      # Forms & schedules
├── embedded/                   # Embedded views
├── bindings/                   # Data bindings
└── transforms/                 # Data transforms
```

## Skill Categories

| Category | Description | Count |
|----------|-------------|-------|
| fundamentals | View construction basics | 6 |
| containers | Layout components | 10 |
| display | Display components | 16 |
| input | Input components | 13 |
| buttons | Button & navigation | 5 |
| gauges | Gauges & indicators | 6 |
| charts | Chart components | 6 |
| industrial | Industrial symbols | 6 |
| alarms | Alarm components | 2 |
| forms | Forms & schedules | 2 |
| embedded | Embedded views | 2 |
| bindings | Data bindings | 8 |
| transforms | Data transforms | 4 |

**Total: 86 skills**

## API Reference

### Types

```typescript
type SkillCategory =
  | 'fundamentals'
  | 'containers'
  | 'display'
  | 'input'
  | 'buttons'
  | 'gauges'
  | 'charts'
  | 'industrial'
  | 'alarms'
  | 'forms'
  | 'embedded'
  | 'bindings'
  | 'transforms';

interface SkillMetadata {
  id: string;
  name: string;
  category: SkillCategory;
  description: string;
  filePath: string;
  tags: string[];
}

interface SkillContent {
  metadata: SkillMetadata;
  raw: string;
  description: string;
  documentation: string;
  schema?: string;
}
```

### Functions

#### `getAllSkills()`
Returns an array of all skill metadata objects.

#### `getSkillsByCategory(category: SkillCategory)`
Returns an array of skills in the specified category.

#### `searchSkills(query: string)`
Searches skills by name, description, or tags.

#### `getSkillsForTask(task: string)`
Returns skill IDs relevant to a specific task (e.g., "create view", "style component").

#### `loadSkillContent(skillId: string)`
Loads the full content of a skill, including parsed description, documentation, and schema.

#### `getSkillMetadata(skillId: string)`
Returns metadata for a specific skill.

## Development

### Build

```bash
npm run build
```

### Validate Skills

```bash
npm run validate
```

### Type Check

```bash
npm run lint
```

## Contributing

1. Add new skill markdown files to the appropriate category directory
2. Update the skill registry in `src/loader.ts`
3. Update `skills/SKILL.md` with the new skill entry
4. Run validation to ensure everything is correct

## License

MIT
