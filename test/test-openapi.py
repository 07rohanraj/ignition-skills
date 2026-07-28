import requests

host = "http://localhost:8088"
token = "LB73hoLmQ8RgYkHuV0zcbBDpvSDygcqpjuActkcZEVY"
headers = {"X-Ignition-API-Token": token}

# Try /data/api/v1/openapi with longer timeout
try:
    r = requests.get(f"{host}/openapi.json", headers=headers, timeout=30)
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        import json
        spec = r.json()
        paths = spec.get("paths", {})
        tag_paths = [p for p in paths if "tag" in p.lower()]
        print(f"Total paths: {len(paths)}")
        print(f"Tag paths: {tag_paths}")
        for p in sorted(tag_paths):
            methods = list(paths[p].keys())
            print(f"  {', '.join(methods).upper():8s} {p}")
    else:
        print(f"Body: {r.text[:500]}")
except requests.exceptions.Timeout:
    print("Request timed out after 30s")
except Exception as e:
    print(f"Error: {e}")
