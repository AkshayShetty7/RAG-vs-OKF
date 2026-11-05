---
doc_id: PR-08
title: "Admission Casebook B: PAT-011, PAT-012, PAT-013, PAT-014"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-003, PAT-007, PAT-011, PAT-012, PAT-013, PAT-014, DIS-001, DIS-004, DIS-005, DIS-008, DIS-009, DIS-010, DIS-016, DIS-017, DIS-018, MED-001, MED-006, MED-007, MED-008, MED-013, MED-016, MED-017, MED-018, MED-019, MED-024, MED-031, LAB-001, LAB-004, LAB-008, LAB-010, LAB-012, LAB-013, LAB-014, LAB-015, LAB-016, LAB-017, LAB-020, LAB-021, LAB-023, LAB-025, PRO-004, PRO-007, PRO-008, PRO-011, PRO-013, PRO-016, DEP-001, DEP-003, DEP-007, DEP-010, DEP-014, INC-006, FPA-02, FPA-03, FPA-05, FPA-06, FPA-09, FPA-11, FPA-14]
related_docs: [DG-01, DG-02, DG-03, DG-04, DG-05, DG-07, HO-03, HO-04, HO-07, HO-08, LD-02, LD-03, LD-04, LD-05, LD-06, MP-01, MP-02, MP-03, MP-04, MP-06, PR-01, PR-03, PR-06, PR-07]
---

# PR-08: Admission Casebook B (PAT-011, PAT-012, PAT-013, PAT-014)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-08 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Contents | Four shorter admission charts, one per patient (sections 3 to 6) |
| Reference guidelines | DG-01, DG-02, DG-03, DG-04, DG-05, DG-07 |
| Reference monographs | MP-01, MP-02, MP-03, MP-04, MP-06 |
| Policies applied | PRO-004, PRO-007, PRO-008, PRO-011, PRO-013, PRO-016 (HO-03, HO-04, HO-07) |
| Governance review | INC-006 (HO-08) |

## 2. Purpose and Scope

This casebook holds four patients: a heart-failure readmission with a missed follow-up call in a man on warfarin (PAT-011, INC-006), a non-severe pneumonia treated with a short, stewardship-guided course (PAT-012), urosepsis with acute kidney injury and pharmacy-managed vancomycin (PAT-013), and iron-deficiency anemia complicated by a levothyroxine absorption problem (PAT-014). Facts are specific to each patient; several features deliberately resemble charts in PR-01, PR-03, PR-06 and PR-07 and must not be confused with them. Laboratory values are given inline unless a separate report is cited.

## 3. PAT-011: Walter Brennan-Osei (INC-006)

| Item | Value |
|---|---|
| Date of birth / age | 1948-04-02 / 78 years; male |
| Weight | Dry weight 76.0 kg at 2026-01-17 discharge |
| Problems | Heart failure with reduced ejection fraction (DIS-004); atrial fibrillation (DIS-005) |
| Allergy | None known |
| Medications | Furosemide (MED-007), spironolactone 25 mg daily (MED-008), metoprolol succinate 50 mg daily (MED-006), warfarin (MED-013) with default INR target 2.0 to 3.0 |

### 3.1 First admission, 2026-01-12 to 2026-01-17 (ENC-011-01)
Admitted with three weeks of worsening dyspnea, orthopnea, and edema; weight 79.8 kg. NT-proBNP (LAB-008) 4,820 pg/mL. ECG (LAB-021): atrial fibrillation, rate 96. Echocardiogram (LAB-023, LD-06) on 2026-01-13: LVEF 30%. INR (LAB-010) 2.6. Potassium 4.5 mmol/L, eGFR 52. Intravenous furosemide produced a 3.8 kg loss; at discharge furosemide was increased from 40 mg daily to 40 mg twice daily. Discharged **2026-01-17 at 14:30**.

### 3.2 Follow-up obligations after discharge (PRO-011, PRO-016, PRO-007)

| Obligation | Rule (source) | Deadline from discharge time |
|---|---|---|
| Phone call | Within 48 hours (FPA-06; HO-07) | 2026-01-19 14:30 |
| Clinic visit | Within 7 days (FPA-06; HO-07) | 2026-01-24 14:30 |
| INR check | Within 72 hours of discharge (FPA-05; HO-04) | 2026-01-20 14:30 |

### 3.3 What happened (INC-006)
- The discharge contact number had two digits transposed. The single call attempt on 2026-01-19 at 11:05 reached a wrong number; no second attempt was made and no escalation to the emergency contact occurred.
- The clinic appointment for 2026-01-23 was missed (no-show) and no outreach followed.
- No INR check took place within 72 hours.
The HF follow-up calls (DEP-014, with clinical co-ownership by DEP-003) therefore **did not meet** FPA-06. Review of the incident is in HO-08.

### 3.4 Readmission, 2026-02-02 to 2026-02-08 (ENC-011-02)
Returned 16 days after discharge with dyspnea and weight 80.1 kg (4.1 kg above dry weight). NT-proBNP 5,300 pg/mL. INR **3.4**, above the 2.0 to 3.0 target. Warfarin was reduced from 4 mg to 3.5 mg daily and an INR recheck was set for 2026-02-05 (3 days), when INR was 2.8. Diuresis resumed; furosemide 40 mg twice daily continued; spironolactone continued (K 4.6). The patient reported a high-salt diet and missing two metoprolol doses per week.

Discharged **2026-02-08 at 11:00** with all three obligations met: call completed 2026-02-09 at 09:30 (22 hours 30 minutes), INR 2.6 on 2026-02-10, clinic visit 2026-02-12 (4 days). The case is the principal example of a missed heart-failure follow-up in this dataset; PAT-001 (PR-01) in contrast completed all follow-up on time.

## 4. PAT-012: Mei-Ling Castellanos

| Item | Value |
|---|---|
| Date of birth / age | 1965-02-18 / 61 years; female |
| Problems | Community-acquired pneumonia (DIS-008); type 2 diabetes (DIS-001) |
| Allergy | **None known**; tolerated amoxicillin-clavulanate with no reaction |
| Medications | Metformin 500 mg twice daily (MED-001), amoxicillin-clavulanate 875/125 mg twice daily (MED-016) |

### 4.1 Admission, 2026-05-05 to 2026-05-08
Admitted 2026-05-05 with fever 38.5 C, productive cough, and right-sided pleuritic pain; no sepsis alert was triggered (PRO-004 not activated). Chest X-ray (LAB-020): right middle lobe infiltrate. Procalcitonin (LAB-015) **0.42 ng/mL**; C-reactive protein (LAB-016) 96 mg/L; eGFR 82; HbA1c 7.4%. Because PAT-012 has **no allergy flag**, the dual-verification rule (FPA-09) did not apply; the first dose of amoxicillin-clavulanate was given at 13:20 on 2026-05-05 after standard verification. Compare PAT-007 (PR-07).

### 4.2 Course and stewardship decision
Afebrile since 06:00 on 2026-05-06. Procalcitonin on 2026-05-07 was **0.18 ng/mL**. Under DG-05 a non-severe pneumonia in a clinically stable patient is treated for a minimum of 5 days; under the stewardship rule in HO-04 (PRO-013), antibiotics may stop at day 5 when procalcitonin is below 0.25 ng/mL and the patient has been afebrile for at least 48 hours. Both conditions were met, and antibiotics were stopped after the final dose on **2026-05-09 (day 5)**. Metformin was continued (eGFR above the FPA-03 renal band). Discharged 2026-05-08. Follow-up chest X-ray on 2026-06-19 was clear.

## 5. PAT-013: Daniel Oyelaran-Whitfield

| Item | Value |
|---|---|
| Date of birth / age | 1960-09-04 / 66 years; male |
| Weight | 82 kg |
| Problems | Complicated UTI with obstruction from benign prostate enlargement (DIS-010); sepsis (DIS-009); acute kidney injury (DIS-017) |
| Allergy | None known |
| Medications | Piperacillin-tazobactam (MED-018), vancomycin (MED-019), ceftriaxone (MED-017) |

### 5.1 Sepsis bundle, 2026-06-18 (PRO-004 version 3)
The bundle in force on this date was **version 3**: first antibiotic within 50 minutes of the sepsis alert (FPA-02; effective 2026-03-01).

| Clock time | Event |
|---|---|
| 03:40 | Arrival at DEP-001 with fever, rigors, and urinary retention |
| 04:10 | Sepsis alert (temperature 39.2 C, heart rate 118, BP 92/54) |
| 04:20 | Lactate (LAB-014) 3.0 mmol/L |
| 04:25 | Blood cultures (LAB-012) and urine culture (LAB-013) drawn |
| 04:52 | First antibiotic: piperacillin-tazobactam 4.5 g IV (MED-018), **42 minutes** after the alert |
| 05:50 | Repeat lactate 1.7 mmol/L (within 2 hours of the first) |

Compliance with version 3: **met** (42 minutes against 50). A urinary catheter was placed with 650 mL drained.

### 5.2 Vancomycin and renal function (PRO-013, PRO-008, FPA-11)
Vancomycin IV (MED-019) was started for early gram-positive cover, pharmacy-managed (DEP-010). Creatinine and eGFR (LAB-004) rose after admission, with piperacillin-tazobactam plus vancomycin as a recognized nephrotoxicity pairing (MP-06).

| Date | Creatinine mg/dL (umol/L) | eGFR | Actions |
|---|---|---|---|
| Baseline 2025-11 | 1.0 (88) | 79 | |
| 2026-06-18 | 1.9 (168) | 38 | |
| 2026-06-19 | 2.3 (203) | 30 | Piperacillin-tazobactam reduced to 3.375 g every 6 h (PRO-008 tier) |
| 2026-06-20 | 1.8 (159) | 40 | |
| 2026-06-22 | 1.3 (115) | 59 | |

The peak of 2.3 mg/dL is 2.3 times baseline: AKI stage 2 (DG-03).

| Vancomycin dose | Time | Dose |
|---|---|---|
| 1 | 2026-06-18 05:10 | 1,250 mg |
| 2 | 2026-06-18 17:10 | 1,000 mg |
| 3 | 2026-06-19 05:10 | 1,000 mg |
| Level | 2026-06-19 16:40 | **24.1 mg/L**, drawn 30 minutes before dose 4 (due 17:10) |
| 4 | Held | Pharmacy changed to 1,000 mg every 24 h |
| Final dose | 2026-06-20 05:10 | 1,000 mg; stopped at 12:00 |

FPA-11 requires the first level before the fourth dose: **met**. Vancomycin was stopped at 12:00 on 2026-06-20 after cultures grew gram-negative bacilli only (stewardship, DEP-007).

### 5.3 Culture-directed therapy
Blood and urine cultures grew Escherichia coli, susceptible to piperacillin-tazobactam and ceftriaxone, non-ESBL (report in LD-05). Piperacillin-tazobactam ran from 2026-06-18 to 2026-06-20; ceftriaxone 2 g IV daily from 2026-06-21 to 2026-06-24 completed 7 days (DG-05). Discharged 2026-06-24 at 17:00 with outpatient urology follow-up. Compare PAT-003 (PR-03), also treated with vancomycin but under sepsis bundle version 2.

## 6. PAT-014: Ingrid Solheim-Banerjee

| Item | Value |
|---|---|
| Date of birth / age | 1971-06-15 / 55 years; female |
| Problems | Iron-deficiency anemia (DIS-018); hypothyroidism (DIS-016) |
| Allergy | None known |
| Medications | Levothyroxine 100 micrograms daily (MED-024) since 2018; ferrous sulfate 325 mg daily (MED-031) from 2026-04-07 |

### 6.1 Diagnosis, 2026-03-30
Fatigue for four months. Hemoglobin (LAB-001) **9.8 g/dL**, MCV 71 fL; ferritin (LAB-025) **7 ng/mL**; TSH (LAB-017) 2.4 mIU/L. DG-07 defines iron-deficiency anemia in women as hemoglobin below 12.0 g/dL with ferritin below 15 ng/mL; both criteria were met. Upper endoscopy and colonoscopy on 2026-04-20 showed mild gastritis and no bleeding source. Heavy perimenopausal menstrual bleeding was identified as the likely source and managed by gynecology (a non-registry service).

### 6.2 The levothyroxine problem
Ferrous sulfate was started 2026-04-07, taken at 07:00, 30 minutes after levothyroxine at 06:30. On 2026-05-12 TSH was **8.9 mIU/L** although the levothyroxine dose had not changed. The cause was reduced levothyroxine absorption from co-administered iron (MP-06, MP-02). Under FPA-14 the two must be separated by at least 4 hours. The schedule was changed to **levothyroxine at 06:30 and ferrous sulfate at 14:00** (7.5 hours apart). TSH on 2026-07-14 was 3.2 mIU/L, with no change in levothyroxine dose.

### 6.3 Response
On 2026-07-14: hemoglobin 12.4 g/dL, ferritin 38 ng/mL. On 2026-09-18: hemoglobin 12.9 g/dL, ferritin 61 ng/mL, TSH 3.0. Iron continues until 2026-10-14 (three months after hemoglobin normalized).

## 7. Policy Compliance Review (retrospective)

| Patient | Policy | Observed | Result |
|---|---|---|---|
| PAT-011 | PRO-016 / FPA-06 call within 48 h and visit within 7 days (first discharge) | No call reached; visit missed | Not met; INC-006 |
| PAT-011 | PRO-007 / FPA-05 INR within 72 h of discharge (first discharge) | Not done | Not met |
| PAT-011 | FPA-06 and FPA-05 (second discharge) | Call 22 h 30 min; INR day 2; visit day 4 | Met |
| PAT-012 | PRO-013 stop rule at day 5 | PCT 0.18; afebrile 48 h or more | Met |
| PAT-013 | PRO-004 v3, antibiotic within 50 minutes | 42 minutes | Met |
| PAT-013 | PRO-013 / FPA-11 level before dose 4 | 30 minutes before dose 4 | Met |
| PAT-014 | FPA-14 4-hour separation | Initially 30 minutes; corrected to 7.5 hours | Corrected after TSH rise |

## 8. Other Records (non-diagnostic and background)

- PAT-011: retired bus mechanic; influenza vaccine 2025-10-22; hearing aids; daughter is the emergency contact (listed with the correct number only after 2026-02-02).
- PAT-012: office manager; retinal screening 2025-09-09 normal; influenza vaccine 2025-10-09.
- PAT-013: retired surveyor; urology review 2026-08-04 recommended elective prostate procedure; PSA not in registry.
- PAT-014: school administrator; dietitian visit 2026-04-14; vitamin C with iron advised, tea separated.

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| HF algorithm; warfarin with AF | DG-01, MP-03 |
| HF follow-up rules; INC-006 review | HO-07, HO-04, HO-08 |
| INR, ferritin, hemoglobin reports | LD-02 |
| Creatinine and TSH reports | LD-03 |
| Procalcitonin, CRP, lactate | LD-04 |
| Culture reports | LD-05 |
| Echo and ECG | LD-06 |
| Pneumonia and UTI durations; stewardship stop rule | DG-05, HO-04 |
| Vancomycin monitoring; amoxicillin-clavulanate, piperacillin-tazobactam monographs | MP-04 |
| Levothyroxine-iron interaction; ferrous sulfate monograph | MP-06, MP-02 |
| Sepsis bundle versions | HO-03, HO-08 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic casebook (Pass 1) |
