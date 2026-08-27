# SUSHI Configuration Logical Model - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SUSHI Configuration Logical Model**

## Logical Model: SUSHI Configuration Logical Model 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SushiConfigLogicalModel | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:SushiConfigLogicalModel |

 
Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SushiConfigLogicalModel.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SushiConfigLogicalModel.csv), [Excel](StructureDefinition-SushiConfigLogicalModel.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SushiConfigLogicalModel",
  "url" : "http://smart.who.int/base/StructureDefinition/SushiConfigLogicalModel",
  "version" : "1.0.0",
  "name" : "SushiConfigLogicalModel",
  "title" : "SUSHI Configuration Logical Model",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/SushiConfigLogicalModel",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "SushiConfigLogicalModel",
      "path" : "SushiConfigLogicalModel",
      "short" : "SUSHI Configuration Logical Model",
      "definition" : "Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing."
    },
    {
      "id" : "SushiConfigLogicalModel.id",
      "path" : "SushiConfigLogicalModel.id",
      "short" : "IG Identifier",
      "definition" : "Unique identifier for the IG, should match DAK id (e.g., smart.who.int.trust)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.canonical",
      "path" : "SushiConfigLogicalModel.canonical",
      "short" : "Canonical URL",
      "definition" : "Canonical URL for the IG, should match DAK publicationUrl (e.g., http://smart.who.int/trust)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.name",
      "path" : "SushiConfigLogicalModel.name",
      "short" : "IG Name",
      "definition" : "Short name for the IG, should derive from DAK name (e.g., Trust)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.title",
      "path" : "SushiConfigLogicalModel.title",
      "short" : "IG Title",
      "definition" : "Full title of the IG, should match DAK title (e.g., WHO SMART Trust)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.description",
      "path" : "SushiConfigLogicalModel.description",
      "short" : "IG Description",
      "definition" : "Description of the IG, should match DAK description",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.version",
      "path" : "SushiConfigLogicalModel.version",
      "short" : "IG Version",
      "definition" : "Version of the IG, should match DAK version",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.status",
      "path" : "SushiConfigLogicalModel.status",
      "short" : "IG Status",
      "definition" : "Publication status of the IG",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://hl7.org/fhir/ValueSet/publication-status"
      }
    },
    {
      "id" : "SushiConfigLogicalModel.license",
      "path" : "SushiConfigLogicalModel.license",
      "short" : "License",
      "definition" : "License under which the IG is published, should match DAK license",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://hl7.org/fhir/ValueSet/spdx-license"
      }
    },
    {
      "id" : "SushiConfigLogicalModel.copyrightYear",
      "path" : "SushiConfigLogicalModel.copyrightYear",
      "short" : "Copyright Year",
      "definition" : "Year or year range for copyright, should match DAK",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.experimental",
      "path" : "SushiConfigLogicalModel.experimental",
      "short" : "Experimental",
      "definition" : "Whether this IG is experimental, should match DAK",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.releaseLabel",
      "path" : "SushiConfigLogicalModel.releaseLabel",
      "short" : "Release Label",
      "definition" : "Label for this release (e.g., ci-build, draft, ballot)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.publisher",
      "path" : "SushiConfigLogicalModel.publisher",
      "short" : "Publisher",
      "definition" : "Organization responsible for publishing the IG",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.publisher.name",
      "path" : "SushiConfigLogicalModel.publisher.name",
      "short" : "Publisher Name",
      "definition" : "Name of the publishing organization, should match DAK publisher name",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.publisher.url",
      "path" : "SushiConfigLogicalModel.publisher.url",
      "short" : "Publisher URL",
      "definition" : "URL of the publishing organization, should match DAK publisher URL",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.publisher.email",
      "path" : "SushiConfigLogicalModel.publisher.email",
      "short" : "Publisher Email",
      "definition" : "Contact email for the publisher",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.fhirVersion",
      "path" : "SushiConfigLogicalModel.fhirVersion",
      "short" : "FHIR Version",
      "definition" : "Version of FHIR this IG is built on",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://hl7.org/fhir/ValueSet/FHIR-version"
      }
    },
    {
      "id" : "SushiConfigLogicalModel.dependencies",
      "path" : "SushiConfigLogicalModel.dependencies",
      "short" : "Dependencies",
      "definition" : "Other IGs or packages this IG depends on",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.dependencies.id",
      "path" : "SushiConfigLogicalModel.dependencies.id",
      "short" : "Dependency Package ID",
      "definition" : "Package ID of the dependency",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.dependencies.version",
      "path" : "SushiConfigLogicalModel.dependencies.version",
      "short" : "Dependency Version",
      "definition" : "Version of the dependency",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.dependencies.reason",
      "path" : "SushiConfigLogicalModel.dependencies.reason",
      "short" : "Dependency Reason",
      "definition" : "Reason for this dependency",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.pages",
      "path" : "SushiConfigLogicalModel.pages",
      "short" : "Pages",
      "definition" : "Custom pages included in the IG",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.pages.filename",
      "path" : "SushiConfigLogicalModel.pages.filename",
      "short" : "Page Filename",
      "definition" : "Filename of the page (e.g., index.md)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.pages.title",
      "path" : "SushiConfigLogicalModel.pages.title",
      "short" : "Page Title",
      "definition" : "Title of the page",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.menu",
      "path" : "SushiConfigLogicalModel.menu",
      "short" : "Menu Structure",
      "definition" : "Navigation menu structure for the IG",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.menu.title",
      "path" : "SushiConfigLogicalModel.menu.title",
      "short" : "Menu Title",
      "definition" : "Title of the menu item",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.menu.url",
      "path" : "SushiConfigLogicalModel.menu.url",
      "short" : "Menu URL",
      "definition" : "URL of the menu item",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.menu.subItems",
      "path" : "SushiConfigLogicalModel.menu.subItems",
      "short" : "Sub Menu Items",
      "definition" : "Sub-menu items",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.menu.subItems.title",
      "path" : "SushiConfigLogicalModel.menu.subItems.title",
      "short" : "Sub-item Title",
      "definition" : "Title of the sub-menu item",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.menu.subItems.url",
      "path" : "SushiConfigLogicalModel.menu.subItems.url",
      "short" : "Sub-item URL",
      "definition" : "URL of the sub-menu item",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources",
      "path" : "SushiConfigLogicalModel.resources",
      "short" : "Resource Definitions",
      "definition" : "Explicit resource definitions for the IG",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources.reference",
      "path" : "SushiConfigLogicalModel.resources.reference",
      "short" : "Resource Reference",
      "definition" : "Reference to the resource (used as YAML key)",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources.name",
      "path" : "SushiConfigLogicalModel.resources.name",
      "short" : "Resource Name",
      "definition" : "Human-readable name for the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources.description",
      "path" : "SushiConfigLogicalModel.resources.description",
      "short" : "Resource Description",
      "definition" : "Description of the resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources.exampleBoolean",
      "path" : "SushiConfigLogicalModel.resources.exampleBoolean",
      "short" : "Is Example",
      "definition" : "Whether this resource is an example",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources.exampleCanonical",
      "path" : "SushiConfigLogicalModel.resources.exampleCanonical",
      "short" : "Example Canonical",
      "definition" : "Canonical URL this resource is an example of",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "canonical"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.resources.groupingId",
      "path" : "SushiConfigLogicalModel.resources.groupingId",
      "short" : "Grouping ID",
      "definition" : "ID of the group this resource belongs to",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.groups",
      "path" : "SushiConfigLogicalModel.groups",
      "short" : "Resource Groups",
      "definition" : "Logical groupings of resources in the IG",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.groups.id",
      "path" : "SushiConfigLogicalModel.groups.id",
      "short" : "Group ID",
      "definition" : "Identifier for the group",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.groups.name",
      "path" : "SushiConfigLogicalModel.groups.name",
      "short" : "Group Name",
      "definition" : "Human-readable name for the group",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.groups.description",
      "path" : "SushiConfigLogicalModel.groups.description",
      "short" : "Group Description",
      "definition" : "Description of the group",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.groups.resources",
      "path" : "SushiConfigLogicalModel.groups.resources",
      "short" : "Group Resources",
      "definition" : "List of resources in this group",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.global",
      "path" : "SushiConfigLogicalModel.global",
      "short" : "Global Profiles",
      "definition" : "Global profile assignments",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.global.type",
      "path" : "SushiConfigLogicalModel.global.type",
      "short" : "Resource Type",
      "definition" : "FHIR resource type",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.global.profile",
      "path" : "SushiConfigLogicalModel.global.profile",
      "short" : "Profile URL",
      "definition" : "URL of the profile to apply globally",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "canonical"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.meta",
      "path" : "SushiConfigLogicalModel.meta",
      "short" : "IG Metadata",
      "definition" : "Additional metadata for the IG",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.meta.profile",
      "path" : "SushiConfigLogicalModel.meta.profile",
      "short" : "Meta Profiles",
      "definition" : "Profiles this IG conforms to",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "canonical"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.contact",
      "path" : "SushiConfigLogicalModel.contact",
      "short" : "Contact Information",
      "definition" : "Contact details for this IG",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "ContactDetail"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.useContext",
      "path" : "SushiConfigLogicalModel.useContext",
      "short" : "Use Context",
      "definition" : "Context where this IG is intended to be used",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "UsageContext"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.jurisdiction",
      "path" : "SushiConfigLogicalModel.jurisdiction",
      "short" : "Jurisdiction",
      "definition" : "Jurisdictions where this IG applies",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "CodeableConcept"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.FSHOnly",
      "path" : "SushiConfigLogicalModel.FSHOnly",
      "short" : "FSH Only",
      "definition" : "Whether to export only FSH resources without IG content",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.applyExtensionMetadataToRoot",
      "path" : "SushiConfigLogicalModel.applyExtensionMetadataToRoot",
      "short" : "Apply Extension Metadata",
      "definition" : "Whether to apply extension metadata to root elements",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.instanceOptions",
      "path" : "SushiConfigLogicalModel.instanceOptions",
      "short" : "Instance Options",
      "definition" : "Configuration for instance processing",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.instanceOptions.setMetaProfile",
      "path" : "SushiConfigLogicalModel.instanceOptions.setMetaProfile",
      "short" : "Set Meta Profile",
      "definition" : "When to automatically set meta.profile",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    },
    {
      "id" : "SushiConfigLogicalModel.instanceOptions.setId",
      "path" : "SushiConfigLogicalModel.instanceOptions.setId",
      "short" : "Set ID",
      "definition" : "When to automatically set id",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    }]
  }
}

```
