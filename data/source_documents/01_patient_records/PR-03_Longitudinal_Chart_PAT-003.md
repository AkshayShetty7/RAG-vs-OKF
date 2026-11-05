---
doc_id: PR-03
title: "Longitudinal Chart: PAT-003 (Thomas Okonkwo-Reyes)"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, DIS-007, DIS-008, DIS-009, DIS-023, MED-016, MED-017, MED-018, MED-019, MED-021, MED-022, MED-023, LAB-012, LAB-014, LAB-015, LAB-016, LAB-018, LAB-019, LAB-020, LAB-024, PRO-004, PRO-009, PRO-012, PRO-013, PRO-015, DEP-001, DEP-002, DEP-006, DEP-007, DEP-009, DEP-010, STF-008, STF-009, STF-011, INC-004, FPA-02, FPA-10, FPA-11]
related_docs: [DG-04, DG-05, HO-03, HO-04, HO-05, HO-06, HO-08, LD-04, LD-05, LD-07, LD-08, MP-04, MP-05]
---

# PR-03: Longitudinal Chart, PAT-003 (Thomas Okonkwo-Reyes)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-03 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Record period covered | 2024-11-20 to 2026-08-11 |
| Patient | PAT-003 |
| Primary services | DEP-006 Pulmonology (head STF-008); DEP-001; DEP-009 ICU (head STF-011); DEP-007 Infectious Diseases (head STF-009); DEP-002 |
| Reference guidelines | DG-04 (COPD, pneumonia), DG-05 (sepsis, C. difficile) |
| Reference monographs | MP-04, MP-05 |
| Policies applied | PRO-004 (version 2), PRO-009, PRO-012, PRO-013, PRO-015 (HO-03, HO-04, HO-05, HO-06) |
| Governance review | INC-004 (HO-08) |

## 2. Purpose and Scope

This chart follows PAT-003, who has chronic obstructive pulmonary disease (DIS-007), through a single 19-day admission (2026-02-26 to 2026-03-16) that began as a COPD exacerbation with community-acquired pneumonia (DIS-008), progressed to sepsis (DIS-009) and ICU care, required antibiotic escalation and later de-escalation, and ended with hospital-onset Clostridioides difficile infection (DIS-023). It supplies the event times needed to judge compliance with the sepsis bundle in force on the date of admission, the vancomycin level-timing rule, and the isolation rule.

## 3. Patient Summary

| Item | Value |
|---|---|
| Patient ID / name | PAT-003 / Thomas Okonkwo-Reyes (synthetic) |
| Date of birth / age | 1968-01-30 / 58 years (at 2026-10-01) |
| Sex | Male |
| Height / weight | 181 cm; 84 kg (2026-02-26), 79 kg (2026-03-16) |
| Occupation | Former warehouse supervisor |
| Smoking | 35 pack-years; stopped 2023 |
| Allergy | **No known drug allergies**; no ALG entity applies |

## 4. Problem List

| Problem | ID | Onset | Status at 2026-08-11 |
|---|---|---|---|
| COPD | DIS-007 | Diagnosed 2021; spirometry-confirmed 2024-11-20 | Active; no exacerbation since discharge |
| Community-acquired pneumonia, right lower lobe | DIS-008 | 2026-02-26 | Resolved |
| Sepsis | DIS-009 | 2026-02-26 | Resolved |
| C. difficile infection, hospital-onset | DIS-023 | 2026-03-06 | Resolved; no recurrence |

## 5. Baseline Respiratory Data

Spirometry (LAB-019, report in LD-08) on 2024-11-20: post-bronchodilator FEV1/FVC 0.54, FEV1 48% of predicted, consistent with the DG-04 diagnostic criteria for COPD. Home regimen before the admission: tiotropium 18 micrograms inhaled daily (MED-022) and albuterol as needed (MED-021). No home oral steroid.

## 6. Admission Timeline, 2026-02-26 to 2026-03-16 (ENC-003-01)

### 6.1 Emergency Department and sepsis bundle (PRO-004 version 2)

On 2026-02-26 the sepsis bundle in force was **version 2** (first antibiotic within 60 minutes of the sepsis alert). Version 3, with a 50-minute target, took effect on 2026-03-01 (FPA-02; change record in HO-08).

| Clock time (2026-02-26) | Event |
|---|---|
| 09:12 | Arrival at DEP-001 with three days of productive cough, fever, and worsening breathlessness |
| 09:40 | Arterial blood gas (LAB-018) on room air: pH 7.28, PaCO2 8.3 kPa (62 mmHg), PaO2 7.7 kPa (58 mmHg) |
| 09:55 | Chest X-ray (LAB-020): right lower lobe consolidation (report in LD-07) |
| 10:05 | **Sepsis alert activated** (temperature 38.9 C, heart rate 124, respiratory rate 30, BP 96/58) |
| 10:20 | Lactate (LAB-014) drawn: 3.4 mmol/L |
| 10:25 | Blood cultures (LAB-012), two sets, drawn before antibiotics |
| 10:58 | **First antibiotic: ceftriaxone 2 g IV (MED-017)**, 53 minutes after the alert |
| 12:05 | Repeat lactate: 2.1 mmol/L (1 hour 45 minutes after the first; repeat required within 2 hours because the first value exceeded 2.5 mmol/L) |

Compliance against version 2 (60 minutes): **met**. The same 53 minutes would **not** have met the version 3 target of 50 minutes. Inflammatory markers on arrival (LD-04): procalcitonin (LAB-015) 12.6 ng/mL; C-reactive protein (LAB-016) 214 mg/L.

Treatment for the COPD exacerbation: prednisone 40 mg daily for 5 days from 2026-02-26 (MED-023), albuterol nebulization every 4 hours, tiotropium continued, controlled oxygen with non-invasive ventilation overnight.

### 6.2 Deterioration and ICU (PRO-015)

At 06:05 on 2026-02-27 the rapid response team was called for respiratory rate 34 and mean arterial pressure 58 mmHg. The patient was fluid-responsive and did not require a vasopressor. He was transferred to DEP-009 at 06:30. Antibiotics were escalated at 07:20: piperacillin-tazobactam 4.5 g IV every 6 hours (MED-018) plus vancomycin IV (MED-019) pending cultures. Ceftriaxone was discontinued.

### 6.3 Vancomycin level timing (PRO-013, FPA-11)

Vancomycin was pharmacy-managed (DEP-010). Doses were given every 12 hours: 07:20 and 19:20 on 2026-02-27, 07:20 and 19:20 on 2026-02-28. FPA-11 requires the first level before the fourth dose. The level was drawn at **18:50 on 2026-02-28**, 30 minutes before the fourth dose, and was 14.8 mg/L; the dose schedule was left unchanged.

### 6.4 Culture results and de-escalation

| Time | Event |
|---|---|
| 2026-02-27 04:10 | Blood culture bottle positive: gram-positive cocci in chains (preliminary) |
| 2026-02-28 09:30 | Organism identified: Streptococcus pneumoniae |
| 2026-03-01 08:20 | Susceptibilities: penicillin-susceptible, ceftriaxone-susceptible (report in LD-05) |
| 2026-03-01 13:00 | Stewardship review (DEP-007, PRO-013): piperacillin-tazobactam and vancomycin stopped; ceftriaxone 2 g IV daily restarted |
| 2026-03-01 | Transfer from ICU to a ward bed in DEP-002; procalcitonin 3.1 ng/mL |
| 2026-03-03 | Oral step-down: amoxicillin-clavulanate 875/125 mg twice daily (MED-016) |
| 2026-03-04 | Final antibiotic dose (day 7 of therapy counted from 2026-02-26) |

### 6.5 Hospital-onset C. difficile infection (INC-004)

Watery diarrhea began on the evening of 2026-03-06 (hospital day 9). A stool specimen for C. difficile toxin/PCR (LAB-024) was sent at 22:10. The positive result was verified at **08:40 on 2026-03-07**. Contact-enteric precautions (PRO-012) were not started until **15:25**, an interval of 6 hours 45 minutes. During this interval the patient used a shared bathroom with one other patient (no secondary case identified on screening). The delay was reported as **INC-004** and reviewed in HO-08.

Treatment: oral vancomycin 125 mg every 6 hours (MED-019, oral route) from 2026-03-07 for 10 days, last dose 2026-03-16. Diarrhea resolved at 06:00 on 2026-03-12. Under FPA-10 precautions continue until 72 hours after diarrhea resolves, so they ended at 06:00 on 2026-03-15 (HO-06). Discharge occurred on 2026-03-16 at 10:20.

## 7. Medication Summary for the Admission

| Medication | ID | Dates | Dose |
|---|---|---|---|
| Ceftriaxone | MED-017 | 2026-02-26; 2026-03-01 to 2026-03-02 | 2 g IV daily |
| Piperacillin-tazobactam | MED-018 | 2026-02-27 to 2026-03-01 | 4.5 g IV every 6 h |
| Vancomycin (IV) | MED-019 | 2026-02-27 to 2026-03-01 | Pharmacy-managed, every 12 h |
| Amoxicillin-clavulanate | MED-016 | 2026-03-03 to 2026-03-04 | 875/125 mg twice daily |
| Vancomycin (oral) | MED-019 | 2026-03-07 to 2026-03-16 | 125 mg every 6 h |
| Prednisone | MED-023 | 2026-02-26 to 2026-03-02 | 40 mg daily |
| Albuterol | MED-021 | Throughout | As needed and scheduled nebulization |
| Tiotropium | MED-022 | Throughout | 18 micrograms daily |

## 8. Policy Compliance Review (retrospective)

| Policy | Requirement | Observed | Result |
|---|---|---|---|
| PRO-004 v2 | Antibiotic within 60 minutes of alert; repeat lactate within 2 hours | 53 minutes; repeat at 1 h 45 min | Met under v2 (would not meet v3, 50 minutes) |
| PRO-015 | Rapid response escalation | Called 06:05, ICU 06:30 | Met |
| PRO-013 / FPA-11 | First vancomycin level before fourth dose | Level 30 minutes before dose 4 | Met |
| PRO-013 | De-escalation after susceptibilities | Within 5 hours of report | Met |
| PRO-012 / FPA-10 | Precautions started promptly; held 72 hours after resolution | Started 6 h 45 min after result; ended 2026-03-15 06:00 | Delay; INC-004 |

## 9. Laboratory Series (consolidated; official reports in LD-04, LD-05, LD-07, LD-08)

| Date | Lactate (mmol/L) | Procalcitonin (ng/mL) | CRP (mg/L) | Other |
|---|---|---|---|---|
| 2026-02-26 | 3.4 then 2.1 | 12.6 | 214 | ABG pH 7.28; blood cultures x2 |
| 2026-02-28 | n/a | n/a | 162 | Vancomycin level 14.8 mg/L |
| 2026-03-01 | n/a | 3.1 | 88 | Susceptibilities |
| 2026-03-05 | n/a | n/a | 31 | |
| 2026-03-07 | n/a | n/a | n/a | C. difficile toxin/PCR positive |

## 10. Follow-up After Discharge

Outpatient pulmonology review on 2026-04-08 (DEP-006): no recurrent diarrhea, SpO2 94% on room air. Repeat chest X-ray 2026-04-22 (LAB-020): consolidation resolved. A further review on 2026-08-11 recorded stable COPD with no exacerbation.

## 11. Other Records (non-diagnostic and background)

- Pneumococcal conjugate vaccine given 2026-04-08 after recovery.
- Smoking-cessation counseling 2026-04-08; patient remains abstinent.
- Nutrition review 2026-03-10: weight loss 5 kg during admission, high-protein supplements advised.
- Physiotherapy: pulmonary rehabilitation referral 2026-03-16, 8 sessions completed.
- Social history: lives with sister; independent in daily activities.

## 12. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| COPD diagnostic criteria; pneumonia severity and duration | DG-04, DG-05 |
| Sepsis bundle versions and effective dates | HO-03, HO-08 |
| Vancomycin monitoring; antibiotic monographs | MP-04, HO-04 |
| Blood culture organism and susceptibilities | LD-05 |
| Lactate, procalcitonin, CRP, ABG | LD-04 |
| Chest X-ray; spirometry | LD-07, LD-08 |
| Isolation rules | HO-06 |
| INC-004 review | HO-08 |

## 13. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic chart (Pass 1) |
