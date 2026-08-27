# Test Scenario Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Test Scenario Source**

## Logical Model: Test Scenario Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/TestScenarioSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:TestScenarioSource |

 
Source reference for Test Scenario - exactly one of the following must be provided: 
* url (url data type): URL to retrieve TestScenario definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the TestScenario definition
* instance: Inline TestScenario instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-TestScenarioSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-TestScenarioSource.csv), [Excel](StructureDefinition-TestScenarioSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "TestScenarioSource",
  "url" : "http://smart.who.int/base/StructureDefinition/TestScenarioSource",
  "version" : "1.0.0",
  "name" : "TestScenarioSource",
  "title" : "Test Scenario Source",
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
  "description" : "Source reference for Test Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve TestScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the TestScenario definition\n- instance: Inline TestScenario instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/TestScenarioSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "TestScenarioSource",
      "path" : "TestScenarioSource",
      "short" : "Test Scenario Source",
      "definition" : "Source reference for Test Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve TestScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the TestScenario definition\n- instance: Inline TestScenario instance data"
    },
    {
      "id" : "TestScenarioSource.url",
      "path" : "TestScenarioSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve TestScenario definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "TestScenarioSource.canonical",
      "path" : "TestScenarioSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the TestScenario definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/TestScenario"]
      }]
    },
    {
      "id" : "TestScenarioSource.instance",
      "path" : "TestScenarioSource.instance",
      "short" : "Instance",
      "definition" : "Inline TestScenario instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/TestScenario"
      }]
    }]
  }
}

```
