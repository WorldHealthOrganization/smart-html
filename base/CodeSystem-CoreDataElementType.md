# Core Data Element Type - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Core Data Element Type**

## CodeSystem: Core Data Element Type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/CoreDataElementType | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CoreDataElementType |

 
CodeSystem for Core Data Element types - defines the type of FHIR resource that a Core Data Element references. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Core Data Element Type Value Set](ValueSet-CoreDataElementTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "CoreDataElementType",
  "url" : "http://smart.who.int/base/CodeSystem/CoreDataElementType",
  "version" : "1.0.0",
  "name" : "CoreDataElementType",
  "title" : "Core Data Element Type",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-08-27T08:35:55+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "CodeSystem for Core Data Element types - defines the type of FHIR resource that a Core Data Element references.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "valueset",
    "display" : "ValueSet",
    "definition" : "Reference to a FHIR ValueSet resource"
  },
  {
    "code" : "codesystem",
    "display" : "CodeSystem",
    "definition" : "Reference to a FHIR CodeSystem resource"
  },
  {
    "code" : "conceptmap",
    "display" : "ConceptMap",
    "definition" : "Reference to a FHIR ConceptMap resource"
  },
  {
    "code" : "logicalmodel",
    "display" : "Logical Model",
    "definition" : "Reference to a Logical Model adherent to SGLogicalModel"
  }]
}

```
