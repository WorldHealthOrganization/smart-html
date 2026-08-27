# Resource SGAuthoring.Skills.AuthorConceptMaps



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Skills.AuthorConceptMaps",
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
      "valueString" : "create FHIR ConceptMap resources for cross-terminology mappings"
    },
    {
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "cross-terminology relationships are formally defined enabling semantic interoperability"
    }],
    "url" : "http://smart.who.int/base/StructureDefinition/SGUserStory"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.url",
    "valueUri" : "http://smart.who.int/base/Requirements/SGAuthoring.Skills.AuthorConceptMaps"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.name",
    "valueString" : "SkillAuthorConceptMaps"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.title",
    "valueString" : "Can author concept maps"
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
    "valueMarkdown" : "Capability to create FHIR ConceptMap resources for cross-terminology mappings."
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
      "valueId" : "CM-01"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Create ConceptMap resources"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can create FHIR ConceptMap resources defining mappings between source and target code systems."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "CM-02"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Define equivalence relationships"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can define appropriate equivalence relationships (equivalent, wider, narrower, etc.) between mapped concepts."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "CM-03"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Write FSH for ConceptMaps"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can author ConceptMap definitions using FHIR Shorthand (FSH) syntax."
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
