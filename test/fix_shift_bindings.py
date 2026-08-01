import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

shift_script = (
    'from java.time import LocalTime\n'
    'hour = LocalTime.now().getHour()\n'
    'if 6 <= hour < 14:\n'
    '\treturn "Shift A"\n'
    'elif 14 <= hour < 22:\n'
    '\treturn "Shift B"\n'
    'else:\n'
    '\treturn "Shift C"'
)

def fix_shift_bindings(node):
    if isinstance(node, dict):
        if 'propConfig' in node:
            pc = node['propConfig']
            for pk in ('props.value', 'props.text'):
                if pk in pc and 'binding' in pc[pk]:
                    b = pc[pk]['binding']
                    if b.get('type') == 'script':
                        # Replace standalone script binding with expression binding + script transform
                        pc[pk]['binding'] = {
                            "config": {
                                "expression": "now(60000)"
                            },
                            "transforms": [
                                {
                                    "code": shift_script,
                                    "type": "script"
                                }
                            ],
                            "type": "expr"
                        }
                        name = node.get("meta", {}).get("name", "?")
                        print(f"Fixed: {name}")
        for k, v in node.items():
            fix_shift_bindings(v)
    elif isinstance(node, list):
        for item in node:
            fix_shift_bindings(item)

fix_shift_bindings(data)

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify
import re
with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    content = f.read()

script_count = len(re.findall(r'"type":\s*"script"', content))
standalone_script = len(re.findall(r'"binding"\s*:\s*\{[^}]*"type":\s*"script"', content))
print(f'"type": "script" occurrences: {script_count}')
print(f'Standalone script bindings: {standalone_script}')
