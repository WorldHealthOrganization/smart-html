# MedicationOverviewLMToMedicationOverviewBundle - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **MedicationOverviewLMToMedicationOverviewBundle**

## StructureMap: MedicationOverviewLMToMedicationOverviewBundle 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureMap/MedicationOverviewLMToMedicationOverviewBundle | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:MedicationOverviewLMToMedicationOverviewBundle |



## Resource Content

```json
{
  "resourceType" : "StructureMap",
  "id" : "MedicationOverviewLMToMedicationOverviewBundle",
  "url" : "http://smart.who.int/ph4h/StructureMap/MedicationOverviewLMToMedicationOverviewBundle",
  "version" : "0.9.9",
  "name" : "MedicationOverviewLMToMedicationOverviewBundle",
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
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationOverviewLM",
    "mode" : "source",
    "alias" : "MedicationOverviewLM"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/PatientLM",
    "mode" : "source",
    "alias" : "PatientLM"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationTreatmentLineLM",
    "mode" : "source",
    "alias" : "MedicationTreatmentLineLM"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/PractitionerLM",
    "mode" : "source",
    "alias" : "PractitionerLM"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationOverview",
    "mode" : "target",
    "alias" : "MedicationOverviewBundle"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationOverviewComposition",
    "mode" : "target",
    "alias" : "MedicationOverviewComposition"
  },
  {
    "url" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/MedicationTreatmentLine",
    "mode" : "target",
    "alias" : "MedicationTreatmentLine"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/Patient",
    "mode" : "target",
    "alias" : "Patient"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/Practitioner",
    "mode" : "target",
    "alias" : "Practitioner"
  }],
  "group" : [{
    "name" : "MedicationOverviewLMToMedicationOverviewBundle",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nTop-level group: assemble MedicationOverview Bundle (document)\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "MedicationOverviewLM",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "MedicationOverviewBundle",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "bundleType",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "type",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "document"
        }]
      }]
    },
    {
      "name" : "bundleTimestamp",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "timestamp",
        "transform" : "evaluate",
        "parameter" : [{
          "valueString" : "now()"
        }]
      }]
    },
    {
      "name" : "setEntries",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "bid",
        "transform" : "uuid"
      },
      {
        "contextType" : "variable",
        "variable" : "cid",
        "transform" : "uuid"
      },
      {
        "contextType" : "variable",
        "variable" : "pid",
        "transform" : "uuid"
      }],
      "rule" : [{
        "name" : "bundleIdentifier",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "identifier",
          "variable" : "id"
        },
        {
          "context" : "id",
          "contextType" : "variable",
          "element" : "system",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "urn:ietf:rfc:4122"
          }]
        },
        {
          "context" : "id",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "bid"
          }]
        }]
      },
      {
        "name" : "compositionEntry",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "entry",
          "variable" : "ce"
        },
        {
          "context" : "ce",
          "contextType" : "variable",
          "element" : "fullUrl",
          "transform" : "append",
          "parameter" : [{
            "valueString" : "urn:uuid:"
          },
          {
            "valueId" : "cid"
          }]
        },
        {
          "context" : "ce",
          "contextType" : "variable",
          "element" : "resource",
          "variable" : "comp",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "MedicationOverviewComposition"
          }]
        }],
        "rule" : [{
          "name" : "compositionContent",
          "source" : [{
            "context" : "src"
          }],
          "dependent" : [{
            "name" : "MedicationOverviewLMToComposition",
            "variable" : ["src", "comp", "pid", "tgt"]
          }]
        }]
      },
      {
        "name" : "patientEntry",
        "source" : [{
          "context" : "src",
          "element" : "patient",
          "variable" : "pref"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "entry",
          "variable" : "pe"
        },
        {
          "context" : "pe",
          "contextType" : "variable",
          "element" : "fullUrl",
          "transform" : "append",
          "parameter" : [{
            "valueString" : "urn:uuid:"
          },
          {
            "valueId" : "pid"
          }]
        },
        {
          "context" : "pe",
          "contextType" : "variable",
          "element" : "resource",
          "variable" : "pat",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Patient"
          }]
        }],
        "rule" : [{
          "name" : "patientContent",
          "source" : [{
            "context" : "pref"
          }],
          "dependent" : [{
            "name" : "PatientLMToPatient",
            "variable" : ["pref", "pat"]
          }]
        }]
      }]
    }]
  },
  {
    "name" : "MedicationOverviewLMToComposition",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nMedicationOverviewLM -> MedicationOverviewComposition\r\nReceives the Patient entry's UUID (pid) so subject can reference it.\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "MedicationOverviewLM",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "MedicationOverviewComposition",
      "mode" : "target"
    },
    {
      "name" : "pid",
      "mode" : "source"
    },
    {
      "name" : "bundle",
      "type" : "MedicationOverviewBundle",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "compStatus",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "status",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "final"
        }]
      }]
    },
    {
      "name" : "compType",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "cc",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Coding"
        }]
      },
      {
        "context" : "cc",
        "contextType" : "variable",
        "element" : "system",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://loinc.org"
        }]
      },
      {
        "context" : "cc",
        "contextType" : "variable",
        "element" : "code",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "56445-0"
        }]
      },
      {
        "context" : "cc",
        "contextType" : "variable",
        "element" : "display",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "Medication summary Document"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "ct",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "CodeableConcept"
        }]
      },
      {
        "context" : "ct",
        "contextType" : "variable",
        "element" : "coding",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "cc"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "type",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ct"
        }]
      }]
    },
    {
      "name" : "compSubject",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "subj",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Reference"
        }]
      },
      {
        "context" : "subj",
        "contextType" : "variable",
        "element" : "reference",
        "transform" : "append",
        "parameter" : [{
          "valueString" : "urn:uuid:"
        },
        {
          "valueId" : "pid"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "subject",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "subj"
        }]
      }]
    },
    {
      "name" : "compDate",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "date",
        "transform" : "evaluate",
        "parameter" : [{
          "valueString" : "now()"
        }]
      }]
    },
    {
      "name" : "compTitle",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "title",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "Medication Overview"
        }]
      }]
    },
    {
      "name" : "compAuthor",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "au",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Reference"
        }]
      },
      {
        "context" : "au",
        "contextType" : "variable",
        "element" : "display",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "Medication Overview generator"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "author",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "au"
        }]
      }]
    },
    {
      "name" : "sectionTreatmentLines",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "section",
        "variable" : "sect"
      }],
      "rule" : [{
        "name" : "sectTitle",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "context" : "sect",
          "contextType" : "variable",
          "element" : "title",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "Medication Treatment Lines"
          }]
        }]
      },
      {
        "name" : "sectCode",
        "source" : [{
          "context" : "src"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "scc",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Coding"
          }]
        },
        {
          "context" : "scc",
          "contextType" : "variable",
          "element" : "system",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "http://loinc.org"
          }]
        },
        {
          "context" : "scc",
          "contextType" : "variable",
          "element" : "code",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "10160-0"
          }]
        },
        {
          "context" : "scc",
          "contextType" : "variable",
          "element" : "display",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "History of Medication use Narrative"
          }]
        },
        {
          "contextType" : "variable",
          "variable" : "sc",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "CodeableConcept"
          }]
        },
        {
          "context" : "sc",
          "contextType" : "variable",
          "element" : "coding",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "scc"
          }]
        },
        {
          "context" : "sect",
          "contextType" : "variable",
          "element" : "code",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "sc"
          }]
        }]
      },
      {
        "name" : "treatmentLines",
        "source" : [{
          "context" : "src",
          "element" : "medicationTreatmentLine",
          "variable" : "lref"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "tid",
          "transform" : "uuid"
        }],
        "rule" : [{
          "name" : "sectEntry",
          "source" : [{
            "context" : "lref"
          }],
          "target" : [{
            "context" : "sect",
            "contextType" : "variable",
            "element" : "entry",
            "variable" : "se"
          },
          {
            "context" : "se",
            "contextType" : "variable",
            "element" : "reference",
            "transform" : "append",
            "parameter" : [{
              "valueString" : "urn:uuid:"
            },
            {
              "valueId" : "tid"
            }]
          }]
        },
        {
          "name" : "lineEntry",
          "source" : [{
            "context" : "lref"
          }],
          "target" : [{
            "context" : "bundle",
            "contextType" : "variable",
            "element" : "entry",
            "variable" : "te"
          },
          {
            "context" : "te",
            "contextType" : "variable",
            "element" : "fullUrl",
            "transform" : "append",
            "parameter" : [{
              "valueString" : "urn:uuid:"
            },
            {
              "valueId" : "tid"
            }]
          },
          {
            "context" : "te",
            "contextType" : "variable",
            "element" : "resource",
            "variable" : "ms",
            "transform" : "create",
            "parameter" : [{
              "valueString" : "MedicationTreatmentLine"
            }]
          }],
          "rule" : [{
            "name" : "lineContent",
            "source" : [{
              "context" : "lref"
            }],
            "dependent" : [{
              "name" : "MedicationTreatmentLineLMToMedicationStatement",
              "variable" : ["lref", "ms", "pid"]
            }]
          }]
        }]
      }]
    },
    {
      "name" : "attester",
      "source" : [{
        "context" : "src",
        "element" : "verification",
        "variable" : "v"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "attester",
        "variable" : "att"
      }],
      "rule" : [{
        "name" : "attMode",
        "source" : [{
          "context" : "v"
        }],
        "target" : [{
          "context" : "att",
          "contextType" : "variable",
          "element" : "mode",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "professional"
          }]
        }]
      },
      {
        "name" : "attTime",
        "source" : [{
          "context" : "v",
          "element" : "verificationTime",
          "variable" : "vt"
        }],
        "target" : [{
          "context" : "att",
          "contextType" : "variable",
          "element" : "time",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "vt"
          }]
        }]
      },
      {
        "name" : "attParty",
        "source" : [{
          "context" : "v",
          "element" : "practicioner",
          "variable" : "pr"
        }],
        "target" : [{
          "context" : "att",
          "contextType" : "variable",
          "element" : "party",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "pr"
          }]
        }]
      }]
    },
    {
      "name" : "noteFromComment",
      "source" : [{
        "context" : "src",
        "element" : "comment",
        "variable" : "cm"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ext",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "url",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-Composition.note"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "nt",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Annotation"
        }]
      }],
      "rule" : [{
        "name" : "noteText",
        "source" : [{
          "context" : "cm",
          "element" : "commentText",
          "variable" : "ctxt"
        }],
        "target" : [{
          "context" : "nt",
          "contextType" : "variable",
          "element" : "text",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ctxt"
          }]
        }]
      },
      {
        "name" : "noteTime",
        "source" : [{
          "context" : "cm",
          "element" : "date",
          "variable" : "d"
        }],
        "target" : [{
          "context" : "nt",
          "contextType" : "variable",
          "element" : "time",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "d"
          }]
        }]
      },
      {
        "name" : "noteAuthor",
        "source" : [{
          "context" : "cm",
          "element" : "author",
          "variable" : "a"
        }],
        "target" : [{
          "context" : "nt",
          "contextType" : "variable",
          "element" : "author",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "a"
          }]
        }]
      },
      {
        "name" : "noteAssign",
        "source" : [{
          "context" : "cm"
        }],
        "target" : [{
          "context" : "ext",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "nt"
          }]
        },
        {
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ext"
          }]
        }]
      }]
    }]
  },
  {
    "name" : "PatientLMToPatient",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nPatientLM -> FHIR Patient\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "PatientLM",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "Patient",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "patIdentifier",
      "source" : [{
        "context" : "src",
        "element" : "identifier",
        "variable" : "id"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "identifier",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "id"
        }]
      }]
    },
    {
      "name" : "patName",
      "source" : [{
        "context" : "src",
        "element" : "name",
        "variable" : "n"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "name",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "n"
        }]
      }]
    },
    {
      "name" : "patGender",
      "source" : [{
        "context" : "src",
        "element" : "gender",
        "variable" : "g"
      }],
      "rule" : [{
        "name" : "patGenderCoding",
        "source" : [{
          "context" : "g",
          "element" : "coding",
          "variable" : "gc"
        }],
        "rule" : [{
          "name" : "patGenderCode",
          "source" : [{
            "context" : "gc",
            "element" : "code",
            "variable" : "gcode"
          }],
          "target" : [{
            "context" : "tgt",
            "contextType" : "variable",
            "element" : "gender",
            "transform" : "copy",
            "parameter" : [{
              "valueId" : "gcode"
            }]
          }]
        }]
      }]
    },
    {
      "name" : "patBirthDate",
      "source" : [{
        "context" : "src",
        "element" : "dateOfBirth",
        "variable" : "d"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "birthDate",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "d"
        }]
      }]
    }]
  },
  {
    "name" : "MedicationTreatmentLineLMToMedicationStatement",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nMedicationTreatmentLineLM -> MedicationTreatmentLine (profile on MedicationStatement, R4)\r\nReceives the Patient entry's UUID (pid) so MS.subject can reference it.\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "MedicationTreatmentLineLM",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "MedicationTreatmentLine",
      "mode" : "target"
    },
    {
      "name" : "pid",
      "mode" : "source"
    }],
    "rule" : [{
      "name" : "identifier",
      "source" : [{
        "context" : "src",
        "element" : "identifier",
        "variable" : "id"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "identifier",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "id"
        }]
      }]
    },
    {
      "name" : "subject",
      "source" : [{
        "context" : "src"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "subj",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Reference"
        }]
      },
      {
        "context" : "subj",
        "contextType" : "variable",
        "element" : "reference",
        "transform" : "append",
        "parameter" : [{
          "valueString" : "urn:uuid:"
        },
        {
          "valueId" : "pid"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "subject",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "subj"
        }]
      }]
    },
    {
      "name" : "status",
      "source" : [{
        "context" : "src",
        "element" : "status",
        "variable" : "st"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "status",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "st"
        }]
      }]
    },
    {
      "name" : "medicationRef",
      "source" : [{
        "context" : "src",
        "type" : "Reference",
        "element" : "medication",
        "variable" : "mr"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "medication",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "mr"
        }]
      }]
    },
    {
      "name" : "medicationCC",
      "source" : [{
        "context" : "src",
        "type" : "CodeableConcept",
        "element" : "medication",
        "variable" : "mc"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "medication",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "mc"
        }]
      }]
    },
    {
      "name" : "effectivePeriod",
      "source" : [{
        "context" : "src",
        "element" : "effectivePeriod",
        "variable" : "ep"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "effective",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ep"
        }]
      }]
    },
    {
      "name" : "recordingMetadata",
      "source" : [{
        "context" : "src",
        "element" : "recordingMetadata",
        "variable" : "rm"
      }],
      "rule" : [{
        "name" : "dateAsserted",
        "source" : [{
          "context" : "rm",
          "element" : "recordedTime",
          "variable" : "rt"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "dateAsserted",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "rt"
          }]
        }]
      },
      {
        "name" : "informationSource",
        "source" : [{
          "context" : "rm",
          "element" : "recorder",
          "variable" : "rc"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "informationSource",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "rc"
          }]
        }]
      }]
    },
    {
      "name" : "reasonIndication",
      "source" : [{
        "context" : "src",
        "element" : "indication",
        "variable" : "ind"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "reasonCode",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ind"
        }]
      }]
    },
    {
      "name" : "reasonIndicationText",
      "source" : [{
        "context" : "src",
        "element" : "indicationText",
        "variable" : "it"
      }],
      "target" : [{
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
        "element" : "text",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "it"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "reasonCode",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "cc"
        }]
      }]
    },
    {
      "name" : "dosage",
      "source" : [{
        "context" : "src",
        "element" : "usageInstructions",
        "variable" : "ui"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "dosage",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ui"
        }]
      }]
    },
    {
      "name" : "prepInstructions",
      "source" : [{
        "context" : "src",
        "element" : "preparationInstructions",
        "variable" : "pi"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "dos",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Dosage"
        }]
      },
      {
        "context" : "dos",
        "contextType" : "variable",
        "element" : "text",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "pi"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "dosage",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "dos"
        }]
      }]
    },
    {
      "name" : "lineNote",
      "source" : [{
        "context" : "src",
        "element" : "comment",
        "variable" : "cm"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "nt",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Annotation"
        }]
      }],
      "rule" : [{
        "name" : "lineNoteText",
        "source" : [{
          "context" : "cm",
          "element" : "commentText",
          "variable" : "ct"
        }],
        "target" : [{
          "context" : "nt",
          "contextType" : "variable",
          "element" : "text",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ct"
          }]
        }]
      },
      {
        "name" : "lineNoteTime",
        "source" : [{
          "context" : "cm",
          "element" : "date",
          "variable" : "d"
        }],
        "target" : [{
          "context" : "nt",
          "contextType" : "variable",
          "element" : "time",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "d"
          }]
        }]
      },
      {
        "name" : "lineNoteAuthor",
        "source" : [{
          "context" : "cm",
          "element" : "author",
          "variable" : "a"
        }],
        "target" : [{
          "context" : "nt",
          "contextType" : "variable",
          "element" : "author",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "a"
          }]
        }]
      },
      {
        "name" : "lineNoteAssign",
        "source" : [{
          "context" : "cm"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "note",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "nt"
          }]
        }]
      }]
    },
    {
      "name" : "extAdherence",
      "source" : [{
        "context" : "src",
        "element" : "treatmentStatus",
        "variable" : "ts"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ext",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "url",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-MedicationStatement.adherence"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "e1",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      },
      {
        "context" : "e1",
        "contextType" : "variable",
        "element" : "url",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "code"
        }]
      },
      {
        "context" : "e1",
        "contextType" : "variable",
        "element" : "value",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ts"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "extension",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "e1"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "extension",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ext"
        }]
      }]
    },
    {
      "name" : "extAdherenceReason",
      "source" : [{
        "context" : "src",
        "element" : "treatmentStatusReasonCode",
        "variable" : "tsr"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ext",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "url",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-MedicationStatement.adherence"
        }]
      },
      {
        "contextType" : "variable",
        "variable" : "e1",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      },
      {
        "context" : "e1",
        "contextType" : "variable",
        "element" : "url",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "reason"
        }]
      },
      {
        "context" : "e1",
        "contextType" : "variable",
        "element" : "value",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "tsr"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "extension",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "e1"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "extension",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ext"
        }]
      }]
    },
    {
      "name" : "category",
      "source" : [{
        "context" : "src",
        "element" : "category",
        "variable" : "cat"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "category",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "cat"
        }]
      }]
    },
    {
      "name" : "derivedFrom",
      "source" : [{
        "context" : "src",
        "element" : "derivedFrom",
        "variable" : "df"
      }],
      "rule" : [{
        "name" : "derivedFromRequest",
        "source" : [{
          "context" : "df",
          "element" : "request",
          "variable" : "rq"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "derivedFrom",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "rq"
          }]
        }]
      },
      {
        "name" : "derivedFromStatement",
        "source" : [{
          "context" : "df",
          "element" : "statement",
          "variable" : "stm"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "derivedFrom",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "stm"
          }]
        }]
      },
      {
        "name" : "derivedFromDispensation",
        "source" : [{
          "context" : "df",
          "element" : "dispensation",
          "variable" : "dsp"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "derivedFrom",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "dsp"
          }]
        }]
      },
      {
        "name" : "derivedFromAdministration",
        "source" : [{
          "context" : "df",
          "element" : "administration",
          "variable" : "adm"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "derivedFrom",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "adm"
          }]
        }]
      },
      {
        "name" : "derivedFromOther",
        "source" : [{
          "context" : "df",
          "element" : "other",
          "variable" : "oth"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "derivedFrom",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "oth"
          }]
        }]
      }]
    },
    {
      "name" : "extVersion",
      "source" : [{
        "context" : "src",
        "element" : "version",
        "variable" : "v"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ext",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "url",
        "transform" : "copy",
        "parameter" : [{
          "valueString" : "http://hl7.org/fhir/StructureDefinition/artifact-version"
        }]
      },
      {
        "context" : "ext",
        "contextType" : "variable",
        "element" : "value",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "v"
        }]
      },
      {
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "extension",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "ext"
        }]
      }]
    },
    {
      "name" : "extVerification",
      "source" : [{
        "context" : "src",
        "element" : "verificationInformation",
        "variable" : "vi"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ext",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      }],
      "rule" : [{
        "name" : "viUrl",
        "source" : [{
          "context" : "vi"
        }],
        "target" : [{
          "context" : "ext",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/ihe-ext-medicationstatement-verificationinformation"
          }]
        }]
      },
      {
        "name" : "viVerifier",
        "source" : [{
          "context" : "vi",
          "element" : "verifier",
          "variable" : "vr"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "e1",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Extension"
          }]
        },
        {
          "context" : "e1",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "verifier"
          }]
        },
        {
          "context" : "e1",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "vr"
          }]
        },
        {
          "context" : "ext",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "e1"
          }]
        }]
      },
      {
        "name" : "viTime",
        "source" : [{
          "context" : "vi",
          "element" : "verificationTime",
          "variable" : "vt"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "e2",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Extension"
          }]
        },
        {
          "context" : "e2",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "verificationTime"
          }]
        },
        {
          "context" : "e2",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "vt"
          }]
        },
        {
          "context" : "ext",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "e2"
          }]
        }]
      },
      {
        "name" : "viAssign",
        "source" : [{
          "context" : "vi"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ext"
          }]
        }]
      }]
    },
    {
      "name" : "extSubstitution",
      "source" : [{
        "context" : "src",
        "element" : "substitution",
        "variable" : "sub"
      }],
      "target" : [{
        "contextType" : "variable",
        "variable" : "ext",
        "transform" : "create",
        "parameter" : [{
          "valueString" : "Extension"
        }]
      }],
      "rule" : [{
        "name" : "subUrl",
        "source" : [{
          "context" : "sub"
        }],
        "target" : [{
          "context" : "ext",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "https://profiles.ihe.net/PHARM/MEOW/StructureDefinition/ihe-ext-medicationstatement-substitution"
          }]
        }]
      },
      {
        "name" : "subType",
        "source" : [{
          "context" : "sub",
          "element" : "substitutionType",
          "variable" : "t"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "e1",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Extension"
          }]
        },
        {
          "context" : "e1",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "substitutionType"
          }]
        },
        {
          "context" : "e1",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "t"
          }]
        },
        {
          "context" : "ext",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "e1"
          }]
        }]
      },
      {
        "name" : "subReason",
        "source" : [{
          "context" : "sub",
          "element" : "substitutionTypeReason",
          "variable" : "r"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "e2",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Extension"
          }]
        },
        {
          "context" : "e2",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "substitutionTypeReason"
          }]
        },
        {
          "context" : "e2",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "r"
          }]
        },
        {
          "context" : "ext",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "e2"
          }]
        }]
      },
      {
        "name" : "subReasonText",
        "source" : [{
          "context" : "sub",
          "element" : "substitutionTypeReasonText",
          "variable" : "rt"
        }],
        "target" : [{
          "contextType" : "variable",
          "variable" : "e3",
          "transform" : "create",
          "parameter" : [{
            "valueString" : "Extension"
          }]
        },
        {
          "context" : "e3",
          "contextType" : "variable",
          "element" : "url",
          "transform" : "copy",
          "parameter" : [{
            "valueString" : "substitutionTypeReasonText"
          }]
        },
        {
          "context" : "e3",
          "contextType" : "variable",
          "element" : "value",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "rt"
          }]
        },
        {
          "context" : "ext",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "e3"
          }]
        }]
      },
      {
        "name" : "subAssign",
        "source" : [{
          "context" : "sub"
        }],
        "target" : [{
          "context" : "tgt",
          "contextType" : "variable",
          "element" : "extension",
          "transform" : "copy",
          "parameter" : [{
            "valueId" : "ext"
          }]
        }]
      }]
    }]
  },
  {
    "name" : "PractitionerLMToPractitioner",
    "typeMode" : "none",
    "documentation" : "---------------------------------------------------------------------------\r\nPractitionerLM -> FHIR Practitioner\r\n---------------------------------------------------------------------------",
    "input" : [{
      "name" : "src",
      "type" : "PractitionerLM",
      "mode" : "source"
    },
    {
      "name" : "tgt",
      "type" : "Practitioner",
      "mode" : "target"
    }],
    "rule" : [{
      "name" : "practIdentifier",
      "source" : [{
        "context" : "src",
        "element" : "identifier",
        "variable" : "id"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "identifier",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "id"
        }]
      }]
    },
    {
      "name" : "practName",
      "source" : [{
        "context" : "src",
        "element" : "name",
        "variable" : "n"
      }],
      "target" : [{
        "context" : "tgt",
        "contextType" : "variable",
        "element" : "name",
        "transform" : "copy",
        "parameter" : [{
          "valueId" : "n"
        }]
      }]
    }]
  }]
}

```
