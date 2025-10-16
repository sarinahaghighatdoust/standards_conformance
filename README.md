
# Smart-City KPI Standards & Conformance Pack (Algorithmic Metropolis Edition)

This repository accompanies the paper *“The Algorithmic Metropolis: A Review of Architectures, Enabling Technologies, and Socio-Technical Challenges in Smart City Implementation”* by Sarina Haghighatdoust (2025).  
It provides a reproducible checklist linking ISO 37120/37122 and ITU Y.4900 KPIs to concrete data fields and an executable test harness for automated conformance checks.

## Contents
- `mapping/kpi_mapping_city.csv` — filled KPI-to-data mapping for city domains (mobility, energy, public safety).
- `harness/kpi_test_harness_city.csv` — executable test harness with KPI rules (thresholds, lookbacks, actions).
- `scripts/validate_kpis.py` — validator script for referential/syntax checks.
- `Supplementary_Log_S4_validator.txt` — output log confirming schema and integrity.
- `LICENSE` — MIT License for code, CC-BY 4.0 for data.


## How to use
1. Use the provided filled CSVs (`kpi_mapping_city.csv` and `kpi_test_harness_city.csv`) as your reproducible reference implementation.
2. Run a basic check:  
   ```bash
   python scripts/validate_kpis.py mapping/kpi_mapping_city.csv harness/kpi_test_harness_city.csv > Supplementary_Log_S4_validator.txt 2>&1
   ```
3. Wire the harness into your analytics jobs:
   - Join the KPI mapping to your telemetry views.
   - Compute KPIs per the `calculation_method`.
   - Apply tests from `kpi_test_harness_*` by `kpi_id`, respecting `lookback_window`, `min_sample_size`, and `group_by`.
   - Emit a conformance report (CSV/JSON) with pass/fail and evidence.

## Citation
If archived on Zenodo, cite as:
> *Smart-City KPI Standards & Conformance Pack (Algorithmic Metropolis Edition)*, v1.0.  
> DOI: [10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)


## Suggested reference text (for your manuscript)
“We release a machine-readable **Standards & Conformance Checklist** (DOI:10.5281/zenodo.XXXXXXX) that maps each KPI to a specific data field set and ships an executable **test harness** for automated verification.  
This artifact enables reproducible KPI validation and governance-by-design checks for smart-city infrastructures.”

## Licensing
- Code: MIT License  
- Data/CSVs: CC BY 4.0 License  
(See LICENSE for details.)

## Acknowledgment
Prepared under supervision of Dr. Aledhari to support reproducibility and traceability in smart-city KPI governance.

