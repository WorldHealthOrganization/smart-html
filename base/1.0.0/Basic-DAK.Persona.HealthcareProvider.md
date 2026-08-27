# Resource DAK.Persona.HealthcareProvider



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "DAK.Persona.HealthcareProvider",
  "extension" : [{
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
    "valueUri" : "http://smart.who.int/base/ActorDefinition/DAK.Persona.HealthcareProvider"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
    "valueString" : "HealthcareProvider"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
    "valueString" : "Healthcare Provider"
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
    "valueMarkdown" : "A member of the health workforce who delivers health interventions. This group\nhas also been described as 'health workers' or 'healthcare workers'.\n\nHealthcare providers use DHIs to:\n- Identify and register persons for health services (2.1)\n- Manage person-centred health records (2.2)\n- Receive clinical decision support prompts and checklists (2.3)\n- Conduct telemedicine consultations and remote monitoring (2.4)\n- Communicate with supervisors, peers, and receive AI-assisted content (2.5)\n- Coordinate referrals and emergency transport (2.6)\n- Schedule and plan their clinical activities (2.7)\n- Access training content and assessments (2.8)\n- Manage prescriptions and medication adherence (2.9)\n- Order and receive laboratory and diagnostic results (2.10)\n- Verify health coverage and receive payments from individuals (2.11)\n\n**ISCO-08**: 2211 (Generalist medical practitioners), 2212 (Specialist medical\npractitioners), 2221 (Nursing professionals), 2222 (Midwifery professionals),\n3211 (Medical imaging and therapeutic equipment technicians), 3212 (Medical\nand pathology laboratory technicians), 3213 (Pharmaceutical technicians and\nassistants), 3221 (Nursing associate professionals), 3222 (Midwifery associate\nprofessionals), 3255 (Community health workers).\n\n**Examples**: Physician, nurse, midwife, clinical officer, pharmacist,\nlaboratory technician, dentist, allied health professional."
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.jurisdiction"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.type",
    "valueCode" : "person"
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
