# Health Interventions and Recommendations (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Health Interventions and Recommendations (DAK)**

## Logical Model: Health Interventions and Recommendations (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/HealthInterventions | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:HealthInterventions |

 
Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK. 

**Usages:**

* Use this Logical Model: [Health Interventions Source](StructureDefinition-HealthInterventionsSource.md)
* Refer to this Logical Model: [Health Interventions Source](StructureDefinition-HealthInterventionsSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-HealthInterventions.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-HealthInterventions.csv), [Excel](StructureDefinition-HealthInterventions.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "HealthInterventions",
  "url" : "http://smart.who.int/base/StructureDefinition/HealthInterventions",
  "version" : "1.0.0",
  "name" : "HealthInterventions",
  "title" : "Health Interventions and Recommendations (DAK)",
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
  "description" : "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/HealthInterventions",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "HealthInterventions",
      "path" : "HealthInterventions",
      "short" : "Health Interventions and Recommendations (DAK)",
      "definition" : "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK."
    },
    {
      "id" : "HealthInterventions.id",
      "path" : "HealthInterventions.id",
      "short" : "Health Intervention ID",
      "definition" : "An identifier for the health intervention",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "HealthInterventions.description[x]",
      "path" : "HealthInterventions.description[x]",
      "short" : "Description",
      "definition" : "Description of the health intervention - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      },
      {
        "code" : "uri"
      }]
    },
    {
      "id" : "HealthInterventions.reference",
      "path" : "HealthInterventions.reference",
      "short" : "Reference",
      "definition" : "Reference data element using Dublin Core metadata",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/DublinCore"
      }]
    }]
  }
}

```
