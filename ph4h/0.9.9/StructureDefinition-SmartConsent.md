# SMART Consent - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **SMART Consent**

## Resource Profile: SMART Consent 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureDefinition/SmartConsent | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:SmartConsent |

 
A profile of the consent resource to track consent of a pilgrim to participate 
FHIR R5 upgrade notes (need this implemented as a structure map): 
* make cardinality of decision 1.. and should stop using it in lieu of verification.verified
* use verification.verifiedBy instead of Consent.organization
* the period extenion should be replaced by Consent.period
* the Consent.patient should be replaced by Consent.subject
* Consent.verification.verifiedBy should be used instead of Consent.organization
 

**Usages:**

* Examples for this Profile: [Consent/c7781f44-6df8-4a8b-9e06-0b34263a47c6](Consent-c7781f44-6df8-4a8b-9e06-0b34263a47c6.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.ph4h|current/StructureDefinition/StructureDefinition-SmartConsent.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SmartConsent.csv), [Excel](StructureDefinition-SmartConsent.xlsx), [Schematron](StructureDefinition-SmartConsent.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SmartConsent",
  "url" : "http://smart.who.int/ph4h/StructureDefinition/SmartConsent",
  "version" : "0.9.9",
  "name" : "SmartConsent",
  "title" : "SMART Consent",
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
  "description" : "A profile of the consent resource to track consent of a pilgrim to participate\n\nFHIR R5 upgrade notes (need this implemented as a structure map):\n * make cardinality of decision 1.. and should stop using it in lieu of verification.verified\n * use verification.verifiedBy instead of Consent.organization\n * the period extenion should be replaced by Consent.period\n * the Consent.patient should be replaced by Consent.subject\n * Consent.verification.verifiedBy should be used instead of Consent.organization\n",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Consent",
  "baseDefinition" : "https://profiles.ihe.net/ITI/PCF/StructureDefinition/IHE.PCF.consentIntermediate",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Consent",
      "path" : "Consent"
    },
    {
      "id" : "Consent.provision.period",
      "path" : "Consent.provision.period",
      "min" : 1
    },
    {
      "id" : "Consent.provision.purpose",
      "path" : "Consent.provision.purpose",
      "min" : 1
    }]
  }
}

```
