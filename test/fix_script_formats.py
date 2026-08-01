import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

# The correct script formats with def transform and proper tab indentation
kpi_code = (
    'def transform(self, value, quality, timestamp):\n'
    '\tif value is not None:\n'
    '\t\treturn str(round(value, 1))\n'
    '\treturn "0.0"'
)

energy_code = (
    'def transform(self, value, quality, timestamp):\n'
    '\tif value is not None:\n'
    '\t\treturn "Energy: " + str(round(value, 1)) + " kWh"\n'
    '\treturn "Energy: 0.0 kWh"'
)

shift_code = (
    'def transform(self, value, quality, timestamp):\n'
    '\tfrom java.time import LocalTime\n'
    '\thour = LocalTime.now().getHour()\n'
    '\tif 6 <= hour < 14:\n'
    '\t\treturn "Shift A"\n'
    '\telif 14 <= hour < 22:\n'
    '\t\treturn "Shift B"\n'
    '\telse:\n'
    '\t\treturn "Shift C"'
)

codes_to_check = {
    kpi_code: 'kpi',
    energy_code: 'energy',
    shift_code: 'shift',
}

def get_code_type(code):
    if 'Energy:' in code or 'energy' in code.lower():
        return 'energy'
    if 'Shift' in code or 'LocalTime' in code or 'shift' in code:
        return 'shift'
    if 'round(value' in code:
        return 'kpi'
    return 'unknown'

def fix_script_transforms(node):
    fixed = 0
    if isinstance(node, dict):
        if 'transforms' in node:
            for i, t in enumerate(node['transforms']):
                if t.get('type') == 'script':
                    old_code = t.get('code', '')
                    ctype = get_code_type(old_code)
                    new_code = None
                    if ctype == 'kpi':
                        new_code = kpi_code
                    elif ctype == 'energy':
                        new_code = energy_code
                    elif ctype == 'shift':
                        new_code = shift_code
                    if new_code and old_code != new_code:
                        node['transforms'][i]['code'] = new_code
                        fixed += 1
        for k, v in node.items():
            fixed += fix_script_transforms(v)
    elif isinstance(node, list):
        for item in node:
            fixed += fix_script_transforms(item)
    return fixed

count = fix_script_transforms(data)
print(f'Fixed {count} script transforms')

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify
import re
with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    content = f.read()

# Check all codes have def transform + proper indent
matches = re.findall(r'"code":\s*"([^"]*)"', content)
print(f'\nTotal code values: {len(matches)}')
for i, m in enumerate(matches):
    # Unescape JSON string for display
    code = m.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"')
    print(f'\n--- Code {i+1} (first 80 chars) ---')
    print(repr(code[:100]))
    has_def = 'def transform' in code
    has_tab_body = code.count('\\t') > 0
    print(f'  Has def transform: {has_def}')
