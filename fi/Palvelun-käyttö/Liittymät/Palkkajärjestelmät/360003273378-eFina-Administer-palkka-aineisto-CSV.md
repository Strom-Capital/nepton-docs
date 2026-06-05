---
id: 360003273378
title: eFina Administer palkka-aineisto, CSV
url: https://support.nepton.com/hc/fi/articles/360003273378-eFina-Administer-palkka-aineisto-CSV
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
updated_at: '2025-08-06T09:08:39Z'
edited_at: '2023-09-04T06:38:35Z'
---

# eFina Administer palkka-aineisto, CSV

## Tiedostomuoto
Siirtotiedosto on puolipisteella erotettua tekstimuotoista dataa. Rivinvaihto on CR & LF. Merkistökoodaus on UTF-8.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
Column | Field | Integration query field | Format | Notes  
---|---|---|---|---  
A | Personnel number | Set automatically, cannot be overridden | number | Mandatory, maximum length 8  
B | Social security number | Set automatically | string | Can be overridden with `eFinaSocialSecurityNumber`. Maximum length 11  
C | Salary code | SalaryCode | number | Mandatory, maximum length 3  
D | Amount | Amount | decimal | Comma (`,`) as decimal separator. Maximum length 9  
E | Unit price | UnitPrice | decimal | Comma (`,`) as decimal separator. Maximum length 9. Can be overridden with `UnitPrice`  
F | Total price | TotalPrice | decimal | Comma (`,`) as decimal separator. Maximum length 9. Can be overridden with `TotalPrice`  
G | Comment | Comment | string | Maximum length 58 (automatically limited in file)  
H | Project Code 1 | ProjectCode1 | number | Maximum length 6. Populated from `ProjectCode1`  
I | Project Code 2 | ProjectCode2 | number | Maximum length 6. Populated from `ProjectCode2`  
J | Project Code 3 | ProjectCode3 | number | Maximum length 6. Populated from `ProjectCode3`  
K | Employee Name | eFinaEmployeeName | string | Person's first and last name. Can be overridden with `eFinaEmployeeName`  
L | Project Code 4 | ProjectCode4 | number | Maximum length 6. Populated from `ProjectCode4`  
M | Project Code 5 | ProjectCode5 | number | Maximum length 6. Populated from `ProjectCode5`  
N | Project Code 6 | ProjectCode6 | number | Maximum length 6. Populated from `ProjectCode6`
