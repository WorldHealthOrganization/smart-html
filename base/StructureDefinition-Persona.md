# Persona (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Persona (DAK)**

## Logical Model: Persona (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/Persona | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:Persona |

 
Logical Model for representing Personas from a DAK 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-Persona.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-Persona.csv), [Excel](StructureDefinition-Persona.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Persona",
  "url" : "http://smart.who.int/base/StructureDefinition/Persona",
  "version" : "1.0.0",
  "name" : "Persona",
  "title" : "Persona (DAK)",
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
  "description" : "Logical Model for representing Personas from a DAK",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/Persona",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Persona",
      "path" : "Persona",
      "short" : "Persona (DAK)",
      "definition" : "Logical Model for representing Personas from a DAK"
    },
    {
      "id" : "Persona.id",
      "path" : "Persona.id",
      "short" : "Persona ID",
      "definition" : "An identifier or code for the persona",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "Persona.name",
      "path" : "Persona.name",
      "short" : "Name",
      "definition" : "Name",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Persona.description",
      "path" : "Persona.description",
      "short" : "Description",
      "definition" : "Description of the persona",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Persona.ISCO",
      "path" : "Persona.ISCO",
      "short" : "ISCO Code",
      "definition" : "ISCO Code",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "CodeableConcept"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "urn:oid:2.16.840.1.113883.2.9.6.2.7"
      }
    },
    {
      "id" : "Persona.type",
      "path" : "Persona.type",
      "short" : "Type of Persona",
      "definition" : "Persona Types: Key/Related/System/Hardware Device",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/SGPersonaTypesVS"
      }
    }]
  }
}

```
