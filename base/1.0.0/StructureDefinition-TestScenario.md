# Test Scenario (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Test Scenario (DAK)**

## Logical Model: Test Scenario (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/TestScenario | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:TestScenario |

 
Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK. 

**Usages:**

* Use this Logical Model: [Test Scenario Source](StructureDefinition-TestScenarioSource.md)
* Refer to this Logical Model: [Test Scenario Source](StructureDefinition-TestScenarioSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-TestScenario.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-TestScenario.csv), [Excel](StructureDefinition-TestScenario.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "TestScenario",
  "url" : "http://smart.who.int/base/StructureDefinition/TestScenario",
  "version" : "1.0.0",
  "name" : "TestScenario",
  "title" : "Test Scenario (DAK)",
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
  "description" : "Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/TestScenario",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "TestScenario",
      "path" : "TestScenario",
      "short" : "Test Scenario (DAK)",
      "definition" : "Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK."
    },
    {
      "id" : "TestScenario.feature",
      "path" : "TestScenario.feature",
      "short" : "Feature File",
      "definition" : "Link to a feature file containing the test scenarios",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "TestScenario.description[x]",
      "path" : "TestScenario.description[x]",
      "short" : "Description",
      "definition" : "Description of the test scenario - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      },
      {
        "code" : "uri"
      }]
    }]
  }
}

```
