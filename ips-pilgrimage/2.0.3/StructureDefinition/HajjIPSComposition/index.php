<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.html');
else 
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.3/StructureDefinition-HajjIPSComposition.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
