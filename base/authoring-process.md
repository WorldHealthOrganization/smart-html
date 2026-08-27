# Authoring Process - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* **Authoring Process**

## Authoring Process

### Authoring Process

The SMART Guidelines authoring lifecycle encompasses DAK development, L3 FHIR authoring, quality control, translation, and publication. This process is defined as a BPMN 2.0 collaboration diagram with swimlanes for each [authoring persona](authoring-personas.md).

The process is based on the [WHO SMART IG Starter Kit](https://smart.who.int/ig-starter-kit/) guidance.

#### Lifecycle Overview

```
Phase 1          Phase 2a         Phase 2b        Phase 3       Phase 4
PLANNING    →    L2 DAK      →    L3 FHIR    →    QUALITY   →   PUBLICATION
                 AUTHORING        AUTHORING       CONTROL
Programme        Business         FHIR            QC            Publication
Manager          Analyst          Modeller        Reviewer      Manager
                 Clinical SME     Terminologist   Translator
                 Technical Officer

```

#### Phase 1: Planning (Programme Manager)

1. **Scoping**— Define DAK purpose, target audience, and gaps
1. **Form team**— Assemble DAK development team (<10 people), define RASCI matrix
1. **Establish process**— Select Agile/Scrum methodology and project tooling
1. **Gather source documents**— Collect WHO guidelines, registers, policy documents
1. **Plan timeline**— Draft project roadmap, create backlog, set sprint cadence
1. **Plan consultations**— Schedule SME consultation format and frequency
1. **Assign work**— Begin sprint cycle

#### Phase 2a: L2 DAK Authoring (Business Analyst, iterative)

The L2 authoring follows an iterative sprint cycle of **Fill → Validate → Incorporate**:

1. **Review L1 source documents**for current sprint scope
1. **Identify health interventions and recommendations**(Component 1)
1. **Author generic personas**(Component 2)
1. **Author user scenarios**(Component 3)
1. **Author BPMN business processes**(Component 4)
1. **For each business process:**
* Draft detailed workflow annotations
* Define core data elements (Component 5)
* Develop decision-support logic (Component 6)
* Develop scheduling logic (Component 7)
* List indicators and metrics (Component 8)
* Define functional/non-functional requirements (Component 9)

1. **Streamline**all DAK components for cross-component consistency
1. **Validate with SMEs**(Clinical SME review)
1. **Incorporate feedback**and begin next sprint

#### Clinical Review (Clinical SME)

* Validate DAK components against L1 recommendations
* Ground-truth with field practice (country visits, facility interviews)
* Provide clinical feedback and identify gaps

#### Phase 2b: L3 FHIR Authoring (FHIR Modeller)

1. **Verify L2 input**availability and consistency
1. **Set up IG repository**from smart-ig-empty template
1. **Author L3 artifacts**in recommended sequence:
* Logical Models → Profiles → Questionnaires → StructureMaps
* CodeSystems, ValueSets, ConceptMaps (with Terminologist)
* CQL (decision logic, scheduling, indicators)
* PlanDefinitions (processes, decision tables)
* ActorDefinitions (reusing Commons repository)
* Measures, Requirements, Scenarios, Tests

1. **Run IG Publisher build**and fix issues iteratively

#### Terminology Management (Terminologist, concurrent with L3)

* Review terminology bindings and code systems
* Map concepts to WHO Commons dictionary
* Map to ICD-11, SNOMED CT, LOINC
* Onboard new concepts through governance process

#### Phase 3: Quality Control (QC Reviewer)

1. **Review QA report**(qa.html) from IG Publisher
1. **Review checklist**items across L1, L2, L3, L4, Global sections
1. **Validate artifact conformance**to CRMI profiles
1. **Test L3 functionality**(StructureMaps, CQL, Measures)
1. **Decision gate**: Publication ready?
* **No**: Report issues to FHIR Modeller for resolution → re-review
* **Yes**: Approve for publication

1. **Review translated content**for completeness

#### Translation (Translator, concurrent with QC)

* Translate narrative and resource metadata
* Create example resources per UN language
* Submit translations for QC review

#### Phase 4: Publication (Publication Manager)

1. **Review changes**since last release, determine version number
1. **Optionally create**release-candidate branch
1. **Update IG status**— status=active, version=X.Y.Z, releaseLabel=release
1. **Create publication-request.json**
1. **Run final build**and verify
1. **Create GitHub release and tag**(vX.Y.Z) — triggers automated workflow
1. **Verify**automated publication succeeded (sitepreview)
1. **Request WHO team**to update smart.who.int
1. **Reset main**to draft, update version for next cycle

#### BPMN Process Diagram

The formal BPMN 2.0 process diagram is available at: [SGAuthoring.DAKLifecycle.bpmn](bpmn/SGAuthoring.DAKLifecycle.bpmn)

This diagram models the full lifecycle as a collaboration with swimlanes for each authoring persona, including message flows between participants for handoffs (e.g. Business Analyst → Clinical SME for validation, QC Reviewer → Publication Manager for approval).

