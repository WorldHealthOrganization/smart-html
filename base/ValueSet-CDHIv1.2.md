# Digital Health Interventions for Health Workers - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Digital Health Interventions for Health Workers**

## ValueSet: Digital Health Interventions for Health Workers (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/CDHIv1.2 | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CDHIv1.2 |

 
Digital Health Interventions whose primary user group is Health Workers. Group 2 of the Classification of Digital Health Interventions v1 (2018). 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |

## API Information

##### Digital Health Interventions for Health Workers Schema API

JSON Schema for Digital Health Interventions for Health Workers ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-CDHIv1.2.schema.json

#### JSON Schema definition for the enumeration ValueSet-CDHIv1.2

This endpoint serves the JSON Schema definition for the enumeration ValueSet-CDHIv1.2.

## Schema Definition

### ValueSet-CDHIv1.2

**Description:** JSON Schema for Digital Health Interventions for Health Workers ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "CDHIv1.2",
  "url" : "http://smart.who.int/base/ValueSet/CDHIv1.2",
  "version" : "1.0.0",
  "name" : "CDHIv1.2",
  "title" : "Digital Health Interventions for Health Workers",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-08-27T08:35:55+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Digital Health Interventions whose primary user group is Health Workers. Group 2 of the Classification of Digital Health Interventions v1 (2018).",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/CDHIv1",
      "concept" : [{
        "code" : "2.0"
      },
      {
        "code" : "2.1"
      },
      {
        "code" : "2.1.1"
      },
      {
        "code" : "2.1.2"
      },
      {
        "code" : "2.2"
      },
      {
        "code" : "2.2.1"
      },
      {
        "code" : "2.2.2"
      },
      {
        "code" : "2.2.3"
      },
      {
        "code" : "2.2.4"
      },
      {
        "code" : "2.3"
      },
      {
        "code" : "2.3.1"
      },
      {
        "code" : "2.3.2"
      },
      {
        "code" : "2.3.3"
      },
      {
        "code" : "2.4"
      },
      {
        "code" : "2.4.1"
      },
      {
        "code" : "2.4.2"
      },
      {
        "code" : "2.4.3"
      },
      {
        "code" : "2.4.4"
      },
      {
        "code" : "2.5"
      },
      {
        "code" : "2.5.1"
      },
      {
        "code" : "2.5.2"
      },
      {
        "code" : "2.5.3"
      },
      {
        "code" : "2.5.4"
      },
      {
        "code" : "2.5.5"
      },
      {
        "code" : "2.6"
      },
      {
        "code" : "2.6.1"
      },
      {
        "code" : "2.6.2"
      },
      {
        "code" : "2.6.3"
      },
      {
        "code" : "2.7"
      },
      {
        "code" : "2.7.1"
      },
      {
        "code" : "2.7.2"
      },
      {
        "code" : "2.8"
      },
      {
        "code" : "2.8.1"
      },
      {
        "code" : "2.8.2"
      },
      {
        "code" : "2.9"
      },
      {
        "code" : "2.9.1"
      },
      {
        "code" : "2.9.2"
      },
      {
        "code" : "2.9.3"
      },
      {
        "code" : "2.10"
      },
      {
        "code" : "2.10.1"
      },
      {
        "code" : "2.10.2"
      },
      {
        "code" : "2.10.3"
      },
      {
        "code" : "2.10.4"
      }]
    }]
  }
}

```
