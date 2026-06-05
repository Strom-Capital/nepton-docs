---
id: 360003355918
title: Populus, palkka-aineisto, CSV
url: https://support.nepton.com/hc/fi/articles/360003355918-Populus-palkka-aineisto-CSV
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
updated_at: '2025-06-12T07:50:20Z'
edited_at: '2025-06-12T07:49:42Z'
---

# Populus, palkka-aineisto, CSV

## Tiedostomuoto
  * Siirtotiedosto on puolipisteellä erotettua tekstimuotoista dataa. Rivinvaihto on line feed (`LF`). Merkistökoodaus on UTF-8. Tiedostolla ei ole otsikkoriviä.


## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa.
  * Toimii vain integraation sääntöjoukkojen kanssa.
  * Mikäli poimintasäännössä valitaan joku kentistä N - Y (CustomData1 - 12), sisällytetään tuloksiin myös näiden kaikkien kenttien tyhjät arvot. Mikäli kenttiä N - Y ei käytetä valinnassa, näytetään tulokset vain kenttään M asti. 


### Aineston tietueet
Column | Description | Integration query field | Format | Notes  
---|---|---|---|---  
A | Personnel number | Asetetaan automaattisesti, ei voi yliajaa | number | Maksimipituus: 6 merkkiä.  
B | Ps-ID | PopulusPsId | number | Maksimipituus: 6 merkkiä. Haetaan kentästä `PopulusPsId`  
C | Salary type | SalaryCode | number | Palkkalajikoodi, esimerkiksi "1000". Maksimipituus: 4 merkkiä.  
D | Start date | StartDateTime (päivämäärän muoto käsitellään automaattisesti) | date | Muoto: `YYYYMMDD`. Rivin alkamisaika.  
E | End date |  EndDateTime (fpäivämäärän muoto käsitellään automaattisesti) | date | Muoto: `YYYYMMDD`. Rivin päättymisaika.  
F | Amount | Amount | decimal | Pilkku `,` toimii desimaalierottimena, tarkkuus 2 desimaalia. Maksimipituus: 8 merkkiä.  
G | Unit price | UnitPrice | decimal | Piste `.` toimii desimaalierottimena, tarkkuus 2 desimaalia. Haetaan kentästä `UnitPrice`. Maksimipituus: 8 merkkiä  
H | Total price | TotalPrice | decimal | Piste `.` toimii desimaalierottimena, tarkkuus 2 desimaalia. Haetaan kentästä `TotalPrice`. Maksimipituus: 8 merkkiä  
I | Account | PopulusAccount | string | Haetaan kentästä `PopulusAccount`. Maksimipituus: 8 merkkiä  
J | Cost centre | UserCostGroup | string | Haetaan henkilön kustannuspaikan tiedosta. Maksimipituus: 10 merkkiä  
K | Order | PopulusOrder | number | Haetaan kentästä `PopulusOrder`. Maksimipituus: 12 merkkiä  
L | VAT | PopulusVat | string | Haetaan kentästä `PopulusVat`. Maksimipituus: 2 merkkiä  
M | Additional identifier | PopulusAdditionalIdentifier | string | Haetaan kentästä `PopulusAdditionalIdentifier`. Maksimipituus: 15 merkkiä  
N | Custom data 1 | CustomData1 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test1' as CustomData1  
O | Custom data 2 | CustomData2 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test2' as CustomData2  
P | Custom data 3 | CustomData3 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test3' as CustomData3  
Q | Custom data 4 | CustomData4 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test4' as CustomData4  
R | Custom data 5 | CustomData5 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test5' as CustomData5  
S | Custom data 6 | CustomData6 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test6' as CustomData6  
T | Custom data 7 | CustomData7 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test7' as CustomData7  
U | Custom data 8 | CustomData8 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test8' as CustomData8  
V | Custom data 9 | CustomData9 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test9' as CustomData9  
W | Custom data 10 | CustomData10 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test10' as CustomData10  
X | Custom data 11 | CustomData11 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test11' as CustomData11  
Y | Custom data 12 | CustomData12 | string | Voidaan käyttää mukautetun tiedon vientiin, esim. 'test12' as CustomData12
