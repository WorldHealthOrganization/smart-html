# User Scenario (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **User Scenario (DAK)**

## Logical Model: User Scenario (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/UserScenario | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:UserScenario |

 
Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other. 

**Usages:**

* Use this Logical Model: [User Scenario Source](StructureDefinition-UserScenarioSource.md)
* Refer to this Logical Model: [User Scenario Source](StructureDefinition-UserScenarioSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-UserScenario.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-UserScenario.csv), [Excel](StructureDefinition-UserScenario.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "UserScenario",
  "url" : "http://smart.who.int/base/StructureDefinition/UserScenario",
  "version" : "1.0.0",
  "name" : "UserScenario",
  "title" : "User Scenario (DAK)",
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
  "description" : "Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/UserScenario",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "UserScenario",
      "path" : "UserScenario",
      "short" : "User Scenario (DAK)",
      "definition" : "Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other."
    },
    {
      "id" : "UserScenario.title",
      "path" : "UserScenario.title",
      "short" : "Title",
      "definition" : "Title of the user scenario",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "UserScenario.id",
      "path" : "UserScenario.id",
      "short" : "Scenario ID",
      "definition" : "An identifier for the user scenario",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "UserScenario.description[x]",
      "path" : "UserScenario.description[x]",
      "short" : "Description",
      "definition" : "Description of the scenario - either Markdown content or a URI to a Markdown file (absolute or relative to repository root, like input/pagecontent/scenario-XYZ.md)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      },
      {
        "code" : "uri"
      }]
    },
    {
      "id" : "UserScenario.personas",
      "path" : "UserScenario.personas",
      "short" : "Personas",
      "definition" : "References to persona IDs that participate in this scenario",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "id"
      }]
    }]
  }
}

```
