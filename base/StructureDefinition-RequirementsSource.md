# Requirements Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Requirements Source**

## Logical Model: Requirements Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/RequirementsSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:RequirementsSource |

 
Source reference for Requirements - exactly one of the following must be provided: 
* url (url data type): URL to retrieve Requirements definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the Requirements definition
* instance: Inline Requirements instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-RequirementsSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-RequirementsSource.csv), [Excel](StructureDefinition-RequirementsSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "RequirementsSource",
  "url" : "http://smart.who.int/base/StructureDefinition/RequirementsSource",
  "version" : "1.0.0",
  "name" : "RequirementsSource",
  "title" : "Requirements Source",
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
  "description" : "Source reference for Requirements - exactly one of the following must be provided:\n- url (url data type): URL to retrieve Requirements definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the Requirements definition\n- instance: Inline Requirements instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/RequirementsSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "RequirementsSource",
      "path" : "RequirementsSource",
      "short" : "Requirements Source",
      "definition" : "Source reference for Requirements - exactly one of the following must be provided:\n- url (url data type): URL to retrieve Requirements definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the Requirements definition\n- instance: Inline Requirements instance data"
    },
    {
      "id" : "RequirementsSource.url",
      "path" : "RequirementsSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve Requirements definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "RequirementsSource.canonical",
      "path" : "RequirementsSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the Requirements definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/Requirements"]
      }]
    },
    {
      "id" : "RequirementsSource.instance",
      "path" : "RequirementsSource.instance",
      "short" : "Instance",
      "definition" : "Inline Requirements instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/Requirements"
      }]
    }]
  }
}

```
