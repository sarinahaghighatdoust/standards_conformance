
import sys, csv, json, statistics
from datetime import datetime

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main(kpi_map_csv, harness_csv):
    km = read_csv(kpi_map_csv)
    hz = read_csv(harness_csv)
    # Basic referential integrity
    kpi_ids = {r["kpi_id"] for r in km}
    orphans = [t for t in hz if t["kpi_id"] not in kpi_ids]
    if orphans:
        print("[FAIL] Test harness references unknown KPI ids:", sorted({t["kpi_id"] for t in orphans}))
    else:
        print("[OK] All test harness KPI ids are defined in KPI mapping.")
    # Sanity checks
    for r in hz:
        if r["rule_type"] == "threshold" and r["comparator"] not in {"<","<=",">",">=","==","!=","between"}:
            print(f"[FAIL] Invalid comparator in {r['test_id']}: {r['comparator']}")
        if r["expected_update_latency"] and r["expected_update_latency"].endswith("m"):
            pass
    # Print a short manifest
    domains = {}
    for r in km:
        dom = r.get("standard","NA")
        domains.setdefault(dom, 0); domains[dom] += 1
    print("[INFO] KPI counts by standard:", domains)
    print("[INFO] Example complete. For full validation, plug into your data pipeline.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_kpis.py <kpi_mapping.csv> <kpi_test_harness.csv>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
