---
id: 360003317317
title: Visma Nova palkanlaskennan tiedot
url: https://support.nepton.com/hc/fi/articles/360003317317-Visma-Nova-palkanlaskennan-tiedot
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
edited_at: '2023-09-11T12:12:50Z'
---

# Visma Nova palkanlaskennan tiedot

## Tiedostomuoto
Siirtotiedosto on ISO-8859-1 puolipiste-eroteltua tietoa, jossa rivien erottimena toimii carriage return line feed (`CRLF`). Siirrettävä aineisto on Visma Nova palkanlaskennan tiedot – siirtomuodon mukaista.
Aineistossa toteutaan tietuetyypit 3 ja 4.
## Uuden version lisäsarakkeet
Uudessa Visma Nova -versiossa on käytettävissä uusia sarakkeita, kuten esimerkiksi ansainta-ajan alku ja -loppupäivämäärä. Tarkempi kuvaus sarakkeista löytyy alempaa.
Uuden tiedostomuodon voit ottaa käyttöön menemällä **Työaika - > Hallinta -> Työyhteisön asetukset -> Liittymät -> Visma** ja valitsemalla Visma Nova -otsikon alta "Käytä uutta tiedostomuotoa palkka-aineistolla" arvoksi Kyllä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360005431577)
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
Tietuetyypit:
  1. **Henkilö (ei siirretä)**
  2. **Palkkalajit (ei siirretä)**
  3. **Palkkakauden tiedot**
Tietueet siirretään alla olevilla otsikoilla:
[code] TYYPPI3;MAKSUPVM;HNRO;SELITE;ALKUPVM;LOPPUPVM;TYOPAIVAT;VEROPAIVAT;RAHAPALKKA;EISOTUNALAISET;LUONTOISEDUT;EVAHENNYKSET;KORVAUKSET;ENNAKONPIDATYS;EVAK;TVAK;AY_MAKSU;MVAHENNYKSET;MAKSETAAN;SOTU;EMAKSU;TMAKSU;EITEL;EPL6;TTVMAKSU;TILA;TILIOITY;EVAKUUTUS;TVAKUUTUS;PIDTAPA;TXT;AYNRO2;TIETUEMPVM;TIETUEMUSER;VALUUTTA;NUMERO;
[/code]
Jos asetuksista on otettu käyttöön uudempi Visma Nova tiedostomuoto, tietueet siirretään seuraavilla otsikoilla:
[code] TYYPPI3;MAKSUPVM;HNRO;SELITE;ALKUPVM;LOPPUPVM;TYOPAIVAT;VEROPAIVAT;RAHAPALKKA;EISOTUNALAISET;LUONTOISEDUT;EVAHENNYKSET;KORVAUKSET;ENNAKONPIDATYS;EVAK;TVAK;AY_MAKSU;MVAHENNYKSET;MAKSETAAN;SOTU;EMAKSU;TMAKSU;EITEL;EPL6;TTVMAKSU;TILA;TILIOITY;EVAKUUTUS;TVAKUUTUS;PIDTAPA;TXT;AYNRO2;TIETUEPVM;TIETUEUSER;TIETUEMPVM;TIETUEMUSER;VALUUTTA;OSASTO;EIENNAKKOA;EITVAK;EIAY;NUMERO;
[/code]
  4. **Palkkakauden tapahtumat**
Tietueet siirretään alla olevilla otsikoilla:
[code] TYYPPI4;MAKSUPVM;HNRO;PLAJI;KPL;AHINTA;YHTEENSA;TILI;KPAIKKA;PROJEKTI;PVM;NUMERO;
[/code]
Jos asetuksista on otettu käyttöön uudempi Visma Nova tiedostomuoto, tietueet siirretään seuraavilla otsikoilla:
[code] TYYPPI4;MAKSUPVM;HNRO;PLAJI;KPL;AHINTA;YHTEENSA;TILI;KPAIKKA;PROJEKTI;PVM;TYONRO;SELITE;TVR;RIVI;VALUUTTA;NUMERO;PLAJISELITE;TYONUMERO;TYOVAIHE;AALKUPVM;ALOPPUPVM;
[/code]


### Tietuetyyppi 3 (palkkakauden tiedot)
Sarake | Kenttä | Sääntöjoukon kentän nimi | Tyyppi/pituus | Otsikko | Selite | Pakollinen  
---|---|---|---|---|---|---  
A | **Tietuetyyppi** | **** | smallint | TYYPPI3 | Siirretään aina arvolla `3` (palkkakauden tiedot). | Kyllä  
B | **Maksupäivä** | PayDate**  
** | date | MAKSUPVM |  Palkkakauden maksupäivämäärä, muodossa `yyyy-mm-dd`. Kentän arvo annetaan tiedoston latauksessa käyttöliittymässä ja voidaan korvata poimintasäännössä kentällä `PayDate` | Kyllä  
C | **Henkilönumero** | _Lisätään automaattisesti, ei korvattavissa_ | int | HNRO | Henkilön Visma-tunniste, jos se on asetettu, muutoin henkilönumero | Kyllä  
D | **Selite** | **** | string (25) | SELITE | Palkkakauden selite, siirretään aina tyhjänä | Ei  
E | **Alkupäivämäärä** | StartDateTime**  
** | date | ALKUPVM | Palkkakauden alkupäivämäärä, muodossa `yyyy-mm-dd` | Kyllä  
F | **Loppupäivämäärä** | EndDateTime**  
** | date | LOPPUPVM | Palkkakauden loppupäivämäärä, muodossa `yyyy-mm-dd` | Kyllä  
G | **Työpäivät** | **** | money | TYOPAIVAT | Palkkakauden työpäivät, siirretään aina tyhjänä | Ei  
H | **Veropäivät** | **** | money | VEROPAIVAT | Palkkakauden veropäivät, siirretään aina tyhjänä | Ei  
I | **Rahapalkka** | **** | money | RAHAPALKKA | Palkkakauden rahapalkka, siirretään aina tyhjänä | Ei  
J | **Ei sotunalaiset** | **** | money | EISOTUNALAISET | Siirretään aina tyhjänä | Ei  
K | **Luontoisedut** | **** | money | LUONTOISEDUT | Siirretään aina tyhjänä | Ei  
L | **Veronalaiset vähennykset** | **** | money | EVAHENNYKSET | Siirretään aina tyhjänä | Ei  
M | **Korvaukset** | **** | money | KORVAUKSET | Siirretään aina tyhjänä | Ei  
N | **Ennakonpidätys** | **** | money | ENNAKONPIDATYS | Siirretään aina tyhjänä | Ei  
O | **Eläkev. osuus** | **** | money | EVAK | Työntekijän eläkev. osuus, siirretään aina tyhjänä | Ei  
P | **Työttöm.vak. osuus** | **** | money | TVAK | Työntekijän työttöm.vak. osuus, siirretään aina tyhjänä | Ei  
Q | **Ammattiyhdistysmaksu** | **** | money | AY_MAKSU | Siirretään aina tyhjänä | Ei  
R | **Muut +/- vähennykset** | **** | money | MVAHENNYKSET | Siirretään aina tyhjänä | Ei  
S | **Maksetaan** | **** | money | MAKSETAAN | Siirretään aina tyhjänä | Ei  
T | **Sosiaaliturvamaksu** | **** | money | SOTU | Siirretään aina tyhjänä | Ei  
U | **Kokonaiseläkevak. maksu** | **** | money | EMAKSU | Siirretään aina tyhjänä | Ei  
V | **Kokonaistyöttöm.vak.maksu** | **** | money | TMAKSU | Siirretään aina tyhjänä | Ei  
W | **Ei tellin alaiset ansiot** | **** | money | EITEL | Siirretään aina tyhjänä | Ei  
X | **EPL6:n alainen tulo** | **** | money | EPL6 | Siirretään aina tyhjänä | Ei  
Y | **Tapaturmavakuutusmaksu** | **** | money | TTVMAKSU | Siirretään aina tyhjänä | Ei  
Z | **Palkan tila** | **** | smallint | TILA | Siirretään aina tyhjänä | Ei  
AA | **Tiliöity vaiko ei** | **** | smallint | TILIOITY | Siirretään aina tyhjänä | Ei  
AB | **Eläkevakuutus** | **** | smallint | EVAKUUTUS | Siirretään aina tyhjänä | Ei  
AC | **Työttömyysvakuutus** | **** | smallint | TVAKUUTUS | Siirretään aina tyhjänä | Ei  
AD | **Pidätystapa** | **** | string (30) | PIDTAPA | Siirretään aina tyhjänä | Ei  
AE | **Palkkakauden vapaa teksti** | **** | string (2000) | TXT | Siirretään aina tyhjänä | Ei  
AF | **Ammattiyhdistysnumero** | **** | string (4) | AYNRO2 | Siirretään aina tyhjänä | Ei  
AG | **Tietueen luontipvm** | **** | date | TIETUEPVM | Siirretään aina tyhjänä | Ei  
AH | **Tietueen perustaja** | **** | date | TIETUEUSER | Siirretään aina tyhjänä | Ei  
AI | **Tietueen muutospvm** | **** | date | TIETUEMPVM | Siirretään aina tyhjänä | Ei  
AJ | **Tietueen muuttaja** | **** | string (20) | TIETUEMUSER | Siirretään aina tyhjänä | Ei  
AK | **Valuutta** | **** | string (5) | VALUUTTA | Siirretään aina tyhjänä | Ei  
AL | **Osasto** | **** | string (10) | OSASTO | Siirretään aina tyhjänä | Ei  
AM | **Ei ennakon alaiset** | **** | money | EIENNAKKOA | Siirretään aina tyhjänä | Ei  
AN | **Ei tvak:n alaiset** | **** | money | EITVAK | Siirretään aina tyhjänä | Ei  
AO | **Ei ay:n alaiset** | **** | money | EIAY | Siirretään aina tyhjänä | Ei  
AP | **Numero** | VismaNovaSalaryRowNumber | integer | NUMERO | Avain jolla linkitetään tapahtumat. Tieto asetetaan poimintasäännön kentällä `VismaNovaSalaryRowNumber` | Kyllä  
### Tietuetyyppi 4 (palkkakauden tapahtumat)
Sarake | Kenttä | Tyyppi/pituus | Otsikko | Selite | Sääntöjoukon kentän nimi | Pakollinen  
---|---|---|---|---|---|---  
A | **Tietuetyyppi** | smallint | TYYPPI4 | Siirretään aina arvolla `4` (palkkakauden tapahtumat). |  | Kyllä  
B | **Maksupäivä** | date | MAKSUPVM |  Palkkakauden maksupäivämäärä, muodossa `yyyy-mm-dd`. Kentän arvo annetaan tiedoston latauksessa käyttöliittymässä ja voidaan asettaa poimintasäännössä kentällä `PayDate` | PayDate | Kyllä  
C | **Henkilönumero** | int | HNRO | Henkilön Visma-tunniste, jos se on asetettu, muutoin henkilönumero | _Lisätään automaattisesti, ei korvattavissa_ | Kyllä  
D | **Palkkalaji** | smallint | PLAJI | Rivin palkkalajikoodi | SalaryCode | Kyllä  
E | **Kappalemäärä** | decimal | KPL |  Rivin määrä 2 desimaalin tarkkuudella. Desimaalierottimena käytetään pilkkua. Jos rivin määrä on rahallinen arvo, esimerkiksi työlisästä tai matkalaskusta, rivin määränä on `1,00` ja valuuttamäärä esitetään yksikköhinta-kolumnissa. | Amount | Kyllä  
F | **Yksikköhinta** | money | AHINTA |  Rivin yksikköhinta 2 desimaalin tarkkuudella. Desimaalierottimena käytetään pilkkua. Jos rivin määrä on rahallinen arvo, esimerkiksi työlisästä tai matkalaskusta, esitetään se tällä sarakkeella. Muutoin sarakkeen arvo on oletuksena tyhjä. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `UnitPrice` | _Lisätään automaattisesti, ei korvattavissa_ | Ei  
G | **Rivi yhteensä** | money | YHTEENSA |  Arvo esitetään 2 desimaalin tarkkuudella. Desimaalierottimena käytetään pilkkua. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `TotalPrice` | TotalPrice | Ei  
H | **Kirjanpitotili** | string (6) | TILI | Sarakkeen arvo voidaan asettaa poimintasäännön kentällä`VismaAccount` | VismaAccount | Ei  
I | **Kustannuspaikka** | string (20) | KPAIKKA | Arvo tulee henkilön Visma kustannuspaikka -tiedosta, joka voidaan määrittää henkilön tunnisteista. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `VismaCostCentre` | VismaCostCentre | Ei  
J | **Projekti** | string (20) | PROJEKTI | Ensimmäisen projektin projektikoodi. | ProjectCode1 | Ei  
K | **Tapahtuman päiväys** | date | PVM | Tapahtuman päiväys muodossa `yyyy-mm-dd`. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `SalaryRenderingDate`. | SalaryRenderingDate | Ei  
L | **Työnumero** | string | TYONRO |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä`VismaWorkOrder` | VismaWorkOrder | Ei  
M | **Tapahtuman selite** | string | SELITE |  Tieto tuodaan vain uudemmassa tiedostomallissa. Kirjatun tapahtuman kuvaus. Rajattu 50 merkkiin. | Comment | Ei  
N | **Työn vaativuusryhmä** | string | TVR |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `VismaWorkCompetenceGroup` | VismaWorkCompetenceGroup | Ei  
O | **Rivilaskuri** | integer | RIVI |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännöllä kentällä `VismaRowCounter` | VismaRowCounter | Ei  
P | **Valuutta** | string | VALUUTTA |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännöllä kentällä `VismaCurrency` | VismaCurrency | Ei  
Q | **Numero** | integer | NUMERO | Avain jolla linkitetään palkkakauden yläosa. Sarakkeen arvo voidaan asettaa poimintasäännöllä kentällä `VismaNovaSalaryRowNumber` | VismaNovaSalaryRowNumber | Kyllä  
R | **Palkkalajin selite** | string | PLAJISELITE |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `SalaryTypeDescription` | SalaryTypeDescription | Ei  
S | **Työnumero** | integer | TYONUMERO |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `VismaWorkNumber` | VismaWorkNumber | Ei  
T | **Työvaihe** | smallint | TYOVAIHE |  Tieto tuodaan vain uudemmassa tiedostomallissa. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `VismaWorkStep` | VismaWorkStep | Ei  
U | **Ansainta-ajan alkupvm** | date | AALKUPVM |  Tieto tuodaan vain uudemmassa tiedostomallissa. Arvo on oletuksena palkkakauden alkupäivämäärä, muodossa `yyyy-mm-dd`. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä`EarningPeriodStartDate` | EarningPeriodStartDate | Ei  
V | **Ansainta-ajan loppupvm** | date | ALOPPUPVM |  Tieto tuodaan vain uudemmassa tiedostomallissa. Arvo on oletuksena palkkakauden alkupäivämäärä, muodossa `yyyy-mm-dd`. Sarakkeen arvo voidaan asettaa poimintasäännön kentällä `EarningPeriodEndDate` | EarningPeriodEndDate | Ei
