import json

path = r'C:\Program Files\Inductive Automation\Ignition\data\projects\EVManufacture\com.inductiveautomation.perspective\views\Safety\view.json'
with open(path) as f:
    data = json.load(f)

def fix_spacing(node, path=''):
    if not isinstance(node, dict):
        return
    name = node.get('meta', {}).get('name', '')
    
    # Fix GaugeRow - increase basis to fit cards
    if name == 'GaugeRow':
        node['position']['basis'] = '340px'
        print(f'Fixed {name}: basis 280px -> 340px')
    
    # Fix GaugeCards - reduce basis so they fit in the row
    if name in ('GaugeCard_L1', 'GaugeCard_L2', 'GaugeCard_L3'):
        node['position']['basis'] = '280px'
        node['position']['grow'] = 1
        # Add gap between items inside the card
        node['props']['gap'] = '4px'
        print(f'Fixed {name}: basis 310px -> 280px, added gap')
    
    # Fix SafetyMetricsRow - increase basis
    if name == 'SafetyMetricsRow':
        node['position']['basis'] = '110px'
        print(f'Fixed {name}: basis 80px -> 110px')
    
    # Fix Safety metric cards - reduce basis
    if name in ('IncidentsCard', 'DaysCard', 'NearMissCard', 'TargetCard'):
        node['position']['basis'] = '0px'
        node['position']['grow'] = 1
        # Ensure vertical layout with proper spacing
        node['props']['direction'] = 'column'
        node['props']['justify'] = 'center'
        node['props']['gap'] = '2px'
        print(f'Fixed {name}: removed fixed basis, added gap')
    
    # Fix LineStatusRow - increase basis
    if name == 'LineStatusRow':
        node['position']['basis'] = '170px'
        print(f'Fixed {name}: basis 130px -> 170px')
    
    # Fix LineStatus cards - ensure proper sizing
    if name in ('LineStatus_L1', 'LineStatus_L2', 'LineStatus_L3'):
        node['position']['basis'] = '0px'
        node['position']['grow'] = 1
        node['props']['gap'] = '8px'
        print(f'Fixed {name}: removed fixed basis, added gap')
    
    # Fix Info columns inside LineStatus cards
    if name in ('L1_InfoCol', 'L2_InfoCol', 'L3_InfoCol'):
        node['props']['gap'] = '2px'
        print(f'Fixed {name}: added gap')
    
    # Fix ContentArea - add overflow handling
    if name == 'ContentArea':
        node['props']['style']['overflow'] = 'auto'
        print(f'Fixed {name}: added overflow auto')
    
    # Fix Gauge subtitles - increase basis for readability
    if name in ('FlashRate_L1', 'FlashRate_L2', 'FlashRate_L3', 
                'PaintRate_L1', 'PaintRate_L2', 'PaintRate_L3'):
        node['position']['basis'] = '24px'
        print(f'Fixed {name}: basis 20px -> 24px')
    
    for i, child in enumerate(node.get('children', [])):
        fix_spacing(child, f'{path}/child[{i}]')

fix_spacing(data['root'], 'root')

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
print('\nFile saved.')
