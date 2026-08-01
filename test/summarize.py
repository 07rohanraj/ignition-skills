import json, sys
from collections import Counter

def summarize(path):
    d = json.load(open(path, encoding='utf-8'))
    counts = Counter()
    typecount = Counter()
    alarm_tags = []
    udt_types = []
    details = []

    def walk(o, depth=0, pathstr=""):
        if isinstance(o, dict):
            tagType = o.get('tagType')
            name = o.get('name', '?')
            typecount[tagType] += 1
            counts['nodes'] += 1
            cur = pathstr + '/' + name if pathstr else name
            if tagType == 'UdtInstance':
                udt_types.append((cur, o.get('typeId'), sorted(o.get('parameters', {}).keys())))
            if tagType == 'UdtType':
                udt_types.append((cur, 'DEF', sorted(o.get('parameters', {}).keys())))
            if o.get('alarms'):
                for a in o['alarms']:
                    alarm_tags.append((cur, a.get('name'), a.get('priority'), a.get('mode')))
            for k, v in o.items():
                if isinstance(v, (dict, list)):
                    walk(v, depth + 1, cur)
        elif isinstance(o, list):
            for v in o:
                walk(v, depth, pathstr)

    walk(d)
    print(f"=== {path} ===")
    print("node types:", dict(typecount))
    print("total nodes:", counts['nodes'])
    if alarm_tags:
        print("alarm tags (%d):" % len(alarm_tags))
        for t in alarm_tags:
            print("   ", t)
    else:
        print("alarm tags: NONE")
    if udt_types:
        print("UDT defs/instances (%d):" % len(udt_types))
        for t in udt_types:
            print("   ", t)
    else:
        print("UDT defs/instances: NONE")

summarize(sys.argv[1])
