<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:ns prefix="f" uri="http://hl7.org/fhir"/>
  <sch:ns prefix="h" uri="http://www.w3.org/1999/xhtml"/>
  <!-- 
    This file contains just the constraints for the profile ANCServiceRequest
    It includes the base constraints for the resource as well.
    Because of the way that schematrons and containment work, 
    you may need to use this schematron fragment to build a, 
    single schematron that validates contained resources (if you have any) 
  -->
  <sch:pattern>
    <sch:title>f:ServiceRequest</sch:title>
    <sch:rule context="f:ServiceRequest">
      <sch:assert test="count(f:extension[@url = 'http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-rationale']) &lt;= 1">extension with URL = 'http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-rationale': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:code) &gt;= 1">code: minimum cardinality of 'code' is 1</sch:assert>
      <sch:assert test="count(f:occurrence[x]) &gt;= 1">occurrence[x]: minimum cardinality of 'occurrence[x]' is 1</sch:assert>
      <sch:assert test="count(f:authoredOn) &gt;= 1">authoredOn: minimum cardinality of 'authoredOn' is 1</sch:assert>
      <sch:assert test="count(f:requester) &gt;= 1">requester: minimum cardinality of 'requester' is 1</sch:assert>
      <sch:assert test="count(f:locationReference) &gt;= 1">locationReference: minimum cardinality of 'locationReference' is 1</sch:assert>
      <sch:assert test="count(f:locationReference) &lt;= 1">locationReference: maximum cardinality of 'locationReference' is 1</sch:assert>
      <sch:assert test="count(f:note) &gt;= 1">note: minimum cardinality of 'note' is 1</sch:assert>
      <sch:assert test="count(f:note) &lt;= 1">note: maximum cardinality of 'note' is 1</sch:assert>
      <sch:assert test="count(f:relevantHistory) &gt;= 1">relevantHistory: minimum cardinality of 'relevantHistory' is 1</sch:assert>
      <sch:assert test="count(f:relevantHistory) &lt;= 1">relevantHistory: maximum cardinality of 'relevantHistory' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
