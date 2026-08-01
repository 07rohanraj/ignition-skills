import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

def find_script_bindings(node, path=''):
    if isinstance(node, dict):
        if 'propConfig' in node:
            pc = node['propConfig']
            for pk in ('props.value', 'props.text'):
                if pk in pc and 'binding' in pc[pk]:
                    b = pc[pk]['binding']
                    if b.get('type') == 'script':
                        name = node.get("meta", {}).get("name", "?")
                        print(f'--- {name} (path={path}.{pk}) ---')
                        print(json.dumps(b, indent=2))
                        print()
        for k, v in node.items():
            find_script_bindings(v, f'{path}.{k}')
    elif isinstance(node, list):
        for i, item in enumerate(node):
            find_script_bindings(item, f'{path}[{i}]')

find_script_bindings(data)
