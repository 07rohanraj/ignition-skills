import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
data = json.load(open(path))

issues = []

def check(node, path=''):
    if not isinstance(node, dict):
        return
    # Check propConfig bindings
    for pk, pv in node.get('propConfig', {}).items():
        b = pv.get('binding', {})
        if b.get('type') == 'tag':
            tp = b.get('config', {}).get('tagPath', '')
            if '+' in tp or 'if(' in tp or 'str(' in tp or 'format(' in tp:
                issues.append(f'{path}.{pk}: tag binding with expression: {tp[:80]}')
        if b.get('type') == 'expression':
            expr = b.get('config', {}).get('expression', '')
            if 'str(' in expr or 'format(' in expr:
                issues.append(f'{path}.{pk}: expression with bad function: {expr[:80]}')
    # Check component type
    typ = node.get('type', '')
    if 'alarm' in typ.lower() and typ != 'ia.display.alarmstatustable':
        issues.append(f'{path}: bad alarm type: {typ}')
    for i, c in enumerate(node.get('children', [])):
        check(c, f'{path}/child[{i}]')

check(data['root'], 'root')

if issues:
    for i in issues:
        print(f'ISSUE: {i}')
else:
    print('All clear - no issues found')
