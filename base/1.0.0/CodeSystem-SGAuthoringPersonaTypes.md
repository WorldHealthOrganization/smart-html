# SMART Guidelines Authoring Persona Types - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Authoring Persona Types**

## CodeSystem: SMART Guidelines Authoring Persona Types (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/SGAuthoringPersonaTypes | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGAuthoringPersonaTypes |

 
CodeSystem for SMART Guidelines authoring persona types. These represent roles involved in the authoring, review, and publication of SMART Guidelines and Digital Adaptation Kits, as distinct from the clinical/health personas defined within a DAK. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [SMART Guidelines Authoring Persona Types ValueSet](ValueSet-SGAuthoringPersonaTypesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "SGAuthoringPersonaTypes",
  "url" : "http://smart.who.int/base/CodeSystem/SGAuthoringPersonaTypes",
  "version" : "1.0.0",
  "name" : "SGAuthoringPersonaTypes",
  "title" : "SMART Guidelines Authoring Persona Types",
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
  "description" : "CodeSystem for SMART Guidelines authoring persona types.\nThese represent roles involved in the authoring, review, and publication\nof SMART Guidelines and Digital Adaptation Kits, as distinct from\nthe clinical/health personas defined within a DAK.",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 10,
  "concept" : [{
    "code" : "programme-manager",
    "display" : "Programme Manager",
    "definition" : "Manages DAK development scope, timeline, resources, and stakeholder engagement"
  },
  {
    "code" : "technical-officer",
    "display" : "Technical Officer",
    "definition" : "Coordinates DAK development work and performs first-pass content review"
  },
  {
    "code" : "clinical-sme",
    "display" : "Clinical Subject Matter Expert",
    "definition" : "Validates clinical accuracy of DAK content against L1 guidelines"
  },
  {
    "code" : "business-analyst",
    "display" : "Business Analyst",
    "definition" : "Authors L2 DAK components including business processes, data dictionaries, and requirements"
  },
  {
    "code" : "fhir-modeller",
    "display" : "FHIR Modeller",
    "definition" : "Authors L3 FHIR artifacts from L2 DAK specifications"
  },
  {
    "code" : "terminologist",
    "display" : "Terminologist",
    "definition" : "Manages terminology bindings, concept mappings, and WHO Commons dictionary alignment"
  },
  {
    "code" : "qc-reviewer",
    "display" : "Quality Control Reviewer",
    "definition" : "Reviews publication readiness using checklists and QA validation reports"
  },
  {
    "code" : "publication-manager",
    "display" : "Publication Manager",
    "definition" : "Manages IG configuration, build process, versioning, and release publication"
  },
  {
    "code" : "content-reviewer",
    "display" : "Content Reviewer / Approver",
    "definition" : "Reviews and formally approves content at decision gates in the authoring lifecycle"
  },
  {
    "code" : "translator",
    "display" : "Translator",
    "definition" : "Translates IG content across UN languages"
  }]
}

```
