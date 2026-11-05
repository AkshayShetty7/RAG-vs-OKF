---
doc_id: MP-04
title: "Anti-Infective Monographs"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, PAT-006, PAT-007, PAT-009, PAT-012, PAT-013, DIS-008, DIS-009, DIS-010, DIS-023, MED-013, MED-016, MED-017, MED-018, MED-019, MED-020, MED-023, MED-031, LAB-004, PRO-002, PRO-003, PRO-004, PRO-007, PRO-008, PRO-013, DEP-007, DEP-010, STF-002, STF-009, ALG-001, INC-001, INC-003, FPA-09, FPA-11]
related_docs: [DG-04, DG-05, HO-02, HO-03, HO-04, LD-05, MP-06, MP-07]
---

# MP-04: Anti-Infective Monographs

> **SYNTHETIC DATA NOTICE.** This formulary is fictional and was written for software benchmarking and education. Doses, thresholds, and rules are invented, may differ from real-world practice, and must not be used for clinical decisions. "MediCore Policy" items are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-04 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, STF-002) with Infectious Diseases (DEP-007, STF-009); approved by the P&T Committee and the ASC |
| Medications covered | MED-016 amoxicillin-clavulanate, MED-017 ceftriaxone, MED-018 piperacillin-tazobactam, MED-019 vancomycin (IV and oral), MED-020 ciprofloxacin |
| Related documents | DG-04, DG-05; MP-06; MP-07; HO-03 (PRO-004), HO-04 (PRO-013); LD-05 |

## 2. Purpose and Scope

Monographs for five antibiotics, with spectrum, dosing, renal adjustment, monitoring, and allergy handling. Penicillin allergy (ALG-001) governs MED-016 and MED-018; cephalosporin cross-reactivity rules are in MP-07. Antibiotic duration is set in DG-05, and the stewardship stop rule is MediCore Policy in HO-04.

## 3. MED-016 Amoxicillin-Clavulanate

| Item | Detail |
|---|---|
| Class | Aminopenicillin with beta-lactamase inhibitor |
| Indications | Non-severe community-acquired pneumonia (DIS-008); oral step-down |
| Adult dosing | 875/125 mg orally twice daily with food |
| Renal | Avoid the 875 mg tablet when eGFR is below 30 (MP-07) |
| **Allergy** | **Contraindicated in penicillin allergy (ALG-001).** Any first dose in a patient with an allergy flag requires **dual verification by pharmacist and nurse** (MediCore Policy FPA-09, PRO-003; HO-02) |
| Interactions | Moderate INR rise with warfarin (MP-06) |
| High-alert | No |
| Dataset patients | PAT-003 (step-down 2026-03-03 to 2026-03-04); PAT-012 (2026-05-05 to 2026-05-09; tolerated); **PAT-007 (given in error 2026-05-17; anaphylaxis, INC-001)** |

## 4. MED-017 Ceftriaxone

| Item | Detail |
|---|---|
| Class | Third-generation cephalosporin |
| Indications | CAP (DIS-008); sepsis (DIS-009); complicated UTI (DIS-010) |
| Adult dosing | 1 to 2 g IV once daily; 2 g daily for severe infection |
| Renal | No adjustment |
| **Allergy** | Cross-reactivity with penicillin allergy is low; rules in MP-07: permitted after a **non-severe** penicillin reaction with dual verification; **avoid after a severe reaction (anaphylaxis, angioedema)** until allergy evaluation |
| Interactions | Moderate INR rise with warfarin |
| Dataset patients | PAT-003 (2026-02-26, 2026-03-01 to 2026-03-02); PAT-009 (1 g daily, 7 days); PAT-013 (2 g daily, 2026-06-21 to 2026-06-24) |

## 5. MED-018 Piperacillin-Tazobactam

| Item | Detail |
|---|---|
| Class | Antipseudomonal penicillin with beta-lactamase inhibitor |
| Indications | Sepsis (DIS-009) with broad cover needed; complicated UTI (DIS-010) |
| Adult dosing | 4.5 g IV every 6 hours |
| **Renal adjustment** | **eGFR above 30: 4.5 g every 6 hours. eGFR 30 or below: 3.375 g every 6 hours** (PRO-008) |
| **Allergy** | **Contraindicated in penicillin allergy (ALG-001); dual verification applies** |
| Interactions | With vancomycin (MED-019): **Major nephrotoxicity risk** (MP-06) |
| High-alert | No |
| Dataset patients | PAT-003 (2026-02-27 to 2026-03-01); PAT-013 (4.5 g at 2026-06-18 04:52; 3.375 g every 6 hours from 2026-06-19 at eGFR 30) |

## 6. MED-019 Vancomycin (IV and Oral)

| Item | Detail |
|---|---|
| Class | Glycopeptide |
| **IV indications** | Sepsis with possible resistant gram-positive organisms (DIS-009) |
| **Oral indication** | C. difficile infection (DIS-023): 125 mg orally every 6 hours for 10 days; not absorbed systemically; no renal adjustment |
| **IV dosing** | **Pharmacy-managed (DEP-010).** Load 20 to 25 mg/kg then individualized to renal function and levels |
| **Level timing (MediCore Policy FPA-11, PRO-013)** | **First level before the fourth dose.** A level above 20 mg/L prompts holding the next dose and re-dosing by pharmacy |
| Monitoring | Creatinine/eGFR (LAB-004) daily during IV therapy |
| Stewardship | Stop IV vancomycin at 48 hours when cultures show no resistant gram-positive organism (HO-04) |
| Interactions | With piperacillin-tazobactam: Major nephrotoxicity; with furosemide: Moderate ototoxicity (MP-06) |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-003 (IV 2026-02-27 to 2026-03-01, level 14.8 mg/L before dose 4; oral 2026-03-07 to 2026-03-16); PAT-013 (IV 2026-06-18 to 2026-06-20, level 24.1 mg/L before dose 4, dose held, interval extended to every 24 hours) |

## 7. MED-020 Ciprofloxacin

| Item | Detail |
|---|---|
| Class | Fluoroquinolone |
| Indications | Complicated UTI (DIS-010) when susceptible and no safer option |
| Adult dosing | 500 mg orally twice daily |
| Renal | eGFR 30 to 50: 250 to 500 mg every 12 hours; below 30: 250 to 500 mg every 18 to 24 hours (MP-07) |
| Cautions | Tendon rupture, especially with corticosteroids; QT prolongation; blood glucose disturbance |
| **Key interaction** | **Warfarin (MED-013): Major; raises INR.** A written INR recheck plan is required before the first dose (PRO-007) or a non-interacting agent should be chosen |
| Other interactions | Iron (MED-031): separate; prednisone (MED-023): tendon risk |
| High-alert | No |
| Dataset patients | PAT-006 (2025-10-21 to 2025-10-26; INR 2.4 to 6.8; INC-003) |

## 8. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Pneumonia, sepsis, UTI, C. difficile guidelines | DG-04, DG-05 |
| Interaction severities | MP-06 |
| Allergy rules and renal dosing | MP-07 |
| Cultures and C. difficile reports | LD-05 |
| Sepsis bundle; allergy and stewardship protocols | HO-03, HO-02, HO-04 |

## 9. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic monograph set (Pass 1) |
