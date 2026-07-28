import requests

host = "http://localhost:8088"
token = "LB73hoLmQ8RgYkHuV0zcbBDpvSDygcqpjuActkcZEVY"

# Check the modules list endpoint
r = requests.get(f"{host}/data/api/v1/modules", headers={"X-Ignition-API-Token": token}, timeout=10)
print(f"Modules: {r.status_code}")
if r.status_code == 200:
    print(r.text[:2000])
else:
    print(r.text[:300])

# Check system properties
r2 = requests.get(f"{host}/data/api/v1/system/properties", headers={"X-Ignition-API-Token": token}, timeout=10)
print(f"\nSystem props: {r2.status_code}")
if r2.status_code == 200:
    print(r2.text[:1000])
else:
    print(r2.text[:300])

# Check tag providers
r3 = requests.get(f"{host}/data/api/v1/tags/providers", headers={"X-Ignition-API-Token": token}, timeout=10)
print(f"\nTag providers: {r3.status_code}")
print(r3.text[:300])
