# Resource SGAuthoring.Persona.FHIRModeller



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Persona.FHIRModeller",
  "extension" : [{
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
    "valueUri" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.FHIRModeller"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
    "valueString" : "FHIRModeller"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
    "valueString" : "FHIR Modeller"
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
    "valueMarkdown" : "An L3 author who creates machine-readable FHIR artifacts from L2 DAK\nspecifications. FHIR Modellers use FSH (FHIR Shorthand), SUSHI, and\nthe IG Publisher toolchain to produce conformant Implementation Guides.\n\nKey activities:\n- Verify L2 input availability and consistency\n- Author FHIR Logical Models from L2 data dictionaries\n- Create FHIR Profiles (StructureDefinitions)\n- Author FHIR Questionnaires from L2 forms\n- Write CQL for decision logic, scheduling logic, and indicators\n- Create StructureMaps for data extraction\n- Author PlanDefinitions for business processes and decision tables\n- Create ActorDefinitions from L2 personas (reusing Commons repository)\n- Create ExampleScenario resources from L2 user scenarios\n- Author FHIR Measure resources from L2 indicators\n- Create FHIR Requirements resources\n- Develop test cases (TestPlan, TestScript, example instances)\n- Ensure all artifacts conform to CRMI Shareable/Publishable profiles\n\n**Source**: IG Starter Kit, L2-L3 Overview and all L3 authoring pages"
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
