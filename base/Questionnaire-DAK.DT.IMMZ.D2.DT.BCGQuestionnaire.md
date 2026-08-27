# Questionnaire for IMMZ.D2 Determine required vaccination(s) if any - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Questionnaire for IMMZ.D2 Determine required vaccination(s) if any**

## Questionnaire: Questionnaire for IMMZ.D2 Determine required vaccination(s) if any
Branch:



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "DAK.DT.IMMZ.D2.DT.BCGQuestionnaire",
  "url" : "http://smart.who.int/base/Questionnaire/DAK.DT.IMMZ.D2.DT.BCGQuestionnaire",
  "version" : "1.0.0",
  "name" : "DAK.DT.IMMZ.D2.DT.BCGQuestionnaire",
  "title" : "IMMZ.D2 Determine required vaccination(s) if any",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-08-27T08:35:55+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "This questionnaire supports the decision logic for: IMMZ.D2 Determine required vaccination(s) if any",
  "item" : [{
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.NumberofBCGprimaryseriesdosesadministered",
    "text" : "Number of BCG primary series doses administered",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "No BCG primary series dose was administered"
    },
    {
      "valueString" : "One BCG primary series dose was administered"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.Age",
    "text" : "Age",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Clients age is between 28 days and 5 years"
    },
    {
      "valueString" : "Clients age is less than or equal to 28 days"
    },
    {
      "valueString" : "Clients age is more than 5 years"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.HIVstatus",
    "text" : "HIV status",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Clients HIV status is negative or unknown"
    },
    {
      "valueString" : "Clients HIV status is positive"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.CurrentlyonART",
    "text" : "Currently on ART",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Client is currently not receiving antiretroviral therapy"
    },
    {
      "valueString" : "Client is currently receiving antiretroviral therapy"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.Immunologicallystable",
    "text" : "Immunologically stable",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Client is immunologically stable"
    },
    {
      "valueString" : "Client is not immunologically stable"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.TBinfectiontestresult",
    "text" : "TB infection test result",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Clients TB infection test result is negative"
    },
    {
      "valueString" : "Clients TB infection test result is positive"
    },
    {
      "valueString" : "Clients TB infection test result is unknown (test not done or no result yet)"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.Timepassedsincealivevaccinewasadministered",
    "text" : "Time passed since a live vaccine was administered",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Live vaccine was administered in the last four weeks"
    },
    {
      "valueString" : "No live vaccine was administered"
    },
    {
      "valueString" : "No live vaccine was administered in the last four weeks"
    }]
  },
  {
    "linkId" : "input.DAK.DT.IMMZ.D2.DT.BCG.Clinicallywell",
    "text" : "Clinically well",
    "type" : "choice",
    "required" : false,
    "answerOption" : [{
      "valueString" : "Client is clinically well"
    },
    {
      "valueString" : "Client is not clinically well"
    }]
  }]
}

```
