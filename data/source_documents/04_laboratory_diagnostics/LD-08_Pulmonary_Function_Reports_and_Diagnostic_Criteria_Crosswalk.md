---
doc_id: LD-08
title: "Pulmonary Function Reports and Diagnostic Criteria Crosswalk"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, PAT-007, DIS-001, DIS-002, DIS-003, DIS-004, DIS-005, DIS-006, DIS-007, DIS-008, DIS-009, DIS-010, DIS-011, DIS-012, DIS-013, DIS-014, DIS-015, DIS-016, DIS-017, DIS-018, DIS-019, DIS-020, DIS-021, DIS-022, DIS-023, DIS-024, LAB-001, LAB-002, LAB-003, LAB-004, LAB-005, LAB-007, LAB-008, LAB-009, LAB-010, LAB-012, LAB-013, LAB-014, LAB-015, LAB-016, LAB-017, LAB-018, LAB-019, LAB-020, LAB-021, LAB-022, LAB-023, LAB-024, LAB-025, LAB-026, LAB-027, LAB-028, DEP-006, DEP-011, STF-008, FPA-01]
related_docs: [DG-01, DG-02, DG-03, DG-04, DG-05, DG-06, DG-07, DG-08, LD-01, PR-03, PR-07]
---

# LD-08: Pulmonary Function Reports and Diagnostic Criteria Crosswalk

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every patient, value, criterion, and report number in this document are fictional. The content exists only for software benchmarking and education and must not be used for clinical decisions. Criteria are mirrored from the fictional guidelines DG-01 to DG-08 and may differ from real-world practice.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-08 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Performing department | Pulmonology (DEP-006, head STF-008) with Clinical Laboratory (DEP-011) |
| Tests | LAB-019 spirometry (reports); crosswalk covers LAB-001 to LAB-028 |
| Related documents | PR-03, PR-07; DG-01 to DG-08; LD-01 |

## 2. Purpose and Scope

Part A holds the two spirometry reports in the dataset. Part B maps every disease DIS-001 to DIS-024 to the tests and thresholds that define it. **The crosswalk repeats the values stated in the guideline documents; if a guideline changes, this table must be updated at the same time.**

## 3. Part A: Spirometry Reports (LAB-019)

### 3.1 PAT-003 (Thomas Okonkwo-Reyes), 2024-11-20

| Report | Parameter | Result |
|---|---|---|
| RPT-LD08-001 | Pre-bronchodilator FEV1 | 1.44 L |
| | **Post-bronchodilator FEV1** | **1.52 L = 48% of predicted** (predicted 3.17 L) |
| | Post-bronchodilator FVC | 2.81 L |
| | **Post-bronchodilator FEV1/FVC** | **0.54** |
| | Bronchodilator response | +80 mL (+5.6%): not significant |
| | Interpretation | **Severe airflow obstruction** (FEV1 30 to 49%); FEV1/FVC below 0.70 confirms COPD (DG-04) |

### 3.2 PAT-007 (Hannah Whitcombe-Rao), 2026-06-23

| Report | Parameter | Result |
|---|---|---|
| RPT-LD08-002 | Pre-bronchodilator FEV1 | 2.23 L |
| | **Post-bronchodilator FEV1** | **2.54 L = 82% of predicted** (predicted 3.10 L) |
| | Post-bronchodilator FVC | 3.26 L |
| | **Post-bronchodilator FEV1/FVC** | **0.78** |
| | **Bronchodilator reversibility** | **+310 mL (+14%)**; criterion 12% and 200 mL met |
| | Interpretation | No fixed obstruction; significant reversibility supports asthma (DG-04) |

## 4. Part B: Diagnostic Criteria Crosswalk

| Disease | Tests (LAB) | Criterion (mirrors the guideline) | Guideline |
|---|---|---|---|
| DIS-001 Type 2 diabetes | LAB-003, LAB-028 | HbA1c 6.5% or higher, or fasting glucose 7.0 mmol/L or higher | DG-02 |
| DIS-002 Hypertension | None (clinic blood pressure) | 140/90 mmHg or higher on two visits; target below 130/80 with diabetes, CKD or vascular disease | DG-01 |
| DIS-003 CKD | LAB-004 | eGFR below 60 for at least 3 months; G3b = 30 to 44; G4 = 15 to 29; G5 below 15 | DG-03 |
| DIS-004 HFrEF | LAB-023, LAB-008 | LVEF 40% or lower; NT-proBNP above 450 (under 50), 900 (50 to 75), 1,800 (over 75) pg/mL | DG-01 |
| DIS-005 Atrial fibrillation | LAB-021 | Irregular rhythm without P waves for at least 30 seconds | DG-01 |
| DIS-006 ACS (NSTEMI) | LAB-007, LAB-021 | hs-troponin rise and/or fall above the 99th percentile (14 ng/L) with ischemic symptoms or ECG change | DG-01 |
| DIS-007 COPD | LAB-019 | Post-bronchodilator FEV1/FVC below 0.70; severe = FEV1 30 to 49% of predicted | DG-04 |
| DIS-008 Pneumonia | LAB-020, LAB-015, LAB-016 | New infiltrate on chest X-ray with clinical features; procalcitonin and CRP supportive | DG-04 |
| DIS-009 Sepsis | LAB-014, LAB-012, LAB-015 | Suspected infection with organ dysfunction; lactate above 2.0 mmol/L as a trigger; cultures before antibiotics | DG-05 |
| DIS-010 Complicated UTI | LAB-013 | Urinalysis and culture (10^5 CFU/mL or more) with fever, obstruction or other complicating features | DG-05 |
| DIS-011 Ischemic stroke | LAB-022 | Clinical deficit with CT excluding hemorrhage; severity by NIHSS | DG-06 |
| DIS-012 VTE | LAB-026, LAB-027 | D-dimer 500 ng/mL FEU or higher then CTPA confirmation | DG-06 |
| DIS-013 DKA | LAB-028, LAB-018, LAB-002 | Beta-hydroxybutyrate 3.0 mmol/L or higher with pH below 7.30 or bicarbonate below 18; euglycemic variant glucose below 14 mmol/L; resolution below 0.6 | DG-02 |
| DIS-014 Hyperlipidemia | LAB-009 | LDL-C targets: below 1.4 (established disease), below 1.8 (high risk), below 2.6 mmol/L (moderate risk) | DG-02 |
| DIS-015 Asthma | LAB-019 | FEV1 improvement of 12% and 200 mL or more after bronchodilator | DG-04 |
| DIS-016 Hypothyroidism | LAB-017 | TSH above 4.0 mIU/L (reference 0.4 to 4.0) with low or low-normal free thyroxine | DG-02 |
| DIS-017 AKI | LAB-004 | Creatinine rise of 26.5 umol/L within 48 hours or 1.5 times baseline; stage 2 = 2.0 to 2.9 times baseline | DG-03 |
| DIS-018 Iron-deficiency anemia | LAB-001, LAB-025 | Hemoglobin below 12.0 g/dL (women) or 13.0 (men) and ferritin below 15 ng/mL | DG-07 |
| DIS-019 Hyperkalemia | LAB-005, LAB-021 | Mild 5.5 to 5.9, moderate 6.0 to 6.4, severe 6.5 mmol/L or higher; MediCore critical 6.2 or higher (FPA-01) | DG-03 |
| DIS-020 Major depressive disorder | None | PHQ-9 score of 10 or higher with symptoms for 2 weeks | DG-08 |
| DIS-021 Osteoarthritis | None | Clinical diagnosis | DG-08 |
| DIS-022 Upper GI bleeding | LAB-001, LAB-010, LAB-025 | Melena or hematemesis; transfuse below 7 g/dL (below 8 with cardiovascular disease) | DG-07 |
| DIS-023 C. difficile infection | LAB-024 | Positive toxin/PCR with 3 or more unformed stools in 24 hours | DG-05 |
| DIS-024 Anaphylaxis | None | Skin or mucosal involvement with respiratory compromise or hypotension after exposure | DG-07 |

## 5. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Reference ranges | LD-01 |
| Guidelines | DG-01 to DG-08 |
| Patient charts | PR-03 (PAT-003), PR-07 (PAT-007) |

## 6. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic report and crosswalk (Pass 1) |
