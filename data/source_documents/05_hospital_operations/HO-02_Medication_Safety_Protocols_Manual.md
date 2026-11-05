---
doc_id: HO-02
title: "Medication Safety Protocols Manual"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-004, PAT-005, PAT-007, PAT-009, PAT-010, MED-002, MED-003, MED-012, MED-013, MED-014, MED-015, MED-016, MED-017, MED-018, MED-019, MED-026, MED-029, MED-030, LAB-028, PRO-001, PRO-002, PRO-003, PRO-007, PRO-008, PRO-010, DEP-004, DEP-005, DEP-010, DEP-012, DEP-013, ALG-001, ALG-003, ALG-004, ALG-005, ALG-006, INC-001, INC-003, INC-005, FPA-03, FPA-04, FPA-09, FPA-12]
related_docs: [DG-02, DG-03, DG-07, DG-08, HO-04, HO-05, HO-08, LD-03, MP-01, MP-02, MP-06, MP-07, PR-01, PR-04, PR-05, PR-07]
---

# HO-02: Medication Safety Protocols Manual

> **SYNTHETIC DATA NOTICE.** These protocols are fictional MediCore Policy written for software benchmarking and education. Every time target, threshold, and rule is an invented parameter that may differ from real practice and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-02 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 (all protocols shown as in force on 2026-10-01) |
| Protocols | PRO-001 reconciliation, PRO-002 high-alert medications, PRO-003 allergy alerts, PRO-008 renal dose adjustment, PRO-010 hypoglycemia and insulin safety |
| Owners | DEP-010 (PRO-001, 002, 008), DEP-013 (PRO-003), DEP-004 (PRO-010); approved by the CPRB |
| Clinical rules behind these protocols | DG-02, DG-03, DG-07, DG-08; MP-01 to MP-07 |
| Version history of every protocol | HO-08 |

## 2. PRO-001: Medication Reconciliation (version 2, effective 2024-06-01)

1. A pharmacist or trained technician obtains a **best possible medication history** within **24 hours of admission**, from at least two sources, and **explicitly includes over-the-counter drugs, supplements, and potassium-containing salt substitutes**.
2. Every medicine is matched to an active indication, kidney function (MP-07), documented allergies (MP-07), and interaction rules (MP-06).
3. At discharge a reconciled list is given to the patient and sent to the primary physician.
4. Patients taking five or more regular medicines receive a structured pharmacist review at least every **90 days** in outpatient care (DG-08).
5. Reconciliation findings that change therapy are recorded in the chart. Example: aspirin 81 mg taken over the counter by PAT-010 was found at the admission interview (PR-07).

## 3. PRO-002: High-Alert Medication Safety (version 2, effective 2025-03-01)

High-alert medications at MediCore are **MED-002, MED-003, MED-012, MED-013, MED-014, MED-015, MED-019, MED-029** (insulin glargine, insulin regular, apixaban, warfarin, unfractionated heparin, enoxaparin, vancomycin, epinephrine).

| Rule | Requirement |
|---|---|
| Ordering | Structured order sets only; dose and weight displayed |
| Verification | Pharmacist verification before dispensing; for MED-012 within **4 hours** of a new order (FPA-04, PRO-007) |
| Administration | Independent double check by two nurses for insulin infusions, heparin infusions, and IV vancomycin; epinephrine for anaphylaxis is exempt from pre-administration double check but is reviewed afterward |
| Storage | Separate labeled bins; no look-alike storage |
| Monitoring | Drug-specific (HO-04 for anticoagulants and vancomycin; section 6 for insulin) |

## 4. PRO-003: Allergy Documentation and Alerts (version 2, effective 2026-07-01)

### 4.1 Allergy record
Each flag records allergen class (ALG-001 to ALG-006), reaction, severity, date, **verification status**, and source. An **unverified or patient-reported flag is treated as the worst credible reaction** until verified (MP-07). The allergy is updated the same day after any event.

### 4.2 Dual verification (FPA-09)
Before the **first dose of any beta-lactam** (MED-016, MED-017, MED-018 and any other penicillin or cephalosporin) in a patient with **any allergy flag**, **both a pharmacist and a nurse must independently verify** the allergy, the drug, and the cross-reactivity rule in MP-07. The two checks are recorded separately.

### 4.3 Version 2 change (after INC-001)
In **version 1 (to 2026-06-30)** the bar-code "urgent override" could bypass the nursing check if the prescriber documented urgency. In **version 2 (from 2026-07-01)** the override is a **hard stop**: the nursing check cannot be bypassed for a first beta-lactam dose in a patient with an allergy flag. The event that triggered the change is INC-001 (PAT-007, 2026-05-17; PR-07, HO-08).

### 4.4 Special flags
- **ALG-005 (iodinated contrast):** flag is displayed to Radiology (DEP-012); the pre-medication pathway is chosen by Radiology and the prescriber. No patient currently carries this flag.
- **ALG-006 (latex):** the patient's wristband and room are marked; latex-free gloves, catheters and tourniquets are supplied. Example: PAT-009 (PR-07).
- **ALG-003 and ALG-004:** order sets must not default to aspirin or ACE inhibitors for flagged patients. A default aspirin order for PAT-005 was cancelled before administration on 2026-04-14 and logged as a near-miss (PR-05, HO-08).

## 5. PRO-008: Renal Dose Adjustment (version 3, effective 2026-05-01)

1. Every inpatient order and every outpatient prescription for a drug in the MP-07 section 4.2 list is checked against the **most recent eGFR**. Pharmacy owns the check; Nephrology (DEP-005) advises.
2. **Metformin (FPA-03):** eGFR 45 or higher no cap; **eGFR 30 to 44 maximum 1,000 mg/day; eGFR below 30 stop** (MP-02, MP-07).
3. Other renal rules follow MP-07, including piperacillin-tazobactam (**3.375 g every 6 hours at eGFR 30 or below**), enoxaparin, lisinopril, spironolactone and apixaban.
4. A new eGFR that falls into a lower band triggers a **renal-dose alert**. In version 1 (to 2025-04-30) the alert went only to the pharmacist work queue; in **version 2 (2025-05-01 to 2026-04-30)** it also went to the prescriber's inbox; in **version 3 (from 2026-05-01)** it does both and in addition:
   - An **NSAID order (for example MED-026) at eGFR below 60 is a hard stop**; override requires a second pharmacist and a documented reason.
5. The metformin cap should be implemented within **14 days** of the qualifying eGFR. (PAT-001's cap was applied 21 days after the eGFR of 2025-02-20, during version 1 of this protocol, which routed the alert only to the pharmacist queue; PR-01.)
6. The change to version 3 followed INC-005 (PAT-009, ibuprofen prescribed 2026-03-05 with an overridden alert; PR-07, HO-08).

## 6. PRO-010: Hypoglycemia and Insulin Safety (version 2, effective 2025-01-01)

### 6.1 Hypoglycemia alert (FPA-12)
A glucose **below 4.0 mmol/L (72 mg/dL)** triggers an alert: confirm by capillary measurement, give treatment, recheck in 15 minutes, notify the prescriber. During an insulin infusion, **dextrose is added to the infusion** and the rate reviewed.

### 6.2 DKA insulin infusion transition (FPA-12)
1. Infusion of MED-003 at 0.1 units/kg/hour begins after the potassium rule in DG-02 is satisfied.
2. Beta-hydroxybutyrate (LAB-028) and glucose are checked hourly at first, then every 2 hours.
3. **Transition to subcutaneous insulin is permitted when beta-hydroxybutyrate is below 0.6 mmol/L on two consecutive checks.**
4. Give the first subcutaneous basal dose (MED-002) at least **2 hours before** the infusion is stopped.
5. Example: PAT-004 had values of 0.5 mmol/L at 14:00 and 0.4 at 16:00 on 2025-12-10, so the criterion was met at 16:00; glargine was given at 16:30 and the infusion stopped at 18:30 (PR-04, LD-03).

### 6.3 SGLT2 inhibitors
A patient prescribed MED-030 receives sick-day teaching at initiation, recorded in the chart (DG-02). After an episode of DKA the drug is recorded as an adverse reaction and cannot be reordered without a documented override (MP-02, MP-07).

## 7. Override Audit

Overridden **Major** interaction alerts and all overridden renal or allergy hard stops are audited monthly by Clinical Pharmacy (DEP-010) and reported to the PSC. Overrides involved in INC-001, INC-003 and INC-005 are recorded in HO-08.

## 8. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Monographs, interactions, allergy and renal dosing | MP-01 to MP-07 |
| DKA, CKD/AKI, anaphylaxis, polypharmacy guidance | DG-02, DG-03, DG-07, DG-08 |
| Anticoagulant and stewardship protocols | HO-04 |
| Critical results | HO-05 |
| Incident reviews and version history | HO-08 |
| Patient charts | PR-01, PR-04, PR-05, PR-07 |

## 9. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic manual (Pass 1) |
