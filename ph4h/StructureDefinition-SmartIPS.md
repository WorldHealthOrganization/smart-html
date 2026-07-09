# SMART Bundle (IPS) - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* [**Artifact Index**](artifacts.md)
* **SMART Bundle (IPS)**

## Resource Profile: SMART Bundle (IPS) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ph4h/StructureDefinition/SmartIPS | *Version*:0.9.9 |
| Draft as of 2026-07-09 | *Computable Name*:SmartIPS |

 
This profile represents the constraints applied to the Bundle resource by the International Patient Summary (IPS) for use within the SMART Guidelines. 
Note: The profile expects atleast one SMART Consent entry to be present. 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.ph4h|current/StructureDefinition/StructureDefinition-SmartIPS.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SmartIPS.csv), [Excel](StructureDefinition-SmartIPS.xlsx), [Schematron](StructureDefinition-SmartIPS.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SmartIPS",
  "url" : "http://smart.who.int/ph4h/StructureDefinition/SmartIPS",
  "version" : "0.9.9",
  "name" : "SmartIPS",
  "title" : "SMART Bundle (IPS)",
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
  "description" : "This profile represents the constraints applied to the Bundle resource by the International Patient Summary (IPS) for use within the SMART Guidelines.\n\nNote: The profile expects atleast one SMART Consent entry to be present.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "cda",
    "uri" : "http://hl7.org/v3/cda",
    "name" : "CDA (R2)"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Bundle",
  "baseDefinition" : "http://hl7.org/fhir/uv/ips/StructureDefinition/Bundle-uv-ips",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Bundle",
      "path" : "Bundle",
      "constraint" : [{
        "key" : "containsSmartConsent",
        "severity" : "error",
        "human" : "At least one entry in the Bundle must be SmartConsent",
        "expression" : "Bundle.entry.resource.ofType(Consent).where(conformsTo('http://smart.who.int/ph4h/StructureDefinition/SmartConsent')).exists()",
        "source" : "http://smart.who.int/ph4h/StructureDefinition/SmartIPS"
      },
      {
        "key" : "containsSmartConsent-cmp",
        "severity" : "error",
        "human" : "At least one consent in the Advanced Directives section must be SmartConsent",
        "expression" : "Bundle.entry.resource.ofType(Composition).section.where(title='Advance Directives').entry.resolve().where(conformsTo('http://smart.who.int/ph4h/StructureDefinition/SmartConsent')).exists()",
        "source" : "http://smart.who.int/ph4h/StructureDefinition/SmartIPS"
      }]
    },
    {
      "id" : "Bundle.entry",
      "path" : "Bundle.entry",
      "comment" : "Must contain the IPS Composition as the first entry (only a single Composition resource instance may be included) and a Patient resource.  Additional constraints are specified in the IPS Composition profile.",
      "min" : 3
    },
    {
      "id" : "Bundle.entry:composition",
      "path" : "Bundle.entry",
      "sliceName" : "composition"
    },
    {
      "id" : "Bundle.entry:composition.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:composition.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:composition.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:composition.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:patient",
      "path" : "Bundle.entry",
      "sliceName" : "patient"
    },
    {
      "id" : "Bundle.entry:patient.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:patient.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:patient.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:patient.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:allergyintolerance",
      "path" : "Bundle.entry",
      "sliceName" : "allergyintolerance"
    },
    {
      "id" : "Bundle.entry:allergyintolerance.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:allergyintolerance.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:allergyintolerance.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:allergyintolerance.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:condition",
      "path" : "Bundle.entry",
      "sliceName" : "condition"
    },
    {
      "id" : "Bundle.entry:condition.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:condition.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:condition.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:condition.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:device",
      "path" : "Bundle.entry",
      "sliceName" : "device"
    },
    {
      "id" : "Bundle.entry:device.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:device.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:device.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:device.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:deviceusestatement",
      "path" : "Bundle.entry",
      "sliceName" : "deviceusestatement"
    },
    {
      "id" : "Bundle.entry:deviceusestatement.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:deviceusestatement.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:deviceusestatement.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:deviceusestatement.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:diagnosticreport",
      "path" : "Bundle.entry",
      "sliceName" : "diagnosticreport"
    },
    {
      "id" : "Bundle.entry:diagnosticreport.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:diagnosticreport.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:diagnosticreport.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:diagnosticreport.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:imagingstudy",
      "path" : "Bundle.entry",
      "sliceName" : "imagingstudy"
    },
    {
      "id" : "Bundle.entry:imagingstudy.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:imagingstudy.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:imagingstudy.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:imagingstudy.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:immunization",
      "path" : "Bundle.entry",
      "sliceName" : "immunization"
    },
    {
      "id" : "Bundle.entry:immunization.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:immunization.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:immunization.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:immunization.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:media",
      "path" : "Bundle.entry",
      "sliceName" : "media"
    },
    {
      "id" : "Bundle.entry:media.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:media.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:media.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:media.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medication",
      "path" : "Bundle.entry",
      "sliceName" : "medication"
    },
    {
      "id" : "Bundle.entry:medication.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:medication.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medication.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medication.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medicationrequest",
      "path" : "Bundle.entry",
      "sliceName" : "medicationrequest"
    },
    {
      "id" : "Bundle.entry:medicationrequest.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:medicationrequest.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medicationrequest.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medicationrequest.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medicationstatement",
      "path" : "Bundle.entry",
      "sliceName" : "medicationstatement"
    },
    {
      "id" : "Bundle.entry:medicationstatement.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:medicationstatement.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medicationstatement.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:medicationstatement.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:practitioner",
      "path" : "Bundle.entry",
      "sliceName" : "practitioner"
    },
    {
      "id" : "Bundle.entry:practitioner.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:practitioner.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:practitioner.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:practitioner.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:practitionerrole",
      "path" : "Bundle.entry",
      "sliceName" : "practitionerrole"
    },
    {
      "id" : "Bundle.entry:practitionerrole.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:practitionerrole.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:practitionerrole.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:practitionerrole.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:procedure",
      "path" : "Bundle.entry",
      "sliceName" : "procedure"
    },
    {
      "id" : "Bundle.entry:procedure.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:procedure.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:procedure.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:procedure.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:organization",
      "path" : "Bundle.entry",
      "sliceName" : "organization"
    },
    {
      "id" : "Bundle.entry:organization.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:organization.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:organization.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:organization.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-edd",
      "path" : "Bundle.entry",
      "sliceName" : "observation-pregnancy-edd"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-edd.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-edd.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-edd.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-edd.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-outcome",
      "path" : "Bundle.entry",
      "sliceName" : "observation-pregnancy-outcome"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-outcome.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-outcome.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-outcome.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-outcome.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-status",
      "path" : "Bundle.entry",
      "sliceName" : "observation-pregnancy-status"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-status.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-status.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-status.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-pregnancy-status.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-alcohol-use",
      "path" : "Bundle.entry",
      "sliceName" : "observation-alcohol-use"
    },
    {
      "id" : "Bundle.entry:observation-alcohol-use.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:observation-alcohol-use.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-alcohol-use.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-alcohol-use.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-tobacco-use",
      "path" : "Bundle.entry",
      "sliceName" : "observation-tobacco-use"
    },
    {
      "id" : "Bundle.entry:observation-tobacco-use.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:observation-tobacco-use.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-tobacco-use.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-tobacco-use.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-results",
      "path" : "Bundle.entry",
      "sliceName" : "observation-results"
    },
    {
      "id" : "Bundle.entry:observation-results.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:observation-results.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-results.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:observation-results.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:specimen",
      "path" : "Bundle.entry",
      "sliceName" : "specimen"
    },
    {
      "id" : "Bundle.entry:specimen.fullUrl",
      "path" : "Bundle.entry.fullUrl",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Bundle.entry:specimen.search",
      "path" : "Bundle.entry.search",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:specimen.request",
      "path" : "Bundle.entry.request",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:specimen.response",
      "path" : "Bundle.entry.response",
      "max" : "0"
    },
    {
      "id" : "Bundle.entry:consent",
      "path" : "Bundle.entry",
      "sliceName" : "consent",
      "min" : 1,
      "max" : "*"
    },
    {
      "id" : "Bundle.entry:consent.resource",
      "path" : "Bundle.entry.resource",
      "type" : [{
        "code" : "Consent"
      }]
    }]
  }
}

```
