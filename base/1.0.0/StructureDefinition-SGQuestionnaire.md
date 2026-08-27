# SMART Guidelines Questionnaire - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Questionnaire**

## Resource Profile: SMART Guidelines Questionnaire 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGQuestionnaire | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGQuestionnaire |

 
Defines the minimum expectations for Questionnaire resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGQuestionnaire.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGQuestionnaire.csv), [Excel](StructureDefinition-SGQuestionnaire.xlsx), [Schematron](StructureDefinition-SGQuestionnaire.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGQuestionnaire",
  "url" : "http://smart.who.int/base/StructureDefinition/SGQuestionnaire",
  "version" : "1.0.0",
  "name" : "SGQuestionnaire",
  "title" : "SMART Guidelines Questionnaire",
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
  "description" : "Defines the minimum expectations for Questionnaire resources used in SMART Guidelines",
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
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Questionnaire",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareablequestionnaire",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Questionnaire",
      "path" : "Questionnaire"
    },
    {
      "id" : "Questionnaire.extension",
      "path" : "Questionnaire.extension",
      "min" : 2
    },
    {
      "id" : "Questionnaire.extension:actor",
      "path" : "Questionnaire.extension",
      "sliceName" : "actor",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGActorExt"]
      }]
    },
    {
      "id" : "Questionnaire.extension:task",
      "path" : "Questionnaire.extension",
      "sliceName" : "task",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGcode"]
      }]
    },
    {
      "id" : "Questionnaire.name",
      "path" : "Questionnaire.name",
      "min" : 1
    },
    {
      "id" : "Questionnaire.publisher",
      "path" : "Questionnaire.publisher",
      "min" : 1
    }]
  }
}

```
