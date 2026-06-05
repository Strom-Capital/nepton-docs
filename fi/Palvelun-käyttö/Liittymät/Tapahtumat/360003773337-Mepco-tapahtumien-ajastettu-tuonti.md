---
id: 360003773337
title: Mepco tapahtumien ajastettu tuonti
url: https://support.nepton.com/hc/fi/articles/360003773337-Mepco-tapahtumien-ajastettu-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels:
- S365
promoted: false
updated_at: '2024-11-14T11:00:01Z'
edited_at: '2024-11-14T11:00:01Z'
---

# Mepco tapahtumien ajastettu tuonti

Palveluun voidaan tuoda vain seuraavia tapahtumia Mepcosta: Koulutus, Lomautus, Vuosiloma, Työajan lyhennysvapaa, Saldovapaa, Pankkivapaa, Sairausloma, Poissaolo. Mepcon tapahtumien tuonnin asetukset Neptonissa tehdään: **Työaika - > Hallinta -> Työyhteisö / Asetusryhmät -> Liittymät -> Accountor Mepco HRM Poissaolojen tuonti**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21077991097245)
SFTP-palvelimelle tulee muodostaa csv-muotoinen aineisto kyseisestä tiedosta. Tuotavan aineiston tulee sisältää kaikki voimassa olevat tapahtumat siirrettävältä ajanjaksolta. Muodostettavan aineiston tulee tiedostonimessä sisältää luontihetken aikaleima.
Tuonti voidaan ajastaa tapahtumaan automaattisesti. Ajastukset löytyvät valikosta **Työaika - > Hallinta -> Työyhteisön asetukset -> Liittymät -> Ajastus **Ajastuksista voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>)
Tiedosto tallennetaan ISO-8859-1 koodauksella. Tietueet ovat erotettu puolipisteellä (`;`). Rivinvaihdon merkkinä on line feed (`LF`). Tämä rivinvaihto muodostuu oletuksena lähes kaikista tietojärjestelmistä.
Aineisto ei sisällä otsikkoriviä. Aineistossa yksi tapahtuma ja sen voimassaoloajat esitetään yhdellä rivillä.
Tapahtumien tuonti suoritetaan käyttöliittymässä määritellyllä käyttäjällä ja muutokset näkyvät palvelussa hänen tekemänään. Palvelu suorittaa tiedon poiston, muokkauksen ja lisäämisen alla olevassa järjestyksessä.
  1. Aineistosta puuttuvat tapahtumat poistetaan henkilön kalenterista, mikäli kalenterissa oleva tapahtuma on perustettu samalla käyttäjällä kuin siirtoa suoritetaan. Palveluun asetetaan se päivien määrä, jota siirrettävää aineistoa tulkitaan historiaan. Tätä päivien määrää verrataan tapahtuman päättymispäivään. Tapahtumat poistetaan siltä ajalta, milloin ne ovat voimassa henkilön kalenterissa päivitettävällä ajanjaksolla, ja eivät ole siirtoaineistossa. Tapahtuman on täten löydyttävä siirtotiedostosta koko sen voimassaoloajan lisättynä menneisyyteen päivitettävien päivien lukumäärällä. Mikäli aikarajaa ei ole asetettu käytetään arvona 0 päivää.
  2. Uudet tapahtumat lisätään henkilön kalentereihin siltä osin kuin ne puuttuvat sieltä. Siirrossa perustetaan ne aineistossa olevat tapahtumat, jotka alkavat määritellyn aikarajan jälkeen ja enintään 10 vuotta nykyhetkestä eteenpäin.
Esimerkiksi jos ajo tehdään 20.1. ja aikarajaksi on asetettu 20 päivää niin edellisenä vuonna voimassa olleita tapahtumia ei tuoda palveluun. Jos tapahtuma ajoittuu osittainkin tammikuulle niin tapahtuma lisätään kalenteriin. Tässä esimerkissä tapahtumat poistetaan 1.1. alkaen, jollei ne sisälly siirrettävään aineistoon.
  3. Päivitettävältä ajanjaksolta kalenterissa sekä aineistossa olevat tapahtumat säilyvät palvelussa.


## Tapahtumien kellonaikojen tulkinta
Peruskentät sisältävät poissaoloille ainoastaan alkamis- ja päättymispäivän. Peruskentillä lisättävän tapahtuman alkamis-, ja päättymisaika asetetaan seuraavasti:
  1. Jos päivällä on suunniteltu työvuoro tai oletetut työajat, lisätään poissaolon kelloajat sen alkamisen ja päättymisen perusteella. Huom! yövuorojen kohdalla asetus 'Työtapahtumien näyttö' (Työaika > Hallinta > Työyhteisön asetukset > Työtunnit) määrittää mille päivälle työvuoro tulkitaan kuuluvaksi. 
  2. asetetetaan aloituskellonajaksi 00:00 ja päättymiskellonajaksi 24:00


Valinnaisilla kentillä on mahdollista määrittää aloitus- ja lopetuskellonajat ja/tai kesto. Jos vaihtoehtoisten lisäkenttien avulla on ilmoitettu kesto, mutta ei alkamisaikaa sijoitetaan tapahtuma käyttäjän työpäivälle seuraavan kaavan mukaisesti:
  1. Jos henkilöllä ei kyseisellä päivällä ole yhtään tapahtumaa, Käytä 8:00 alkamisaikana
  2. Jos päivällä on avoin tapahtuma tai koko päivän kattava tapahtuma, käytä 8:00 alkamisaikana
  3. Jos päivän ensimmäinen tapahtuma alkaa vasta 12:00 tai myöhemmin ja tuotava tapahtuma on alle 5 tuntia, sijoita tuotava tapahtuma päivän alkuun
  4. Jos tuotavan tapahtuman sijoittaminen päivän loppuun ylittäisi 18:00 rajan ja se mahtuisi 8:00 ja päivän ensimmäisen tapahtuman väliin, sijoita se siihen
  5. Jos mikään edellämainituista ei osu kohdalleen, aloita tuotava tapahtuma päivän viimeisen tapahtuman jälkeen


## Aineiston kentät
Alla on luettelo aineiston perustietueista ja niiden lisätiedoista.
Sarake | Kenttä | Kuvaus  
---|---|---  
A | Sukunimi | Henkilön sukunimi. Nepton ei käytä tietoa tuonnissa.  
B | Etunimi | Henkilön etunimi. Nepton ei käytä tietoa tuonnissa.  
C | Henkilönumero | Henkilön Mepco-tunnus / henkilönumero  
D | Poissaolon alkamispvm | Tapahtuman alkamispäivämäärä, formaatti `YYYY-MM-DD` tai `DD.MM.YYYY`  
E | Poissaolon päättymispvm | Tapahtuman päättymispäivämäärä, formaatti `YYYY-MM-DD` tai `DD.MM.YYYY`  
F | Poissaolokoodi | Tapahtuman koodi. Lista tuetuista koodeista alempana. Jos koodia ei ole mainittu alempana eikä se oli koodi joka on mainittu koodeissa joita ei käsitellä, tuodaan tapahtuma oletuksena poissaolona.  
G | Poissaolon tyyppi | Mahdolliset arvot: 
  * **L** – loma
  * **P** – poissaolo.

Nepton ei käytä tietoa tuonnissa.  
H | Poissaolo palkallinen päivämäärään saakka | Tapahtuma palkallinen päivämäärään saakka. Jos tapahtuma päättyy myöhemmin kuin sen palkallisuus, Nepton jatkaa tapahtumaa palkattomalla merkinnällä. Tieto on tyhjä kokonaan palkattomilla tapahtumilla. Formaatti `YYYY-MM-DD` tai `DD.MM.YYYY`  
## Valinnaiset kentät
Valinnaiset kentät alla olevassa luettelossa eivät ole käytettävissä Mepcossa. Niiden tarkoitus on lisätä joustavuutta Mepco-muotoisen aineiston käyttöön muiden järjestelmien kanssa.
Sarake | Kenttä | Kuvaus  
---|---|---  
I | Poissaolon alkamisaika | Kellonaika milloin tapahtuma alkaa. Formaatti `HH:MM`  
J | Poissaolon päättymisaika | Kellonaika milloin tapahtuma päättyy. Formaatti `HH:MM`  
K | Poissaolo palkallinen kellonaikaan saakka | Kellonaika mihin asti tapahtuma on palkallinen. Jos tapahtuma päättyy myöhemmin kuin sen palkallisuus, Nepton jatkaa tapahtumaa palkattomalla merkinnällä. Tieto on tyhjä kokonaan palkattomilla tapahtumilla. Formaatti `HH:MM`  
L | Poissaolon pituus | Tapahtuman pituus tunteina ja minuutteina. Jos tämä tieto on annettu, se ohittaa sarakkeissa `J` ja `K` olevan tiedon. Formaatti `HH:MM`.  
## Tuetut koodit
Poissaolokoodi | Kuvaus  
---|---  
**4  
4.1  
4.2  
4.3  
4.4  
04  
04.1  
04.2  
04.3  
04.4** | Koulutus  
**5.0  
05.0** | Lomautus  
**6.1  
6.1.1  
6.3  
6.7  
6.8  
6.9  
06.1  
06.1.1  
06.3  
06.7  
06.8  
06.9** | Vuosiloma  
**6.2  
06.2** | Työajan lyhennysvapaa  
**6.5  
06.5** | Saldovapaa  
**6.6  
06.6** | Pankkivapaa  
**6.10** **06.10** **11.0** **11.3** **11.5** | Poissaolo, muu syy  
**8.0  
8.1  
8.2  
8.3  
8.4  
8.4.1  
8.5  
8.6  
08.0  
08.1  
08.2  
08.3  
08.4  
08.4.1  
08.5  
08.6** | Sairausloma  
**9.0  
9.1  
09.0  
09.1** | Sairausloma, työtapaturma  
**10.2  
10.10  
10.11  
010.2  
010.10  
010.11** | Poissaolo, vanhempainvapaa  
**10.3  
010.3** | Poissaolo, hoitovapaa  
**10.5  
010.5** | Sairausloma, lapsi sairas  
**10.55  
010.55** | Poissaolo, omaishoitovapaa  
**11.2  
011.2** | Poissaolo, opintovapaa  
**11.3.1  
011.3.1** | Poissaolo, poissaolo pakottavien perhesyiden takia  
**11.4  
011.4** | Poissaolo, vuorotteluvapaa  
**11.8  
011.8** | Poissaolo, ase- tai siviilipalvelusaika  
**11.9  
011.9** | Poissaolo, kertausharjoitukset  
**Tuntematon koodi (koodi jota ei  
ole määriteltytässä taulukossa tai   
poissaolokoodina, joita ei käsitellä)** | Poissaolo  
## Poissaolokoodit, joita ei käsitellä
Seuraavilla poissaolokoodeilla olevia tapahtumia ei tuoda Neptoniin.
  * 8.7
  * 10.4
  * 10.8
  * 13.1
  * 13.2
  * 08.7
  * 010.4
  * 010.8
  * 013.1
  * 013.2


## Esimerkkitiedostot
Esimerkkitiedosto ilman valinnaisia sarakkeita:
[code] 
    Esimerkki;Erika;1109;24.01.2014;24.01.2014;06.1;L;
    Hollola;Heidi;2404;01.10.2014;03.10.2014;08.0;P;
    Hollola;Heidi;2404;22.09.2014;26.09.2014;08.0;P;
    Hollola;Heidi;2404;22.10.2014;26.10.2014;010.3;P;
    Hollola;Heidi;2404;03.11.2014;05.11.2014;04.3;P;
    Hollola;Heidi;2404;06.11.2014;06.11.2014;06.6;P;06.11.2014
[/code]
Esimerkkitiedosto valinnaisilla sarakkeilla:
[code] 
    Esimerkki;Erika;1109;24.01.2014;25.01.2014;06.1;L;;;;;
    Hollola;Heidi;2404;01.10.2014;01.10.2014;08.0;P;01.10.2014;08:00;10:00;10:00;
    Hollola;Heidi;2404;22.09.2014;26.09.2014;08.0;P;;06:00;;;04:00
    
[/code]
