---
doc_id: MP-02
title: "Formulary Monographs: Endocrine, GI and Supplements"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-004, PAT-010, PAT-012, PAT-014, DIS-001, DIS-013, DIS-016, DIS-018, DIS-019, DIS-022, MED-001, MED-002, MED-003, MED-020, MED-024, MED-028, MED-030, MED-031, LAB-001, LAB-003, LAB-004, LAB-005, LAB-017, LAB-025, LAB-028, PRO-002, PRO-008, PRO-010, DEP-010, STF-002, FPA-03, FPA-12, FPA-14]
related_docs: [DG-02, DG-03, DG-07, HO-02, LD-02, LD-03, MP-06, MP-07]
---

# MP-02: Formulary Monographs, Endocrine, GI and Supplements

> **SYNTHETIC DATA NOTICE.** This formulary is fictional and was written for software benchmarking and education. Doses, thresholds, and rules are invented, may differ from real-world practice, and must not be used for clinical decisions. "MediCore Policy" items are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-02 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, STF-002), approved by the P&T Committee |
| Medications covered | MED-001 metformin, MED-002 insulin glargine, MED-003 insulin regular, MED-024 levothyroxine, MED-028 pantoprazole, MED-030 empagliflozin, MED-031 ferrous sulfate |
| Related documents | DG-02, DG-07 (clinical rules); MP-06; MP-07; HO-02 (PRO-008 renal dose, PRO-010 insulin); LD-03 |

## 2. Purpose and Scope

Monographs for seven agents used in diabetes, thyroid disease, gastrointestinal protection, and iron deficiency. Interaction severities are owned by MP-06; kidney tiers by MP-07.

## 3. MED-001 Metformin

| Item | Detail |
|---|---|
| Class | Biguanide |
| Indications | Type 2 diabetes (DIS-001) |
| Adult dosing | Start 500 mg daily with food; increase to 500 mg twice daily, then to a usual maximum of 1,000 mg twice daily (2,000 mg/day) |
| **Renal adjustment (MediCore Policy FPA-03, PRO-008)** | eGFR 45 or higher: no cap. **eGFR 30 to 44: maximum 1,000 mg/day.** eGFR below 30: **stop** |
| Hold during | Dehydrating illness, vomiting, diarrhea, contrast studies with AKI risk (sick-day rule) |
| Monitoring | Creatinine/eGFR (LAB-004) at least every 6 months at eGFR below 60; HbA1c (LAB-003) every 3 to 6 months |
| Contraindications | eGFR below 30; acute metabolic acidosis; severe hepatic impairment |
| Key interactions | Ciprofloxacin (MED-020): glucose disturbance, Moderate; see MP-06 |
| High-alert | No |
| Dataset patients | PAT-001 (1,000 mg twice daily until 2025-03-13, then 500 mg twice daily); PAT-004 (1,000 mg twice daily; eGFR 88, no cap); PAT-012 (500 mg twice daily; eGFR 82) |

## 4. MED-002 Insulin Glargine

| Item | Detail |
|---|---|
| Class | Long-acting basal insulin |
| Indications | Type 2 diabetes (DIS-001); transition after DKA (DIS-013) |
| Adult dosing | Start 10 units nightly or 0.1 to 0.2 units/kg; titrate to fasting glucose; subcutaneous only |
| Renal adjustment | Reduced clearance in CKD raises hypoglycemia risk; titrate cautiously |
| Monitoring | Capillary glucose; HbA1c; hypoglycemia alert below 4.0 mmol/L (FPA-12) |
| High-alert (PRO-002) | **Yes** |
| DKA transition | Give the first subcutaneous dose at least 2 hours before the intravenous infusion is stopped (DG-02) |
| Dataset patients | PAT-004 (20 units nightly from 2023-04; 24 units from 2025-12-30) |

## 5. MED-003 Insulin Regular

| Item | Detail |
|---|---|
| Class | Short-acting human insulin; used here as an intravenous infusion and bolus |
| Indications | DKA (DIS-013); hyperkalemia shift (DIS-019) |
| Adult dosing | **DKA:** 0.1 units/kg/hour IV after potassium is safe. **Hyperkalemia:** 10 units IV with 25 g dextrose (DG-03) |
| Monitoring | Hourly glucose and ketones in DKA (LAB-028); potassium (LAB-005) every 2 to 4 hours; glucose for 4 to 6 hours after a hyperkalemia dose |
| Policy | Transition rules and hypoglycemia alert threshold in PRO-010 and FPA-12 (HO-02): beta-hydroxybutyrate below 0.6 mmol/L on two consecutive checks; glucose below 4.0 mmol/L |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-004 (infusion 2025-12-09 19:55 to 2025-12-10 18:30); PAT-001 (inpatient hyperkalemia dose, 2025-09-17) |

## 6. MED-024 Levothyroxine

| Item | Detail |
|---|---|
| Class | Synthetic thyroid hormone |
| Indications | Hypothyroidism (DIS-016) |
| Adult dosing | 1.6 micrograms/kg/day; start 25 to 50 micrograms in older adults or those with heart disease; take once daily, fasting, 30 to 60 minutes before breakfast |
| Monitoring | TSH (LAB-017) 6 to 8 weeks after any dose change or new interacting drug; reference interval 0.4 to 4.0 mIU/L |
| **Interaction (MediCore Policy FPA-14)** | Oral iron (MED-031), calcium, antacids: separate by **at least 4 hours** (Moderate, MP-06) |
| High-alert | No |
| Dataset patients | PAT-004 (88 micrograms); PAT-014 (100 micrograms; TSH 2.4 then 8.9 then 3.2 mIU/L) |

## 7. MED-028 Pantoprazole

| Item | Detail |
|---|---|
| Class | Proton pump inhibitor |
| Indications | Upper GI bleeding (DIS-022); GI protection during combined antithrombotic therapy |
| Adult dosing | **High-risk ulcer:** 80 mg IV bolus then 40 mg every 12 hours. **Low-risk ulcer:** 40 mg IV every 12 hours. Then 40 mg orally twice daily for 8 weeks; then 40 mg daily while antithrombotic therapy continues (DG-07) |
| Renal / hepatic | No renal adjustment; consider dose reduction in severe hepatic impairment |
| Interactions | Preferred PPI with clopidogrel because of weak CYP2C19 inhibition (Minor, MP-06) |
| High-alert | No |
| Dataset patients | PAT-002 (40 mg daily from 2025-03-04; escalated 2025-05-19; step-down 2025-07-15); PAT-010 (IV then 40 mg twice daily for 8 weeks) |

## 8. MED-030 Empagliflozin

| Item | Detail |
|---|---|
| Class | SGLT2 inhibitor |
| Indications | Type 2 diabetes (DIS-001) |
| Adult dosing | 10 mg once daily |
| Renal | Glycemic effect declines below eGFR 45; do not start below eGFR 20 |
| **Safety rules** | Teach the **sick-day rule**: stop during vomiting, fever, or poor intake, and 3 days before elective surgery. **Ketoacidosis with near-normal glucose** can occur; check ketones when unwell |
| **After DKA** | **Never re-challenge**; record as an adverse drug reaction (DG-02, MP-07) |
| Key interactions | Additive glucose lowering with insulin; Minor with metformin (MP-06) |
| High-alert | No |
| Dataset patients | PAT-004 (10 mg from 2024-09-10; permanently stopped 2025-12-09) |

## 9. MED-031 Ferrous Sulfate

| Item | Detail |
|---|---|
| Class | Oral iron (325 mg tablet contains 65 mg elemental iron) |
| Indications | Iron-deficiency anemia (DIS-018) |
| Adult dosing | 325 mg once daily, with vitamin C if tolerated; continue 3 months after hemoglobin normalizes (DG-07) |
| Monitoring | Hemoglobin (LAB-001) at 4 weeks; ferritin (LAB-025) at 3 months |
| Interactions | **Levothyroxine: separate by at least 4 hours (FPA-14).** Ciprofloxacin: separate (Moderate, MP-06) |
| Adverse effects | Constipation, dark stools |
| High-alert | No |
| Dataset patients | PAT-002 (2025-05-24 to 2025-08-24); PAT-014 (from 2026-04-07; taken at 14:00 from 2026-05-12) |

## 10. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Diabetes, DKA, hypothyroidism, GI bleeding, anemia guidelines | DG-02, DG-07 |
| Interaction severities | MP-06 |
| Renal dosing tiers | MP-07 |
| HbA1c, ketone, TSH, creatinine reports | LD-03 |
| Ferritin and hemoglobin reports | LD-02 |
| Renal dose and insulin safety protocols | HO-02 |

## 11. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic monograph set (Pass 1) |
