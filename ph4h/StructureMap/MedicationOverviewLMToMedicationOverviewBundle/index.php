<?php
function Redirect($url)
{
  header('Location: ' . $url, true, 302);
  exit();
}

$accept = $_SERVER['HTTP_ACCEPT'];
if (strpos($accept, 'application/json+fhir') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.json2');
elseif (strpos($accept, 'application/fhir+json') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.json1');
elseif (strpos($accept, 'json') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.json');
elseif (strpos($accept, 'application/xml+fhir') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.xml2');
elseif (strpos($accept, 'application/fhir+xml') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.xml1');
elseif (strpos($accept, 'html') !== false)
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.html');
else 
  Redirect('http://smart.who.int/ph4h/0.9.9/StructureMap-MedicationOverviewLMToMedicationOverviewBundle.xml');
?>
    
You should not be seeing this page. If you do, PHP has failed badly.
