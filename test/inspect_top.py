import json, sys

path = sys.argv[1]
d = json.load(open(path, encoding='utf-8'))
print('top keys:', list(d.keys()) if isinstance(d, dict) else type(d))

def walk(o, depth=0, maxdepth=3):
    if depth > maxdepth:
        return
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('tags',) and isinstance(v, list) and v:
                item = v[0]
                print('  ' * depth, 'first child keys:', sorted(item.keys())[:15])
                walk(item, depth + 1, maxdepth)
                break
    elif isinstance(o, list) and o:
        walk(o[0], depth, maxdepth)

walk(d)
