# SMART Guidelines Actor - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Actor**

## Resource Profile: SMART Guidelines Actor 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGActor | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:SGActor |

 
Smart Guidelines Actor 

**Usages:**

* Refer to this Profile: [Functional Requirement (DAK)](StructureDefinition-FunctionalRequirement.md) and [SGActorExt](StructureDefinition-SGActorExt.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGActor.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGActor.csv), [Excel](StructureDefinition-SGActor.xlsx), [Schematron](StructureDefinition-SGActor.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGActor",
  "url" : "http://smart.who.int/base/StructureDefinition/SGActor",
  "version" : "1.0.0",
  "name" : "SGActor",
  "status" : "draft",
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Smart Guidelines Actor",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "ActorDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/ActorDefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "ActorDefinition",
      "path" : "ActorDefinition"
    },
    {
      "id" : "ActorDefinition.name",
      "path" : "ActorDefinition.name",
      "min" : 1
    },
    {
      "id" : "ActorDefinition.title",
      "path" : "ActorDefinition.title",
      "min" : 1
    },
    {
      "id" : "ActorDefinition.status",
      "path" : "ActorDefinition.status",
      "mustSupport" : true
    },
    {
      "id" : "ActorDefinition.experimental",
      "path" : "ActorDefinition.experimental",
      "min" : 1
    },
    {
      "id" : "ActorDefinition.description",
      "path" : "ActorDefinition.description",
      "min" : 1
    },
    {
      "id" : "ActorDefinition.type",
      "path" : "ActorDefinition.type",
      "mustSupport" : true
    }]
  }
}

```
