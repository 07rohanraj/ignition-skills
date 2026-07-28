import requests
import json

host = "http://localhost:8088"
token = "LB73hoLmQ8RgYkHuV0zcbBDpvSDygcqpjuActkcZEVY"
headers = {"X-Ignition-API-Token": token}

# Try resource-based endpoints for tags
tests = [
    ("GET", "/data/api/v1/resources/list/core/ignition/tag-definition"),
    ("GET", "/data/api/v1/resources/list"),
    ("GET", "/data/api/v1/resources"),
]

for method, path in tests:
    url = f"{host}{path}"
    try:
        if method == "GET":
            r = requests.get(url, headers=headers, timeout=10)
        print(f"{r.status_code} {method} {path}")
        if r.status_code == 200:
            print(f"  Body: {r.text[:300]}")
        else:
            print(f"  Body: {r.text[:200]}")
    except Exception as e:
        print(f"ERR {method} {path}: {e}")
