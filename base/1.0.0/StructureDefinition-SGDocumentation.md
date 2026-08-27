# SGDocumentation - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SGDocumentation**

## Extension: SGDocumentation 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGDocumentation | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGDocumentation |

Smart Guidelines Documentation extension

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [SGTransaction](StructureDefinition-SGTransaction.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGDocumentation.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGDocumentation.csv), [Excel](StructureDefinition-SGDocumentation.xlsx), [Schematron](StructureDefinition-SGDocumentation.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGDocumentation",
  "url" : "http://smart.who.int/base/StructureDefinition/SGDocumentation",
  "version" : "1.0.0",
  "name" : "SGDocumentation",
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
  "description" : "Smart Guidelines Documentation extension",
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
      "definition" : "Smart Guidelines Documentation extension"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:code",
      "path" : "Extension.extension",
      "sliceName" : "code",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGcode"]
      }]
    },
    {
      "id" : "Extension.extension:doc",
      "path" : "Extension.extension",
      "sliceName" : "doc",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGMarkdown"]
      }]
    },
    {
      "id" : "Extension.extension:requirements",
      "path" : "Extension.extension",
      "sliceName" : "requirements",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGRequirementExt"]
      }]
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/SGDocumentation"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
