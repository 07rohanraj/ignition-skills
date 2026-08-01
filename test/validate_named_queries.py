import os
import subprocess
import re

base_dir = r"C:\Program Files\Inductive Automation\Ignition\data\projects\WaterControlSystem\ignition\named-query\WCS"
psql_cmd = r"C:\Program Files\PostgreSQL\17\bin\psql.exe"

os.environ["PGPASSWORD"] = "root"

# Sample values for parameter replacement during testing
test_params = {
    ":LocationName": "'Test Facility'",
    ":TimeZone": "'America/Chicago'",
    ":Address1": "'123 Test St'",
    ":Address2": "'Suite 1'",
    ":City": "'Houston'",
    ":State": "'Texas'",
    ":ZipCode": "'77001'",
    ":Country": "'USA'",
    ":SiteKey": "1",
    ":SiteId": "'S00001'",
    ":TankSystemId": "'TK001'",
    ":HeaterType": "'Immersion 15kW'",
    ":PanelType": "'Panel A'",
    ":PanelSerial": "'PNL-9999'",
    ":NamespaceName": "'S00001_TK001'",
    ":NamespaceId": "1",
    ":NamespaceIgnId": "2",
    ":NamespaceIgnName": "'S00001_TK001_IGN'",
    ":TankKey": "1",
    ":ExcludeSiteKey": "NULL::integer",
    ":ExcludeTankKey": "NULL::integer",
    ":UserId": "1"
}

def test_query(qname):
    sql_file = os.path.join(base_dir, qname, "query.sql")
    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()

    test_sql = sql
    # Sort params by length descending so longer params replace before shorter prefixes
    for param in sorted(test_params.keys(), key=len, reverse=True):
        val = test_params[param]
        # Replace :param when followed by a non-word char or end of line
        pattern = re.escape(param) + r'(?!\w)'
        test_sql = re.sub(pattern, val, test_sql)

    wrapped = f"BEGIN;\n{test_sql}\nROLLBACK;"

    cmd = [psql_cmd, "-h", "localhost", "-U", "postgres", "-d", "WCS", "-c", wrapped]
    res = subprocess.run(cmd, capture_output=True, text=True)

    if res.returncode == 0 and "ERROR" not in res.stderr:
        print(f"PASS: {qname}")
        return True
    else:
        print(f"FAIL: {qname}")
        print("  Error:", res.stderr.strip() or res.stdout.strip())
        print("  SQL executed:\n", test_sql)
        return False

queries = sorted(os.listdir(base_dir))
passed = 0
failed = 0

print(f"Validating {len(queries)} queries against PostgreSQL WCS database...\n")
for q in queries:
    if test_query(q):
        passed += 1
    else:
        failed += 1

print(f"\nResult: {passed} passed, {failed} failed out of {len(queries)}")
