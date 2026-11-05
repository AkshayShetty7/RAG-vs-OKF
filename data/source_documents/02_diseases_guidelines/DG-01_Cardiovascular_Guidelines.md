---
doc_id: DG-01
title: "Cardiovascular Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-005, PAT-008, PAT-011, DIS-001, DIS-002, DIS-003, DIS-004, DIS-005, DIS-006, MED-004, MED-005, MED-006, MED-007, MED-008, MED-009, MED-010, MED-011, MED-012, MED-013, MED-028, LAB-001, LAB-004, LAB-005, LAB-007, LAB-008, LAB-010, LAB-021, LAB-023, PRO-006, PRO-007, PRO-009, PRO-016, DEP-003, STF-005, ALG-003, ALG-004, FPA-06, FPA-08]
related_docs: [DG-03, DG-04, HO-03, HO-04, HO-05, HO-07, LD-01, LD-04, LD-06, MP-01, MP-03, MP-06, MP-07, PR-01, PR-02, PR-05, PR-07, PR-08]
---

# DG-01: Cardiovascular Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements (time targets and workflow rules owned by the HO documents).

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-01 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Hypertension (DIS-002), HFrEF (DIS-004), atrial fibrillation (DIS-005), acute coronary syndrome (DIS-006) |
| Owner | Cardiology (DEP-003, head STF-005), approved by the Clinical Protocol Review Board (CPRB) |
| Companion documents | Monographs MP-01 and MP-03; interaction matrix MP-06; allergy reference MP-07; protocols HO-03, HO-04, HO-07; test definitions LD-01 |

## 2. Purpose and Scope

This guideline defines how MediCore diagnoses and treats four cardiovascular conditions. It supplies the criteria that patient charts (PR-01, PR-02, PR-05, PR-07, PR-08) apply and that protocols (HO-03, HO-07) implement with MediCore time targets. Where a time target appears here it is labeled as a pointer to the protocol; the authoritative value is in the HO document.

## 3. Hypertension (DIS-002)

### 3.1 Diagnosis and targets
Hypertension is diagnosed when clinic blood pressure is 140/90 mmHg or higher on two visits, or 135/85 mmHg or higher on home monitoring. The treatment target is below 140/90 mmHg for most adults and **below 130/80 mmHg** for patients with diabetes (DIS-001), chronic kidney disease (DIS-003), or established cardiovascular disease.

### 3.2 Drug selection

| Situation | Preferred agent | Notes |
|---|---|---|
| Hypertension with HFrEF, diabetes, or CKD | ACE inhibitor: lisinopril (MED-004) | Check potassium and creatinine at baseline, 1 week, and after each dose increase |
| Hypertension without compelling indication | Calcium-channel blocker: amlodipine (MED-005) | Ankle edema is the commonest adverse effect |
| Hypertension after myocardial infarction | Beta-blocker: metoprolol succinate (MED-006) | Cardioselective; see asthma caution in DG-04 |
| Hypertension with fluid overload | Loop diuretic: furosemide (MED-007) | Monitor potassium and renal function |

### 3.3 When an ACE inhibitor must not be used
An ACE inhibitor is **contraindicated** after a previous episode of ACE-inhibitor-associated angioedema (ALG-004). Related receptor-blocking agents also require caution because angioedema can recur at a lower rate (MP-01, MP-06, MP-07). Example: PAT-008 (PR-07).

## 4. Heart Failure with Reduced Ejection Fraction (DIS-004)

### 4.1 Diagnosis
HFrEF requires symptoms or signs of heart failure plus a left ventricular ejection fraction (LVEF) of **40% or lower** on echocardiography (LAB-023). NT-proBNP (LAB-008) supports the diagnosis when above 450 pg/mL under age 50, above 900 pg/mL between 50 and 75, and above 1,800 pg/mL over 75. NT-proBNP is not a stand-alone diagnostic test.

### 4.2 Treatment pillars

| Pillar | Agent | Reference rule |
|---|---|---|
| Renin-angiotensin blockade | Lisinopril (MED-004) | Titrate to tolerated dose; hold during vomiting, diarrhea, or hyperkalemia |
| Beta-blocker | Metoprolol succinate (MED-006) | Start low; double at 2-week intervals if heart rate and blood pressure allow |
| Mineralocorticoid antagonist | Spironolactone (MED-008) | Start when potassium is 5.0 mmol/L or lower and eGFR is 30 or higher |
| Congestion control | Furosemide (MED-007) | Lowest dose that maintains dry weight |

### 4.3 Potassium safety for mineralocorticoid antagonists
Check potassium (LAB-005) and creatinine/eGFR (LAB-004) at **1 week and 4 weeks** after starting or increasing spironolactone. Do not increase the dose when potassium is above 5.0 mmol/L. Hold spironolactone and the ACE inhibitor if potassium reaches 5.5 mmol/L or higher; the management algorithm is in DG-03. The combination of MED-004 with MED-008 in CKD is a recognized hyperkalemia hazard (MP-06, MP-01); PAT-001 (PR-01) illustrates the monitoring schedule.

### 4.4 Sick-day rule
During vomiting, diarrhea, or poor oral intake the patient should pause the ACE inhibitor, spironolactone, diuretic, and metformin until eating and drinking normally for 24 to 48 hours.

### 4.5 After discharge
Discharge after a heart-failure admission requires structured follow-up. The MediCore protocol is PRO-016 in HO-07, which sets a telephone call within 48 hours and a clinic visit within 7 days (FPA-06). Patients on warfarin (MED-013) also need an INR check within 72 hours of discharge under PRO-007 (HO-04). PAT-011 (PR-08) shows what happens when these steps fail.

## 5. Atrial Fibrillation (DIS-005)

### 5.1 Diagnosis
Diagnose by 12-lead ECG (LAB-021) or a monitor strip showing at least 30 seconds of irregular rhythm without discernible P waves. Paroxysmal AF terminates within 7 days; persistent AF lasts longer. Echocardiography (LAB-023) is indicated at diagnosis.

### 5.2 Stroke prevention
An oral anticoagulant is recommended in adults with AF at moderate or high stroke risk. First choice is apixaban 5 mg twice daily (MED-012); warfarin (MED-013, target INR 2.0 to 3.0) is used when apixaban is unsuitable. Dose-reduction criteria for apixaban are in MP-03.

### 5.3 Bleeding-risk rubric (MediCore Bleeding-Risk Rubric, fictional)
One point each for: age over 65; body weight under 60 kg; hypertension; previous major bleed; renal impairment (eGFR below 45); concomitant antiplatelet drug. A score of **3 or more** is elevated risk and prompts minimization of concomitant antiplatelet therapy and use of a proton pump inhibitor (MED-028). PAT-002 (PR-02) scored 3.

### 5.4 Rate control
Metoprolol succinate (MED-006) is the first-line rate-control agent when LVEF is reduced or after myocardial infarction.

## 6. Acute Coronary Syndrome (DIS-006)

### 6.1 Diagnosis
ACS is diagnosed from symptoms, ECG (LAB-021), and hs-troponin (LAB-007). Non-ST-elevation myocardial infarction (NSTEMI) requires a rise and/or fall of hs-troponin above the 99th percentile in the LD-01 range with ischemic symptoms or ECG change. Serial sampling at 0 and 2 hours is the MediCore standard (FPA-08; HO-03). ST-depression, as in PAT-002 and PAT-008, supports the diagnosis but is not required.

### 6.2 Initial treatment
Aspirin 300 mg loading dose (MED-010) unless contraindicated; clopidogrel 300 mg loading dose (MED-011) before angiography; high-intensity statin (atorvastatin 80 mg, MED-009); beta-blocker (MED-006) if no contraindication. If aspirin is contraindicated (ALG-003), clopidogrel alone is used for the antiplatelet effect (MP-07).

### 6.3 Antithrombotic therapy when ACS and AF coexist
This situation requires balancing stent thrombosis against bleeding.

| Rule | Reference guideline statement |
|---|---|
| Aspirin duration | Aspirin is added only for the peri-procedural period and is limited to **7 days or less** |
| Anticoagulant | Continue or resume apixaban (MED-012) as soon as the procedure is complete |
| P2Y12 inhibitor | Clopidogrel 75 mg daily for **6 months** after the stent, together with apixaban; then apixaban alone |
| Gastric protection | Proton pump inhibitor for the duration of combined therapy |
| Review | Pharmacist review of every combination with an anticoagulant and an antiplatelet (PRO-007, HO-04) |

PAT-002 (PR-02) followed this pattern: aspirin for 5 days, clopidogrel to 2025-09-04.

### 6.4 ACS without AF
Dual antiplatelet therapy (aspirin 81 mg plus clopidogrel 75 mg) continues for **12 months**. PAT-008 (PR-07) follows this schedule.

### 6.5 Renin-angiotensin blockade after ACS
An ACE inhibitor is recommended after ACS when LVEF is below 50% or hypertension persists. If an ACE inhibitor is contraindicated (ALG-004), no alternative agent is started automatically; cardiology reviews at 6 weeks (MP-01).

### 6.6 Pathway timing
Time-critical steps (ECG within 10 minutes of arrival; 0 and 2 hour hs-troponin; critical-result calling) are MediCore protocols owned by PRO-006 and PRO-009 in HO-03 and HO-05.

## 7. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-001 | HFrEF therapy, MRA monitoring, hyperkalemia | PR-01 |
| PAT-002 | AF with NSTEMI; limited aspirin; 6 months clopidogrel plus apixaban | PR-02 |
| PAT-005 | New AF after stroke; blood-pressure treatment | PR-05 |
| PAT-008 | NSTEMI without AF; ACE inhibitor contraindicated | PR-07 |
| PAT-011 | HFrEF with AF on warfarin; follow-up failure | PR-08 |

## 8. Monitoring Summary

| Condition | Test | Frequency |
|---|---|---|
| HFrEF on MRA | Potassium, creatinine/eGFR | 1 week, 4 weeks, then each visit |
| HFrEF | NT-proBNP (LAB-008) | At diagnosis and at clinic review |
| AF on apixaban | Creatinine/eGFR, CBC (LAB-001) | At least yearly; sooner after bleeding |
| AF on warfarin | INR (LAB-010) | Per HO-04 |

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Drug monographs | MP-01, MP-03 |
| Interaction severities | MP-06 |
| Allergy reference | MP-07 |
| Lab definitions and ranges | LD-01 |
| Troponin and BNP reports | LD-04 |
| ECG and echocardiogram reports | LD-06 |
| Chest-pain pathway; HF follow-up protocol | HO-03, HO-07 |
| Anticoagulation protocol | HO-04 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
