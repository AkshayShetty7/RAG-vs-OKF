---
doc_id: PR-07
title: "Admission Casebook A: PAT-007, PAT-008, PAT-009, PAT-010"
folder: 01_Patient_Records
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-007, PAT-008, PAT-009, PAT-010, PAT-012, DIS-002, DIS-003, DIS-006, DIS-010, DIS-014, DIS-015, DIS-017, DIS-020, DIS-021, DIS-022, DIS-024, MED-004, MED-006, MED-007, MED-009, MED-010, MED-011, MED-016, MED-017, MED-021, MED-025, MED-026, MED-027, MED-028, MED-029, LAB-001, LAB-002, LAB-004, LAB-007, LAB-013, LAB-019, LAB-021, LAB-023, PRO-001, PRO-003, PRO-006, PRO-008, PRO-009, DEP-001, DEP-003, DEP-009, ALG-001, ALG-004, ALG-006, INC-001, INC-005, FPA-08, FPA-09]
related_docs: [DG-01, DG-03, DG-04, DG-07, DG-08, HO-02, HO-03, HO-05, HO-08, LD-03, LD-04, LD-05, LD-06, LD-08, MP-01, MP-03, MP-04, MP-05, MP-06, MP-07, PR-01, PR-02, PR-08]
---

# PR-07: Admission Casebook A (PAT-007, PAT-008, PAT-009, PAT-010)

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every person, record, value, date, and event in this document are fictional. This document exists only for software benchmarking and education. It is not a real medical record, it contains no real patient information, and nothing in it is clinical guidance. Policy values cited from MediCore protocols are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | PR-07 |
| Folder | 01_Patient_Records |
| Version / date | 1.0 / 2026-10-01 |
| Contents | Four shorter admission charts, one per patient (sections 3 to 6) |
| Reference guidelines | DG-01, DG-03, DG-04, DG-07, DG-08 |
| Reference monographs | MP-01, MP-03, MP-04, MP-05, MP-06, MP-07 |
| Policies applied | PRO-001, PRO-003, PRO-006, PRO-008, PRO-009 (HO-02, HO-03, HO-05) |
| Governance reviews | INC-001 and INC-005 (HO-08) |

## 2. Purpose and Scope

This casebook holds four patients selected for distinct medication-safety lessons: a penicillin anaphylaxis incident (PAT-007, INC-001), an acute coronary syndrome in a man who cannot take ACE inhibitors (PAT-008), acute kidney injury on chronic kidney disease after an NSAID prescription (PAT-009, INC-005), and a gastrointestinal bleed on an SSRI combined with two antiplatelet-acting drugs (PAT-010). Each patient has an independent allergy and medication profile; do not combine facts between sections. Laboratory values for these patients are given inline unless a separate report is cited.

## 3. PAT-007: Hannah Whitcombe-Rao (INC-001)

| Item | Value |
|---|---|
| Date of birth / age | 1992-02-11 / 34 years; female |
| Weight | 64 kg |
| Problems | Asthma (DIS-015); anaphylaxis to amoxicillin-clavulanate on 2026-05-17 (DIS-024) |
| Allergy | **ALG-001 (penicillins)**, severity upgraded to anaphylaxis on 2026-05-17 |
| Medications | Albuterol as needed (MED-021); amoxicillin-clavulanate (MED-016) given in error; epinephrine (MED-029) |

### 3.1 Allergy flag before the event
At registration in 2024-09 the patient reported a childhood rash to a penicillin. It was entered in the allergy field as "Penicillins: rash, patient-reported, unverified." The low severity and "unverified" status led staff to treat the flag as low risk.

### 3.2 Event timeline, 2026-05-17

| Clock time | Event |
|---|---|
| 18:40 | Arrival at DEP-001 with an asthma exacerbation and fever 38.2 C with purulent sputum |
| 19:10 | Albuterol nebulization, prednisone 40 mg |
| 20:30 | ED physician ordered amoxicillin-clavulanate 875/125 mg orally for a suspected bacterial respiratory infection |
| 20:48 | Pharmacist verified the order and recorded the allergy flag |
| 21:05 | Nurse administered the first dose. The independent nursing check required by FPA-09 (dual verification for a first beta-lactam dose in a patient with any allergy flag) was **not performed**; the bar-code "urgent override" function was used |
| 21:17 | Urticaria, lip swelling, wheeze |
| 21:19 | BP 82/48, heart rate 128; **epinephrine 0.5 mg intramuscular** (MED-029) given |
| 21:27 | Second epinephrine 0.5 mg intramuscular dose; IV fluids; nebulized albuterol |
| 21:40 | BP 104/62, wheeze improving |
| 22:30 | Transferred to DEP-009 for observation |

### 3.3 Outcome and follow-up
The patient stayed 24 hours in the ICU, then on a ward. She was discharged on 2026-05-19 with an epinephrine auto-injector prescription (MED-029) and a revised allergy entry: **ALG-001, anaphylaxis, confirmed 2026-05-17**; cephalosporin cross-reactivity cautions were added per MP-07. Allergy clinic referral was made. Spirometry (LAB-019) on 2026-06-23 (LD-08): FEV1 82% of predicted, FEV1/FVC 0.78, bronchodilator reversibility 14%, supporting well-controlled asthma. The event was reported as **INC-001**; the review, the change to PRO-003 (a hard stop on override of the dual-verification step for beta-lactams, effective 2026-07-01), and the audit findings are in HO-08. Contrast this case with PAT-012 in PR-08, who tolerated the same antibiotic and has no allergy flag.

## 4. PAT-008: Robert Chaudhary-Lowe

| Item | Value |
|---|---|
| Date of birth / age | 1957-08-30 / 69 years; male |
| Weight | 88 kg |
| Problems | Acute coronary syndrome, NSTEMI (DIS-006); hyperlipidemia (DIS-014); hypertension (DIS-002) |
| Allergy | **ALG-004 (ACE-inhibitor angioedema)**: lip and tongue swelling on lisinopril in 2019; drug stopped |
| Medications | Aspirin (MED-010), clopidogrel (MED-011), metoprolol succinate (MED-006), atorvastatin (MED-009) |

### 4.1 Chest-pain pathway, 2026-02-03 (PRO-006, FPA-08)

| Clock time | Event | Requirement |
|---|---|---|
| 07:42 | Arrival at DEP-001 with 90 minutes of chest pressure; BP 168/94 | Start event |
| 07:49 | 12-lead ECG (LAB-021): ST depression 1.5 mm in V2 to V5 | Within 10 minutes: met (7 minutes) |
| 07:55 | Aspirin 300 mg given | |
| 07:58 | hs-troponin 0 hour draw (LAB-007) | |
| 08:10 | Clopidogrel 300 mg given | |
| 08:28 | Result verified: 62 ng/L | |
| 10:02 | hs-troponin 2 hour draw (2 h 04 min after the 0 hour draw) | 0 and 2 hour series |
| 10:18 | Result verified: 155 ng/L | |
| 10:26 | Result phoned to the cardiology fellow, 8 minutes after verification | PRO-009: met |

### 4.2 Management
Coronary angiography on 2026-02-04 (DEP-003) showed a 85% right coronary artery stenosis treated with one drug-eluting stent. Echocardiogram (LAB-023, LD-06): LVEF 48%, mild inferior hypokinesis. Metoprolol succinate was started at 25 mg and raised to 50 mg daily; atorvastatin 80 mg daily; aspirin 81 mg daily long term; clopidogrel 75 mg daily for 12 months.

### 4.3 The ACE-inhibitor decision
DG-01 recommends a renin-angiotensin system blocker after ACS when LVEF is below 50% or hypertension persists. For PAT-008 the standard choice, an ACE inhibitor such as lisinopril (MED-004), is **contraindicated by ALG-004** (MP-01, MP-06, MP-07). MP-01 also advises caution with related receptor-blocking agents after ACE-inhibitor angioedema. No renin-angiotensin agent was started; blood pressure was addressed with metoprolol and cardiology re-review planned at 6 weeks (completed 2026-03-17, BP 132/80). Discharged 2026-02-07. Compare PAT-001 (PR-01), who takes lisinopril without any allergy flag.

## 5. PAT-009: Lucia Fernandes-Adler (INC-005)

| Item | Value |
|---|---|
| Date of birth / age | 1945-06-03 / 81 years; female |
| Weight | 61 kg |
| Problems | Chronic kidney disease stage G3b (DIS-003); acute kidney injury (DIS-017); complicated UTI (DIS-010); osteoarthritis of both knees (DIS-021) |
| Allergy | **ALG-006 (latex)**: contact urticaria; latex-free supplies required |
| Medications | Lisinopril 5 mg (MED-004), furosemide 20 mg (MED-007), ibuprofen (MED-026), ceftriaxone (MED-017), acetaminophen (MED-027) |

### 5.1 Background and the prescription (INC-005)
Baseline creatinine 1.3 mg/dL (115 umol/L), eGFR 40, on 2026-03-05. At an ambulatory visit that day for a knee flare, the clinic physician prescribed ibuprofen 600 mg three times daily for 14 days. The PharmaSafe alert for an NSAID in CKD (MP-05, MP-06) was overridden as "short course." The patient continued lisinopril and furosemide, producing an unsafe combination of an NSAID, an ACE inhibitor, and a diuretic in a patient with CKD.

### 5.2 Admission, 2026-03-22 to 2026-03-28
On 2026-03-19 she developed dysuria and fever and had poor oral intake. She was admitted on 2026-03-22: BP 94/58, creatinine 2.6 mg/dL (230 umol/L). Creatinine and eGFR were measured as part of the basic metabolic panel (LAB-002, LAB-004; reports in LD-03). Urinalysis (LAB-013) positive; urine culture grew Escherichia coli, ceftriaxone-susceptible (LD-05).

| Date | Creatinine mg/dL (umol/L) | eGFR | Actions |
|---|---|---|---|
| 2026-03-05 | 1.3 (115) | 40 | Baseline; ibuprofen prescribed |
| 2026-03-22 | 2.6 (230) | 17 | Ibuprofen, lisinopril, furosemide stopped; IV fluids; ceftriaxone 1 g IV daily (MED-017) started |
| 2026-03-23 | 2.9 (256) | 15 | Peak |
| 2026-03-24 | 2.4 (212) | 19 | |
| 2026-03-25 | 1.9 (168) | 26 | |
| 2026-03-27 | 1.6 (141) | 32 | |
| 2026-03-28 | 1.5 (133) | 34 | Discharged |

The peak creatinine of 2.9 mg/dL is 2.2 times baseline, meeting stage 2 of the AKI staging in DG-03 (2.0 to 2.9 times baseline). The doses of ceftriaxone were reviewed against the PRO-008 renal tiers and needed no reduction. Pain control used acetaminophen 650 mg every 6 hours (MED-027). A latex-free urinary catheter was used because of ALG-006. Ceftriaxone was given for 7 days (2026-03-22 to 2026-03-28).

### 5.3 Follow-up
Lisinopril resumed at 5 mg and furosemide at 20 mg on 2026-03-31. Creatinine on 2026-04-14: 1.4 mg/dL (eGFR 37), the new baseline. NSAIDs were added to the chart as "avoid: CKD". The event was reported as **INC-005** (HO-08).

## 6. PAT-010: Victor Anselmo-Kaur

| Item | Value |
|---|---|
| Date of birth / age | 1977-09-12 / 49 years; male |
| Weight | 92 kg |
| Problems | Major depressive disorder (DIS-020); osteoarthritis (DIS-021); upper GI bleeding (DIS-022); hypertension (DIS-002); hyperlipidemia (DIS-014) |
| Allergy | None known |
| Medications | Sertraline 100 mg (MED-025); ibuprofen 600 mg three times daily (MED-026); aspirin 81 mg (MED-010); atorvastatin 40 mg (MED-009); pantoprazole (MED-028) started during admission |

### 6.1 Medication reconciliation finding (PRO-001)
On admission the pharmacist interview found aspirin 81 mg taken daily, bought over the counter for "heart prevention," which was not on the medication list. Ibuprofen had been prescribed 2026-04-14 for hand and knee osteoarthritis. The combination with sertraline was recognized by PharmaSafe as a **Major** additive bleeding-risk interaction (SSRI-related platelet dysfunction, NSAID mucosal injury, aspirin platelet inhibition; MP-06).

### 6.2 Admission, 2026-06-10 to 2026-06-14
Black stools for two days. BP 102/64, heart rate 104. Hemoglobin (LAB-001) 8.8 g/dL against a baseline of 14.6 g/dL on 2026-01-14. Upper endoscopy on 2026-06-11: 1.5 cm gastric antral ulcer with a clean base; no endoscopic therapy; H. pylori stool antigen negative. No transfusion was required. Pantoprazole 40 mg IV twice daily then 40 mg orally twice daily for 8 weeks (MED-028). Ibuprofen and aspirin were stopped permanently; acetaminophen (MED-027) was used for arthritis pain. Sertraline was **continued** because depression was stable, with the PPI as protection (DG-08 conflict rule). Hb 9.6 g/dL at discharge on 2026-06-14 and 12.8 g/dL on 2026-07-22.

**Differences from PAT-002 (PR-02), a similar bleed:** PAT-010 had a gastric ulcer, a 5.8 g/dL fall from baseline, no transfusion, and no anticoagulant; PAT-002 had a duodenal ulcer with a visible vessel, two units transfused, and was on apixaban and clopidogrel.

## 7. Policy Compliance Review (retrospective)

| Patient | Policy | Observed | Result |
|---|---|---|---|
| PAT-007 | PRO-003 / FPA-09 dual verification | Nursing check bypassed | Not met; INC-001 |
| PAT-008 | PRO-006 / FPA-08 ECG within 10 minutes; troponin at 0 and 2 hours | 7 minutes; 2 h 04 min | Met |
| PAT-008 | PRO-009 call within 20 minutes | 8 minutes | Met |
| PAT-009 | PRO-008 renal-tier check at prescribing | NSAID alert overridden | Not met; INC-005 |
| PAT-010 | PRO-001 reconciliation of over-the-counter agents | Found at admission interview | Gap before admission |

## 8. Other Records (non-diagnostic and background)

- PAT-007: employed as a graphic designer; non-smoker; asthma action plan updated 2026-06-23.
- PAT-008: retired electrician; former smoker (stopped 2008); cardiac rehabilitation 12 sessions from 2026-03-02.
- PAT-009: widowed; lives with her daughter; hearing aids; influenza vaccine 2025-10-17.
- PAT-010: software engineer; psychotherapy sessions fortnightly; no alcohol.

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Anaphylaxis treatment; drug-allergy management | DG-07, MP-05 (epinephrine), MP-07 |
| Dual-verification rule and the INC-001 review | HO-02, HO-08 |
| ACS algorithm; ACE-inhibitor contraindication | DG-01, MP-01, MP-06 |
| Troponin and ECG reports | LD-04, LD-06 |
| AKI staging; NSAID contraindication in CKD | DG-03, MP-05 |
| Creatinine reports; urine and culture reports | LD-03, LD-05 |
| SSRI, NSAID, aspirin interaction; GI bleed management | MP-06, DG-07, DG-08 |
| Spirometry | LD-08 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic casebook (Pass 1) |
