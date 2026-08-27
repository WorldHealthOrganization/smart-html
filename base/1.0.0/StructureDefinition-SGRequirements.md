# SMART Guidelines Requirements - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Requirements**

## Resource Profile: SMART Guidelines Requirements 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGRequirements | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:SGRequirements |

 
Smart Guidelines Requirements 

**Usages:**

* Refer to this Profile: [SGRequirementExt](StructureDefinition-SGRequirementExt.md) and [Satisfies](StructureDefinition-Satisfies.md)
* Examples for this Profile: [SkillAuthorActorDefinitions](Requirements-SGAuthoring.Skills.AuthorActorDefinitions.md), [SkillAuthorBusinessProcesses](Requirements-SGAuthoring.Skills.AuthorBusinessProcesses.md), [SkillAuthorCQL](Requirements-SGAuthoring.Skills.AuthorCQL.md), [SkillAuthorCodeSystems](Requirements-SGAuthoring.Skills.AuthorCodeSystems.md)... Show 37 more, [SkillAuthorConceptMaps](Requirements-SGAuthoring.Skills.AuthorConceptMaps.md), [SkillAuthorDataDictionary](Requirements-SGAuthoring.Skills.AuthorDataDictionary.md), [SkillAuthorDecisionLogic](Requirements-SGAuthoring.Skills.AuthorDecisionLogic.md), [SkillAuthorExampleScenarios](Requirements-SGAuthoring.Skills.AuthorExampleScenarios.md), [SkillAuthorFHIRProfiles](Requirements-SGAuthoring.Skills.AuthorFHIRProfiles.md), [SkillAuthorFHIRRequirements](Requirements-SGAuthoring.Skills.AuthorFHIRRequirements.md), [SkillAuthorFunctionalRequirements](Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.md), [SkillAuthorIndicators](Requirements-SGAuthoring.Skills.AuthorIndicators.md), [SkillAuthorLogicalModels](Requirements-SGAuthoring.Skills.AuthorLogicalModels.md), [SkillAuthorMeasures](Requirements-SGAuthoring.Skills.AuthorMeasures.md), [SkillAuthorPersonas](Requirements-SGAuthoring.Skills.AuthorPersonas.md), [SkillAuthorPlanDefinitions](Requirements-SGAuthoring.Skills.AuthorPlanDefinitions.md), [SkillAuthorQuestionnaires](Requirements-SGAuthoring.Skills.AuthorQuestionnaires.md), [SkillAuthorSchedulingLogic](Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.md), [SkillAuthorStructureMaps](Requirements-SGAuthoring.Skills.AuthorStructureMaps.md), [SkillAuthorTestCases](Requirements-SGAuthoring.Skills.AuthorTestCases.md), [SkillAuthorUserScenarios](Requirements-SGAuthoring.Skills.AuthorUserScenarios.md), [SkillAuthorValueSets](Requirements-SGAuthoring.Skills.AuthorValueSets.md), [SkillBuildIG](Requirements-SGAuthoring.Skills.BuildIG.md), [SkillConfigureIG](Requirements-SGAuthoring.Skills.ConfigureIG.md), [SkillInterpretClinicalRecommendations](Requirements-SGAuthoring.Skills.InterpretClinicalRecommendations.md), [SkillManageGovernance](Requirements-SGAuthoring.Skills.ManageGovernance.md), [SkillManageReleases](Requirements-SGAuthoring.Skills.ManageReleases.md), [SkillManageStakeholders](Requirements-SGAuthoring.Skills.ManageStakeholders.md), [SkillMapConcepts](Requirements-SGAuthoring.Skills.MapConcepts.md), [SkillPlanIterations](Requirements-SGAuthoring.Skills.PlanIterations.md), [SkillReviewAndApproveContent](Requirements-SGAuthoring.Skills.ReviewAndApproveContent.md), [SkillReviewChecklist](Requirements-SGAuthoring.Skills.ReviewChecklist.md), [SkillReviewL1Guidelines](Requirements-SGAuthoring.Skills.ReviewL1Guidelines.md), [SkillReviewTerminology](Requirements-SGAuthoring.Skills.ReviewTerminology.md), [SkillReviewTranslations](Requirements-SGAuthoring.Skills.ReviewTranslations.md), [SkillRunQAChecks](Requirements-SGAuthoring.Skills.RunQAChecks.md), [SkillScopeDAK](Requirements-SGAuthoring.Skills.ScopeDAK.md), [SkillTranslateContent](Requirements-SGAuthoring.Skills.TranslateContent.md), [SkillValidateArtifactConformance](Requirements-SGAuthoring.Skills.ValidateArtifactConformance.md), [SkillValidateDAKContent](Requirements-SGAuthoring.Skills.ValidateDAKContent.md) and [SkillValidateL3Functionality](Requirements-SGAuthoring.Skills.ValidateL3Functionality.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGRequirements.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGRequirements.csv), [Excel](StructureDefinition-SGRequirements.xlsx), [Schematron](StructureDefinition-SGRequirements.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGRequirements",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-implements",
    "valueUri" : "http://hl7.org/fhir/StructureDefinition/CanonicalResource"
  }],
  "url" : "http://smart.who.int/base/StructureDefinition/SGRequirements",
  "version" : "1.0.0",
  "name" : "SGRequirements",
  "title" : "SMART Guidelines Requirements",
  "status" : "draft",
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Smart Guidelines Requirements",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Requirements",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Requirements",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Requirements",
      "path" : "Requirements"
    },
    {
      "id" : "Requirements.extension",
      "path" : "Requirements.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Requirements.extension:task",
      "path" : "Requirements.extension",
      "sliceName" : "task",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGTask"]
      }]
    },
    {
      "id" : "Requirements.extension:satisfies",
      "path" : "Requirements.extension",
      "sliceName" : "satisfies",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/Satisfies"]
      }]
    },
    {
      "id" : "Requirements.extension:userstory",
      "path" : "Requirements.extension",
      "sliceName" : "userstory",
      "min" : 0,
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGUserStory"]
      }]
    },
    {
      "id" : "Requirements.name",
      "path" : "Requirements.name",
      "min" : 1
    },
    {
      "id" : "Requirements.title",
      "path" : "Requirements.title",
      "min" : 1
    },
    {
      "id" : "Requirements.status",
      "path" : "Requirements.status",
      "mustSupport" : true
    },
    {
      "id" : "Requirements.experimental",
      "path" : "Requirements.experimental",
      "min" : 1
    },
    {
      "id" : "Requirements.description",
      "path" : "Requirements.description",
      "min" : 1
    },
    {
      "id" : "Requirements.statement.label",
      "path" : "Requirements.statement.label",
      "min" : 1
    }]
  }
}

```
