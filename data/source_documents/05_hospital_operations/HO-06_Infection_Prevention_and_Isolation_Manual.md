---
doc_id: HO-06
title: "Infection Prevention and Isolation Manual"
folder: 05_Hospital_Operations
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-003, DIS-023, LAB-024, PRO-009, PRO-012, DEP-013, STF-014, INC-004, FPA-10]
related_docs: [DG-05, HO-04, HO-05, HO-08, LD-05, MP-04, PR-03]
---

# HO-06: Infection Prevention and Isolation Manual

> **SYNTHETIC DATA NOTICE.** This protocol is fictional MediCore Policy written for software benchmarking and education. Every time target, duration, and rule is an invented parameter that may differ from real practice and must not be used for clinical decisions.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | HO-06 |
| Folder | 05_Hospital_Operations |
| Version / date | 1.0 / 2026-10-01 |
| Protocol | PRO-012 infection prevention and isolation |
| Owner | Quality, Patient Safety and Infection Control (DEP-013, STF-014); approved by the CPRB |
| Clinical rules | DG-05 (C. difficile) |
| Related documents | LD-05, HO-05, HO-08, PR-03 |

## 2. PRO-012: Version History

| Version | Effective | Change |
|---|---|---|
| 1 | 2023-01-01 to 2026-04-30 | Ward nurse starts precautions after being told by Infection Control |
| **2** | **2026-05-01** | On a laboratory call for a positive C. difficile result the **ward nurse starts contact-enteric precautions immediately**, before Infection Control confirms; LabLink notifies Infection Control automatically (after INC-004) |

## 3. Isolation Categories

| Category | Used for | Key measures |
|---|---|---|
| Standard | All patients | Hand hygiene, personal protective equipment by risk |
| Contact | Resistant organisms, wounds with drainage | Gown and gloves; single room preferred |
| **Contact-enteric** | **C. difficile infection (DIS-023)** | Gown and gloves; single room with dedicated toilet; **soap-and-water hand hygiene** (alcohol rub does not remove spores); dedicated equipment; sporicidal cleaning |
| Droplet | Influenza-like and pneumococcal outbreaks | Surgical mask; single room |
| Airborne | Open tuberculosis, measles | Negative-pressure room; respirator |

## 4. C. difficile Precautions (FPA-10)

1. **Trigger:** a positive C. difficile result (LAB-024), or three or more unformed stools in 24 hours in a patient at risk, which allows precautions to start before the result.
2. **Start:** immediately on the call from the laboratory (version 2); the ward nurse records the start time.
3. **Duration:** precautions continue until **72 hours after diarrhea has resolved** (formed stool or return to baseline, FPA-10). Discharge or transfer before that time requires the receiving unit to be informed.
4. **Room and toilet:** single room with dedicated toilet or commode; no shared bathroom.
5. **Cleaning:** sporicidal agent daily and at terminal clean.
6. **Antibiotic review:** stewardship (HO-04) reviews the need for the inciting antibiotic.
7. **Treatment:** oral vancomycin 125 mg every 6 hours for 10 days (DG-05, MP-04).

## 5. Outbreak Triggers

Two or more hospital-onset C. difficile cases on the same ward within 7 days, or any cluster of three or more related infections, prompt notification of the Head of Infection Control, a ward review and enhanced cleaning. No outbreak was declared in the dataset.

## 6. Worked Example: PAT-003 and INC-004

| Event (2026) | Time |
|---|---|
| Watery diarrhea begins | 03-06 evening; stool sent 22:10 |
| Result positive, verified | 03-07 08:40 |
| Laboratory phones ward nurse | 08:52 (12 minutes; compliant with PRO-009) |
| Infection Prevention notified by the charge nurse | 14:50 |
| **Contact-enteric precautions started** | **15:25 (6 h 45 min after verification)** |
| Diarrhea resolved | 03-12 06:00 |
| **Precautions ended** | **03-15 06:00 (72 hours after resolution, FPA-10)** |
| Discharge | 03-16 10:20 |

Under version 1 the nurse waited for Infection Control; this produced the delay reported as **INC-004** (HO-08). During the delay the patient used a shared bathroom with one other patient. Screening of that patient found no secondary case, and no outbreak criteria were met (PR-03, LD-05).

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| C. difficile diagnosis and treatment | DG-05 |
| Result calling | HO-05, LD-05 |
| Stewardship | HO-04 |
| Incident review and version history | HO-08 |
| Patient chart | PR-03 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic manual (Pass 1) |
