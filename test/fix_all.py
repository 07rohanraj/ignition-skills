import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
with open(path) as f:
    data = json.load(f)

TAG = "[default]EV Manufacturing"

def fix_bindings(node):
    if not isinstance(node, dict):
        return
    pc = node.get('propConfig', {})
    for prop_key, prop_conf in pc.items():
        binding = prop_conf.get('binding', {})
        cfg = binding.get('config', {})
        if binding.get('type') == 'tag':
            tag_path = cfg.get('tagPath', '')
            # If tagPath has expression logic (+, if(), etc), convert to expression binding
            if '+' in tag_path or 'if(' in tag_path or 'str(' in tag_path:
                binding['type'] = 'expression'
                binding['config'] = {'expression': tag_path}
                # Remove mode key if present
                cfg.pop('mode', None)
    # Fix alarm component type
    if node.get('type') == 'ia.alarm.status':
        node['type'] = 'ia.display.alarmstatustable'
    for child in node.get('children', []):
        fix_bindings(child)

fix_bindings(data)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
print("Fixed bindings and alarm type")
