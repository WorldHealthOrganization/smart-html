# SMART Guidelines StructureDefinition - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines StructureDefinition**

## Resource Profile: SMART Guidelines StructureDefinition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGStructureDefinition | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGStructureDefinition |

 
Defines the minimum expectations for StructureDefinition resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGStructureDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGStructureDefinition.csv), [Excel](StructureDefinition-SGStructureDefinition.xlsx), [Schematron](StructureDefinition-SGStructureDefinition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGStructureDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/SGStructureDefinition",
  "version" : "1.0.0",
  "name" : "SGStructureDefinition",
  "title" : "SMART Guidelines StructureDefinition",
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
  "description" : "Defines the minimum expectations for StructureDefinition resources used in SMART Guidelines",
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
  },
  {
    "identity" : "iso11179",
    "uri" : "http://metadata-standards.org/11179/",
    "name" : "ISO 11179"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "StructureDefinition",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareablestructuredefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "StructureDefinition",
      "path" : "StructureDefinition"
    },
    {
      "id" : "StructureDefinition.publisher",
      "path" : "StructureDefinition.publisher",
      "min" : 1
    }]
  }
}

```
