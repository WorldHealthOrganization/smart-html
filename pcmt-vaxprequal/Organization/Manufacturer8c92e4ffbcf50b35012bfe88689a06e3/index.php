<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Manufacturer8c92e4ffbcf50b35012bfe88689a06e3.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
