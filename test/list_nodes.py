import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
data = json.load(open(path))

def find_all(node, path=''):
    if not isinstance(node, dict):
        return
    name = node.get('meta', {}).get('name', '')
    typ = node.get('type', '')
    pos = node.get('position', {})
    sty = node.get('props', {}).get('style', {})
    label = f'{path}: type={typ}'
    if name:
        label += f' name={name}'
    if pos:
        label += f' pos={json.dumps(pos)}'
    if sty:
        label += f' style={json.dumps(sty)}'
    print(label)
    for i, c in enumerate(node.get('children', [])):
        find_all(c, f'{path}/child[{i}]')

find_all(data['root'], 'root')
