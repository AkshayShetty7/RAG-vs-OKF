---
doc_id: LD-01
title: "Test Catalog and Reference Ranges"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [LAB-001, LAB-002, LAB-003, LAB-004, LAB-005, LAB-006, LAB-007, LAB-008, LAB-009, LAB-010, LAB-011, LAB-012, LAB-013, LAB-014, LAB-015, LAB-016, LAB-017, LAB-018, LAB-019, LAB-020, LAB-021, LAB-022, LAB-023, LAB-024, LAB-025, LAB-026, LAB-027, LAB-028, PRO-004, PRO-009, PRO-014, DEP-011, DEP-012, STF-012, STF-013, FPA-01, FPA-05, FPA-07, FPA-08, FPA-12, FPA-13]
related_docs: [DG-01, DG-02, DG-03, DG-04, DG-05, DG-06, DG-07, HO-03, HO-04, HO-05, LD-02, LD-03, LD-04, LD-05, LD-06, LD-07, LD-08]
---

# LD-01: Test Catalog and Reference Ranges

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every value, range, threshold, and report number in this document are fictional. The catalog exists only for software benchmarking and education, must not be used for clinical decisions, and its ranges may differ from real-world laboratory practice.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-01 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Laboratory (DEP-011, Laboratory Director STF-012); imaging entries with Radiology (DEP-012, STF-013) |
| Systems | LabLink (laboratory information system); MediChart (EHR) |
| Related documents | LD-02 to LD-08 (patient reports); HO-05 (critical results and labeling, PRO-009 and PRO-014); DG-01 to DG-07 (clinical use) |

## 2. Purpose and Scope

This is the master definition of every test LAB-001 to LAB-028: specimen, units, reference interval, critical value where one applies, and turnaround. Reference values here are authoritative; reports in LD-02 to LD-08 repeat them. Units are SI with conventional values in parentheses where useful.

## 3. Critical Result Scope

MediCore Policy PRO-009 (HO-05) applies to **LAB-005, LAB-007, LAB-010, LAB-012, LAB-014 and LAB-024 only**. Critical results must be telephoned to the responsible clinician **within 20 minutes of verification, with read-back** (FPA-13). Other abnormal results are flagged H or L in the report but are not telephoned. Specimens are labeled under PRO-014.

| Test | Critical value (PRO-009) |
|---|---|
| LAB-005 Potassium | **6.2 mmol/L or higher, or 2.9 mmol/L or lower** (FPA-01) |
| LAB-007 hs-troponin | **100 ng/L or higher** |
| LAB-010 INR | **5.0 or higher** |
| LAB-012 Blood culture | Any positive bottle (Gram stain result) |
| LAB-014 Lactate | **4.0 mmol/L or higher** |
| LAB-024 C. difficile | Any positive result (call to ward and Infection Control) |

## 4. Test Catalog

### 4.1 Hematology and coagulation (report doc LD-02)

| ID | Test | Specimen | Unit | Reference interval | Notes |
|---|---|---|---|---|---|
| LAB-001 | Complete blood count | EDTA whole blood | g/dL, fL, x10^9/L | Hemoglobin: women 12.0 to 15.5, men 13.0 to 17.0. MCV 80 to 100. Platelets 150 to 400 | Not a PRO-009 test; low hemoglobin is flagged only |
| LAB-010 | PT/INR | Citrate plasma | ratio | INR 0.8 to 1.2 off anticoagulants; warfarin target 2.0 to 3.0 (FPA-05) | Critical 5.0 or higher |
| LAB-011 | aPTT | Citrate plasma | seconds | 25 to 35; heparin target 60 to 80 | Treatment target is not a reference range |
| LAB-025 | Ferritin and iron studies | Serum | ng/mL, % | Ferritin: women 15 to 150, men 30 to 400. Transferrin saturation 20 to 50% | Iron-deficiency criterion ferritin below 15 (DG-07) |
| LAB-026 | D-dimer | Citrate plasma | ng/mL FEU | Below 500 | Normal value excludes VTE at low probability (DG-06) |

### 4.2 Chemistry and metabolic (report doc LD-03)

| ID | Test | Specimen | Unit | Reference interval | Notes |
|---|---|---|---|---|---|
| LAB-002 | Basic metabolic panel | Serum | mmol/L, umol/L | Sodium 135 to 145; potassium 3.5 to 5.0; bicarbonate 22 to 29; anion gap 8 to 16 | Includes creatinine |
| LAB-003 | HbA1c | EDTA whole blood | % | Below 5.7 normal; 6.5 or higher diabetes; treatment target 7.0 to 7.5 (DG-02) | |
| LAB-004 | Serum creatinine and eGFR | Serum | umol/L (mg/dL); mL/min/1.73 m2 | Creatinine: men 62 to 106 (0.7 to 1.2 mg/dL); women 44 to 80 (0.5 to 0.9). eGFR 90 or higher | CKD stages per DG-03. Conversion: 1 mg/dL = 88.4 umol/L |
| LAB-005 | Potassium | Serum | mmol/L | 3.5 to 5.0 | **Critical 6.2 or higher / 2.9 or lower** |
| LAB-006 | Sodium | Serum | mmol/L | 135 to 145 | |
| LAB-009 | Lipid panel | Fasting serum | mmol/L | Total cholesterol below 5.2; LDL-C targets by risk in DG-02 | |
| LAB-017 | TSH | Serum | mIU/L | **0.4 to 4.0** | |
| LAB-028 | Glucose and beta-hydroxybutyrate | Plasma / capillary | mmol/L | Fasting glucose 4.0 to 5.5; beta-hydroxybutyrate below 0.6 | DKA threshold 3.0 or higher (DG-02); hypoglycemia alert below 4.0 (FPA-12) |

### 4.3 Cardiac, sepsis and gas exchange (report doc LD-04)

| ID | Test | Specimen | Unit | Reference interval | Notes |
|---|---|---|---|---|---|
| LAB-007 | hs-troponin | Lithium-heparin plasma | ng/L | 99th percentile **14 ng/L** | **Critical 100 ng/L or higher.** Serial draws at 0 and 2 hours (FPA-08) |
| LAB-008 | NT-proBNP | Serum | pg/mL | Supports HFrEF when above 450 (under 50 years), 900 (50 to 75), 1,800 (over 75) (DG-01) | |
| LAB-014 | Lactate | Fluoride plasma | mmol/L | 0.5 to 2.0 | **Critical 4.0 or higher.** Sepsis bundle repeat rule in PRO-004 (HO-03) |
| LAB-015 | Procalcitonin | Serum | ng/mL | Below 0.10; below 0.25 low likelihood of bacterial infection | Stewardship stop value 0.25 (HO-04) |
| LAB-016 | C-reactive protein | Serum | mg/L | Below 5 | |
| LAB-018 | Arterial blood gas | Arterial blood | pH, kPa (mmHg), mmol/L | pH 7.35 to 7.45; PaCO2 4.7 to 6.0 kPa (35 to 45); PaO2 above 10.6 kPa (80); bicarbonate 22 to 29 | |

### 4.4 Microbiology (report doc LD-05)

| ID | Test | Specimen | Reference | Notes |
|---|---|---|---|---|
| LAB-012 | Blood culture with susceptibility | Two sets, aerobic and anaerobic bottles | No growth at 5 days | **Any positive bottle is critical.** Susceptibilities follow identification |
| LAB-013 | Urinalysis and urine culture | Midstream or catheter urine | Nitrite and leukocyte esterase negative; culture below 10^5 CFU/mL | |
| LAB-024 | C. difficile toxin/PCR | Unformed stool | Negative | Only for 3 or more unformed stools in 24 hours (DG-05); **positive is critical** |

### 4.5 Cardiovascular diagnostics (report doc LD-06)

| ID | Test | Reference | Notes |
|---|---|---|---|
| LAB-021 | 12-lead ECG | Sinus rhythm; PR 120 to 200 ms; QRS below 120 ms | Chest-pain pathway target: within 10 minutes of arrival (FPA-08) |
| LAB-023 | Transthoracic echocardiogram | LVEF 55% or higher normal; 41 to 54% mildly reduced; **40% or lower reduced** | HFrEF criterion in DG-01 |

### 4.6 Imaging (report doc LD-07)

| ID | Test | Notes |
|---|---|---|
| LAB-020 | Chest X-ray | Pneumonia criterion: new infiltrate (DG-04) |
| LAB-022 | CT head, non-contrast | Stroke-code target: door to CT start within 20 minutes (FPA-07) |
| LAB-027 | CT pulmonary angiogram | Confirms pulmonary embolism after elevated D-dimer (DG-06) |

### 4.7 Pulmonary function (report doc LD-08)

| ID | Test | Reference |
|---|---|---|
| LAB-019 | Spirometry | FEV1/FVC 0.70 or higher; FEV1 80% of predicted or higher; bronchodilator reversibility under 12% and 200 mL |

## 5. Turnaround Targets (MediCore Policy, urgent samples)

| Test group | Target from receipt to verification |
|---|---|
| hs-troponin, potassium, BMP, lactate, CBC, INR | 45 minutes |
| Blood gas | 15 minutes |
| Procalcitonin, CRP, ferritin, TSH, HbA1c | 4 hours |
| Blood culture Gram stain | Immediately on bottle positivity |
| Culture identification / susceptibility | 24 to 72 hours after positivity |
| C. difficile toxin/PCR | Within 12 hours of receipt |
| Imaging read | Stroke CT within 10 minutes of scan; others within 60 minutes (urgent) |

## 6. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Critical result and labeling protocols | HO-05 |
| Diagnostic criteria by disease | DG-01 to DG-07; LD-08 crosswalk |
| Patient report series | LD-02 to LD-08 |

## 7. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic catalog (Pass 1) |
