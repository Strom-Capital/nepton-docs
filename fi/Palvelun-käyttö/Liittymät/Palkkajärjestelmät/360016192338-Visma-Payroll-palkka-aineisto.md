---
id: 360016192338
title: Visma Payroll, palkka-aineisto
url: https://support.nepton.com/hc/fi/articles/360016192338-Visma-Payroll-palkka-aineisto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2020-12-04T05:27:46Z'
---

# Visma Payroll, palkka-aineisto

Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto Visma Payroll -järjestelmään.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden Visma henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360009211157/mceclip0.png)
HUOM.! Jos henkilön Visma henkilötunnistetta ei ole asetettu, käytetään henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymää varten pitää luoda integraation sääntöjoukko. Sääntöjoukon poiminnan ohje löytyy [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Tiedostomuoto
Siirtotiedosto on puolipisteella erotettua tekstimuotoista dataa. Rivinvaihto on `CR` & `LF`. Merkistökoodauksena on ISO-8859-1.
Aineisto sisältää seuraavan otsikkorivin:
[code] 
    Hnro;Hetu;Palkkalaji;Alkupvm;Loppupvm;Määrä;Hinta;Kerroin;Arvo;PRJ1;PRJ2;PRJ3;PRJ4;PRJ5;PRJ6;PRJ7;PRJ8;PRJ9;PRJ10;PRJ11;PRJ12;Selite
    
[/code]
## Rajaukset
Henkilöt henkilönumerolla 0 eivät tule osaksi aineistoa
## Aineiston tietueet
Sarake | Kenttä | Otsikkorivin nimike | Sääntöjoukon kentän nimi | Muoto | Selite  
---|---|---|---|---|---  
A | Henkilönumero | Hnro | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Visma henkilötunniste. Jos Visma henkilötunnistetta ei ole asetettu, käytetään henkilönumeroa  
B | Henkilötunnus | Hetu | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Henkilön henkilönumero, jos tieto on asetettu Neptoniin. Pakollinen jos henkilönumeroa ei ole.  
C | Palkkalaji | Palkkalaji | SalaryCode | merkkijono | Tapahtuman palkkalajin tunnus.  
D | Alkupäivä | Alkupvm | StartDateTime | päivämäärä |  Tapahtuman alkupäivämäärä. Päivämäärä muodossa `VV.KK.PPPP`. Kenttään voi valita päivämäärän muodossa `VVVV-KK-PP`, se muotoillaan oikein riville.  
E | Loppupäivä | Loppupvm | EndDateTime | päivämäärä |  Tapahtuman loppupäivämäärä. Päivämäärä muodossa `VV.KK.PPPP`. Kenttään voi valita päivämäärän muodossa `VVVV-KK-PP`, se muotoillaan oikein riville.  
F | Määrä | Määrä | Amount | desimaaliluku |  Jos rivin määrä on jokin muu kuin määrä euroina, esitetään määrä tässä sarakkeessa. Muutoin sarake on tyhjä. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
G | Euromäärä | Hinta | Amount | desimaaliluku |  Jos rivin määrä on euroina, esitetään määrä tässä sarakkeessa. Muutoin sarake on tyhjä. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
H | Kerroin | Kerroin | _Lisätään automaattisesti, ei korvattavissa_ | desimaaliluku | Aina tyhjä  
I | Euromäärä kokonaisuudessaan | Arvo | _Lisätään automaattisesti, ei korvattavissa_ | desimaaliluku | Aina tyhjä  
J | Projektikoodi 1 | PRJ1 | ProjectCode1 | merkkijono | Projektikoodi 1  
K | Projektikoodi 2 | PRJ2 | ProjectCode2 | merkkijono | Projektikoodi 2  
L | Projektikoodi 3 | PRJ3 | ProjectCode3 | merkkijono | Projektikoodi 3  
M | Projektikoodi 4 | PRJ4 | ProjectCode4 | merkkijono | Projektikoodi 4  
N | Projektikoodi 5 | PRJ5 | ProjectCode5 | merkkijono | Projektikoodi 5  
O | Projektikoodi 6 | PRJ6 | ProjectCode6 | merkkijono | Projektikoodi 6  
P | Projektikoodi 7 | PRJ7 | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Aina tyhjä  
Q | Projektikoodi 8 | PRJ8 | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Aina tyhjä  
R | Projektikoodi 9 | PRJ9 | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Aina tyhjä  
S | Projektikoodi 10 | PRJ10 | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Aina tyhjä  
T | Projektikoodi 11 | PRJ11 | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Aina tyhjä  
U | Projektikoodi 12 | PRJ12 | _Lisätään automaattisesti, ei korvattavissa_ | merkkijono | Aina tyhjä  
V | Tapahtuman huomautus | Selite | Comment | merkkijono | Neptoniin kirjatulle tapahtumalle merkitty huomautus.  
### Esimerkki
[code] 
    Hnro;Hetu;Palkkalaji;Alkupvm;Loppupvm;Määrä;Hinta;Kerroin;Arvo;PRJ1;PRJ2;PRJ3;PRJ4;PRJ5;PRJ6;PRJ7;PRJ8;PRJ9;PRJ10;PRJ11;PRJ12;Selite
    9001;010190-123A;1000;08.07.2019;08.07.2019;7,50;;;;PROJ1;PROJ2;;;;;;;;;;;Maanantain vuoro
[/code]
