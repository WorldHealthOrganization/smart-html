# Resource SGAuthoring.Persona.ContentReviewer



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Persona.ContentReviewer",
  "extension" : [{
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
    "valueUri" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.ContentReviewer"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
    "valueString" : "ContentReviewer"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
    "valueString" : "Content Reviewer / Approver"
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
    "valueDateTime" : "2026-08-27T08:31:36+00:00"
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
    "valueMarkdown" : "A designated reviewer responsible for approving SMART Guidelines content\nat key decision gates in the authoring lifecycle. Content Reviewers ensure\nthat DAK and IG content meets quality standards, accurately reflects WHO\nnormative guidance, and is ready to proceed to the next phase.\n\nContent Reviewers may be senior technical officers, programme leads, or\ndesignated governance committee members. They provide formal sign-off at\nphase transitions (L2→L3, draft→publication).\n\nKey activities:\n- Review and approve L2 DAK content before L3 authoring begins\n- Review and approve L3 IG content before publication\n- Assess whether content changes are breaking or non-breaking\n- Approve draft publications for stakeholder circulation\n- Provide final sign-off for release publication\n- Ensure content aligns with WHO guidelines governance policies\n- Participate in cross-programme content harmonization reviews\n\n**Source**: IG Starter Kit, Publication page (review process);\nDAK Authoring, Section 2.2 \"Validate DAK content with SMEs\""
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
