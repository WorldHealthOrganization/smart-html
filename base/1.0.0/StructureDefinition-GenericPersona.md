# Generic Persona (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Generic Persona (DAK)**

## Logical Model: Generic Persona (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/GenericPersona | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:GenericPersona |

 
Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway. 

**Usages:**

* Use this Logical Model: [Generic Persona Source](StructureDefinition-GenericPersonaSource.md)
* Refer to this Logical Model: [Generic Persona Source](StructureDefinition-GenericPersonaSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-GenericPersona.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-GenericPersona.csv), [Excel](StructureDefinition-GenericPersona.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "GenericPersona",
  "url" : "http://smart.who.int/base/StructureDefinition/GenericPersona",
  "version" : "1.0.0",
  "name" : "GenericPersona",
  "title" : "Generic Persona (DAK)",
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
  "description" : "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/GenericPersona",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "GenericPersona",
      "path" : "GenericPersona",
      "short" : "Generic Persona (DAK)",
      "definition" : "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway."
    },
    {
      "id" : "GenericPersona.title",
      "path" : "GenericPersona.title",
      "short" : "Title",
      "definition" : "Title of the persona",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "GenericPersona.id",
      "path" : "GenericPersona.id",
      "short" : "Persona ID",
      "definition" : "Identifier for the persona",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "GenericPersona.description[x]",
      "path" : "GenericPersona.description[x]",
      "short" : "Description",
      "definition" : "Description of the persona - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
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
      "id" : "GenericPersona.otherNames",
      "path" : "GenericPersona.otherNames",
      "short" : "Other Names/Examples",
      "definition" : "Other names or examples for the persona",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "GenericPersona.iscoCode",
      "path" : "GenericPersona.iscoCode",
      "short" : "ISCO Code",
      "definition" : "ISCO-08 codes for occupation classification",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://smart.who.int/base/ValueSet/ISCO08ValueSet"
      }
    }]
  }
}

```
