# Artifact Index - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* **Artifact Index**

## Artifact Index

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Structures: Logical Models 

These define data models that represent the domain covered by this implementation guide in more business-friendly terms than the underlying FHIR resources.

| | |
| :--- | :--- |
| [Medication Overview (Minimal)](StructureDefinition-MedicationOverviewMin.md) | Minimal medication overview payload for use within a QR code payload. Based on the IHE Pharmacy Medication Overview logical model, with short element labels (one or two letters) and simple data |
| [Medication Treatment Line (Minimal)](StructureDefinition-MedicationTreatmentLineMin.md) | Minimal medication treatment line payload for use within a QR code payload. Based on the IHE Pharmacy Medication Treatment Line logical model, with short element labels (one or two letters) and simple data types suitable for encoding in a compact QR code payload. |

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [SMART Bundle (IPS)](StructureDefinition-SmartIPS.md) | This profile represents the constraints applied to the Bundle resource by the International Patient Summary (IPS) for use within the SMART Guidelines.Note: The profile expects atleast one SMART Consent entry to be present. |
| [SMART Composition (IPS)](StructureDefinition-SmartIPSComposition.md) | This profile represents the constraints applied to the Composition resource by the International Patient Summary (IPS) for use within the SMART GuidelinesNote: The profile expects atleast one SMART Consent entry to be present within Advance Directives section |
| [SMART Consent](StructureDefinition-SmartConsent.md) | A profile of the consent resource to track consent of a pilgrim to participateFHIR R5 upgrade notes (need this implemented as a structure map):* make cardinality of decision 1.. and should stop using it in lieu of verification.verified
* use verification.verifiedBy instead of Consent.organization
* the period extenion should be replaced by Consent.period
* the Consent.patient should be replaced by Consent.subject
* Consent.verification.verifiedBy should be used instead of Consent.organization
 |

### Terminology: Structure Maps 

These define transformations to convert between data structures used by systems conforming to this implementation guide.

| |
| :--- |
| [MedicationOverviewLMToMedicationOverviewBundle](StructureMap-MedicationOverviewLMToMedicationOverviewBundle.md) |
| [MedicationOverviewMinToMedicationOverviewBundle](StructureMap-MedicationOverviewMinToMedicationOverviewBundle.md) |
| [MedicationOverviewMinToMedicationOverviewLM](StructureMap-MedicationOverviewMinToMedicationOverviewLM.md) |

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| | |
| :--- | :--- |
| [Example DocumentReference Consent Paperwork](DocumentReference-ex-documentreference1.md) | Example copied from FHIR-IPS used for Composition |
| [Example MedicationOverviewMin (compact QR payload)](Binary-574687583.md) | Minimal medication overview payload for Martha DeLarosa with two medication lines, suitable for QR code transmission. |
| [Example SMART Consent](Consent-c7781f44-6df8-4a8b-9e06-0b34263a47c6.md) | Example SMART Consent |
| [MedicationOverviewTransformed](Bundle-MedicationOverviewTransformed.md) |  |

