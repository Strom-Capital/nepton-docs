---
id: 360003305257
title: Hogia Lön / Hogia LönPlus
url: https://support.nepton.com/hc/fi/articles/360003305257-Hogia-L%C3%B6n-Hogia-L%C3%B6nPlus
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
edited_at: '2020-10-05T10:06:43Z'
---

# Hogia Lön / Hogia LönPlus

### 
##  Tiedostomuoto
Siirtotiedosto on positioeroteltua tekstimuotoista dataa. Lön / Lönplus sisältävät erilaisia aineiston tuontimuotoja. Nepton muodostaa aineiston, jonka tunniste on 214006. Rivinvaihto on CR& LF.
Ensimmäinen rivi sisältää kuusi nollaa (000000) ja viimeinen rivi sisältää kuusi yhdeksikköä (999999)
##  Rajaukset 
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
**__Type 214006__**
**Start Stop Length Content**
Identifier 1 6 6 '214006' - Cannot be overridden
Employment number 7 17 11 N,00000000001-99999999999
Pay Type Generator 18 18 1 AN
’L’ = Pay Type
’A’ = Pay Type Generator
Else = Pay Type Generator
Pay Type nr 19 21 3 N,001-999 - "SalaryCode"
Quantity 22 31 10 N,O, - "Amount"
Ex. 000002350
-000002350
Antal*100, max 9 digits
Price 32 41 10 N,O, - Not used
Ex. 000002350
-000002350
A-pris*100(ören), max 9 digits
Amount 42 58 17 N,O - Not used
Ex. 0000000000678000
-0000000000678000
Belopp*100(ören),max 11 digits
Date from 59 66 8 N,U, format YYYYMMDD - "StartDateTime"
Ex. 20040517
Time from 67 71 5 N,O, format HH:MM - "00:00"
Ex. 17:10
Date up to 72 79 8 N,O, format YYYYMMDD - "EndDateTime"
Ex. 20040520
Time up to 1 80 84 5 N,O, format HH:MM - "00:00"
Ex. 21:45
Date from Pay Type Generator  85 92 8 N,O, format YYYYMMDD
Ex. 20040517
Date up to Pay Type Generator 93 100 8 N,O, format YYYYMMDD
Ex. 20040520
See note below.
Source 101 103 3 N,O, 001-999. See note below
Approved 104 105 2 N,O, 00-01. 01 = Approved
Processed 106 106 1 0. Used by HogiaLön
Cost centre 107 126 20 AN - Not used
Project 127 146 20 AN - "ProjectCode1"
Account 147 158 12 AN - Not used
Cost unit 159 178 20 AN - Not used
Extent 179 184 6 N,O, Percent, 2 decimals. "100.00" - Cannot be overridden
Max 100%, delimiter = ’.’ eller ’,’
Omitted = 100%
Note 185 - - AN, up to 66 characters
