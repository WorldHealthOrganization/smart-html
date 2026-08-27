# Business Process Workflow Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Business Process Workflow Source**

## Logical Model: Business Process Workflow Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflowSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:BusinessProcessWorkflowSource |

 
Source reference for Business Process Workflow - exactly one of the following must be provided: 
* url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition
* instance: Inline BusinessProcessWorkflow instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-BusinessProcessWorkflowSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-BusinessProcessWorkflowSource.csv), [Excel](StructureDefinition-BusinessProcessWorkflowSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "BusinessProcessWorkflowSource",
  "url" : "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflowSource",
  "version" : "1.0.0",
  "name" : "BusinessProcessWorkflowSource",
  "title" : "Business Process Workflow Source",
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
  "description" : "Source reference for Business Process Workflow - exactly one of the following must be provided:\n- url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition\n- instance: Inline BusinessProcessWorkflow instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflowSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "BusinessProcessWorkflowSource",
      "path" : "BusinessProcessWorkflowSource",
      "short" : "Business Process Workflow Source",
      "definition" : "Source reference for Business Process Workflow - exactly one of the following must be provided:\n- url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition\n- instance: Inline BusinessProcessWorkflow instance data"
    },
    {
      "id" : "BusinessProcessWorkflowSource.url",
      "path" : "BusinessProcessWorkflowSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve BusinessProcessWorkflow definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "BusinessProcessWorkflowSource.canonical",
      "path" : "BusinessProcessWorkflowSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the BusinessProcessWorkflow definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow"]
      }]
    },
    {
      "id" : "BusinessProcessWorkflowSource.instance",
      "path" : "BusinessProcessWorkflowSource.instance",
      "short" : "Instance",
      "definition" : "Inline BusinessProcessWorkflow instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow"
      }]
    }]
  }
}

```
