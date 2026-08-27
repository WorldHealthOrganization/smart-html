# SMART Guidelines Group Definition - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Group Definition**

## Resource Profile: SMART Guidelines Group Definition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGGroupDefinition | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:SGGroupDefinition |

 
WHO SMART Guidelines Group Definition 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGGroupDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGGroupDefinition.csv), [Excel](StructureDefinition-SGGroupDefinition.xlsx), [Schematron](StructureDefinition-SGGroupDefinition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGGroupDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/SGGroupDefinition",
  "version" : "1.0.0",
  "name" : "SGGroupDefinition",
  "title" : "WHO SMART Guidelines Group Definition",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "WHO SMART Guidelines Group Definition",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Group",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-groupdefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Group",
      "path" : "Group",
      "mustSupport" : false
    },
    {
      "id" : "Group.identifier",
      "path" : "Group.identifier",
      "min" : 1,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Group.identifier.use",
      "path" : "Group.identifier.use",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Group.identifier.system",
      "path" : "Group.identifier.system",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Group.identifier.value",
      "path" : "Group.identifier.value",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Group.active",
      "path" : "Group.active",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    }]
  }
}

```
