<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.html');
else 
  Redirect('http://smart.who.int/ips-pilgrimage/v2.0.2/StructureDefinition-HajjIPS-Composition.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
