# Decision Support Logic Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Decision Support Logic Source**

## Logical Model: Decision Support Logic Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/DecisionSupportLogicSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:DecisionSupportLogicSource |

 
Source reference for Decision Support Logic - exactly one of the following must be provided: 
* url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition
* instance: Inline DecisionSupportLogic instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-DecisionSupportLogicSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-DecisionSupportLogicSource.csv), [Excel](StructureDefinition-DecisionSupportLogicSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "DecisionSupportLogicSource",
  "url" : "http://smart.who.int/base/StructureDefinition/DecisionSupportLogicSource",
  "version" : "1.0.0",
  "name" : "DecisionSupportLogicSource",
  "title" : "Decision Support Logic Source",
  "status" : "active",
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Source reference for Decision Support Logic - exactly one of the following must be provided:\n- url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition\n- instance: Inline DecisionSupportLogic instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/DecisionSupportLogicSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "DecisionSupportLogicSource",
      "path" : "DecisionSupportLogicSource",
      "short" : "Decision Support Logic Source",
      "definition" : "Source reference for Decision Support Logic - exactly one of the following must be provided:\n- url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition\n- instance: Inline DecisionSupportLogic instance data"
    },
    {
      "id" : "DecisionSupportLogicSource.url",
      "path" : "DecisionSupportLogicSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve DecisionSupportLogic definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "DecisionSupportLogicSource.canonical",
      "path" : "DecisionSupportLogicSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the DecisionSupportLogic definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/DecisionSupportLogic"]
      }]
    },
    {
      "id" : "DecisionSupportLogicSource.instance",
      "path" : "DecisionSupportLogicSource.instance",
      "short" : "Instance",
      "definition" : "Inline DecisionSupportLogic instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/DecisionSupportLogic"
      }]
    }]
  }
}

```
