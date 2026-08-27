# SMART Guidelines Transaction - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Transaction**

## Resource Profile: SMART Guidelines Transaction 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGTransaction | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:SGTransaction |

 
SMART Guidelines Transaction Definition 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGTransaction.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGTransaction.csv), [Excel](StructureDefinition-SGTransaction.xlsx), [Schematron](StructureDefinition-SGTransaction.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGTransaction",
  "url" : "http://smart.who.int/base/StructureDefinition/SGTransaction",
  "version" : "1.0.0",
  "name" : "SGTransaction",
  "status" : "draft",
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "SMART Guidelines Transaction Definition",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "objimpl",
    "uri" : "http://hl7.org/fhir/object-implementation",
    "name" : "Object Implementation Information"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "GraphDefinition",
  "baseDefinition" : "http://smart.who.int/base/StructureDefinition/SGGraphDefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "GraphDefinition",
      "path" : "GraphDefinition"
    },
    {
      "id" : "GraphDefinition.extension",
      "path" : "GraphDefinition.extension",
      "min" : 2
    },
    {
      "id" : "GraphDefinition.extension:node",
      "path" : "GraphDefinition.extension",
      "sliceName" : "node",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "nodeId"
        }],
        "rules" : "closed"
      },
      "min" : 2,
      "max" : "2"
    },
    {
      "id" : "GraphDefinition.extension:node/source",
      "path" : "GraphDefinition.extension",
      "sliceName" : "node/source",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.extension:node/source.extension",
      "path" : "GraphDefinition.extension.extension",
      "min" : 3
    },
    {
      "id" : "GraphDefinition.extension:node/source.extension:nodeId",
      "path" : "GraphDefinition.extension.extension",
      "sliceName" : "nodeId"
    },
    {
      "id" : "GraphDefinition.extension:node/source.extension:nodeId.value[x]",
      "path" : "GraphDefinition.extension.extension.value[x]",
      "patternId" : "source"
    },
    {
      "id" : "GraphDefinition.extension:node/source.extension:type",
      "path" : "GraphDefinition.extension.extension",
      "sliceName" : "type"
    },
    {
      "id" : "GraphDefinition.extension:node/source.extension:type.value[x]",
      "path" : "GraphDefinition.extension.extension.value[x]",
      "patternCode" : "ActorDefinition"
    },
    {
      "id" : "GraphDefinition.extension:node/source.extension:actor",
      "path" : "GraphDefinition.extension.extension",
      "sliceName" : "actor",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGActorExt"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.extension:node/target",
      "path" : "GraphDefinition.extension",
      "sliceName" : "node/target",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.extension:node/target.extension",
      "path" : "GraphDefinition.extension.extension",
      "min" : 3
    },
    {
      "id" : "GraphDefinition.extension:node/target.extension:nodeId",
      "path" : "GraphDefinition.extension.extension",
      "sliceName" : "nodeId"
    },
    {
      "id" : "GraphDefinition.extension:node/target.extension:nodeId.value[x]",
      "path" : "GraphDefinition.extension.extension.value[x]",
      "patternId" : "target"
    },
    {
      "id" : "GraphDefinition.extension:node/target.extension:type",
      "path" : "GraphDefinition.extension.extension",
      "sliceName" : "type"
    },
    {
      "id" : "GraphDefinition.extension:node/target.extension:type.value[x]",
      "path" : "GraphDefinition.extension.extension.value[x]",
      "patternCode" : "ActorDefinition"
    },
    {
      "id" : "GraphDefinition.extension:node/target.extension:actor",
      "path" : "GraphDefinition.extension.extension",
      "sliceName" : "actor",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGActorExt"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link",
      "path" : "GraphDefinition.link",
      "max" : "1"
    },
    {
      "id" : "GraphDefinition.link.extension",
      "path" : "GraphDefinition.link.extension",
      "min" : 7
    },
    {
      "id" : "GraphDefinition.link.extension:sourceId",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "sourceId"
    },
    {
      "id" : "GraphDefinition.link.extension:sourceId.value[x]",
      "path" : "GraphDefinition.link.extension.value[x]",
      "patternId" : "source"
    },
    {
      "id" : "GraphDefinition.link.extension:targetId",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "targetId"
    },
    {
      "id" : "GraphDefinition.link.extension:targetId.value[x]",
      "path" : "GraphDefinition.link.extension.value[x]",
      "patternId" : "target"
    },
    {
      "id" : "GraphDefinition.link.extension:requestTrigger",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "requestTrigger",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:requestTrigger.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:requestTrigger.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "request-trigger"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:requestSemantics",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "requestSemantics",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:requestSemantics.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:requestSemantics.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "request-semantics"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:requestActions",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "requestActions",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:requestActions.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:requestActions.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "request-actions"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:responseTrigger",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "responseTrigger",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:responseTrigger.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:responseTrigger.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "response-trigger"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:responseSemantics",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "responseSemantics",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:responseSemantics.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:responseSemantics.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "response-semantics"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:responseActions",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "responseActions",
      "min" : 1,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:responseActions.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:responseActions.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "response-actions"
      }
    },
    {
      "id" : "GraphDefinition.link.extension:securityConsiderations",
      "path" : "GraphDefinition.link.extension",
      "sliceName" : "securityConsiderations",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://smart.who.int/base/StructureDefinition/SGDocumentation"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "GraphDefinition.link.extension:securityConsiderations.extension:code",
      "path" : "GraphDefinition.link.extension.extension",
      "sliceName" : "code"
    },
    {
      "id" : "GraphDefinition.link.extension:securityConsiderations.extension:code.value[x]",
      "path" : "GraphDefinition.link.extension.extension.value[x]",
      "patternCoding" : {
        "system" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
        "code" : "security-considerations"
      }
    }]
  }
}

```
