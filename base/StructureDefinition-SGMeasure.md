# SMART Guidelines Measure - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Measure**

## Resource Profile: SMART Guidelines Measure 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGMeasure | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGMeasure |

 
Defines the minimum expectations for Measure resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGMeasure.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGMeasure.csv), [Excel](StructureDefinition-SGMeasure.xlsx), [Schematron](StructureDefinition-SGMeasure.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGMeasure",
  "url" : "http://smart.who.int/base/StructureDefinition/SGMeasure",
  "version" : "1.0.0",
  "name" : "SGMeasure",
  "title" : "SMART Guidelines Measure",
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
  "description" : "Defines the minimum expectations for Measure resources used in SMART Guidelines",
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
  "type" : "Measure",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareablemeasure",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Measure",
      "path" : "Measure"
    },
    {
      "id" : "Measure.name",
      "path" : "Measure.name",
      "min" : 1
    },
    {
      "id" : "Measure.publisher",
      "path" : "Measure.publisher",
      "min" : 1
    }]
  }
}

```
