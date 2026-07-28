import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
data = json.load(open(path))

issues = []

def check(node, path=''):
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
        
        if btype == 'tag':
            mode = cfg.get('mode', '')
            tag_path = cfg.get('tagPath', '')
            if mode == 'expression' and ('+' in tag_path or 'if(' in tag_path):
                issues.append(f'{path}.{pk}: tag+expression still present')
        elif btype == 'expression':
            expr = cfg.get('expression', '')
            if isinstance(expr, str) and ('+' in expr or 'if(' in expr):
                # Check it's a proper expression binding
                pass  # These are fine now
    
    for i, child in enumerate(node.get('children', [])):
        check(child, f'{path}/child[{i}]')

check(data['root'], 'root')

if issues:
    for i in issues:
        print(f'ISSUE: {i}')
else:
    print('All clear - no tag+expression bindings remaining')
