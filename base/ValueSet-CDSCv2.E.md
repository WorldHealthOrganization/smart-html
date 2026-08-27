# Services and Application Types: Surveillance and Response - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Services and Application Types: Surveillance and Response**

## ValueSet: Services and Application Types: Surveillance and Response (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/CDSCv2.E | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CDSCv2.E |

 
Systems that support the detection, monitoring, and response to disease outbreaks and public health threats. Group E of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023). 

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

##### Services and Application Types: Surveillance and Response Schema API

JSON Schema for Services and Application Types: Surveillance and Response ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-CDSCv2.E.schema.json

#### JSON Schema definition for the enumeration ValueSet-CDSCv2.E

This endpoint serves the JSON Schema definition for the enumeration ValueSet-CDSCv2.E.

## Schema Definition

### ValueSet-CDSCv2.E

**Description:** JSON Schema for Services and Application Types: Surveillance and Response ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "CDSCv2.E",
  "url" : "http://smart.who.int/base/ValueSet/CDSCv2.E",
  "version" : "1.0.0",
  "name" : "CDSCv2.E",
  "title" : "Services and Application Types: Surveillance and Response",
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
  "description" : "Systems that support the detection, monitoring, and response to disease outbreaks and public health threats. Group E of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023).",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/CDSCv2",
      "concept" : [{
        "code" : "E"
      },
      {
        "code" : "E1"
      },
      {
        "code" : "E2"
      }]
    }]
  }
}

```
