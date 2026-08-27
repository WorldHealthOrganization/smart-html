# Business Process Workflow (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Business Process Workflow (DAK)**

## Logical Model: Business Process Workflow (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:BusinessProcessWorkflow |

 
Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area. 

**Usages:**

* Use this Logical Model: [Business Process Workflow Source](StructureDefinition-BusinessProcessWorkflowSource.md)
* Refer to this Logical Model: [Business Process Workflow Source](StructureDefinition-BusinessProcessWorkflowSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-BusinessProcessWorkflow.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-BusinessProcessWorkflow.csv), [Excel](StructureDefinition-BusinessProcessWorkflow.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "BusinessProcessWorkflow",
  "url" : "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow",
  "version" : "1.0.0",
  "name" : "BusinessProcessWorkflow",
  "title" : "Business Process Workflow (DAK)",
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
  "description" : "Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "BusinessProcessWorkflow",
      "path" : "BusinessProcessWorkflow",
      "short" : "Business Process Workflow (DAK)",
      "definition" : "Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area."
    },
    {
      "id" : "BusinessProcessWorkflow.id",
      "path" : "BusinessProcessWorkflow.id",
      "short" : "Business Process ID",
      "definition" : "An identifier for the business process workflow",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.description[x]",
      "path" : "BusinessProcessWorkflow.description[x]",
      "short" : "Description",
      "definition" : "Description of the business process - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
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
      "id" : "BusinessProcessWorkflow.source",
      "path" : "BusinessProcessWorkflow.source",
      "short" : "Source",
      "definition" : "Link to a BPMN file containing the workflow definition. Source URI could be absolute or relative to the root of the DAK",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.scenario",
      "path" : "BusinessProcessWorkflow.scenario",
      "short" : "Scenario",
      "definition" : "References to user scenario IDs related to this workflow",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.objectives",
      "path" : "BusinessProcessWorkflow.objectives",
      "short" : "Objectives",
      "definition" : "Description of the objectives of the workflow",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.task",
      "path" : "BusinessProcessWorkflow.task",
      "short" : "Task",
      "definition" : "Tasks within the business process workflow",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.task.identifier",
      "path" : "BusinessProcessWorkflow.task.identifier",
      "short" : "Task ID",
      "definition" : "Identifier for the task",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.task.name",
      "path" : "BusinessProcessWorkflow.task.name",
      "short" : "Task Name",
      "definition" : "Name of the task",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "BusinessProcessWorkflow.task.description",
      "path" : "BusinessProcessWorkflow.task.description",
      "short" : "Task Description",
      "definition" : "Description of what the task involves",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    }]
  }
}

```
