---
doc_id: LD-03
title: "Chemistry and Metabolic Reports"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-004, PAT-006, PAT-009, PAT-012, PAT-013, PAT-014, LAB-002, LAB-003, LAB-004, LAB-005, LAB-006, LAB-009, LAB-017, LAB-028, PRO-008, PRO-009, DEP-011, STF-012, INC-002, INC-005, FPA-01, FPA-12, FPA-13]
related_docs: [DG-02, DG-03, HO-02, HO-05, HO-08, LD-01, LD-04, MP-01, MP-02, MP-07, PR-01, PR-04, PR-06, PR-07, PR-08]
---

# LD-03: Chemistry and Metabolic Reports

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every patient, value, and report number in this document are fictional. The reports exist only for software benchmarking and education and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-03 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Performing department | Clinical Laboratory (DEP-011); verified under STF-012 |
| Tests | LAB-002 BMP, LAB-003 HbA1c, LAB-004 creatinine and eGFR, LAB-005 potassium, LAB-006 sodium, LAB-009 lipid panel, LAB-017 TSH, LAB-028 glucose and beta-hydroxybutyrate |
| Reference ranges | LD-01 (authoritative); critical potassium is 6.2 mmol/L or higher or 2.9 or lower (FPA-01) |
| Related documents | PR-01, PR-04, PR-06, PR-07, PR-08; DG-02, DG-03; MP-01, MP-02; HO-05 |

## 2. Purpose and Scope

Report series for five patients. Creatinine is given in umol/L with mg/dL in parentheses (1 mg/dL = 88.4 umol/L); eGFR in mL/min/1.73 m2. No patient in this set had a lipid panel (LAB-009) ordered; the test is defined in LD-01 for completeness. The only PRO-009 test in this document is LAB-005.

## 3. PAT-001 (Marcus E. Doyle), man, 67 years

### 3.1 Longitudinal series

| Report | Date | HbA1c % | K mmol/L | Creatinine umol/L | eGFR | Comment |
|---|---|---|---|---|---|---|
| RPT-LD03-001 | 2024-01-18 | 8.1 | 4.7 | 142 (1.61) | 49 | Stage G3a at the time |
| RPT-LD03-002 | 2024-06-11 | n/a | 4.9 | 146 (1.65) | 48 | One-week safety check after spironolactone start |
| RPT-LD03-003 | 2024-07-10 | 7.6 | 4.8 | 146 (1.65) | 48 | |
| RPT-LD03-004 | 2024-11-05 | n/a | 4.8 | n/a | n/a | |
| RPT-LD03-005 | 2025-02-20 | 7.4 | 4.9 | **158 (1.79)** | **44** | Meets the metformin cap band (eGFR 30 to 44) |
| RPT-LD03-006 | 2025-05-14 | n/a | 4.8 | 160 (1.81) | 43 | |
| RPT-LD03-007 | 2025-09-26 | n/a | 4.8 | 158 | 44 | Post-admission |
| RPT-LD03-008 | 2025-10-23 | n/a | 4.7 | 164 | 42 | |
| RPT-LD03-009 | 2025-11-20 | n/a | 4.8 | n/a | n/a | Four-week potassium check |
| RPT-LD03-010 | 2026-04-08 | 7.1 | 4.6 | 170 | 39 | |
| RPT-LD03-011 | 2026-09-02 | 7.0 | 4.7 | 168 | 40 | |

### 3.2 Hyperkalemia admission, 2025-09-17 to 2025-09-20 (INC-002)

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD03-012 | 2025-09-17 07:42 | **08:05** | BMP: **potassium 6.4 mmol/L**; creatinine **176 umol/L (1.99 mg/dL)**; eGFR **38**; sodium **134 mmol/L** | K above 6.2 | **C** (phoned **08:41**, 36 minutes after verification; policy 20 minutes, FPA-13) |
| RPT-LD03-013 | 2025-09-17 10:15 | 10:48 | Potassium 5.6 mmol/L | High | H |
| RPT-LD03-014 | 2025-09-17 13:00 | 13:34 | Potassium 5.3 mmol/L | High | H |
| RPT-LD03-015 | 2025-09-18 06:00 | 06:40 | Potassium 5.1; creatinine 168 umol/L; eGFR 40 | | H |
| RPT-LD03-016 | 2025-09-19 06:00 | 06:38 | Potassium 4.9; creatinine 164; eGFR 41 | In range | |
| RPT-LD03-017 | 2025-09-20 06:00 | 06:37 | Potassium 4.8; creatinine 163; eGFR 41 | In range | |

The critical call for RPT-LD03-012 and its delay are the facts of INC-002 (PR-01, HO-05, HO-08).

## 4. PAT-004 (Elena Voss), woman, 54 years

| Report | Collected | Test | Result | Flag |
|---|---|---|---|---|
| RPT-LD03-018 | 2024-09-10 | HbA1c 8.4%; K 4.2; eGFR 90 | Diabetes, above target | H |
| RPT-LD03-019 | 2025-03-12 | HbA1c 7.5%; K 4.3; eGFR 89 | | H |
| RPT-LD03-020 | 2025-12-09 19:30 | BMP: sodium 137; **potassium 3.3 mmol/L**; bicarbonate **9 mmol/L**; creatinine 0.8 mg/dL (71 umol/L); eGFR 88; **anion gap 24**; glucose **11.8 mmol/L (212 mg/dL)**; HbA1c **7.6%** | Low K, low bicarbonate, high gap | L, H |
| RPT-LD03-021 | 2025-12-09 20:00 | Beta-hydroxybutyrate **5.4 mmol/L** | DKA range (3.0 or higher) | H |
| RPT-LD03-022 | 2025-12-09 21:00 | BHB **4.8** | | H |
| RPT-LD03-023 | 2025-12-09 23:00 | BHB **3.9** | | H |
| RPT-LD03-024 | 2025-12-10 02:00 | BHB **2.6** | | H |
| RPT-LD03-025 | 2025-12-10 03:20 | Capillary glucose **3.8 mmol/L (68 mg/dL)** | Below 4.0 alert (FPA-12) | L |
| RPT-LD03-026 | 2025-12-10 04:20 | Capillary glucose 6.2 mmol/L | After dextrose | |
| RPT-LD03-027 | 2025-12-10 06:00 | BHB **1.5**; potassium 3.9 | | H |
| RPT-LD03-028 | 2025-12-10 10:00 | BHB **0.9** | | H |
| RPT-LD03-029 | 2025-12-10 14:00 | BHB **0.5** | First value below 0.6 | |
| RPT-LD03-030 | 2025-12-10 16:00 | BHB **0.4**; glucose 7.1 mmol/L; potassium 4.0 | **Second consecutive value below 0.6; transition criterion met** (FPA-12) | |
| RPT-LD03-031 | 2025-12-10 | TSH (LAB-017) **4.1 mIU/L** | Upper reference limit 4.0; acute illness | H |
| RPT-LD03-032 | 2025-12-30 | HbA1c 7.6%; K 4.4; eGFR 87 | | H |
| RPT-LD03-033 | 2026-03-18 | HbA1c 7.2%; K 4.3; eGFR 88; TSH **3.8 mIU/L** | TSH in range | |
| RPT-LD03-034 | 2026-09-09 | HbA1c 7.0%; K 4.4; eGFR 87 | | |

The arterial blood gas of 2025-12-09 (pH 7.18) is reported in LD-04.

## 5. PAT-006 (Grace Lindqvist-Obi), woman, 63 years

| Report | Collected | Test | Result |
|---|---|---|---|
| RPT-LD03-035 | 2025-08-29 | Creatinine 80 umol/L (0.9 mg/dL); **eGFR 74** | Within range; no renal dose adjustment for enoxaparin (PRO-008, MP-07) |

## 6. PAT-009 (Lucia Fernandes-Adler), woman, 81 years (INC-005)

| Report | Date | Creatinine umol/L (mg/dL) | eGFR | Comment |
|---|---|---|---|---|
| RPT-LD03-036 | 2026-03-05 | 115 (1.3) | 40 | Baseline; ibuprofen prescribed that day |
| RPT-LD03-037 | 2026-03-22 | 230 (2.6) | 17 | Admission |
| RPT-LD03-038 | 2026-03-23 | **256 (2.9)** | **15** | Peak; 2.2 times baseline, AKI stage 2 (DG-03) |
| RPT-LD03-039 | 2026-03-24 | 212 (2.4) | 19 | |
| RPT-LD03-040 | 2026-03-25 | 168 (1.9) | 26 | |
| RPT-LD03-041 | 2026-03-27 | 141 (1.6) | 32 | |
| RPT-LD03-042 | 2026-03-28 | 133 (1.5) | 34 | Discharge |
| RPT-LD03-043 | 2026-04-14 | 124 (1.4) | 37 | New baseline |

## 7. PAT-013 (Daniel Oyelaran-Whitfield), man, 66 years

| Report | Date | Creatinine umol/L (mg/dL) | eGFR | Comment |
|---|---|---|---|---|
| RPT-LD03-044 | 2025-11 (baseline) | 88 (1.0) | 79 | |
| RPT-LD03-045 | 2026-06-18 | 168 (1.9) | 38 | Admission with urosepsis |
| RPT-LD03-046 | 2026-06-19 | **203 (2.3)** | **30** | Peak; 2.3 times baseline, AKI stage 2; piperacillin-tazobactam reduced (MP-07) |
| RPT-LD03-047 | 2026-06-20 | 159 (1.8) | 40 | |
| RPT-LD03-048 | 2026-06-22 | 115 (1.3) | 59 | |

## 8. Other Patients (chemistry values held inline in charts)

PAT-012 (PR-08): HbA1c 7.4%, eGFR 82 (2026-05-05). PAT-014 (PR-08): TSH 2.4, 8.9 and 3.2 mIU/L (2026-03-30, 2026-05-12, 2026-07-14). They are not reproduced as report entries here.

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Reference ranges; critical potassium | LD-01, HO-05 |
| CKD, AKI and hyperkalemia criteria | DG-03 |
| Diabetes, DKA and TSH rules | DG-02 |
| Renal dosing | MP-07, HO-02 |
| Blood gases | LD-04 |
| Patient charts | PR-01, PR-04, PR-06, PR-07, PR-08 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic report series (Pass 1) |
