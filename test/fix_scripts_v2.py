import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

# code = just the body (def transform ... already provided by engine)
# one tab indent for body, two tabs for nested if-body
kpi_code = (
    '\tif value is not None:\n'
    '\t\treturn str(round(value, 1))\n'
    '\treturn "0.0"'
)

energy_code = (
    '\tif value is not None:\n'
    '\t\treturn "Energy: " + str(round(value, 1)) + " kWh"\n'
    '\treturn "Energy: 0.0 kWh"'
)

shift_code = (
    '\tfrom java.time import LocalTime\n'
    '\thour = LocalTime.now().getHour()\n'
    '\tif 6 <= hour < 14:\n'
    '\t\treturn "Shift A"\n'
    '\telif 14 <= hour < 22:\n'
    '\t\treturn "Shift B"\n'
    '\telse:\n'
    '\t\treturn "Shift C"'
)

def code_type(code):
    if 'Energy:' in code or 'energy' in code:
        return 'energy'
    if 'Shift' in code or 'LocalTime' in code:
        return 'shift'
    if 'round(value' in code or '0.0' in code:
        return 'kpi'
    return 'unknown'

def fix(node):
    fixed = 0
    if isinstance(node, dict):
        if 'transforms' in node:
            for i, t in enumerate(node['transforms']):
                if t.get('type') == 'script':
                    old = t.get('code', '')
                    ct = code_type(old)
                    new = None
                    if ct == 'kpi':
                        new = kpi_code
                    elif ct == 'energy':
                        new = energy_code
                    elif ct == 'shift':
                        new = shift_code
                    if new and old != new:
                        node['transforms'][i]['code'] = new
                        fixed += 1
        for v in node.values():
            fixed += fix(v)
    elif isinstance(node, list):
        for item in node:
            fixed += fix(item)
    return fixed

n = fix(data)
print(f'Fixed {n} script transforms')

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify no 'def transform' in any code value
import re
with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    content = f.read()

codes = re.findall(r'"code":\s*"([^"]*)"', content)
bad = [c for c in codes if 'def transform' in c]
print(f'Codes with "def transform": {len(bad)}')
print(f'Total codes: {len(codes)}')
print(f'All start with \\t: {all(c.startswith("\\\\t") or c.startswith("\\t") for c in codes)}')
