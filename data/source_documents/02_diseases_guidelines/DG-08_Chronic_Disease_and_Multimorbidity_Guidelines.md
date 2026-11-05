---
doc_id: DG-08
title: "Chronic Disease and Multimorbidity Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-004, PAT-005, PAT-006, PAT-007, PAT-008, PAT-009, PAT-010, PAT-013, PAT-014, DIS-001, DIS-003, DIS-017, DIS-019, DIS-020, DIS-021, DIS-024, MED-001, MED-004, MED-010, MED-011, MED-013, MED-016, MED-018, MED-020, MED-025, MED-026, MED-027, MED-028, MED-030, MED-031, PRO-001, DEP-002, DEP-010, ALG-001, ALG-003, ALG-004, ALG-006, INC-001, INC-005]
related_docs: [DG-02, DG-03, DG-06, DG-07, HO-02, HO-08, MP-05, MP-06, MP-07, PR-01, PR-04, PR-05, PR-06, PR-07, PR-08]
---

# DG-08: Chronic Disease and Multimorbidity Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-08 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Major depressive disorder (DIS-020), osteoarthritis (DIS-021), polypharmacy and condition-drug conflicts across DIS-001 to DIS-024 |
| Owner | Internal Medicine (DEP-002) with Clinical Pharmacy (DEP-010), approved by the CPRB |
| Companion documents | MP-05, MP-06, MP-07, HO-02, HO-08 |

## 2. Purpose and Scope

Patients seldom have one disease. This guideline covers two chronic conditions that frequently conflict with other treatments and supplies the **conflict rules** that tell clinicians which drug to avoid in which disease, and what to use instead. It is the hub document for medication-versus-condition conflicts in the dataset.

## 3. Major Depressive Disorder (DIS-020)

### 3.1 Diagnosis
Five or more depressive symptoms for at least two weeks with functional impairment, supported by a PHQ-9 score of **10 or higher**.

### 3.2 Treatment
Psychotherapy and/or an SSRI. Sertraline (MED-025) 50 mg daily, titrated to 100 to 200 mg. Review response at 4 to 6 weeks. Continue for at least 6 months after remission.

### 3.3 Bleeding risk with SSRIs
SSRIs impair platelet function. The risk of gastrointestinal bleeding rises when an SSRI is combined with an NSAID (MED-026), aspirin (MED-010) or an anticoagulant. MP-06 rates the combination of sertraline with ibuprofen and aspirin as **Major**.

### 3.4 After a bleed
After an NSAID- or aspirin-associated bleed in a patient on sertraline whose depression is stable: **stop the NSAID and the aspirin permanently, continue sertraline, and add a proton pump inhibitor** (MED-028) for as long as bleeding risk persists (DG-07). Switching an SSRI during a stable remission is not required. PAT-010 followed this rule (PR-07).

## 4. Osteoarthritis (DIS-021)

### 4.1 Diagnosis
Clinical: age over 45, activity-related joint pain, brief morning stiffness, bony enlargement; imaging when needed.

### 4.2 Treatment ladder

| Step | Intervention |
|---|---|
| 1 | Exercise, weight management, physiotherapy |
| 2 | **Acetaminophen** (MED-027) up to 3 g per day |
| 3 | Topical agents |
| 4 | Oral NSAID (ibuprofen, MED-026), only when none of the contraindications in 4.3 applies, at the lowest dose and shortest duration |
| 5 | Joint injection or replacement |

### 4.3 When an NSAID must not be used
Avoid oral NSAIDs in: chronic kidney disease or AKI (DG-03); anticoagulant therapy (DG-06); a history of gastrointestinal bleeding (DG-07); concurrent SSRI plus antiplatelet (section 3); heart failure; NSAID/aspirin hypersensitivity (ALG-003, MP-07). Where any applies, remain at step 2.

PAT-009 (CKD G3b) was prescribed ibuprofen against this rule and developed AKI (INC-005, PR-07). PAT-006 (anticoagulated) used acetaminophen (PR-06). PAT-010 developed a bleed on ibuprofen with aspirin and sertraline (PR-07).

## 5. Polypharmacy Review

### 5.1 Definition
Polypharmacy is five or more regular medicines. Patients in this dataset with polypharmacy include PAT-001 (six), PAT-002 (seven), PAT-009 and PAT-010.

### 5.2 Method
At each admission and discharge and at periodic outpatient review (the MediCore reconciliation protocol is PRO-001, HO-02):
1. List every medicine including over-the-counter and supplements (PAT-010 took aspirin 81 mg unrecorded).
2. Match each to an active indication.
3. Check each against kidney function (MP-07).
4. Check each pair against MP-06.
5. Check each against documented allergies (ALG entities, MP-07).
6. Stop or reduce anything without an indication.

## 6. Condition-Drug Conflict Rules

| # | Condition or state | Drug to avoid | Reason | Preferred approach | Dataset example |
|---|---|---|---|---|---|
| 1 | CKD (DIS-003) or AKI (DIS-017) | Ibuprofen (MED-026) | Nephrotoxic; with ACE inhibitor and diuretic raises AKI risk | Acetaminophen (MED-027) | PAT-009, PR-07 |
| 2 | CKD with eGFR 30 to 44 | Metformin above 1,000 mg/day (MED-001) | Accumulation | Cap dose (DG-02, DG-03) | PAT-001, PR-01 |
| 3 | NSAID/aspirin hypersensitivity (ALG-003) | Aspirin (MED-010), ibuprofen | Bronchospasm, urticaria | Clopidogrel (MED-011), acetaminophen | PAT-005, PR-05 |
| 4 | ACE-inhibitor angioedema (ALG-004) | Lisinopril (MED-004) | Recurrent angioedema | No ACE inhibitor; caution with related agents | PAT-008, PR-07 |
| 5 | Penicillin allergy (ALG-001) | Amoxicillin-clavulanate (MED-016), piperacillin-tazobactam (MED-018) | Anaphylaxis risk | Non-penicillin agent per MP-07 | PAT-006, PAT-007 |
| 6 | Hyperkalemia (DIS-019) or K above 5.5 | Lisinopril, spironolactone | Potassium retention | Hold, then restart with monitoring | PAT-001, PR-01 |
| 7 | Warfarin therapy (MED-013) | Ciprofloxacin (MED-020) without INR plan | INR rise | INR recheck plan or alternative agent | PAT-006, PR-06 |
| 8 | SSRI plus antiplatelet | Ibuprofen, aspirin | Additive bleeding | Stop NSAID/aspirin; PPI | PAT-010, PR-07 |
| 9 | Hypothyroidism on levothyroxine | Ferrous sulfate within 4 hours (MED-031) | Reduced absorption | Separate by 4 hours or more | PAT-014, PR-08 |
| 10 | Acute illness with poor intake on SGLT2 inhibitor | Empagliflozin (MED-030) | Euglycemic ketoacidosis | Pause during illness; never re-challenge after DKA | PAT-004, PR-04 |
| 11 | Latex allergy (ALG-006) | Latex-containing devices | Contact urticaria | Latex-free supplies | PAT-009, PR-07 |
| 12 | Vancomycin with piperacillin-tazobactam | Combination without level and creatinine monitoring | Nephrotoxicity | Early levels; pharmacy dosing | PAT-013, PR-08 |

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Sertraline, ibuprofen, acetaminophen monographs | MP-05 |
| Interaction severities | MP-06 |
| Allergy and renal dosing references | MP-07 |
| Reconciliation, renal-dose and allergy protocols | HO-02 |
| Incident reviews (INC-005, INC-001) | HO-08 |
| Related guidelines | DG-02, DG-03, DG-06, DG-07 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
