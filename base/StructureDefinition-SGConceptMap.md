# SMART Guidelines ConceptMap - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines ConceptMap**

## Resource Profile: SMART Guidelines ConceptMap 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGConceptMap | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGConceptMap |

 
Defines the minimum expectations for ConceptMap resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGConceptMap.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGConceptMap.csv), [Excel](StructureDefinition-SGConceptMap.xlsx), [Schematron](StructureDefinition-SGConceptMap.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGConceptMap",
  "url" : "http://smart.who.int/base/StructureDefinition/SGConceptMap",
  "version" : "1.0.0",
  "name" : "SGConceptMap",
  "title" : "SMART Guidelines ConceptMap",
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
  "description" : "Defines the minimum expectations for ConceptMap resources used in SMART Guidelines",
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
  "type" : "ConceptMap",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareableconceptmap",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "ConceptMap",
      "path" : "ConceptMap"
    },
    {
      "id" : "ConceptMap.name",
      "path" : "ConceptMap.name",
      "min" : 1
    },
    {
      "id" : "ConceptMap.publisher",
      "path" : "ConceptMap.publisher",
      "min" : 1
    }]
  }
}

```
