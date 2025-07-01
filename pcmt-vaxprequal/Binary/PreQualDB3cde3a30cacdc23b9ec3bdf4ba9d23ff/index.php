<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Binary-PreQualDB3cde3a30cacdc23b9ec3bdf4ba9d23ff.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
