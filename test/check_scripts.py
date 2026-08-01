import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

def find_script_transforms(node, path=''):
    if isinstance(node, dict):
        if 'transforms' in node:
            for i, t in enumerate(node['transforms']):
                if t.get('type') == 'script':
                    code = t.get('code', '')
                    name = '?'
                    # Try to find parent meta name
                    print(f'[Transform at {path}] code (repr):')
                    print(repr(code))
                    print()
                    # Show the actual code
                    print('Code as-is:')
                    for line_num, line in enumerate(code.split('\n')):
                        print(f'{line_num}: {repr(line)}')
                    print()
        for k, v in node.items():
            find_script_transforms(v, f'{path}.{k}')
    elif isinstance(node, list):
        for i, item in enumerate(node):
            find_script_transforms(item, f'{path}[{i}]')

# Get meta name context
def name_context(node):
    if isinstance(node, dict):
        if 'meta' in node and 'name' in node['meta']:
            return node['meta']['name']
        for k, v in node.items():
            if isinstance(v, (dict, list)):
                result = name_context(v)
                if result:
                    return result
    elif isinstance(node, list):
        for item in node:
            result = name_context(item)
            if result:
                return result
    return None

find_script_transforms(data)
