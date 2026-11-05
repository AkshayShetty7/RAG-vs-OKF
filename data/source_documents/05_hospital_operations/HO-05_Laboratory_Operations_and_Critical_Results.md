---
doc_id: HO-05
title: "Laboratory Operations and Critical Results"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-003, PAT-006, PAT-008, PAT-011, PAT-013, LAB-005, LAB-007, LAB-010, LAB-012, LAB-014, LAB-024, PRO-009, PRO-012, PRO-014, DEP-011, DEP-013, STF-012, INC-002, INC-004, FPA-01, FPA-13]
related_docs: [HO-06, HO-08, LD-01, LD-02, LD-03, LD-04, LD-05, PR-01, PR-02, PR-03, PR-04, PR-06, PR-07, PR-08]
---

# HO-05: Laboratory Operations and Critical Results

> **SYNTHETIC DATA NOTICE.** These protocols are fictional MediCore Policy written for software benchmarking and education. Every time target, threshold, and rule is an invented parameter that may differ from real practice and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-05 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 |
| Protocols | PRO-009 critical laboratory value notification; PRO-014 patient identification and specimen labeling |
| Owner | Clinical Laboratory (DEP-011, Laboratory Director STF-012); approved by the CPRB |
| Test definitions and ranges | LD-01 |
| Version history | HO-08 |

## 2. PRO-009: Critical Laboratory Value Notification

### 2.1 Version history

| Version | Effective | Change |
|---|---|---|
| 1 | 2023-01-01 to 2025-10-31 | Call the responsible clinician or the ward or triage line |
| **2** | **2025-11-01** | After **two unanswered or busy attempts** the call **escalates automatically to the responsible clinician's pager** (after INC-002) |

### 2.2 Scope
PRO-009 applies to **LAB-005, LAB-007, LAB-010, LAB-012, LAB-014 and LAB-024 only**. Other abnormal results (for example hemoglobin, creatinine, ferritin, NT-proBNP) are flagged in the report but not telephoned.

### 2.3 Critical values (LD-01)

| Test | Critical value |
|---|---|
| Potassium (LAB-005) | **6.2 mmol/L or higher, or 2.9 mmol/L or lower** (FPA-01) |
| hs-troponin (LAB-007) | **100 ng/L or higher** |
| INR (LAB-010) | **5.0 or higher** |
| Blood culture (LAB-012) | Any positive bottle |
| Lactate (LAB-014) | **4.0 mmol/L or higher** |
| C. difficile (LAB-024) | Any positive result; also notify Infection Control (PRO-012, HO-06) |

### 2.4 Time and method (FPA-13)
1. The result is verified in LabLink by laboratory staff.
2. The laboratory **telephones the responsible clinician within 20 minutes of verification** (not of collection).
3. The recipient reads back the patient name, identifiers, test, value and units; the laboratory records recipient, time, and read-back.
4. If the responsible clinician cannot be reached, the call goes to the covering clinician; from version 2, to the pager after two failed attempts.
5. A call outside 20 minutes is reported as a notification deviation and reviewed by the Laboratory Director and Quality (DEP-013).

### 2.5 Results recorded in the dataset

| Patient | Test and value | Verified | Called | Interval | Compliance |
|---|---|---|---|---|---|
| PAT-001 | Potassium 6.4 mmol/L, 2025-09-17 | 08:05 | 08:41 | 36 min | **Not met: INC-002** |
| PAT-002 | hs-troponin 112 ng/L, 2025-03-04 | 00:10 | 00:20 | 10 min | Met |
| PAT-008 | hs-troponin 155 ng/L, 2026-02-03 | 10:18 | 10:26 | 8 min | Met |
| PAT-006 | INR 6.8, 2025-10-26 | 15:20 | 15:36 | 16 min | Met |
| PAT-003 | Positive blood culture bottle, 2026-02-27 (bottle positive 04:10) | 04:10 | 04:18 | 8 min | Met |
| PAT-003 | C. difficile positive, 2026-03-07 | 08:40 | 08:52 (ward nurse) | 12 min | Met (laboratory call); downstream isolation delay is INC-004 |
| PAT-013 | Positive blood culture bottle, 2026-06-19 (bottle positive 14:30) | 14:30 | 14:41 | 11 min | Met |

Results below the critical value (for example PAT-002 0-hour troponin 48 ng/L, PAT-008 0-hour troponin 62 ng/L, PAT-003 lactate 3.4 mmol/L, PAT-011 INR 3.4) were not telephoned.

### 2.6 INC-002 detail
For PAT-001 the first two call attempts, at 08:08 and 08:20 on 2025-09-17, reached the busy ED triage line; the third at 08:41 reached the physician. Under version 1 no automatic escalation existed. Version 2 closes this gap. The patient was already on cardiac monitoring after the ECG at 07:50, and no harm resulted (PR-01, HO-08).

## 3. PRO-014: Patient Identification and Specimen Labeling (version 2, effective 2024-08-01)

| Rule | Requirement |
|---|---|
| Identifiers | Two identifiers (full name and date of birth) checked against the wristband at the bedside |
| Labeling | Label printed at the point of care by bar-code scan and applied **in the patient's presence, before leaving the bedside** |
| Collector | Collector identity and time recorded in LabLink |
| Rejection | Unlabeled or mislabeled specimens, wrong container, clotted samples, insufficient volume, or hemolyzed potassium samples (recollect urgently) |
| Blood cultures | Two sets from separate sites, drawn before antibiotics where feasible |
| Transport | Urgent specimens sent immediately; target receipt within 15 minutes |

Worked example: PAT-001's 07:42 potassium specimen was labeled under PRO-014 (PR-01).

## 4. Turnaround Targets (urgent specimens; LD-01)

| Test group | Receipt to verification |
|---|---|
| hs-troponin, potassium, BMP, lactate, CBC, INR | 45 minutes |
| Blood gas | 15 minutes |
| C. difficile toxin/PCR | 12 hours |

## 5. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Test catalog, ranges, critical values | LD-01 |
| Chart reports containing these results | LD-02, LD-03, LD-04, LD-05 |
| Isolation after positive C. difficile | HO-06 |
| Incident reviews and version history | HO-08 |
| Patient charts | PR-01, PR-02, PR-03, PR-04, PR-06, PR-07, PR-08 |

## 6. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic protocols (Pass 1) |
