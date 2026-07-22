export type SkillCategory =
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

export interface SkillMetadata {
  id: string;
  name: string;
  category: SkillCategory;
  description: string;
  filePath: string;
  tags: string[];
}

export interface SkillContent {
  metadata: SkillMetadata;
  raw: string;
  description: string;
  documentation: string;
  schema?: string;
}

export interface SkillRoute {
  skillId: string;
  whenToUse: string;
  description: string;
}

export interface SkillCategoryInfo {
  id: SkillCategory;
  name: string;
  description: string;
  skills: SkillRoute[];
}

export interface LoadOptions {
  category?: SkillCategory;
  skillId?: string;
  basePath?: string;
}

export interface ValidationResult {
  valid: boolean;
  errors: string[];
  warnings: string[];
}
