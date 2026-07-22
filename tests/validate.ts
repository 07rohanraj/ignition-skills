import * as path from 'path';
import { validateAllSkills, validateSkillRegistry } from '../src/validator';

const SKILLS_DIR = path.join(__dirname, '..', 'skills');

console.log('=== Ignition Skills Validation ===\n');

console.log('1. Validating skill registry structure...');
const registryResult = validateSkillRegistry();

if (!registryResult.valid) {
  console.error('\nRegistry validation failed:');
  for (const error of registryResult.errors) {
    console.error(`  - ${error}`);
  }
  process.exit(1);
}

console.log('\n2. Validating skill files...');
const filesResult = validateAllSkills(SKILLS_DIR);

if (!filesResult.valid) {
  console.error('\nFile validation failed:');
  for (const error of filesResult.errors) {
    console.error(`  - ${error}`);
  }
  process.exit(1);
}

console.log('\n✅ All validations passed!');
