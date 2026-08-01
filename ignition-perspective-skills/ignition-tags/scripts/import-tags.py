#!/usr/bin/env python3
"""
Import tags to Ignition Gateway via REST API.

This is a self-contained script that requires only the 'requests' library.
No other local modules are needed.

Usage:
    python import-tags.py --file tags.json
    python import-tags.py --file tags.json --provider default --path "Motors" --collision Overwrite

Configuration (priority: CLI args > env vars > config.json):
    config.json  - Config file (place in scripts/ or project root)
    IGNI_HOST    - Gateway URL (e.g., http://localhost:8088)
    IGNI_TOKEN   - API token from Gateway > Platform > Security > API Keys

Requirements:
    pip install requests
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Installing...", file=sys.stderr)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests


def load_config_file():
    """Load config from config.json file."""
    script_dir = Path(__file__).parent
    search_paths = [
        script_dir / "config.json",
        script_dir.parent / "config.json",
        Path.cwd() / "config.json"
    ]
    
    for config_path in search_paths:
        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                print(f"Loaded config from: {config_path}")
                return config
            except json.JSONDecodeError as e:
                print(f"Warning: Invalid config file {config_path}: {e}", file=sys.stderr)
            except Exception as e:
                print(f"Warning: Could not read {config_path}: {e}", file=sys.stderr)
    
    return {}


def get_config():
    """Get configuration from config file, environment variables, or defaults."""
    file_config = load_config_file()
    
    host = os.environ.get("IGNI_HOST") or file_config.get("host")
    token = os.environ.get("IGNI_TOKEN") or file_config.get("token")
    
    if not host:
        print("Error: Gateway host not configured", file=sys.stderr)
        print("Options:", file=sys.stderr)
        print("  1. Set IGNI_HOST environment variable", file=sys.stderr)
        print("  2. Add 'host' to config.json", file=sys.stderr)
        print("Example: export IGNI_HOST=http://localhost:8088", file=sys.stderr)
        sys.exit(1)
    
    if not token:
        print("Error: API token not configured", file=sys.stderr)
        print("Options:", file=sys.stderr)
        print("  1. Set IGNI_TOKEN environment variable", file=sys.stderr)
        print("  2. Add 'token' to config.json", file=sys.stderr)
        print("Get token from: Gateway > Platform > Security > API Keys", file=sys.stderr)
        sys.exit(1)
    
    return host.rstrip("/"), token


def validate_json(file_path):
    """Validate JSON file before import."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if "tags" not in data:
            if "name" not in data:
                print("Warning: JSON does not contain 'tags' array or 'name' field", file=sys.stderr)
            data = {"tags": [data]}
        
        tag_count = len(data.get("tags", []))
        print(f"JSON validation passed: {tag_count} tag(s) found")
        return True, data
    except json.JSONDecodeError as e:
        print(f"JSON validation failed: {e}", file=sys.stderr)
        return False, None
    except FileNotFoundError:
        print(f"File not found: {file_path}", file=sys.stderr)
        return False, None


def import_tags(host, token, file_path, provider="default", path="", collision_policy="Overwrite", dry_run=False):
    """Import tags to Ignition Gateway."""
    is_valid, data = validate_json(file_path)
    if not is_valid:
        return None
    
    if dry_run:
        print("Dry run - would import:")
        output = json.dumps(data, indent=2)
        if len(output) > 500:
            output = output[:500] + "..."
        print(output)
        return {"status": "dry_run"}
    
    url = f"{host}/data/api/v1/tags/import"
    params = {
        "provider": provider,
        "type": "json",
        "collisionPolicy": collision_policy
    }
    
    if path:
        params["path"] = path
    
    headers = {
        "X-Ignition-API-Token": token,
        "Content-Type": "application/octet-stream"
    }
    
    try:
        with open(file_path, "rb") as f:
            response = requests.post(url, params=params, headers=headers, data=f, timeout=30)
        
        if response.status_code == 200:
            result = response.json() if response.content else {"status": "ok"}
            print("Import successful!")
            if result:
                print(f"Result: {json.dumps(result, indent=2)}")
            return result
        else:
            print(f"Import failed with status {response.status_code}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
            return None
    
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to {host}", file=sys.stderr)
        print("Check that the Gateway is running and IGNI_HOST is correct", file=sys.stderr)
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Import tags to Ignition Gateway via REST API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --file motor-tags.json
  %(prog)s --file tags.json --provider myprovider --path "Area1/Motors"
  %(prog)s --file tags.json --collision MergeOverwrite
  %(prog)s --file tags.json --dry-run

Collision Policies:
  Abort          - Stop if any tag exists
  Overwrite      - Replace existing tags
  Rename         - Rename to avoid conflicts
  Ignore         - Skip existing tags
  MergeOverwrite - Merge properties, overwriting values
        """
    )
    
    parser.add_argument("--file", "-f", required=True,
                        help="Path to tag JSON file")
    parser.add_argument("--provider", "-p", default="default",
                        help="Tag provider name (default: 'default')")
    parser.add_argument("--path", default="",
                        help="Root path for import (default: root)")
    parser.add_argument("--collision", "-c", default="Overwrite",
                        choices=["Abort", "Overwrite", "Rename", "Ignore", "MergeOverwrite"],
                        help="Collision policy (default: Overwrite)")
    parser.add_argument("--dry-run", "-n", action="store_true",
                        help="Validate JSON without importing")
    parser.add_argument("--validate-only", "-v", action="store_true",
                        help="Only validate JSON file, don't import")
    
    args = parser.parse_args()
    
    if args.validate_only:
        is_valid, data = validate_json(args.file)
        sys.exit(0 if is_valid else 1)
    
    if args.dry_run:
        result = import_tags(
            host="",
            token="",
            file_path=args.file,
            provider=args.provider,
            path=args.path,
            collision_policy=args.collision,
            dry_run=True
        )
    else:
        host, token = get_config()
        result = import_tags(
            host=host,
            token=token,
            file_path=args.file,
            provider=args.provider,
            path=args.path,
            collision_policy=args.collision,
            dry_run=False
        )
    
    sys.exit(0 if result is not None else 1)


if __name__ == "__main__":
    main()
