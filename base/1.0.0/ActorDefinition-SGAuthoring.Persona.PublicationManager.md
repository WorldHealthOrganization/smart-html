# Publication Manager - SMART Base v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Publication Manager**

## ActorDefinition: Publication Manager (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ActorDefinition/SGAuthoring.Persona.PublicationManager | *Version*:1.0.0 |
| Draft as of 2026-08-27 | *Computable Name*:PublicationManager |

 
A specialist responsible for managing the FHIR Implementation Guide configuration, build process, versioning, and release publication workflow. Publication Managers ensure IGs are correctly configured, built, and published to smart.who.int following the established publication process. 
Key activities: 
* Set up IG repositories from smart-ig-empty template
* Configure sushi-config.yaml (canonical URL, package ID, dependencies)
* Enable GitHub Pages and CI build workflows
* Run FHIR IG Publisher builds and verify output
* Manage semantic versioning (major.minor.patch)
* Create publication-request.json for releases
* Create release branches, tags, and GitHub releases
* Monitor automated publication workflows
* Coordinate with WHO SMART Guidelines team for smart.who.int updates
* Manage cross-IG governance for shared artifacts
* Reset main branch to draft status after publication
 
**Source**: IG Starter Kit, IG Setup, IG Publication, and IG Configuration pages 

