import * as fs from 'fs';
import * as path from 'path';
import { SkillMetadata, ValidationResult, SkillCategory } from './types';
import { getAllSkills, loadSkillContent } from './loader';

const REQUIRED_SECTIONS = ['Description', 'Documentation'];

const VALID_CATEGORIES: SkillCategory[] = [
  'fundamentals',
  'containers',
  'display',
  'input',
  'buttons',
  'gauges',
  'charts',
  'industrial',
  'alarms',
  'forms',
  'embedded',
  'bindings',
  'transforms'
];

export function validateSkillFile(metadata: SkillMetadata, basePath?: string): ValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];

  const content = loadSkillContent(metadata.id, basePath);

  if (!content) {
    errors.push(`Could not load skill file: ${metadata.filePath}`);
    return { valid: false, errors, warnings };
  }

  // Validate metadata
  if (!metadata.id || metadata.id.trim() === '') {
    errors.push('Skill ID is empty');
  }

  if (!metadata.name || metadata.name.trim() === '') {
    errors.push('Skill name is empty');
  }

  if (!VALID_CATEGORIES.includes(metadata.category)) {
    errors.push(`Invalid category: ${metadata.category}`);
  }

  if (!metadata.description || metadata.description.trim() === '') {
    warnings.push('Skill description is empty');
  }

  if (!metadata.filePath || metadata.filePath.trim() === '') {
    errors.push('Skill file path is empty');
  }

  // Validate content structure
  if (!content.raw || content.raw.trim() === '') {
    errors.push('Skill file is empty');
    return { valid: false, errors, warnings };
  }

  // Check for required sections
  for (const section of REQUIRED_SECTIONS) {
    const regex = new RegExp(`## ${section}`, 'i');
    if (!regex.test(content.raw)) {
      warnings.push(`Missing recommended section: ${section}`);
    }
  }

  // Check for Description section content
  if (!content.description || content.description.trim() === '') {
    warnings.push('Description section is empty');
  }

  // Check for Documentation section content
  if (!content.documentation || content.documentation.trim() === '') {
    warnings.push('Documentation section is empty');
  }

  // Check for Schema section (optional but recommended)
  if (!content.schema) {
    warnings.push('No schema section found (recommended for components)');
  }

  // Validate file exists
  const skillsDir = basePath || path.join(__dirname, '..', 'skills');
  const filePath = path.join(skillsDir, metadata.filePath);
  if (!fs.existsSync(filePath)) {
    errors.push(`File does not exist: ${filePath}`);
  }

  return {
    valid: errors.length === 0,
    errors,
    warnings
  };
}

export function validateAllSkills(basePath?: string): ValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  const skills = getAllSkills();

  console.log(`Validating ${skills.length} skills...\n`);

  for (const skill of skills) {
    const result = validateSkillFile(skill, basePath);

    if (!result.valid) {
      console.error(`❌ ${skill.id}:`);
      for (const error of result.errors) {
        console.error(`   - ${error}`);
        errors.push(`${skill.id}: ${error}`);
      }
    } else if (result.warnings.length > 0) {
      console.warn(`⚠️  ${skill.id}:`);
      for (const warning of result.warnings) {
        console.warn(`   - ${warning}`);
        warnings.push(`${skill.id}: ${warning}`);
      }
    } else {
      console.log(`✅ ${skill.id}`);
    }
  }

  console.log('\n--- Validation Summary ---');
  console.log(`Total skills: ${skills.length}`);
  console.log(`Errors: ${errors.length}`);
  console.log(`Warnings: ${warnings.length}`);

  return {
    valid: errors.length === 0,
    errors,
    warnings
  };
}

export function validateSkillRegistry(): ValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  const skills = getAllSkills();

  // Check for duplicate IDs
  const ids = skills.map(s => s.id);
  const uniqueIds = new Set(ids);
  if (uniqueIds.size !== ids.length) {
    errors.push('Duplicate skill IDs found');
  }

  // Check for duplicate file paths
  const paths = skills.map(s => s.filePath);
  const uniquePaths = new Set(paths);
  if (uniquePaths.size !== paths.length) {
    errors.push('Duplicate file paths found');
  }

  // Check category distribution
  const categoryCounts: Record<string, number> = {};
  for (const skill of skills) {
    categoryCounts[skill.category] = (categoryCounts[skill.category] || 0) + 1;
  }

  console.log('Category distribution:');
  for (const [category, count] of Object.entries(categoryCounts)) {
    console.log(`  ${category}: ${count}`);
  }

  return {
    valid: errors.length === 0,
    errors,
    warnings
  };
}
