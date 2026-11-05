---
doc_id: LD-06
title: "ECG and Echocardiography Reports"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-005, PAT-008, PAT-011, LAB-021, LAB-023, PRO-009, DEP-003, STF-005, ALG-004, FPA-08]
related_docs: [DG-01, DG-06, HO-03, LD-01, LD-03, LD-04, MP-01, PR-01, PR-02, PR-05, PR-07, PR-08]
---

# LD-06: ECG and Echocardiography Reports

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every patient, measurement, and report number in this document are fictional. The reports exist only for software benchmarking and education and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-06 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Performing department | Cardiology (DEP-003, head STF-005) |
| Tests | LAB-021 12-lead ECG, LAB-023 transthoracic echocardiogram |
| References | LD-01 (normal intervals; LVEF categories: 55% or higher normal, 41 to 54% mildly reduced, 40% or lower reduced) |
| Related documents | PR-01, PR-02, PR-05, PR-07, PR-08; DG-01, DG-06; HO-03 |

## 2. Purpose and Scope

ECG and echocardiogram reports for five patients. ECG and echo are not PRO-009 tests. Intervals: PR normal 120 to 200 ms; QRS normal below 120 ms.

## 3. PAT-001 (Marcus E. Doyle)

| Report | Date and time | Study | Findings | Interpretation |
|---|---|---|---|---|
| RPT-LD06-001 | 2024-02-12 | ECG | Sinus rhythm 76 bpm; **QRS 108 ms** | Normal intervals |
| RPT-LD06-002 | 2024-02-12 | Echo | **LVEF 34%**; LV end-diastolic diameter 6.1 cm; mild functional mitral regurgitation | Reduced ejection fraction; supports HFrEF (DG-01) |
| RPT-LD06-003 | 2025-09-17 07:50 | ECG | **Peaked T waves; PR 224 ms; QRS 112 ms** | Changes of hyperkalemia (potassium 6.4 mmol/L, LD-03) |
| RPT-LD06-004 | 2026-09-02 | ECG | Sinus rhythm 68 bpm; QRS 108 ms | Normal intervals |
| RPT-LD06-005 | 2026-09-02 | Echo | **LVEF 38%** | Reduced; improved from 34% |

## 4. PAT-002 (Priya Nandakumar)

| Report | Date and time | Study | Findings | Interpretation |
|---|---|---|---|---|
| RPT-LD06-006 | 2023-09-12 | Monitor strip | Irregular rhythm without P waves, rate 118 | Paroxysmal atrial fibrillation (DG-01) |
| RPT-LD06-007 | 2023-10-02 | Echo | **LVEF 55%** | Normal |
| RPT-LD06-008 | 2025-03-03 21:22 | ECG | Sinus rhythm 84; **ST depression 1 mm in V4 to V6** | Ischemic changes; recorded 7 minutes after arrival at 21:15 (target 10 minutes, FPA-08) |
| RPT-LD06-009 | 2025-03-04 | Echo | **LVEF 50%**; mild apical hypokinesis | Mildly reduced |

## 5. PAT-005 (Samuel Adeyemi-Clarke)

| Report | Date and time | Study | Findings | Interpretation |
|---|---|---|---|---|
| RPT-LD06-010 | 2026-04-14 | ECG | **Atrial fibrillation, ventricular rate 112** | New atrial fibrillation found during stroke admission |
| RPT-LD06-011 | 2026-04-16 | Echo | **LVEF 55%**; left atrium moderately enlarged; no thrombus seen | Normal LVEF; atrial enlargement consistent with AF (DG-06) |

## 6. PAT-008 (Robert Chaudhary-Lowe)

| Report | Date and time | Study | Findings | Interpretation |
|---|---|---|---|---|
| RPT-LD06-012 | 2026-02-03 07:49 | ECG | **ST depression 1.5 mm in V2 to V5** | Recorded 7 minutes after arrival at 07:42; supports NSTEMI with troponin (LD-04) |
| RPT-LD06-013 | 2026-02-04 | Echo | **LVEF 48%**; mild inferior hypokinesis | Mildly reduced; below 50% supports a renin-angiotensin blocker after ACS, but ALG-004 prevents an ACE inhibitor (DG-01, MP-01) |

## 7. PAT-011 (Walter Brennan-Osei)

| Report | Date | Study | Findings | Interpretation |
|---|---|---|---|---|
| RPT-LD06-014 | 2026-01-12 | ECG | **Atrial fibrillation, ventricular rate 96** | Known AF |
| RPT-LD06-015 | 2026-01-13 | Echo | **LVEF 30%** | Reduced; HFrEF |

## 8. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Normal intervals and LVEF categories | LD-01 |
| HFrEF, AF, ACS criteria | DG-01 |
| Stroke work-up | DG-06 |
| Chest-pain pathway timing | HO-03 |
| Patient charts | PR-01, PR-02, PR-05, PR-07, PR-08 |

## 9. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic report series (Pass 1) |
