# Health Interventions Source - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Health Interventions Source**

## Logical Model: Health Interventions Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/HealthInterventionsSource | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:HealthInterventionsSource |

 
Source reference for Health Interventions - exactly one of the following must be provided: 
* url (url data type): URL to retrieve HealthInterventions definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition
* instance: Inline HealthInterventions instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-HealthInterventionsSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-HealthInterventionsSource.csv), [Excel](StructureDefinition-HealthInterventionsSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "HealthInterventionsSource",
  "url" : "http://smart.who.int/base/StructureDefinition/HealthInterventionsSource",
  "version" : "1.0.0",
  "name" : "HealthInterventionsSource",
  "title" : "Health Interventions Source",
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
  "description" : "Source reference for Health Interventions - exactly one of the following must be provided:\n- url (url data type): URL to retrieve HealthInterventions definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition\n- instance: Inline HealthInterventions instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/HealthInterventionsSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "HealthInterventionsSource",
      "path" : "HealthInterventionsSource",
      "short" : "Health Interventions Source",
      "definition" : "Source reference for Health Interventions - exactly one of the following must be provided:\n- url (url data type): URL to retrieve HealthInterventions definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition\n- instance: Inline HealthInterventions instance data"
    },
    {
      "id" : "HealthInterventionsSource.url",
      "path" : "HealthInterventionsSource.url",
      "short" : "URL",
      "definition" : "URL to retrieve HealthInterventions definition from input/ or external source",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "HealthInterventionsSource.canonical",
      "path" : "HealthInterventionsSource.canonical",
      "short" : "Canonical",
      "definition" : "Canonical URI pointing to the HealthInterventions definition",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/HealthInterventions"]
      }]
    },
    {
      "id" : "HealthInterventionsSource.instance",
      "path" : "HealthInterventionsSource.instance",
      "short" : "Instance",
      "definition" : "Inline HealthInterventions instance data",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/HealthInterventions"
      }]
    }]
  }
}

```
