# Functional Requirement (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Functional Requirement (DAK)**

## Logical Model: Functional Requirement (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/FunctionalRequirement | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:FunctionalRequirement |

 
Logical Model for representing functional requirement from a DAK 

**Usages:**

* Use this Logical Model: [Functional and Non-Functional Requirements (DAK)](StructureDefinition-Requirements.md)
* Refer to this Logical Model: [Functional and Non-Functional Requirements (DAK)](StructureDefinition-Requirements.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-FunctionalRequirement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-FunctionalRequirement.csv), [Excel](StructureDefinition-FunctionalRequirement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "FunctionalRequirement",
  "url" : "http://smart.who.int/base/StructureDefinition/FunctionalRequirement",
  "version" : "1.0.0",
  "name" : "FunctionalRequirement",
  "title" : "Functional Requirement (DAK)",
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
  "description" : "Logical Model for representing functional requirement from a DAK",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/FunctionalRequirement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "FunctionalRequirement",
      "path" : "FunctionalRequirement",
      "short" : "Functional Requirement (DAK)",
      "definition" : "Logical Model for representing functional requirement from a DAK"
    },
    {
      "id" : "FunctionalRequirement.id",
      "path" : "FunctionalRequirement.id",
      "short" : "Requirement ID",
      "definition" : "An identifier or code for the requirement",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "FunctionalRequirement.activity",
      "path" : "FunctionalRequirement.activity",
      "short" : "Activity",
      "definition" : "Description of the activity being performed",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "FunctionalRequirement.actor",
      "path" : "FunctionalRequirement.actor",
      "short" : "Actor",
      "definition" : "The actor(s) that should fulfill the requirement",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGActor"]
      }]
    },
    {
      "id" : "FunctionalRequirement.capability[x]",
      "path" : "FunctionalRequirement.capability[x]",
      "short" : "Capability",
      "definition" : "Capability achieved by an actor fulfilling the requirement (I want)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      },
      {
        "code" : "Coding"
      }]
    },
    {
      "id" : "FunctionalRequirement.benefit[x]",
      "path" : "FunctionalRequirement.benefit[x]",
      "short" : "Benefit",
      "definition" : "Benefit to an actor fulfilling the requirement (so that)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      },
      {
        "code" : "Coding"
      }]
    },
    {
      "id" : "FunctionalRequirement.classification",
      "path" : "FunctionalRequirement.classification",
      "short" : "Classification",
      "definition" : "Classification of the identifier",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Coding"
      }]
    }]
  }
}

```
