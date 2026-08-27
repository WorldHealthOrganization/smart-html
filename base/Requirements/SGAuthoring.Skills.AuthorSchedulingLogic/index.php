<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.html');
else 
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
