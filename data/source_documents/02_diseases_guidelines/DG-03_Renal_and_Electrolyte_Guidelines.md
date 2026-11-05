---
doc_id: DG-03
title: "Renal and Electrolyte Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-009, PAT-011, PAT-013, DIS-003, DIS-017, DIS-019, MED-001, MED-003, MED-004, MED-007, MED-008, MED-026, MED-027, LAB-004, LAB-005, LAB-021, PRO-008, PRO-009, DEP-005, STF-007, INC-002, FPA-01]
related_docs: [DG-01, DG-02, HO-02, HO-05, HO-08, LD-01, LD-03, MP-01, MP-02, MP-04, MP-05, MP-06, MP-07, PR-01, PR-07, PR-08]
---

# DG-03: Renal and Electrolyte Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-03 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Chronic kidney disease (DIS-003), acute kidney injury (DIS-017), hyperkalemia (DIS-019) |
| Owner | Nephrology (DEP-005, head STF-007), approved by the CPRB |
| Companion documents | MP-01, MP-05, MP-06, MP-07, LD-01, LD-03, HO-02, HO-05 |

## 2. Purpose and Scope

This guideline defines kidney-function staging, acute kidney injury staging, nephrotoxin avoidance, and the hyperkalemia algorithm. It is the clinical basis for renal dose adjustment (PRO-008, HO-02) and critical potassium calling (PRO-009, HO-05). Charts applying it: PR-01, PR-07 (PAT-009), PR-08 (PAT-011, PAT-013).

## 3. Chronic Kidney Disease (DIS-003)

### 3.1 Definition and staging
CKD is present when eGFR (LAB-004) is below 60 mL/min/1.73 m2 for at least 3 months, or when markers of kidney damage persist for 3 months.

| Stage | eGFR (mL/min/1.73 m2) |
|---|---|
| G1 | 90 or higher (with kidney damage) |
| G2 | 60 to 89 (with kidney damage) |
| G3a | 45 to 59 |
| **G3b** | **30 to 44** |
| G4 | 15 to 29 |
| G5 | below 15 |

PAT-001 (eGFR 38 to 44) and PAT-009 (baseline eGFR 40) are stage G3b.

### 3.2 Drug and dose consequences
- **Metformin (MED-001):** maximum 1,000 mg/day at eGFR 30 to 44; stop below 30 (also in DG-02, MP-02; protocol PRO-008).
- **NSAIDs including ibuprofen (MED-026):** avoid in CKD (MP-05). Acetaminophen (MED-027) is the preferred analgesic.
- **ACE inhibitor (MED-004) and spironolactone (MED-008):** permitted with monitoring; check potassium and creatinine at 1 week and 4 weeks after starting or increasing (DG-01).
- **Other agents:** renal tiers for MED-004, 007, 008, 012, 015, 018, 019, 020 and 030 are tabulated in MP-07.

### 3.3 Monitoring
Review eGFR at least every 6 months in G3b, and after any acute illness. Counsel patients to avoid potassium-based salt substitutes when taking an ACE inhibitor or spironolactone (PR-01).

## 4. Acute Kidney Injury (DIS-017)

### 4.1 Definition
AKI is diagnosed by any of: serum creatinine rise of 26.5 umol/L (0.3 mg/dL) or more within 48 hours; creatinine at least 1.5 times baseline within 7 days; or urine output below 0.5 mL/kg/hour for 6 hours.

### 4.2 Staging by creatinine

| Stage | Creatinine criterion |
|---|---|
| Stage 1 | 1.5 to 1.9 times baseline, or a rise of 26.5 umol/L (0.3 mg/dL) or more |
| **Stage 2** | **2.0 to 2.9 times baseline** |
| Stage 3 | 3.0 times baseline or more, or creatinine 354 umol/L (4.0 mg/dL) or more, or renal replacement therapy |

Worked examples: PAT-009 baseline 1.3 mg/dL, peak 2.9 mg/dL = 2.2 times, stage 2 (PR-07); PAT-013 baseline 1.0 mg/dL, peak 2.3 mg/dL = 2.3 times, stage 2 (PR-08).

### 4.3 Causes and nephrotoxin avoidance
Evaluate prerenal causes (volume depletion), renal causes (nephrotoxins, sepsis), and post-renal obstruction. Key nephrotoxin hazards in this dataset:
- **NSAIDs with an ACE inhibitor and a diuretic**, the "triple combination," in a patient with CKD (PAT-009).
- **Vancomycin with piperacillin-tazobactam** (MP-06, MP-04), requiring pharmacy-managed dosing and early level checks (PAT-013).
- Dehydration during infection, with diuretics and ACE inhibitors continued.

### 4.4 Management
Stop or hold nephrotoxic and renally cleared drugs (ibuprofen, lisinopril, furosemide, metformin as applicable); restore volume; treat infection; relieve obstruction; recheck creatinine daily; adjust drug doses to current eGFR using MP-07. Resume ACE inhibitor and diuretic only after creatinine plateaus and oral intake is normal (PAT-009 resumed on 2026-03-31).

## 5. Hyperkalemia (DIS-019)

### 5.1 Reference guideline severity classes

| Class | Potassium (LAB-005) |
|---|---|
| Mild | 5.5 to 5.9 mmol/L |
| Moderate | 6.0 to 6.4 mmol/L |
| Severe | 6.5 mmol/L or higher |

**Distinction from MediCore Policy:** the laboratory *critical value* that triggers an urgent telephone call is set separately by MediCore Policy at **6.2 mmol/L or higher or 2.9 mmol/L or lower** (FPA-01; HO-05). The two systems are intentionally different: a result of 6.4 mmol/L is "moderate" in this guideline and "critical" under MediCore Policy.

### 5.2 Algorithm
1. Obtain a 12-lead ECG (LAB-021) and repeat the sample if hemolysis is suspected.
2. If ECG changes (peaked T waves, prolonged PR or QRS) or potassium is 6.2 mmol/L or higher: give IV calcium for membrane stabilization.
3. Shift potassium into cells: insulin regular 10 units IV with 25 g dextrose (MED-003).
4. Remove the cause: stop or hold spironolactone (MED-008) and the ACE inhibitor (MED-004); stop potassium supplements and salt substitutes; continue the loop diuretic (MED-007) if the patient is not volume-depleted.
5. Recheck potassium at 1 to 2 hours and then every 4 to 6 hours until below 5.5 mmol/L.
6. Before restarting an ACE inhibitor or MRA, potassium should be below 5.0 mmol/L, with a 1-week and 4-week recheck after the restart; a restart at a reduced dose is acceptable.

### 5.3 Application
PAT-001 presented on 2025-09-17 with potassium 6.4 mmol/L and ECG changes after three days of vomiting and diarrhea during which the sick-day rule (DG-01) was not followed (PR-01). Spironolactone, lisinopril, furosemide and metformin were held; lisinopril restarted at 5 mg on 2025-09-26 and spironolactone resumed at 12.5 mg on 2025-10-23 with 1-week and 4-week potassium checks. The telephone-notification delay for the result produced INC-002 (HO-08).

## 6. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-001 | CKD G3b, hyperkalemia | PR-01 |
| PAT-009 | CKD G3b, AKI stage 2 after NSAID | PR-07 |
| PAT-011 | HF with kidney function monitoring | PR-08 |
| PAT-013 | Urosepsis with AKI stage 2 | PR-08 |

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| ACE inhibitor, spironolactone, furosemide monographs | MP-01 |
| Ibuprofen and acetaminophen monographs | MP-05 |
| Interaction severities | MP-06 |
| Renal dosing tiers | MP-07 |
| Creatinine/eGFR and potassium reports; reference ranges | LD-03, LD-01 |
| Renal dose adjustment protocol | HO-02 |
| Critical results notification | HO-05 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
