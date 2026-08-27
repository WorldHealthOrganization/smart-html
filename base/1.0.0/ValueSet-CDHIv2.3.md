# Digital Health Interventions for Health Management and Support Personnel - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Digital Health Interventions for Health Management and Support Personnel**

## ValueSet: Digital Health Interventions for Health Management and Support Personnel (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/CDHIv2.3 | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CDHIv2.3 |

 
Digital Health Interventions whose primary user group is Health Management and Support Personnel. Group 3 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023). 

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

##### Digital Health Interventions for Health Management and Support Personnel Schema API

JSON Schema for Digital Health Interventions for Health Management and Support Personnel ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-CDHIv2.3.schema.json

#### JSON Schema definition for the enumeration ValueSet-CDHIv2.3

This endpoint serves the JSON Schema definition for the enumeration ValueSet-CDHIv2.3.

## Schema Definition

### ValueSet-CDHIv2.3

**Description:** JSON Schema for Digital Health Interventions for Health Management and Support Personnel ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "CDHIv2.3",
  "url" : "http://smart.who.int/base/ValueSet/CDHIv2.3",
  "version" : "1.0.0",
  "name" : "CDHIv2.3",
  "title" : "Digital Health Interventions for Health Management and Support Personnel",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Digital Health Interventions whose primary user group is Health Management and Support Personnel. Group 3 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023).",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/CDHIv2",
      "concept" : [{
        "code" : "3"
      },
      {
        "code" : "3.1"
      },
      {
        "code" : "3.1.1"
      },
      {
        "code" : "3.1.2"
      },
      {
        "code" : "3.1.3"
      },
      {
        "code" : "3.1.4"
      },
      {
        "code" : "3.1.5"
      },
      {
        "code" : "3.2"
      },
      {
        "code" : "3.2.1"
      },
      {
        "code" : "3.2.2"
      },
      {
        "code" : "3.2.3"
      },
      {
        "code" : "3.2.4"
      },
      {
        "code" : "3.2.5"
      },
      {
        "code" : "3.2.6"
      },
      {
        "code" : "3.3"
      },
      {
        "code" : "3.3.1"
      },
      {
        "code" : "3.4"
      },
      {
        "code" : "3.4.1"
      },
      {
        "code" : "3.4.2"
      },
      {
        "code" : "3.5"
      },
      {
        "code" : "3.5.1"
      },
      {
        "code" : "3.5.2"
      },
      {
        "code" : "3.5.3"
      },
      {
        "code" : "3.5.4"
      },
      {
        "code" : "3.5.5"
      },
      {
        "code" : "3.5.6"
      },
      {
        "code" : "3.5.7"
      },
      {
        "code" : "3.5.8"
      },
      {
        "code" : "3.6"
      },
      {
        "code" : "3.6.1"
      },
      {
        "code" : "3.6.2"
      },
      {
        "code" : "3.7"
      },
      {
        "code" : "3.7.1"
      },
      {
        "code" : "3.7.2"
      },
      {
        "code" : "3.8"
      },
      {
        "code" : "3.8.1"
      },
      {
        "code" : "3.8.2"
      },
      {
        "code" : "3.8.3"
      }]
    }]
  }
}

```
