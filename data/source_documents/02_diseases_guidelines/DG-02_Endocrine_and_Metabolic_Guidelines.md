---
doc_id: DG-02
title: "Endocrine and Metabolic Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-004, PAT-008, PAT-012, PAT-014, DIS-001, DIS-013, DIS-014, DIS-016, MED-001, MED-002, MED-003, MED-009, MED-024, MED-030, LAB-002, LAB-003, LAB-005, LAB-009, LAB-017, LAB-018, LAB-028, PRO-008, PRO-010, DEP-004, STF-006, FPA-03, FPA-12, FPA-14]
related_docs: [DG-01, HO-02, LD-01, LD-03, LD-04, MP-02, MP-06, MP-07, PR-01, PR-04, PR-07, PR-08]
---

# DG-02: Endocrine and Metabolic Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-02 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Type 2 diabetes (DIS-001), diabetic ketoacidosis (DIS-013), hyperlipidemia (DIS-014), hypothyroidism (DIS-016) |
| Owner | Endocrinology and Diabetes (DEP-004, head STF-006), approved by the CPRB |
| Companion documents | MP-02, MP-06, MP-07, LD-01, LD-03, LD-04, HO-02 |

## 2. Purpose and Scope

This guideline gives diagnostic criteria, targets, and treatment rules for four endocrine and metabolic conditions. It is the clinical rationale behind the renal dose cap for metformin (operationalized in PRO-008), the SGLT2-inhibitor safety rules, the insulin-infusion transition (operationalized in PRO-010), and the levothyroxine separation rule. Charts that apply it are PR-01, PR-04, PR-07 and PR-08.

## 3. Type 2 Diabetes Mellitus (DIS-001)

### 3.1 Diagnosis
Diagnose with HbA1c (LAB-003) of **6.5% or higher** or fasting glucose of 7.0 mmol/L (126 mg/dL) or higher, confirmed on a second occasion unless symptomatic with a random glucose of 11.1 mmol/L (200 mg/dL) or higher.

### 3.2 Targets
HbA1c target is **7.0% to 7.5%** for most adults. Less stringent targets (up to 8.0%) are acceptable in frail patients or those with limited life expectancy. Blood pressure target is below 130/80 mmHg (DG-01); lipid targets are in section 5.

### 3.3 Treatment

| Step | Agent | Rule |
|---|---|---|
| First line | Metformin (MED-001) | Start 500 mg daily; titrate to 1,000 mg twice daily if eGFR allows |
| Add-on | SGLT2 inhibitor: empagliflozin (MED-030) | Only with sick-day teaching; see 3.5 |
| Insulin | Basal insulin glargine (MED-002) | Start 10 units nightly or 0.1 to 0.2 units/kg; titrate to fasting glucose |

### 3.4 Metformin and kidney function (rationale for the renal cap)
Metformin is renally cleared; accumulation raises the risk of lactic acidosis. The reference guideline rule is:

| eGFR (mL/min/1.73 m2) | Rule |
|---|---|
| 45 or higher | No reduction required |
| **30 to 44** | **Maximum 1,000 mg per day** |
| Below 30 | Stop |

MediCore applies this rule through PRO-008 and FPA-03 (HO-02); the practical dose tables are in MP-02 and MP-07. During acute illness with dehydration, pause metformin (sick-day rule). Charts showing the rule in action: PR-01 (eGFR 44 on 2025-02-20, dose reduced 2025-03-13) and PR-04 (eGFR 88, no cap).

### 3.5 SGLT2 inhibitor precautions
SGLT2 inhibitors can cause ketoacidosis with near-normal glucose. The reference guideline requires:
1. Teach the **sick-day rule** at initiation: stop the drug during vomiting, fever, diarrhea, or poor oral intake, and for 3 days before elective surgery.
2. Check ketones if unwell even when glucose is not high.
3. After an episode of ketoacidosis attributed to an SGLT2 inhibitor, **do not re-challenge** with the drug class (MP-02).

PAT-004 (PR-04) developed ketoacidosis on 2025-12-09 after not following the sick-day rule; empagliflozin was permanently stopped and recorded as an adverse drug reaction.

## 4. Diabetic Ketoacidosis (DIS-013)

### 4.1 Diagnosis
Diagnose when all are present: (1) beta-hydroxybutyrate (LAB-028) of **3.0 mmol/L or higher**; (2) venous or arterial pH below 7.30 or bicarbonate below 18 mmol/L (LAB-018, LAB-002); (3) diabetes or known risk. The **euglycemic variant** is diagnosed when glucose is below 14 mmol/L (250 mg/dL) with the same ketone and acid-base criteria; the SGLT2 inhibitor is the usual cause. Severity: mild pH 7.25 to 7.29; moderate 7.00 to 7.24; severe below 7.00. PAT-004 presented with pH 7.18 (moderate).

### 4.2 Management

| Component | Reference rule |
|---|---|
| Fluids | Isotonic fluid resuscitation first |
| Potassium | Check potassium (LAB-005) before insulin. If below 3.3 mmol/L, replace first and delay insulin. If 3.3 to 5.2 mmol/L, give replacement with the insulin infusion |
| Insulin | Insulin regular (MED-003) IV infusion at 0.1 units/kg/hour; add dextrose when glucose falls below 14 mmol/L in the typical form, or earlier in the euglycemic form |
| Monitoring | Beta-hydroxybutyrate and glucose hourly initially, then every 2 hours; potassium every 2 to 4 hours |
| Hypoglycemia | Glucose below the alert threshold needs dextrose added and the infusion rate reviewed |
| Transition | Switch to subcutaneous insulin when ketones have cleared, with **basal insulin given at least 2 hours before the infusion is stopped** |

### 4.3 Resolution criterion
The reference guideline defines resolution of ketoacidosis as beta-hydroxybutyrate below 0.6 mmol/L. MediCore requires this on **two consecutive checks** before transition (MediCore Policy, FPA-12, PRO-010, HO-02), and defines its hypoglycemia alert at a glucose below 4.0 mmol/L (72 mg/dL).

### 4.4 Application
PAT-004: ketones fell from 5.4 to 0.4 mmol/L over 20 hours; the criterion was first met at 16:00 on 2025-12-10 (PR-04); glargine was given at 16:30 and the infusion stopped at 18:30, a 2-hour overlap.

## 5. Hyperlipidemia (DIS-014)

### 5.1 Diagnosis and risk categories
The lipid panel (LAB-009) is used. LDL-cholesterol targets by risk category:

| Risk category | LDL-C target |
|---|---|
| Established atherosclerotic disease (for example after ACS) | below 1.4 mmol/L (55 mg/dL) |
| High risk (diabetes with CKD or multiple risk factors) | below 1.8 mmol/L (70 mg/dL) |
| Moderate risk | below 2.6 mmol/L (100 mg/dL) |

### 5.2 Treatment
Atorvastatin (MED-009) is first line: 40 mg daily for high risk, 80 mg daily after ACS. Recheck lipids 6 to 8 weeks after starting or changing the dose. Report muscle symptoms. PAT-008 (PR-07) started 80 mg after NSTEMI; PAT-001 (PR-01) takes 40 mg.

## 6. Hypothyroidism (DIS-016)

### 6.1 Diagnosis
TSH (LAB-017) above the upper limit of the reference interval (**0.4 to 4.0 mIU/L**, LD-01) with low or low-normal free thyroxine.

### 6.2 Treatment
Levothyroxine (MED-024), starting at 1.6 micrograms/kg/day in healthy adults (25 to 50 micrograms in older patients or those with heart disease). Take once daily on an empty stomach, 30 to 60 minutes before breakfast.

### 6.3 Interactions that reduce absorption
Oral iron, calcium, and antacids must be separated from levothyroxine by **at least 4 hours** (MediCore Policy FPA-14; MP-02, MP-06). If a new interacting drug is started, recheck TSH after 6 to 8 weeks.

### 6.4 Interpreting TSH
Acute illness can transiently alter TSH; avoid dose changes on a single value during illness (PAT-004: TSH 4.1 mIU/L during ketoacidosis, 3.8 on 2026-03-18). Persistent elevation after a new co-medication suggests an absorption problem rather than disease progression (PAT-014: TSH 2.4, then 8.9 after iron was taken 30 minutes after levothyroxine, then 3.2 after separation; PR-08).

## 7. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-001 | T2DM with CKD; metformin cap | PR-01 |
| PAT-004 | SGLT2-associated euglycemic DKA; hypothyroidism | PR-04 |
| PAT-008 | Post-ACS statin | PR-07 |
| PAT-012 | T2DM with metformin during pneumonia | PR-08 |
| PAT-014 | Levothyroxine absorption | PR-08 |

## 8. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Metformin, insulin, empagliflozin, levothyroxine monographs | MP-02 |
| Interaction severities | MP-06 |
| Renal dosing tiers | MP-07 |
| HbA1c, ketone, glucose, TSH reports; reference ranges | LD-03, LD-01 |
| Blood gas reports | LD-04 |
| Renal dose protocol; insulin infusion transition | HO-02 |

## 9. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
