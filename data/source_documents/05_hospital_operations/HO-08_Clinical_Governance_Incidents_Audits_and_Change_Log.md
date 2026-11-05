---
doc_id: HO-08
title: "Clinical Governance: Incidents, Audits and Policy Change Log"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-003, PAT-005, PAT-006, PAT-007, PAT-009, PAT-011, PAT-013, MED-002, MED-016, MED-020, MED-024, MED-026, MED-031, PRO-001, PRO-002, PRO-003, PRO-004, PRO-005, PRO-006, PRO-007, PRO-008, PRO-009, PRO-010, PRO-011, PRO-012, PRO-013, PRO-014, PRO-015, PRO-016, DEP-013, STF-014, ALG-001, ALG-003, INC-001, INC-002, INC-003, INC-004, INC-005, INC-006, FPA-01, FPA-02, FPA-03, FPA-04, FPA-05, FPA-06, FPA-07, FPA-08, FPA-09, FPA-10, FPA-11, FPA-12, FPA-13, FPA-14]
related_docs: [HO-02, HO-03, HO-04, HO-05, HO-06, HO-07, LD-01, MP-02, MP-03, MP-04, MP-06, MP-07, PR-01, PR-03, PR-05, PR-06, PR-07, PR-08]
---

# HO-08: Clinical Governance, Incidents, Audits and Policy Change Log

> **SYNTHETIC DATA NOTICE.** MediCore Hospital, its incidents, review findings, and policy versions are fictional and exist only for software benchmarking and education. They are not real patient safety records and give no clinical guidance.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-08 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Quality, Patient Safety and Infection Control (DEP-013, STF-014); chair of the Patient Safety Committee (PSC) |
| Contents | Incident reports INC-001 to INC-006; near-miss log; audit findings; policy change log for PRO-001 to PRO-016; policy anchor (FPA) register |
| Related documents | PR-01, PR-03, PR-05, PR-06, PR-07, PR-08; MP-06, MP-07; HO-02 to HO-07 |

## 2. Harm Scale (MediCore)

| Level | Meaning |
|---|---|
| No harm | Event reached the patient; no effect |
| Temporary harm | Monitoring or minor intervention needed |
| Serious harm | Hospitalization, ICU, or major intervention |
| Sentinel | Death or permanent harm |

## 3. Incident Reports

### 3.1 INC-001: Penicillin anaphylaxis (PAT-007)

| Item | Detail |
|---|---|
| Date | 2026-05-17; chart PR-07 |
| Event | Amoxicillin-clavulanate (MED-016) 875/125 mg given at 21:05 to a patient with an ALG-001 flag recorded as "rash, patient-reported, unverified"; anaphylaxis at 21:17; epinephrine 0.5 mg IM at 21:19 and 21:27 |
| Harm | **Serious** (ICU observation 24 hours); recovered |
| Findings | Pharmacist verified the order at 20:48. The **nursing independent check required by dual verification (PRO-003, FPA-09) was bypassed with the bar-code "urgent override"**. The low severity and unverified status of the flag led staff to treat it as low risk |
| PSC review | 2026-05-27 |
| Corrective actions | PRO-003 version 2, **effective 2026-07-01**: the override becomes a hard stop; unverified flags are treated as the worst credible reaction; allergy record upgraded to confirmed anaphylaxis; allergy clinic referral; staff briefing |
| Status | Closed 2026-08-12 |

### 3.2 INC-002: Delayed critical potassium call (PAT-001)

| Item | Detail |
|---|---|
| Date | 2025-09-17; chart PR-01 |
| Event | Potassium 6.4 mmol/L verified at 08:05; telephoned to the ED physician at 08:41, **36 minutes** after verification against the 20-minute policy (FPA-13) |
| Harm | **No harm**; the patient was already monitored after the ECG at 07:50 |
| Findings | The first two call attempts at 08:08 and 08:20 reached the busy ED triage line; there was no escalation route in PRO-009 version 1 |
| PSC review | 2025-10-08 |
| Corrective actions | PRO-009 version 2, **effective 2025-11-01**: automatic escalation to the clinician's pager after two unanswered or busy attempts |
| Status | Closed 2025-12-03 |

### 3.3 INC-003: Ciprofloxacin and warfarin alert override (PAT-006)

| Item | Detail |
|---|---|
| Date | 2025-10-21 to 2025-10-26; chart PR-06 |
| Event | Ciprofloxacin (MED-020) started on 2025-10-21 at 17:30; the PharmaSafe Major alert at 17:32 was overridden with "will monitor"; **no INR recheck plan** was made. INR rose from 2.4 to **6.8** (verified 15:20, phoned 15:36 on 2025-10-26) |
| Harm | **Temporary harm** (gum bleeding, bruising; warfarin held; no transfusion) |
| Findings | PRO-007 version 1 expected a recheck plan but did not enforce it; the override reason field accepted free text |
| PSC review | 2025-11-12 |
| Corrective actions | PRO-007 version 2, **effective 2025-12-01**: structured, mandatory INR recheck plan; the INR within 3 days is auto-ordered |
| Status | Closed 2026-01-14 |

### 3.4 INC-004: Delayed isolation for C. difficile (PAT-003)

| Item | Detail |
|---|---|
| Date | 2026-03-07; chart PR-03 |
| Event | Positive result verified 08:40; laboratory phoned the ward nurse at 08:52 (compliant); Infection Prevention notified at 14:50; **precautions started 15:25, 6 hours 45 minutes after verification** |
| Harm | **No harm**; one other patient shared a bathroom; screening found no secondary case |
| Findings | Under PRO-012 version 1 the ward waited for Infection Control confirmation before starting precautions |
| PSC review | 2026-03-25 |
| Corrective actions | PRO-012 version 2, **effective 2026-05-01**: ward nurse starts contact-enteric precautions on the laboratory call; LabLink notifies Infection Control automatically |
| Status | Closed 2026-06-10 |

### 3.5 INC-005: NSAID prescribed in CKD with AKI (PAT-009)

| Item | Detail |
|---|---|
| Date | 2026-03-05 prescription; admission 2026-03-22; chart PR-07 |
| Event | Ibuprofen (MED-026) 600 mg three times daily prescribed for a patient with CKD (baseline creatinine 1.3 mg/dL, eGFR 40) taking lisinopril and furosemide; the PharmaSafe alert was overridden as "short course". AKI stage 2 followed (peak creatinine 2.9 mg/dL on 2026-03-23, 2.2 times baseline) |
| Harm | **Serious** (hospitalization 6 days); recovered to a new baseline of 1.4 mg/dL |
| Findings | Version 2 of PRO-008 allowed override of the NSAID alert without a second check |
| PSC review | 2026-04-15 |
| Corrective actions | PRO-008 version 3, **effective 2026-05-01**: NSAID order at eGFR below 60 is a hard stop requiring a second pharmacist; NSAIDs added to the patient's chart as "avoid" |
| Status | Closed 2026-07-08 |

### 3.6 INC-006: Missed heart-failure follow-up (PAT-011)

| Item | Detail |
|---|---|
| Date | 2026-01-17 discharge; readmission 2026-02-02; chart PR-08 |
| Event | The discharge telephone number had two digits transposed; the only call, at 11:05 on 2026-01-19, reached a wrong number; the clinic visit of 2026-01-23 was missed; the INR check due by 2026-01-20 14:30 was not done. Readmitted 16 days after discharge with INR 3.4 |
| Harm | **Serious** (readmission 6 days) |
| Findings | No second call attempt, no emergency-contact fallback, no outreach for a missed visit, risk score field not completed (HO-07) |
| PSC review | 2026-02-24 |
| Corrective actions | PRO-016 version 2, **effective 2026-04-01**: second attempt within 24 hours, emergency contact, number verified at discharge, outreach within 1 working day of a missed visit |
| Status | Closed 2026-05-20 |

## 4. Near-Miss Log (not in the INC series)

| Date | Patient | Event | Outcome |
|---|---|---|---|
| 2026-04-14 | PAT-005 | The admission order set auto-populated aspirin 300 mg for a patient with ALG-003; the PRO-003 alert fired and the pharmacist cancelled the order at 19:46, 6 minutes after it was placed | No dose given; order-set default corrected 2026-05-04 |

## 5. Audit Findings

| Audit | Finding | Source |
|---|---|---|
| Renal-dose audit 2025 | PAT-001's metformin cap was applied 21 days after the qualifying eGFR of 2025-02-20 (alert filed only in the pharmacist queue under PRO-008 version 1); this led to PRO-008 version 2 (2025-05-01) routing the alert to the prescriber inbox as well. Not an incident | PR-01 |
| Override audit, Major interaction alerts | Overrides underlying INC-001, INC-003 and INC-005 were found; monthly audit introduced | MP-06 section 5 |
| Sepsis bundle audit 2026 | PAT-003's 53-minute first antibiotic was compliant with version 2 (60 minutes) but would not have met version 3 (50 minutes); PAT-013's 42 minutes met version 3 | PR-03, PR-08 |
| Critical-result audit | Seven recorded calls in the dataset; six within 20 minutes, one outside (INC-002) | HO-05 |
| Follow-up audit | HF follow-up compliance reviewed after INC-006 | HO-07 |

## 6. Policy Change Log (current version in force on 2026-10-01 in bold)

| Protocol | Version | Effective | Superseded | Change |
|---|---|---|---|---|
| PRO-001 | 1 | 2023-01-01 | 2024-05-31 | Initial |
| PRO-001 | **2** | **2024-06-01** | | Over-the-counter and supplements explicit |
| PRO-002 | 1 | 2023-01-01 | 2025-02-28 | Initial |
| PRO-002 | **2** | **2025-03-01** | | List updated to MED-002, 003, 012, 013, 014, 015, 019, 029 |
| PRO-003 | 1 | 2023-01-01 | 2026-06-30 | Dual verification with bar-code urgent override |
| PRO-003 | **2** | **2026-07-01** | | Override is a hard stop (after INC-001) |
| PRO-004 | 1 | 2022-03-01 | 2024-12-31 | First antibiotic within 90 minutes |
| PRO-004 | 2 | 2025-01-01 | 2026-02-28 | 60 minutes |
| PRO-004 | **3** | **2026-03-01** | | **50 minutes** (FPA-02) |
| PRO-005 | 1 | 2023-05-01 | 2025-05-31 | Door-to-CT 25 minutes |
| PRO-005 | **2** | **2025-06-01** | | Door-to-CT **20 minutes** (FPA-07) |
| PRO-006 | 1 | 2023-01-01 | 2024-12-31 | Troponin at 0 and 3 hours |
| PRO-006 | **2** | **2025-01-01** | | Troponin at 0 and 2 hours; ECG within 10 minutes (FPA-08) |
| PRO-007 | 1 | 2023-01-01 | 2025-11-30 | Initial |
| PRO-007 | **2** | **2025-12-01** | | Mandatory structured INR plan (after INC-003) |
| PRO-008 | 1 | 2023-01-01 | 2025-04-30 | Alert to pharmacist queue only |
| PRO-008 | 2 | 2025-05-01 | 2026-04-30 | Alert to prescriber inbox and pharmacist queue |
| PRO-008 | **3** | **2026-05-01** | | NSAID hard stop at eGFR below 60 (after INC-005) |
| PRO-009 | 1 | 2023-01-01 | 2025-10-31 | 20-minute call rule (FPA-13) |
| PRO-009 | **2** | **2025-11-01** | | Pager escalation after two failed attempts (after INC-002) |
| PRO-010 | 1 | 2023-09-01 | 2024-12-31 | Single ketone check for transition |
| PRO-010 | **2** | **2025-01-01** | | Two consecutive checks below 0.6 mmol/L (FPA-12) |
| PRO-011 | 1 | 2023-01-01 | 2025-05-31 | Initial |
| PRO-011 | **2** | **2025-06-01** | | INR within 72 hours and contact verification |
| PRO-012 | 1 | 2023-01-01 | 2026-04-30 | Precautions after Infection Control confirmation |
| PRO-012 | **2** | **2026-05-01** | | Start on laboratory call (after INC-004) |
| PRO-013 | 1 | 2023-06-01 | 2025-08-31 | Culture review at 72 hours |
| PRO-013 | **2** | **2025-09-01** | | Level before dose 4; 48-hour review (FPA-11) |
| PRO-014 | 1 | 2023-01-01 | 2024-07-31 | Initial |
| PRO-014 | **2** | **2024-08-01** | | Bar-code labeling at the bedside |
| PRO-015 | 1 | 2023-01-01 | 2025-02-28 | Initial |
| PRO-015 | **2** | **2025-03-01** | | Response within 10 minutes |
| PRO-016 | 1 | 2024-07-01 | 2026-03-31 | Single call attempt |
| PRO-016 | **2** | **2026-04-01** | | Second attempt, emergency contact, outreach (after INC-006) |

## 7. Policy Anchor (FPA) Register

| ID | Anchor | Protocol | Defined in |
|---|---|---|---|
| FPA-01 | Critical potassium 6.2 or higher or 2.9 or lower mmol/L | PRO-009 | HO-05, LD-01 |
| FPA-02 | Sepsis antibiotic 50 minutes (version 3); 60 minutes (version 2); repeat lactate within 2 hours if above 2.5 mmol/L | PRO-004 | HO-03 |
| FPA-03 | Metformin maximum 1,000 mg/day at eGFR 30 to 44; stop below 30 | PRO-008 | HO-02, MP-02, MP-07 |
| FPA-04 | New apixaban order verified within 4 hours | PRO-007 | HO-04, MP-03 |
| FPA-05 | INR target 2.0 to 3.0; above 4.5 clinic call within 24 hours; INR within 72 hours of discharge | PRO-007, PRO-011 | HO-04, HO-07 |
| FPA-06 | HF discharge call within 48 hours and visit within 7 days | PRO-016 | HO-07 |
| FPA-07 | Door-to-CT-head within 20 minutes | PRO-005 | HO-03 |
| FPA-08 | ECG within 10 minutes; hs-troponin at 0 and 2 hours | PRO-006 | HO-03 |
| FPA-09 | Dual verification for first beta-lactam dose with any allergy flag | PRO-003 | HO-02 |
| FPA-10 | Precautions until 72 hours after diarrhea resolves | PRO-012 | HO-06 |
| FPA-11 | First vancomycin level before the fourth dose | PRO-013 | HO-04, MP-04 |
| FPA-12 | Two consecutive ketones below 0.6 mmol/L; hypoglycemia alert below 4.0 mmol/L | PRO-010 | HO-02 |
| FPA-13 | Critical results phoned within 20 minutes with read-back | PRO-009 | HO-05 |
| FPA-14 | Levothyroxine and oral iron at least 4 hours apart | MED-024, MED-031 | MP-02, MP-06 |

## 8. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Patient charts for each incident | PR-01 (INC-002), PR-03 (INC-004), PR-06 (INC-003), PR-07 (INC-001, INC-005), PR-08 (INC-006) |
| Override audit and ADR list | MP-06, MP-07 |
| Protocol text | HO-02 to HO-07 |

## 9. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic governance record (Pass 1) |
