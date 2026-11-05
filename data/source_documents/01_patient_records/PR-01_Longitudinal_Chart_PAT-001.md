---
doc_id: PR-01
title: "Longitudinal Chart: PAT-001 (Marcus E. Doyle)"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, DIS-001, DIS-002, DIS-003, DIS-004, DIS-019, MED-001, MED-003, MED-004, MED-006, MED-007, MED-008, MED-009, LAB-002, LAB-003, LAB-004, LAB-005, LAB-008, LAB-021, LAB-023, PRO-008, PRO-009, PRO-011, PRO-014, PRO-016, DEP-001, DEP-002, DEP-003, DEP-005, DEP-010, STF-005, STF-007, ALG-001, ALG-006, INC-002, FPA-01, FPA-03, FPA-06, FPA-13]
related_docs: [DG-01, DG-02, DG-03, HO-02, HO-05, HO-07, HO-08, LD-01, LD-03, LD-04, LD-06, MP-01, MP-02, MP-06]
---

# PR-01: Longitudinal Chart, PAT-001 (Marcus E. Doyle)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-01 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Record period covered | 2024-01-18 to 2026-09-02 |
| Patient | PAT-001 |
| Primary service | DEP-002 Internal Medicine; co-managed by DEP-003 Cardiology (head STF-005) and DEP-005 Nephrology (head STF-007) |
| Reference guidelines | DG-01 (heart failure, hypertension), DG-02 (diabetes), DG-03 (CKD, hyperkalemia) |
| Reference monographs | MP-01, MP-02; interaction matrix MP-06 |
| Policies applied | PRO-008, PRO-009, PRO-011, PRO-016 (texts in HO-02, HO-05, HO-07) |
| Governance review | INC-002 (see HO-08) |

## 2. Purpose and Scope

This chart records three years of cardio-renal-metabolic care for PAT-001. It documents (a) the chronic management of type 2 diabetes (DIS-001), hypertension (DIS-002), chronic kidney disease (DIS-003), and heart failure with reduced ejection fraction (DIS-004); (b) the hyperkalemia admission of 2025-09-17 to 2025-09-20 (DIS-019, INC-002); and (c) the metformin renal-dose adjustment of 2025-03-13 under PRO-008. Policy values are cited, not defined, here; the authoritative text for each policy is in the HO documents named above.

## 3. Patient Summary

| Item | Value |
|---|---|
| Patient ID / name | PAT-001 / Marcus E. Doyle (synthetic) |
| Date of birth / age | 1959-03-14 / 67 years (at 2026-10-01) |
| Sex | Male |
| Height / weight | 175 cm; 92 kg (2024-01-18), 89 kg (2026-09-02) |
| Occupation | Retired municipal bus dispatcher |
| Primary care physician | Internal Medicine clinic, DEP-002 |
| Smoking / alcohol | Former smoker (stopped 2010); alcohol under 4 drinks per week |
| Code status | Full code; advance care planning note dated 2025-11-20 (section 12) |

## 4. Problem List

| Problem | ID | Onset | Status at 2026-09-02 |
|---|---|---|---|
| Type 2 diabetes mellitus | DIS-001 | 2014 | Active; HbA1c 7.0% on 2026-09-02 |
| Hypertension | DIS-002 | 2012 | Controlled; clinic BP 128/78 on 2026-09-02 |
| Chronic kidney disease, stage G3b | DIS-003 | Diagnosed 2021 as G3a; G3b from 2025-09-26 (second eGFR below 45 after recovery) | Active; eGFR 40 mL/min/1.73 m2 |
| Heart failure with reduced ejection fraction | DIS-004 | Diagnosed 2023 | Active; LVEF 38% on 2026-09-02 echocardiogram |
| Hyperkalemia (episode) | DIS-019 | 2025-09-17 | Resolved 2025-09-20; no recurrence |

## 5. Allergies and Intolerances

PAT-001 has **no known drug allergies**. This was verified with the patient at every encounter in section 7 (last verification 2026-09-02, ENC-001-14). No allergen class (ALG-001 to ALG-006) applies to PAT-001. No intolerance to any listed medication is documented.

## 6. Medication History

All medications were prescribed under DEP-002 or DEP-003 unless stated. Doses are fictional.

| Medication | ID | Dose history | Notes |
|---|---|---|---|
| Metformin | MED-001 | 1,000 mg twice daily (2,000 mg/day) from 2014 to 2025-03-13; **500 mg twice daily (1,000 mg/day) from 2025-03-13**; held 2025-09-17 to 2025-09-24 (sick-day rule); 500 mg twice daily from 2025-09-24 | Renal cap per PRO-008 (see section 9) |
| Lisinopril | MED-004 | 10 mg daily from 2016; 20 mg daily from 2024-11-05; **held 2025-09-17**; 5 mg daily from 2025-09-26; 10 mg daily from 2025-10-23 | ACE inhibitor for DIS-002 and DIS-004 |
| Metoprolol succinate | MED-006 | 50 mg daily from 2024-02-12; 100 mg daily from 2024-06-04 | Unchanged since 2024-06-04 |
| Furosemide | MED-007 | 40 mg daily (long-standing); held 2025-09-17 to 2025-09-19; 40 mg daily from 2025-09-20 | Loop diuretic for congestion |
| Spironolactone | MED-008 | 25 mg daily from 2024-06-04; **held 2025-09-17**; 12.5 mg daily from 2025-10-23 | Mineralocorticoid antagonist for DIS-004 |
| Atorvastatin | MED-009 | 40 mg daily from 2019 | Unchanged |

During the 2025-09-17 ED treatment, a single dose of regular insulin (MED-003) was given as part of hyperkalemia management (section 9). This was an administered dose, not a standing prescription.

## 7. Encounter Log

| Encounter | Date | Service | Key findings |
|---|---|---|---|
| ENC-001-01 | 2024-01-18 | DEP-002 clinic | BP 148/86; HbA1c 8.1% (65 mmol/mol); creatinine 142 umol/L, eGFR 49; K 4.7 mmol/L; metformin 1,000 mg twice daily continued |
| ENC-001-02 | 2024-02-12 | DEP-003 | Echocardiogram: LVEF 34%; NT-proBNP 1,850 pg/mL; metoprolol succinate 50 mg started |
| ENC-001-03 | 2024-06-04 | DEP-003 | K 4.6; metoprolol increased to 100 mg; spironolactone 25 mg started; safety BMP booked |
| ENC-001-04 | 2024-06-11 | Lab visit | K 4.9; creatinine 146 umol/L, eGFR 48 |
| ENC-001-05 | 2024-07-10 | DEP-002 | HbA1c 7.6%; K 4.8; creatinine 146, eGFR 48; weight 91 kg |
| ENC-001-06 | 2024-11-05 | DEP-003 | NT-proBNP 1,120 pg/mL; K 4.8; lisinopril increased to 20 mg |
| ENC-001-07 | 2025-02-20 | DEP-002 | HbA1c 7.4%; **creatinine 158 umol/L, eGFR 44**; K 4.9; metformin dose not yet changed |
| ENC-001-08 | 2025-03-13 | DEP-010 | Pharmacist renal-dose review: metformin reduced to 500 mg twice daily |
| ENC-001-09 | 2025-05-14 | DEP-002 | creatinine 160, eGFR 43; K 4.8; BP 134/80 |
| ENC-001-10 | 2025-09-17 to 2025-09-20 | DEP-001 then DEP-002 | Hyperkalemia admission (section 9) |
| ENC-001-11 | 2025-09-26 | HF clinic, DEP-003 | K 4.8; creatinine 158, eGFR 44; lisinopril restarted at 5 mg |
| ENC-001-12 | 2025-10-23 | Joint DEP-003 / DEP-005 | K 4.7; creatinine 164, eGFR 42; lisinopril 10 mg; spironolactone resumed at 12.5 mg |
| ENC-001-13 | 2025-11-20 | Lab visit and DEP-002 | K 4.8; advance care planning note |
| ENC-001-14 | 2026-04-08 | DEP-002 | HbA1c 7.1%; K 4.6; creatinine 170, eGFR 39; NT-proBNP 940 pg/mL |
| ENC-001-15 | 2026-09-02 | DEP-003 | Echocardiogram LVEF 38%; HbA1c 7.0%; K 4.7; creatinine 168, eGFR 40 |

(ENC-001-14 and ENC-001-15 are the 2026 visits referred to in section 5 and the problem list; the 2026-09-02 allergy verification occurred at ENC-001-15.)

## 8. Visit Narratives

### 8.1 ENC-001-01, 2024-01-18 (baseline visit)

Mr. Doyle attended for scheduled review. He reported stable exertional dyspnea at two flights of stairs and no orthopnea. Examination: BP 148/86, heart rate 74 regular, mild ankle edema, lungs clear. Laboratory results (LD-03): HbA1c 8.1%, creatinine 142 umol/L (eGFR 49 mL/min/1.73 m2, stage G3a at that time), potassium 4.7 mmol/L. Plan: refer to cardiology for echocardiography; continue metformin 1,000 mg twice daily (eGFR at that date was above the PRO-008 cap threshold of 45); repeat labs in 6 months.

### 8.2 ENC-001-02 and ENC-001-03, cardiology (2024-02-12, 2024-06-04)

The echocardiogram (LAB-023, report in LD-06) showed LVEF 34%, left ventricular end-diastolic diameter 6.1 cm, and mild functional mitral regurgitation. The 12-lead ECG (LAB-021) showed sinus rhythm at 76 beats per minute with a QRS duration of 108 ms. Dr. Rohan Deshmukh-Ellis (STF-005) started metoprolol succinate 50 mg, increased to 100 mg on 2024-06-04, and started spironolactone 25 mg on the same day, with a safety potassium and creatinine check booked at one week (ENC-001-04: K 4.9, eGFR 48). The guideline reference for these steps is DG-01.

### 8.3 ENC-001-06, 2024-11-05

NT-proBNP (LAB-008) fell from 1,850 to 1,120 pg/mL. Blood pressure remained above target at 142/84, so lisinopril was increased from 10 mg to 20 mg daily. Potassium 4.8 mmol/L was noted as acceptable but at the upper end of the clinic comfort range; a recheck at the next visit was requested. The potential for hyperkalemia with MED-004 plus MED-008 is described in MP-06 and MP-01.

### 8.4 ENC-001-07 to ENC-001-09, the metformin adjustment (2025-02-20 to 2025-05-14)

On 2025-02-20 creatinine was 158 umol/L, eGFR 44. Under PRO-008 (see HO-02), metformin is capped at 1,000 mg/day when eGFR is 30 to 44 (FPA-03). The PharmaSafe system generated a renal-dose advisory, but it was filed in the pharmacist work queue rather than the prescriber inbox. The dose therefore remained 2,000 mg/day for **21 days** until the pharmacist telephone review of 2025-03-13 (ENC-001-08), when the dose was reduced to 500 mg twice daily and the patient was counseled on sick-day rules. At ENC-001-09 (2025-05-14), eGFR 43 with metformin 1,000 mg/day was compliant. Metformin would be stopped if eGFR fell below 30; it has not.

### 8.5 ENC-001-11 and ENC-001-12, post-admission titration

After the hyperkalemia admission (section 9), the heart failure clinic restarted lisinopril cautiously at 5 mg (2025-09-26). On 2025-10-23 a joint cardiology and nephrology review (STF-005, STF-007) increased lisinopril to 10 mg and resumed spironolactone at half the previous dose (12.5 mg), with potassium checks at 1 and 4 weeks. The 4-week check on 2025-11-20 gave K 4.8 mmol/L. The renal rationale is in DG-03.

### 8.6 ENC-001-14 and ENC-001-15, 2026 follow-up

On 2026-04-08 HbA1c was 7.1%, NT-proBNP 940 pg/mL, creatinine 170 umol/L (eGFR 39). On 2026-09-02 the repeat echocardiogram (LAB-023) showed LVEF 38%; the ECG (LAB-021) showed sinus rhythm at 68 beats per minute, QRS 108 ms. HbA1c 7.0%, K 4.7, creatinine 168 umol/L (eGFR 40). Allergy status re-verified as none. No medication changes were made. The next review is booked for 2027-03.

## 9. Hyperkalemia Admission, 2025-09-17 to 2025-09-20 (ENC-001-10, INC-002)

### 9.1 Background

For three days before presentation, Mr. Doyle had vomiting and diarrhea with poor oral intake. He continued lisinopril 20 mg, spironolactone 25 mg, furosemide 40 mg, and metformin. He presented to the Emergency Department (DEP-001) on 2025-09-17 with generalized weakness and palpitations.

### 9.2 Timeline

| Time (2025-09-17) | Event |
|---|---|
| 07:20 | Arrival at DEP-001 triage |
| 07:42 | Blood drawn (BMP, LAB-002; potassium, LAB-005); specimen labeled under PRO-014 |
| 07:50 | 12-lead ECG (LAB-021): peaked T waves, PR 224 ms, QRS 112 ms |
| 08:05 | LabLink verifies **potassium 6.4 mmol/L** (critical; FPA-01 threshold 6.2 or higher); creatinine 176 umol/L, eGFR 38; sodium 134 mmol/L |
| 08:41 | Result telephoned to the ED physician with read-back, **36 minutes after verification** (policy window 20 minutes, FPA-13) |
| 08:50 | Membrane stabilization given per the DG-03 hyperkalemia algorithm |
| 08:58 | Regular insulin 10 units IV (MED-003) with dextrose 25 g |
| 10:15 | K 5.6 mmol/L |
| 13:00 | K 5.3 mmol/L; admitted to DEP-002 |

Lisinopril, spironolactone, furosemide, and metformin were held. The 36-minute interval between verification and notification was reported and reviewed as **INC-002** (HO-05 describes the notification protocol PRO-009; HO-08 records the review).

### 9.3 Course and discharge

| Date | K (mmol/L) | Creatinine (umol/L) / eGFR | Comment |
|---|---|---|---|
| 2025-09-18 06:00 | 5.1 | 168 / 40 | Oral fluids tolerated |
| 2025-09-19 06:00 | 4.9 | 164 / 41 | Furosemide restarted 2025-09-20 |
| 2025-09-20 06:00 | 4.8 | 163 / 41 | Discharged |

Discharge planning followed PRO-011 (HO-07). Because PAT-001 has heart failure, the heart-failure follow-up protocol PRO-016 also applied: the 48-hour telephone call was completed on 2025-09-22 and the clinic visit on 2025-09-26, both within FPA-06 limits (48 hours and 7 days). Metformin was resumed on 2025-09-24 at 500 mg twice daily.

## 10. Policy Compliance Review (retrospective)

| Policy | Requirement (source) | Observed in this chart | Result |
|---|---|---|---|
| PRO-008 | Metformin cap 1,000 mg/day at eGFR 30-44 (FPA-03; HO-02) | Cap applied 2025-03-13; 21 days after the qualifying eGFR on 2025-02-20 | Delayed implementation (not an incident) |
| PRO-009 | Critical result phoned within 20 minutes (FPA-13; HO-05) | 36 minutes on 2025-09-17 | Not met; INC-002 |
| PRO-011 | Discharge planning (HO-07) | Documented 2025-09-20 | Met |
| PRO-016 | Call within 48 hours; visit within 7 days (FPA-06; HO-07) | Call day 2; visit day 6 | Met |

## 11. Laboratory Series (consolidated; official reports in LD-03 and LD-04)

Columns: HbA1c (LAB-003), potassium (LAB-005), creatinine and eGFR (LAB-004, with BMP LAB-002), NT-proBNP (LAB-008).

| Date | HbA1c (%) | K (mmol/L) | Creatinine (umol/L) | eGFR | NT-proBNP (pg/mL) |
|---|---|---|---|---|---|
| 2024-01-18 | 8.1 | 4.7 | 142 | 49 | n/a |
| 2024-02-12 | n/a | n/a | n/a | n/a | 1,850 |
| 2024-06-11 | n/a | 4.9 | 146 | 48 | n/a |
| 2024-07-10 | 7.6 | 4.8 | 146 | 48 | n/a |
| 2024-11-05 | n/a | 4.8 | n/a | n/a | 1,120 |
| 2025-02-20 | 7.4 | 4.9 | 158 | 44 | n/a |
| 2025-05-14 | n/a | 4.8 | 160 | 43 | n/a |
| 2025-09-17 | n/a | 6.4 | 176 | 38 | n/a |
| 2025-09-26 | n/a | 4.8 | 158 | 44 | n/a |
| 2025-10-23 | n/a | 4.7 | 164 | 42 | n/a |
| 2025-11-20 | n/a | 4.8 | n/a | n/a | n/a |
| 2026-04-08 | 7.1 | 4.6 | 170 | 39 | 940 |
| 2026-09-02 | 7.0 | 4.7 | 168 | 40 | n/a |

## 12. Other Records (non-diagnostic and background)

These entries are included for completeness and are not related to the diagnoses above.

- **Immunizations:** influenza vaccine 2024-10-15 and 2025-10-10; pneumococcal vaccine 2024-10-15.
- **Eye and foot screening:** retinal screening 2025-03-04 showed no retinopathy; foot examination 2025-03-04 showed intact sensation.
- **Dietitian visit** 2024-09-02: sodium restriction to 2 g/day and fluid advice of 1.5 L/day were reinforced.
- **Social history:** lives with spouse; two adult children; drives short distances; no reported falls.
- **Advance care planning** (2025-11-20): the patient named his spouse as healthcare proxy and confirmed full treatment.
- **Dental:** routine cleaning 2026-02-11; no antibiotic prophylaxis indicated.

## 13. Cross-Reference Table

| Topic in this chart | Where to verify |
|---|---|
| Metformin renal cap and sick-day rules | MP-02 (monograph), HO-02 (PRO-008), DG-03 |
| ACE inhibitor plus spironolactone hyperkalemia risk | MP-06, MP-01, DG-03 |
| Critical potassium threshold and call window | LD-01, HO-05 |
| Lab reports for K, creatinine, HbA1c | LD-03 |
| NT-proBNP reports | LD-04 |
| ECG and echocardiogram reports | LD-06 |
| Heart-failure follow-up requirements | HO-07 |
| INC-002 review | HO-08 |

## 14. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic chart (Pass 1) |
