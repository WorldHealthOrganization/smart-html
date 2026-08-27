# Non-Functional Requirement (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Non-Functional Requirement (DAK)**

## Logical Model: Non-Functional Requirement (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:NonFunctionalRequirement |

 
Logical Model for representing non-functional requirement from a DAK 

**Usages:**

* Use this Logical Model: [Functional and Non-Functional Requirements (DAK)](StructureDefinition-Requirements.md)
* Refer to this Logical Model: [Functional and Non-Functional Requirements (DAK)](StructureDefinition-Requirements.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-NonFunctionalRequirement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-NonFunctionalRequirement.csv), [Excel](StructureDefinition-NonFunctionalRequirement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "NonFunctionalRequirement",
  "url" : "http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement",
  "version" : "1.0.0",
  "name" : "NonFunctionalRequirement",
  "title" : "Non-Functional Requirement (DAK)",
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
  "description" : "Logical Model for representing non-functional requirement from a DAK",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "NonFunctionalRequirement",
      "path" : "NonFunctionalRequirement",
      "short" : "Non-Functional Requirement (DAK)",
      "definition" : "Logical Model for representing non-functional requirement from a DAK"
    },
    {
      "id" : "NonFunctionalRequirement.id",
      "path" : "NonFunctionalRequirement.id",
      "short" : "Requirement ID",
      "definition" : "An identifier or code for the requirement",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "NonFunctionalRequirement.requirement",
      "path" : "NonFunctionalRequirement.requirement",
      "short" : "Requirement",
      "definition" : "Description of the requirement",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "NonFunctionalRequirement.category",
      "path" : "NonFunctionalRequirement.category",
      "short" : "Category",
      "definition" : "Category of the non-functional requirement",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "Coding"
      }]
    },
    {
      "id" : "NonFunctionalRequirement.classification",
      "path" : "NonFunctionalRequirement.classification",
      "short" : "Classification",
      "definition" : "Classification or category of the requirement",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Coding"
      }]
    }]
  }
}

```
