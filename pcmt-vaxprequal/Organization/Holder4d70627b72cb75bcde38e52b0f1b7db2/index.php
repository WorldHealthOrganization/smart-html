<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.html');
else 
  Redirect('http://smart.who.int/pcmt-vaxprequal/v0.1.0/Organization-Holder4d70627b72cb75bcde38e52b0f1b7db2.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
