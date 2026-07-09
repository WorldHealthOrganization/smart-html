# Medication Overview (Minimal) - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **Medication Overview (Minimal)**

## Logical Model: Medication Overview (Minimal) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureDefinition/MedicationOverviewMin | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:MedicationOverviewMin |

 
Minimal medication overview payload for use within a QR code payload. Based on the IHE Pharmacy Medication Overview logical model, with short element labels (one or two letters) and simple data 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.ph4h|current/StructureDefinition/StructureDefinition-MedicationOverviewMin.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-MedicationOverviewMin.csv), [Excel](StructureDefinition-MedicationOverviewMin.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "MedicationOverviewMin",
  "url" : "http://smart.who.int/ph4h/StructureDefinition/MedicationOverviewMin",
  "version" : "0.9.9",
  "name" : "MedicationOverviewMin",
  "title" : "Medication Overview (Minimal)",
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
  "description" : "Minimal medication overview payload for use within a QR code payload. Based on the IHE Pharmacy Medication Overview logical model, with short element labels (one or two letters) and simple data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/ph4h/StructureDefinition/MedicationOverviewMin",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "MedicationOverviewMin",
      "path" : "MedicationOverviewMin",
      "short" : "Medication Overview (Minimal)",
      "definition" : "Minimal medication overview payload for use within a QR code payload. Based on the IHE Pharmacy Medication Overview logical model, with short element labels (one or two letters) and simple data",
      "constraint" : [{
        "key" : "MedicationOverviewMin-TreatmentLines",
        "severity" : "error",
        "human" : "If more than one medication treatment line is present, there can be a maximum of 3 medication treatment lines to ensure the overall payload remains compact enough for encoding in a QR code.",
        "expression" : "m.count() <= 3",
        "source" : "http://smart.who.int/ph4h/StructureDefinition/MedicationOverviewMin"
      }]
    },
    {
      "id" : "MedicationOverviewMin.n",
      "path" : "MedicationOverviewMin.n",
      "short" : "Patient Name",
      "definition" : "Patient Name",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "MedicationOverviewMin.dob",
      "path" : "MedicationOverviewMin.dob",
      "short" : "Patient Date of Birth",
      "definition" : "Patient Date of Birth",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "MedicationOverviewMin.s",
      "path" : "MedicationOverviewMin.s",
      "short" : "Sex",
      "definition" : "Sex",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://hl7.org/fhir/ValueSet/administrative-gender"
      }
    },
    {
      "id" : "MedicationOverviewMin.nt",
      "path" : "MedicationOverviewMin.nt",
      "short" : "Nationality",
      "definition" : "Nationality",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://hl7.org/fhir/ValueSet/iso3166-1-3"
      }
    },
    {
      "id" : "MedicationOverviewMin.id",
      "path" : "MedicationOverviewMin.id",
      "short" : "National Identifier",
      "definition" : "National Identifier",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "MedicationOverviewMin.dt",
      "path" : "MedicationOverviewMin.dt",
      "short" : "National Identifier Type",
      "definition" : "Type of national identifier (e.g., social security number, national health ID, etc.)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://terminology.hl7.org/ValueSet/v2-0203"
      }
    },
    {
      "id" : "MedicationOverviewMin.m",
      "path" : "MedicationOverviewMin.m",
      "short" : "Medication Treatment Lines",
      "definition" : "List of medication treatment lines associated with the patient, represented in a minimal format suitable for encoding in a compact QR code payload.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/ph4h/StructureDefinition/MedicationTreatmentLineMin"
      }]
    }]
  }
}

```
