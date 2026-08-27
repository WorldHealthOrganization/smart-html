# Digital Health Interventions for Persons - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Digital Health Interventions for Persons**

## ValueSet: Digital Health Interventions for Persons (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/CDHIv2.1 | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CDHIv2.1 |

 
Digital Health Interventions whose primary user group is Persons (health service users). Group 1 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023). 

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

##### Digital Health Interventions for Persons Schema API

JSON Schema for Digital Health Interventions for Persons ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-CDHIv2.1.schema.json

#### JSON Schema definition for the enumeration ValueSet-CDHIv2.1

This endpoint serves the JSON Schema definition for the enumeration ValueSet-CDHIv2.1.

## Schema Definition

### ValueSet-CDHIv2.1

**Description:** JSON Schema for Digital Health Interventions for Persons ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "CDHIv2.1",
  "url" : "http://smart.who.int/base/ValueSet/CDHIv2.1",
  "version" : "1.0.0",
  "name" : "CDHIv2.1",
  "title" : "Digital Health Interventions for Persons",
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
  "description" : "Digital Health Interventions whose primary user group is Persons (health service users). Group 1 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023).",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/CDHIv2",
      "concept" : [{
        "code" : "1"
      },
      {
        "code" : "1.1"
      },
      {
        "code" : "1.1.1"
      },
      {
        "code" : "1.1.2"
      },
      {
        "code" : "1.1.3"
      },
      {
        "code" : "1.1.4"
      },
      {
        "code" : "1.2"
      },
      {
        "code" : "1.2.1"
      },
      {
        "code" : "1.2.2"
      },
      {
        "code" : "1.3"
      },
      {
        "code" : "1.3.1"
      },
      {
        "code" : "1.4"
      },
      {
        "code" : "1.4.1"
      },
      {
        "code" : "1.4.2"
      },
      {
        "code" : "1.4.3"
      },
      {
        "code" : "1.4.4"
      },
      {
        "code" : "1.5"
      },
      {
        "code" : "1.5.1"
      },
      {
        "code" : "1.5.2"
      },
      {
        "code" : "1.6"
      },
      {
        "code" : "1.6.1"
      },
      {
        "code" : "1.6.2"
      },
      {
        "code" : "1.7"
      },
      {
        "code" : "1.7.1"
      },
      {
        "code" : "1.7.2"
      },
      {
        "code" : "1.7.3"
      },
      {
        "code" : "1.8"
      },
      {
        "code" : "1.8.1"
      }]
    }]
  }
}

```
