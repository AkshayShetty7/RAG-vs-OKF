---
doc_id: MP-07
title: "Allergy, ADR and Organ-Function Dosing Reference"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-004, PAT-005, PAT-006, PAT-007, PAT-008, PAT-009, PAT-010, PAT-013, PAT-014, MED-001, MED-002, MED-003, MED-004, MED-005, MED-006, MED-007, MED-008, MED-009, MED-010, MED-011, MED-012, MED-013, MED-015, MED-016, MED-017, MED-018, MED-019, MED-020, MED-026, MED-027, MED-028, MED-030, MED-031, PRO-003, PRO-008, DEP-010, DEP-013, STF-002, STF-014, ALG-001, ALG-002, ALG-003, ALG-004, ALG-005, ALG-006, INC-001, INC-002, INC-003, INC-005, FPA-03, FPA-09, FPA-11]
related_docs: [DG-03, DG-07, HO-02, HO-08, MP-01, MP-05, MP-06, PR-01, PR-06, PR-07, PR-08]
---

# MP-07: Allergy, ADR and Organ-Function Dosing Reference

> **SYNTHETIC DATA NOTICE.** This reference is fictional and was written for software benchmarking and education. Allergy rules, dosing tiers, and reporting rules are invented, may differ from real-world practice, and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-07 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, STF-002) with Quality and Patient Safety (DEP-013, STF-014); approved by the P&T Committee |
| Scope | Allergen classes ALG-001 to ALG-006; adverse drug reaction (ADR) reporting; renal and hepatic dosing rules for MED-001 to MED-031 |
| Related documents | MP-01 to MP-06; DG-03, DG-07; HO-02 (PRO-003, PRO-008); HO-08 |

## 2. Allergen Classes (ALG)

### 2.1 Definitions and rules

| ID | Allergen class | Typical reactions | Drug rule | Dataset patients |
|---|---|---|---|---|
| **ALG-001** | Penicillins and aminopenicillins | Urticaria, angioedema, anaphylaxis | **MED-016 and MED-018 contraindicated.** Ceftriaxone (MED-017): see 2.2 | PAT-006 (urticaria 2004); PAT-007 (anaphylaxis, confirmed 2026-05-17) |
| **ALG-002** | Sulfonamide antibiotics | Rash | Sulfonamide antibiotics avoided. Non-antibiotic sulfonamides such as furosemide (MED-007) have low cross-reactivity and may be given with monitoring | PAT-002 (rash 2009) |
| **ALG-003** | NSAIDs including aspirin | Bronchospasm, urticaria, facial swelling (respiratory-type pattern in asthma) | **MED-010 and MED-026 contraindicated.** Acetaminophen (MED-027) tolerated at standard doses. Clopidogrel (MED-011) is the antiplatelet alternative | PAT-005 (reaction 2012) |
| **ALG-004** | ACE-inhibitor-associated angioedema | Lip, tongue, or airway swelling | **MED-004 contraindicated.** Related receptor-blocking agents: caution, specialist review | PAT-008 (2019) |
| **ALG-005** | Iodinated contrast media | Urticaria, bronchospasm | Policy-only class: flag, pre-medication pathway, radiology review. Contrast agents are not in the formulary | **No patient** |
| **ALG-006** | Latex | Contact urticaria | Latex-free gloves, catheters, tourniquets | PAT-009 |

### 2.2 Penicillin to cephalosporin cross-reactivity (rule for ceftriaxone)

| Prior penicillin reaction | Ceftriaxone (MED-017) |
|---|---|
| Non-severe (for example urticaria without airway or circulatory involvement) | Permitted; **dual verification by pharmacist and nurse** for the first dose (PRO-003, FPA-09) |
| Severe (anaphylaxis, angioedema, severe cutaneous reaction) | **Avoid** until allergy evaluation or a supervised graded challenge |
| Unverified, patient-reported | Treated as the **worst credible reaction** until verified; an unverified flag must not be treated as low risk (DG-07) |

PAT-006 (non-severe urticaria) could receive ceftriaxone under this rule but was prescribed ciprofloxacin (PR-06). PAT-007 (anaphylaxis) must avoid ceftriaxone until allergy evaluation.

### 2.3 Allergy record standard
Each allergy entry records: allergen class (ALG), reaction, severity, date, verification status (verified or unverified), and source. After an event the record is updated the same day. Dual verification before the first dose of any beta-lactam in a patient with **any** allergy flag is MediCore Policy (FPA-09, PRO-003).

## 3. Adverse Drug Reaction (ADR) Reporting

### 3.1 MediCore ADR severity scale

| Level | Definition |
|---|---|
| Mild | No treatment needed |
| Moderate | Treatment or monitoring needed |
| Severe | Hospitalization, life-threatening, or permanent effect |
| Sentinel | Death or permanent harm |

### 3.2 Process
Report any suspected ADR in PharmaSafe the same day. Severe and sentinel reports go to the Patient Safety Committee (PSC) within 24 hours and to HO-08. Pharmacy reviews trends monthly.

### 3.3 ADRs recorded in the dataset

| ADR | Patient | Drug | Severity | Outcome |
|---|---|---|---|---|
| Euglycemic ketoacidosis | PAT-004 | Empagliflozin MED-030 | Severe | Drug permanently stopped; no re-challenge |
| Anaphylaxis | PAT-007 | Amoxicillin-clavulanate MED-016 | Severe | Epinephrine; allergy record upgraded; INC-001 |
| Supratherapeutic INR 6.8 | PAT-006 | Ciprofloxacin with warfarin | Moderate | Warfarin held; INC-003 |
| Hyperkalemia 6.4 mmol/L | PAT-001 | Lisinopril with spironolactone, during dehydration | Severe | Held, restarted at lower doses; INC-002 concerns result notification |
| Acute kidney injury stage 2 | PAT-009 | Ibuprofen with lisinopril and furosemide | Severe | NSAID stopped; INC-005 |
| Upper GI bleed | PAT-010 | Ibuprofen and aspirin with sertraline | Severe | NSAID and aspirin stopped |
| Levothyroxine under-absorption | PAT-014 | Ferrous sulfate co-administration | Mild | Dosing times separated |

## 4. Renal Dosing Reference

### 4.1 General tier labels
Tier labels are used in PRO-008 (HO-02) and in this document. eGFR is in mL/min/1.73 m2.

| Tier | eGFR |
|---|---|
| Tier 1 | 60 or higher |
| Tier 2 | 45 to 59 |
| Tier 3 | 30 to 44 (CKD stage G3b) |
| Tier 4 | 15 to 29 |
| Tier 5 | below 15 |

### 4.2 Drug-specific rules (the thresholds below take precedence over tier labels)

| Drug | Rule |
|---|---|
| MED-001 metformin | **Tier 1 and 2: no cap. Tier 3 (30 to 44): maximum 1,000 mg/day. Below 30: stop** (FPA-03) |
| MED-004 lisinopril | Tier 3: start 2.5 to 5 mg, maximum 20 mg/day. Tier 4: start 2.5 mg, maximum 10 mg/day, specialist. Tier 5: avoid unless nephrology agrees |
| MED-007 furosemide | No reduction; larger doses may be required at low eGFR |
| MED-008 spironolactone | eGFR 45 or higher: start 25 mg. 30 to 44: start 12.5 mg. Below 30: avoid |
| MED-012 apixaban | 2.5 mg twice daily if at least two of: age 80 or older, weight 60 kg or less, creatinine 1.5 mg/dL or higher. Avoid below eGFR 15 |
| MED-015 enoxaparin | eGFR below 30: 1 mg/kg once daily, or use unfractionated heparin |
| MED-016 amoxicillin-clavulanate | Avoid the 875 mg tablet below eGFR 30 |
| MED-018 piperacillin-tazobactam | **eGFR above 30: 4.5 g every 6 hours. eGFR 30 or below: 3.375 g every 6 hours** |
| MED-019 vancomycin IV | Pharmacy-managed by levels; interval extended as eGFR falls; first level before the fourth dose (FPA-11) |
| MED-020 ciprofloxacin | eGFR 30 to 50: 250 to 500 mg every 12 hours; below 30: every 18 to 24 hours |
| MED-026 ibuprofen | Avoid in CKD stages G3 to G5 and in AKI |
| MED-030 empagliflozin | Do not start below eGFR 20; reduced glucose lowering below 45 |
| MED-002 / MED-003 insulin | Reduced clearance; lower starting doses and watch for hypoglycemia |
| Other formulary drugs | No renal adjustment |

### 4.3 Worked examples from the dataset
- PAT-001, eGFR 44 on 2025-02-20: Tier 3, metformin capped at 1,000 mg/day; implemented 2025-03-13 (PR-01).
- PAT-013, eGFR 30 on 2026-06-19: piperacillin-tazobactam reduced to 3.375 g every 6 hours (PR-08).
- PAT-009, eGFR 40 baseline: ibuprofen contraindicated (INC-005, PR-07).

## 5. Hepatic Dosing Notes

| Drug | Rule |
|---|---|
| MED-027 acetaminophen | Maximum 2 g/day in chronic liver disease |
| MED-009 atorvastatin | Contraindicated in active liver disease |
| MED-005 amlodipine | Start 2.5 mg in severe impairment |
| MED-006 metoprolol | Reduce dose in severe impairment |
| MED-028 pantoprazole | Consider reduction in severe impairment |
| MED-013 warfarin | Increased sensitivity; monitor INR closely |

## 6. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Monographs | MP-01 to MP-05 |
| Interaction severities | MP-06 |
| Allergy and anaphylaxis management | DG-07 |
| Kidney guidelines | DG-03 |
| Dual verification, renal dose, reconciliation protocols | HO-02 |
| Incident reviews | HO-08 |

## 7. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic reference (Pass 1) |
