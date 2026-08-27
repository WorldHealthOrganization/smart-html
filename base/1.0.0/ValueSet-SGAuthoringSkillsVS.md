# SMART Guidelines Authoring Skills ValueSet - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Authoring Skills ValueSet**

## ValueSet: SMART Guidelines Authoring Skills ValueSet (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/SGAuthoringSkillsVS | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGAuthoringSkillsVS |

 
ValueSet for all SMART Guidelines authoring skill capabilities 

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

##### SMART Guidelines Authoring Skills ValueSet Schema API

JSON Schema for SMART Guidelines Authoring Skills ValueSet ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-SGAuthoringSkillsVS.schema.json

#### JSON Schema definition for the enumeration ValueSet-SGAuthoringSkillsVS

This endpoint serves the JSON Schema definition for the enumeration ValueSet-SGAuthoringSkillsVS.

## Schema Definition

### ValueSet-SGAuthoringSkillsVS

**Description:** JSON Schema for SMART Guidelines Authoring Skills ValueSet ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "SGAuthoringSkillsVS",
  "url" : "http://smart.who.int/base/ValueSet/SGAuthoringSkillsVS",
  "version" : "1.0.0",
  "name" : "SGAuthoringSkillsVS",
  "title" : "SMART Guidelines Authoring Skills ValueSet",
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
  "description" : "ValueSet for all SMART Guidelines authoring skill capabilities",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/SGAuthoringSkills"
    }]
  }
}

```
