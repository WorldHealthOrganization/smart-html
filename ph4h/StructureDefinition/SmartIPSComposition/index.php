<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.html');
else 
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureDefinition-SmartIPSComposition.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
