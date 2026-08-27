# Resource SGAuthoring.Skills.AuthorTestCases



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Skills.AuthorTestCases",
  "meta" : {
    "profile" : ["http://smart.who.int/base/StructureDefinition/SGRequirements"]
  },
  "extension" : [{
    "url" : "http://smart.who.int/base/StructureDefinition/SGTask",
    "valueCoding" : {
      "system" : "http://smart.who.int/base/CodeSystem/SGTasks",
      "code" : "userTask",
      "display" : "User Task"
    }
  },
  {
    "url" : "http://smart.who.int/base/StructureDefinition/SGTask",
    "valueCoding" : {
      "system" : "http://smart.who.int/base/CodeSystem/SGTasks",
      "code" : "userTask",
      "display" : "User Task"
    }
  },
  {
    "url" : "http://smart.who.int/base/StructureDefinition/SGTask",
    "valueCoding" : {
      "system" : "http://smart.who.int/base/CodeSystem/SGTasks",
      "code" : "userTask",
      "display" : "User Task"
    }
  },
  {
    "url" : "http://smart.who.int/base/StructureDefinition/SGTask",
    "valueCoding" : {
      "system" : "http://smart.who.int/base/CodeSystem/SGTasks",
      "code" : "scriptTask",
      "display" : "Script Task"
    }
  },
  {
    "extension" : [{
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "create TestPlan, TestScript, and example instances for validation"
    },
    {
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "L3 artifacts are validated against defined acceptance criteria with reproducible tests"
    }],
    "url" : "http://smart.who.int/base/StructureDefinition/SGUserStory"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.url",
    "valueUri" : "http://smart.who.int/base/Requirements/SGAuthoring.Skills.AuthorTestCases"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.name",
    "valueString" : "SkillAuthorTestCases"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.title",
    "valueString" : "Can author test cases"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.status",
    "valueCode" : "draft"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.experimental",
    "valueBoolean" : true
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.date",
    "valueDateTime" : "2026-08-27T08:31:36+00:00"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.publisher",
    "valueString" : "WHO"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.contact",
    "valueContactDetail" : {
      "name" : "WHO",
      "telecom" : [{
        "system" : "url",
        "value" : "http://who.int"
      }]
    }
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.description",
    "valueMarkdown" : "Capability to create TestPlan, TestScript, and example instances for validation of L3 artifacts."
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.jurisdiction"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.actor",
    "valueCanonical" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.FHIRModeller"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TEST-01"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Create TestPlan resources"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can create FHIR TestPlan resources defining test scope and acceptance criteria."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TEST-02"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Create TestScript resources"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHOULD"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can create FHIR TestScript resources for automated validation."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TEST-03"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Create example instances"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can create example resource instances for each non-abstract profile in each UN language."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TEST-04"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Create test data"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHOULD"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can create test data or Synthea scripts for validating CQL execution and measure calculation."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://hl7.org/fhir/fhir-types",
      "code" : "Requirements"
    }]
  }
}

```
