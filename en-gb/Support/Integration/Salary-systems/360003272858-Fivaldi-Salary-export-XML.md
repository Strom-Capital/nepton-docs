---
id: 360003272858
title: 'Fivaldi Salary export, XML '
url: https://support.nepton.com/hc/en-gb/articles/360003272858-Fivaldi-Salary-export-XML
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-06-09T08:54:01Z'
---

# Fivaldi Salary export, XML 

**Sorry!**  
This article has not been translated yet.
## Tiedostomuoto
Siirtotiedosto on XML-muotoista tietoa.
<PayrollBatchId> arvo on 'Palkat pp.kk.vv'. Päivämäärä tulee poimintajakson ensimmäisestä päivästä. Esim. poimitaan jaksolta 1.1.2022-15.1.2022 on ko. arvo 'Palkat 01.01.22'. Ko. arvon voi korvata poimintasäännössä kentällä FivaldiBatchIdentifier. Tämä vastaa csv-muotoisen aineiston Erä-kenttää.
## Rajaukset 
  * Fivaldi Business ID tulee olla syötetty Nepton-palveluun valikossa _Työaika - Hallinta - Työyhteisön asetukset - Liittymät - Visma Fivaldi.![](https://support.nepton.com/hc/article_attachments/11467184356509)_
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston rakenne 
<?xml version="1.0" encoding="ISO-8859-15"?>
<FivaldiXML xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://asp.fivaldi.net/fivaldi/FivaldiXMLv1_7.xsd">
<FVBusinessId>01010ÄÄ1-1</FVBusinessId> //Fivaldi businessId setting is used. Can be overridden with SQL rule.
<FVCreationTime>2017-12-13T14:15:16+02:00</FVCreationTime> //file creation time
<Payroll>
<PayrollBatchId>Palkat 12.04.16</PayrollBatchId> //always contains text palkat and salary range start date
<PayrollRow>
<PayrollEmployeeId></PayrollEmployeeId>
<PayrollDate>2016-05-11</PayrollDate> //Fetched from SalaryRenderingDate
<PayrollSalaryType>200</PayrollSalaryType>
<PayrollAmount>8.00</PayrollAmount>
<PayrollFollowUp1> // up to 4 elements from PayrollFollowUp1 to PayrollFollowup4
<FVFollowUpId>PROJ</FVFollowUpId> //project code
</PayrollFollowUp1>
</PayrollRow>
</Payroll>
</FivaldiXML>
