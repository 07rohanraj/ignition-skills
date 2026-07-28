#!/usr/bin/env python3
"""
Fetch OpenAPI spec from Ignition Gateway.

Usage:
    python fetch-openapi.py
    python fetch-openapi.py --host http://localhost:8088 --token YOUR_TOKEN
"""

import json
import sys
import argparse
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

OPENAPI_PATH = Path(__file__).parent / "openapi.json"


def fetch_openapi(host, token, force=False):
    """Fetch and save OpenAPI spec."""
    if OPENAPI_PATH.exists() and not force:
        print(f"OpenAPI spec already exists at: {OPENAPI_PATH}")
        print("Use --force to re-download.")
        return
    
    url = f"{host.rstrip('/')}/openapi.json"
    headers = {"X-Ignition-API-Token": token}
    
    print(f"Fetching from: {url}")
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    
    spec = response.json()
    
    with open(OPENAPI_PATH, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)
    
    paths = spec.get("paths", {})
    print(f"Saved: {OPENAPI_PATH}")
    print(f"Found {len(paths)} API endpoints")


def main():
    parser = argparse.ArgumentParser(description="Fetch OpenAPI spec from Ignition Gateway")
    parser.add_argument("--host", default="http://localhost:8088", help="Gateway URL")
    parser.add_argument("--token", required=True, help="API token")
    parser.add_argument("--force", action="store_true", help="Re-download even if exists")
    
    args = parser.parse_args()
    
    try:
        fetch_openapi(args.host, args.token, args.force)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
