import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
with open(path) as f:
    raw = f.read()

# Find all type:"tag" bindings with expressions in tagPath
import re
# Find tagPath values that contain expression logic
for m in re.finditer(r'"type":\s*"tag"', raw):
    start = max(0, m.start() - 500)
    end = min(len(raw), m.end() + 200)
    context = raw[start:end]
    # Find the tagPath
    tp = re.search(r'"tagPath":\s*"([^"]*)"', context)
    if tp:
        tag = tp.group(1)
        if '+' in tag or 'if(' in tag or 'str(' in tag:
            # Find component name
            name_m = re.search(r'"name":\s*"([^"]*)"', raw[start:m.start()])
            name = name_m.group(1) if name_m else '?'
            print(f'PROBLEM: {name} has tag binding with expression: {tag[:100]}')

# Find all component types
for m in re.finditer(r'"type":\s*"(ia\.[^"]*)"', raw):
    t = m.group(1)
    if 'alarm' in t.lower() or 'status' in t.lower():
        start = max(0, m.start() - 200)
        context = raw[start:m.end()]
        name_m = re.search(r'"name":\s*"([^"]*)"', context)
        name = name_m.group(1) if name_m else '?'
        print(f'ALARM TYPE: {name} -> {t}')
