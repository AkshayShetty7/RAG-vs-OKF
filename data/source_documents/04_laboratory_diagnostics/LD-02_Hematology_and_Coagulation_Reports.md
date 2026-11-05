---
doc_id: LD-02
title: "Hematology and Coagulation Reports"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, PAT-005, PAT-006, PAT-010, PAT-011, PAT-014, LAB-001, LAB-010, LAB-011, LAB-025, LAB-026, PRO-009, DEP-011, STF-012, INC-003, INC-006, FPA-05]
related_docs: [DG-06, DG-07, HO-04, HO-08, LD-01, MP-03, MP-06, PR-02, PR-05, PR-06, PR-07, PR-08]
---

# LD-02: Hematology and Coagulation Reports

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every patient, value, and report number in this document are fictional. The reports exist only for software benchmarking and education and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-02 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Performing department | Clinical Laboratory (DEP-011); verified under STF-012 |
| Tests | LAB-001 CBC, LAB-010 PT/INR, LAB-011 aPTT, LAB-025 ferritin and iron studies, LAB-026 D-dimer |
| Reference ranges | LD-01 (authoritative); abnormal flags: H high, L low, C critical (PRO-009) |
| Related documents | PR-02, PR-05, PR-06, PR-08 (patient charts); DG-06, DG-07; MP-03; HO-04 |

## 2. Purpose and Scope

This document holds the laboratory report series for five patients. Values must match the patient charts. The only PRO-009 test in this document is **LAB-010 (INR critical at 5.0 or higher)**; hemoglobin and ferritin results are flagged but not telephoned.

## 3. PAT-002 (Priya Nandakumar), woman, 72 years

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD02-001 | 2025-03-03 21:40 | 22:05 | CBC: Hb 12.6 g/dL; MCV 88 fL; platelets 241 | Within range | |
| RPT-LD02-002 | 2025-04-15 | 2025-04-15 | CBC: Hb **12.3 g/dL** (baseline); MCV 87 | Within range | |
| RPT-LD02-003 | 2025-05-19 08:10 | 08:48 | CBC: Hb **8.4 g/dL**; MCV 82; platelets 268. INR (LAB-010) **1.1** | Hb low | L |
| RPT-LD02-004 | 2025-05-20 06:00 | 06:38 | CBC: Hb **7.6 g/dL** (nadir) | Low | L |
| RPT-LD02-005 | 2025-05-21 | 2025-05-21 | CBC: Hb **9.1 g/dL** after two units red cells. Ferritin (LAB-025) **9 ng/mL**; transferrin saturation **6%**; MCV 76 | Iron deficiency by DG-07 criteria | L |
| RPT-LD02-006 | 2025-05-23 | 2025-05-23 | CBC: Hb 9.2 g/dL (stable 48 hours) | Low | L |
| RPT-LD02-007 | 2025-05-24 | 2025-05-24 | CBC: Hb 9.4 g/dL | Low | L |
| RPT-LD02-008 | 2025-07-10 | 2025-07-10 | CBC: Hb 11.2 g/dL. Ferritin **31 ng/mL** | Hb low; ferritin normal | L |
| RPT-LD02-009 | 2025-09-04 | 2025-09-04 | CBC: Hb 12.0 g/dL | Within range | |
| RPT-LD02-010 | 2026-08-20 | 2026-08-20 | CBC: Hb 12.4 g/dL. Ferritin 64 ng/mL | Within range | |

Interpretation: iron-deficiency anemia after upper GI bleeding on apixaban and clopidogrel, recovered after transfusion, endoscopic therapy and oral iron (PR-02, DG-07).

## 4. PAT-005 (Samuel Adeyemi-Clarke), man, 76 years

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD02-011 | 2026-04-14 19:05 | 19:40 | CBC: Hb **14.1 g/dL**; platelets **232 x10^9/L**; MCV 91. INR (LAB-010) **1.0** | Within range | |
| RPT-LD02-012 | 2026-05-20 | 2026-05-20 | CBC: Hb 13.8 g/dL | Within range | |

Interpretation: baseline before anticoagulation after ischemic stroke; no coagulopathy (PR-05, DG-06).

## 5. PAT-006 (Grace Lindqvist-Obi), woman, 63 years

### 5.1 Pulmonary embolism work-up and anticoagulation, 2025-08-29 to 2025-09-07

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD02-013 | 2025-08-29 13:10 | 13:52 | D-dimer (LAB-026): **3,850 ng/mL FEU**. INR 1.0. aPTT (baseline) 31 s | D-dimer high | H |
| RPT-LD02-014 | 2025-08-29 22:10 | 22:44 | aPTT (LAB-011) **72 s** at 6 hours of heparin | Therapeutic (60 to 80) | |
| RPT-LD02-015 | 2025-08-30 06:00 | 06:35 | aPTT 68 s | Therapeutic | |
| RPT-LD02-016 | 2025-08-31 06:00 | 06:36 | aPTT 74 s | Therapeutic | |
| RPT-LD02-017 | 2025-09-01 06:00 | 06:34 | aPTT 66 s | Therapeutic | |
| RPT-LD02-018 | 2025-09-02 | 2025-09-02 | INR **1.6** | | |
| RPT-LD02-019 | 2025-09-04 | 2025-09-04 | INR **1.9** | | |
| RPT-LD02-020 | 2025-09-06 | 2025-09-06 | INR **2.3** | | |
| RPT-LD02-021 | 2025-09-07 | 2025-09-07 | INR **2.6** | In target 2.0 to 3.0 | |

Interpretation: INR 2.3 and 2.6 on consecutive checks at or above 2.0 allowed enoxaparin to stop on 2025-09-07 (DG-06, HO-04). Parenteral anticoagulation lasted 10 days.

### 5.2 INR during the ciprofloxacin interaction (INC-003), 2025-10-20 to 2025-10-29

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD02-022 | 2025-10-20 | 2025-10-20 | INR | **2.4** (baseline before ciprofloxacin) | |
| RPT-LD02-023 | 2025-10-26 14:50 | **15:20** | INR **6.8**; Hb 12.9 g/dL | **Critical (5.0 or higher); phoned 15:36, 16 minutes after verification** | **C** |
| RPT-LD02-024 | 2025-10-27 | 2025-10-27 | INR 4.1 | Above range | H |
| RPT-LD02-025 | 2025-10-28 | 2025-10-28 | INR 3.2 | Above range | H |
| RPT-LD02-026 | 2025-10-29 | 2025-10-29 | INR 2.6 | In target | |

Interpretation: INR rise attributed to ciprofloxacin (MP-06). The INR above 4.5 triggered the 24-hour anticoagulation-clinic call (FPA-05).

## 6. PAT-011 (Walter Brennan-Osei), man, 78 years

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD02-027 | 2026-01-12 | 2026-01-12 | INR **2.6** (admission) | In target | |
| RPT-LD02-028 | 2026-02-02 | 2026-02-02 | INR **3.4** (readmission) | Above range; below critical | H |
| RPT-LD02-029 | 2026-02-05 | 2026-02-05 | INR **2.8** (3-day recheck after dose reduction) | In target | |
| RPT-LD02-030 | 2026-02-10 | 2026-02-10 | INR **2.6** (within 72 hours of the second discharge) | In target | |

No INR was drawn within 72 hours of the first discharge (2026-01-17), the gap addressed in INC-006 (PR-08, HO-08).

## 7. PAT-014 (Ingrid Solheim-Banerjee), woman, 55 years

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD02-031 | 2026-03-30 | 2026-03-30 | CBC: Hb **9.8 g/dL**; MCV **71 fL**; ferritin **7 ng/mL** | Meets DG-07 criteria (Hb below 12.0, ferritin below 15) | L |
| RPT-LD02-032 | 2026-07-14 | 2026-07-14 | CBC: Hb **12.4 g/dL**; ferritin **38 ng/mL** | Hb within range | |
| RPT-LD02-033 | 2026-09-18 | 2026-09-18 | CBC: Hb **12.9 g/dL**; ferritin **61 ng/mL** | Within range | |

TSH for PAT-014 appears in PR-08 (inline values 2.4, 8.9, 3.2 mIU/L) and is not repeated as a separate report here.

## 8. Other Patients (hematology values held inline in charts)

PAT-010 (PR-07): Hb 14.6 g/dL (2026-01-14), 8.8 (2026-06-10), 9.6 (2026-06-14), 12.8 (2026-07-22). They are not reproduced as report entries in this document.

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Reference ranges and critical INR | LD-01 |
| Iron deficiency and GI bleed criteria | DG-07 |
| VTE diagnosis and warfarin transition | DG-06 |
| Antithrombotic monographs | MP-03 |
| Anticoagulation protocol | HO-04 |
| Patient charts | PR-02, PR-05, PR-06, PR-08 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic report series (Pass 1) |
