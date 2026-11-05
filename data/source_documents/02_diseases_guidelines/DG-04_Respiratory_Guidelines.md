---
doc_id: DG-04
title: "Respiratory Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, PAT-005, PAT-007, PAT-012, DIS-007, DIS-008, DIS-015, MED-006, MED-016, MED-017, MED-021, MED-022, MED-023, LAB-012, LAB-015, LAB-016, LAB-018, LAB-019, LAB-020, PRO-003, PRO-013, DEP-006, STF-008, ALG-001, ALG-003, INC-001, FPA-09]
related_docs: [DG-05, HO-02, HO-04, HO-08, LD-01, LD-04, LD-07, LD-08, MP-04, MP-05, MP-07, PR-03, PR-05, PR-07, PR-08]
---

# DG-04: Respiratory Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-04 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | COPD (DIS-007), community-acquired pneumonia (DIS-008), asthma (DIS-015) |
| Owner | Pulmonology (DEP-006, head STF-008), approved by the CPRB |
| Companion documents | DG-05 (sepsis and antibiotic duration), MP-04, MP-05, LD-01, LD-04, LD-07, LD-08 |

## 2. Purpose and Scope

This guideline gives diagnostic criteria, severity classes, and treatment steps for three respiratory conditions. The patient applications are PAT-003 (PR-03), PAT-005 (PR-05), PAT-007 (PR-07) and PAT-012 (PR-08). Antibiotic duration and sepsis management are owned by DG-05.

## 3. Chronic Obstructive Pulmonary Disease (DIS-007)

### 3.1 Diagnosis
Spirometry (LAB-019) is required: a **post-bronchodilator FEV1/FVC below 0.70** confirms persistent airflow limitation in a patient with symptoms and risk factors (tobacco, occupational exposure).

### 3.2 Severity by FEV1 (percent predicted)

| Class | FEV1 |
|---|---|
| Mild | 80% or higher |
| Moderate | 50% to 79% |
| Severe | 30% to 49% |
| Very severe | below 30% |

PAT-003 had FEV1/FVC 0.54 and FEV1 48% of predicted on 2024-11-20: **severe** COPD (PR-03, LD-08).

### 3.3 Maintenance treatment
Long-acting antimuscarinic: tiotropium 18 micrograms inhaled daily (MED-022). Short-acting beta-agonist: albuterol as needed (MED-021). Smoking cessation and pulmonary rehabilitation are mandatory elements of care.

### 3.4 Acute exacerbation
Triggers: increased dyspnea, sputum volume, or purulence.

| Component | Reference rule |
|---|---|
| Bronchodilator | Albuterol nebulization every 4 hours initially (MED-021) |
| Corticosteroid | Prednisone 40 mg daily for **5 days** (MED-023) |
| Antibiotic | When sputum is purulent or there is radiographic pneumonia |
| Oxygen | Controlled oxygen, target SpO2 88% to 92% |
| Non-invasive ventilation | Indicated when arterial pH is **below 7.35 with PaCO2 above 6.0 kPa (45 mmHg)** despite initial treatment (LAB-018) |

PAT-003 arrived with pH 7.28 and PaCO2 8.3 kPa and received non-invasive ventilation (PR-03).

## 4. Community-Acquired Pneumonia (DIS-008)

### 4.1 Diagnosis
Clinical features (fever, cough, pleuritic pain, new crackles) plus a new infiltrate on chest X-ray (LAB-020, LD-07). Procalcitonin (LAB-015) and C-reactive protein (LAB-016) support bacterial infection but do not replace imaging.

### 4.2 Severity classes

| Class | Criteria |
|---|---|
| Non-severe | None of the severe features |
| **Severe** | Any of: respiratory rate 30 or higher; systolic blood pressure below 90 mmHg; new confusion; sepsis (DG-05); need for ICU care |

PAT-003 met severe criteria (respiratory rate 30, sepsis, later ICU); PAT-012 was non-severe (PR-08).

### 4.3 Antibiotic choice

| Class | First-line agent | Notes |
|---|---|---|
| Non-severe | Amoxicillin-clavulanate 875/125 mg twice daily (MED-016) | Not for patients with a penicillin allergy (ALG-001); see MP-07 for alternatives |
| Severe | Ceftriaxone 2 g IV daily (MED-017), with escalation per sepsis guideline (DG-05) | Obtain blood cultures (LAB-012) before the first dose |

### 4.4 Duration and de-escalation
Duration is set in **DG-05**: non-severe pneumonia, a minimum of 5 days; severe or bacteremic pneumococcal pneumonia, 7 days. The stewardship stop rule (procalcitonin below 0.25 ng/mL and afebrile for 48 hours at day 5) is MediCore Policy in HO-04 (PRO-013), not a guideline rule.

### 4.5 Follow-up
Repeat chest X-ray at 6 weeks in patients over 50 or smokers to confirm resolution. PAT-003 and PAT-012 both had follow-up films (PR-03, PR-08).

## 5. Asthma (DIS-015)

### 5.1 Diagnosis
Variable respiratory symptoms plus reversible airflow limitation: FEV1 improvement of **12% and 200 mL or more** after bronchodilator on spirometry (LAB-019). PAT-007 showed 14% reversibility with FEV1 82% of predicted (PR-07, LD-08).

### 5.2 Control and treatment
Short-acting beta-agonist (albuterol, MED-021) for symptoms; inhaled corticosteroid for persistent symptoms. Exacerbations: albuterol nebulization, prednisone 40 mg daily for 5 days (MED-023).

### 5.3 NSAID- and aspirin-exacerbated respiratory disease
In some patients with asthma, aspirin and other NSAIDs provoke bronchospasm, urticaria, or facial swelling (ALG-003). These drugs must be avoided entirely; the definition and cross-reactivity are in MP-07. PAT-005 has this pattern (PR-05). A beta-blocker (MED-006) is a caution in asthma; cardioselective agents are used with monitoring when indicated.

### 5.4 Antibiotics in an asthma exacerbation
Antibiotics are not routinely required. A beta-lactam given to a patient with a penicillin allergy flag requires the dual-verification step (MediCore Policy PRO-003, FPA-09, HO-02). The failure of that step in PAT-007 is documented in PR-07 and HO-08 (INC-001).

## 6. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-003 | Severe COPD exacerbation with severe CAP | PR-03 |
| PAT-005 | Asthma with NSAID/aspirin hypersensitivity | PR-05 |
| PAT-007 | Asthma exacerbation with antibiotic anaphylaxis | PR-07 |
| PAT-012 | Non-severe CAP | PR-08 |

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Antibiotic duration; sepsis | DG-05 |
| Antibiotic monographs | MP-04 |
| Albuterol, tiotropium, prednisone monographs | MP-05 |
| Allergy definitions | MP-07 |
| Procalcitonin, CRP, ABG | LD-04 |
| Chest X-ray reports | LD-07 |
| Spirometry reports and diagnostic crosswalk | LD-08 |
| Stewardship protocol; allergy protocol | HO-04, HO-02 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
