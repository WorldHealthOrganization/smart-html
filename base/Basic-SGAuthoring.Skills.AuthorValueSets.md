# Resource SGAuthoring.Skills.AuthorValueSets



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Skills.AuthorValueSets",
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
    "extension" : [{
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "create and maintain FHIR ValueSet resources"
    },
    {
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "value sets are properly defined and conform to executable profiles for implementation"
    }],
    "url" : "http://smart.who.int/base/StructureDefinition/SGUserStory"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.url",
    "valueUri" : "http://smart.who.int/base/Requirements/SGAuthoring.Skills.AuthorValueSets"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.name",
    "valueString" : "SkillAuthorValueSets"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.title",
    "valueString" : "Can author value sets"
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
    "valueDateTime" : "2026-08-27T08:35:55+00:00"
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
    "valueMarkdown" : "Capability to create and maintain FHIR ValueSet resources with appropriate terminology bindings."
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.jurisdiction"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.actor",
    "valueCanonical" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.Terminologist"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "VS-01"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Create ValueSet resources"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can create FHIR ValueSet resources with appropriate include/exclude criteria."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "VS-02"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Conform to Executable profile"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can ensure ValueSets conform to the CRMI Executable profile where required."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "VS-03"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Write FSH for ValueSets"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can author ValueSet definitions using FHIR Shorthand (FSH) syntax."
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
