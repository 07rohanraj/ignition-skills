import json, re, sys

path = sys.argv[1]
data = open(path, encoding='utf-8').read()
print('priority values:', sorted(set(re.findall(r'"priority": "([^"]+)"', data))))
print('mode values:', sorted(set(re.findall(r'"mode": "([^"]+)"', data))))
print('ackMode values:', sorted(set(re.findall(r'"ackMode": "([^"]+)"', data))))
print('has alarms array:', '"alarms"' in data)

d = json.loads(data)
def walk(o):
    if isinstance(o, dict):
        if o.get('alarms'):
            yield o
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)

for t in walk(d):
    print(json.dumps({k: t.get(k) for k in ('name', 'tagType', 'dataType', 'alarms')}, indent=1)[:2000])
