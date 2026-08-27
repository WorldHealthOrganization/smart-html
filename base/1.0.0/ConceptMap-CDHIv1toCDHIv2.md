# Mapping from CDHI v1 to CDISAH v2 - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mapping from CDHI v1 to CDISAH v2**

## ConceptMap: Mapping from CDHI v1 to CDISAH v2 (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ConceptMap/CDHIv1toCDHIv2 | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:CDHIv1toCDHIv2 |

 
Mapping from the Classification of Digital Health Interventions v1 (CDHI v1, 2018) to the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH v2, 2023). 
Key structural changes reflected in this map: 
* User group labels updated throughout (e.g. 'Clients' → 'Persons', 'Health workers' → 'Healthcare providers', 'Health system managers' → 'Health management and support personnel').
* Civil Registration and Vital Statistics (CRVS) consolidated: six v1 codes (3.4.1–3.4.6) merged into two v2 codes (3.4.1, 3.4.2).
* Health financing section restructured: v1 3.5.1 (insurance membership) and 3.5.2 (billing) updated; v1 3.5.3–3.5.6 shifted by one (now 3.5.4–3.5.6 + new 3.5.3).
* Data services (group 4) substantially revised: 4.1.1 changed scope, 4.3 expanded from 4 to 5 codes, 4.4 split from 1 to 3 codes, 4.5 is entirely new.
* New v2 categories with no v1 equivalent are listed as 'unmatched' targets.
 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "CDHIv1toCDHIv2",
  "url" : "http://smart.who.int/base/ConceptMap/CDHIv1toCDHIv2",
  "version" : "1.0.0",
  "name" : "CDHIv1toCDHIv2",
  "title" : "Mapping from CDHI v1 to CDISAH v2",
  "status" : "draft",
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
  "description" : "Mapping from the Classification of Digital Health Interventions v1 (CDHI v1, 2018)\nto the Classification of Digital Interventions, Services and Applications in Health v2\n(CDISAH v2, 2023).\n\nKey structural changes reflected in this map:\n- User group labels updated throughout (e.g. 'Clients' → 'Persons',\n  'Health workers' → 'Healthcare providers', 'Health system managers' →\n  'Health management and support personnel').\n- Civil Registration and Vital Statistics (CRVS) consolidated: six v1 codes\n  (3.4.1–3.4.6) merged into two v2 codes (3.4.1, 3.4.2).\n- Health financing section restructured: v1 3.5.1 (insurance membership) and\n  3.5.2 (billing) updated; v1 3.5.3–3.5.6 shifted by one (now 3.5.4–3.5.6 + new 3.5.3).\n- Data services (group 4) substantially revised: 4.1.1 changed scope,\n  4.3 expanded from 4 to 5 codes, 4.4 split from 1 to 3 codes, 4.5 is entirely new.\n- New v2 categories with no v1 equivalent are listed as 'unmatched' targets.",
  "sourceCanonical" : "http://smart.who.int/base/ValueSet/CDHIv1",
  "targetCanonical" : "http://smart.who.int/base/ValueSet/CDHIv2",
  "group" : [{
    "source" : "http://smart.who.int/base/CodeSystem/CDHIv1",
    "target" : "http://smart.who.int/base/CodeSystem/CDHIv2",
    "element" : [{
      "code" : "1.0",
      "target" : [{
        "code" : "1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Clients' → 'Persons'"
      }]
    },
    {
      "code" : "2.0",
      "target" : [{
        "code" : "2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health workers' → 'Healthcare providers'"
      }]
    },
    {
      "code" : "3.0",
      "target" : [{
        "code" : "3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health system managers' → 'Health management and support personnel'"
      }]
    },
    {
      "code" : "4.0",
      "target" : [{
        "code" : "4",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.1",
      "target" : [{
        "code" : "1.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Targeted client communication' → 'Targeted communication to Persons'"
      }]
    },
    {
      "code" : "1.1.1",
      "target" : [{
        "code" : "1.1.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.1.2",
      "target" : [{
        "code" : "1.1.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client[s]' → 'person[s]'"
      }]
    },
    {
      "code" : "1.1.3",
      "target" : [{
        "code" : "1.1.3",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.1.4",
      "target" : [{
        "code" : "1.1.4",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.2",
      "target" : [{
        "code" : "1.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Untargeted client communication' → 'Untargeted communication to Persons'"
      }]
    },
    {
      "code" : "1.2.1",
      "target" : [{
        "code" : "1.2.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.2.2",
      "target" : [{
        "code" : "1.2.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.3",
      "target" : [{
        "code" : "1.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Client to client communication' → 'Person to Person communication'"
      }]
    },
    {
      "code" : "1.3.1",
      "target" : [{
        "code" : "1.3.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Peer group for clients' → 'Peer group for individuals'"
      }]
    },
    {
      "code" : "1.4",
      "target" : [{
        "code" : "1.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Personal health tracking' [unchanged]"
      }]
    },
    {
      "code" : "1.4.1",
      "target" : [{
        "code" : "1.4.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Access by client' → 'Access by the individual'"
      }]
    },
    {
      "code" : "1.4.2",
      "target" : [{
        "code" : "1.4.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Self monitoring of health... by client' → '...by the individual'"
      }]
    },
    {
      "code" : "1.4.3",
      "target" : [{
        "code" : "1.4.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Active data capture/documentation by client' → '...by an individual'"
      }]
    },
    {
      "code" : "1.5",
      "target" : [{
        "code" : "1.5",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Citizen-based reporting' → 'Person based reporting'"
      }]
    },
    {
      "code" : "1.5.1",
      "target" : [{
        "code" : "1.5.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'by clients' → 'by persons'"
      }]
    },
    {
      "code" : "1.5.2",
      "target" : [{
        "code" : "1.5.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "1.6",
      "target" : [{
        "code" : "1.6",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'On-demand information services to clients' → 'On demand communication with persons'"
      }]
    },
    {
      "code" : "1.6.1",
      "target" : [{
        "code" : "1.6.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Client look-up of health information' → 'Look-up of information on health and health services by individuals'"
      }]
    },
    {
      "code" : "1.7",
      "target" : [{
        "code" : "1.7",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Client financial transactions' → 'Person-centred financial transactions'"
      }]
    },
    {
      "code" : "1.7.1",
      "target" : [{
        "code" : "1.7.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'by client[s]' → 'by individuals'"
      }]
    },
    {
      "code" : "1.7.2",
      "target" : [{
        "code" : "1.7.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'to client[s]' → 'to individuals'"
      }]
    },
    {
      "code" : "1.7.3",
      "target" : [{
        "code" : "1.7.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'to client[s]' → 'to individuals'"
      }]
    },
    {
      "code" : "2.1",
      "target" : [{
        "code" : "2.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Client identification and registration' → 'Identification and registration of persons'"
      }]
    },
    {
      "code" : "2.1.1",
      "target" : [{
        "code" : "2.1.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Verify client unique identity' → 'Verify a person's unique identity'"
      }]
    },
    {
      "code" : "2.1.2",
      "target" : [{
        "code" : "2.1.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client' → 'person[s]'"
      }]
    },
    {
      "code" : "2.2",
      "target" : [{
        "code" : "2.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Client health records' → 'Person-centred health records'"
      }]
    },
    {
      "code" : "2.2.1",
      "target" : [{
        "code" : "2.2.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'clients' → 'person's'"
      }]
    },
    {
      "code" : "2.2.2",
      "target" : [{
        "code" : "2.2.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client's' → 'person-centred'"
      }]
    },
    {
      "code" : "2.2.3",
      "target" : [{
        "code" : "2.2.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client's' → 'person-centred'; now explicitly includes examples [notes; images; documents]"
      }]
    },
    {
      "code" : "2.2.4",
      "target" : [{
        "code" : "2.2.4",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.3",
      "target" : [{
        "code" : "2.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health worker decision support' → 'Healthcare provider decision support'"
      }]
    },
    {
      "code" : "2.3.1",
      "target" : [{
        "code" : "2.3.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.3.2",
      "target" : [{
        "code" : "2.3.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.3.3",
      "target" : [{
        "code" : "2.3.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'clients' → 'persons'"
      }]
    },
    {
      "code" : "2.4",
      "target" : [{
        "code" : "2.4",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.4.1",
      "target" : [{
        "code" : "2.4.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client' → 'person'"
      }]
    },
    {
      "code" : "2.4.2",
      "target" : [{
        "code" : "2.4.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client' → 'person's'"
      }]
    },
    {
      "code" : "2.4.3",
      "target" : [{
        "code" : "2.4.3",
        "equivalence" : "equivalent",
        "comment" : "Expanded: now explicitly lists examples [images; notes; videos]"
      }]
    },
    {
      "code" : "2.4.4",
      "target" : [{
        "code" : "2.4.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare providers'"
      }]
    },
    {
      "code" : "2.5",
      "target" : [{
        "code" : "2.5",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health worker communication' → 'Healthcare provider communication'"
      }]
    },
    {
      "code" : "2.5.1",
      "target" : [{
        "code" : "2.5.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider'"
      }]
    },
    {
      "code" : "2.5.2",
      "target" : [{
        "code" : "2.5.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "2.5.3",
      "target" : [{
        "code" : "2.5.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "2.5.4",
      "target" : [{
        "code" : "2.5.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "2.5.5",
      "target" : [{
        "code" : "2.5.5",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Peer group for health workers' → 'Peer group for healthcare providers'"
      }]
    },
    {
      "code" : "2.6",
      "target" : [{
        "code" : "2.6",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.6.1",
      "target" : [{
        "code" : "2.6.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.6.2",
      "target" : [{
        "code" : "2.6.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.6.3",
      "target" : [{
        "code" : "2.6.3",
        "equivalence" : "wider",
        "comment" : "Scope expanded: v2 explicitly includes social services; police; justice; economic support schemes"
      }]
    },
    {
      "code" : "2.7",
      "target" : [{
        "code" : "2.7",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health worker activity planning' → 'Scheduling and activity planning for healthcare providers'"
      }]
    },
    {
      "code" : "2.7.1",
      "target" : [{
        "code" : "2.7.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client[s]' → 'persons'"
      }]
    },
    {
      "code" : "2.7.2",
      "target" : [{
        "code" : "2.7.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker's' → 'healthcare provider's'"
      }]
    },
    {
      "code" : "2.8",
      "target" : [{
        "code" : "2.8",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health worker training' → 'Healthcare provider training'"
      }]
    },
    {
      "code" : "2.8.1",
      "target" : [{
        "code" : "2.8.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "2.8.2",
      "target" : [{
        "code" : "2.8.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "2.9",
      "target" : [{
        "code" : "2.9",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.9.1",
      "target" : [{
        "code" : "2.9.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.9.2",
      "target" : [{
        "code" : "2.9.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'client's' → 'individual's'"
      }]
    },
    {
      "code" : "2.9.3",
      "target" : [{
        "code" : "2.9.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'adverse drug events' → 'adverse drug effects'"
      }]
    },
    {
      "code" : "2.10",
      "target" : [{
        "code" : "2.10",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker' → 'healthcare provider'"
      }]
    },
    {
      "code" : "2.10.1",
      "target" : [{
        "code" : "2.10.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Transmit diagnostic result to health worker' → 'Transmit person's diagnostic result to healthcare provider'"
      }]
    },
    {
      "code" : "2.10.2",
      "target" : [{
        "code" : "2.10.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.10.3",
      "target" : [{
        "code" : "2.10.3",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "2.10.4",
      "target" : [{
        "code" : "2.10.4",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.1",
      "target" : [{
        "code" : "3.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.1.1",
      "target" : [{
        "code" : "3.1.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.1.2",
      "target" : [{
        "code" : "3.1.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "3.1.3",
      "target" : [{
        "code" : "3.1.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "3.1.4",
      "target" : [{
        "code" : "3.1.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker[s]' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "3.2",
      "target" : [{
        "code" : "3.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.2.1",
      "target" : [{
        "code" : "3.2.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.2.2",
      "target" : [{
        "code" : "3.2.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.2.3",
      "target" : [{
        "code" : "3.2.3",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.2.4",
      "target" : [{
        "code" : "3.2.4",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.2.5",
      "target" : [{
        "code" : "3.2.5",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.2.6",
      "target" : [{
        "code" : "3.2.6",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'by clients' → 'by persons'"
      }]
    },
    {
      "code" : "3.3",
      "target" : [{
        "code" : "3.3",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.3.1",
      "target" : [{
        "code" : "3.3.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.4",
      "target" : [{
        "code" : "3.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Civil Registration and Vital Statistics' [same concept]"
      }]
    },
    {
      "code" : "3.4.1",
      "target" : [{
        "code" : "3.4.1",
        "equivalence" : "wider",
        "comment" : "Consolidated: v1 'Notify birth event' merged with v1 3.4.2 [register] and 3.4.3 [certify] into v2 3.4.1 'Notify; register and certify birth event'"
      }]
    },
    {
      "code" : "3.4.2",
      "target" : [{
        "code" : "3.4.1",
        "equivalence" : "wider",
        "comment" : "Consolidated: v1 'Register birth event' merged into v2 3.4.1 'Notify; register and certify birth event'"
      }]
    },
    {
      "code" : "3.4.3",
      "target" : [{
        "code" : "3.4.1",
        "equivalence" : "wider",
        "comment" : "Consolidated: v1 'Certify birth event' merged into v2 3.4.1 'Notify; register and certify birth event'"
      }]
    },
    {
      "code" : "3.4.4",
      "target" : [{
        "code" : "3.4.2",
        "equivalence" : "wider",
        "comment" : "Consolidated: v1 'Notify death event' merged with v1 3.4.5 [register] and 3.4.6 [certify] into v2 3.4.2 'Notify; register and certify death event'"
      }]
    },
    {
      "code" : "3.4.5",
      "target" : [{
        "code" : "3.4.2",
        "equivalence" : "wider",
        "comment" : "Consolidated: v1 'Register death event' merged into v2 3.4.2 'Notify; register and certify death event'"
      }]
    },
    {
      "code" : "3.4.6",
      "target" : [{
        "code" : "3.4.2",
        "equivalence" : "wider",
        "comment" : "Consolidated: v1 'Certify death event' merged into v2 3.4.2 'Notify; register and certify death event'"
      }]
    },
    {
      "code" : "3.5",
      "target" : [{
        "code" : "3.5",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Health financing' → 'Health system financial management'"
      }]
    },
    {
      "code" : "3.5.1",
      "target" : [{
        "code" : "3.5.1",
        "equivalence" : "equivalent",
        "comment" : "Updated wording: now covers all coverage schemes; not only insurance"
      }]
    },
    {
      "code" : "3.5.2",
      "target" : [{
        "code" : "3.5.2",
        "equivalence" : "equivalent",
        "comment" : "Updated wording: 'Track insurance billing and claims submission' → 'Track and manage insurance billing and claims processes'"
      }]
    },
    {
      "code" : "3.5.4",
      "target" : [{
        "code" : "3.5.4",
        "equivalence" : "equivalent",
        "comment" : "Renumbered from v1 3.5.4; health worker → healthcare provider"
      }]
    },
    {
      "code" : "3.5.5",
      "target" : [{
        "code" : "3.5.5",
        "equivalence" : "equivalent",
        "comment" : "Renumbered from v1 3.5.5; health worker → healthcare provider"
      }]
    },
    {
      "code" : "3.5.6",
      "target" : [{
        "code" : "3.5.6",
        "equivalence" : "equivalent",
        "comment" : "Renumbered from v1 3.5.6; reworded to include revenue and expenditures"
      }]
    },
    {
      "code" : "3.6",
      "target" : [{
        "code" : "3.6",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.6.1",
      "target" : [{
        "code" : "3.6.1",
        "equivalence" : "equivalent",
        "comment" : "Expanded: 'Monitor status' → 'Monitor status and maintenance'"
      }]
    },
    {
      "code" : "3.6.2",
      "target" : [{
        "code" : "3.6.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.7",
      "target" : [{
        "code" : "3.7",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.7.1",
      "target" : [{
        "code" : "3.7.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "3.7.2",
      "target" : [{
        "code" : "3.7.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "4.1",
      "target" : [{
        "code" : "4.1",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Data collection; management; and use' → 'Data Management'"
      }]
    },
    {
      "code" : "4.1.1",
      "target" : [{
        "code" : "4.1.1",
        "equivalence" : "inexact",
        "comment" : "v1: 'Non-routine data collection and management'; v2: 'Form creation for data acquisition' — overlapping but distinct scope"
      }]
    },
    {
      "code" : "4.1.2",
      "target" : [{
        "code" : "4.1.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "4.1.3",
      "target" : [{
        "code" : "4.1.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'visualisation' → 'visualizations'"
      }]
    },
    {
      "code" : "4.1.4",
      "target" : [{
        "code" : "4.1.4",
        "equivalence" : "equivalent",
        "comment" : "Scope extended to explicitly include AI and machine learning"
      }]
    },
    {
      "code" : "4.2",
      "target" : [{
        "code" : "4.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "4.2.1",
      "target" : [{
        "code" : "4.2.1",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "4.2.2",
      "target" : [{
        "code" : "4.2.2",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "4.2.3",
      "target" : [{
        "code" : "4.2.3",
        "equivalence" : "equivalent"
      }]
    },
    {
      "code" : "4.3",
      "target" : [{
        "code" : "4.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Location mapping' → 'Geo spatial information management'; expanded from 4 to 5 sub-codes"
      }]
    },
    {
      "code" : "4.3.1",
      "target" : [{
        "code" : "4.3.1",
        "equivalence" : "equivalent",
        "comment" : "Expanded: 'Map location of health facilities/structures' → '...and households'"
      }]
    },
    {
      "code" : "4.3.2",
      "target" : [{
        "code" : "4.3.2",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Map location of health events' → 'Map location of health event'"
      }]
    },
    {
      "code" : "4.3.3",
      "target" : [{
        "code" : "4.3.3",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'clients and households' → 'persons and settlements'"
      }]
    },
    {
      "code" : "4.3.4",
      "target" : [{
        "code" : "4.3.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'health worker' → 'healthcare provider[s]'"
      }]
    },
    {
      "code" : "4.4",
      "target" : [{
        "code" : "4.4",
        "equivalence" : "equivalent",
        "comment" : "Renamed: 'Data exchange and interoperability'; split from 1 leaf code into 3 in v2"
      }]
    },
    {
      "code" : "4.4.1",
      "target" : [{
        "code" : "4.4.1",
        "equivalence" : "wider",
        "comment" : "v1 'Data exchange across systems' is broader; v2 4.4.1 covers only point-to-point integration. See also v2 4.4.2 [standards-compliant] and 4.4.3 [message routing]."
      }]
    },
    {
      "code" : "4.4.1",
      "target" : [{
        "code" : "4.4.2",
        "equivalence" : "wider",
        "comment" : "v2 4.4.2 'Standards-compliant interoperability' partially covers the broader v1 4.4.1 concept"
      }]
    },
    {
      "code" : "4.4.1",
      "target" : [{
        "code" : "4.4.3",
        "equivalence" : "wider",
        "comment" : "v2 4.4.3 'Message routing' partially covers the broader v1 4.4.1 concept"
      }]
    }]
  }]
}

```
