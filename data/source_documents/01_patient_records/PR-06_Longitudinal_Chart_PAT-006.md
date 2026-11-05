---
doc_id: PR-06
title: "Longitudinal Chart: PAT-006 (Grace Lindqvist-Obi)"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-006, DIS-010, DIS-012, DIS-021, MED-013, MED-014, MED-015, MED-020, MED-027, LAB-004, LAB-010, LAB-011, LAB-013, LAB-026, LAB-027, PRO-007, PRO-008, PRO-009, PRO-013, DEP-002, DEP-007, DEP-010, DEP-012, ALG-001, INC-003, FPA-05]
related_docs: [DG-05, DG-06, HO-02, HO-04, HO-05, HO-08, LD-02, LD-03, LD-05, LD-07, MP-03, MP-04, MP-06, MP-07]
---

# PR-06: Longitudinal Chart, PAT-006 (Grace Lindqvist-Obi)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-06 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Record period covered | 2025-08-12 to 2026-03-10 |
| Patient | PAT-006 |
| Primary services | DEP-002 Internal Medicine; DEP-010 Clinical Pharmacy (anticoagulation clinic); DEP-012 Radiology; DEP-007 Infectious Diseases (stewardship) |
| Reference guidelines | DG-06 (venous thromboembolism), DG-05 (complicated UTI) |
| Reference monographs | MP-03 (heparin, enoxaparin, warfarin), MP-04 (ciprofloxacin), MP-06, MP-07 |
| Policies applied | PRO-007, PRO-008, PRO-009, PRO-013 (HO-02, HO-04, HO-05) |
| Governance review | INC-003 (HO-08) |

## 2. Purpose and Scope

This chart records a pulmonary embolism (DIS-012) 17 days after right total knee replacement for osteoarthritis (DIS-021), the transition from parenteral heparin to warfarin, and a later urinary tract infection (DIS-010) in a patient with a **penicillin allergy (ALG-001)**. The UTI was treated with ciprofloxacin (MED-020), which interacts with warfarin (MED-013); the interaction alert was overridden, leading to a supratherapeutic INR and incident **INC-003**.

## 3. Patient Summary

| Item | Value |
|---|---|
| Patient ID / name | PAT-006 / Grace Lindqvist-Obi (synthetic) |
| Date of birth / age | 1963-04-25 / 63 years (at 2026-10-01) |
| Sex | Female |
| Height / weight | 167 cm; 78 kg (2025-08-29) |
| Occupation | Pharmacy technician (retired 2024) |
| Renal function | eGFR 74 mL/min/1.73 m2 (LAB-004, 2025-08-29); no renal dose reduction needed (PRO-008) |

### 3.1 Allergy: ALG-001 (penicillins)
Urticaria after an aminopenicillin in 2004; not anaphylaxis. Recorded in the allergy field at registration. Penicillin-class agents were avoided; this is why ciprofloxacin was chosen for the UTI. Cross-reactivity guidance for cephalosporins is in MP-07.

## 4. Problem List

| Problem | ID | Onset | Status at 2026-03-10 |
|---|---|---|---|
| Pulmonary embolism (provoked by surgery) | DIS-012 | 2025-08-29 | Treated; warfarin completed 2025-11-29 |
| Osteoarthritis, right knee (replaced), left knee (conservative) | DIS-021 | 2015 | Active, managed with acetaminophen |
| Complicated urinary tract infection | DIS-010 | 2025-10-21 | Resolved |

## 5. Medication History

| Medication | ID | Dose history | Notes |
|---|---|---|---|
| Acetaminophen | MED-027 | 650 mg every 6 hours as needed from 2025-08-12 | NSAIDs avoided because of anticoagulation |
| Heparin (unfractionated) infusion | MED-014 | 2025-08-29 16:10 to 2025-09-02 | aPTT-guided (LAB-011) |
| Warfarin | MED-013 | 5 mg daily from 2025-08-30; reduced to 4 mg daily from 2025-10-28; stopped 2025-11-29 | Target INR 2.0 to 3.0 (FPA-05) |
| Enoxaparin | MED-015 | 80 mg subcutaneous every 12 hours, 2025-09-02 to 2025-09-07 | 1 mg per kg; eGFR 74, no renal adjustment |
| Ciprofloxacin | MED-020 | 500 mg twice daily, 2025-10-21 to 2025-10-26 | See section 8; stopped early because of interaction harm |

## 6. Encounter Log

| Encounter | Date | Service | Key findings |
|---|---|---|---|
| ENC-006-01 | 2025-08-12 to 2025-08-15 | Surgical ward, DEP-002 co-management | Right total knee replacement, uncomplicated |
| ENC-006-02 | 2025-08-29 to 2025-09-03 | DEP-002 | Pulmonary embolism admission (section 7) |
| ENC-006-03 | 2025-09-07 | Anticoagulation clinic | INR 2.6; enoxaparin stopped |
| ENC-006-04 | 2025-10-20 | Anticoagulation clinic | INR 2.4 (baseline before infection) |
| ENC-006-05 | 2025-10-21 | Clinic | Urinary symptoms; ciprofloxacin prescribed |
| ENC-006-06 | 2025-10-26 | Clinic | Gum bleeding, bruising; INR 6.8 |
| ENC-006-07 | 2025-11-29 | Anticoagulation clinic | Course complete; warfarin stopped |
| ENC-006-08 | 2026-03-10 | Orthopedic follow-up | Right knee flexion 120 degrees |

## 7. Pulmonary Embolism, 2025-08-29 to 2025-09-03 (ENC-006-02)

### 7.1 Presentation and diagnosis
On 2025-08-29 (postoperative day 17) PAT-006 presented with pleuritic chest pain and dyspnea. Heart rate 104, SpO2 93% on room air, right calf swelling. D-dimer (LAB-026) was 3,850 ng/mL FEU. CT pulmonary angiogram (LAB-027) began at 14:40 and the report was issued at 15:25: segmental emboli in the right lower lobe, no right-heart strain (report in LD-07). Diagnosis per DG-06: elevated D-dimer followed by positive CTPA. The embolism was classified as provoked (major surgery).

### 7.2 Treatment

| Date | Action |
|---|---|
| 2025-08-29 16:10 | Unfractionated heparin infusion started (MED-014), aPTT monitoring (target 60 to 80 seconds); aPTT at 6 hours 72 s |
| 2025-08-30 | Warfarin 5 mg started (MED-013); heparin continued as overlap |
| 2025-09-02 | INR 1.6. Heparin stopped; enoxaparin 80 mg every 12 hours started (MED-015) because discharge was planned |
| 2025-09-03 | Discharged with enoxaparin and warfarin; INR 1.9 on 2025-09-04 |
| 2025-09-06 | INR 2.3 |
| 2025-09-07 | INR 2.6 on two consecutive checks at or above 2.0; enoxaparin stopped |

Total parenteral anticoagulation lasted 10 days (2025-08-29 to 2025-09-07), consistent with the minimum 5-day overlap and INR 2.0 or higher rule in HO-04 (PRO-007). DG-06 specifies a 3-month course for a provoked embolism.

## 8. Ciprofloxacin, Warfarin Interaction and INC-003

### 8.1 Timeline

| Date and time | Event |
|---|---|
| 2025-10-20 | Routine INR 2.4 |
| 2025-10-21 | Dysuria, urgency, temperature 38.1 C. Urinalysis (LAB-013) positive for nitrite and leukocyte esterase; culture sent. Classified as complicated (fever, recent hospitalization, anticoagulated). |
| 2025-10-21 17:30 | Ciprofloxacin 500 mg twice daily prescribed (MED-020). Penicillin-class drugs were avoided because of ALG-001. |
| 2025-10-21 17:32 | The PharmaSafe alert for ciprofloxacin with warfarin (interaction category in MP-06) was **overridden** with the comment "will monitor"; no INR order was placed. |
| 2025-10-23 | Culture: Escherichia coli, susceptible to ciprofloxacin and ceftriaxone, resistant to ampicillin (report in LD-05) |
| 2025-10-24 | Symptoms resolved |
| 2025-10-26 14:50 | Patient attended with gum bleeding and bruising; INR drawn |
| 2025-10-26 15:20 | Laboratory verified INR (LAB-010) **6.8** |
| 2025-10-26 15:36 | Result phoned to the clinic physician, 16 minutes after verification (PRO-009, within 20 minutes) |
| 2025-10-26 18:05 | Anticoagulation clinic nurse telephoned the patient, 2 hours 45 minutes after verification |

### 8.2 Management
Ciprofloxacin was stopped after 5 days. Stewardship (DEP-007, PRO-013) reviewed the course and accepted 5 days because symptoms had resolved and the interaction harm outweighed further benefit; a repeat urine culture on 2025-11-04 was negative. Warfarin was held on 2025-10-26 and 2025-10-27. INR was 4.1 on 2025-10-27, 3.2 on 2025-10-28, and 2.6 on 2025-10-29. Warfarin resumed on 2025-10-28 at 4 mg daily. Hemoglobin on 2025-10-26 was 12.9 g/dL; there was no major bleeding. The anticoagulation rule that an INR above 4.5 triggers a clinic call within 24 hours (FPA-05) was **met**. The overridden alert, with no INR plan, was reported as **INC-003** and reviewed in HO-08. Warfarin was completed on 2025-11-29 (about 3 months from 2025-08-29).

## 9. Policy Compliance Review (retrospective)

| Policy | Requirement | Observed | Result |
|---|---|---|---|
| PRO-007 | Parenteral overlap; INR 2.0 or higher before stopping parenteral therapy | 10 days overlap; INR 2.3 and 2.6 | Met |
| PRO-009 | Critical result phoned within 20 minutes | 16 minutes | Met |
| FPA-05 | INR above 4.5: clinic call within 24 hours | 2 h 45 min | Met |
| PRO-007 | INR recheck plan when an interacting drug is started | None ordered | Not met; INC-003 |
| PRO-008 | Renal dose check for enoxaparin | eGFR 74, no adjustment | Met |

## 10. Laboratory Series (consolidated; official reports in LD-02, LD-03, LD-05, LD-07)

| Date | INR | aPTT (s) | eGFR | Other |
|---|---|---|---|---|
| 2025-08-29 | 1.0 | 31 then 72 at 6 h | 74 | D-dimer 3,850 ng/mL FEU |
| 2025-09-02 | 1.6 | n/a | n/a | |
| 2025-09-04 | 1.9 | n/a | n/a | |
| 2025-09-06 | 2.3 | n/a | n/a | |
| 2025-09-07 | 2.6 | n/a | n/a | |
| 2025-10-20 | 2.4 | n/a | n/a | |
| 2025-10-26 | **6.8** | n/a | n/a | Hb 12.9 |
| 2025-10-27 | 4.1 | n/a | n/a | |
| 2025-10-28 | 3.2 | n/a | n/a | |
| 2025-10-29 | 2.6 | n/a | n/a | |

## 11. Other Records (non-diagnostic and background)

- Physiotherapy: 12 sessions after knee replacement, completed 2025-11-15.
- Influenza vaccine 2025-10-06.
- Dermatology: benign naevus reviewed 2025-12-02, no excision.
- Social history: lives with husband; walks with a cane for 6 weeks postoperatively; no tobacco; alcohol on weekends.

## 12. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| PE diagnosis and anticoagulation duration | DG-06 |
| Heparin, enoxaparin, warfarin monographs | MP-03 |
| Ciprofloxacin monograph; interaction with warfarin | MP-04, MP-06 |
| Penicillin allergy and cephalosporin cross-reactivity | MP-07 |
| INR, aPTT, D-dimer reports | LD-02 |
| Creatinine / eGFR report | LD-03 |
| Urine and culture reports | LD-05 |
| CTPA report | LD-07 |
| Anticoagulation protocol and stewardship | HO-04 |
| INC-003 review | HO-08 |

## 13. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic chart (Pass 1) |
