---
id: 360003301277
title: CGI Palkat, poissaolot
url: https://support.nepton.com/hc/fi/articles/360003301277-CGI-Palkat-poissaolot
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
edited_at: '2021-06-22T09:16:41Z'
---

# CGI Palkat, poissaolot

### 
##  Tiedostomuoto
Siirtotiedosto on puolipisteella erotettua tekstimuotoista dataa. Rivinvaihto on CR& LF.
##  Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet 
**Column** |  **Field** |  **Integration rule field  
** |  **Format** |  **Notes**  
---|---|---|---|---  
A |  User cost group |  UserCostGroup |  string |  This can be used for payment group  
B |  Personnel number |  Set automatically, cannot be overridden |  string |   
C |  Absence type |  SalaryCode |  string |  Salary code, for example "85"  
F |  Start date |  StartDateTime |  date |  Format: DD.MM.YYYY. This field exports the event start date. Note that if salary calculations are done for a shift start or end date, the StartDateTime must be overridden to target the shift for the correct salary day.  
G |  End date |  EndDateTime |  date |  Format: DD.MM.YYYY. This field exports the event end date. Note that if salary calculations are done for a shift start or end date, the EndDateTime must be overridden to target the shift for the correct salary day.  
#
