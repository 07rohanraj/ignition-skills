import json

with open('C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views/Pages/Dashboard/view.json') as f:
    data = json.load(f)

# Paths from earlier search
extrusion = data['root']['children'][1]['children'][0]['children'][0]['children'][1]
injection = data['root']['children'][1]['children'][1]['children'][0]['children'][1]

print("=== EXTRUSION SHIFT BINDING ===")
print(json.dumps(extrusion['propConfig']['props.text']['binding'], indent=2))

print("\n=== INJECTION SHIFT BINDING ===")
print(json.dumps(injection['propConfig']['props.text']['binding'], indent=2))

print("\n=== ARE THEY IDENTICAL? ===")
print(extrusion['propConfig']['props.text']['binding'] == injection['propConfig']['props.text']['binding'])
