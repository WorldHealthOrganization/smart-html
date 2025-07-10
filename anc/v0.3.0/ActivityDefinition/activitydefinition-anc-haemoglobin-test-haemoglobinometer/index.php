<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.html');
else 
  Redirect('http://smart.who.int/anc/v0.3.0/ActivityDefinition-activitydefinition-anc-haemoglobin-test-haemoglobinometer.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
