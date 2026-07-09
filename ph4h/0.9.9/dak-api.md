# DAK API Documentation Hub - SMART PH4H v0.9.9

* [**Table of Contents**](toc.md)
* **DAK API Documentation Hub**

## DAK API Documentation Hub

This page provides access to Data Access Kit (DAK) API documentation and schemas.

### API Enumeration Endpoints

These endpoints provide lists of all available schemas and vocabularies of each type:

#### LogicalModels.schema.json

Enumeration of all available Logical Model schemas

##### Available Endpoints:

* [StructureDefinition-MedicationOverviewMin.schema.json](schemas/StructureDefinition-MedicationOverviewMin.schema.json) - JSON Schema for Medication Overview (Minimal)
* [StructureDefinition-MedicationTreatmentLineMin.schema.json](schemas/StructureDefinition-MedicationTreatmentLineMin.schema.json) - JSON Schema for Medication Treatment Line (Minimal)

### Logical Model Schemas (2 available)

JSON Schema definitions for FHIR Logical Models, defining structured data elements and their relationships:

#### Medication Overview (Minimal)

Minimal medication overview payload for use within a QR code payload. Based on the IHE Pharmacy Medication Overview logical model, with short element labels (one or two letters) and simple data

[🩺 FHIR](StructureDefinition-MedicationOverviewMin.md)
[📄 JSON Schema](schemas/StructureDefinition-MedicationOverviewMin.schema.json)
[🔗 OpenAPI](schemas/StructureDefinition-MedicationOverviewMin.openapi.json)

#### Medication Treatment Line (Minimal)

Minimal medication treatment line payload for use within a QR code payload. Based on the IHE Pharmacy Medication Treatment Line logical model, with short element labels (one or two letters) and simple data types suitable for encoding in a compact QR code payload.

[🩺 FHIR](StructureDefinition-MedicationTreatmentLineMin.md)
[📄 JSON Schema](schemas/StructureDefinition-MedicationTreatmentLineMin.schema.json)
[🔗 OpenAPI](schemas/StructureDefinition-MedicationTreatmentLineMin.openapi.json)

### OpenAPI Documentation

Complete API specification documentation for all available endpoints:

#### StructureDefinition-MedicationOverviewMin Endpoints

API endpoints for Medication Overview (Minimal)

[📄 JSON Schema](schemas/StructureDefinition-MedicationOverviewMin.schema.json)
[🔗 OpenAPI](schemas/StructureDefinition-MedicationOverviewMin.openapi.json)

#### StructureDefinition-MedicationTreatmentLineMin Endpoints

API endpoints for Medication Treatment Line (Minimal)

[📄 JSON Schema](schemas/StructureDefinition-MedicationTreatmentLineMin.schema.json)
[🔗 OpenAPI](schemas/StructureDefinition-MedicationTreatmentLineMin.openapi.json)

#### LogicalModels Enumeration Endpoint

Complete list of all available Logical Model schemas

[📄 JSON Schema](LogicalModels.schema.json)
[🔗 OpenAPI](LogicalModels-enumeration.openapi.json)

#### StructureDefinition-MedicationOverviewMin API

OpenAPI specification for StructureDefinition-MedicationOverviewMin

[📖 Documentation](StructureDefinition-MedicationOverviewMin.md)
[🔗 OpenAPI Spec](schemas/StructureDefinition-MedicationOverviewMin.openapi.json)

#### StructureDefinition-MedicationTreatmentLineMin API

OpenAPI specification for StructureDefinition-MedicationTreatmentLineMin

[📖 Documentation](StructureDefinition-MedicationTreatmentLineMin.md)
[🔗 OpenAPI Spec](schemas/StructureDefinition-MedicationTreatmentLineMin.openapi.json)

### Using the DAK API

#### Schema Validation

Each JSON Schema can be used to validate data structures in your applications.

* Type definitions and constraints
* Property descriptions and examples
* Required field specifications
* Enumeration values with links to definitions

#### JSON-LD Semantic Integration

The JSON-LD vocabularies provide semantic web integration for ValueSet enumerations.

#### Integration with FHIR

All schemas are derived from the FHIR definitions in this implementation guide.

#### API Endpoints

The enumeration endpoints provide machine-readable lists of all available schemas.

-------

**This documentation hub is automatically generated from the available schema and API definitions.**

