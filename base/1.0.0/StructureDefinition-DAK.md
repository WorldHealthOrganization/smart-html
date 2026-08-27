# Digital Adaptation Kit (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Digital Adaptation Kit (DAK)**

## Logical Model: Digital Adaptation Kit (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/DAK | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:DAK |

 
Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-DAK.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-DAK.csv), [Excel](StructureDefinition-DAK.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "DAK",
  "url" : "http://smart.who.int/base/StructureDefinition/DAK",
  "version" : "1.0.0",
  "name" : "DAK",
  "title" : "Digital Adaptation Kit (DAK)",
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
  "description" : "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/DAK",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "DAK",
      "path" : "DAK",
      "short" : "Digital Adaptation Kit (DAK)",
      "definition" : "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components"
    },
    {
      "id" : "DAK.id",
      "path" : "DAK.id",
      "short" : "DAK ID",
      "definition" : "Identifier for the DAK (e.g., smart.who.int.base)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DAK.name",
      "path" : "DAK.name",
      "short" : "DAK Name",
      "definition" : "Short name for the DAK (e.g., Base)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DAK.title",
      "path" : "DAK.title",
      "short" : "DAK Title",
      "definition" : "Full title of the DAK (e.g., SMART Base)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DAK.description[x]",
      "path" : "DAK.description[x]",
      "short" : "DAK Description",
      "definition" : "Description of the DAK - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
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
      "id" : "DAK.version",
      "path" : "DAK.version",
      "short" : "DAK Version",
      "definition" : "Version of the DAK",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DAK.status",
      "path" : "DAK.status",
      "short" : "DAK Status",
      "definition" : "Publication status of the DAK",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    },
    {
      "id" : "DAK.publicationUrl",
      "path" : "DAK.publicationUrl",
      "short" : "Publication URL",
      "definition" : "Canonical URL for the published DAK (e.g., https://smart.who.int/base for WHO repositories)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "DAK.previewUrl",
      "path" : "DAK.previewUrl",
      "short" : "Preview URL",
      "definition" : "Preview URL for the current CI build (e.g., https://worldhealthorganization.github.io/smart-base)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "DAK.canonicalUrl",
      "path" : "DAK.canonicalUrl",
      "short" : "Canonical URL",
      "definition" : "The canonical URL to use for this DAK instance - equals publicationUrl for release branches, previewUrl for development branches",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "DAK.license",
      "path" : "DAK.license",
      "short" : "License",
      "definition" : "License under which the DAK is published",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    },
    {
      "id" : "DAK.copyrightYear",
      "path" : "DAK.copyrightYear",
      "short" : "Copyright Year",
      "definition" : "Year or year range for copyright",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DAK.publisher",
      "path" : "DAK.publisher",
      "short" : "Publisher",
      "definition" : "Organization responsible for publishing the DAK",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "DAK.publisher.name",
      "path" : "DAK.publisher.name",
      "short" : "Publisher Name",
      "definition" : "Name of the publishing organization",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DAK.publisher.url",
      "path" : "DAK.publisher.url",
      "short" : "Publisher URL",
      "definition" : "URL of the publishing organization",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "DAK.healthInterventions",
      "path" : "DAK.healthInterventions",
      "short" : "Health Interventions and Recommendations",
      "definition" : "Overview of the health interventions and WHO, regional or national recommendations included within the DAK",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/HealthInterventionsSource"
      }]
    },
    {
      "id" : "DAK.personas",
      "path" : "DAK.personas",
      "short" : "Generic Personas",
      "definition" : "Depiction of the human and system actors",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/GenericPersonaSource"
      }]
    },
    {
      "id" : "DAK.userScenarios",
      "path" : "DAK.userScenarios",
      "short" : "User Scenarios",
      "definition" : "Narratives that describe how the different personas may interact with each other",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/UserScenarioSource"
      }]
    },
    {
      "id" : "DAK.businessProcesses",
      "path" : "DAK.businessProcesses",
      "short" : "Generic Business Processes and Workflows",
      "definition" : "Business processes and workflows for achieving health programme objectives",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflowSource"
      }]
    },
    {
      "id" : "DAK.dataElements",
      "path" : "DAK.dataElements",
      "short" : "Core Data Elements",
      "definition" : "Data elements required throughout the different points of a workflow",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/CoreDataElementSource"
      }]
    },
    {
      "id" : "DAK.decisionLogic",
      "path" : "DAK.decisionLogic",
      "short" : "Decision-Support Logic",
      "definition" : "Decision-support logic and algorithms to support appropriate service delivery",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/DecisionSupportLogicSource"
      }]
    },
    {
      "id" : "DAK.indicators",
      "path" : "DAK.indicators",
      "short" : "Program Indicators",
      "definition" : "Core set of indicators for decision-making, performance metrics and reporting",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/ProgramIndicatorSource"
      }]
    },
    {
      "id" : "DAK.requirements",
      "path" : "DAK.requirements",
      "short" : "Functional and Non-Functional Requirements",
      "definition" : "High-level list of core functions and capabilities that the system must have",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/RequirementsSource"
      }]
    },
    {
      "id" : "DAK.testScenarios",
      "path" : "DAK.testScenarios",
      "short" : "Test Scenarios",
      "definition" : "Set of test scenarios to validate an implementation of the DAK",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/TestScenarioSource"
      }]
    }]
  }
}

```
