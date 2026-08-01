import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

def audit(node, path=''):
    issues = []
    if isinstance(node, dict):
        if 'propConfig' in node:
            pc = node['propConfig']
            for pk in ('props.value', 'props.text'):
                if pk in pc and 'binding' in pc[pk]:
                    b = pc[pk]['binding']
                    name = node.get('meta', {}).get('name', '?')
                    bt = b.get('type', '?')
                    
                    # Validate structure
                    if bt == 'query':
                        qp = b.get('config', {}).get('queryPath', '')
                        rf = b.get('config', {}).get('returnFormat', '')
                        params = b.get('config', {}).get('parameters', {})
                        ntrans = len(b.get('transforms', []))
                        print(f'  QRY {name:25s} path={qp:30s} returnFormat={rf:8s} params={str(params):30s} transforms={ntrans}')
                        
                    elif bt == 'expr':
                        expr = b.get('config', {}).get('expression', '')
                        ntrans = len(b.get('transforms', []))
                        print(f'  EXP {name:25s} expr={expr:40s} transforms={ntrans}')
                    
                    # Check for wrong script format  
                    if 'transforms' in b:
                        for i, t in enumerate(b['transforms']):
                            if t.get('type') == 'script':
                                if 'config' in t:
                                    issues.append(f'{name}: script transform uses config wrapper (should use code directly)')
                                if 'code' not in t:
                                    issues.append(f'{name}: script transform missing code property')
                                    
        for k, v in node.items():
            issues.extend(audit(v, f'{path}.{k}'))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            issues.extend(audit(item, f'{path}[{i}]'))
    return issues

print("Dashboard binding audit:")
print("="*120)
issues = audit(data)
print("="*120)
if issues:
    print(f"\nISSUES FOUND ({len(issues)}):")
    for i in issues:
        print(f"  - {i}")
else:
    print("\nNo issues found - all bindings valid!")
