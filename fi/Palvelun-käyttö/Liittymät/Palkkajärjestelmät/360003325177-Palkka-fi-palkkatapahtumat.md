---
id: 360003325177
title: Palkka.fi palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003325177-Palkka-fi-palkkatapahtumat
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
edited_at: '2020-10-05T10:32:17Z'
---

# Palkka.fi palkkatapahtumat

###  Tiedostomuoto  
Siirtotiedosto on UTF-8 muotoista puolipisteellä (;) eroteltua tekstimuotoista dataa. Kenttien pituuksille ei ole määritelty ylärajaa. Palkka.fi – palvelussa tietuejärjestys ja niiden sisältö on kiinteä.
Palkka.fi rajapinnan tiedostokuvaus löytyy osoitteesta <https://www.palkka.fi/Ohjeet/Ohje/y/190>
### 
###  Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


###  Aineiston tietueet
**Column** |  **Field** |  **Integration query field  
** |  **Format** |  **Header title** |  **Notes**  
---|---|---|---|---|---  
A |  Social security number |  Set automatically, cannot be overridden |  string |  Henkilötunnus |   
B |  Payroll period start date |  Set automatically, cannot be overridden |  string |  Kauden alkupvm |  Format: DD.MM.YYYY  
C |  Payroll period end date |  Set automatically, cannot be overridden |  string |  Kauden päät.pvm |  Format: DD.MM.YYYY  
D |  Salary pay date |  Set when running |  string |  Maksupvm |  Format: DD.MM.YYYY  
E |  Salary code |  SalaryCode |  string |  Palkkalaji |  Salary code. Code must be 3 numbers and it can be followed by string text of the salary code name  
F |  Amount |  Amount |  decimal |  Määrä |  Comma acts as decimal separator  
G |  Unit price |  UserCostGroup |  decimal |  A-hinta |  Mandatory value, comma acts as decimal separator. CostGroup from employee information is put into this field.  
H |  Total Price |  |  Decimal |  Summa |  Optional, left empty  
### 
###    
Esimerkki
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360004530657/mceclip0.png)
