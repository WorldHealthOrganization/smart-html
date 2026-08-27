# SMART Guidelines ImplementationGuide - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines ImplementationGuide**

## Resource Profile: SMART Guidelines ImplementationGuide 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGImplementationGuide | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGImplementationGuide |

 
Defines the minimum expectations for ImplementationGuide resources used in SMART Guidelines 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGImplementationGuide.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGImplementationGuide.csv), [Excel](StructureDefinition-SGImplementationGuide.xlsx), [Schematron](StructureDefinition-SGImplementationGuide.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGImplementationGuide",
  "url" : "http://smart.who.int/base/StructureDefinition/SGImplementationGuide",
  "version" : "1.0.0",
  "name" : "SGImplementationGuide",
  "title" : "SMART Guidelines ImplementationGuide",
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
  "description" : "Defines the minimum expectations for ImplementationGuide resources used in SMART Guidelines",
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
  "type" : "ImplementationGuide",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareableimplementationguide",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "ImplementationGuide",
      "path" : "ImplementationGuide"
    },
    {
      "id" : "ImplementationGuide.publisher",
      "path" : "ImplementationGuide.publisher",
      "min" : 1
    },
    {
      "id" : "ImplementationGuide.license",
      "path" : "ImplementationGuide.license",
      "patternCode" : "CC-BY-SA-3.0-IGO"
    },
    {
      "id" : "ImplementationGuide.definition.resource",
      "path" : "ImplementationGuide.definition.resource",
      "slicing" : {
        "discriminator" : [{
          "type" : "profile",
          "path" : "reference.resolve()"
        }],
        "rules" : "open"
      }
    },
    {
      "id" : "ImplementationGuide.definition.resource:ActivityDefinition",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "ActivityDefinition",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:ActivityDefinition.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGActivityDefinition"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:ActivityDefinition.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "ActivityDefinition"
    },
    {
      "id" : "ImplementationGuide.definition.resource:CodeSystem",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "CodeSystem",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:CodeSystem.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGCodeSystem"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:CodeSystem.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "CodeSystem"
    },
    {
      "id" : "ImplementationGuide.definition.resource:ConceptMap",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "ConceptMap",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:ConceptMap.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGConceptMap"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:ConceptMap.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "ConceptMap"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Extension",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "Extension",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Library",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "Library",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Library.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGLibrary"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:Library.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "Library"
    },
    {
      "id" : "ImplementationGuide.definition.resource:LogicalModel",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "LogicalModel",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:LogicalModel.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGLogicalModel"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:LogicalModel.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "StructureDefinition"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Measure",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "Measure",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Measure.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGMeasure"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:Measure.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "Measure"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Profile",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "Profile",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Profile.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGStructureDefinition"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:Profile.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "StructureDefinition"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Questionnaire",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "Questionnaire",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:Questionnaire.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGQuestionnaire"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:Questionnaire.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "Questionnaire"
    },
    {
      "id" : "ImplementationGuide.definition.resource:StructureMap",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "StructureMap",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:StructureMap.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGStructureMap"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:StructureMap.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "StructureMap"
    },
    {
      "id" : "ImplementationGuide.definition.resource:ValueSet",
      "path" : "ImplementationGuide.definition.resource",
      "sliceName" : "ValueSet",
      "min" : 0,
      "max" : "*"
    },
    {
      "id" : "ImplementationGuide.definition.resource:ValueSet.reference",
      "path" : "ImplementationGuide.definition.resource.reference",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGValueSet"]
      }]
    },
    {
      "id" : "ImplementationGuide.definition.resource:ValueSet.reference.type",
      "path" : "ImplementationGuide.definition.resource.reference.type",
      "patternUri" : "ValueSet"
    }]
  }
}

```
