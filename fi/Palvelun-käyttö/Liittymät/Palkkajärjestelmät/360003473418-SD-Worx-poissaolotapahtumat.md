---
id: 360003473418
title: SD Worx poissaolotapahtumat
url: https://support.nepton.com/hc/fi/articles/360003473418-SD-Worx-poissaolotapahtumat
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels:
- NEPTONNEEDSREVIEW
- sdworks
- sdworx
- SD worx
promoted: false
updated_at: '2026-03-11T11:59:15Z'
edited_at: '2026-03-11T11:59:15Z'
---

# SD Worx poissaolotapahtumat

SD Worx oli aiemmin nimellä Personec W.
## Tiedostomuoto
Siirtotiedosto on ISO-8859-1 muotoista puolipisteellä (;) eroteltua tekstimuotoista dataa. Aineisto ei sisällä otsikoita. Kenttien pituuksille ei ole määritelty ylärajaa.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa.


## Aineiston tietueet
Jos halutaan poimia esimerkiksi usean päivän kestävä yhtäjaksoinen tapahtuman ja haluaa aineistolle tämän pidemmän tapahtuman alku- ja loppupäivämäärän, voi käyttää seuraavaa koodia:  
  
MIN(StartDateTime) AS OverrideStartDateTime,   
MAX(EndDateTime) AS OverrideEndDateTime,
Jos vastaavasti haluaa vaihtaa ajetun jakson alku- ja loppupäivän, niin voi käyttää seuraavaa koodia:
:ExportPeriodStartDate AS OverrideStartDatetime  
:ExportPeriodEndDate AS OverrideEndDatetime
**Column** |  **Description** |  **Integration rule field name  
** |  **Format** |  **Notes**  
---|---|---|---|---  
A |  Cost group |  UserCostGroup |  string |  Employees cost group  
B |  Employee identifier |  Set automatically, cannot be overridden in query |  string |  If integration ID is empty, employee number will be used.  
C |  Start date |  StartDateTime |  string |  Row start date. Format DD.MM.YYYY  
D |  End date |  EndDateTime |  string |  Row end date. Format DD.MM.YYYY  
E |  Salary code |  SalaryCode |  string |   
F |  Checklist |  |  string |  Left empty in export  
G |  Amount |  Amount |  decimal |  With accuracy of 2 decimals, , as decimal separator. Unit conversion is automatic  
H |  Custom data 1 | CustomData1 |  |  Can be overridden in the query to add additional data to the export e.g. SELECT *, 123 as OverrideCustomData1  
I |  Custom data 2 | CustomData2 |  |  Same as above  
J |  Custom data 3 |  CustomData3 |  |  Same as above  
#
