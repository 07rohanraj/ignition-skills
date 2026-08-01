import json, glob, os, re

base = 'C:/Program Files/Inductive Automation/Ignition/data/projects/Ashirvad/com.inductiveautomation.perspective/views'
for fpath in glob.glob(base + '/**/view.json', recursive=True):
    with open(fpath) as fh:
        content = fh.read()
    codes = re.findall(r'"code":\s*"([^"]*)"', content)
    for c in codes:
        if 'def transform' in c:
            rel = os.path.relpath(fpath, base)
            print(rel + ': ' + repr(c[:80]))
print('Done')
