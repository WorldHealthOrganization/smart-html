<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.html');
else 
  Redirect('https://smart.who.int/base/1.0.0/Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
