---
doc_id: LD-07
title: "Imaging Reports"
folder: 04_Laboratory_Diagnostics
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, PAT-005, PAT-006, PAT-012, LAB-020, LAB-022, LAB-027, PRO-009, DEP-012, STF-013, FPA-07]
related_docs: [DG-04, DG-06, HO-03, LD-01, LD-02, LD-04, PR-03, PR-05, PR-06, PR-08]
---

# LD-07: Imaging Reports

> **SYNTHETIC DATA NOTICE.** MediCore Hospital and every patient, finding, and report number in this document are fictional. The reports exist only for software benchmarking and education and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | LD-07 |
| Folder | 04_Laboratory_Diagnostics |
| Version / date | 1.0 / 2026-10-01 |
| Performing department | Radiology and Imaging (DEP-012, head STF-013) |
| Tests | LAB-020 chest X-ray, LAB-022 CT head non-contrast, LAB-027 CT pulmonary angiogram |
| Targets (LD-01, HO-03) | Stroke CT read within 10 minutes of scan; other urgent reads within 60 minutes; stroke-code door-to-CT-start 20 minutes (FPA-07) |
| Related documents | PR-03, PR-05, PR-06, PR-08; DG-04, DG-06; HO-03 |

## 2. Purpose and Scope

Imaging reports for four patients. Imaging is not a PRO-009 test; urgent findings are communicated by the radiologist directly under the radiology policy.

## 3. PAT-003 (Thomas Okonkwo-Reyes)

| Report | Date and time | Study | Findings | Impression |
|---|---|---|---|---|
| RPT-LD07-001 | 2026-02-26 09:55 | Chest X-ray (LAB-020) | **Right lower lobe consolidation** with air bronchograms; no effusion | Lobar pneumonia (DG-04) |
| RPT-LD07-002 | 2026-04-22 | Chest X-ray | **Consolidation resolved**; hyperinflated lungs | Resolution; changes of COPD |

## 4. PAT-005 (Samuel Adeyemi-Clarke)

| Report | Date and time | Study | Findings | Impression |
|---|---|---|---|---|
| RPT-LD07-003 | **2026-04-14 19:14 (scan start)**; read 19:20 | CT head, non-contrast (LAB-022) | **No intracranial hemorrhage.** Early hypodensity in the left middle cerebral artery territory | Acute ischemic stroke. Door time 18:55, so door-to-CT start **19 minutes** (target 20, FPA-07); read 6 minutes after scan start |
| RPT-LD07-004 | 2026-04-18 | CT head, non-contrast | Evolving infarct as expected; **no hemorrhagic transformation** | Day 4: allows anticoagulation to start on day 5 (DG-06) |

## 5. PAT-006 (Grace Lindqvist-Obi)

| Report | Date and time | Study | Findings | Impression |
|---|---|---|---|---|
| RPT-LD07-005 | **2025-08-29 14:40 (scan start)**; report issued **15:25** | CT pulmonary angiogram (LAB-027) | **Segmental and subsegmental emboli in the right lower lobe.** No right ventricular strain. Main pulmonary arteries clear | Pulmonary embolism; follows D-dimer 3,850 ng/mL FEU (LD-02). Report issued 45 minutes after scan start |

## 6. PAT-012 (Mei-Ling Castellanos)

| Report | Date | Study | Findings | Impression |
|---|---|---|---|---|
| RPT-LD07-006 | 2026-05-05 | Chest X-ray (LAB-020) | **Right middle lobe infiltrate** | Pneumonia, non-severe (DG-04) |
| RPT-LD07-007 | 2026-06-19 | Chest X-ray | **Clear** | Resolution |

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Time targets | LD-01, HO-03 |
| Pneumonia criteria | DG-04 |
| Stroke and PE criteria | DG-06 |
| Related laboratory reports | LD-02 (D-dimer), LD-04 (procalcitonin) |
| Patient charts | PR-03, PR-05, PR-06, PR-08 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic report series (Pass 1) |
