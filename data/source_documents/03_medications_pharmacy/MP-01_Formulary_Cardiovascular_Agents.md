---
doc_id: MP-01
title: "Formulary Monographs: Cardiovascular Agents"
folder: 03_Medications_Pharmacy
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-001, PAT-002, PAT-005, PAT-008, PAT-009, PAT-010, PAT-011, DIS-002, DIS-004, DIS-005, DIS-006, DIS-014, MED-004, MED-005, MED-006, MED-007, MED-008, MED-009, MED-019, MED-021, MED-026, MED-029, LAB-004, LAB-005, LAB-006, LAB-009, LAB-021, PRO-002, DEP-010, STF-002, ALG-002, ALG-004]
related_docs: [DG-01, DG-02, DG-03, DG-04, HO-02, LD-01, LD-03, MP-06, MP-07]
---

# MP-01: Formulary Monographs, Cardiovascular Agents

> **SYNTHETIC DATA NOTICE.** This formulary is fictional and was written for software benchmarking and education. Doses, thresholds, and rules are invented, may differ from real-world practice, and must not be used for clinical decisions. "MediCore Policy" items are invented parameters.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | MP-01 |
| Folder | 03_Medications_Pharmacy |
| Version / date | 1.0 / 2026-10-01 |
| Owner | Clinical Pharmacy (DEP-010, Chief Pharmacist STF-002), approved by the Pharmacy and Therapeutics Committee (P&T) |
| Medications covered | MED-004 lisinopril, MED-005 amlodipine, MED-006 metoprolol succinate, MED-007 furosemide, MED-008 spironolactone, MED-009 atorvastatin |
| Related documents | DG-01, DG-02, DG-03 (clinical rules); MP-06 (interactions); MP-07 (allergy and organ-function dosing); HO-02 (protocols) |

## 2. Purpose and Scope

Each monograph gives class, indications, adult dosing, kidney and liver adjustments, monitoring tests, contraindications, key interactions, and the patients in this dataset who received the drug. Interaction severities are owned by MP-06 and renal tiers by MP-07; they are repeated here only as pointers. The standard severity scale is Contraindicated, Major, Moderate, Minor.

## 3. MED-004 Lisinopril

| Item | Detail |
|---|---|
| Class | ACE inhibitor |
| Indications | Hypertension (DIS-002); HFrEF (DIS-004); post-ACS when LVEF is below 50% (DG-01) |
| Adult dosing | Start 2.5 to 10 mg daily; usual range 5 to 40 mg daily; HFrEF target 20 to 40 mg daily |
| Renal adjustment | eGFR 30 to 44: start 2.5 to 5 mg, maximum 20 mg/day; eGFR 15 to 29: start 2.5 mg, maximum 10 mg/day, specialist supervision; below 15: avoid unless nephrology agrees (MP-07) |
| Monitoring | Potassium (LAB-005) and creatinine/eGFR (LAB-004) at baseline, 1 week, and 1 week after each dose increase; blood pressure |
| Contraindications | **History of ACE-inhibitor angioedema (ALG-004): absolute.** Pregnancy; bilateral renal artery stenosis |
| Hold during | Vomiting, diarrhea, poor intake (sick-day rule, DG-01); hyperkalemia (DG-03); AKI |
| Key interactions | Spironolactone (MED-008): hyperkalemia, Major in CKD; ibuprofen (MED-026): kidney injury and reduced antihypertensive effect, Major, and with furosemide the "triple" combination (MP-06) |
| High-alert (PRO-002) | No |
| Dataset patients | PAT-001 (20 mg, held and restarted at 5 mg then 10 mg); PAT-009 (5 mg, held during AKI, resumed 2026-03-31); **PAT-008 not prescribed because of ALG-004** |

## 4. MED-005 Amlodipine

| Item | Detail |
|---|---|
| Class | Dihydropyridine calcium-channel blocker |
| Indications | Hypertension (DIS-002) |
| Adult dosing | 5 mg daily, increase to 10 mg daily |
| Renal / hepatic | No renal adjustment; start 2.5 mg in severe hepatic impairment |
| Monitoring | Blood pressure; ankle edema |
| Contraindications | Severe aortic stenosis; cardiogenic shock |
| Key interactions | None Major in this formulary; additive hypotension with other antihypertensives |
| High-alert | No |
| Dataset patients | PAT-005 (5 mg since 2008; 10 mg from 2026-04-20) |

## 5. MED-006 Metoprolol Succinate

| Item | Detail |
|---|---|
| Class | Cardioselective beta-blocker, extended release |
| Indications | HFrEF (DIS-004); atrial fibrillation rate control (DIS-005); post-ACS (DIS-006); hypertension (DIS-002) |
| Adult dosing | Start 25 to 50 mg daily; target 100 to 200 mg daily; double at 2-week intervals if heart rate above 60 and systolic pressure above 100 mmHg |
| Renal / hepatic | No renal adjustment; reduce in severe hepatic impairment |
| Monitoring | Heart rate, blood pressure; ECG (LAB-021) if bradycardia |
| Contraindications | Heart rate below 50 with symptoms; second- or third-degree block; decompensated heart failure on initiation |
| Cautions | Asthma: cardioselective agents only with monitoring (DG-04). Epinephrine in anaphylaxis may be less effective (MED-029, MP-06) |
| High-alert | No |
| Dataset patients | PAT-001 (100 mg); PAT-002 (50 mg then 100 mg from 2025-03-07); PAT-008 (25 mg then 50 mg); PAT-011 (50 mg) |

## 6. MED-007 Furosemide

| Item | Detail |
|---|---|
| Class | Loop diuretic. Contains a sulfonamide group that is **not** an antibiotic (see ALG-002 in MP-07) |
| Indications | Congestion in HFrEF (DIS-004); edema |
| Adult dosing | 20 to 80 mg daily orally, in one or two doses; IV for acute decompensation |
| Renal adjustment | Dose-response is blunted at low eGFR; higher doses may be needed. No dose reduction (MP-07) |
| Monitoring | Daily weights; potassium (LAB-005), sodium (LAB-006), creatinine (LAB-004) |
| Contraindications | Anuria; severe volume depletion |
| Hold during | Vomiting, diarrhea, poor oral intake |
| Key interactions | Ibuprofen (MED-026): reduced diuretic effect and kidney injury; albuterol (MED-021): hypokalemia; vancomycin (MED-019): additive ototoxicity and nephrotoxicity, Moderate |
| High-alert | No |
| Dataset patients | PAT-001 (40 mg daily); PAT-009 (20 mg daily, held during AKI); PAT-011 (40 mg twice daily from 2026-01-17) |

## 7. MED-008 Spironolactone

| Item | Detail |
|---|---|
| Class | Mineralocorticoid receptor antagonist |
| Indications | HFrEF (DIS-004) |
| Adult dosing | 12.5 to 50 mg daily; usual HF dose 25 mg daily |
| Renal adjustment | eGFR 45 or higher: start 25 mg; **eGFR 30 to 44: start 12.5 mg daily**; below 30: avoid (MP-07) |
| Start criteria | Potassium 5.0 mmol/L or lower and eGFR 30 or higher (DG-01) |
| Monitoring | **Potassium and creatinine at 1 week and 4 weeks** after start or dose increase, then at each visit; do not increase when potassium is above 5.0 mmol/L |
| Hold | Potassium 5.5 mmol/L or higher (DG-03); vomiting or diarrhea (sick-day rule) |
| Key interactions | Lisinopril (MED-004): hyperkalemia, **Major in CKD**; potassium-containing salt substitutes; ibuprofen (MED-026) |
| High-alert | No |
| Dataset patients | PAT-001 (25 mg from 2024-06-04; held 2025-09-17; resumed 12.5 mg on 2025-10-23); PAT-011 (25 mg) |

## 8. MED-009 Atorvastatin

| Item | Detail |
|---|---|
| Class | HMG-CoA reductase inhibitor (statin) |
| Indications | Hyperlipidemia (DIS-014); ACS (DIS-006); stroke prevention |
| Adult dosing | 40 mg daily for high risk; **80 mg daily after ACS** (DG-02) |
| Renal / hepatic | No renal adjustment; contraindicated in active liver disease |
| Monitoring | Lipid panel (LAB-009) 6 to 8 weeks after start; report muscle symptoms |
| Contraindications | Active liver disease; pregnancy |
| Key interactions | Moderate with some macrolides and azoles (not in this formulary) |
| High-alert | No |
| Dataset patients | PAT-002 (80 mg from 2025-03-04); PAT-008 (80 mg); PAT-010 (40 mg); PAT-001 |

## 9. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Clinical use and targets | DG-01, DG-02, DG-03 |
| Interaction severities | MP-06 |
| Allergy and renal tiers | MP-07 |
| Lab reference ranges | LD-01 |
| Potassium and creatinine reports | LD-03 |
| Renal dose and reconciliation protocols | HO-02 |

## 10. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic monograph set (Pass 1) |
