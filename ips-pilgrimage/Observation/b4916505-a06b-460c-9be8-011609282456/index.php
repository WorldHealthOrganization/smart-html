<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.html');
else 
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-b4916505-a06b-460c-9be8-011609282456.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
