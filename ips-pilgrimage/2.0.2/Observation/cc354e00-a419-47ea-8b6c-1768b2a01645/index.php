<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.html');
else 
  Redirect('http://smart.who.int/ips-pilgrimage/2.0.2/Observation-cc354e00-a419-47ea-8b6c-1768b2a01645.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
