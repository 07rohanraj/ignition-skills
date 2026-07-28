import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
with open(path, 'r') as f:
    data = json.load(f)

# Check GaugeRow children (the 3 gauge cards)
content = data['root']['children'][1]
gauge_row = content['children'][0]
print(f'GaugeRow: {len(gauge_row["children"])} cards')

for i, card in enumerate(gauge_row['children']):
    name = card.get('meta', {}).get('name', '?')
    t = card.get('type', 'none')
    props = card.get('props', {})
    children = card.get('children', [])
    print(f'  Card {i}: name={name}, type={t}, has_direction={("direction" in props)}, children={len(children)}')
    if 'direction' in props:
        print(f'    props.direction={props["direction"]}')
    else:
        # Check if direction is outside props
        if 'direction' in card:
            print(f'    WARNING: direction is OUTSIDE props: card.direction={card["direction"]}')
