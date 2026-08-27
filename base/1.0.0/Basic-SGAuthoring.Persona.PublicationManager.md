# Resource SGAuthoring.Persona.PublicationManager



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "SGAuthoring.Persona.PublicationManager",
  "extension" : [{
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
    "valueUri" : "http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.PublicationManager"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
    "valueString" : "1.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
    "valueString" : "PublicationManager"
  },
  {
    "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
    "valueString" : "Publication Manager"
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
    "valueMarkdown" : "A specialist responsible for managing the FHIR Implementation Guide\nconfiguration, build process, versioning, and release publication workflow.\nPublication Managers ensure IGs are correctly configured, built, and\npublished to smart.who.int following the established publication process.\n\nKey activities:\n- Set up IG repositories from smart-ig-empty template\n- Configure sushi-config.yaml (canonical URL, package ID, dependencies)\n- Enable GitHub Pages and CI build workflows\n- Run FHIR IG Publisher builds and verify output\n- Manage semantic versioning (major.minor.patch)\n- Create publication-request.json for releases\n- Create release branches, tags, and GitHub releases\n- Monitor automated publication workflows\n- Coordinate with WHO SMART Guidelines team for smart.who.int updates\n- Manage cross-IG governance for shared artifacts\n- Reset main branch to draft status after publication\n\n**Source**: IG Starter Kit, IG Setup, IG Publication, and IG Configuration pages"
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
