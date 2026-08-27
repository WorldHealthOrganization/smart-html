# LinkIdExt - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **LinkIdExt**

## Extension: LinkIdExt 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/LinkIdExt | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:LinkIdExt |

Smart Guidelines link identifier extension

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [SGGraphDefinition](StructureDefinition-SGGraphDefinition.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-LinkIdExt.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-LinkIdExt.csv), [Excel](StructureDefinition-LinkIdExt.xlsx), [Schematron](StructureDefinition-LinkIdExt.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "LinkIdExt",
  "url" : "http://smart.who.int/base/StructureDefinition/LinkIdExt",
  "version" : "1.0.0",
  "name" : "LinkIdExt",
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
  "description" : "Smart Guidelines link identifier extension",
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
      "definition" : "Smart Guidelines link identifier extension"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/LinkIdExt"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "type" : [{
        "code" : "id"
      }]
    }]
  }
}

```
