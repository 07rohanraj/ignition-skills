import requests

host = "http://localhost:8088"
url = f"{host}/system/gateway/importTags"

# Try with XML type
params = {
    "provider": "default",
    "type": "xml",
    "collisionPolicy": "Overwrite",
    "path": "EVManufacturing"
}

xml_data = b"""<?xml version="1.0" encoding="UTF-8"?>
<tags>
  <tag name="TestTag" type="AtomicTag" valueSource="memory" dataType="Int4" value="42"/>
</tags>"""

headers = {"Content-Type": "application/xml"}
r = requests.post(url, params=params, headers=headers, data=xml_data, timeout=30)
print(f"XML Status: {r.status_code}")
print(f"XML Body: {r.text[:500]}")

# Also try without type param
params2 = {
    "provider": "default",
    "collisionPolicy": "Overwrite",
    "path": "EVManufacturing"
}
headers2 = {"Content-Type": "application/octet-stream"}
with open(r"C:\Users\rohan.raj.AXCEND\AppData\Local\Temp\opencode\simple-tag.json", "rb") as f:
    r2 = requests.post(url, params=params2, headers=headers2, data=f, timeout=30)
print(f"\nNo type param Status: {r2.status_code}")
print(f"Body: {r2.text[:500]}")
