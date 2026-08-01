import os
import json
import secrets
from datetime import datetime, timezone

base = r'C:\Program Files\Inductive Automation\Ignition\data\projects\WaterControlSystem\ignition\named-query\WCS'
os.makedirs(base, exist_ok=True)

common_attrs = {
    "scope": "DG",
    "version": 2,
    "restricted": False,
    "overridable": True,
    "files": ["query.sql"],
    "attributes": {
        "useMaxReturnSize": False,
        "autoBatchEnabled": False,
        "fallbackValue": "",
        "maxReturnSize": 100,
        "cacheUnit": "SEC",
        "enabled": True,
        "cacheAmount": 1,
        "cacheEnabled": False,
        "database": "WCS",
        "fallbackEnabled": False,
        "lastModificationSignature": "",
        "permissions": [{"zone": "", "role": ""}],
        "lastModification": {
            "actor": "admin",
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    }
}

def make_signature():
    return secrets.token_hex(32)

# Queries definitions
queries = [
    # 1. addSite
    (
        "addSite", "UpdateQuery",
        """INSERT INTO public.site (location_name, time_zone, address1, address2, city, state, zip_code, country)
VALUES (:LocationName, :TimeZone, :Address1, :Address2, :City, :State, :ZipCode, :Country);""",
        [
            {"type": "Parameter", "identifier": "LocationName", "sqlType": 8},
            {"type": "Parameter", "identifier": "TimeZone", "sqlType": 8},
            {"type": "Parameter", "identifier": "Address1", "sqlType": 8},
            {"type": "Parameter", "identifier": "Address2", "sqlType": 8},
            {"type": "Parameter", "identifier": "City", "sqlType": 8},
            {"type": "Parameter", "identifier": "State", "sqlType": 8},
            {"type": "Parameter", "identifier": "ZipCode", "sqlType": 8},
            {"type": "Parameter", "identifier": "Country", "sqlType": 8}
        ]
    ),
    # 2. editSite
    (
        "editSite", "UpdateQuery",
        """UPDATE public.site
SET
    location_name = :LocationName,
    time_zone = :TimeZone,
    address1 = :Address1,
    address2 = :Address2,
    city = :City,
    state = :State,
    zip_code = :ZipCode,
    country = :Country
WHERE site_key = :SiteKey;""",
        [
            {"type": "Parameter", "identifier": "LocationName", "sqlType": 8},
            {"type": "Parameter", "identifier": "TimeZone", "sqlType": 8},
            {"type": "Parameter", "identifier": "Address1", "sqlType": 8},
            {"type": "Parameter", "identifier": "Address2", "sqlType": 8},
            {"type": "Parameter", "identifier": "City", "sqlType": 8},
            {"type": "Parameter", "identifier": "State", "sqlType": 8},
            {"type": "Parameter", "identifier": "ZipCode", "sqlType": 8},
            {"type": "Parameter", "identifier": "Country", "sqlType": 8},
            {"type": "Parameter", "identifier": "SiteKey", "sqlType": 2}
        ]
    ),
    # 3. deleteSite
    (
        "deleteSite", "UpdateQuery",
        """WITH s AS (
    SELECT site_id FROM public.site WHERE site_key = :SiteKey
)
DELETE FROM public.site
WHERE site_key = :SiteKey
  AND NOT EXISTS (
    SELECT 1 FROM public.tank_system t JOIN s ON t.site_id = s.site_id
  );""",
        [
            {"type": "Parameter", "identifier": "SiteKey", "sqlType": 2}
        ]
    ),
    # 4. addTank
    (
        "addTank", "UpdateQuery",
        """INSERT INTO public.tank_system (tank_system_id, site_id, heater_type, panel_type, panel_serial, namespace_name, namespace_id, "namespaceIgn_id", "namespaceIgn_name")
VALUES (:TankSystemId, :SiteId, :HeaterType, :PanelType, :PanelSerial, :NamespaceName, :NamespaceId, :NamespaceIgnId, :NamespaceIgnName);""",
        [
            {"type": "Parameter", "identifier": "TankSystemId", "sqlType": 8},
            {"type": "Parameter", "identifier": "SiteId", "sqlType": 8},
            {"type": "Parameter", "identifier": "HeaterType", "sqlType": 8},
            {"type": "Parameter", "identifier": "PanelType", "sqlType": 8},
            {"type": "Parameter", "identifier": "PanelSerial", "sqlType": 8},
            {"type": "Parameter", "identifier": "NamespaceName", "sqlType": 8},
            {"type": "Parameter", "identifier": "NamespaceId", "sqlType": 2},
            {"type": "Parameter", "identifier": "NamespaceIgnId", "sqlType": 2},
            {"type": "Parameter", "identifier": "NamespaceIgnName", "sqlType": 8}
        ]
    ),
    # 5. editTank
    (
        "editTank", "UpdateQuery",
        """UPDATE public.tank_system
SET
    tank_system_id = :TankSystemId,
    site_id = :SiteId,
    heater_type = :HeaterType,
    panel_type = :PanelType,
    panel_serial = :PanelSerial,
    namespace_name = :NamespaceName,
    namespace_id = :NamespaceId,
    "namespaceIgn_id" = :NamespaceIgnId,
    "namespaceIgn_name" = :NamespaceIgnName
WHERE tank_key = :TankKey;""",
        [
            {"type": "Parameter", "identifier": "TankSystemId", "sqlType": 8},
            {"type": "Parameter", "identifier": "SiteId", "sqlType": 8},
            {"type": "Parameter", "identifier": "HeaterType", "sqlType": 8},
            {"type": "Parameter", "identifier": "PanelType", "sqlType": 8},
            {"type": "Parameter", "identifier": "PanelSerial", "sqlType": 8},
            {"type": "Parameter", "identifier": "NamespaceName", "sqlType": 8},
            {"type": "Parameter", "identifier": "NamespaceId", "sqlType": 2},
            {"type": "Parameter", "identifier": "NamespaceIgnId", "sqlType": 2},
            {"type": "Parameter", "identifier": "NamespaceIgnName", "sqlType": 8},
            {"type": "Parameter", "identifier": "TankKey", "sqlType": 2}
        ]
    ),
    # 6. deleteTank
    (
        "deleteTank", "UpdateQuery",
        """DELETE FROM public.tank_system WHERE tank_key = :TankKey;""",
        [
            {"type": "Parameter", "identifier": "TankKey", "sqlType": 2}
        ]
    ),
    # 7. getAllSites
    (
        "getAllSites", "Query",
        """SELECT site_key, site_id, location_name, time_zone, address1, address2, city, state, zip_code, country
FROM public.site
WHERE site_key IS NOT NULL
ORDER BY site_key;""",
        []
    ),
    # 8. getAllTanks
    (
        "getAllTanks", "Query",
        """SELECT t.tank_key, t.tank_system_id, t.site_id, s.site_id AS site_site_id, s.location_name,
       t.heater_type, t.panel_type, t.panel_serial,
       t.namespace_name, t.namespace_id, t."namespaceIgn_id", t."namespaceIgn_name"
FROM public.tank_system t
JOIN public.site s ON s.site_id = t.site_id
ORDER BY t.tank_key;""",
        []
    ),
    # 9. getTanksBySite
    (
        "getTanksBySite", "Query",
        """SELECT t.tank_key, t.tank_system_id, t.site_id, s.site_id AS site_site_id, s.location_name,
       t.heater_type, t.panel_type, t.panel_serial,
       t.namespace_name, t.namespace_id, t."namespaceIgn_id", t."namespaceIgn_name"
FROM public.tank_system t
JOIN public.site s ON s.site_id = t.site_id
WHERE t.site_id = :SiteId
ORDER BY t.tank_key;""",
        [
            {"type": "Parameter", "identifier": "SiteId", "sqlType": 8}
        ]
    ),
    # 10. checkDuplicateSiteName
    (
        "checkDuplicateSiteName", "Query",
        """SELECT COUNT(*) AS DuplicateCount
FROM public.site
WHERE LOWER(location_name) = LOWER(:LocationName)
  AND (:ExcludeSiteKey IS NULL OR site_key <> :ExcludeSiteKey);""",
        [
            {"type": "Parameter", "identifier": "LocationName", "sqlType": 8},
            {"type": "Parameter", "identifier": "ExcludeSiteKey", "sqlType": 2}
        ]
    ),
    # 11. checkDuplicateTankId
    (
        "checkDuplicateTankId", "Query",
        """SELECT COUNT(*) AS DuplicateCount
FROM public.tank_system
WHERE tank_system_id = :TankSystemId
  AND (:ExcludeTankKey IS NULL OR tank_key <> :ExcludeTankKey);""",
        [
            {"type": "Parameter", "identifier": "TankSystemId", "sqlType": 8},
            {"type": "Parameter", "identifier": "ExcludeTankKey", "sqlType": 2}
        ]
    ),
    # 12. getNextSiteId
    (
        "getNextSiteId", "Query",
        """SELECT 'S' || lpad((COALESCE(MAX(site_key), 0) + 1)::text, 5, '0') AS NextSiteId
FROM public.site;""",
        []
    ),
    # 13. getTodayAlarmCountsByType
    (
        "getTodayAlarmCountsByType", "Query",
        """SELECT
    name AS AlarmType,
    COUNT(*) AS TotalCount,
    COUNT(*) FILTER (WHERE eventtype = 0) AS ActiveCount,
    COUNT(*) FILTER (WHERE eventtype = 1) AS ClearCount
FROM public.alarm_events
WHERE eventtime >= CURRENT_DATE AND eventtime < CURRENT_DATE + INTERVAL '1 day'
GROUP BY name
ORDER BY TotalCount DESC;""",
        []
    ),
    # 14. getActiveAlarms
    (
        "getActiveAlarms", "Query",
        """SELECT id, eventtype, severity, path, source, displaypath, name, value, unitstring, active, state, eventtime, duration, notes
FROM public.alarm_events
WHERE active = true
  AND (:SiteId IS NULL OR path LIKE '/tag:WCS/' || :SiteId || '%')
  AND (:TankSystemId IS NULL OR path LIKE '%/Tanks/' || :TankSystemId || '/%')
ORDER BY eventtime DESC;""",
        [
            {"type": "Parameter", "identifier": "SiteId", "sqlType": 8},
            {"type": "Parameter", "identifier": "TankSystemId", "sqlType": 8}
        ]
    ),
    # 15. getUserSites
    (
        "getUserSites", "Query",
        """SELECT s.site_key, s.site_id, s.location_name, s.city, s.state, s.country
FROM public.user_site us
JOIN public.site s ON s.site_key = us.site_key
WHERE us.user_id = :UserId
ORDER BY s.site_key;""",
        [
            {"type": "Parameter", "identifier": "UserId", "sqlType": 2}
        ]
    ),
    # 16. insertUserSite
    (
        "insertUserSite", "UpdateQuery",
        """INSERT INTO public.user_site (user_id, site_key) VALUES (:UserId, :SiteKey);""",
        [
            {"type": "Parameter", "identifier": "UserId", "sqlType": 2},
            {"type": "Parameter", "identifier": "SiteKey", "sqlType": 2}
        ]
    ),
    # 17. deleteUserSites
    (
        "deleteUserSites", "UpdateQuery",
        """DELETE FROM public.user_site WHERE user_id = :UserId;""",
        [
            {"type": "Parameter", "identifier": "UserId", "sqlType": 2}
        ]
    ),
]

for name, qtype, sql, params in queries:
    qdir = os.path.join(base, name)
    os.makedirs(qdir, exist_ok=True)

    with open(os.path.join(qdir, "query.sql"), "w", encoding="utf-8") as f:
        f.write(sql)

    res = json.loads(json.dumps(common_attrs))
    res["attributes"]["type"] = qtype
    res["attributes"]["lastModificationSignature"] = make_signature()
    if params:
        res["attributes"]["parameters"] = params

    with open(os.path.join(qdir, "resource.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)

    print(f"Created named query: WCS/{name} ({qtype}, {len(params)} params)")

print(f"\nSuccessfully generated {len(queries)} named queries!")
