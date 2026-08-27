# SMART Guidelines CodeSystem - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines CodeSystem**

## Resource Profile: SMART Guidelines CodeSystem 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGCodeSystem | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGCodeSystem |

 
Defines the minimum expectations for CodeSystem resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGCodeSystem.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGCodeSystem.csv), [Excel](StructureDefinition-SGCodeSystem.xlsx), [Schematron](StructureDefinition-SGCodeSystem.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGCodeSystem",
  "url" : "http://smart.who.int/base/StructureDefinition/SGCodeSystem",
  "version" : "1.0.0",
  "name" : "SGCodeSystem",
  "title" : "SMART Guidelines CodeSystem",
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
  "description" : "Defines the minimum expectations for CodeSystem resources used in SMART Guidelines",
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
  "type" : "CodeSystem",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareablecodesystem",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "CodeSystem",
      "path" : "CodeSystem"
    },
    {
      "id" : "CodeSystem.name",
      "path" : "CodeSystem.name",
      "min" : 1
    },
    {
      "id" : "CodeSystem.publisher",
      "path" : "CodeSystem.publisher",
      "min" : 1
    }]
  }
}

```
