# Resource SGAuthoring.Persona.QCReviewer



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Persona.QCReviewer",
  "extension" : [{
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
    "valueUri" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.QCReviewer"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
    "valueString" : "QCReviewer"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
    "valueString" : "Quality Control Reviewer"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.status",
    "valueCode" : "draft"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.experimental",
    "valueBoolean" : true
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.date",
    "valueDateTime" : "2026-08-27T08:35:55+00:00"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.publisher",
    "valueString" : "WHO"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.contact",
    "valueContactDetail" : {
      "name" : "WHO",
      "telecom" : [{
        "system" : "url",
        "value" : "http://who.int"
      }]
    }
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.description",
    "valueMarkdown" : "A quality assurance specialist responsible for reviewing SMART Guidelines\nImplementation Guides for publication readiness. QC Reviewers use the\npublication checklist across L1-L4 layers, interpret QA validation reports,\nand verify artifact conformance and cross-component consistency.\n\nKey activities:\n- Run and interpret IG Publisher QA reports (qa.html)\n- Review publication checklist across L1, L2, L3, L4, and Global sections\n- Verify conformance to Shareable, Publishable, Computable, Executable profiles\n- Validate StructureMap extraction produces expected output\n- Verify CQL execution and measure calculations\n- Check cross-component consistency (personas, data elements, processes)\n- Validate all artifacts have required title, description, and mappings\n- Confirm naming conventions and reference resolution\n- Review change log completeness and versioning compliance\n\n**Source**: IG Starter Kit, QA Check page, Checklist page, Validating IG page"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.jurisdiction"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.type",
    "valueCode" : "person"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://hl7.org/fhir/fhir-types",
      "code" : "ActorDefinition"
    }]
  }
}

```
