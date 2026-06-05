---
id: 360003299237
title: CGI Palkat, loma-aineisto
url: https://support.nepton.com/hc/fi/articles/360003299237-CGI-Palkat-loma-aineisto
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
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2020-10-05T09:47:04Z'
---

# CGI Palkat, loma-aineisto

## Tiedostomuoto 
Siirtotiedosto on puolipisteella erotettua tekstimuotoista dataa. Rivinvaihto on CR& LF. 
##  Rajaukset 
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet 
**Column** |  **Field** |  **Integration query field  
** |  **Format** |  **Notes**  
---|---|---|---|---  
A |  User cost group |  UserCostGroup |  string |  This can be used for paymen group  
B |  Personnel number |  _Lisätään automaattisesti, ei korvattavissa_ |  string |   
C |  Holiday Type |  _Saa arvonsa sääntöjoukon yksittäisen säännön Koodi-kentästä ja voidaan korvata käyttämällä kenttänimeä_ OverrideSalaryCode |  string |  Salary code, for example "L"  
F |  Start date |  StartDateTime |  date |  Format: DD.MM.YYYY. Row start date  
G |  End date |  EndDateTime |  date |  Format: DD.MM.YYYY. Row end date  
H |  Holiday target year |  Comment |  string |  Event comment, trimmed to 2000 characters
