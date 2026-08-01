import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

kpi_script = (
    'if value is not None:\n'
    '\treturn str(round(value, 1))\n'
    'return "0.0"'
)

def fix_transforms(node):
    if isinstance(node, dict):
        if 'transforms' in node:
            new_transforms = []
            for t in node['transforms']:
                if t.get('type') == 'format':
                    # Replace format transform with script transform
                    new_transforms.append({
                        "code": kpi_script,
                        "type": "script"
                    })
                else:
                    new_transforms.append(t)
            node['transforms'] = new_transforms
        for k, v in node.items():
            fix_transforms(v)
    elif isinstance(node, list):
        for item in node:
            fix_transforms(item)

fix_transforms(data)

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify
import re
with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    content = f.read()

format_count = len(re.findall(r'"type":\s*"format"', content))
script_count = len(re.findall(r'"type":\s*"script"', content))
print(f'Format transforms remaining: {format_count}')
print(f'Script transforms: {script_count}')

# Show all transforms per binding
print("\nBinding audit:")
data2 = json.loads(content)
def audit(node):
    if isinstance(node, dict):
        if 'transforms' in node:
            name = node.get('meta', {}).get('name', '?')
            types = [t.get('type') for t in node['transforms']]
            print(f'  {name}: {types}')
        for k, v in node.items():
            audit(v)
    elif isinstance(node, list):
        for item in node:
            audit(item)
audit(data2)
