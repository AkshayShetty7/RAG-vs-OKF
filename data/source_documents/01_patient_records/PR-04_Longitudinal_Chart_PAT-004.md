---
doc_id: PR-04
title: "Longitudinal Chart: PAT-004 (Elena Voss)"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-004, DIS-001, DIS-013, DIS-016, MED-001, MED-002, MED-003, MED-024, MED-030, LAB-002, LAB-003, LAB-005, LAB-017, LAB-018, LAB-028, PRO-009, PRO-010, DEP-001, DEP-004, DEP-009, STF-006, FPA-03, FPA-12]
related_docs: [DG-02, HO-02, HO-05, LD-03, LD-04, MP-02, MP-06]
---

# PR-04: Longitudinal Chart, PAT-004 (Elena Voss)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-04 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Record period covered | 2024-09-10 to 2026-09-09 |
| Patient | PAT-004 |
| Primary services | DEP-004 Endocrinology and Diabetes (head STF-006); DEP-001; DEP-009 |
| Reference guideline | DG-02 (diabetes, DKA, hypothyroidism) |
| Reference monographs | MP-02 (metformin, insulins, empagliflozin, levothyroxine), MP-06 |
| Policies applied | PRO-010 (insulin infusion transition, hypoglycemia alert), PRO-009 (HO-02, HO-05) |

## 2. Purpose and Scope

This chart records the care of PAT-004, who has type 2 diabetes (DIS-001) and hypothyroidism (DIS-016). It centers on an admission on 2025-12-09 for **diabetic ketoacidosis with near-normal glucose** (DIS-013) associated with the SGLT2 inhibitor empagliflozin (MED-030) during an acute febrile illness. The chart documents the ketone series, the insulin infusion and its transition criterion (FPA-12), a hypoglycemia alert during the infusion, and the permanent discontinuation of empagliflozin.

## 3. Patient Summary

| Item | Value |
|---|---|
| Patient ID / name | PAT-004 / Elena Voss (synthetic) |
| Date of birth / age | 1972-05-09 / 54 years (at 2026-10-01) |
| Sex | Female |
| Height / weight | 165 cm; 72 kg (2025-12-09), 70 kg (2026-09-09) |
| Occupation | Primary school teacher |
| Allergy | **No known drug allergies**; no ALG entity applies |
| Adverse drug reaction (not an allergy) | Empagliflozin: ketoacidosis 2025-12-09; do not re-challenge |

## 4. Problem List

| Problem | ID | Onset | Status at 2026-09-09 |
|---|---|---|---|
| Type 2 diabetes mellitus | DIS-001 | 2016 | Active; HbA1c 7.0% |
| Diabetic ketoacidosis, SGLT2-inhibitor-associated, near-normal glucose | DIS-013 | 2025-12-09 | Resolved |
| Hypothyroidism | DIS-016 | 2019 | Stable; TSH 3.8 mIU/L |

## 5. Medication History

| Medication | ID | Dose history | Notes |
|---|---|---|---|
| Metformin | MED-001 | 1,000 mg twice daily since 2016; held 2025-12-09 to 2025-12-11; resumed 2025-12-12 | eGFR 88; no renal cap applies (FPA-03 applies only at eGFR 44 or lower) |
| Insulin glargine | MED-002 | 20 units nightly from 2023-04; increased to 24 units on 2025-12-30 | Basal insulin |
| Empagliflozin | MED-030 | 10 mg daily from 2024-09-10; **stopped 2025-12-09 permanently** | See section 7 |
| Levothyroxine | MED-024 | 88 micrograms daily since 2019; unchanged | Taken at 06:30 fasting |
| Insulin regular (IV infusion) | MED-003 | 2025-12-09 19:55 to 2025-12-10 18:30 | Inpatient only |

## 6. Encounter Log

| Encounter | Date | Service | Key findings |
|---|---|---|---|
| ENC-004-01 | 2024-09-10 | DEP-004 | HbA1c (LAB-003) 8.4%; empagliflozin added; sick-day teaching given (hold empagliflozin and metformin during vomiting, fever, or poor intake) |
| ENC-004-02 | 2025-03-12 | DEP-004 | HbA1c 7.5%; weight 73 kg |
| ENC-004-03 | 2025-12-09 to 2025-12-12 | DEP-001, DEP-009 | DKA admission (section 7) |
| ENC-004-04 | 2025-12-30 | DEP-004 | HbA1c 7.6%; glargine increased to 24 units; empagliflozin documented as ADR |
| ENC-004-05 | 2026-03-18 | DEP-004 | HbA1c 7.2%; TSH 3.8 |
| ENC-004-06 | 2026-09-09 | DEP-004 | HbA1c 7.0%; weight 70 kg |

## 7. Admission for Ketoacidosis, 2025-12-09 to 2025-12-12 (ENC-004-03)

### 7.1 Background
Three days of fever (38.4 C), vomiting, and almost no oral intake after a household viral illness. The patient continued empagliflozin and metformin and reduced insulin glargine to 10 units. She presented to DEP-001 at 19:10 on 2025-12-09 with abdominal pain, rapid breathing, and drowsiness.

### 7.2 Initial results
| Test | Result |
|---|---|
| Glucose (LAB-028) | 11.8 mmol/L (212 mg/dL), only mildly raised |
| Beta-hydroxybutyrate (LAB-028), 20:00 | 5.4 mmol/L |
| ABG (LAB-018) | pH 7.18, bicarbonate 9 mmol/L, PaCO2 2.4 kPa (18 mmHg) |
| BMP (LAB-002) | Sodium 137, potassium 3.3 mmol/L (LAB-005), creatinine 0.8 mg/dL, eGFR 88, anion gap 24 |
| HbA1c (LAB-003) | 7.6% |
| TSH (LAB-017), drawn 2025-12-10 | 4.1 mIU/L |

Because the glucose was not markedly elevated, the diagnosis rested on ketones and acidosis, in line with DG-02. The pattern was attributed to empagliflozin combined with starvation and reduced insulin.

### 7.3 Insulin infusion and ketone series (PRO-010, FPA-12)
An insulin regular infusion (MED-003) was begun at 19:55 at 0.1 units per kg per hour (7.2 units/h) with fluids and potassium replacement (a non-registry electrolyte agent). Admission to DEP-009 for monitoring.

| Time | Beta-hydroxybutyrate (mmol/L) | Comment |
|---|---|---|
| 2025-12-09 20:00 | 5.4 | Baseline |
| 21:00 | 4.8 | |
| 23:00 | 3.9 | |
| 2025-12-10 02:00 | 2.6 | |
| 06:00 | 1.5 | K 3.9 mmol/L |
| 10:00 | 0.9 | |
| 14:00 | 0.5 | First value below 0.6 |
| 16:00 | 0.4 | Second consecutive value below 0.6 |

**Transition criterion:** FPA-12 requires beta-hydroxybutyrate below 0.6 mmol/L on two consecutive checks. The criterion was first met at **16:00 on 2025-12-10**. Insulin glargine 20 units was given subcutaneously at 16:30 and the infusion was stopped at 18:30 after a two-hour overlap.

### 7.4 Hypoglycemia alert
At 03:20 on 2025-12-10 the capillary glucose was 3.8 mmol/L (68 mg/dL). The hypoglycemia alert threshold in FPA-12 is below 4.0 mmol/L, so the alert was triggered. Dextrose 10% was added to the infusion fluid and the glucose rose to 6.2 mmol/L by 04:20. Ketone clearance continued.

### 7.5 Discharge and decisions
Metformin was resumed 2025-12-12 once oral intake was normal. Empagliflozin was permanently discontinued and entered as an adverse drug reaction; MP-02 and DG-02 describe the contraindication for re-challenge. Discharged 2025-12-12 on glargine 20 units, metformin 1,000 mg twice daily, levothyroxine 88 micrograms. Patient re-taught sick-day rules by diabetes educator.

## 8. Hypothyroidism Management

TSH was 4.1 mIU/L during the admission (acute illness can alter TSH), 3.8 on 2026-03-18, and levothyroxine was unchanged. No interacting supplements were reported; levothyroxine interactions with oral iron are described in MP-06 and MP-02 but do not apply to this patient.

## 9. Policy Compliance Review (retrospective)

| Policy | Requirement | Observed | Result |
|---|---|---|---|
| PRO-010 / FPA-12 | Transition when BHB below 0.6 on two consecutive checks | First met 16:00 on 2025-12-10; transition 16:30 | Met |
| PRO-010 / FPA-12 | Hypoglycemia alert below 4.0 mmol/L | Alert at 3.8 mmol/L, corrected within 60 minutes | Met |
| PRO-009 | Critical results phoned | No critical-threshold result in the series | Not triggered |
| DG-02 sick-day rule | Hold SGLT2 inhibitor during acute illness | Not followed by patient; taught 2024-09-10 | Patient factor |

## 10. Laboratory Series (consolidated; official reports in LD-03, LD-04)

| Date | HbA1c (%) | Glucose (mmol/L) | BHB (mmol/L) | K (mmol/L) | pH | eGFR |
|---|---|---|---|---|---|---|
| 2024-09-10 | 8.4 | n/a | n/a | 4.2 | n/a | 90 |
| 2025-03-12 | 7.5 | n/a | n/a | 4.3 | n/a | 89 |
| 2025-12-09 | 7.6 | 11.8 | 5.4 | 3.3 | 7.18 | 88 |
| 2025-12-10 16:00 | n/a | 7.1 | 0.4 | 4.0 | n/a | n/a |
| 2025-12-30 | 7.6 | n/a | n/a | 4.4 | n/a | 87 |
| 2026-03-18 | 7.2 | n/a | n/a | 4.3 | n/a | 88 |
| 2026-09-09 | 7.0 | n/a | n/a | 4.4 | n/a | 87 |

## 11. Other Records (non-diagnostic and background)

- Retinal screening 2025-04-02 and 2026-04-01: no retinopathy.
- Influenza vaccine 2025-10-14 and 2026-09-24.
- Dietitian visits 2025-12-15 and 2026-03-18: carbohydrate counting and hydration plan.
- Dental: routine cleaning 2026-05-06.
- Social history: lives with partner and one teenage child; walks daily; no tobacco; alcohol occasional.

## 12. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| DKA criteria; SGLT2 inhibitor precautions | DG-02, MP-02 |
| Insulin infusion transition and hypoglycemia alert | HO-02 (PRO-010) |
| Ketone, glucose, HbA1c, TSH reports | LD-03 |
| Blood gas reports | LD-04 |
| Critical result notification | HO-05 |
| Drug interactions for empagliflozin and levothyroxine | MP-06 |

## 13. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic chart (Pass 1) |
