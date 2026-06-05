---
id: 360003473538
title: Sonet palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003473538-Sonet-palkkatapahtumat
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
updated_at: '2025-02-11T08:50:25Z'
edited_at: '2025-02-11T08:50:24Z'
---

# Sonet palkkatapahtumat

## Lyhytliittymä
### Tiedostomuoto
Siirtotiedosto on positioeroteltua tekstimuotoista dataa. Tietuepituus 200 + 2.
Tietueet eroteltuna. Tietueet päättyvät joko `CR`+`LF`, `CR` tai `LF` -merkkeihin.
Negatiiviset luvut: kentän ensimmäinen nolla (0) korvataan miinus (`-`) merkillä.
### Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


### Aineiston tietueet – lyhytliittymä
Positiot | Sarakkeen nimi | Sääntöjoukon kentän nimi | Muoto | Kuvaus  
---|---|---|---|---  
1-3 | Yritysnumero | _Lisätään automaattisesti, ei korvattavissa_ | String | Yrityksen tunnus Sonet-järjestelmässä. Infotieto. Tapahtumat ohjautuvat valittuna olevalle yritykselle.  
4-6 | Siirtotunnus | _Lisätään automaattisesti, ei korvattavissa_ | String | Siirtomateriaalin tunnus, joka siirtyy sellaisenaan palkkatapahtumalle. Voidaan käyttää lähdeaineiston tunnistamisessa ja poistossa. Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
7 | Palkansaajantunnisteen tyyppi | _Lisätään automaattisesti, ei korvattavissa_ | String |  Tyyppi ilmaisee, millä tunnisteella palkansaaja tunnistetaan liittymässä. Käytössä olevat tyyppikoodit:
  * 1 = palkansaajan numero (+ tarkennin)
  * 2 = henkilönumero henkilöstöhallinnossa
  * 3 = henkilötunnus

Siirtyy aina aineistossa arvolla 1.  
8-22 | Palkansaajan tunniste | _Lisätään automaattisesti, ei korvattavissa_ | String |  Palkansaajan tunniste. Sisältö määräytyy em. tyypin mukaan. Muoto:
  * 1 = 00200-01 tai 00200
  * 2 = 000001
  * 3 = 101080-001A

  
23-27 | Palkkalaji | SalaryCode | String | Tapahtuman palkkalajin tunnus. Jos liittymässä tulee Sonetin palkkalaji, tuodaan palkkalaji liittymässä sen muotoisena kuin se Sonetissa on (etunollat).  
28 |  |  | String | Tyhjää  
29 | Vastaavuustarkistetunnus |  | String |  Tuodaan 1, jos vastaavuustaulukko on käytössä, muuten tyhjä. Vastaavuustaulukko määritellään siirron ohjauksessa. Tapahtuman palkkalajille voidaan määritellä eri palkkalajin tunnus Sonet-järjestelmässä. Lisäksi voidaan määritellä poikkeussääntöjä ja kustannuspaikan ohjausta. Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
30-40 | Eurosumma |  | String |  Tapahtuman rahasumma. Palkkatapahtuman rahasumma voidaan myös laskea palkkalajikohtaisten laskentakaavojen avulla muiden siirtotapahtumalla ja palkkaustiedoissa olevien tietojen perusteella (esim. tunnit * palkka). HUOM. Jos tässä kentässä tuodaan euroja, siirtyvät ne suoraan tapahtumarivin summaksi, eli tällöin liittymässä ei suoriteta laskentoja. Siirtyy aina aineistossa arvolla 0  
41-49 | Tunnit | "Amount" field if unitType = 'H', 'S' or 'J' | Numeric | Tapahtuman tunnit. Laskukaavassa: SK01  
50 -56 | Määrä | "Amount" field if unitType = 'U', 'D', or 'C' | Numeric | Tapahtuman määrätieto, esim. päivät. Laskukaavassa: SK04  
57-66 | Kustannuspaikka |  | String |  Kustannuspaikka tapahtumalla, mikäli tyhjä, kustannuspaikaksi oletetaan henkilön kustannuspaikka. Aineistossa siiryy tapahtumalle valitun projektin koodi  
67-76 | Tili |  | String |  Kirjanpidon tili, mikäli tyhjä, siirrossa päätellään tapahtuman tili joko henkilöltä tai palkkalajilta. Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
77-79 | Lomasääntö |  | String |  Palkkatapahtuman lomasääntö, vain erillissopimuksesta käytössä Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
80-93 | Varatila |  | String | Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
94-96 | Poissaolokoodi |  | String | Poissaolon syykoodi. Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
97-116 | Viite |  | String | Viitetieto tapahtumalle. Voidaan käyttää vain aineiston tuonnissa Neptoniin mutta ei aineiston vientiin ulos Neptonista.  
117-124 | AlkuPvm | StartDateTime (date format will be converted automatically) | String | Tapahtuman alkupäivä. Hinnoittelu yleensä tämän päivän mukaan. Jos tyhjä, niin palkkakauden alkupäivä tapahtumalle. Siirtyy aina alkupäivä muodossa `PPKKVVVV`  
125-132 | Loppupvm | EndDateTime (date format will be converted automatically) | String | Tapahtuman loppupäivä. Jos tyhjä, niin palkkakauden loppupäivä tapahtumalle. Siirtyy aina loppupäivä muodossa PPKKVVVV  
133-172 | Henkilönimi |  | String | Infotieto, ei siirry liittymässä. Tietue on aina tyhjä.  
173-200 | Varalla |  | String | Tyhjää  
### Esimerkki - lyhytliittymä
[code] 
    001   144                    000000000000000007500000000190                                                         0102201801022018                                                                   
    001   144                    000000000000000007500000000190                                                         0202201802022018                                                                   
    001   144                    000000000000000007500000000190                                                         0502201805022018                                                                   
    001   144                    000000000000000007500000000190                                                         0602201806022018                                                                   
[/code]
## Parametroitu liittymä
Liittymää voidaan käyttää yhdessä Sonet Premiumin kanssa.
### Tiedostomuoto – parametroitu liittymä
Siirtotiedosto on UTF-8 muotoista puolipisteellä (`;`) eroteltua tekstimuotoista dataa. Rivinvaihtona toimii carriage return line feed (`CR`+`LF`)
Kenttien pituuksille ei ole määritelty ylärajaa. Sonetiin määritellään tiedoston luentaan tätä aineistoa vastaavat sarakkeet ja käsittelysäännöt.
Tiedosiirto on mahdollista ottaa käyttöön myös vain yhdellä projektikohdenteella.
### Rajaukset – parametroitu liittymä
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


### Aineiston tietueet – parametroitu liittymä
Sarake | Kentän nimi | Formaatti | Kuvaus  
---|---|---|---  
A | Yritysnumero | string | Siirretään oletuksena arvolla `001`. Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetCompanyNumber`.  
(B) | Siirtotunnus | string | Siirtotunnus, sarake sisällytetään aineistoon vain jos siirtotunnus on asetettu työajan asetuksissa kohdassa CGI Sonet > Siirtotunnus. Jos siirtotunnus sisällytetään, tulee se toisena sarakkeena (B) ja muut sarakkeet siirtyvät sen jälkeen.   
B | Henkilönumero | string | Henkilön Sonet-tunnus / henkilönumero, ei voi korvata  
C | Palkkalajikoodi | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideSalaryCode`  
D | Palkkalajin alakoodi | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideSubSalaryCode`  
E | Amount | decimal | 2 desimaalin tarkkuudella, desimaalierottimena on piste (`.`). Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideAmount`  
F | Määrä yksikköinä | string | 2 desimaalin tarkkuudella, desimaalierottimena on piste (`.`). Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideUnitAmount`.  
G | StartDateTime | date | Päivämäärän muoto: `YYYY-MM-DD`. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideStartDateTime`.  
H | Alkukellonaika | string | Ajan muoto: `hh:mm:ss` kentästä StartDateTime. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideStartDateTime`.  
I | EndDateTime | date | Päivämäärän muoto: `YYYY-MM-DD`. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideEndDateTime`.  
J | Loppukellonaika | string | Ajan muoto: `hh:mm:ss`kentästä EndDateTime. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideEndDateTime`.  
K | Palkkalajikoodin kuvaus | string | Palkkalajin kuvaus. Voidaan ohittaa sääntöjoukon säännössä kentällä `RowDescription`  
L | Palkkalajin alakoodin kuvaus | string | Tarkempi palkkalajin kuvaus. Jos esimerkiksi palkkalajikoodin kuvaus on "Palkallinen poissaolo", sen alakoodin kuvaus voisi esimerkiksi olla "Omat vihkiäiset". Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetSubRowDescription`.  
M | Tapahtuman kuvaus | string | Tapahtuman kuvaus / kommentti. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideComment`.  
N | ProjectCode1 | string | Projektikoodi 1. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode1`.  
O | ProjectCode2 | string | Projektikoodi 2. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode2`.  
P | ProjectCode3 | string | Projektikoodi 3. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode3`.  
Q | ProjectCode4 | string | Projektikoodi 4. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode4`.  
R | ProjectCode5 | string | Projektikoodi 5. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode5`.  
S | ProjectCode6 | string | Projektikoodi 6. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode6`.  
T | Projektikoodit ketjutettuna | string | Jos projektikoodi 1 on "A" ja projektikoodi 2 on "B", tämän kolumnin arvona olisi "AB". Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetConcatenatedProjects`.  
U | Projektikoodi 1:n dimensio 1 | string |  Dimensiotiedoissa esitetään ensimmäinen projektikoodi, joka on jaettu osiin merkillä `/`. Jos projektikoodi 1 on esimerkiksi "Finland/Espoo/Derby", dimension 1 arvona olisi "Finland", dimension 2 arvona "Espoo" ja dimension 3 arvona "Derby". Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetProjectDimension1`.  
V | Projektikoodi 1:n dimensio 2 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetProjectDimension2`  
W | Projektikoodi 1:n dimensio 3 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetProjectDimension3`  
X | Projektikoodi 1:n dimensio 4 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetProjectDimension4`  
Y | Projektikoodi 1:n dimensio 5 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetProjectDimension5`  
Z | Projektikoodi 1:n dimensio 6 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `SonetProjectDimension6`  
### Esimerkki – parametroitu liittymä
[code] 
    001;44;;;7.50;0;2018-02-28;00:00:00;2018-02-28;23:59:00;Palkaton poissaolo;Vanhempainvapaa;;190;;;;;;190;190;;;;;  
    001;15;;;10.00;0;2018-02-01;00:00:00;2018-02-28;23:59:59;Työpäivien lukumäärä;;;;;;;;;;;;;;;
[/code]
