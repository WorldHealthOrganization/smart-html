# SMART Composition (IPS) - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **SMART Composition (IPS)**

## Resource Profile: SMART Composition (IPS) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureDefinition/SmartIPSComposition | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:SmartIPSComposition |

 
This profile represents the constraints applied to the Composition resource by the International Patient Summary (IPS) for use within the SMART Guidelines 
Note: The profile expects atleast one SMART Consent entry to be present within Advance Directives section 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.ph4h|current/StructureDefinition/StructureDefinition-SmartIPSComposition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SmartIPSComposition.csv), [Excel](StructureDefinition-SmartIPSComposition.xlsx), [Schematron](StructureDefinition-SmartIPSComposition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SmartIPSComposition",
  "url" : "http://smart.who.int/ph4h/StructureDefinition/SmartIPSComposition",
  "version" : "0.9.9",
  "name" : "SmartIPSComposition",
  "title" : "SMART Composition (IPS)",
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
  "description" : "This profile represents the constraints applied to the Composition resource by the International Patient Summary (IPS) for use within the SMART Guidelines\n\nNote: The profile expects atleast one SMART Consent entry to be present within Advance Directives section",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "cda",
    "uri" : "http://hl7.org/v3/cda",
    "name" : "CDA (R2)"
  },
  {
    "identity" : "fhirdocumentreference",
    "uri" : "http://hl7.org/fhir/documentreference",
    "name" : "FHIR DocumentReference"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Composition",
  "baseDefinition" : "http://hl7.org/fhir/uv/ips/StructureDefinition/Composition-uv-ips",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Composition",
      "path" : "Composition"
    },
    {
      "id" : "Composition.section",
      "path" : "Composition.section",
      "min" : 4
    },
    {
      "id" : "Composition.section:sectionAdvanceDirectives",
      "path" : "Composition.section",
      "sliceName" : "sectionAdvanceDirectives",
      "min" : 1
    },
    {
      "id" : "Composition.section:sectionAdvanceDirectives.entry",
      "path" : "Composition.section.entry",
      "constraint" : [{
        "key" : "containsSmartConsent-cmp2",
        "severity" : "error",
        "human" : "At least one entry of consent must be SmartConsent",
        "expression" : "reference.resolve().where(conformsTo('http://smart.who.int/ph4h/StructureDefinition/SmartConsent')).exists()",
        "source" : "http://smart.who.int/ph4h/StructureDefinition/SmartIPSComposition"
      }]
    }]
  }
}

```
