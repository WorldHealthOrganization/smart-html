# SMART Guidelines Decision Table - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Decision Table**

## Resource Profile: SMART Guidelines Decision Table 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGDecisionTable | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGDecisionTable |

 
Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines which are derived from DAK Decision Tables 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGDecisionTable.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGDecisionTable.csv), [Excel](StructureDefinition-SGDecisionTable.xlsx), [Schematron](StructureDefinition-SGDecisionTable.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGDecisionTable",
  "url" : "http://smart.who.int/base/StructureDefinition/SGDecisionTable",
  "version" : "1.0.0",
  "name" : "SGDecisionTable",
  "title" : "SMART Guidelines Decision Table",
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
  "description" : "Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines which are derived from DAK Decision Tables ",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "objimpl",
    "uri" : "http://hl7.org/fhir/object-implementation",
    "name" : "Object Implementation Information"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "PlanDefinition",
  "baseDefinition" : "http://smart.who.int/base/StructureDefinition/SGPlanDefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "PlanDefinition",
      "path" : "PlanDefinition"
    },
    {
      "id" : "PlanDefinition.library",
      "path" : "PlanDefinition.library",
      "min" : 1
    }]
  }
}

```
