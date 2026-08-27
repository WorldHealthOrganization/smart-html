# Core Data Element (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Core Data Element (DAK)**

## Logical Model: Core Data Element (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/CoreDataElement | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CoreDataElement |

 
Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs. 

**Usages:**

* Use this Logical Model: [Core Data Element Source](StructureDefinition-CoreDataElementSource.md)
* Refer to this Logical Model: [Core Data Element Source](StructureDefinition-CoreDataElementSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-CoreDataElement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-CoreDataElement.csv), [Excel](StructureDefinition-CoreDataElement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "CoreDataElement",
  "url" : "http://smart.who.int/base/StructureDefinition/CoreDataElement",
  "version" : "1.0.0",
  "name" : "CoreDataElement",
  "title" : "Core Data Element (DAK)",
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
  "description" : "Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/CoreDataElement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "CoreDataElement",
      "path" : "CoreDataElement",
      "short" : "Core Data Element (DAK)",
      "definition" : "Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs."
    },
    {
      "id" : "CoreDataElement.type",
      "path" : "CoreDataElement.type",
      "short" : "Type",
      "definition" : "Type of core data element: valueset, codesystem, conceptmap, or logicalmodel",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/CoreDataElementTypeVS"
      }
    },
    {
      "id" : "CoreDataElement.canonical",
      "path" : "CoreDataElement.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI/IRI pointing to the ValueSet, CodeSystem, ConceptMap, or Logical Model definition",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "CoreDataElement.id",
      "path" : "CoreDataElement.id",
      "short" : "Element ID",
      "definition" : "Identifier for the core data element",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "CoreDataElement.description[x]",
      "path" : "CoreDataElement.description[x]",
      "short" : "Description",
      "definition" : "Description of the core data element - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
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
