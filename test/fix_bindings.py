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
        if not isinstance(binding, dict):
            continue
        btype = binding.get('type', '')
        cfg = binding.get('config', {})
        if not isinstance(cfg, dict):
            continue
        
        # Fix tag bindings with expression mode that contain display logic
        if btype == 'tag':
            mode = cfg.get('mode', '')
            tag_path = cfg.get('tagPath', '')
            if mode == 'expression' and ('+' in tag_path or 'if(' in tag_path):
                # This is a tag binding in expression mode, but the expression
                # computes display text, not a tag path. Convert to expression binding.
                binding['type'] = 'expression'
                binding['config'] = {'expression': tag_path}
                # Remove old config keys
                cfg.pop('mode', None)
                cfg.pop('tagPath', None)
                cfg.pop('fallbackDelay', None)
                fixed += 1
                print(f'  Fixed: {pk} (was tag+expression, now expression)')
    
    for child in node.get('children', []):
        fix(child)

print('Fixing Safety view bindings...')
fix(data['root'])
print(f'\nTotal fixed: {fixed}')

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
print('File saved.')
