import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\.agents\skills\ignition-perspective-skills\ignition-tags\examples\EV Manufacturing Tags.json'
with open(path) as f:
    data = json.load(f)

def list_tags(node, prefix=''):
    name = node.get('name', '?')
    full = f'{prefix}/{name}' if prefix else name
    if node.get('tagType') == 'Folder':
        print(f'  [Folder] {full}')
        for child in node.get('tags', []):
            list_tags(child, full)
    else:
        vs = node.get('valueSource', '?')
        print(f'  [{vs}] {full}')

for tag in data['tags']:
    list_tags(tag)
