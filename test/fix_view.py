import json
import re

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'

with open(path, 'r') as f:
    content = f.read()

# Find duplicate props blocks by looking for patterns like:
# "props": { ... },
# "type": "ia.container.flex",
# "props": { ... },
# We need to merge them

# Strategy: find all "props" occurrences and check for duplicates at same nesting
lines = content.split('\n')
for i, line in enumerate(lines):
    stripped = line.strip()
    if '"props"' in stripped and '{' in stripped:
        indent = len(line) - len(line.lstrip())
        print(f'Line {i+1}: indent={indent}, content={stripped[:80]}')
