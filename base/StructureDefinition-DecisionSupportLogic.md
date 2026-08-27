# Decision-Support Logic (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Decision-Support Logic (DAK)**

## Logical Model: Decision-Support Logic (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/DecisionSupportLogic | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:DecisionSupportLogic |

 
Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines. 

**Usages:**

* Use this Logical Model: [Decision Support Logic Source](StructureDefinition-DecisionSupportLogicSource.md)
* Refer to this Logical Model: [Decision Support Logic Source](StructureDefinition-DecisionSupportLogicSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-DecisionSupportLogic.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-DecisionSupportLogic.csv), [Excel](StructureDefinition-DecisionSupportLogic.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "DecisionSupportLogic",
  "url" : "http://smart.who.int/base/StructureDefinition/DecisionSupportLogic",
  "version" : "1.0.0",
  "name" : "DecisionSupportLogic",
  "title" : "Decision-Support Logic (DAK)",
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
  "description" : "Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/DecisionSupportLogic",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "DecisionSupportLogic",
      "path" : "DecisionSupportLogic",
      "short" : "Decision-Support Logic (DAK)",
      "definition" : "Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines."
    },
    {
      "id" : "DecisionSupportLogic.id",
      "path" : "DecisionSupportLogic.id",
      "short" : "Decision Support Logic ID",
      "definition" : "An identifier for the decision support logic",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "DecisionSupportLogic.description[x]",
      "path" : "DecisionSupportLogic.description[x]",
      "short" : "Description",
      "definition" : "Description of the decision support logic - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
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
      "id" : "DecisionSupportLogic.source",
      "path" : "DecisionSupportLogic.source",
      "short" : "Source",
      "definition" : "Link to a DMN file containing the decision logic. Source URI could be absolute or relative to the root of the DAK",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    }]
  }
}

```
