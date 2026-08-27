# Resource SGAuthoring.Skills.TranslateContent



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Skills.TranslateContent",
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
      "code" : "userTask",
      "display" : "User Task"
    }
  },
  {
    "extension" : [{
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "translate IG content across UN languages"
    },
    {
      "url" : "http://smart.who.int/base/StructureDefinition/SGString",
      "valueString" : "SMART Guidelines are accessible to implementers in all UN languages"
    }],
    "url" : "http://smart.who.int/base/StructureDefinition/SGUserStory"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.url",
    "valueUri" : "http://smart.who.int/base/Requirements/SGAuthoring.Skills.TranslateContent"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.name",
    "valueString" : "SkillTranslateContent"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.title",
    "valueString" : "Can translate content"
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
    "valueMarkdown" : "Capability to translate IG content across UN languages."
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.jurisdiction"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.actor",
    "valueCanonical" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.Translator"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TRANS-01"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Translate narrative pages"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can translate IG narrative page content (markdown/HTML) to target UN languages."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TRANS-02"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Translate resource metadata"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can translate FHIR resource display names, titles, and descriptions."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TRANS-03"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Manage translation files"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHALL"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can manage .pot/.po translation template files and the translation extraction/registration workflow."
    }],
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement"
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.key",
      "valueId" : "TRANS-04"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.label",
      "valueString" : "Coordinate domain terminology"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.conformance",
      "valueCode" : "SHOULD"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Requirements.statement.requirement",
      "valueMarkdown" : "Can coordinate with clinical SMEs for domain-specific terminology in translations."
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
