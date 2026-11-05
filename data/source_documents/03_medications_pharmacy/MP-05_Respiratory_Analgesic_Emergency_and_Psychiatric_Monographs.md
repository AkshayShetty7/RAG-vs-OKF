---
doc_id: MP-05
title: "Monographs: Respiratory, Analgesic, Emergency and Psychiatric"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, PAT-005, PAT-006, PAT-007, PAT-009, PAT-010, DIS-003, DIS-007, DIS-015, DIS-017, DIS-020, DIS-021, DIS-024, MED-006, MED-010, MED-021, MED-022, MED-023, MED-025, MED-026, MED-027, MED-029, LAB-005, PRO-002, DEP-010, STF-002, ALG-003, INC-001, INC-005]
related_docs: [DG-03, DG-04, DG-07, DG-08, HO-02, MP-06, MP-07]
---

# MP-05: Monographs, Respiratory, Analgesic, Emergency and Psychiatric

> **SYNTHETIC DATA NOTICE.** This formulary is fictional and was written for software benchmarking and education. Doses, thresholds, and rules are invented, may differ from real-world practice, and must not be used for clinical decisions. "MediCore Policy" items are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-05 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, STF-002), approved by the P&T Committee |
| Medications covered | MED-021 albuterol, MED-022 tiotropium, MED-023 prednisone, MED-025 sertraline, MED-026 ibuprofen, MED-027 acetaminophen, MED-029 epinephrine |
| Related documents | DG-04, DG-07, DG-08, DG-03; MP-06; MP-07; HO-02 |

## 2. Purpose and Scope

Monographs for seven agents with very different uses. Two of them, ibuprofen and epinephrine, are central to safety events in the dataset: an NSAID given to a patient with CKD (INC-005) and epinephrine for anaphylaxis (INC-001).

## 3. MED-021 Albuterol

| Item | Detail |
|---|---|
| Class | Short-acting beta-2 agonist |
| Indications | Asthma (DIS-015); COPD exacerbation (DIS-007); adjunct for wheeze in anaphylaxis (DIS-024) |
| Adult dosing | Inhaler 100 micrograms per puff, 2 puffs as needed; nebulized 2.5 mg every 4 hours initially in exacerbation |
| Monitoring | Heart rate; potassium (LAB-005) with repeated high doses |
| Interactions | Furosemide: additive hypokalemia, Moderate; metoprolol: antagonism reduced with cardioselective dosing, Moderate (MP-06) |
| Dataset patients | PAT-003 (nebulized, 2026-02-26 onward); PAT-005 (as needed); PAT-007 (as needed; nebulized during anaphylaxis) |

## 4. MED-022 Tiotropium

| Item | Detail |
|---|---|
| Class | Long-acting antimuscarinic bronchodilator |
| Indications | COPD maintenance (DIS-007) |
| Adult dosing | 18 micrograms inhaled once daily |
| Cautions | Urinary retention, narrow-angle glaucoma; reduce use with eGFR below 60 only under supervision |
| Dataset patients | PAT-003 (home medication, continued) |

## 5. MED-023 Prednisone

| Item | Detail |
|---|---|
| Class | Systemic corticosteroid |
| Indications | COPD exacerbation (DIS-007); asthma exacerbation (DIS-015) |
| Adult dosing | **40 mg once daily for 5 days** (DG-04) |
| Monitoring | Glucose in patients with diabetes |
| Interactions | Ibuprofen: Major GI bleeding risk; ciprofloxacin: tendon risk, Moderate; insulin: hyperglycemia, Moderate |
| Dataset patients | PAT-003 (2026-02-26 to 2026-03-02); PAT-007 (2026-05-17) |

## 6. MED-025 Sertraline

| Item | Detail |
|---|---|
| Class | Selective serotonin reuptake inhibitor (SSRI) |
| Indications | Major depressive disorder (DIS-020) |
| Adult dosing | Start 50 mg daily; usual 50 to 200 mg daily; review at 4 to 6 weeks |
| Renal | No adjustment |
| **Bleeding risk** | Impairs platelet function. With ibuprofen (MED-026) and aspirin (MED-010) together: **Major** (MP-06). After a GI bleed, **continue sertraline with a proton pump inhibitor** if depression is stable (DG-08) |
| Cautions | Hyponatremia in older adults; serotonin syndrome with other serotonergic drugs |
| Dataset patients | PAT-010 (100 mg daily since 2023-02; continued after bleed) |

## 7. MED-026 Ibuprofen

| Item | Detail |
|---|---|
| Class | NSAID |
| Indications | Short-term pain and inflammation (osteoarthritis, DIS-021) when no contraindication |
| Adult dosing | 400 to 600 mg three times daily with food; maximum 2,400 mg/day |
| **Contraindications** | **CKD or AKI (DIS-003, DIS-017); NSAID/aspirin hypersensitivity (ALG-003); active or recent GI bleeding; anticoagulant therapy; heart failure** (DG-03, DG-07, DG-08, MP-07) |
| Interactions | Lisinopril plus furosemide: Major kidney-injury "triple" combination; warfarin, apixaban, aspirin, sertraline: Major bleeding; prednisone: Major (MP-06) |
| Preferred alternative | Acetaminophen (MED-027) |
| Dataset patients | PAT-009 (prescribed 2026-03-05, INC-005; stopped 2026-03-22); PAT-010 (prescribed 2026-04-14; stopped 2026-06-10); **PAT-005 avoided because of ALG-003** |

## 8. MED-027 Acetaminophen

| Item | Detail |
|---|---|
| Class | Analgesic and antipyretic |
| Indications | Mild to moderate pain; osteoarthritis first-line (DG-08); fever |
| Adult dosing | 650 mg every 6 hours as needed; **maximum 3 g per day** |
| Hepatic | Reduce maximum to 2 g per day in chronic liver disease |
| Interactions | Sustained doses above 2 g per day can raise the INR on warfarin, Moderate (MP-06) |
| Hypersensitivity | Tolerated by patients with ALG-003 at standard doses (MP-07) |
| Dataset patients | PAT-006 (post-operative and UTI pain); PAT-009 (650 mg every 6 hours after AKI); PAT-010 (arthritis pain after the bleed) |

## 9. MED-029 Epinephrine

| Item | Detail |
|---|---|
| Class | Catecholamine |
| Indications | Anaphylaxis (DIS-024) |
| **Adult dosing** | **0.5 mg intramuscular** into the anterolateral thigh; **repeat every 5 to 15 minutes** if no improvement (DG-07) |
| Outpatient | Prescribe an auto-injector and teach use after the event |
| Cautions | Palpitations, tremor; beta-blockers (MED-006) can blunt the response, Major (MP-06) |
| High-alert (PRO-002) | **Yes** |
| Dataset patients | PAT-007 (0.5 mg IM at 21:19 and 21:27 on 2026-05-17; auto-injector at discharge) |

## 10. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Respiratory, anaphylaxis, GI bleed, depression, osteoarthritis guidelines | DG-04, DG-07, DG-08 |
| NSAID and CKD | DG-03 |
| Interaction severities | MP-06 |
| Allergy and renal dosing | MP-07 |
| Medication safety protocols | HO-02 |

## 11. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic monograph set (Pass 1) |
