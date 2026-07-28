#!/usr/bin/env python3
"""
Ignition Gateway API Explorer

Search and explore the OpenAPI specification to find the APIs you need.
One file to search all Gateway APIs.

Usage:
    python api-explorer.py --search "tag"
    python api-explorer.py --search "alarm"
    python api-explorer.py --list-tags
    python api-explorer.py --get /system/tag/{provider}/browse
"""

import json
import sys
import argparse
from pathlib import Path

OPENAPI_PATH = Path(__file__).parent / "openapi.json"


def load_openapi():
    """Load the OpenAPI specification."""
    if not OPENAPI_PATH.exists():
        print(f"Error: OpenAPI spec not found at {OPENAPI_PATH}", file=sys.stderr)
        print("Run: python fetch-openapi.py  (to download it first)", file=sys.stderr)
        sys.exit(1)
    
    with open(OPENAPI_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def search_apis(spec, keyword):
    """Search for APIs containing keyword in path or description."""
    results = []
    keyword_lower = keyword.lower()
    
    for path, methods in spec.get("paths", {}).items():
        # Search in path
        if keyword_lower in path.lower():
            results.append((path, methods))
            continue
        
        # Search in operation summaries/descriptions
        for method, details in methods.items():
            if isinstance(details, dict):
                summary = details.get("summary", "").lower()
                description = details.get("description", "").lower()
                if keyword_lower in summary or keyword_lower in description:
                    results.append((path, methods))
                    break
    
    return results


def list_all_apis(spec):
    """List all available API endpoints."""
    results = []
    for path, methods in spec.get("paths", {}).items():
        results.append((path, methods))
    return results


def get_api_details(spec, path):
    """Get detailed info for a specific API path."""
    if path in spec.get("paths", {}):
        return spec["paths"][path]
    return None


def print_api_list(apis, title="APIs"):
    """Print a formatted list of APIs."""
    print(f"\n{title}:")
    print("-" * 60)
    
    for path, methods in sorted(apis):
        method_list = [m.upper() for m in methods.keys() if m in ("get", "post", "put", "delete", "patch")]
        print(f"  {', '.join(method_list):12s} {path}")
    
    print(f"\nTotal: {len(apis)} endpoint(s)")


def print_api_details(path, methods):
    """Print detailed API information."""
    print(f"\nEndpoint: {path}")
    print("=" * 60)
    
    for method, details in methods.items():
        if method not in ("get", "post", "put", "delete", "patch"):
            continue
        
        print(f"\n  Method: {method.upper()}")
        
        if isinstance(details, dict):
            if "summary" in details:
                print(f"  Summary: {details['summary']}")
            if "description" in details:
                print(f"  Description: {details['description'][:200]}")
            if "parameters" in details:
                print(f"  Parameters:")
                for param in details["parameters"]:
                    name = param.get("name", "")
                    location = param.get("in", "")
                    required = param.get("required", False)
                    print(f"    - {name} ({location}) {'[required]' if required else ''}")
            if "requestBody" in details:
                print(f"  Request Body: Yes")
            if "responses" in details:
                print(f"  Responses: {list(details['responses'].keys())}")


def main():
    parser = argparse.ArgumentParser(
        description="Search and explore Ignition Gateway APIs"
    )
    parser.add_argument("--search", "-s", help="Search for APIs by keyword")
    parser.add_argument("--get", "-g", help="Get details for specific API path")
    parser.add_argument("--list-tags", action="store_true", help="List all tag-related APIs")
    parser.add_argument("--list-alarm", action="store_true", help="List all alarm-related APIs")
    parser.add_argument("--list-project", action="store_true", help="List all project-related APIs")
    parser.add_argument("--list-db", action="store_true", help="List all database-related APIs")
    parser.add_argument("--list-all", action="store_true", help="List all APIs")
    parser.add_argument("--count", action="store_true", help="Count total APIs")
    
    args = parser.parse_args()
    spec = load_openapi()
    
    if args.search:
        results = search_apis(spec, args.search)
        print_api_list(results, f"APIs matching '{args.search}'")
    
    elif args.get:
        details = get_api_details(spec, args.get)
        if details:
            print_api_details(args.get, details)
        else:
            print(f"API not found: {args.get}")
    
    elif args.list_tags:
        results = search_apis(spec, "tag")
        print_api_list(results, "Tag APIs")
    
    elif args.list_alarm:
        results = search_apis(spec, "alarm")
        print_api_list(results, "Alarm APIs")
    
    elif args.list_project:
        results = search_apis(spec, "project")
        print_api_list(results, "Project APIs")
    
    elif args.list_db:
        results = search_apis(spec, "db")
        print_api_list(results, "Database APIs")
    
    elif args.list_all:
        results = list_all_apis(spec)
        print_api_list(results, "All APIs")
    
    elif args.count:
        paths = spec.get("paths", {})
        print(f"Total API endpoints: {len(paths)}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
