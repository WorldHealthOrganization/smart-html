# Mapping from CDSC v1 to Services and Application Types v2 - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mapping from CDSC v1 to Services and Application Types v2**

## ConceptMap: Mapping from CDSC v1 to Services and Application Types v2 (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ConceptMap/CDSCv1toCDSCv2 | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:CDSCv1toCDSCv2 |

 
Mapping from the Classification of Digital Health System Categories v1 (CDSCv1, 2018) to the Classification of Digital Health Services and Application Types v2 (CDSCv2, 2023). 
The v1 used 25 single-letter codes (A–Y). The v2 completely restructured this into 5 representations within the digital health enterprise architecture, each with alphanumeric codes (A1–A9, B1–B8, C1–C11, D1–D8, E1–E2). 
Several new v2 categories have no v1 equivalent: A3 (Decision support), A4 (Diagnostics), B1 (Blood bank), B3 (Health program monitoring), B7 (Patient administration), C4 (Facility registries), C5 (Health worker registry), C7 (Immunisation information), C8 (Master patient index), C9 (Product catalogues), C10 (Public Key directories), D1 (Analytics), D3 (Data warehouses). 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "CDSCv1toCDSCv2",
  "url" : "http://smart.who.int/base/ConceptMap/CDSCv1toCDSCv2",
  "version" : "1.0.0",
  "name" : "CDSCv1toCDSCv2",
  "title" : "Mapping from CDSC v1 to Services and Application Types v2",
  "status" : "draft",
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
  "description" : "Mapping from the Classification of Digital Health System Categories v1 (CDSCv1, 2018)\nto the Classification of Digital Health Services and Application Types v2 (CDSCv2, 2023).\n\nThe v1 used 25 single-letter codes (A–Y). The v2 completely restructured this into\n5 representations within the digital health enterprise architecture, each with\nalphanumeric codes (A1–A9, B1–B8, C1–C11, D1–D8, E1–E2).\n\nSeveral new v2 categories have no v1 equivalent:\nA3 (Decision support), A4 (Diagnostics), B1 (Blood bank), B3 (Health program monitoring),\nB7 (Patient administration), C4 (Facility registries), C5 (Health worker registry),\nC7 (Immunisation information), C8 (Master patient index), C9 (Product catalogues),\nC10 (Public Key directories), D1 (Analytics), D3 (Data warehouses).",
  "sourceCanonical" : "http://smart.who.int/base/ValueSet/CDSCv1",
  "targetCanonical" : "http://smart.who.int/base/ValueSet/CDSCv2",
  "group" : [{
    "source" : "http://smart.who.int/base/CodeSystem/CDSCv1",
    "target" : "http://smart.who.int/base/CodeSystem/CDSCv2",
    "element" : [{
      "code" : "A",
      "target" : [{
        "code" : "C1",
        "equivalence" : "equivalent",
        "comment" : "v1 'Census; population information & data warehouse' → v2 C1 'Census and population information systems'"
      }]
    },
    {
      "code" : "B",
      "target" : [{
        "code" : "C2",
        "equivalence" : "equivalent",
        "comment" : "v1 'Civil Registration and Vital Statistics' → v2 C2 [same concept; refined name]"
      }]
    },
    {
      "code" : "C",
      "target" : [{
        "code" : "A7",
        "equivalence" : "inexact",
        "comment" : "v1 'Client applications' [broad] most closely maps to v2 A7 'Personal health records'; point-of-service apps generally fall under A. group"
      }]
    },
    {
      "code" : "D",
      "target" : [{
        "code" : "A1",
        "equivalence" : "equivalent",
        "comment" : "v1 'Client communication system' → v2 A1 'Communication systems'"
      }]
    },
    {
      "code" : "E",
      "target" : [{
        "code" : "C11",
        "equivalence" : "equivalent",
        "comment" : "v1 'Clinical terminology and classifications' → v2 C11 'Terminology and classification systems'"
      }]
    },
    {
      "code" : "F",
      "target" : [{
        "code" : "A2",
        "equivalence" : "equivalent",
        "comment" : "v1 'Community-based Information System' → v2 A2 'Community-based information systems'"
      }]
    },
    {
      "code" : "G",
      "target" : [{
        "code" : "D2",
        "equivalence" : "equivalent",
        "comment" : "v1 'Data interchange interoperability and accessibility' → v2 D2 'Data interchange and interoperability'"
      }]
    },
    {
      "code" : "H",
      "target" : [{
        "code" : "A5",
        "equivalence" : "equivalent",
        "comment" : "v1 'Electronic Medical Record' → v2 A5 'Electronic medical record systems'"
      }]
    },
    {
      "code" : "I",
      "target" : [{
        "code" : "E1",
        "equivalence" : "equivalent",
        "comment" : "v1 'Emergency response system' → v2 E1 'Emergency preparedness and response systems'"
      }]
    },
    {
      "code" : "J",
      "target" : [{
        "code" : "D4",
        "equivalence" : "equivalent",
        "comment" : "v1 'Environmental monitoring systems' → v2 D4 'Environmental monitoring systems'"
      }]
    },
    {
      "code" : "K",
      "target" : [{
        "code" : "C3",
        "equivalence" : "equivalent",
        "comment" : "v1 'Facility Management Information System' → v2 C3 'Facility management information systems'"
      }]
    },
    {
      "code" : "L",
      "target" : [{
        "code" : "D5",
        "equivalence" : "equivalent",
        "comment" : "v1 'Geographic Information Systems' → v2 D5 'Geographic information systems [GIS]'"
      }]
    },
    {
      "code" : "M",
      "target" : [{
        "code" : "B2",
        "equivalence" : "equivalent",
        "comment" : "v1 'Health finance and insurance system' → v2 B2 'Health finance-related information systems'"
      }]
    },
    {
      "code" : "N",
      "target" : [{
        "code" : "D6",
        "equivalence" : "equivalent",
        "comment" : "v1 'Health Management Information System' → v2 D6 'Health Management Information systems [HMIS]'"
      }]
    },
    {
      "code" : "O",
      "target" : [{
        "code" : "B4",
        "equivalence" : "equivalent",
        "comment" : "v1 'Human Resource Information System' → v2 B4 'Human resource information systems'"
      }]
    },
    {
      "code" : "P",
      "target" : [{
        "code" : "C6",
        "equivalence" : "equivalent",
        "comment" : "v1 'Identification registries and directories' → v2 C6 [same concept]"
      }]
    },
    {
      "code" : "Q",
      "target" : [{
        "code" : "D7",
        "equivalence" : "equivalent",
        "comment" : "v1 'Knowledge Management' → v2 D7 'Knowledge management systems'"
      }]
    },
    {
      "code" : "R",
      "target" : [{
        "code" : "A6",
        "equivalence" : "equivalent",
        "comment" : "v1 'Laboratory and Diagnostic System' → v2 A6 'Laboratory information systems'"
      }]
    },
    {
      "code" : "S",
      "target" : [{
        "code" : "B5",
        "equivalence" : "equivalent",
        "comment" : "v1 'Learning and Training System' → v2 B5 'Learning and training systems'"
      }]
    },
    {
      "code" : "T",
      "target" : [{
        "code" : "B6",
        "equivalence" : "equivalent",
        "comment" : "v1 'Logistics Management Information System' → v2 B6 'Logistics management information systems [LMIS]'"
      }]
    },
    {
      "code" : "U",
      "target" : [{
        "code" : "A8",
        "equivalence" : "equivalent",
        "comment" : "v1 'Pharmacy Information System' → v2 A8 'Pharmacy information systems'"
      }]
    },
    {
      "code" : "V",
      "target" : [{
        "code" : "E2",
        "equivalence" : "equivalent",
        "comment" : "v1 'Public health and disease surveillance' → v2 E2 'Public health and disease surveillance systems'"
      }]
    },
    {
      "code" : "W",
      "target" : [{
        "code" : "B8",
        "equivalence" : "equivalent",
        "comment" : "v1 'Research information system' → v2 B8 'Research information systems'"
      }]
    },
    {
      "code" : "X",
      "target" : [{
        "code" : "D8",
        "equivalence" : "equivalent",
        "comment" : "v1 'SHR and health information repositories' → v2 D8 'Shared Health Record and Health Information Repository'"
      }]
    },
    {
      "code" : "Y",
      "target" : [{
        "code" : "A9",
        "equivalence" : "equivalent",
        "comment" : "v1 'Telemedicine' → v2 A9 'Telehealth systems'"
      }]
    }]
  }]
}

```
