---
id: 360003515197
title: SD Worx lomatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003515197-SD-Worx-lomatapahtumat
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
updated_at: '2025-07-09T04:53:13Z'
edited_at: '2025-07-09T04:53:13Z'
---

# SD Worx lomatapahtumat

SD Worx oli aiemmin nimellä Personec W.
## Tiedostomuoto
Siirtotiedosto on ISO-8859-1 muotoista puolipisteellä (;) eroteltua tekstimuotoista dataa. Aineisto ei sisällä otsikoita. Kenttien pituuksille ei ole määritelty ylärajaa.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
**Column** |  **Description** |  **Integration query field  
** |  **Format** |  **Notes**  
---|---|---|---|---  
A |  Cost group |  UserCostGroup |  string |  Employees cost group  
B |  Employee identifier |  Set automatically, cannot be overridden |  string |  If integration ID is empty, employee number will be used.  
C |  Vacation year |  |  integer |  Left empty in export  
D |  Start date |  StartDateTime |  string |  Row start date. Format DD.MM.YYYY  
E |  End date |  EndDateTime |  string |  Row end date. Format DD.MM.YYYY  
F |  Amount of vacation days in seconds |  Amount |  decimal |  With accuracy of 2 decimals, ',' as decimal separator  
G |  Amount of holiday pay leave days |  |  decimal |  Left empty (string) in export  
H |  Amount of vacation days into bank |  |  decimal |  Left empty (string) in export  
I |  Salary code |  SalaryCode |  string |   
J |  Is vacation held |  |  string |  Left empty in export  
K |  Is vacation paid |  |  string |  Left empty in export  
L |  Vacation pay date |  |  string |  Left empty in export
