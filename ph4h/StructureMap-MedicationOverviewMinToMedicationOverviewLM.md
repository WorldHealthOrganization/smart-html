# MedicationOverviewMinToMedicationOverviewLM - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **MedicationOverviewMinToMedicationOverviewLM**

## StructureMap: MedicationOverviewMinToMedicationOverviewLM 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureMap/MedicationOverviewMinToMedicationOverviewLM | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:MedicationOverviewMinToMedicationOverviewLM |



## Resource Content

```json
{
  "resourceType" : "StructureMap",
  "id" : "MedicationOverviewMinToMedicationOverviewLM",
  "url" : "http://smart.who.int/ph4h/StructureMap/MedicationOverviewMinToMedicationOverviewLM",
  "version" : "0.9.9",
  "name" : "MedicationOverviewMinToMedicationOverviewLM",
  "status" : "draft",
  "date" : "2026-07-09T08:39:10+00:00",
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
    "url" : "http://smart.who.int/ph4h/StructureDefinition/MedicationTreatmentLineMin",
    "mode" : "source",
    "alias" : "MedicationTreatmentLineMin"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationOverviewLM",
    "mode" : "target",
    "alias" : "MedicationOverviewLM"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/PatientLM",
    "mode" : "target",
    "alias" : "PatientLM"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationTreatmentLineLM",
    "mode" : "target",
    "alias" : "MedicationTreatmentLineLM"
  }],
  "group" : [{
    "name" : "MedicationOverviewMinToMedicationOverviewLM",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nTop-level group: 1 patient + 0..* medication treatment lines\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "MedicationOverviewMin",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "MedicationOverviewLM",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "patient",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "patient",
        "variable" : "patient"
      }],
      "dependent" : [{
        "name" : "MedicationOverviewMinToPatientLM",
        "variable" : ["src", "patient"]
      }]
    },
    {
      "name" : "treatmentLine",
      "source" : [{
        "context" : "src",
        "element" : "m",
        "variable" : "line"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "medicationTreatmentLine",
        "variable" : "tline"
      }],
      "dependent" : [{
        "name" : "MedicationTreatmentLineMinToMedicationTreatmentLineLM",
        "variable" : ["line", "tline"]
      }]
    }]
  },
  {
    "name" : "MedicationOverviewMinToPatientLM",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nMedicationOverviewMin demographic fields -> PatientLM\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "MedicationOverviewMin",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "PatientLM",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "name",
      "source" : [{
        "context" : "src",
        "element" : "n",
        "variable" : "n"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "hn",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "HumanName"
        }]
      },
      {
        "context" : "hn",
        "contextType" : "variable",
        "element" : "text",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "n"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "name",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "hn"
        }]
      }]
    },
    {
      "name" : "dateOfBirth",
      "source" : [{
        "context" : "src",
        "element" : "dob",
        "variable" : "dob"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "dateOfBirth",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "dob"
        }]
      }]
    },
    {
      "name" : "gender",
      "source" : [{
        "context" : "src",
        "element" : "s",
        "variable" : "s"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "gc",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Coding"
        }]
      },
      {
        "context" : "gc",
        "contextType" : "variable",
        "element" : "system",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://hl7.org/fhir/administrative-gender"
        }]
      },
      {
        "context" : "gc",
        "contextType" : "variable",
        "element" : "code",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "s"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "g",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "CodeableConcept"
        }]
      },
      {
        "context" : "g",
        "contextType" : "variable",
        "element" : "coding",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "gc"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "gender",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "g"
        }]
      }]
    },
    {
      "name" : "identifier",
      "source" : [{
        "context" : "src",
        "element" : "id",
        "variable" : "id"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ident",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Identifier"
        }]
      }],
      "rule" : [{
        "name" : "identifierValue",
        "source" : [{
          "context" : "id"
        }],
        "target" : [{
          "context" : "ident",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "id"
          }]
        }]
      },
      {
        "name" : "identifierAssign",
        "source" : [{
          "context" : "id"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "identifier",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ident"
          }]
        }]
      }]
    }]
  },
  {
    "name" : "MedicationTreatmentLineMinToMedicationTreatmentLineLM",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nOne MedicationTreatmentLineMin -> one MedicationTreatmentLineLM\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "MedicationTreatmentLineMin",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "MedicationTreatmentLineLM",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "status",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "status",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "active"
        }]
      }]
    },
    {
      "name" : "medication",
      "source" : [{
        "context" : "src",
        "element" : "m",
        "variable" : "med"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "c",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Coding"
        }]
      },
      {
        "context" : "c",
        "contextType" : "variable",
        "element" : "system",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://snomed.info/sct"
        }]
      },
      {
        "context" : "c",
        "contextType" : "variable",
        "element" : "code",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "med"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "cc",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "CodeableConcept"
        }]
      },
      {
        "context" : "cc",
        "contextType" : "variable",
        "element" : "coding",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "c"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "medication",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "cc"
        }]
      }]
    },
    {
      "name" : "effectivePeriod",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ep",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Period"
        }]
      }],
      "rule" : [{
        "name" : "effStart",
        "source" : [{
          "context" : "src",
          "element" : "es",
          "variable" : "es"
        }],
        "target" : [{
          "context" : "ep",
          "contextType" : "variable",
          "element" : "start",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "es"
          }]
        }]
      },
      {
        "name" : "effEnd",
        "source" : [{
          "context" : "src",
          "element" : "ee",
          "variable" : "ee"
        }],
        "target" : [{
          "context" : "ep",
          "contextType" : "variable",
          "element" : "end",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ee"
          }]
        }]
      },
      {
        "name" : "effAssign",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "effectivePeriod",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ep"
          }]
        }]
      }]
    },
    {
      "name" : "dateAsserted",
      "source" : [{
        "context" : "src",
        "element" : "da",
        "variable" : "da"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "recordingMetadata",
        "variable" : "rm"
      }],
      "rule" : [{
        "name" : "recordedTime",
        "source" : [{
          "context" : "da"
        }],
        "target" : [{
          "context" : "rm",
          "contextType" : "variable",
          "element" : "recordedTime",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "da"
          }]
        }]
      }]
    },
    {
      "name" : "dosage",
      "source" : [{
        "context" : "src",
        "element" : "d",
        "variable" : "d"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "preparationInstructions",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "d"
        }]
      }]
    },
    {
      "name" : "reason",
      "source" : [{
        "context" : "src",
        "element" : "r",
        "variable" : "r"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "indicationText",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "r"
        }]
      }]
    },
    {
      "name" : "adherence",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "tsc",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Coding"
        }]
      },
      {
        "context" : "tsc",
        "contextType" : "variable",
        "element" : "system",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://hl7.org/fhir/CodeSystem/medication-statement-status"
        }]
      },
      {
        "context" : "tsc",
        "contextType" : "variable",
        "element" : "code",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "active"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "ts",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "CodeableConcept"
        }]
      },
      {
        "context" : "ts",
        "contextType" : "variable",
        "element" : "coding",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "tsc"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "treatmentStatus",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ts"
        }]
      }],
      "rule" : [{
        "name" : "adherenceValue",
        "source" : [{
          "context" : "src",
          "element" : "a",
          "variable" : "a"
        }],
        "target" : [{
          "context" : "tsc",
          "contextType" : "variable",
          "element" : "code",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "a"
          }]
        }]
      }]
    }]
  }]
}

```
