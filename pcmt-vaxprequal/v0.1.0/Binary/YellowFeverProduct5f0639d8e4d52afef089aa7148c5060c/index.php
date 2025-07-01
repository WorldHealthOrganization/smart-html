<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-YellowFeverProduct5f0639d8e4d52afef089aa7148c5060c.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
