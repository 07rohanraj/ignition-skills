import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'r') as f:
    data = json.load(f)

def print_bindings(node, path=""):
    if isinstance(node, dict):
        meta = node.get('meta', {}).get('name', '')
        if 'propConfig' in node:
            pc = node['propConfig']
            for pk in ('props.value', 'props.text'):
                if pk in pc and 'binding' in pc[pk]:
                    b = pc[pk]['binding']
                    bt = b.get('type', '')
                    if bt == 'query':
                        qp = b.get('config', {}).get('queryPath', '')
                        rf = b.get('config', {}).get('returnFormat', '')
                        params = b.get('config', {}).get('parameters', {})
                        ntrans = len(b.get('transforms', []))
                        print(f'{meta:30s} queryPath={qp:25s} returnFormat={rf:8s} params={params} transforms={ntrans}')
                    elif bt == 'script':
                        print(f'{meta:30s} script binding')
                    else:
                        print(f'{meta:30s} type={bt}')
        for k, v in node.items():
            print_bindings(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            print_bindings(item, f"{path}[{i}]")

print_bindings(data)

# Also check no remaining GetLatestKpis
content = json.dumps(data)
if 'GetLatestKpis' in content:
    print('\nWARNING: GetLatestKpis still referenced!')
else:
    print('\nNo GetLatestKpis references - all migrated to GetKpiValue')
