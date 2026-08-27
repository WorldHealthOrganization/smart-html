# Program Indicator Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Program Indicator Source**

## Logical Model: Program Indicator Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/ProgramIndicatorSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:ProgramIndicatorSource |

 
Source reference for Program Indicator - exactly one of the following must be provided: 
* url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition
* instance: Inline ProgramIndicator instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-ProgramIndicatorSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ProgramIndicatorSource.csv), [Excel](StructureDefinition-ProgramIndicatorSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ProgramIndicatorSource",
  "url" : "http://smart.who.int/base/StructureDefinition/ProgramIndicatorSource",
  "version" : "1.0.0",
  "name" : "ProgramIndicatorSource",
  "title" : "Program Indicator Source",
  "status" : "active",
  "date" : "2026-08-27T08:35:55+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Source reference for Program Indicator - exactly one of the following must be provided:\n- url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition\n- instance: Inline ProgramIndicator instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/ProgramIndicatorSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "ProgramIndicatorSource",
      "path" : "ProgramIndicatorSource",
      "short" : "Program Indicator Source",
      "definition" : "Source reference for Program Indicator - exactly one of the following must be provided:\n- url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition\n- instance: Inline ProgramIndicator instance data"
    },
    {
      "id" : "ProgramIndicatorSource.url",
      "path" : "ProgramIndicatorSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve ProgramIndicator definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "ProgramIndicatorSource.canonical",
      "path" : "ProgramIndicatorSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the ProgramIndicator definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/ProgramIndicator"]
      }]
    },
    {
      "id" : "ProgramIndicatorSource.instance",
      "path" : "ProgramIndicatorSource.instance",
      "short" : "Instance",
      "definition" : "Inline ProgramIndicator instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/ProgramIndicator"
      }]
    }]
  }
}

```
