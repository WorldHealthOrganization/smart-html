<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-HepatitisBProduct2c7bb1d3d1f6b656f2b91e6399ac8935.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
