<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDBe3b135252953c7f29f4a82b3cdfded35.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
