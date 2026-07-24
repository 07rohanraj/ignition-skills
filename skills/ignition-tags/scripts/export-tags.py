#!/usr/bin/env python3
"""
Export tags from Ignition Gateway via REST API.

Usage:
    python export-tags.py --output tags.json
    python export-tags.py --provider default --path "Motors" --output motors.json

Configuration (priority: CLI args > env vars > config.json):
    config.json  - Config file (place in scripts/ or project root)
    IGNI_HOST    - Gateway URL (e.g., http://localhost:8088)
    IGNI_TOKEN   - API token from Gateway > Platform > Security > API Keys
"""

import os
import sys
import json
import argparse
import requests
from pathlib import Path


def load_config_file():
    """Load config from config.json file."""
    # Look for config.json in script directory, then parent, then current working directory
    script_dir = Path(__file__).parent.parent
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
    # Load config file
    file_config = load_config_file()
    
    # Priority: environment variables > config file
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


def export_tags(host, token, provider="default", path="", output="exported-tags.json",
                export_type="json", recursive=True, include_udts=True):
    """
    Export tags from Ignition Gateway.
    
    Args:
        host: Gateway URL
        token: API token
        provider: Tag provider name
        path: Root path to export
        output: Output file path
        export_type: "json" or "xml"
        recursive: Export sub-folders
        include_udts: Include UDT definitions
    
    Returns:
        True on success, False on error
    """
    url = f"{host}/data/api/v1/tags/export"
    params = {
        "provider": provider,
        "type": export_type,
        "recursive": str(recursive).lower(),
        "includeUdts": str(include_udts).lower()
    }
    
    if path:
        params["path"] = path
    
    headers = {
        "X-Ignition-API-Token": token
    }
    
    try:
        print(f"Exporting tags from provider '{provider}'...")
        if path:
            print(f"Path: {path}")
        
        response = requests.get(url, params=params, headers=headers, timeout=60)
        
        if response.status_code == 200:
            # Save to file
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, "wb") as f:
                f.write(response.content)
            
            print(f"Export successful!")
            print(f"Saved to: {output_path.absolute()}")
            
            # Show summary if JSON
            if export_type == "json":
                try:
                    data = json.loads(response.content)
                    if "tags" in data:
                        print(f"Exported {len(data['tags'])} tag(s)")
                except:
                    pass
            
            return True
        else:
            print(f"Export failed with status {response.status_code}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
            return False
    
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to {host}", file=sys.stderr)
        print("Check that the Gateway is running and IGNI_HOST is correct", file=sys.stderr)
        return False
    except requests.exceptions.Timeout:
        print("Error: Request timed out", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Export tags from Ignition Gateway via REST API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --output all-tags.json
  %(prog)s --provider default --path "Motors" --output motors.json
  %(prog)s --path "Area1" --output area1.json --no-recursive
  %(prog)s --output tags.xml --type xml
        """
    )
    
    parser.add_argument("--output", "-o", default="exported-tags.json",
                        help="Output file path (default: exported-tags.json)")
    parser.add_argument("--provider", "-p", default="default",
                        help="Tag provider name (default: 'default')")
    parser.add_argument("--path", default="",
                        help="Root path to export (default: root)")
    parser.add_argument("--type", "-t", choices=["json", "xml"], default="json",
                        help="Export format (default: json)")
    parser.add_argument("--no-recursive", action="store_true",
                        help="Don't export sub-folders")
    parser.add_argument("--no-udts", action="store_true",
                        help="Don't include UDT definitions")
    
    args = parser.parse_args()
    
    # Get config
    host, token = get_config()
    
    # Export
    success = export_tags(
        host=host,
        token=token,
        provider=args.provider,
        path=args.path,
        output=args.output,
        export_type=args.type,
        recursive=not args.no_recursive,
        include_udts=not args.no_udts
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
