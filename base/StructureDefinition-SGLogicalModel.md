# SMART Guidelines Logical Model - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Logical Model**

## Resource Profile: SMART Guidelines Logical Model 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGLogicalModel | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGLogicalModel |

 
Defines the minimum expectations for Logical Models used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGLogicalModel.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGLogicalModel.csv), [Excel](StructureDefinition-SGLogicalModel.xlsx), [Schematron](StructureDefinition-SGLogicalModel.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGLogicalModel",
  "url" : "http://smart.who.int/base/StructureDefinition/SGLogicalModel",
  "version" : "1.0.0",
  "name" : "SGLogicalModel",
  "title" : "SMART Guidelines Logical Model",
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
  "description" : "Defines the minimum expectations for Logical Models used in SMART Guidelines",
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
    "identity" : "iso11179",
    "uri" : "http://metadata-standards.org/11179/",
    "name" : "ISO 11179"
  },
  {
    "identity" : "objimpl",
    "uri" : "http://hl7.org/fhir/object-implementation",
    "name" : "Object Implementation Information"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "StructureDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/StructureDefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "StructureDefinition",
      "path" : "StructureDefinition"
    },
    {
      "id" : "StructureDefinition.title",
      "path" : "StructureDefinition.title",
      "min" : 1
    },
    {
      "id" : "StructureDefinition.publisher",
      "path" : "StructureDefinition.publisher",
      "min" : 1
    },
    {
      "id" : "StructureDefinition.description",
      "path" : "StructureDefinition.description",
      "min" : 1
    },
    {
      "id" : "StructureDefinition.kind",
      "path" : "StructureDefinition.kind",
      "patternCode" : "logical"
    },
    {
      "id" : "StructureDefinition.differential.element.code",
      "path" : "StructureDefinition.differential.element.code",
      "slicing" : {
        "discriminator" : [{
          "type" : "pattern",
          "path" : "system"
        }],
        "description" : "Types of codes that the element corresponds to",
        "ordered" : false,
        "rules" : "open"
      },
      "min" : 1
    },
    {
      "id" : "StructureDefinition.differential.element.code:smart",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "smart",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:smart.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/smart"
    },
    {
      "id" : "StructureDefinition.differential.element.code:loinc",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "loinc",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:loinc.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/loinc"
    },
    {
      "id" : "StructureDefinition.differential.element.code:snomed",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "snomed",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:snomed.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/snomed"
    },
    {
      "id" : "StructureDefinition.differential.element.code:icd-10",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "icd-10",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:icd-10.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/icd-10"
    },
    {
      "id" : "StructureDefinition.differential.element.code:icd-11",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "icd-11",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:icd-11.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/icd-11"
    },
    {
      "id" : "StructureDefinition.differential.element.code:icf",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "icf",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:icf.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/icf"
    },
    {
      "id" : "StructureDefinition.differential.element.code:ichi",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "ichi",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:ichi.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/ichi"
    },
    {
      "id" : "StructureDefinition.differential.element.code:snomed-gps",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "snomed-gps",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:snomed-gps.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/smart-gps"
    },
    {
      "id" : "StructureDefinition.differential.element.code:atc",
      "path" : "StructureDefinition.differential.element.code",
      "sliceName" : "atc",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "StructureDefinition.differential.element.code:atc.system",
      "path" : "StructureDefinition.differential.element.code.system",
      "min" : 1,
      "patternUri" : "http://who.smart.codes/atc"
    },
    {
      "id" : "StructureDefinition.differential.element.short",
      "path" : "StructureDefinition.differential.element.short",
      "min" : 1
    },
    {
      "id" : "StructureDefinition.differential.element.definition",
      "path" : "StructureDefinition.differential.element.definition",
      "min" : 1
    },
    {
      "id" : "StructureDefinition.differential.element.type",
      "path" : "StructureDefinition.differential.element.type",
      "min" : 1,
      "max" : "1"
    }]
  }
}

```
