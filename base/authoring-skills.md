# Authoring Skills - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* **Authoring Skills**

## Authoring Skills

### Authoring Skills

Each authoring skill is modeled as a [FHIR Requirements](https://hl7.org/fhir/R5/requirements.html) resource conforming to the [SGRequirements](StructureDefinition-SGRequirements.md) profile. Each skill states a capability (e.g. "Can review terminology") and contains checklist statements that define the criteria for demonstrating that capability.

Skills are organized by domain and assigned to [authoring personas](authoring-personas.md) to define each persona's skill package.

#### Skill Inventory

##### Content Review Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can review and approve content](Requirements-SGAuthoring.Skills.ReviewAndApproveContent.md) | Review and formally approve content at decision gates | Content Reviewer |

##### Project Management Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can scope DAK](Requirements-SGAuthoring.Skills.ScopeDAK.md) | Define DAK scope, source documents, and development process | Programme Manager | | [Can manage stakeholders](Requirements-SGAuthoring.Skills.ManageStakeholders.md) | Engage SMEs, coordinate consultations, manage RASCI | Programme Manager, Technical Officer | | [Can plan iterations](Requirements-SGAuthoring.Skills.PlanIterations.md) | Plan sprints, maintain backlog, facilitate retrospectives | Programme Manager |

##### L1 Review Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can review L1 guidelines](Requirements-SGAuthoring.Skills.ReviewL1Guidelines.md) | Review WHO L1 guidelines for accuracy and completeness | Technical Officer, Clinical SME, Business Analyst, QC Reviewer | | [Can interpret clinical recommendations](Requirements-SGAuthoring.Skills.InterpretClinicalRecommendations.md) | Interpret clinical recommendations with domain expertise | Clinical SME, Technical Officer |

##### L2 DAK Authoring Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can author personas](Requirements-SGAuthoring.Skills.AuthorPersonas.md) | Define generic personas from guidelines and ground-truthing | Business Analyst, Clinical SME | | [Can author user scenarios](Requirements-SGAuthoring.Skills.AuthorUserScenarios.md) | Create user scenario narratives | Business Analyst | | [Can author business processes](Requirements-SGAuthoring.Skills.AuthorBusinessProcesses.md) | Create BPMN 2.0 business process diagrams | Business Analyst | | [Can author data dictionary](Requirements-SGAuthoring.Skills.AuthorDataDictionary.md) | Define core data elements with terminology mappings | Business Analyst | | [Can author decision-support logic](Requirements-SGAuthoring.Skills.AuthorDecisionLogic.md) | Develop DMN decision-support logic tables | Business Analyst | | [Can author scheduling logic](Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.md) | Develop DMN scheduling logic tables | Business Analyst | | [Can author indicators](Requirements-SGAuthoring.Skills.AuthorIndicators.md) | Define indicators with numerator/denominator | Business Analyst | | [Can author functional requirements](Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.md) | Define functional and non-functional requirements | Business Analyst | | [Can validate DAK content](Requirements-SGAuthoring.Skills.ValidateDAKContent.md) | Review DAK for L1 accuracy and cross-component consistency | Technical Officer, Clinical SME, Business Analyst, QC Reviewer |

##### L3 FHIR Authoring Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can author logical models](Requirements-SGAuthoring.Skills.AuthorLogicalModels.md) | Create FHIR logical models from L2 data dictionaries | FHIR Modeller | | [Can author FHIR profiles](Requirements-SGAuthoring.Skills.AuthorFHIRProfiles.md) | Create FHIR profiles constraining base resources | FHIR Modeller | | [Can author questionnaires](Requirements-SGAuthoring.Skills.AuthorQuestionnaires.md) | Create FHIR Questionnaire resources | FHIR Modeller | | [Can author CQL](Requirements-SGAuthoring.Skills.AuthorCQL.md) | Write CQL for decision logic, scheduling, and indicators | FHIR Modeller | | [Can author structure maps](Requirements-SGAuthoring.Skills.AuthorStructureMaps.md) | Create FHIR StructureMaps for data extraction | FHIR Modeller | | [Can author plan definitions](Requirements-SGAuthoring.Skills.AuthorPlanDefinitions.md) | Create PlanDefinitions for processes and decision tables | FHIR Modeller | | [Can author actor definitions](Requirements-SGAuthoring.Skills.AuthorActorDefinitions.md) | Create ActorDefinitions, reusing Commons repository | FHIR Modeller | | [Can author example scenarios](Requirements-SGAuthoring.Skills.AuthorExampleScenarios.md) | Create ExampleScenario resources | FHIR Modeller | | [Can author measures](Requirements-SGAuthoring.Skills.AuthorMeasures.md) | Create FHIR Measure resources from L2 indicators | FHIR Modeller | | [Can author FHIR requirements](Requirements-SGAuthoring.Skills.AuthorFHIRRequirements.md) | Create FHIR Requirements resources | FHIR Modeller | | [Can author test cases](Requirements-SGAuthoring.Skills.AuthorTestCases.md) | Create TestPlan, TestScript, and example instances | FHIR Modeller |

##### Terminology Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can review terminology](Requirements-SGAuthoring.Skills.ReviewTerminology.md) | Review terminology bindings, code systems, and value sets | Terminologist, QC Reviewer | | [Can map concepts](Requirements-SGAuthoring.Skills.MapConcepts.md) | Map to WHO Commons, ICD-11, SNOMED CT, LOINC | Terminologist | | [Can author code systems](Requirements-SGAuthoring.Skills.AuthorCodeSystems.md) | Create and maintain FHIR CodeSystem resources | Terminologist, FHIR Modeller | | [Can author value sets](Requirements-SGAuthoring.Skills.AuthorValueSets.md) | Create and maintain FHIR ValueSet resources | Terminologist, FHIR Modeller | | [Can author concept maps](Requirements-SGAuthoring.Skills.AuthorConceptMaps.md) | Create FHIR ConceptMap resources | Terminologist, FHIR Modeller |

##### Quality Control Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can run QA checks](Requirements-SGAuthoring.Skills.RunQAChecks.md) | Run and interpret IG Publisher QA reports | QC Reviewer, FHIR Modeller, Publication Manager, Terminologist | | [Can review checklist](Requirements-SGAuthoring.Skills.ReviewChecklist.md) | Review publication checklist across L1-L4 | QC Reviewer, Publication Manager | | [Can validate artifact conformance](Requirements-SGAuthoring.Skills.ValidateArtifactConformance.md) | Verify CRMI profile conformance | QC Reviewer | | [Can validate L3 functionality](Requirements-SGAuthoring.Skills.ValidateL3Functionality.md) | Test StructureMaps, CQL, and Measures | QC Reviewer |

##### Publication Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can configure IG](Requirements-SGAuthoring.Skills.ConfigureIG.md) | Set up IG repository and sushi-config | Publication Manager, FHIR Modeller | | [Can build IG](Requirements-SGAuthoring.Skills.BuildIG.md) | Run IG Publisher build process | Publication Manager, FHIR Modeller | | [Can manage releases](Requirements-SGAuthoring.Skills.ManageReleases.md) | Manage versioning, tags, and publication workflow | Publication Manager | | [Can manage governance](Requirements-SGAuthoring.Skills.ManageGovernance.md) | Manage cross-IG shared artifacts and governance | Publication Manager, Terminologist |

##### Translation Skills

| Skill | Description | Personas | |——-|————-|———-| | [Can translate content](Requirements-SGAuthoring.Skills.TranslateContent.md) | Translate IG content across UN languages | Translator | | [Can review translations](Requirements-SGAuthoring.Skills.ReviewTranslations.md) | Review translated content for accuracy | Translator, QC Reviewer |

#### Persona Skill Packages

Each persona has a defined package of skills. The full set of skills for each persona is available on the persona's Requirements resource page:

| | | |
| :--- | :--- | :--- |
| Programme Manager | 3 | Project Management |
| Technical Officer | 4 | L1 Review, Stakeholder Management, DAK Validation |
| Clinical SME | 4 | L1 Review, Clinical Interpretation, DAK Validation |
| Business Analyst | 11 | L2 DAK Authoring (all 9 components), L1 Review |
| FHIR Modeller | 17 | L3 FHIR Authoring, Terminology, QA, IG Build |
| Terminologist | 7 | Terminology Management, Governance |
| QC Reviewer | 7 | QA, Checklists, Conformance, Functionality Testing |
| Content Reviewer | 1 | Content Approval at decision gates |
| Publication Manager | 6 | IG Configuration, Build, Release, Governance |
| Translator | 2 | Translation, Review |

#### BPMN Swimlane Validation

As part of the BPMN authoring and review process, every innermost swimlane in a BPMN diagram **SHALL** correspond to an ActorDefinition resource. The [`bpmn_layout` skill](.github/skills/bpmn_layout/skills.yaml) includes a `validate-swimlanes` command that checks this automatically.

When a swimlane has no matching ActorDefinition, the author must resolve by:

1. **Referencing**an ActorDefinition from a dependency IG
1. **Creating**a new ActorDefinition in this IG
1. **Correcting**a typo in the swimlane name

