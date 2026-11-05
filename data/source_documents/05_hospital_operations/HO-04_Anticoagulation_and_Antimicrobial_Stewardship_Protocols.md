---
doc_id: HO-04
title: "Anticoagulation and Antimicrobial Stewardship Protocols"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, PAT-003, PAT-005, PAT-006, PAT-011, PAT-012, PAT-013, PRO-004, PRO-007, PRO-009, PRO-011, PRO-013, DEP-007, DEP-010, INC-003, INC-006, FPA-04, FPA-05, FPA-11]
related_docs: [DG-01, DG-05, DG-06, DG-07, HO-03, HO-05, HO-07, HO-08, LD-02, LD-05, MP-03, MP-04, MP-06, PR-02, PR-03, PR-05, PR-06, PR-08]
---

# HO-04: Anticoagulation and Antimicrobial Stewardship Protocols

> **SYNTHETIC DATA NOTICE.** These protocols are fictional MediCore Policy written for software benchmarking and education. Every time target, threshold, and rule is an invented parameter that may differ from real practice and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-04 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 |
| Protocols | PRO-007 anticoagulation management and monitoring; PRO-013 antimicrobial stewardship |
| Owners | DEP-010 (PRO-007, with the anticoagulation clinic); DEP-007 and the ASC (PRO-013); approved by the CPRB |
| Clinical rules | DG-01, DG-05, DG-06, DG-07; MP-03, MP-04 |
| Version history | HO-08 |

## 2. PRO-007: Anticoagulation Management and Monitoring

### 2.1 Version history

| Version | Effective | Change |
|---|---|---|
| 1 | 2023-01-01 to 2025-11-30 | Core rules below; the INR recheck plan was a free-text expectation |
| **2** | **2025-12-01** | INR recheck plan becomes a **mandatory structured field**: an order for a drug in the MP-06 warfarin interaction list cannot be signed without it (after INC-003) |

### 2.2 Rules (apply to both versions unless stated)

| Rule | Requirement |
|---|---|
| New apixaban order | **Pharmacist verification within 4 hours** (FPA-04) |
| Anticoagulant plus antiplatelet | Pharmacist review of every combination (DG-01) |
| Default warfarin target | **INR 2.0 to 3.0** (FPA-05) |
| Parenteral overlap | Continue heparin or enoxaparin for **at least 5 days and until INR is 2.0 or higher on two consecutive checks** (DG-06) |
| INR below 2.0 | Increase weekly dose by 10 to 15% |
| **INR above range up to 4.5** | Reduce weekly dose by about 10% and **recheck INR within 3 days** |
| **INR above 4.5** | Hold 1 to 2 doses; **anticoagulation-clinic telephone call within 24 hours** (FPA-05); recheck the next day |
| Critical INR | **5.0 or higher** is also a PRO-009 critical result, phoned within 20 minutes (HO-05) |
| **After discharge** | **INR check within 72 hours of discharge** for every patient on warfarin (FPA-05); also scheduled in the discharge plan (PRO-011, HO-07) |
| **Interacting drug started** | A **written INR recheck plan** must exist before the first dose of an interacting drug (MP-06), with an INR within 3 days; in version 2 this is enforced by the order screen |
| Bleeding | Apixaban held; resumption 3 to 7 days after hemostasis once hemoglobin is stable for 48 hours, with pharmacist verification in 4 hours (DG-07) |

### 2.3 Worked examples

| Patient | Event | Rule applied | Result |
|---|---|---|---|
| PAT-006 | Parenteral therapy 2025-08-29 to 2025-09-07; INR 2.3 and 2.6 on 2025-09-06 and 2025-09-07 | Overlap at least 5 days and INR 2.0 or higher twice | Met (10 days) |
| PAT-006 | Ciprofloxacin started 2025-10-21; INR 6.8 on 2025-10-26 (critical, phoned in 16 minutes); clinic call 2 h 45 min after verification | INR recheck plan required (version 1); call within 24 hours | Plan not made: INC-003; call met |
| PAT-011 | INR 3.4 on 2026-02-02; dose reduced from 4 mg to 3.5 mg daily; recheck 2026-02-05 (INR 2.8) | Above range up to 4.5: recheck within 3 days | Met |
| PAT-011 | First discharge 2026-01-17 14:30; INR deadline 2026-01-20 14:30 | INR within 72 hours | Not done: INC-006; at second discharge INR 2.6 on 2026-02-10, met |
| PAT-002 | Apixaban orders 2025-03-05 08:00 and 2025-05-23 08:15; verified in 72 and 85 minutes | Verification within 4 hours | Met |
| PAT-005 | Apixaban order 2026-04-19 08:30; verified 10:05 (95 minutes) | Verification within 4 hours | Met |

## 3. PRO-013: Antimicrobial Stewardship

### 3.1 Version history

| Version | Effective | Change |
|---|---|---|
| 1 | 2023-06-01 to 2025-08-31 | Culture review at 72 hours |
| **2** | **2025-09-01** | Level timing rule and 48-hour review added |

### 3.2 Rules (version 2)

| Rule | Requirement |
|---|---|
| Cultures first | Blood cultures before the first antibiotic where feasible (PRO-004, HO-03) |
| **Vancomycin levels (FPA-11)** | IV vancomycin is pharmacy-managed; the **first level is drawn before the fourth dose**. A level above 20 mg/L prompts holding the next dose and re-dosing by pharmacy (MP-04) |
| **48-hour review** | Every broad-spectrum course is reviewed by stewardship at 48 hours. **IV vancomycin is stopped at 48 hours if no resistant gram-positive organism has been identified** |
| De-escalation | When susceptibilities are available, narrow to the most selective effective agent; stewardship documents the decision within 24 hours of the report |
| Duration | Follows DG-05: non-severe CAP minimum 5 days, severe or bacteremic pneumococcal pneumonia 7 days, complicated UTI 7 days, C. difficile 10 days |
| **Procalcitonin stop rule (MediCore Policy)** | In non-severe pneumonia, antibiotics **may stop at day 5 when procalcitonin is below 0.25 ng/mL and the patient has been afebrile for at least 48 hours** |
| Interaction check | Antibiotic orders are checked against MP-06 (for example ciprofloxacin with warfarin) |

### 3.3 Worked examples

| Patient | Event | Rule applied | Result |
|---|---|---|---|
| PAT-003 | Vancomycin 02-27 07:20, 19:20, 02-28 07:20; level 02-28 18:50 (30 minutes before dose 4), 14.8 mg/L; susceptibility report 03-01 08:20, de-escalation 13:00 | Level before dose 4; de-escalation within 24 hours | Met |
| PAT-013 | Vancomycin doses 06-18 05:10, 17:10, 06-19 05:10; level 06-19 16:40 (30 minutes before dose 4), 24.1 mg/L above 20, dose held and interval extended; stopped 06-20 (48 hours) with only gram-negative organisms | Level before dose 4; hold above 20 mg/L; 48-hour stop | Met |
| PAT-012 | Procalcitonin 0.18 ng/mL on 2026-05-07; afebrile since 2026-05-06 06:00; antibiotics stopped after the dose of 2026-05-09 (day 5) | Procalcitonin stop rule | Met |
| PAT-006 | Ciprofloxacin course reduced to 5 days after the INR event; negative repeat culture 2025-11-04 | Stewardship review accepted the shorter course | Accepted |

## 4. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Anticoagulant and antibiotic monographs | MP-03, MP-04 |
| Interaction severities | MP-06 |
| Sepsis, stroke, VTE, CAP, UTI, GI bleed guidelines | DG-05, DG-06, DG-07, DG-01 |
| INR and aPTT reports; culture reports | LD-02, LD-05 |
| Critical result notification | HO-05 |
| Discharge follow-up | HO-07 |
| Incident review and version history | HO-08 |
| Patient charts | PR-02, PR-03, PR-05, PR-06, PR-08 |

## 5. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic protocols (Pass 1) |
