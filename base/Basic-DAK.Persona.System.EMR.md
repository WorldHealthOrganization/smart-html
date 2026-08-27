# Resource DAK.Persona.System.EMR



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "DAK.Persona.System.EMR",
  "extension" : [{
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
    "valueUri" : "http://smart.who.int/base/ActorDefinition/DAK.Persona.System.EMR"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
    "valueString" : "ElectronicMedicalRecord"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
    "valueString" : "Electronic Medical Record (EMR) System"
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
    "valueMarkdown" : "A secure, digital system that holds information about people's health and\nclinical care managed by healthcare providers. Also referred to as an\nElectronic Health Record (EHR).\n\nThe EMR system supports DHIs including:\n- Longitudinal tracking of person's health status and services (2.2.1)\n- Management of structured clinical records (2.2.2)\n- Management of unstructured clinical records such as notes and images (2.2.3)\n- Clinical decision support prompts and checklists (2.3)\n- Person identification and registration (2.1)\n- Prescription and medication management (2.9)\n- Laboratory results reception (2.10.1)\n- Routine health indicator data collection (2.2.4)\n\n**Services and Application Type**: A5 — Electronic medical record systems\n\n**Functional areas**: Clinical decision support, record management,\nperson registration, appointment scheduling, referral tracking."
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.jurisdiction"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.type",
    "valueCode" : "system"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.documentation",
    "valueMarkdown" : "https://www.who.int/publications/i/item/9789240081949"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://hl7.org/fhir/fhir-types",
      "code" : "ActorDefinition"
    }]
  }
}

```
