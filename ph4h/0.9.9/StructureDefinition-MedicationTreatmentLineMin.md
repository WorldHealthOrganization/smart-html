# Medication Treatment Line (Minimal) - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **Medication Treatment Line (Minimal)**

## Logical Model: Medication Treatment Line (Minimal) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureDefinition/MedicationTreatmentLineMin | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:MedicationTreatmentLineMin |

 
Minimal medication treatment line payload for use within a QR code payload. Based on the IHE Pharmacy Medication Treatment Line logical model, with short element labels (one or two letters) and simple data types suitable for encoding in a compact QR code payload. 

**Usages:**

* Use this Logical Model: [Medication Overview (Minimal)](StructureDefinition-MedicationOverviewMin.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.ph4h|current/StructureDefinition/StructureDefinition-MedicationTreatmentLineMin.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-MedicationTreatmentLineMin.csv), [Excel](StructureDefinition-MedicationTreatmentLineMin.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "MedicationTreatmentLineMin",
  "url" : "http://smart.who.int/ph4h/StructureDefinition/MedicationTreatmentLineMin",
  "version" : "0.9.9",
  "name" : "MedicationTreatmentLineMin",
  "title" : "Medication Treatment Line (Minimal)",
  "status" : "draft",
  "date" : "2026-07-09T08:34:46+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Minimal medication treatment line payload for use within a QR code payload. Based on the IHE Pharmacy Medication Treatment Line logical model, with short element labels (one or two letters) and simple data types suitable for encoding in a compact QR code payload.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/ph4h/StructureDefinition/MedicationTreatmentLineMin",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "MedicationTreatmentLineMin",
      "path" : "MedicationTreatmentLineMin",
      "short" : "Medication Treatment Line (Minimal)",
      "definition" : "Minimal medication treatment line payload for use within a QR code payload. Based on the IHE Pharmacy Medication Treatment Line logical model, with short element labels (one or two letters) and simple data types suitable for encoding in a compact QR code payload."
    },
    {
      "id" : "MedicationTreatmentLineMin.m",
      "path" : "MedicationTreatmentLineMin.m",
      "short" : "Medication (Active Ingredient)",
      "definition" : "Active ingredient of the medication.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    },
    {
      "id" : "MedicationTreatmentLineMin.es",
      "path" : "MedicationTreatmentLineMin.es",
      "short" : "Effective Start Date",
      "definition" : "Start date during which the medication treatment line is effective.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "MedicationTreatmentLineMin.ee",
      "path" : "MedicationTreatmentLineMin.ee",
      "short" : "Effective End Date",
      "definition" : "End date during which the medication treatment line is effective.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "MedicationTreatmentLineMin.da",
      "path" : "MedicationTreatmentLineMin.da",
      "short" : "Date Asserted",
      "definition" : "Date the medication treatment line was asserted/recorded.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "MedicationTreatmentLineMin.d",
      "path" : "MedicationTreatmentLineMin.d",
      "short" : "Dosage",
      "definition" : "Dosage instructions as free text.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "MedicationTreatmentLineMin.r",
      "path" : "MedicationTreatmentLineMin.r",
      "short" : "Reason",
      "definition" : "Reason why the product has been prescribed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "MedicationTreatmentLineMin.a",
      "path" : "MedicationTreatmentLineMin.a",
      "short" : "Adherence Status",
      "definition" : "Status of patient adherence to the medication treatment line",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://hl7.org/fhir/ValueSet/medication-statement-status"
      }
    }]
  }
}

```
