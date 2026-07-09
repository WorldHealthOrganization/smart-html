# MedicationOverviewMinToMedicationOverviewBundle - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **MedicationOverviewMinToMedicationOverviewBundle**

## StructureMap: MedicationOverviewMinToMedicationOverviewBundle 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureMap/MedicationOverviewMinToMedicationOverviewBundle | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:MedicationOverviewMinToMedicationOverviewBundle |



## Resource Content

```json
{
  "resourceType" : "StructureMap",
  "id" : "MedicationOverviewMinToMedicationOverviewBundle",
  "url" : "http://smart.who.int/ph4h/StructureMap/MedicationOverviewMinToMedicationOverviewBundle",
  "version" : "0.9.9",
  "name" : "MedicationOverviewMinToMedicationOverviewBundle",
  "status" : "draft",
  "date" : "2026-07-09T08:34:46+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "structure" : [{
    "url" : "http://smart.who.int/ph4h/StructureDefinition/MedicationOverviewMin",
    "mode" : "source",
    "alias" : "MedicationOverviewMin"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationOverview",
    "mode" : "target",
    "alias" : "MedicationOverviewBundle"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationOverviewLM",
    "mode" : "target",
    "alias" : "MedicationOverviewLM"
  }],
  "import" : ["http://smart.who.int/ph4h/StructureMap/MedicationOverviewMinToMedicationOverviewLM",
  "http://smart.who.int/ph4h/StructureMap/MedicationOverviewLMToMedicationOverviewBundle"],
  "group" : [{
    "name" : "MedicationOverviewMinToMedicationOverviewBundle",
    "typeMode" : "none",
    "input" : [{
      "name" : "src",
      "type" : "MedicationOverviewMin",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "MedicationOverviewBundle",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "chainMinToBundle",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "lm",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "MedicationOverviewLM"
        }]
      }],
      "rule" : [{
        "name" : "stage1MinToLM",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "context" : "lm",
          "contextType" : "variable"
        }],
        "dependent" : [{
          "name" : "MedicationOverviewMinToMedicationOverviewLM",
          "variable" : ["src", "lm"]
        }]
      },
      {
        "name" : "stage2LMToBundle",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable"
        }],
        "dependent" : [{
          "name" : "MedicationOverviewLMToMedicationOverviewBundle",
          "variable" : ["lm", "tgt"]
        }]
      }]
    }]
  }]
}

```
