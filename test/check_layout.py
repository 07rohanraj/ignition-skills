import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
data = json.load(open(path))

def find(name, node, path=''):
    if not isinstance(node, dict):
        return
    if node.get('meta', {}).get('name') == name:
        pos = json.dumps(node.get('position', {}))
        sty = json.dumps(node.get('props', {}).get('style', {}))
        print(f'Found {name} at {path}')
        print(f'  position: {pos}')
        print(f'  style: {sty}')
        return
    for i, c in enumerate(node.get('children', [])):
        find(name, c, f'{path}/[{i}]')

find('GaugeRow', data)
find('StatusRow', data)
find('AlarmSection', data)
find('ContentArea', data)
find('root', data)
