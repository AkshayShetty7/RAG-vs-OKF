---
doc_id: MP-03
title: "Antithrombotic Monographs"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, PAT-005, PAT-006, PAT-008, PAT-010, PAT-011, DIS-005, DIS-006, DIS-011, DIS-012, MED-010, MED-011, MED-012, MED-013, MED-014, MED-015, MED-020, MED-025, MED-026, MED-028, LAB-001, LAB-004, LAB-010, LAB-011, PRO-002, PRO-007, PRO-008, DEP-010, STF-002, ALG-003, INC-003, FPA-04, FPA-05]
related_docs: [DG-01, DG-06, DG-07, HO-04, LD-02, MP-06, MP-07]
---

# MP-03: Antithrombotic Monographs

> **SYNTHETIC DATA NOTICE.** This formulary is fictional and was written for software benchmarking and education. Doses, thresholds, and rules are invented, may differ from real-world practice, and must not be used for clinical decisions. "MediCore Policy" items are invented parameters. Reversal agents are outside the dataset formulary and are not described.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-03 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, STF-002), approved by the P&T Committee |
| Medications covered | MED-010 aspirin, MED-011 clopidogrel, MED-012 apixaban, MED-013 warfarin, MED-014 heparin (unfractionated), MED-015 enoxaparin |
| Related documents | DG-01, DG-06, DG-07; MP-06; MP-07; HO-04 (PRO-007); LD-02 |

## 2. Purpose and Scope

Monographs for six drugs that prevent or treat clotting. Four are **high-alert medications** under PRO-002 (apixaban, warfarin, heparin, enoxaparin). The anticoagulation protocol (PRO-007) in HO-04 operationalizes the monitoring rules below; where the two documents share a value (FPA-04, FPA-05) they are identical.

## 3. MED-010 Aspirin

| Item | Detail |
|---|---|
| Class | Antiplatelet (cyclo-oxygenase inhibitor); also an NSAID |
| Indications | ACS (DIS-006); ischemic stroke (DIS-011); primary prevention in selected patients |
| Adult dosing | ACS: 300 mg loading dose then 81 mg daily. Stroke: 300 mg then 75 to 100 mg daily |
| With an anticoagulant | Limit to a peri-procedural course of **7 days or less** (DG-01) |
| Renal | Avoid below eGFR 10; caution below 30 |
| **Contraindications** | **NSAID/aspirin hypersensitivity (ALG-003): absolute**; active GI bleeding; peptic ulcer with recent bleed |
| Interactions | With apixaban, warfarin or heparin: Major (additive bleeding); with sertraline (MED-025) and ibuprofen (MED-026): Major triple combination (MP-06) |
| High-alert | No |
| Dataset patients | PAT-002 (5 days, 2025-03-03 to 2025-03-07); PAT-008 (long-term 81 mg); PAT-010 (over-the-counter 81 mg, stopped after bleed); **PAT-005 never given because of ALG-003** |

## 4. MED-011 Clopidogrel

| Item | Detail |
|---|---|
| Class | P2Y12 inhibitor |
| Indications | ACS (DIS-006) after stent; ischemic stroke when aspirin is contraindicated (DIS-011) |
| Adult dosing | 300 mg loading dose then 75 mg daily |
| Duration | After a coronary stent: **6 months with an anticoagulant**, **12 months without** (DG-01) |
| Renal / hepatic | No renal adjustment |
| GI protection | Add a proton pump inhibitor; pantoprazole (MED-028) preferred |
| Interactions | With apixaban or warfarin: Major (additive bleeding); with aspirin: Moderate (intended dual therapy) |
| High-alert | No |
| Dataset patients | PAT-002 (2025-03-04 to 2025-09-04; continued through GI bleed); PAT-005 (2026-04-14 to 2026-04-18, then stopped when apixaban began); PAT-008 (12 months from 2026-02-03) |

## 5. MED-012 Apixaban

| Item | Detail |
|---|---|
| Class | Direct oral anticoagulant (factor Xa inhibitor) |
| Indications | Stroke prevention in atrial fibrillation (DIS-005); venous thromboembolism (DIS-012) |
| Adult dosing | 5 mg twice daily |
| **Dose reduction** | **2.5 mg twice daily when at least two of three** are present: age 80 years or older; body weight 60 kg or less; creatinine 1.5 mg/dL (133 umol/L) or higher |
| Renal | Avoid below eGFR 15 (MP-07) |
| **Order verification (MediCore Policy FPA-04)** | Pharmacist verification of any new apixaban order **within 4 hours** (PRO-007, HO-04) |
| Holding rules | Hold before invasive procedures per pharmacist plan; hold during active bleeding; **resume 3 to 7 days after endoscopic hemostasis once hemoglobin is stable for 48 hours** (DG-07) |
| Monitoring | Creatinine/eGFR (LAB-004) and CBC (LAB-001) at least yearly |
| Interactions | Major with aspirin, clopidogrel, ibuprofen, warfarin (MP-06) |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-002 (5 mg twice daily; weight 58 kg is one criterion only, so no reduction); PAT-005 (from 2026-04-19; no criteria met) |

## 6. MED-013 Warfarin

| Item | Detail |
|---|---|
| Class | Vitamin K antagonist |
| Indications | AF (DIS-005); VTE (DIS-012) |
| Target INR (LAB-010) | **2.0 to 3.0** by default (FPA-05) |
| Starting dose | 5 mg daily, adjusted to INR; lower for elderly or underweight patients |
| INR-guided dose rules (MediCore Policy, PRO-007) | **Below 2.0:** increase weekly dose by 10 to 15%. **Above range up to 4.5:** reduce weekly dose by about 10% and **recheck within 3 days**. **Above 4.5:** hold 1 to 2 doses, **anticoagulation-clinic telephone call within 24 hours** (FPA-05), recheck next day |
| After discharge | **INR check within 72 hours of discharge** (FPA-05) |
| **Interacting drug started** | A written INR recheck plan is required before the interacting drug is first given (PRO-007) |
| Overlap with parenteral therapy | At least 5 days and until INR is 2.0 or higher on two consecutive checks (DG-06) |
| Key interactions | **Ciprofloxacin (MED-020): Major, raises INR**; amoxicillin-clavulanate and ceftriaxone: Moderate; NSAIDs and aspirin: Major; high-dose acetaminophen: Moderate (MP-06) |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-006 (5 mg then 4 mg from 2025-10-28; INR 6.8 on 2025-10-26, INC-003); PAT-011 (4 mg, reduced to 3.5 mg on 2026-02-02 at INR 3.4) |

## 7. MED-014 Heparin (Unfractionated)

| Item | Detail |
|---|---|
| Class | Parenteral anticoagulant, intravenous infusion |
| Indications | VTE (DIS-012); ACS (DIS-006) per protocol |
| Dosing | Weight-based bolus then infusion; **aPTT (LAB-011) target 60 to 80 seconds**, checked 6 hours after start and after each rate change |
| Monitoring | Platelet count (LAB-001) at baseline and every 2 to 3 days for heparin-induced thrombocytopenia |
| Renal | No adjustment; preferred over low-molecular-weight heparin below eGFR 30 |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-006 (infusion 2025-08-29 16:10 to 2025-09-02; aPTT 72 seconds at 6 hours) |

## 8. MED-015 Enoxaparin

| Item | Detail |
|---|---|
| Class | Low-molecular-weight heparin |
| Indications | VTE (DIS-012) |
| Dosing | **1 mg per kg subcutaneously every 12 hours** |
| Renal | eGFR below 30: 1 mg per kg once daily or switch to unfractionated heparin (MP-07, PRO-008) |
| Monitoring | Creatinine/eGFR (LAB-004); platelets |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-006 (80 mg every 12 hours, 2025-09-02 to 2025-09-07; weight 78 kg; eGFR 74) |

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Antithrombotic use in AF, ACS, stroke, VTE, GI bleed | DG-01, DG-06, DG-07 |
| Interaction severities | MP-06 |
| Allergy and renal dosing | MP-07 |
| INR, aPTT, CBC reports | LD-02 |
| Anticoagulation protocol | HO-04 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic monograph set (Pass 1) |
