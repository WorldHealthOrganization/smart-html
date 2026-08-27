# Program Indicator (DAK) - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Program Indicator (DAK)**

## Logical Model: Program Indicator (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/ProgramIndicator | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:ProgramIndicator |

 
Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting. 

**Usages:**

* Use this Logical Model: [Program Indicator Source](StructureDefinition-ProgramIndicatorSource.md)
* Refer to this Logical Model: [Program Indicator Source](StructureDefinition-ProgramIndicatorSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-ProgramIndicator.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ProgramIndicator.csv), [Excel](StructureDefinition-ProgramIndicator.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ProgramIndicator",
  "url" : "http://smart.who.int/base/StructureDefinition/ProgramIndicator",
  "version" : "1.0.0",
  "name" : "ProgramIndicator",
  "title" : "Program Indicator (DAK)",
  "status" : "active",
  "date" : "2026-08-27T08:35:55+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/ProgramIndicator",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "ProgramIndicator",
      "path" : "ProgramIndicator",
      "short" : "Program Indicator (DAK)",
      "definition" : "Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting."
    },
    {
      "id" : "ProgramIndicator.id",
      "path" : "ProgramIndicator.id",
      "short" : "Indicator ID",
      "definition" : "Identifier for the program indicator",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "ProgramIndicator.description[x]",
      "path" : "ProgramIndicator.description[x]",
      "short" : "Description",
      "definition" : "Description of the program indicator - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      },
      {
        "code" : "uri"
      }]
    },
    {
      "id" : "ProgramIndicator.name",
      "path" : "ProgramIndicator.name",
      "short" : "Name",
      "definition" : "Name of the indicator",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "ProgramIndicator.definition",
      "path" : "ProgramIndicator.definition",
      "short" : "Definition",
      "definition" : "Definition of what the indicator measures",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "ProgramIndicator.numerator",
      "path" : "ProgramIndicator.numerator",
      "short" : "Numerator",
      "definition" : "Description of the numerator calculation",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "ProgramIndicator.denominator",
      "path" : "ProgramIndicator.denominator",
      "short" : "Denominator",
      "definition" : "Description of the denominator calculation",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "ProgramIndicator.disaggregation",
      "path" : "ProgramIndicator.disaggregation",
      "short" : "Disaggregation",
      "definition" : "Description of how the indicator should be disaggregated",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "ProgramIndicator.references",
      "path" : "ProgramIndicator.references",
      "short" : "References",
      "definition" : "References to Health Intervention IDs providing additional context",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "id"
      }]
    }]
  }
}

```
