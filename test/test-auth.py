import requests

token = "LB73hoLmQ8RgYkHuV0zcbBDpvSDygcqpjuActkcZEVY"
payload = b'{"tags":[]}'

r = requests.post(
    "http://localhost:8088/data/api/v1/tags/import",
    params={"provider": "default", "type": "json", "collisionPolicy": "Overwrite"},
    headers={"X-Ignition-API-Token": token, "Content-Type": "application/octet-stream"},
    data=payload,
    timeout=10
)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:500]}")

# Also try without the token to see if the error is different
r2 = requests.post(
    "http://localhost:8088/data/api/v1/tags/import",
    params={"provider": "default", "type": "json", "collisionPolicy": "Overwrite"},
    headers={"Content-Type": "application/octet-stream"},
    data=payload,
    timeout=10
)
print(f"\nNo token Status: {r2.status_code}")
print(f"Body: {r2.text[:200]}")
