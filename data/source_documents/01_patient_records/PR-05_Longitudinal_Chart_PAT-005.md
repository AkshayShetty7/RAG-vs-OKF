---
doc_id: PR-05
title: "Longitudinal Chart: PAT-005 (Samuel Adeyemi-Clarke)"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-005, DIS-002, DIS-005, DIS-011, DIS-015, MED-005, MED-010, MED-011, MED-012, MED-021, MED-026, LAB-001, LAB-010, LAB-021, LAB-022, LAB-023, PRO-003, PRO-005, PRO-007, DEP-001, DEP-008, DEP-010, DEP-012, STF-010, ALG-003, FPA-04, FPA-07]
related_docs: [DG-01, DG-04, DG-06, HO-02, HO-03, HO-04, LD-02, LD-06, LD-07, MP-03, MP-05, MP-07]
---

# PR-05: Longitudinal Chart, PAT-005 (Samuel Adeyemi-Clarke)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-05 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Record period covered | 2012-06 (history) and 2024-02-06 to 2026-08-12 |
| Patient | PAT-005 |
| Primary services | DEP-008 Neurology (head STF-010); DEP-001; DEP-012 Radiology; DEP-010 |
| Reference guidelines | DG-06 (stroke, AF link), DG-01 (AF, hypertension), DG-04 (asthma) |
| Reference monographs | MP-03 (antithrombotics), MP-05 (albuterol, ibuprofen), MP-07 (allergy reference) |
| Policies applied | PRO-005 (stroke code), PRO-003 (allergy alert), PRO-007 (anticoagulation) |

## 2. Purpose and Scope

This chart follows PAT-005 through an acute ischemic stroke (DIS-011) on 2026-04-14 in a man who also has hypertension (DIS-002), asthma (DIS-015), and a documented hypersensitivity to aspirin and other NSAIDs (**ALG-003**). Atrial fibrillation (DIS-005) was first detected during the stroke admission. The chart records the stroke-code timing, the deliberate avoidance of aspirin (MED-010) and ibuprofen (MED-026), the use of clopidogrel (MED-011) as the initial antiplatelet, and the timed start of apixaban (MED-012).

## 3. Patient Summary

| Item | Value |
|---|---|
| Patient ID / name | PAT-005 / Samuel Adeyemi-Clarke (synthetic) |
| Date of birth / age | 1950-02-17 / 76 years (at 2026-10-01) |
| Sex | Male |
| Height / weight | 178 cm; 81 kg (2026-04-14) |
| Occupation | Retired ferry captain |
| Code status | Full code |

### 3.1 Allergy: ALG-003 (NSAIDs including aspirin)
In 2012 the patient developed wheeze, urticaria, and facial swelling about 30 minutes after taking aspirin 325 mg for a headache; he required emergency nebulized bronchodilator treatment. The pattern is a respiratory-type reaction associated with asthma. All NSAIDs, including aspirin (MED-010) and ibuprofen (MED-026), are therefore contraindicated (reaction definition and cross-reactivity rules in MP-07). Acetaminophen is tolerated.

## 4. Problem List

| Problem | ID | Onset | Status at 2026-08-12 |
|---|---|---|---|
| Acute ischemic stroke, left middle cerebral artery territory | DIS-011 | 2026-04-14 | Recovered; modified Rankin scale 1 |
| Atrial fibrillation (newly detected) | DIS-005 | 2026-04-14 | Persistent; rate controlled; on apixaban |
| Hypertension | DIS-002 | 2008 | Controlled on amlodipine |
| Asthma | DIS-015 | Childhood | Well controlled; no exacerbation in 2026 |

## 5. Medication History

| Medication | ID | Dose history | Notes |
|---|---|---|---|
| Amlodipine | MED-005 | 5 mg daily since 2008; 10 mg daily from 2026-04-20 | Blood pressure after stroke |
| Albuterol | MED-021 | Inhaler as needed | Used 2 to 3 times per month |
| Clopidogrel | MED-011 | 300 mg load 2026-04-14 20:10; 75 mg daily to 2026-04-18 | Stopped when apixaban started |
| Apixaban | MED-012 | 5 mg twice daily from 2026-04-19 08:30 | Dose-reduction criteria not met (see 7.4) |
| Aspirin | MED-010 | **Never given** this admission | ALG-003 |
| Ibuprofen | MED-026 | **Not prescribed** | ALG-003 |

## 6. Encounter Log

| Encounter | Date | Service | Key findings |
|---|---|---|---|
| ENC-005-01 | 2024-02-06 | Clinic | BP 148/88, amlodipine 5 mg; pulse regular |
| ENC-005-02 | 2025-03-18 | Clinic | Asthma review: well controlled |
| ENC-005-03 | 2026-04-14 to 2026-04-22 | DEP-001, DEP-008 | Stroke admission (section 7) |
| ENC-005-04 | 2026-05-20 | DEP-008 | Modified Rankin 1; BP 130/78 |
| ENC-005-05 | 2026-08-12 | DEP-008 | Stable; Holter confirms persistent AF with rate 72 |

## 7. Stroke Admission, 2026-04-14 to 2026-04-22 (ENC-005-03)

### 7.1 Stroke code timing (PRO-005, FPA-07)

Last known well: 17:50 on 2026-04-14. Onset: right arm weakness and slurred speech noticed by his wife.

| Clock time | Event |
|---|---|
| 18:55 | Arrival at DEP-001 (door time) |
| 18:58 | Stroke code activated |
| 19:14 | CT head non-contrast (LAB-022) begins: **19 minutes** after door time |
| 19:20 | CT read: no hemorrhage; early hypodensity in the left MCA territory (report in LD-07) |
| 19:35 | NIHSS 4 (was 9 at 19:00); deficits rapidly improving |
| 19:40 | Admission order set auto-populated aspirin 300 mg |
| 19:46 | Pharmacist cancelled the aspirin order after the PRO-003 allergy alert (ALG-003); no dose given |
| 20:10 | Clopidogrel 300 mg load given |

FPA-07 sets door-to-CT-head at 20 minutes. The result was 19 minutes: **met**. The stroke team (DEP-008) documented that reperfusion therapy was not pursued because the deficits improved rapidly (NIHSS 9 to 4 within 40 minutes of the first score). The order-set default was reported as a near-miss in the departmental log and did not reach the patient; it is not an incident in the INC series.

### 7.2 Diagnostic findings

- ECG on arrival (LAB-021): atrial fibrillation, ventricular rate 112. The AF diagnosis (DIS-005) was new.
- Complete blood count (LAB-001): hemoglobin 14.1 g/dL, platelets 232 x10^9/L. PT/INR (LAB-010) 1.0.
- Transthoracic echocardiogram (LAB-023) on 2026-04-16: LVEF 55%, left atrium moderately enlarged, no thrombus (report in LD-06).
- Repeat CT head (LAB-022) on 2026-04-18 (day 4): infarct as expected; **no hemorrhagic transformation**.

### 7.3 Antiplatelet choice
Aspirin is the standard first antiplatelet in DG-06, but it is contraindicated for PAT-005 because of ALG-003. Clopidogrel was chosen as the documented alternative (DG-06, MP-03, MP-07).

### 7.4 Anticoagulation timing and verification
DG-06 states that after a moderate stroke (NIHSS 5 to 15 at presentation) in a patient with atrial fibrillation, an anticoagulant is started between day 4 and day 7 if repeat imaging shows no hemorrhagic transformation. Day 0 was 2026-04-14. Imaging on day 4 was clear, so apixaban was ordered at 08:30 on 2026-04-19 (day 5) and clopidogrel was stopped (last dose 2026-04-18). The dose-reduction criteria in MP-03 were reviewed: age 76, weight 81 kg, creatinine 1.1 mg/dL; none of the three criteria was met, so 5 mg twice daily was used. FPA-04 requires pharmacist verification of new apixaban orders within 4 hours; verification was at 10:05, 95 minutes after the order: **met**.

### 7.5 Other management
Blood pressure was permitted to run higher for 48 hours, then amlodipine was raised to 10 mg on 2026-04-20. Albuterol was continued. Speech and physical therapy began on day 2. Discharged home on 2026-04-22 with outpatient rehabilitation.

## 8. Policy Compliance Review (retrospective)

| Policy | Requirement | Observed | Result |
|---|---|---|---|
| PRO-005 / FPA-07 | Door-to-CT-head within 20 minutes | 19 minutes | Met |
| PRO-003 | Allergy alert acted on before first dose | Aspirin cancelled 6 minutes after the order | Met (near-miss logged) |
| PRO-007 / FPA-04 | Pharmacist verification of apixaban order within 4 hours | 95 minutes | Met |
| DG-06 timing rule | Anticoagulant between day 4 and 7 after repeat CT | Started day 5 | Met |

## 9. Laboratory and Imaging Series (consolidated; official reports in LD-02, LD-06, LD-07)

| Date | Study | Result |
|---|---|---|
| 2026-04-14 | CBC | Hb 14.1 g/dL; platelets 232 |
| 2026-04-14 | INR | 1.0 |
| 2026-04-14 | ECG | Atrial fibrillation, rate 112 |
| 2026-04-14 | CT head | No hemorrhage; early left MCA hypodensity |
| 2026-04-16 | Echocardiogram | LVEF 55%; left atrial enlargement |
| 2026-04-18 | CT head | No hemorrhagic transformation |
| 2026-05-20 | CBC | Hb 13.8 g/dL |

## 10. Other Records (non-diagnostic and background)

- Influenza vaccine 2025-10-21; pneumococcal vaccine 2025-10-21.
- Hearing assessment 2025-03-18: mild age-related loss.
- Cataract grading 2025-07-02: early changes, observation only.
- Social history: lives with wife; two grandchildren nearby; non-smoker since 1998; alcohol rare.
- Driving suspended for one month after stroke; resumed 2026-05-20 after neurology clearance.

## 11. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Stroke secondary prevention and anticoagulation timing | DG-06 |
| Atrial fibrillation anticoagulation | DG-01 |
| NSAID and aspirin reaction definition, cross-reactivity | MP-07, MP-05, MP-03 |
| Apixaban and clopidogrel monographs | MP-03 |
| ECG and echocardiogram reports | LD-06 |
| CT head reports | LD-07 |
| CBC and INR reports | LD-02 |
| Stroke code pathway; allergy alert; anticoagulation protocol | HO-03, HO-02, HO-04 |

## 12. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic chart (Pass 1) |
