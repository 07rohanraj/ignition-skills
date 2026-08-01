import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

energy_code = (
    'if value is not None:\n'
    '\treturn "Energy: " + str(round(value, 1)) + " kWh"\n'
    'return "Energy: 0.0 kWh"'
)

def fix_energy(node, path=''):
    if isinstance(node, dict):
        if 'transforms' in node:
            for i, t in enumerate(node['transforms']):
                if t.get('type') == 'script' and 'config' in t and 'script' in t['config']:
                    # Replace config.script with code
                    node['transforms'][i] = {
                        "code": energy_code,
                        "type": "script"
                    }
                    name = '?'
                    print(f'Fixed energy transform')
        for k, v in node.items():
            fix_energy(v, f'{path}.{k}')
    elif isinstance(node, list):
        for i, item in enumerate(node):
            fix_energy(item, f'{path}[{i}]')

fix_energy(data)

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify no more config.script
import re
with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    content = f.read()

wrong = content.count('"config"') and content.count('"script"')
print(f'Remaining wrong format transforms: 0' if not (('"config"' in content and '"script"' in content and content.find('"config"') > 0) and abs(content.find('"config"') - content.find('"script"')) < 50) else 'Need to check more carefully')

# Better check - grep for config + script in close proximity
import re
matches = re.findall(r'"config"\s*:\s*\{[^}]*"script"', content)
print(f'Remaining config.script patterns: {len(matches)}')
if matches:
    for m in matches:
        print(f'  {m[:80]}')
