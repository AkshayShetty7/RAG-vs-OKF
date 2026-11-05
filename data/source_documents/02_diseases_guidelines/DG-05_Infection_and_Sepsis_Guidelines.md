---
doc_id: DG-05
title: "Infection and Sepsis Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, PAT-006, PAT-009, PAT-012, PAT-013, DIS-008, DIS-009, DIS-010, DIS-023, MED-013, MED-016, MED-017, MED-018, MED-019, MED-020, LAB-012, LAB-013, LAB-014, LAB-015, LAB-024, PRO-004, PRO-007, PRO-008, PRO-012, PRO-013, DEP-007, STF-009, ALG-001, INC-003, INC-004, FPA-10, FPA-11]
related_docs: [DG-04, HO-03, HO-04, HO-06, HO-08, LD-04, LD-05, MP-04, MP-06, MP-07, PR-03, PR-06, PR-07, PR-08]
---

# DG-05: Infection and Sepsis Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-05 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Sepsis (DIS-009), complicated urinary tract infection (DIS-010), C. difficile infection (DIS-023); pneumonia antibiotic durations (DIS-008) |
| Owner | Infectious Diseases (DEP-007, head STF-009), approved by the CPRB and the Antimicrobial Stewardship Committee (ASC) |
| Companion documents | DG-04, MP-04, MP-06, LD-04, LD-05, HO-03, HO-04, HO-06 |

## 2. Purpose and Scope

This guideline sets the clinical rules for recognizing sepsis, choosing and stopping antibiotics, and treating two common infections and one antibiotic-associated infection. MediCore time targets (sepsis bundle, isolation duration, stewardship stop rule) are **policies** in HO-03, HO-04 and HO-06; this document refers to them but does not set their values.

## 3. Sepsis (DIS-009)

### 3.1 Recognition
Sepsis is suspected infection with acute organ dysfunction. Screening triggers: temperature above 38.0 C or below 36.0 C, heart rate above 100, respiratory rate 22 or higher, systolic pressure 100 mmHg or below, altered mentation, or lactate (LAB-014) above 2.0 mmol/L.

### 3.2 Initial management

| Step | Reference guideline statement |
|---|---|
| Cultures | Blood cultures (LAB-012), two sets, **before** antibiotics when this causes no delay; urine culture (LAB-013) when a urinary source is possible |
| Antibiotics | First dose as soon as possible after recognition and within one hour. The MediCore time target and its versions are in PRO-004 (HO-03) |
| Lactate | Measure at recognition and repeat when elevated; the MediCore repeat rule is in PRO-004 |
| Fluids | Crystalloid resuscitation for hypotension or lactate of 4 mmol/L or higher |
| Source control | Drain or remove infected collections or obstruction promptly |

### 3.3 Choice of antibiotics
Empiric cover is based on the source, local susceptibility, and allergy status (MP-07). For severe sepsis from pneumonia, ceftriaxone (MED-017) is the starting agent, with escalation to piperacillin-tazobactam (MED-018) plus vancomycin (MED-019) for deterioration or when resistant gram-positive organisms are possible (PAT-003, PR-03). For a urinary source with obstruction, piperacillin-tazobactam (MED-018) is used (PAT-013, PR-08).

### 3.4 Monitoring antibiotic toxicity
Vancomycin is pharmacy-managed. Draw the **first level before the fourth dose** (MediCore Policy FPA-11, PRO-013). Vancomycin combined with piperacillin-tazobactam carries a recognized nephrotoxicity risk (MP-06); dose to current eGFR and reduce piperacillin-tazobactam at eGFR 30 or below (MP-07, PRO-008).

### 3.5 De-escalation
Review at 48 to 72 hours. When susceptibilities are known, narrow to the most selective effective agent and stop vancomycin if no resistant gram-positive organism is isolated. PAT-003 was de-escalated within 5 hours of the susceptibility report (PR-03); PAT-013 had vancomycin stopped at 48 hours (PR-08).

### 3.6 Procalcitonin
Procalcitonin (LAB-015) supports stopping antibiotics when it falls below **0.25 ng/mL** or by 80% from peak, together with clinical recovery. The binding stewardship stop rule is MediCore Policy in HO-04.

## 4. Antibiotic Duration Summary (Reference Guideline)

| Infection | Duration |
|---|---|
| Non-severe community-acquired pneumonia (DIS-008) | Minimum **5 days**, if afebrile and clinically stable for 48 hours |
| Severe or bacteremic pneumococcal pneumonia | **7 days** |
| Complicated UTI (DIS-010) | **7 days** with clinical response |
| C. difficile infection (DIS-023) | **10 days** of oral vancomycin |

Applied: PAT-012, 5 days (PR-08); PAT-003, 7 days (PR-03); PAT-013, 7 days (PR-08); PAT-003 oral vancomycin, 10 days (PR-03). PAT-006 received only 5 days of ciprofloxacin because of an interaction event; stewardship accepted this with documented symptom resolution and a negative follow-up culture (PR-06).

## 5. Complicated Urinary Tract Infection (DIS-010)

### 5.1 Definition
UTI with fever or systemic features, obstruction, recent hospitalization or instrumentation, immunosuppression, or other conditions that raise treatment failure risk. Diagnosis by urinalysis and culture (LAB-013).

### 5.2 Treatment

| Setting | Options |
|---|---|
| Oral, culture-susceptible | Ciprofloxacin 500 mg twice daily (MED-020) |
| Parenteral | Ceftriaxone (MED-017) or piperacillin-tazobactam (MED-018) |
| Penicillin allergy (ALG-001) | Avoid MED-016 and MED-018; ciprofloxacin or a cephalosporin under MP-07 rules |

### 5.3 Interaction with anticoagulants
Ciprofloxacin raises the INR in patients taking warfarin (MED-013); check INR within the interval specified in PRO-007 (HO-04) or choose a non-interacting agent (MP-06, MP-04). PAT-006 illustrates the consequence of an unplanned interaction (INR 6.8, INC-003, PR-06).

### 5.4 Source control
Relieve obstruction (catheter or stent) in obstructed infection; PAT-013 had a urinary catheter placed with 650 mL drained (PR-08).

## 6. Clostridioides difficile Infection (DIS-023)

### 6.1 Diagnosis
Test (LAB-024) when there are three or more unformed stools in 24 hours without another cause and typically after recent antibiotics or hospitalization. A positive toxin or PCR in a symptomatic patient is diagnostic.

### 6.2 Severity
Severe when white cell count exceeds 15 x 10^9/L or creatinine exceeds 1.5 times baseline.

### 6.3 Treatment
Stop the inciting antibiotic if possible. First episode: **vancomycin 125 mg orally every 6 hours for 10 days** (MED-019, oral route; MP-04). PAT-003 received this regimen from 2026-03-07 to 2026-03-16 (PR-03).

### 6.4 Infection prevention
Contact-enteric precautions and dedicated equipment. The MediCore isolation duration (72 hours after diarrhea resolves) is policy FPA-10 in PRO-012 (HO-06). Delay in starting precautions is reported as an incident (INC-004, HO-08).

## 7. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-003 | Sepsis from CAP, escalation and de-escalation, C. difficile | PR-03 |
| PAT-006 | Complicated UTI with penicillin allergy and warfarin | PR-06 |
| PAT-009 | UTI with AKI | PR-07 |
| PAT-012 | Non-severe CAP, 5-day course | PR-08 |
| PAT-013 | Urosepsis, vancomycin and AKI | PR-08 |

## 8. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Antibiotic monographs, vancomycin monitoring | MP-04 |
| Interaction severities | MP-06 |
| Allergy and renal dosing references | MP-07 |
| Lactate, procalcitonin | LD-04 |
| Cultures, C. difficile reports | LD-05 |
| Sepsis bundle | HO-03 |
| Stewardship; vancomycin level rule | HO-04 |
| Isolation | HO-06 |

## 9. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
