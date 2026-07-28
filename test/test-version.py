import requests

host = "http://localhost:8088"

# Try the /system/gateway-info endpoint
r = requests.get(f"{host}/system/gateway-info", timeout=10)
print(f"gateway-info: {r.status_code}")
if r.status_code == 200:
    print(r.text[:500])

# Try /main/system/gateway-status
r2 = requests.get(f"{host}/main/system/gateway-status", timeout=10)
print(f"\ngateway-status: {r2.status_code}")

# Check if there's a /data/api endpoint specifically
r3 = requests.get(f"{host}/data/api/v1", timeout=10, headers={"X-Ignition-API-Token": "LB73hoLmQ8RgYkHuV0zcbBDpvSDygcqpjuActkcZEVY"})
print(f"\n/data/api/v1: {r3.status_code}")
print(r3.text[:300])
