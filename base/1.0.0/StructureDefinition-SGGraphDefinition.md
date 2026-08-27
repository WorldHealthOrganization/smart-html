# SMART Guidelines GraphDefinition - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines GraphDefinition**

## Resource Profile: SMART Guidelines GraphDefinition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGGraphDefinition | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:SGGraphDefinition |

 
SMART Guidelines Transaction Definition 

**Usages:**

* Derived from this Profile: [SGTransaction](StructureDefinition-SGTransaction.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGGraphDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGGraphDefinition.csv), [Excel](StructureDefinition-SGGraphDefinition.xlsx), [Schematron](StructureDefinition-SGGraphDefinition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGGraphDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/SGGraphDefinition",
  "version" : "1.0.0",
  "name" : "SGGraphDefinition",
  "status" : "draft",
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "SMART Guidelines Transaction Definition",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "objimpl",
    "uri" : "http://hl7.org/fhir/object-implementation",
    "name" : "Object Implementation Information"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "GraphDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/GraphDefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "GraphDefinition",
      "path" : "GraphDefinition"
    },
    {
      "id" : "GraphDefinition.extension",
      "path" : "GraphDefinition.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "GraphDefinition.extension:node",
      "path" : "GraphDefinition.extension",
      "sliceName" : "node",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://hl7.org/fhir/5.0/StructureDefinition/extension-GraphDefinition.node"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.name",
      "path" : "GraphDefinition.name",
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.status",
      "path" : "GraphDefinition.status",
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.experimental",
      "path" : "GraphDefinition.experimental",
      "min" : 1
    },
    {
      "id" : "GraphDefinition.description",
      "path" : "GraphDefinition.description",
      "min" : 1
    },
    {
      "id" : "GraphDefinition.link",
      "path" : "GraphDefinition.link",
      "min" : 1
    },
    {
      "id" : "GraphDefinition.link.extension",
      "path" : "GraphDefinition.link.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:sourceId",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "sourceId",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/LinkIdExt"]
      }]
    },
    {
      "id" : "GraphDefinition.link.extension:targetId",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "targetId",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/LinkIdExt"]
      }]
    }]
  }
}

```
