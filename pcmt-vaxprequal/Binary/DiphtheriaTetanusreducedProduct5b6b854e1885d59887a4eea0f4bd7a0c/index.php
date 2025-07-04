<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-DiphtheriaTetanusreducedProduct5b6b854e1885d59887a4eea0f4bd7a0c.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
