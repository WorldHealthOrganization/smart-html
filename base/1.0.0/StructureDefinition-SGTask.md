# SGTask - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SGTask**

## Extension: SGTask 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGTask | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGTask |

Extension to reference SMART Guidelines task type

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [SMART Guidelines Requirements](StructureDefinition-SGRequirements.md)
* Examples for this Extension: [SkillAuthorActorDefinitions](Requirements-SGAuthoring.Skills.AuthorActorDefinitions.md), [SkillAuthorBusinessProcesses](Requirements-SGAuthoring.Skills.AuthorBusinessProcesses.md), [SkillAuthorCQL](Requirements-SGAuthoring.Skills.AuthorCQL.md), [SkillAuthorCodeSystems](Requirements-SGAuthoring.Skills.AuthorCodeSystems.md)... Show 37 more, [SkillAuthorConceptMaps](Requirements-SGAuthoring.Skills.AuthorConceptMaps.md), [SkillAuthorDataDictionary](Requirements-SGAuthoring.Skills.AuthorDataDictionary.md), [SkillAuthorDecisionLogic](Requirements-SGAuthoring.Skills.AuthorDecisionLogic.md), [SkillAuthorExampleScenarios](Requirements-SGAuthoring.Skills.AuthorExampleScenarios.md), [SkillAuthorFHIRProfiles](Requirements-SGAuthoring.Skills.AuthorFHIRProfiles.md), [SkillAuthorFHIRRequirements](Requirements-SGAuthoring.Skills.AuthorFHIRRequirements.md), [SkillAuthorFunctionalRequirements](Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.md), [SkillAuthorIndicators](Requirements-SGAuthoring.Skills.AuthorIndicators.md), [SkillAuthorLogicalModels](Requirements-SGAuthoring.Skills.AuthorLogicalModels.md), [SkillAuthorMeasures](Requirements-SGAuthoring.Skills.AuthorMeasures.md), [SkillAuthorPersonas](Requirements-SGAuthoring.Skills.AuthorPersonas.md), [SkillAuthorPlanDefinitions](Requirements-SGAuthoring.Skills.AuthorPlanDefinitions.md), [SkillAuthorQuestionnaires](Requirements-SGAuthoring.Skills.AuthorQuestionnaires.md), [SkillAuthorSchedulingLogic](Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.md), [SkillAuthorStructureMaps](Requirements-SGAuthoring.Skills.AuthorStructureMaps.md), [SkillAuthorTestCases](Requirements-SGAuthoring.Skills.AuthorTestCases.md), [SkillAuthorUserScenarios](Requirements-SGAuthoring.Skills.AuthorUserScenarios.md), [SkillAuthorValueSets](Requirements-SGAuthoring.Skills.AuthorValueSets.md), [SkillBuildIG](Requirements-SGAuthoring.Skills.BuildIG.md), [SkillConfigureIG](Requirements-SGAuthoring.Skills.ConfigureIG.md), [SkillInterpretClinicalRecommendations](Requirements-SGAuthoring.Skills.InterpretClinicalRecommendations.md), [SkillManageGovernance](Requirements-SGAuthoring.Skills.ManageGovernance.md), [SkillManageReleases](Requirements-SGAuthoring.Skills.ManageReleases.md), [SkillManageStakeholders](Requirements-SGAuthoring.Skills.ManageStakeholders.md), [SkillMapConcepts](Requirements-SGAuthoring.Skills.MapConcepts.md), [SkillPlanIterations](Requirements-SGAuthoring.Skills.PlanIterations.md), [SkillReviewAndApproveContent](Requirements-SGAuthoring.Skills.ReviewAndApproveContent.md), [SkillReviewChecklist](Requirements-SGAuthoring.Skills.ReviewChecklist.md), [SkillReviewL1Guidelines](Requirements-SGAuthoring.Skills.ReviewL1Guidelines.md), [SkillReviewTerminology](Requirements-SGAuthoring.Skills.ReviewTerminology.md), [SkillReviewTranslations](Requirements-SGAuthoring.Skills.ReviewTranslations.md), [SkillRunQAChecks](Requirements-SGAuthoring.Skills.RunQAChecks.md), [SkillScopeDAK](Requirements-SGAuthoring.Skills.ScopeDAK.md), [SkillTranslateContent](Requirements-SGAuthoring.Skills.TranslateContent.md), [SkillValidateArtifactConformance](Requirements-SGAuthoring.Skills.ValidateArtifactConformance.md), [SkillValidateDAKContent](Requirements-SGAuthoring.Skills.ValidateDAKContent.md) and [SkillValidateL3Functionality](Requirements-SGAuthoring.Skills.ValidateL3Functionality.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGTask.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGTask.csv), [Excel](StructureDefinition-SGTask.xlsx), [Schematron](StructureDefinition-SGTask.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGTask",
  "url" : "http://smart.who.int/base/StructureDefinition/SGTask",
  "version" : "1.0.0",
  "name" : "SGTask",
  "status" : "active",
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Extension to reference SMART Guidelines task type",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "Element"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "definition" : "Extension to reference SMART Guidelines task type"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/SGTask"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "slicing" : {
        "discriminator" : [{
          "type" : "type",
          "path" : "$this"
        }],
        "ordered" : false,
        "rules" : "open"
      },
      "min" : 1
    },
    {
      "id" : "Extension.value[x]:valueCoding",
      "path" : "Extension.value[x]",
      "sliceName" : "valueCoding",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Coding"
      }]
    },
    {
      "id" : "Extension.value[x]:valueCoding.system",
      "path" : "Extension.value[x].system",
      "min" : 1,
      "fixedUri" : "http://smart.who.int/base/CodeSystem/SGTasks",
      "mustSupport" : true
    },
    {
      "id" : "Extension.value[x]:valueCoding.code",
      "path" : "Extension.value[x].code",
      "min" : 1,
      "mustSupport" : true
    }]
  }
}

```
