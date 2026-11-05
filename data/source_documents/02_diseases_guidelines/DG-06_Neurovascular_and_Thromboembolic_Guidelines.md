---
doc_id: DG-06
title: "Neurovascular and Thromboembolic Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, PAT-005, PAT-006, PAT-011, DIS-005, DIS-011, DIS-012, MED-010, MED-011, MED-012, MED-013, MED-014, MED-015, MED-020, MED-026, MED-027, LAB-001, LAB-010, LAB-011, LAB-021, LAB-022, LAB-023, LAB-026, LAB-027, PRO-005, PRO-007, PRO-008, DEP-002, DEP-008, STF-010, ALG-003, FPA-04, FPA-07]
related_docs: [DG-01, DG-02, HO-03, HO-04, LD-02, LD-06, LD-07, MP-03, MP-06, MP-07, PR-02, PR-05, PR-06, PR-08]
---

# DG-06: Neurovascular and Thromboembolic Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-06 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Acute ischemic stroke (DIS-011), venous thromboembolism (DIS-012), and the AF-stroke link (DIS-005) |
| Owner | Neurology (DEP-008, head STF-010) with Internal Medicine (DEP-002), approved by the CPRB |
| Companion documents | DG-01, MP-03, MP-06, MP-07, LD-02, LD-06, LD-07, HO-03, HO-04 |

## 2. Purpose and Scope

This guideline covers diagnosis and secondary prevention after ischemic stroke and the diagnosis and anticoagulant treatment of deep vein thrombosis (DVT) and pulmonary embolism (PE). Time-critical steps for stroke (door-to-CT) are MediCore Policy in PRO-005 (HO-03) and are not set here. The charts that apply it are PR-05 and PR-06.

## 3. Acute Ischemic Stroke (DIS-011)

### 3.1 Initial assessment
Establish last known well time. Score severity with the NIH Stroke Scale (NIHSS). Obtain non-contrast CT head (LAB-022) to exclude hemorrhage before any antithrombotic treatment. Record a 12-lead ECG (LAB-021) and complete blood count (LAB-001), PT/INR (LAB-010) and glucose. The time target for CT is in PRO-005 (HO-03, FPA-07).

### 3.2 Reperfusion decision
Reperfusion therapy is decided by the stroke team (DEP-008) based on last known well, imaging and deficit. It is not recommended when deficits are minor or rapidly resolving. The agents involved are outside the dataset formulary; the decision and its rationale must be documented (PR-05).

### 3.3 Etiology work-up
Echocardiography (LAB-023) and rhythm assessment for a cardioembolic source. New atrial fibrillation (DIS-005) found after stroke is treated as the likely cause.

### 3.4 Secondary prevention: antiplatelet therapy
Aspirin 300 mg then 75 to 100 mg daily (MED-010) is the first-line antiplatelet. **If aspirin is contraindicated** (for example NSAID/aspirin hypersensitivity, ALG-003), use **clopidogrel** (MED-011) 300 mg loading dose then 75 mg daily (MP-03, MP-07). Do not use any NSAID (including ibuprofen, MED-026) in a patient with ALG-003.

### 3.5 Secondary prevention: anticoagulation in atrial fibrillation
Anticoagulation (apixaban, MED-012) is started after stroke with AF at a time determined by stroke severity and imaging:

| Initial NIHSS | Earliest start of anticoagulant (counting day 0 as the day of onset) |
|---|---|
| Below 5 (mild) | Day 2 |
| **5 to 15 (moderate)** | **Between day 4 and day 7**, provided **repeat CT (LAB-022) shows no hemorrhagic transformation** |
| Above 15 (severe) | Day 10 to day 14 |

When the anticoagulant starts, the antiplatelet agent is stopped unless a separate indication exists. Pharmacist verification of the new apixaban order within 4 hours is MediCore Policy (FPA-04, PRO-007, HO-04). PAT-005 started apixaban on day 5, with clopidogrel stopped (PR-05).

### 3.6 Other secondary prevention
Statin therapy (DG-02), blood-pressure reduction to below 130/80 mmHg after the acute phase (DG-01), glucose control, smoking cessation, rehabilitation.

## 4. Venous Thromboembolism (DIS-012)

### 4.1 Diagnosis
1. Estimate clinical pre-test probability.
2. If low or intermediate probability, measure D-dimer (LAB-026). A normal D-dimer excludes VTE; an elevated value requires imaging.
3. Confirm PE by CT pulmonary angiogram (CTPA, LAB-027) or leg ultrasound for DVT.

PAT-006: D-dimer 3,850 ng/mL FEU, followed by CTPA showing right lower lobe segmental emboli (PR-06, LD-02, LD-07).

### 4.2 Parenteral anticoagulation
- Unfractionated heparin infusion (MED-014) with aPTT (LAB-011) target **60 to 80 seconds** when rapid reversibility is desirable or renal function is poor.
- Enoxaparin (MED-015) 1 mg per kg subcutaneously every 12 hours when the patient is stable; reduce or avoid when eGFR is below 30 (MP-07, PRO-008).

### 4.3 Transition to warfarin
Start warfarin (MED-013) on day 1 (the day after heparin starts) with target INR 2.0 to 3.0. Continue parenteral therapy for **at least 5 days and until INR is 2.0 or higher on two consecutive checks**. The MediCore protocol operationalizing this is PRO-007 (HO-04). PAT-006 had 10 days of parenteral cover (PR-06).

### 4.4 Alternative: apixaban
Apixaban (MED-012) may be used for VTE when appropriate (MP-03); this was not the choice for PAT-006.

### 4.5 Duration

| Situation | Anticoagulation duration |
|---|---|
| **Provoked** by a major transient risk factor (for example surgery) | **3 months** |
| Unprovoked | At least 6 months, then review |
| Cancer-associated | Indefinite while cancer active |

PAT-006 (provoked by knee replacement) completed 3 months on 2025-11-29 (PR-06).

### 4.6 Interacting drugs
Many drugs raise or lower the INR. Ciprofloxacin (MED-020) raises it (MP-06). When an interacting drug is started, an INR recheck plan is required (PRO-007). NSAIDs are avoided during anticoagulation; acetaminophen (MED-027) is preferred.

## 5. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-005 | Ischemic stroke with new AF, aspirin contraindicated, apixaban on day 5 | PR-05 |
| PAT-006 | Provoked PE, heparin to warfarin, 3-month course | PR-06 |
| PAT-011 | Warfarin for AF, INR monitoring | PR-08 |
| PAT-002 | AF anticoagulation with ACS | PR-02 |

## 6. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| AF anticoagulation and ACS | DG-01 |
| Antithrombotic monographs | MP-03 |
| Interaction severities | MP-06 |
| Allergy definitions | MP-07 |
| CBC, INR, aPTT, D-dimer reports | LD-02 |
| ECG and echocardiogram | LD-06 |
| CT head and CTPA reports | LD-07 |
| Stroke code pathway; anticoagulation protocol | HO-03, HO-04 |

## 7. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
