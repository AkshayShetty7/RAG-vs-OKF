---
doc_id: MP-06
title: "Drug Interaction and Contraindication Matrix"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-003, PAT-004, PAT-005, PAT-006, PAT-008, PAT-009, PAT-010, PAT-013, PAT-014, MED-001, MED-002, MED-003, MED-004, MED-005, MED-006, MED-007, MED-008, MED-009, MED-010, MED-011, MED-012, MED-013, MED-014, MED-015, MED-016, MED-017, MED-018, MED-019, MED-020, MED-021, MED-023, MED-024, MED-025, MED-026, MED-027, MED-028, MED-029, MED-030, MED-031, PRO-003, PRO-007, DEP-010, STF-002, ALG-001, ALG-002, ALG-003, ALG-004, ALG-005, ALG-006, INC-001, INC-003, INC-005, FPA-03, FPA-14]
related_docs: [DG-02, DG-03, DG-06, DG-07, DG-08, HO-02, HO-04, HO-08, MP-01, MP-05, MP-07, PR-01, PR-06, PR-07, PR-08]
---

# MP-06: Drug Interaction and Contraindication Matrix

> **SYNTHETIC DATA NOTICE.** This matrix is fictional and was written for software benchmarking and education. Severity ratings, mechanisms, and management rules are invented, may differ from real-world practice, and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-06 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, STF-002), approved by the P&T Committee; rules are loaded into the PharmaSafe alert engine |
| Scope | Pairwise interactions among MED-001 to MED-031 relevant to the dataset, plus condition and allergy contraindications |
| Related documents | MP-01 to MP-05 (monographs), MP-07 (allergy and organ-function dosing), DG-03, DG-07, DG-08, HO-02, HO-04, HO-08 |

## 2. Severity Scale (owned by this document)

| Rating | Meaning | Alert behavior in PharmaSafe |
|---|---|---|
| **Contraindicated** | Do not combine or use | Hard stop; override needs a documented second pharmacist |
| **Major** | Serious harm likely; combine only with a documented monitoring plan | Interruptive alert; override reason mandatory |
| **Moderate** | Monitoring or timing adjustment usually enough | Advisory alert |
| **Minor** | Limited clinical effect | Informational |

Overridden Major alerts are audited in HO-08. Two incidents arose from overrides: INC-003 (ciprofloxacin with warfarin) and INC-005 (ibuprofen in CKD).

## 3. Pairwise Interaction Table

| # | Drug A | Drug B | Rating | Mechanism | Management and monitoring | Dataset case |
|---|---|---|---|---|---|---|
| 1 | MED-013 warfarin | MED-020 ciprofloxacin | **Major** | Reduced warfarin metabolism and gut flora vitamin K production raise INR | Prefer another antibiotic; otherwise INR recheck plan written before first dose (PRO-007) with INR within 3 days | PAT-006: INR 2.4 to 6.8, INC-003 (PR-06) |
| 2 | MED-004 lisinopril | MED-008 spironolactone | **Major in CKD** | Both reduce potassium excretion | Potassium and creatinine at 1 and 4 weeks; avoid salt substitutes; hold during illness | PAT-001: K 6.4 on 2025-09-17 (PR-01) |
| 3 | MED-025 sertraline | MED-026 ibuprofen | **Major** | SSRI platelet dysfunction plus NSAID mucosal injury | Avoid; use acetaminophen; PPI if unavoidable | PAT-010 |
| 4 | MED-025 sertraline | MED-010 aspirin | Moderate | Additive platelet inhibition | PPI; review indication | PAT-010 |
| 5 | MED-026 ibuprofen | MED-010 aspirin | Moderate | Additive GI injury; ibuprofen can blunt aspirin antiplatelet effect | Avoid combination | PAT-010 |
| 6 | **Triple: MED-025 + MED-026 + MED-010** | | **Major** | Additive bleeding: SSRI platelet effect, NSAID mucosal injury, aspirin platelet inhibition | Stop NSAID and aspirin; continue SSRI with PPI if depression stable (DG-08) | PAT-010: GI bleed 2026-06-10 (PR-07) |
| 7 | MED-004 lisinopril | MED-026 ibuprofen | **Major** | Afferent and efferent arteriolar effects; AKI and hyperkalemia | Avoid in CKD; with a loop diuretic this is the "triple" kidney-injury combination (row 8) | PAT-009 |
| 8 | **Triple: MED-004 + MED-007 + MED-026** | | **Major** | ACE inhibitor, diuretic and NSAID together precipitate AKI | Avoid; sick-day rule | PAT-009: AKI stage 2, INC-005 (PR-07) |
| 9 | MED-007 furosemide | MED-026 ibuprofen | Moderate | NSAID blunts diuresis | Avoid | PAT-009 |
| 10 | MED-004 lisinopril | MED-007 furosemide | Moderate | First-dose hypotension, volume depletion | Hold during illness | PAT-001 |
| 11 | MED-024 levothyroxine | MED-031 ferrous sulfate | Moderate | Iron binds levothyroxine in the gut and reduces absorption | **Separate by at least 4 hours (FPA-14);** TSH after 6 to 8 weeks | PAT-014: TSH 8.9 (PR-08) |
| 12 | MED-018 piperacillin-tazobactam | MED-019 vancomycin | **Major** | Additive nephrotoxicity | Pharmacy-managed levels; creatinine daily; reduce piperacillin-tazobactam at eGFR 30 or below | PAT-013 (PR-08); PAT-003 |
| 13 | MED-019 vancomycin | MED-007 furosemide | Moderate | Additive ototoxicity and nephrotoxicity | Monitor creatinine, hearing | None |
| 14 | MED-012 apixaban | MED-011 clopidogrel | **Major** | Additive bleeding | Allowed in AF plus stent for 6 months with PPI | PAT-002 |
| 15 | MED-012 apixaban | MED-010 aspirin | **Major** | Additive bleeding | Aspirin 7 days or less | PAT-002 |
| 16 | MED-012 apixaban | MED-026 ibuprofen | **Major** | Additive bleeding | Avoid NSAIDs | None |
| 17 | MED-013 warfarin | MED-026 ibuprofen | **Major** | Additive bleeding | Avoid | None |
| 18 | MED-013 warfarin | MED-010 aspirin | **Major** | Additive bleeding | Only with a clear indication | None |
| 19 | MED-013 warfarin | MED-011 clopidogrel | **Major** | Additive bleeding | Avoid unless stent indication | None |
| 20 | MED-014 heparin | MED-010 / MED-011 / MED-012 | **Major** | Additive bleeding | Platelets and aPTT monitoring | PAT-002 |
| 21 | MED-015 enoxaparin | MED-010 / MED-011 | **Major** | Additive bleeding | Weigh benefit; PPI | None |
| 22 | MED-011 clopidogrel | MED-010 aspirin | Moderate | Intended dual antiplatelet therapy | PPI; fixed duration | PAT-002 (briefly), PAT-008 |
| 23 | MED-011 clopidogrel | MED-028 pantoprazole | Minor | Weak CYP2C19 inhibition | Pantoprazole is the preferred PPI | PAT-002 |
| 24 | MED-013 warfarin | MED-016 amoxicillin-clavulanate | Moderate | Gut flora effect | INR within 3 to 5 days | None |
| 25 | MED-013 warfarin | MED-017 ceftriaxone | Moderate | Gut flora effect | INR within 3 to 5 days | None |
| 26 | MED-013 warfarin | MED-027 acetaminophen | Moderate | Sustained doses above 2 g/day raise INR | Monitor INR | None |
| 27 | MED-013 warfarin | MED-023 prednisone | Moderate | Variable INR effect | INR within 1 week | None |
| 28 | MED-029 epinephrine | MED-006 metoprolol | **Major** | Beta-blockade can blunt epinephrine response in anaphylaxis | Repeat dose early; escalate | None |
| 29 | MED-021 albuterol | MED-006 metoprolol | Moderate | Pharmacologic antagonism, less with cardioselective agents | Monitor | PAT-005 (no beta-blocker) |
| 30 | MED-021 albuterol | MED-007 furosemide | Moderate | Additive hypokalemia | Potassium monitoring | None |
| 31 | MED-023 prednisone | MED-026 ibuprofen | **Major** | Additive GI bleeding | Avoid | None |
| 32 | MED-023 prednisone | MED-020 ciprofloxacin | Moderate | Tendon rupture risk | Counsel | None |
| 33 | MED-023 prednisone | MED-002 / MED-003 insulin | Moderate | Hyperglycemia | Increase glucose monitoring | None |
| 34 | MED-020 ciprofloxacin | MED-031 ferrous sulfate | Moderate | Chelation reduces absorption | Give ciprofloxacin 2 hours before or 6 hours after | None |
| 35 | MED-020 ciprofloxacin | MED-001 metformin | Moderate | Glucose disturbance | Monitor glucose | None |
| 36 | MED-002 / MED-003 insulin | MED-006 metoprolol | Moderate | Masks adrenergic hypoglycemia symptoms | Counsel; check glucose | PAT-004 (not on beta-blocker) |
| 37 | MED-030 empagliflozin | MED-002 insulin | Moderate | Additive glucose lowering and ketoacidosis risk if insulin reduced | Do not reduce insulin sharply during illness | PAT-004 |
| 38 | MED-030 empagliflozin | MED-001 metformin | Minor | Additive glucose lowering | None required | PAT-004 |
| 39 | MED-009 atorvastatin | MED-011 clopidogrel | Minor | None significant | None | PAT-002, PAT-008 |
| 40 | MED-005 amlodipine | MED-006 metoprolol | Minor | Additive hypotension | Monitor blood pressure | None |

## 4. Condition and Allergy Contraindications

| Condition or allergy | Contraindicated drug(s) | Rating | Source rule |
|---|---|---|---|
| ALG-001 penicillins | MED-016, MED-018; MED-017 only after non-severe reactions with dual verification | Contraindicated / Major | MP-07; PRO-003 |
| ALG-002 sulfonamide antibiotics | Sulfonamide antibiotics (none in formulary); furosemide MED-007 allowed with monitoring | Contraindicated / Minor | MP-07 |
| ALG-003 NSAIDs and aspirin | MED-010, MED-026 | Contraindicated | MP-07, DG-06 |
| ALG-004 ACE-inhibitor angioedema | MED-004; related receptor blockers need caution | Contraindicated / Major | MP-01 |
| ALG-005 iodinated contrast | Contrast agents (not in formulary) | Policy only; no patient | MP-07, HO-02 |
| ALG-006 latex | Latex-containing devices | Contraindicated | HO-02 |
| CKD with eGFR 30 to 44 | MED-001 above 1,000 mg/day | Major | FPA-03 |
| eGFR below 30 | MED-001 | Contraindicated | FPA-03 |
| CKD or AKI | MED-026 | Contraindicated | DG-03 |
| Hyperkalemia | MED-004, MED-008 | Contraindicated until corrected | DG-03 |
| DKA or acute illness on SGLT2 inhibitor | MED-030 | Contraindicated; no re-challenge after DKA | DG-02 |
| Active GI bleeding | MED-010, MED-026, MED-012 | Contraindicated | DG-07 |
| Anticoagulant therapy | MED-026 | Major | DG-08 |

## 5. How PharmaSafe Alerts Map to Incidents

| Alert | Override outcome |
|---|---|
| Row 1 (warfarin with ciprofloxacin) | Overridden with "will monitor" and no INR order: INC-003 |
| Row 7 and 8 (ibuprofen in CKD with ACE inhibitor and diuretic) | Overridden as "short course": INC-005 |
| Allergy flag with MED-016 | Dual-verification step bypassed with the "urgent override": INC-001 |

## 6. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Individual drug monographs | MP-01 to MP-05 |
| Allergy classes and organ-function dosing | MP-07 |
| Clinical conflict rules | DG-08, DG-03, DG-07 |
| Override audit and incident review | HO-08 |
| Medication safety and anticoagulation protocols | HO-02, HO-04 |

## 7. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic matrix (Pass 1) |
