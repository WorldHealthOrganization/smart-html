# SMART Guidelines Tasks - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Tasks**

## CodeSystem: SMART Guidelines Tasks (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/SGTasks | *Version*:1.0.0 |
| Active as of 2026-08-27 | *Computable Name*:SGTasks |

 
CodeSystem for SMART Guidelines tasks which are specializations of the Business Process Modeling Notatiton (BPMN) tasks, which are included in this codesystem 
See [BPMN Spectification](https://www.omg.org/spec/BPMN) for more info. The descriptions were adapted from the [normative human readable documentation](https://www.omg.org/spec/BPMN/2.0.2/PDF). 

 This Code system is referenced in the content logical definition of the following value sets: 

* This CodeSystem is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "SGTasks",
  "url" : "http://smart.who.int/base/CodeSystem/SGTasks",
  "version" : "1.0.0",
  "name" : "SGTasks",
  "title" : "SMART Guidelines Tasks",
  "status" : "active",
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
  "description" : "CodeSystem for SMART Guidelines tasks which are specializations of the Business Process Modeling Notatiton (BPMN) tasks, which are included in this codesystem\n\nSee [BPMN Spectification](https://www.omg.org/spec/BPMN) for more info.  The descriptions were adapted from the [normative human readable documentation](https://www.omg.org/spec/BPMN/2.0.2/PDF).",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 8,
  "concept" : [{
    "code" : "businessRuleTask",
    "display" : "Business Rule Task",
    "definition" : "A Business Rule Task provides a mechanism for the Process to provide input to a Business Rules Engine and to get the output of calculations that the Business Rules Engine might provide."
  },
  {
    "code" : "manualTask",
    "display" : "Manual Task",
    "definition" : "A Manual Task is a Task that is expected to be performed without the aid of any business process execution engine or any application. An example of this could be a telephone technician installing a telephone at a customer location."
  },
  {
    "code" : "receiveTask",
    "display" : "Receive Task",
    "definition" : "A Receive Task is a simple Task that is designed to wait for a Message to arrive from an external Participant (relative to the Process). Once the Message has been received, the Task is completed."
  },
  {
    "code" : "scriptTask",
    "display" : "Script Task",
    "definition" : "A Script Task is executed by a business process engine. The modeler or implementer defines a script in a language that the engine can interpret. When the Task is ready to start, the engine will execute the script. When the script is completed, the Task will also be completed."
  },
  {
    "code" : "sendTask",
    "display" : "Send Task",
    "definition" : "A Send Task is a simple Task that is designed to send a Message to an external Participant (relative to the Process). Once the Message has been sent, the Task is completed."
  },
  {
    "code" : "serviceTask",
    "display" : "Service Task",
    "definition" : "A Service Task is a Task that uses some sort of service, which could be a Web service or an automated application.  : The Service Task has exactly one set of inputs and at most one set of outputs."
  },
  {
    "code" : "task",
    "display" : "Task",
    "definition" : "A Task is an atomic Activity within a Process flow. A Task is used when the work in the Process cannot be broken down to a finer level of detail. Generally, an end-user and/or applications are used to perform the Task when it is executed"
  },
  {
    "code" : "userTask",
    "display" : "User Task",
    "definition" : "A User Task is a typical “workflow” Task where a human performer performs the Task with the assistance of a software application and is scheduled through a task list manager of some sort."
  }]
}

```
