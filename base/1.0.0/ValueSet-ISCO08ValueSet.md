# ISCO-08 Value Set - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ISCO-08 Value Set**

## ValueSet: ISCO-08 Value Set 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/ISCO08ValueSet | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:ISCO08ValueSet |

 
Extensible value set of ISCO-08 codes for persona classification 

 **References** 

* [Generic Persona (DAK)](StructureDefinition-GenericPersona.md)

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



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "ISCO08ValueSet",
  "url" : "http://smart.who.int/base/ValueSet/ISCO08ValueSet",
  "version" : "1.0.0",
  "name" : "ISCO08ValueSet",
  "title" : "ISCO-08 Value Set",
  "status" : "active",
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
  "description" : "Extensible value set of ISCO-08 codes for persona classification",
  "compose" : {
    "include" : [{
      "system" : "http://www.ilo.org/public/english/bureau/stat/isco/isco08/"
    }]
  }
}

```
