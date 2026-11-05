---
doc_id: PR-02
title: "Longitudinal Chart: PAT-002 (Priya Nandakumar)"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, DIS-002, DIS-005, DIS-006, DIS-018, DIS-022, MED-006, MED-009, MED-010, MED-011, MED-012, MED-028, MED-031, LAB-001, LAB-007, LAB-010, LAB-021, LAB-023, LAB-025, PRO-003, PRO-006, PRO-007, PRO-009, DEP-001, DEP-002, DEP-003, DEP-010, STF-005, ALG-002, FPA-04, FPA-08, FPA-13]
related_docs: [DG-01, DG-07, HO-02, HO-03, HO-04, HO-05, LD-02, LD-04, LD-06, MP-02, MP-03, MP-06, MP-07]
---

# PR-02: Longitudinal Chart, PAT-002 (Priya Nandakumar)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-02 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Record period covered | 2023-09-12 to 2026-08-20 |
| Patient | PAT-002 |
| Primary services | DEP-003 Cardiology (head STF-005); DEP-001 Emergency Medicine; DEP-010 Clinical Pharmacy |
| Reference guidelines | DG-01 (atrial fibrillation, ACS), DG-07 (GI bleeding, iron deficiency) |
| Reference monographs | MP-02 (pantoprazole, ferrous sulfate), MP-03 (antithrombotics), MP-06, MP-07 |
| Policies applied | PRO-003, PRO-006, PRO-007, PRO-009 (texts in HO-02, HO-03, HO-04, HO-05) |

## 2. Purpose and Scope

This chart follows PAT-002 through three connected events: paroxysmal atrial fibrillation (DIS-005) managed with an anticoagulant, a non-ST-elevation myocardial infarction (DIS-006) on 2025-03-03 treated with a coronary stent and combined antithrombotic therapy, and an upper gastrointestinal bleed (DIS-022) on 2025-05-19 with resulting iron-deficiency anemia (DIS-018). The central questions answered by this record are which antithrombotic agents were used when, why aspirin was stopped at discharge, and how bleeding was managed without abandoning stent protection.

## 3. Patient Summary

| Item | Value |
|---|---|
| Patient ID / name | PAT-002 / Priya Nandakumar (synthetic) |
| Date of birth / age | 1954-07-22 / 72 years (at 2026-10-01) |
| Sex | Female |
| Height / weight | 158 cm; 58 kg (2025-03-03), 57 kg (2025-05-19), 60 kg (2026-08-20) |
| Occupation | Retired school librarian |
| Hypertension (DIS-002) | Long-standing; controlled on metoprolol succinate; clinic BP 126/74 on 2026-08-20 |
| Code status | Full code |

### 3.1 Allergy

PAT-002 has **ALG-002 (sulfonamide antibiotics)**: generalized rash after trimethoprim-sulfamethoxazole in 2009. No sulfonamide antibiotic has been prescribed at MediCore. The allergy was entered in the allergy field on the first registration and was confirmed at each admission under PRO-003 (HO-02). Non-antibiotic sulfonamide handling is described in MP-07; PAT-002 takes no loop diuretic.

## 4. Problem List

| Problem | ID | Onset | Status at 2026-08-20 |
|---|---|---|---|
| Paroxysmal atrial fibrillation | DIS-005 | 2023-09-12 | Active; on apixaban |
| Hypertension | DIS-002 | Over 15 years | Controlled |
| Acute coronary syndrome (NSTEMI) | DIS-006 | 2025-03-03 | Stented; stable; clopidogrel completed |
| Upper GI bleeding (duodenal ulcer) | DIS-022 | 2025-05-19 | Healed on repeat endoscopy 2025-08-12 |
| Iron-deficiency anemia | DIS-018 | 2025-05-21 (ferritin 9 ng/mL) | Resolved; hemoglobin 12.4 g/dL on 2026-08-20 |

## 5. Medication History

| Medication | ID | Dose history | Notes |
|---|---|---|---|
| Apixaban | MED-012 | 5 mg twice daily from 2023-10-02; held 2025-03-03 to 2025-03-05 (pre-angiography); held 2025-05-19 to 2025-05-23 (bleeding); 5 mg twice daily otherwise | Full dose retained; see section 7.3 |
| Aspirin | MED-010 | 300 mg load 2025-03-03 then 81 mg daily until 2025-03-07; **stopped at discharge** | Limited peri-procedural course (5 days) |
| Clopidogrel | MED-011 | 300 mg load 2025-03-04 then 75 mg daily to 2025-09-04 | Six-month course after stent; continued during GI bleed |
| Metoprolol succinate | MED-006 | 50 mg daily to 2025-03-07; 100 mg daily from 2025-03-07 | Post-MI and rate control |
| Atorvastatin | MED-009 | 80 mg daily from 2025-03-04 | Started at NSTEMI |
| Pantoprazole | MED-028 | 40 mg daily from 2025-03-04 (GI protection); 80 mg IV bolus 2025-05-19 then 40 mg twice daily to 2025-07-15; 40 mg daily thereafter while on apixaban | See MP-02 |
| Ferrous sulfate | MED-031 | 325 mg daily from 2025-05-24 to 2025-08-24 | See MP-02 |

## 6. Encounter Log

| Encounter | Date | Service | Key findings |
|---|---|---|---|
| ENC-002-01 | 2023-09-12 | DEP-003 | Palpitations; ECG (LAB-021) paroxysmal AF on monitor, rate 118; AF diagnosed |
| ENC-002-02 | 2023-10-02 | DEP-003 | Apixaban 5 mg twice daily started; echo (LAB-023) LVEF 55% |
| ENC-002-03 | 2025-03-03 to 2025-03-07 | DEP-001 then DEP-003 | NSTEMI admission (section 7) |
| ENC-002-04 | 2025-04-15 | DEP-003 | Hb 12.3 g/dL; no bleeding; BP 124/72 |
| ENC-002-05 | 2025-05-19 to 2025-05-24 | DEP-001 then DEP-002 | Upper GI bleed admission (section 8) |
| ENC-002-06 | 2025-07-10 | DEP-003 | Hb 11.2 g/dL; ferritin 31 ng/mL |
| ENC-002-07 | 2025-08-12 | Endoscopy unit | Ulcer healed |
| ENC-002-08 | 2025-09-04 | DEP-003 | Clopidogrel completed and stopped; Hb 12.0 g/dL |
| ENC-002-09 | 2026-08-20 | DEP-003 | Stable; Hb 12.4 g/dL; ferritin 64 ng/mL; apixaban continued |

## 7. NSTEMI Admission, 2025-03-03 to 2025-03-07 (ENC-002-03)

### 7.1 Presentation and pathway timing (PRO-006, FPA-08)

PAT-002 presented to DEP-001 at 21:15 on 2025-03-03 with two hours of pressure-like chest discomfort radiating to the left arm.

| Time | Event | Pathway requirement |
|---|---|---|
| 21:15 (03-03) | Arrival | Start event |
| 21:22 | 12-lead ECG (LAB-021): sinus rhythm 84, ST depression 1 mm in V4 to V6 | ECG within 10 minutes: met (7 minutes) |
| 21:40 | hs-troponin 0 hour draw (LAB-007) | 0 and 2 hour series |
| 22:08 | Result verified: 48 ng/L; allergy ALG-002 confirmed at nursing intake | |
| 22:15 | Aspirin 300 mg load given | |
| 22:00 | Apixaban dose withheld pending angiography | |
| 23:42 | hs-troponin 2 hour draw (2 h 02 min after the 0 hour draw) | |
| 00:10 (03-04) | Result verified: 112 ng/L | |
| 00:20 | Result telephoned to the cardiology fellow, 10 minutes after verification | PRO-009 20-minute window: met |

### 7.2 Procedure and echo
Coronary angiography on 2025-03-04 at 10:30 (DEP-003) showed a 90% mid-left-anterior-descending stenosis treated with one drug-eluting stent. Clopidogrel 300 mg was loaded before the procedure. Echocardiogram on 2025-03-04 (LAB-023, LD-06): LVEF 50% with mild apical hypokinesis.

### 7.3 Antithrombotic decision and recorded rationale
Apixaban was resumed on 2025-03-05 at 08:00. The pharmacist-verification requirement for apixaban orders (FPA-04, 4 hours) was met: order entered 08:00, verified 09:12 (72 minutes). From 2025-03-05 to 2025-03-07 the patient therefore took three agents (apixaban, clopidogrel, aspirin 81 mg).

At discharge on 2025-03-07 the cardiology team **stopped aspirin and continued apixaban 5 mg twice daily with clopidogrel 75 mg daily**. The recorded rationale was: (1) DG-01 limits aspirin in patients with atrial fibrillation who need an anticoagulant to a peri-procedural course of no more than 7 days; aspirin had been given for 5 days; (2) the bleeding-risk score on the DG-01 rubric was 3 (age over 65, low body weight, hypertension), indicating elevated risk; (3) PRO-007 (HO-04) requires pharmacist review of any combination containing an anticoagulant and an antiplatelet, which was completed on 2025-03-06. The apixaban dose-reduction criteria in MP-03 were reviewed: only one of the three criteria was present (weight 58 kg; age under 80; creatinine 0.9 mg/dL with eGFR 72), so the full dose was kept. Clopidogrel was planned for six months to 2025-09-04.

### 7.4 Discharge medications (2025-03-07)
Apixaban 5 mg twice daily; clopidogrel 75 mg daily; metoprolol succinate 100 mg daily; atorvastatin 80 mg daily; pantoprazole 40 mg daily. Aspirin was not prescribed.

## 8. Upper GI Bleed Admission, 2025-05-19 to 2025-05-24 (ENC-002-05)

### 8.1 Presentation
Black stools for two days, light-headedness. Arrival at DEP-001 at 07:50 on 2025-05-19; BP 98/60, heart rate 112. Hemoglobin (LAB-001) 8.4 g/dL (baseline 12.3 g/dL on 2025-04-15). PT/INR (LAB-010) 1.1. Apixaban and clopidogrel were last taken on the morning of 2025-05-18.

### 8.2 Course

| Date | Events |
|---|---|
| 2025-05-19 | IV pantoprazole 80 mg bolus (MED-028) then 40 mg twice daily. Apixaban held. Clopidogrel continued because the stent was 11 weeks old (stent protection weighed against bleeding by cardiology and gastroenterology jointly, per DG-07). |
| 2025-05-20 | Hb 7.6 g/dL at 06:00 (nadir). Two units of red cells transfused. Upper endoscopy: 1.2 cm duodenal bulb ulcer with a visible vessel treated with endoscopic clips. H. pylori stool antigen negative. |
| 2025-05-21 | Hb 9.1 g/dL after transfusion. Ferritin (LAB-025) 9 ng/mL, transferrin saturation 6%: iron-deficiency anemia (DIS-018) confirmed against the DG-07 criteria. |
| 2025-05-23 | Hb stable 9.2 g/dL for 48 hours. Apixaban resumed 08:15, verified by the pharmacist 09:40 (85 minutes; FPA-04 met). |
| 2025-05-24 | Discharged on apixaban, clopidogrel, pantoprazole 40 mg twice daily, ferrous sulfate 325 mg daily (MED-031). Hb 9.4 g/dL. |

### 8.3 Follow-up
Hb 11.2 g/dL and ferritin 31 ng/mL on 2025-07-10; pantoprazole stepped down to 40 mg daily on 2025-07-15. Repeat endoscopy 2025-08-12: ulcer healed. Ferrous sulfate completed 2025-08-24. Hb 12.0 g/dL on 2025-09-04, when clopidogrel was stopped. On 2026-08-20 hemoglobin 12.4 g/dL, ferritin 64 ng/mL.

## 9. Policy Compliance Review (retrospective)

| Policy | Requirement | Observed | Result |
|---|---|---|---|
| PRO-006 / FPA-08 | ECG within 10 minutes; hs-troponin at 0 and 2 hours | ECG 7 minutes; troponin draws 2 h 02 min apart | Met |
| PRO-009 / FPA-13 | Critical result phoned within 20 minutes | 10 minutes (2025-03-04 00:20) | Met |
| PRO-007 / FPA-04 | Pharmacist verification of apixaban orders within 4 hours | 72 minutes and 85 minutes | Met |
| PRO-003 | Allergy flag verified at admission | ALG-002 confirmed 2025-03-03 and 2025-05-19 | Met |

## 10. Laboratory Series (consolidated; official reports in LD-02, LD-04, LD-06)

| Date | Hb (g/dL) | Ferritin (ng/mL) | hs-troponin (ng/L) | INR | Note |
|---|---|---|---|---|---|
| 2025-03-03 21:40 | 12.6 | n/a | 48 | n/a | 0 hour |
| 2025-03-04 00:10 | n/a | n/a | 112 | n/a | 2 hour |
| 2025-04-15 | 12.3 | n/a | n/a | n/a | Baseline |
| 2025-05-19 | 8.4 | n/a | n/a | 1.1 | Bleed |
| 2025-05-20 | 7.6 | n/a | n/a | n/a | Nadir |
| 2025-05-21 | 9.1 | 9 | n/a | n/a | Post-transfusion |
| 2025-07-10 | 11.2 | 31 | n/a | n/a | |
| 2025-09-04 | 12.0 | n/a | n/a | n/a | |
| 2026-08-20 | 12.4 | 64 | n/a | n/a | |

## 11. Other Records (non-diagnostic and background)

- Influenza vaccine 2024-10-11, 2025-10-09; shingles vaccine 2024-04-22.
- Bone-density screening 2025-02-18: osteopenia, no treatment.
- Cataract surgery right eye 2024-08-05, uncomplicated.
- Social history: lives alone, daughter nearby; walks 30 minutes daily; no tobacco; no alcohol.
- Dietitian 2025-06-02: iron-rich diet advice, tea separated from meals.

## 12. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Aspirin duration limit with an anticoagulant | DG-01 |
| Apixaban dose-reduction criteria, holding rules | MP-03 |
| Interaction of apixaban with clopidogrel/aspirin | MP-06 |
| Sulfonamide antibiotic allergy rules | MP-07 |
| GI bleed management; iron-deficiency criteria | DG-07 |
| Pantoprazole and ferrous sulfate monographs | MP-02 |
| Troponin, ferritin and hemoglobin reports | LD-02, LD-04 |
| ECG and echocardiogram | LD-06 |
| Chest-pain pathway; anticoagulation protocol | HO-03, HO-04 |

## 13. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic chart (Pass 1) |
