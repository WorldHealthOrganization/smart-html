# Authoring Personas - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* **Authoring Personas**

## Authoring Personas

### Authoring Personas

SMART Guidelines and Digital Adaptation Kits (DAKs) are authored by multidisciplinary teams. The **authoring personas** defined here represent the roles involved in the authoring, review, and publication lifecycle — distinct from the clinical/health personas defined within a DAK itself.

These personas are derived from the [WHO SMART IG Starter Kit](https://smart.who.int/ig-starter-kit/) guidance on DAK development teams, authoring processes, and community of practice workstreams.

#### Persona Definitions

| | | |
| :--- | :--- | :--- |
| [Programme Manager](ActorDefinition-SGAuthoring.Persona.ProgrammeManager.md) | Manages DAK scope, timeline, resources, and stakeholder engagement | Planning |
| [Technical Officer](ActorDefinition-SGAuthoring.Persona.TechnicalOfficer.md) | Coordinates DAK work and performs first-pass content review | Planning, L2 Review |
| [Clinical SME](ActorDefinition-SGAuthoring.Persona.ClinicalSME.md) | Validates clinical accuracy against L1 guidelines | L2 Review |
| [Business Analyst](ActorDefinition-SGAuthoring.Persona.BusinessAnalyst.md) | Authors L2 DAK components (BPMN, data dictionary, logic, requirements) | L2 Authoring |
| [FHIR Modeller](ActorDefinition-SGAuthoring.Persona.FHIRModeller.md) | Authors L3 FHIR artifacts from L2 specifications | L3 Authoring |
| [Terminologist](ActorDefinition-SGAuthoring.Persona.Terminologist.md) | Manages terminology, concept mappings, and WHO Commons dictionary | L3 Authoring, Governance |
| [QC Reviewer](ActorDefinition-SGAuthoring.Persona.QCReviewer.md) | Reviews publication readiness using checklists and QA reports | Quality Control |
| [Content Reviewer](ActorDefinition-SGAuthoring.Persona.ContentReviewer.md) | Approves content at decision gates (L2→L3, draft→publication) | Review / Approval |
| [Publication Manager](ActorDefinition-SGAuthoring.Persona.PublicationManager.md) | Manages IG configuration, builds, versioning, and releases | Publication |
| [Translator](ActorDefinition-SGAuthoring.Persona.Translator.md) | Translates IG content across UN languages | Translation |

#### RASCI Matrix

The IG Starter Kit recommends defining a RASCI (Responsible, Accountable, Support, Consulted, Informed) matrix. Below is a reference matrix mapping personas to lifecycle phases:

| | | | | | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Planning | **A/R** | S | C | C | I | I | I | I | I | I |
| L2 Authoring | S | **A** | C | **R** | I | C | I | I | I | I |
| Clinical Review | I | S | **A/R** | S | I | I | I | C | I | I |
| L3 Authoring | I | I | C | S | **A/R** | **R** | I | I | S | I |
| Quality Control | I | I | C | S | S | S | **A/R** | S | S | I |
| Content Approval | I | I | C | I | S | I | S | **A/R** | I | I |
| Translation | I | I | C | I | S | I | S | I | I | **A/R** |
| Publication | I | I | I | I | S | I | S | S | **A/R** | I |

**Legend**: **R** = Responsible, **A** = Accountable, **S** = Support, **C** = Consulted, **I** = Informed

#### Relationship to DAK Personas

These authoring personas should not be confused with DAK component 2 "Generic Personas" which represent end users of healthcare systems (e.g. Community Health Worker, Healthcare Provider). The authoring personas represent the people who **create** the SMART Guidelines, while DAK personas represent the people who **use** the resulting digital systems.

