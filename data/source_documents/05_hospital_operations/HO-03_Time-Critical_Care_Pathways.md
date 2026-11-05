---
doc_id: HO-03
title: "Time-Critical Care Pathways"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, PAT-003, PAT-005, PAT-008, PAT-013, LAB-007, LAB-012, LAB-014, LAB-021, PRO-003, PRO-004, PRO-005, PRO-006, PRO-009, PRO-013, PRO-015, DEP-001, DEP-003, DEP-008, DEP-009, ALG-003, FPA-02, FPA-07, FPA-08]
related_docs: [DG-01, DG-05, DG-06, HO-02, HO-04, HO-05, HO-08, LD-04, LD-06, LD-07, PR-02, PR-03, PR-05, PR-07, PR-08]
---

# HO-03: Time-Critical Care Pathways

> **SYNTHETIC DATA NOTICE.** These pathways are fictional MediCore Policy written for software benchmarking and education. Every time target and threshold is an invented parameter that may differ from real practice and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-03 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 (protocols shown as in force on 2026-10-01 unless a historical version is stated) |
| Protocols | PRO-004 sepsis bundle, PRO-005 stroke code, PRO-006 chest-pain / ACS pathway, PRO-015 rapid response |
| Owners | DEP-001 and DEP-009 (PRO-004); DEP-008 (PRO-005); DEP-003 (PRO-006); DEP-009 (PRO-015); approved by the CPRB |
| Clinical rules | DG-01 (ACS), DG-05 (sepsis), DG-06 (stroke) |
| Version history | HO-08 |

## 2. PRO-004: Sepsis Bundle

### 2.1 Version history (the version in force on the event date applies)

| Version | Effective | Superseded | First-antibiotic target (from sepsis alert) |
|---|---|---|---|
| 1 | 2022-03-01 | 2024-12-31 | 90 minutes |
| 2 | 2025-01-01 | 2026-02-28 | **60 minutes** |
| **3** | **2026-03-01** | In force | **50 minutes** (FPA-02) |

### 2.2 Bundle elements (version 3; identical in version 2 except for the antibiotic target)
1. **Start event:** sepsis alert activated by the screening trigger (DG-05).
2. Measure lactate (LAB-014) at the alert; draw blood cultures (LAB-012) **before** the first antibiotic if this does not delay it.
3. **Give the first antibiotic within 50 minutes of the alert.**
4. Repeat lactate within **2 hours** if the first value is **above 2.5 mmol/L**.
5. Crystalloid resuscitation for hypotension or lactate of 4.0 mmol/L or higher.
6. Reassess and escalate through PRO-015 if mean arterial pressure stays below 65 mmHg.
7. Review cultures and de-escalate at 48 to 72 hours under PRO-013 (HO-04).

### 2.3 Worked examples

| Patient | Date | Version in force | Alert to antibiotic | Target | Result |
|---|---|---|---|---|---|
| PAT-003 | 2026-02-26 | Version 2 | 53 minutes (10:05 to 10:58) | 60 | Met (would not meet version 3) |
| PAT-013 | 2026-06-18 | Version 3 | 42 minutes (04:10 to 04:52) | 50 | Met |

PAT-003's lactate was 3.4 mmol/L at 10:20 and repeated at 12:05 (1 hour 45 minutes), within the 2-hour rule (PR-03, LD-04). PAT-013's lactate was 3.0 mmol/L at 04:20, repeated at 05:50 (PR-08).

## 3. PRO-005: Stroke Code Pathway (version 2, effective 2025-06-01)

| Step | Requirement |
|---|---|
| Activation | Stroke code called by triage on suspected stroke with last-known-well within the treatment window |
| Last known well and NIHSS | Recorded at activation |
| **Door-to-CT-head** | **Scan start within 20 minutes of arrival (FPA-07)**; version 1 target was 25 minutes (to 2025-05-31) |
| CT read | Radiologist read within **10 minutes of scan start** |
| Stroke team | Neurology (DEP-008) at bedside within 15 minutes of activation |
| Decision | Reperfusion decision documented with rationale (DG-06) |
| Antithrombotic | Aspirin or clopidogrel per DG-06; check allergy flag before any order set (PRO-003) |
| Anticoagulant timing | After repeat CT per DG-06; new apixaban order verified within 4 hours (HO-04) |

Worked example: PAT-005, door 18:55, CT start 19:14 (19 minutes), read 19:20 (6 minutes after start), on 2026-04-14: all targets met (PR-05, LD-07).

## 4. PRO-006: Chest-Pain / ACS Pathway (version 2, effective 2025-01-01)

| Step | Requirement (FPA-08) |
|---|---|
| 12-lead ECG (LAB-021) | **Within 10 minutes of arrival** |
| hs-troponin (LAB-007) | Draws at **0 and 2 hours** (version 1 used 0 and 3 hours, to 2024-12-31) |
| Critical troponin | **100 ng/L or higher** is phoned within 20 minutes of verification (PRO-009, HO-05) |
| Antiplatelet | Aspirin 300 mg load unless ALG-003 (clopidogrel alternative); clopidogrel 300 mg before angiography (DG-01) |
| Cardiology | Cardiology fellow notified at critical result |
| Disposition | Admission, angiography and discharge per DG-01 |

Worked examples: PAT-002 (2025-03-03): ECG at 7 minutes, draws 2 h 02 min apart, critical result phoned in 10 minutes. PAT-008 (2026-02-03): ECG at 7 minutes, draws 2 h 04 min apart, critical result phoned in 8 minutes (PR-02, PR-07, LD-04, LD-06).

## 5. PRO-015: Rapid Response and Escalation (version 2, effective 2025-03-01)

### 5.1 Triggers (any one)
Respiratory rate 30 or higher; heart rate above 130; systolic pressure below 90 mmHg or mean arterial pressure below 65 mmHg; acute change in consciousness; staff concern.

### 5.2 Response
Rapid response team (ICU physician and nurse, DEP-009) at the bedside within **10 minutes** of the call; decision on ICU transfer within 30 minutes of the call. Worked example: PAT-003 on 2026-02-27, call at 06:05 for respiratory rate 34 and mean arterial pressure 58 mmHg, ICU transfer at 06:30 (PR-03).

## 6. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Sepsis, ACS and stroke guidelines | DG-05, DG-01, DG-06 |
| Troponin, lactate, ECG and CT reports | LD-04, LD-06, LD-07 |
| Critical-result notification | HO-05 |
| Stewardship and anticoagulation | HO-04 |
| Allergy alerts | HO-02 |
| Incident review and version history | HO-08 |
| Patient charts | PR-02, PR-03, PR-05, PR-07, PR-08 |

## 7. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic pathways (Pass 1) |
