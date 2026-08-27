# Dublin Core Metadata Element Set - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Dublin Core Metadata Element Set**

## Logical Model: Dublin Core Metadata Element Set 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/DublinCore | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:DublinCore |

 
Logical Model representing Dublin Core metadata elements as defined at https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ 

**Usages:**

* Use this Logical Model: [Health Interventions and Recommendations (DAK)](StructureDefinition-HealthInterventions.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-DublinCore.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-DublinCore.csv), [Excel](StructureDefinition-DublinCore.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "DublinCore",
  "url" : "http://smart.who.int/base/StructureDefinition/DublinCore",
  "version" : "1.0.0",
  "name" : "DublinCore",
  "title" : "Dublin Core Metadata Element Set",
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
  "description" : "Logical Model representing Dublin Core metadata elements as defined at https://www.dublincore.org/specifications/dublin-core/dcmi-terms/",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/DublinCore",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "DublinCore",
      "path" : "DublinCore",
      "short" : "Dublin Core Metadata Element Set",
      "definition" : "Logical Model representing Dublin Core metadata elements as defined at https://www.dublincore.org/specifications/dublin-core/dcmi-terms/"
    },
    {
      "id" : "DublinCore.title",
      "path" : "DublinCore.title",
      "short" : "Title",
      "definition" : "A name given to the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.creator",
      "path" : "DublinCore.creator",
      "short" : "Creator",
      "definition" : "An entity responsible for making the resource",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.subject",
      "path" : "DublinCore.subject",
      "short" : "Subject",
      "definition" : "The topic of the resource",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.description",
      "path" : "DublinCore.description",
      "short" : "Description",
      "definition" : "An account of the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "DublinCore.publisher",
      "path" : "DublinCore.publisher",
      "short" : "Publisher",
      "definition" : "An entity responsible for making the resource available",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.contributor",
      "path" : "DublinCore.contributor",
      "short" : "Contributor",
      "definition" : "An entity responsible for making contributions to the resource",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.date",
      "path" : "DublinCore.date",
      "short" : "Date",
      "definition" : "A point or period of time associated with an event in the lifecycle of the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "DublinCore.type",
      "path" : "DublinCore.type",
      "short" : "Type",
      "definition" : "The nature or genre of the resource",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.format",
      "path" : "DublinCore.format",
      "short" : "Format",
      "definition" : "The file format, physical medium, or dimensions of the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.identifier",
      "path" : "DublinCore.identifier",
      "short" : "Identifier",
      "definition" : "An unambiguous reference to the resource within a given context",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.source",
      "path" : "DublinCore.source",
      "short" : "Source",
      "definition" : "A related resource from which the described resource is derived",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.language",
      "path" : "DublinCore.language",
      "short" : "Language",
      "definition" : "A language of the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.relation",
      "path" : "DublinCore.relation",
      "short" : "Relation",
      "definition" : "A related resource",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.coverage",
      "path" : "DublinCore.coverage",
      "short" : "Coverage",
      "definition" : "The spatial or temporal topic of the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "DublinCore.rights",
      "path" : "DublinCore.rights",
      "short" : "Rights",
      "definition" : "Information about rights held in and over the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
