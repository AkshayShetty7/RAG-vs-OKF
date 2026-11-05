---
doc_id: DG-07
title: "Hematology, GI and Hypersensitivity Guidelines (Fictional Reference)"
folder: 02_Diseases_Clinical_Guidelines
version: 1.0
created: 2026-10-01
synthetic: true
entities: [PAT-002, PAT-007, PAT-010, PAT-014, DIS-018, DIS-022, DIS-024, MED-010, MED-011, MED-012, MED-021, MED-024, MED-025, MED-026, MED-027, MED-028, MED-029, MED-031, LAB-001, LAB-010, LAB-025, PRO-001, PRO-003, DEP-001, DEP-002, INC-001, FPA-04, FPA-09, FPA-14]
related_docs: [DG-08, HO-02, HO-08, LD-02, MP-02, MP-03, MP-05, MP-06, MP-07, PR-02, PR-07, PR-08]
---

# DG-07: Hematology, GI and Hypersensitivity Guidelines (Fictional Reference)

> **SYNTHETIC DATA NOTICE.** This document is a fictional reference guideline written for software benchmarking and education. Its criteria, thresholds, and algorithms are invented, may differ from real-world practice, and must not be used for clinical decisions. "Reference Guideline" statements are kept separate from "MediCore Policy" statements owned by the HO documents.

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | DG-07 |
| Folder | 02_Diseases_Clinical_Guidelines |
| Version / date | 1.0 / 2026-10-01 |
| Conditions covered | Iron-deficiency anemia (DIS-018), upper GI bleeding (DIS-022), anaphylaxis and drug hypersensitivity (DIS-024) |
| Owner | Internal Medicine (DEP-002) with Emergency Medicine (DEP-001), approved by the CPRB |
| Companion documents | MP-02, MP-03, MP-05, MP-06, MP-07, LD-02, HO-02 |

## 2. Purpose and Scope

This guideline sets diagnostic criteria and management steps for three conditions that recur across the patient charts: anemia from iron deficiency (PAT-002, PAT-014), gastrointestinal bleeding (PAT-002, PAT-010), and anaphylaxis (PAT-007).

## 3. Iron-Deficiency Anemia (DIS-018)

### 3.1 Diagnostic criteria
Both of the following:

| Sex | Hemoglobin (LAB-001) | Ferritin (LAB-025) |
|---|---|---|
| Women | below **12.0 g/dL** | below **15 ng/mL** |
| Men | below 13.0 g/dL | below 15 ng/mL |

Supporting findings: low MCV, low transferrin saturation. Examples: PAT-014 (Hb 9.8 g/dL, ferritin 7 ng/mL, PR-08); PAT-002 (Hb 7.6 to 9.1 g/dL, ferritin 9 ng/mL, transferrin saturation 6%, PR-02).

### 3.2 Look for the source
Investigate gastrointestinal blood loss in all men and in postmenopausal women; in premenopausal and perimenopausal women consider menstrual loss and, when indicated, endoscopy (PAT-014 had both endoscopies; PR-08).

### 3.3 Treatment
Oral ferrous sulfate 325 mg once daily (MED-031), preferably with vitamin C and away from tea and coffee. Recheck hemoglobin at 4 weeks (expected rise of at least 1 g/dL). Continue for **3 months after hemoglobin normalizes** to restore stores. Intravenous iron is reserved for intolerance, malabsorption, or ongoing loss.

### 3.4 Interactions
Ferrous sulfate reduces levothyroxine (MED-024) absorption: separate by **at least 4 hours** (MediCore Policy FPA-14; MP-02, MP-06). PAT-014 illustrates the TSH rise after co-administration (PR-08).

## 4. Upper Gastrointestinal Bleeding (DIS-022)

### 4.1 Presentation and assessment
Melena or hematemesis, tachycardia, hypotension. Obtain CBC (LAB-001), PT/INR (LAB-010), ferritin (LAB-025) after resuscitation, type and screen. Review all antithrombotic and NSAID exposure including over-the-counter aspirin (PRO-001, HO-02).

### 4.2 Transfusion
Transfuse red cells when hemoglobin is below **7 g/dL**, or below **8 g/dL in patients with cardiovascular disease**. PAT-002 (coronary stent, Hb 7.6 g/dL) was transfused two units; PAT-010 (Hb 8.8 g/dL, no cardiovascular disease) was not (PR-02, PR-07).

### 4.3 Acid suppression
Proton pump inhibitor: pantoprazole (MED-028). For ulcers with high-risk stigmata (visible vessel, active bleeding): 80 mg IV bolus then 40 mg every 12 hours. For low-risk ulcers (clean base): 40 mg IV every 12 hours. Continue 40 mg twice daily for 8 weeks, then once daily for as long as antithrombotic therapy continues (MP-02).

### 4.4 Endoscopy
Within 24 hours of presentation after resuscitation. Test for Helicobacter pylori (stool antigen or biopsy) and treat if positive. Repeat endoscopy for healing is advised for ulcers with a visible vessel or when requested by gastroenterology (PAT-002, repeat 2025-08-12).

### 4.5 Managing antithrombotic drugs during bleeding

| Drug | Rule |
|---|---|
| Anticoagulant (apixaban, MED-012) | Hold. Resume 3 to 7 days after endoscopic hemostasis once hemoglobin has been stable for 48 hours. Pharmacist verifies the new order within 4 hours (FPA-04) |
| P2Y12 inhibitor (clopidogrel, MED-011) with a coronary stent placed within the last 6 months | **Continue** by joint decision of cardiology and gastroenterology |
| Aspirin (MED-010) and NSAIDs (MED-026) | Stop; do not restart NSAIDs |

PAT-002: apixaban held 2025-05-19 to 2025-05-23 (resumed day 4); clopidogrel continued because the stent was 11 weeks old (PR-02).

### 4.6 Preventing recurrence
Avoid NSAIDs; use acetaminophen (MED-027). An SSRI (MED-025) also raises bleeding risk. After an NSAID- or aspirin-associated bleed in a patient on an SSRI, follow DG-08 (stop NSAID and aspirin; continue the SSRI with a PPI if depression is stable). PAT-010 (PR-07).

## 5. Anaphylaxis and Drug Hypersensitivity (DIS-024)

### 5.1 Diagnosis
Acute onset of skin or mucosal involvement (urticaria, flushing, lip swelling) together with respiratory compromise or hypotension, or hypotension alone after exposure to a likely allergen.

### 5.2 First-line treatment
| Step | Rule |
|---|---|
| Remove trigger | Stop the suspected drug |
| **Epinephrine (MED-029)** | **0.5 mg intramuscular** into the anterolateral thigh in adults; **repeat every 5 to 15 minutes** if there is no improvement |
| Position and fluids | Lie flat, raise legs; IV crystalloid for hypotension |
| Adjuncts | Nebulized albuterol (MED-021) for wheeze |
| Observation | Minimum 6 hours; extend to **24 hours** when two or more epinephrine doses were needed |

PAT-007 received epinephrine 0.5 mg IM at 21:19 and again at 21:27 (8 minutes later) and was observed 24 hours (PR-07).

### 5.3 After the event
Prescribe an epinephrine auto-injector (MED-029) and teach use; update the allergy record with the confirmed reaction and severity; refer to allergy services; add cephalosporin cross-reactivity precautions where relevant (MP-07).

### 5.4 Allergy documentation
An allergy entry without verification, such as "rash, patient-reported, unverified," must not be treated as low risk. Before the first dose of a beta-lactam in any patient with an allergy flag, MediCore requires **dual verification** by pharmacist and nurse (PRO-003, FPA-09, HO-02). The failure of this step is the subject of INC-001 (HO-08).

## 6. Patient Applications in the Dataset

| Patient | Application | Chart |
|---|---|---|
| PAT-002 | GI bleed on apixaban and clopidogrel; iron deficiency | PR-02 |
| PAT-007 | Anaphylaxis to amoxicillin-clavulanate | PR-07 |
| PAT-010 | GI bleed on SSRI plus NSAID plus aspirin | PR-07 |
| PAT-014 | Iron-deficiency anemia with hypothyroidism | PR-08 |

## 7. Cross-Reference Table

| Topic | Where to verify |
|---|---|
| Pantoprazole, ferrous sulfate, levothyroxine monographs | MP-02 |
| Aspirin, clopidogrel, apixaban monographs | MP-03 |
| Ibuprofen, sertraline, epinephrine, albuterol monographs | MP-05 |
| Interaction severities | MP-06 |
| Allergy definitions and cross-reactivity | MP-07 |
| CBC, ferritin, INR reports | LD-02 |
| Allergy and reconciliation protocols | HO-02 |
| Related guideline | DG-08 |

## 8. Document Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | Initial synthetic guideline (Pass 1) |
