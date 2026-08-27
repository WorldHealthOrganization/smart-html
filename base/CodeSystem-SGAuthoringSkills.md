# SMART Guidelines Authoring Skills - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Authoring Skills**

## CodeSystem: SMART Guidelines Authoring Skills (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/SGAuthoringSkills | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGAuthoringSkills |

 
CodeSystem for SMART Guidelines authoring skill capabilities. Each code represents a discrete skill that an authoring persona may possess. Skills are used to define Requirements resources as capability statements. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [SMART Guidelines Authoring Skills ValueSet](ValueSet-SGAuthoringSkillsVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "SGAuthoringSkills",
  "url" : "http://smart.who.int/base/CodeSystem/SGAuthoringSkills",
  "version" : "1.0.0",
  "name" : "SGAuthoringSkills",
  "title" : "SMART Guidelines Authoring Skills",
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
  "description" : "CodeSystem for SMART Guidelines authoring skill capabilities.\nEach code represents a discrete skill that an authoring persona may possess.\nSkills are used to define Requirements resources as capability statements.",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 42,
  "concept" : [{
    "code" : "can-review-l1-guidelines",
    "display" : "Can review L1 guidelines",
    "definition" : "Ability to review WHO L1 narrative guidelines and normative products for accuracy and completeness"
  },
  {
    "code" : "can-interpret-clinical-recommendations",
    "display" : "Can interpret clinical recommendations",
    "definition" : "Ability to interpret clinical recommendations from L1 source documents"
  },
  {
    "code" : "can-identify-health-interventions",
    "display" : "Can identify health interventions",
    "definition" : "Ability to identify and catalogue health interventions from WHO UHC menu and guidelines"
  },
  {
    "code" : "can-author-personas",
    "display" : "Can author personas",
    "definition" : "Ability to define generic personas based on task-shifting guidelines and ground-truthing"
  },
  {
    "code" : "can-author-user-scenarios",
    "display" : "Can author user scenarios",
    "definition" : "Ability to create user scenario narratives depicting typical workflows"
  },
  {
    "code" : "can-author-business-processes",
    "display" : "Can author business processes",
    "definition" : "Ability to create BPMN 2.0 business process diagrams for DAK workflows"
  },
  {
    "code" : "can-author-data-dictionary",
    "display" : "Can author data dictionary",
    "definition" : "Ability to define core data elements and map to standard terminologies"
  },
  {
    "code" : "can-author-decision-logic",
    "display" : "Can author decision-support logic",
    "definition" : "Ability to develop decision-support logic tables following DMN standard"
  },
  {
    "code" : "can-author-scheduling-logic",
    "display" : "Can author scheduling logic",
    "definition" : "Ability to develop scheduling logic tables following DMN standard"
  },
  {
    "code" : "can-author-indicators",
    "display" : "Can author indicators",
    "definition" : "Ability to define indicators and performance metrics with numerator/denominator specifications"
  },
  {
    "code" : "can-author-functional-requirements",
    "display" : "Can author functional requirements",
    "definition" : "Ability to define high-level functional and non-functional requirements"
  },
  {
    "code" : "can-validate-dak-content",
    "display" : "Can validate DAK content",
    "definition" : "Ability to review and validate DAK components against L1 source documents"
  },
  {
    "code" : "can-author-logical-models",
    "display" : "Can author logical models",
    "definition" : "Ability to create FHIR logical models from L2 data dictionaries"
  },
  {
    "code" : "can-author-fhir-profiles",
    "display" : "Can author FHIR profiles",
    "definition" : "Ability to create FHIR StructureDefinitions and profiles"
  },
  {
    "code" : "can-author-questionnaires",
    "display" : "Can author questionnaires",
    "definition" : "Ability to create FHIR Questionnaire resources from L2 forms"
  },
  {
    "code" : "can-author-cql",
    "display" : "Can author CQL",
    "definition" : "Ability to write Clinical Quality Language for decision logic, scheduling, and indicators"
  },
  {
    "code" : "can-author-structure-maps",
    "display" : "Can author structure maps",
    "definition" : "Ability to create FHIR StructureMaps for data extraction"
  },
  {
    "code" : "can-author-plan-definitions",
    "display" : "Can author plan definitions",
    "definition" : "Ability to create FHIR PlanDefinitions for business processes and decision tables"
  },
  {
    "code" : "can-author-actor-definitions",
    "display" : "Can author actor definitions",
    "definition" : "Ability to create FHIR ActorDefinitions from L2 personas"
  },
  {
    "code" : "can-author-example-scenarios",
    "display" : "Can author example scenarios",
    "definition" : "Ability to create ExampleScenario resources from L2 user scenarios"
  },
  {
    "code" : "can-author-measures",
    "display" : "Can author measures",
    "definition" : "Ability to create FHIR Measure resources from L2 indicators"
  },
  {
    "code" : "can-author-fhir-requirements",
    "display" : "Can author FHIR requirements",
    "definition" : "Ability to create FHIR Requirements resources from L2 requirements"
  },
  {
    "code" : "can-author-test-cases",
    "display" : "Can author test cases",
    "definition" : "Ability to create TestPlan, TestScript, and example instances for validation"
  },
  {
    "code" : "can-review-terminology",
    "display" : "Can review terminology",
    "definition" : "Ability to review and validate terminology bindings, code systems, and value sets"
  },
  {
    "code" : "can-map-concepts",
    "display" : "Can map concepts",
    "definition" : "Ability to map data elements to WHO Commons dictionary, ICD-11, SNOMED CT, LOINC"
  },
  {
    "code" : "can-author-code-systems",
    "display" : "Can author code systems",
    "definition" : "Ability to create and maintain FHIR CodeSystem resources"
  },
  {
    "code" : "can-author-value-sets",
    "display" : "Can author value sets",
    "definition" : "Ability to create and maintain FHIR ValueSet resources"
  },
  {
    "code" : "can-author-concept-maps",
    "display" : "Can author concept maps",
    "definition" : "Ability to create FHIR ConceptMap resources for cross-terminology mappings"
  },
  {
    "code" : "can-run-qa-checks",
    "display" : "Can run QA checks",
    "definition" : "Ability to run and interpret IG Publisher QA validation reports"
  },
  {
    "code" : "can-review-checklist",
    "display" : "Can review checklist",
    "definition" : "Ability to review SMART Guidelines publication checklist across L1-L4 layers"
  },
  {
    "code" : "can-validate-artifact-conformance",
    "display" : "Can validate artifact conformance",
    "definition" : "Ability to verify conformance to Shareable, Publishable, Computable, and Executable profiles"
  },
  {
    "code" : "can-validate-l3-functionality",
    "display" : "Can validate L3 functionality",
    "definition" : "Ability to test StructureMap extraction, CQL execution, and measure calculation"
  },
  {
    "code" : "can-configure-ig",
    "display" : "Can configure IG",
    "definition" : "Ability to set up and configure a FHIR Implementation Guide (sushi-config, canonical URL, packages)"
  },
  {
    "code" : "can-build-ig",
    "display" : "Can build IG",
    "definition" : "Ability to run the FHIR IG Publisher build process"
  },
  {
    "code" : "can-manage-releases",
    "display" : "Can manage releases",
    "definition" : "Ability to manage versioning, publication-request.json, release tags, and publication workflow"
  },
  {
    "code" : "can-manage-governance",
    "display" : "Can manage governance",
    "definition" : "Ability to manage cross-IG governance for shared artifacts (commons personas, terminology, libraries)"
  },
  {
    "code" : "can-translate-content",
    "display" : "Can translate content",
    "definition" : "Ability to translate IG content across UN languages"
  },
  {
    "code" : "can-review-translations",
    "display" : "Can review translations",
    "definition" : "Ability to review translated content for accuracy and completeness"
  },
  {
    "code" : "can-review-and-approve-content",
    "display" : "Can review and approve content",
    "definition" : "Ability to review and formally approve SMART Guidelines content at decision gates"
  },
  {
    "code" : "can-scope-dak",
    "display" : "Can scope DAK",
    "definition" : "Ability to define DAK scope, identify source documents, and establish development process"
  },
  {
    "code" : "can-manage-stakeholders",
    "display" : "Can manage stakeholders",
    "definition" : "Ability to engage SMEs, coordinate consultations, and manage RASCI matrix"
  },
  {
    "code" : "can-plan-iterations",
    "display" : "Can plan iterations",
    "definition" : "Ability to plan sprint iterations, maintain backlog, and facilitate retrospectives"
  }]
}

```
