import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

def show_codes(node):
    if isinstance(node, dict):
        if 'transforms' in node:
            for i, t in enumerate(node['transforms']):
                if t.get('type') == 'script':
                    code = t.get('code', '')
                    if 'def transform' in code or not code.startswith('\t'):
                        name = '?'
                        print(f'ISSUE: code contains "def transform" or starts without tab')
                        print(repr(code))
                        print('---')
        for v in node.values():
            show_codes(v)
    elif isinstance(node, list):
        for item in node:
            show_codes(item)

show_codes(data)
print("Done scanning")
