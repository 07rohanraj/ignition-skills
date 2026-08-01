import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

def check_all(node, path=''):
    if isinstance(node, dict):
        if 'transforms' in node:
            for i, t in enumerate(node['transforms']):
                if t.get('type') == 'script':
                    # Check format
                    has_config_script = 'config' in t and 'script' in t['config']
                    has_code = 'code' in t
                    name = '?'
                    # Walk up to find meta name
                    print(f'Transform #{i}: has_config.script={has_config_script}, has_code={has_code}')
                    print(f'  Keys: {list(t.keys())}')
                    if has_config_script:
                        print(f'  Wrong format: config.script instead of code')
                    print()
        for k, v in node.items():
            check_all(v, f'{path}.{k}')
    elif isinstance(node, list):
        for i, item in enumerate(node):
            check_all(item, f'{path}[{i}]')

check_all(data)
