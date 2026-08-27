# SGMarkdown - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SGMarkdown**

## Extension: SGMarkdown 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGMarkdown | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGMarkdown |

Smart Guidelines markdown extension

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [SGDocumentation](StructureDefinition-SGDocumentation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGMarkdown.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGMarkdown.csv), [Excel](StructureDefinition-SGMarkdown.xlsx), [Schematron](StructureDefinition-SGMarkdown.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGMarkdown",
  "url" : "http://smart.who.int/base/StructureDefinition/SGMarkdown",
  "version" : "1.0.0",
  "name" : "SGMarkdown",
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
  "description" : "Smart Guidelines markdown extension",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "Element"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "definition" : "Smart Guidelines markdown extension"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/SGMarkdown"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "markdown"
      }],
      "mustSupport" : true
    }]
  }
}

```
