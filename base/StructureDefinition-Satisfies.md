# Satisfies - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Satisfies**

## Extension: Satisfies 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/Satisfies | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:Satisfies |

Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying the referenced requirement.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [SMART Guidelines Requirements](StructureDefinition-SGRequirements.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-Satisfies.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-Satisfies.csv), [Excel](StructureDefinition-Satisfies.xlsx), [Schematron](StructureDefinition-Satisfies.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Satisfies",
  "url" : "http://smart.who.int/base/StructureDefinition/Satisfies",
  "version" : "1.0.0",
  "name" : "Satisfies",
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
  "description" : "Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying  the referenced requirement.",
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
      "definition" : "Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying  the referenced requirement."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/Satisfies"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/SGRequirements"]
      }],
      "mustSupport" : true
    }]
  }
}

```
