---
doc_id: LD-04
title: "Cardiac, Sepsis and Blood Gas Reports"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-003, PAT-004, PAT-008, PAT-011, PAT-012, PAT-013, LAB-007, LAB-008, LAB-014, LAB-015, LAB-016, LAB-018, PRO-004, PRO-006, PRO-009, DEP-011, STF-012, FPA-02, FPA-08, FPA-13]
related_docs: [DG-01, DG-02, DG-04, DG-05, HO-03, HO-04, HO-05, LD-01, PR-01, PR-02, PR-03, PR-04, PR-07, PR-08]
---

# LD-04: Cardiac, Sepsis and Blood Gas Reports

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every patient, value, and report number in this document are fictional. The reports exist only for software benchmarking and education and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-04 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Performing department | Clinical Laboratory (DEP-011); verified under STF-012 |
| Tests | LAB-007 hs-troponin, LAB-008 NT-proBNP, LAB-014 lactate, LAB-015 procalcitonin, LAB-016 CRP, LAB-018 arterial blood gas |
| Reference ranges and critical values | LD-01: hs-troponin 99th percentile 14 ng/L, critical 100 ng/L or higher; lactate critical 4.0 mmol/L or higher (PRO-009, FPA-13: call within 20 minutes of verification) |
| Related documents | PR-01, PR-02, PR-03, PR-04, PR-07, PR-08; DG-01, DG-04, DG-05; HO-03, HO-05 |

## 2. Purpose and Scope

Report series for six patients. PRO-009 tests in this document: LAB-007 and LAB-014. NT-proBNP, procalcitonin, CRP and blood gases are flagged but not telephoned.

## 3. hs-Troponin Series (LAB-007)

Chest-pain pathway rule: draws at 0 and 2 hours, ECG within 10 minutes of arrival (FPA-08, PRO-006).

### 3.1 PAT-002, NSTEMI, 2025-03-03

| Report | Collected | Verified | Result | Interval and call | Flag |
|---|---|---|---|---|---|
| RPT-LD04-001 | 2025-03-03 21:40 (0 hour) | 22:08 (28 min turnaround) | **48 ng/L** | Below critical; not telephoned | H |
| RPT-LD04-002 | 2025-03-03 23:42 (2 h 02 min after 0 hour) | 2025-03-04 00:10 (28 min) | **112 ng/L** | **Critical; phoned 00:20, 10 minutes after verification** | **C** |

Delta: +64 ng/L in 2 hours, consistent with NSTEMI (DG-01, PR-02).

### 3.2 PAT-008, NSTEMI, 2026-02-03

| Report | Collected | Verified | Result | Interval and call | Flag |
|---|---|---|---|---|---|
| RPT-LD04-003 | 2026-02-03 07:58 (0 hour) | 08:28 (30 min) | **62 ng/L** | Below critical; not telephoned | H |
| RPT-LD04-004 | 2026-02-03 10:02 (2 h 04 min after 0 hour) | 10:18 (16 min) | **155 ng/L** | **Critical; phoned 10:26, 8 minutes after verification** | **C** |

Delta: +93 ng/L in about 2 hours (DG-01, PR-07).

## 4. NT-proBNP Series (LAB-008)

PAT-001, man, 67 years (age band 50 to 75: HFrEF supported above 900 pg/mL, DG-01).

| Report | Date | NT-proBNP pg/mL | Flag |
|---|---|---|---|
| RPT-LD04-005 | 2024-02-12 | **1,850** | H |
| RPT-LD04-006 | 2024-11-05 | **1,120** | H |
| RPT-LD04-007 | 2026-04-08 | **940** | H |

PAT-011 values (4,820 and 5,300 pg/mL) are held inline in PR-08.

## 5. Sepsis Markers (LAB-014, LAB-015, LAB-016)

### 5.1 PAT-003, sepsis from pneumonia, 2026-02-26 to 2026-03-05

| Report | Collected | Verified | Test | Result | Flag |
|---|---|---|---|---|---|
| RPT-LD04-008 | 2026-02-26 10:20 | 10:42 | Lactate | **3.4 mmol/L** | H (below critical 4.0) |
| RPT-LD04-009 | 2026-02-26 12:05 | 12:30 | Lactate (repeat, 1 h 45 min after the first) | **2.1 mmol/L** | H |
| RPT-LD04-010 | 2026-02-26 | | Procalcitonin **12.6 ng/mL**; CRP **214 mg/L** | | H |
| RPT-LD04-011 | 2026-02-28 | | CRP **162 mg/L** | | H |
| RPT-LD04-012 | 2026-03-01 | | Procalcitonin **3.1 ng/mL**; CRP **88 mg/L** | | H |
| RPT-LD04-013 | 2026-03-05 | | CRP **31 mg/L** | | H |

The repeat lactate fell within the 2-hour repeat rule of PRO-004 (HO-03).

### 5.2 PAT-012, non-severe pneumonia

| Report | Date | Test | Result | Flag |
|---|---|---|---|---|
| RPT-LD04-014 | 2026-05-05 | Procalcitonin **0.42 ng/mL**; CRP **96 mg/L** | Above 0.25 | H |
| RPT-LD04-015 | 2026-05-07 | Procalcitonin **0.18 ng/mL** | Below the 0.25 stewardship stop value (HO-04) | |

PAT-013 lactate (3.0 and 1.7 mmol/L, 2026-06-18) is held inline in PR-08.

## 6. Arterial Blood Gases (LAB-018)

| Report | Collected | Patient | Result | Interpretation |
|---|---|---|---|---|
| RPT-LD04-016 | 2026-02-26 09:40, room air | PAT-003 | pH **7.28**; PaCO2 **8.3 kPa (62 mmHg)**; PaO2 **7.7 kPa (58 mmHg)**; bicarbonate 29 mmol/L | Acute-on-chronic hypercapnic respiratory acidosis; meets DG-04 criteria for non-invasive ventilation (pH below 7.35 with PaCO2 above 6.0 kPa) |
| RPT-LD04-017 | 2025-12-09 19:30 | PAT-004 | pH **7.18**; PaCO2 **2.4 kPa (18 mmHg)**; PaO2 13.0 kPa; bicarbonate **9 mmol/L** | Metabolic acidosis with respiratory compensation; moderate DKA by pH (DG-02) |

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Reference ranges, critical values | LD-01 |
| Chest-pain pathway timing | HO-03 (PRO-006, FPA-08) |
| Sepsis bundle and repeat lactate | HO-03 (PRO-004, FPA-02) |
| Critical result notification | HO-05 |
| ACS and HFrEF criteria | DG-01 |
| Pneumonia and COPD | DG-04 |
| Sepsis and procalcitonin | DG-05 |
| Patient charts | PR-01, PR-02, PR-03, PR-04, PR-07, PR-08 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic report series (Pass 1) |
