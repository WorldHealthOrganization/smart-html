# Classification of Digital Health Services and Application Types v2 - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Classification of Digital Health Services and Application Types v2**

## CodeSystem: Classification of Digital Health Services and Application Types v2 (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/CDSCv2 | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:CDSCv2 |
| **Copyright/Legal**: WHO © 2023. Some rights reserved. CC BY-NC-SA 3.0 IGO. | |

 
CodeSystem for the Classification of Digital Health Services and Application Types v2, as defined in the Classification of Digital Interventions, Services and Applications in Health (CDISAH), second edition (2023). ISBN 978-92-4-008194-9. 
Services and Application Types represent the types of software, ICT systems and services or communication channels that deliver or execute digital health interventions (DHIs) and health content. 
The types are organised into five representations within the Digital Health Architecture: A. Point of service B. Health system/Provider administration C. Registries and Directories D. Data Management services E. Surveillance and Response 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Services and Application Types](ValueSet-CDSCv2.md)
* [Services and Application Types: Point of Service](ValueSet-CDSCv2.A.md)
* [Services and Application Types: Health System/Provider Administration](ValueSet-CDSCv2.B.md)
* [Services and Application Types: Registries and Directories](ValueSet-CDSCv2.C.md)
* [Services and Application Types: Data Management Services](ValueSet-CDSCv2.D.md)
* [Services and Application Types: Surveillance and Response](ValueSet-CDSCv2.E.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "CDSCv2",
  "url" : "http://smart.who.int/base/CodeSystem/CDSCv2",
  "version" : "1.0.0",
  "name" : "CDSCv2",
  "title" : "Classification of Digital Health Services and Application Types v2",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-08-27T08:31:36+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "CodeSystem for the Classification of Digital Health Services and Application Types v2,\nas defined in the Classification of Digital Interventions, Services and Applications in Health\n(CDISAH), second edition (2023). ISBN 978-92-4-008194-9.\n\nServices and Application Types represent the types of software, ICT systems and services\nor communication channels that deliver or execute digital health interventions (DHIs) and\nhealth content.\n\nThe types are organised into five representations within the Digital Health Architecture:\n  A. Point of service\n  B. Health system/Provider administration\n  C. Registries and Directories\n  D. Data Management services\n  E. Surveillance and Response",
  "copyright" : "WHO © 2023. Some rights reserved. CC BY-NC-SA 3.0 IGO.",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 43,
  "concept" : [{
    "code" : "A",
    "display" : "Point of service",
    "definition" : "Systems that facilitate the provision and delivery of healthcare services to persons at the point of care."
  },
  {
    "code" : "A1",
    "display" : "Communication systems",
    "definition" : "Systems that are used to transfer electronic information. Messages can be exchanged between healthcare providers or between healthcare providers and persons."
  },
  {
    "code" : "A2",
    "display" : "Community-based information systems",
    "definition" : "Applications that facilitate data collection and use at the community level, utilised by community-based workers who provide health promotion and disease prevention activities."
  },
  {
    "code" : "A3",
    "display" : "Decision support systems",
    "definition" : "Computer based tools which combine medical information databases and algorithms with patient specific data, intended to provide healthcare professionals and/or users with recommendations for diagnosis, prognosis, monitoring and treatment."
  },
  {
    "code" : "A4",
    "display" : "Diagnostics information systems",
    "definition" : "Systems for diagnostic applications found in devices (software in a medical device), wearables that collect health data, radiology information systems, medical imaging systems, and picture archiving and communication systems (PACS)."
  },
  {
    "code" : "A5",
    "display" : "Electronic medical record systems",
    "definition" : "A secure, online system that holds information about people's health and clinical care, managed by healthcare providers. Also known as electronic health record (EHR)."
  },
  {
    "code" : "A6",
    "display" : "Laboratory information systems",
    "definition" : "Systems that support the process from patient sample to patient result, including lab requests/test ordering, sample tracking and processing, and results reporting."
  },
  {
    "code" : "A7",
    "display" : "Personal health records",
    "definition" : "A digital personal health record is a record of an individual's health information in a structured digital format, over which the person has agency."
  },
  {
    "code" : "A8",
    "display" : "Pharmacy information systems",
    "definition" : "Systems that manage prescriptions, dispensing, stock and billing for medicines and health products."
  },
  {
    "code" : "A9",
    "display" : "Telehealth systems",
    "definition" : "Systems that enable remote clinical consultation, monitoring and diagnosis between persons and healthcare providers at a distance."
  },
  {
    "code" : "B",
    "display" : "Health system/Provider administration",
    "definition" : "Systems that support the administrative and managerial functions of health systems and healthcare organisations."
  },
  {
    "code" : "B1",
    "display" : "Blood bank information management systems",
    "definition" : "Systems for managing the collection, testing, processing, storage, and distribution of blood and blood products."
  },
  {
    "code" : "B2",
    "display" : "Health finance-related information systems",
    "definition" : "Systems that manage health financing, insurance enrolment, claims, billing, reimbursement, and budgeting."
  },
  {
    "code" : "B3",
    "display" : "Health program monitoring systems",
    "definition" : "Systems used to collect and analyse aggregate health data for programme planning, monitoring and evaluation."
  },
  {
    "code" : "B4",
    "display" : "Human resource information systems",
    "definition" : "Systems for managing health workforce data including cadres, deployment, credentials, performance and payroll."
  },
  {
    "code" : "B5",
    "display" : "Learning and training systems",
    "definition" : "Systems for delivering, tracking, and assessing training and professional development of health workers."
  },
  {
    "code" : "B6",
    "display" : "Logistics management information systems (LMIS)",
    "definition" : "Systems for managing the health supply chain from forecasting to distribution and stock monitoring."
  },
  {
    "code" : "B7",
    "display" : "Patient Administration systems",
    "definition" : "Systems that manage patient administrative information including admissions, discharges, transfers, appointments and billing."
  },
  {
    "code" : "B8",
    "display" : "Research information systems",
    "definition" : "Systems that support the design, conduct, data management and reporting of health research and clinical trials."
  },
  {
    "code" : "C",
    "display" : "Registries and Directories",
    "definition" : "Systems that create, maintain, and provide authoritative master records for persons, providers, facilities, products and health events."
  },
  {
    "code" : "C1",
    "display" : "Census and population information systems",
    "definition" : "Systems that collect, store, and manage population-level demographic data including census information."
  },
  {
    "code" : "C2",
    "display" : "Civil registration and vital statistics (CRVS) systems",
    "definition" : "Systems that register and certify vital events such as births, deaths, marriages and their underlying causes."
  },
  {
    "code" : "C3",
    "display" : "Facility management information systems",
    "definition" : "Systems for managing health facility information, infrastructure, equipment, capacity and assessments."
  },
  {
    "code" : "C4",
    "display" : "(Health) Facility registries",
    "definition" : "Master lists of health facilities with unique identifiers, locations, services offered, and operational information."
  },
  {
    "code" : "C5",
    "display" : "Health worker registry",
    "definition" : "Systems maintaining authoritative directories of health workforce cadres, credentials, and deployment information."
  },
  {
    "code" : "C6",
    "display" : "Identification registries and directories",
    "definition" : "Systems that create, maintain, and verify unique identities for persons, healthcare providers, and other health actors."
  },
  {
    "code" : "C7",
    "display" : "Immunization information systems",
    "definition" : "Systems for recording, tracking, and reporting individual and population-level immunization history and coverage."
  },
  {
    "code" : "C8",
    "display" : "Master patient index",
    "definition" : "Systems that uniquely identify and link patient records across multiple health information systems and facilities."
  },
  {
    "code" : "C9",
    "display" : "Product catalogues",
    "definition" : "Systems that maintain authoritative lists of approved health commodities, medicines, devices and equipment."
  },
  {
    "code" : "C10",
    "display" : "Public Key directories",
    "definition" : "Systems that manage and distribute public cryptographic keys to support digital signature and identity verification."
  },
  {
    "code" : "C11",
    "display" : "Terminology and classification systems",
    "definition" : "Systems for managing and applying standardised clinical terminologies, ontologies, and health classifications."
  },
  {
    "code" : "D",
    "display" : "Data Management services",
    "definition" : "Services and systems that support the collection, aggregation, storage, analysis, and exchange of health data."
  },
  {
    "code" : "D1",
    "display" : "Analytics Systems",
    "definition" : "Systems that process and analyse health data to produce insights, dashboards, reports and predictive models."
  },
  {
    "code" : "D2",
    "display" : "Data interchange and interoperability",
    "definition" : "Systems and standards that enable health data exchange between disparate systems, including APIs, messaging standards, and interoperability platforms."
  },
  {
    "code" : "D3",
    "display" : "Data warehouses",
    "definition" : "Systems that consolidate and store large volumes of historical health data from multiple sources for analysis and reporting."
  },
  {
    "code" : "D4",
    "display" : "Environmental monitoring systems",
    "definition" : "Systems that monitor environmental determinants of health such as air quality, water safety and vector habitats."
  },
  {
    "code" : "D5",
    "display" : "Geographic information systems (GIS)",
    "definition" : "Systems that capture, analyse and visualise geospatial health data for mapping health events, facilities, and populations."
  },
  {
    "code" : "D6",
    "display" : "Health Management Information systems (HMIS)",
    "definition" : "Systems for aggregate health data reporting, target-setting, and programme monitoring, typically at district and national levels."
  },
  {
    "code" : "D7",
    "display" : "Knowledge management systems",
    "definition" : "Systems for curating, organising and disseminating clinical guidelines, protocols, and health knowledge resources."
  },
  {
    "code" : "D8",
    "display" : "Shared Health Record and Health Information Repository",
    "definition" : "Systems that aggregate and share longitudinal health records across facilities and providers."
  },
  {
    "code" : "E",
    "display" : "Surveillance and Response",
    "definition" : "Systems that support the detection, monitoring, and response to disease outbreaks and public health threats."
  },
  {
    "code" : "E1",
    "display" : "Emergency preparedness and response systems",
    "definition" : "Systems that coordinate emergency medical services, disaster preparedness, and mass casualty management."
  },
  {
    "code" : "E2",
    "display" : "Public health and disease surveillance systems",
    "definition" : "Systems for detecting, monitoring, investigating and responding to disease outbreaks and public health threats."
  }]
}

```
