import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
with open(path) as f:
    data = json.load(f)

fixed = 0

def fix(node):
    global fixed
    if not isinstance(node, dict):
        return
    pc = node.get('propConfig', {})
    for pk, pv in pc.items():
        binding = pv.get('binding', {})
        cfg = binding.get('config', {})
        if binding.get('type') == 'tag':
            tag_path = cfg.get('tagPath', '')
            if '+' in tag_path or 'if(' in tag_path or 'str(' in tag_path or 'null' in tag_path:
                binding['type'] = 'expression'
                binding['config'] = {'expression': tag_path}
                cfg.pop('mode', None)
                fixed += 1
    if node.get('type') == 'ia.alarm.status':
        node['type'] = 'ia.display.alarmstatustable'
        fixed += 1
    for child in node.get('children', []):
        fix(child)

# Start from root node, not top-level dict
fix(data['root'])

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
print(f'Fixed {fixed} bindings')
