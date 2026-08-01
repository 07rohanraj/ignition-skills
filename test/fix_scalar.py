import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'r') as f:
    data = json.load(f)

def make_query_binding(machine_id, column, with_format=True, with_energy_prefix=False):
    """Create a query binding config for GetKpiValue with scalar return."""
    params = {
        "machineId": str(machine_id),
        "columnName": "'" + column + "'"
    }
    binding = {
        "config": {
            "queryPath": "KpiData/GetKpiValue",
            "parameters": params,
            "returnFormat": "scalar",
            "polling": {
                "enabled": True,
                "rate": 10
            }
        },
        "type": "query"
    }
    
    transforms = []
    
    if with_energy_prefix:
        transforms.append({
            "config": {
                "script": "def transform(self, value, quality, timestamp):\n\tif value is not None:\n\t\treturn \"Energy: \" + str(round(value, 1)) + \" kWh\"\n\treturn \"Energy: 0.0 kWh\""
            },
            "type": "script"
        })
    
    if with_format and not with_energy_prefix:
        transforms.append({
            "formatType": "numeric",
            "formatValue": "0.0",
            "type": "format"
        })
    
    if transforms:
        binding["transforms"] = transforms
    
    return binding

def update_component_binding(comp, binding):
    """Set the binding on the component's propConfig.props.text or props.value."""
    if 'propConfig' not in comp:
        comp['propConfig'] = {}
    
    # Determine which property to bind based on component type or existing config
    pc = comp['propConfig']
    if 'props.value' in pc:
        pc['props.value']['binding'] = binding
    elif 'props.text' in pc:
        pc['props.text']['binding'] = binding
    else:
        # Add based on component type
        if 'gauge' in comp.get('meta', {}).get('name', ''):
            pc['props.value'] = {'binding': binding}
        else:
            pc['props.text'] = {'binding': binding}

def walk_update(node):
    if isinstance(node, dict):
        meta = node.get('meta', {}).get('name', '')
        
        if 'propConfig' in node:
            pc = node['propConfig']
            binding_key = None
            
            # Determine which property has a binding
            for pk in ('props.value', 'props.text'):
                if pk in pc and 'binding' in pc.get(pk, {}):
                    binding_key = pk
                    break
            
            if binding_key and pc[binding_key]['binding'].get('type') == 'query':
                old_binding = pc[binding_key]['binding']
                qp = old_binding.get('config', {}).get('queryPath', '')
                params = old_binding.get('config', {}).get('parameters', {})
                mid = params.get('machineId', '1')
                
                if qp == 'KpiData/GetLatestKpis':
                    # Determine which column based on meta name
                    column_map = {
                        'gaugeExtrusionOEE': 'oee_pct',
                        'gaugeInjectionOEE': 'oee_pct',
                        'lblExtrusionOEE': 'oee_pct',
                        'lblInjectionOEE': 'oee_pct',
                        'lblExtrAvailValue': 'availability_pct',
                        'lblInjAvailValue': 'availability_pct',
                        'lblExtrQualityValue': 'quality_pct',
                        'lblInjQualityValue': 'quality_pct',
                        'lblExtrPerfValue': 'performance_pct',
                        'lblInjPerfValue': 'performance_pct',
                        'lblExtrYieldValue': 'yield_pct',
                        'lblInjYieldValue': 'yield_pct',
                        'lblExtrusionEnergy': 'energy_kwh',
                        'lblInjectionEnergy': 'energy_kwh',
                    }
                    
                    col = column_map.get(meta)
                    if col:
                        is_energy = col == 'energy_kwh'
                        is_gauge = 'gauge' in meta
                        
                        pc[binding_key]['binding'] = make_query_binding(
                            machine_id=mid,
                            column=col,
                            with_format=not is_gauge,
                            with_energy_prefix=is_energy
                        )
        
        for k, v in node.items():
            walk_update(v)
    elif isinstance(node, list):
        for item in node:
            walk_update(item)

walk_update(data)

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify
count = 0
for line in open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json'):
    if 'GetKpiValue' in line:
        count += 1
print(f'Updated {count} bindings to use GetKpiValue')
