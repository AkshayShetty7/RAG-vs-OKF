---
doc_id: HO-07
title: "Discharge, Follow-up and Readmission Prevention"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-011, DIS-004, PRO-001, PRO-007, PRO-011, PRO-016, DEP-003, DEP-014, STF-005, STF-015, INC-006, FPA-05, FPA-06]
related_docs: [DG-01, DG-02, HO-02, HO-04, HO-08, MP-01, MP-03, PR-01, PR-08]
---

# HO-07: Discharge, Follow-up and Readmission Prevention

> **SYNTHETIC DATA NOTICE.** These protocols are fictional MediCore Policy written for software benchmarking and education. Every time target and rule is an invented parameter that may differ from real practice and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-07 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 |
| Protocols | PRO-011 discharge planning and follow-up scheduling; PRO-016 heart-failure post-discharge follow-up |
| Owner | Care Coordination and Discharge Services (DEP-014, STF-015); PRO-016 clinical co-owner Cardiology (DEP-003, STF-005); approved by the CPRB |
| Clinical rules | DG-01 (heart failure) |
| Version history | HO-08 |

## 2. PRO-011: Discharge Planning and Follow-up Scheduling (version 2, effective 2025-06-01)

### 2.1 Required elements before a patient leaves
1. **Reconciled medication list** (PRO-001, HO-02), with changes explained and the patient given the list.
2. **Contact verification:** the patient's telephone number and an emergency contact are read back and confirmed (strengthened by PRO-016 version 2).
3. **Follow-up appointments booked** before discharge, with dates on the patient's summary.
4. **Pending results and tests** (for example INR) assigned to a named clinician.
5. **Warfarin patients: INR check within 72 hours of discharge** scheduled before departure (FPA-05; HO-04).
6. Equipment, diet and activity instructions; sick-day rules for patients on ACE inhibitors, mineralocorticoid antagonists, diuretics, metformin or SGLT2 inhibitors (DG-01, DG-02).
7. Discharge summary sent to the primary physician within 24 hours.

### 2.2 Documentation
The discharge time is recorded to the minute because follow-up deadlines are counted from it.

## 3. PRO-016: Heart-Failure Post-Discharge Follow-up

### 3.1 Standard (FPA-06; all versions)
For every patient discharged after an admission for heart failure, or with HFrEF (DIS-004) as an active problem:
- **Telephone call within 48 hours of discharge** by Care Coordination.
- **Clinic visit within 7 days of discharge** at the heart-failure clinic (DEP-003).
- INR check within 72 hours if on warfarin (PRO-007).

### 3.2 Version history

| Version | Effective | Change |
|---|---|---|
| 1 | 2024-07-01 to 2026-03-31 | Single call attempt expected; no outreach rule for missed visits |
| **2** | **2026-04-01** | **Second call attempt within 24 hours**, then the emergency contact; **telephone number verified at discharge**; **outreach within 1 working day of a missed visit**; 30-day readmission review (after INC-006) |

### 3.3 Call content
Weight and symptoms, medication adherence, salt and fluid intake, sick-day rule review, appointments, INR if applicable.

### 3.4 Worked examples

| Patient | Discharge | Call deadline | Call | Visit deadline | Visit | INR deadline (warfarin) | INR | Result |
|---|---|---|---|---|---|---|---|---|
| PAT-001 | 2025-09-20 | 2025-09-22 (48 h) | 2025-09-22 | 2025-09-27 (7 d) | 2025-09-26 (day 6) | n/a (not on warfarin) | n/a | Met |
| PAT-011, first | 2026-01-17 14:30 | 2026-01-19 14:30 | Wrong number, 2026-01-19 11:05; no second attempt | 2026-01-24 14:30 | No-show 2026-01-23 | 2026-01-20 14:30 | Not done | **Not met: INC-006** (version 1) |
| PAT-011, second | 2026-02-08 11:00 | 2026-02-10 11:00 | 2026-02-09 09:30 (22 h 30 min) | 2026-02-15 11:00 | 2026-02-12 (day 4) | 2026-02-11 11:00 | 2026-02-10 (INR 2.6) | Met |

PAT-011 was readmitted on 2026-02-02, 16 days after the first discharge (PR-08).

## 4. Readmission Prevention

### 4.1 MediCore Heart-Failure Readmission Risk Score (fictional)
One point each: admission for heart failure in the past 12 months; eGFR below 45; NT-proBNP above the age-band threshold at discharge (DG-01); atrial fibrillation; living alone; unreliable telephone contact. A score of **3 or more** triggers a nurse home-visit offer. PAT-011 scored 3 at the first discharge (atrial fibrillation, NT-proBNP 4,820 pg/mL, prior recent admission), which did not trigger an outreach because the score field was not completed.

### 4.2 Monitoring
Care Coordination reports the 30-day readmission rate for heart failure monthly to the PSC (HO-08).

## 5. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Heart-failure guideline | DG-01 |
| Heart-failure drug monographs | MP-01 |
| Warfarin monograph and INR rules | MP-03, HO-04 |
| Reconciliation and sick-day rules | HO-02 |
| Incident review (INC-006) and version history | HO-08 |
| Patient charts | PR-01, PR-08 |

## 6. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic protocols (Pass 1) |
