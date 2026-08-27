# User Scenario Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **User Scenario Source**

## Logical Model: User Scenario Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/UserScenarioSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:UserScenarioSource |

 
Source reference for User Scenario - exactly one of the following must be provided: 
* url (url data type): URL to retrieve UserScenario definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the UserScenario definition
* instance: Inline UserScenario instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-UserScenarioSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-UserScenarioSource.csv), [Excel](StructureDefinition-UserScenarioSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "UserScenarioSource",
  "url" : "http://smart.who.int/base/StructureDefinition/UserScenarioSource",
  "version" : "1.0.0",
  "name" : "UserScenarioSource",
  "title" : "User Scenario Source",
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
  "description" : "Source reference for User Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve UserScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the UserScenario definition\n- instance: Inline UserScenario instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/UserScenarioSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "UserScenarioSource",
      "path" : "UserScenarioSource",
      "short" : "User Scenario Source",
      "definition" : "Source reference for User Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve UserScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the UserScenario definition\n- instance: Inline UserScenario instance data"
    },
    {
      "id" : "UserScenarioSource.url",
      "path" : "UserScenarioSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve UserScenario definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "UserScenarioSource.canonical",
      "path" : "UserScenarioSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the UserScenario definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/UserScenario"]
      }]
    },
    {
      "id" : "UserScenarioSource.instance",
      "path" : "UserScenarioSource.instance",
      "short" : "Instance",
      "definition" : "Inline UserScenario instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/UserScenario"
      }]
    }]
  }
}

```
