<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.html');
else 
  Redirect('https://smart.who.int/base/1.0.0/ValueSet-CDSCv2.A.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
