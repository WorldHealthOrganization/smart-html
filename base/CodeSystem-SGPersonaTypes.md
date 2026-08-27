# SMART Guidelines Persona Types - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Persona Types**

## CodeSystem: SMART Guidelines Persona Types (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/SGPersonaTypes | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGPersonaTypes |

 
CodeSystem for SMART Guidelines Persona Types 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Smart Guidelines Persona Types Value Set](ValueSet-SGPersonaTypesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "SGPersonaTypes",
  "url" : "http://smart.who.int/base/CodeSystem/SGPersonaTypes",
  "version" : "1.0.0",
  "name" : "SGPersonaTypes",
  "title" : "SMART Guidelines Persona Types",
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
  "description" : "CodeSystem for SMART Guidelines Persona Types",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "key",
    "display" : "Key Persona",
    "definition" : "Key Persona for workflows in this DAK"
  },
  {
    "code" : "related",
    "display" : "Related Persona",
    "definition" : "Related Personas that don't directly enact in any workflow in this DAK"
  },
  {
    "code" : "system",
    "display" : "System",
    "definition" : "Digital Systems that interact in this DAK"
  },
  {
    "code" : "hardware",
    "display" : "Hardware Device",
    "definition" : "Hardware devices required to perform workflows in the DAK"
  }]
}

```
