---
id: 360002559018
title: Osa-aikaisuuden perustaminen
url: https://support.nepton.com/hc/fi/articles/360002559018-Osa-aikaisuuden-perustaminen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Esimerkkejä asetusryhmien perustamiseksi
section_id: 360001483898
section_path:
- Työajan laskenta ja hallinta
- Asetusryhmät
- Esimerkkejä asetusryhmien perustamiseksi
labels:
- NEPTONNEEDSREVIEW
- osatyöaika
promoted: false
updated_at: '2025-10-13T11:51:56Z'
edited_at: '2025-10-13T11:51:56Z'
---

# Osa-aikaisuuden perustaminen

## Osa-aikaisuuden määritelmä ja eri vaihtoehdot Neptonissa
Osa-aikaisilla henkilöillä tarkoitetaan sellaisia henkilöitä, jotka eivät työskentele täyttä tuntimäärää. Eri osa-aikaisuuden muotoja on neljä, vaikka eri työvelvoitteita osa-aikaisilla voi olla käytännössä loputon määrä.
Osa-aikaisuuden määrittämisen neljä vaihtoehtoa Neptonissa:
  * Työaikaprosentin hyödyntäminen - tutustu erilliseen työaikaprosentti-artikkeliin [täällä](<https://support.nepton.com/hc/fi/articles/360003961118>). 
  * Uusi asetusryhmä lyhennettyä päivää tekeville 
  * Uusi asetusryhmä epäsäännöllistä lyhennettyä viikkoa tekeville
  * Uusi asetusryhmä säännöllistä lyhennettyä työviikkoa tekeville. 


## Lyhennettyä päivää tekevät osa-aikaiset
Lyhennetty päivä tarkoittaa sellaista osa-aikaisuuden muotoa, jossa henkilö työskentelee samoina työpäivinä kuin työskentelisi kokoaikaisena, mutta tekee lyhyempiä työpäiviä. 
Esimerkki lyhennettyä päivää tekevästä osa-aikaisuuden muodosta:
Työyhteisön viikkotyöaika on 37,5h ja päivätyöaika 7,5h päivässä, maanantaista perjantaihin. 80% tuntimäärää tekevä, lyhennettyä päivää tekevä osa-aikainen työskentelee siis 30h viikossa, kuusi (6) tuntia päivässä, maanantaista perjantaihin. Työpäivät ovat samat kuin kokoaikaisella työntekijällä, työpäivän pituus on lyhyempi.
Tällainen osa-aikaisuus voidaan määrittää seuraavalla kahdella tavalla.
### Työaikaprosentti
Lyhennettyä päivää tekeville osa-aikaisille asetetaan tieto työaikaprosentista käyttämällä voimassaolotoimintoa. Tyhjä kenttä Työaikaprosentti-kentässä tulkitaan 100 % arvona eli täytenä työaikana. 
Kun työaikaprosentti on käytössä, laskee Nepton automaattisesti prosentin mukaisen vuorokautisen sekä viikoittaisen työajan asetusryhmän määritysten mukaan. Työaika lasketaan jakautuvan tasaisesti viikon työpäiville.
Poissaoloa sekä miinus- ja plussaldoa verrataan henkilön lyhennettyyn päivään ja korvataan henkilön työaikaprosenttiin suhteutettuna. Poissaolojen ja saldotuntien käsittely lyhennettyä päivää tekevillä on automaattista.
Lue lisää työaikaprosentista [täällä](<https://support.nepton.com/hc/fi/articles/360003961118>). 
### Uusi asetusryhmä lyhennettyä päivää tekeville 
Luodaan uusi asetusryhmä lyhennettyä työpäivää tekeville osa-aikaisille. Ohje uuden asetusryhmän luomiseen löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002557537>). Uusi asetusryhmä on suositeltavaa sijoittaa kokoaikaisten asetusryhmän alapuolelle, jotta samat työajan tulkintaan vaikuttavat asetukset periytyvät myös alemmalle tasolle osa-aikaisten asetusryhmään. Varmista, että uudessa osa-aikaisten asetusryhmässä on asetettu oikeat arvot Työpäivän pituudelle (ohje [täällä](<https://support.nepton.com/hc/fi/articles/360002558417>)) sekä Työviikon pituudelle (ohje [täällä](<https://support.nepton.com/hc/fi/articles/360002558537>)).
## Epäsäännöllistä lyhennettyä työviikkoa tekevät osa-aikaiset
Epäsäännöllinen lyhennetty viikko tarkoittaa, että henkilö työskentelee vain osan niistä työpäivistä, jotka hän työskentelisi ollessaan kokoaikainen. Epäsäännöllisessä viikossa työpäiviä ei ole ennalta sovittu, tai sovitut päivät vaihtelevat viikoittain.
Neptonissa epäsäännöllistä lyhennettyä työviikkoa tekevien osa-aikaisten työaikaa voidaan käsitellä kahdella tavalla, työaikaprosentilla tai perustamalla uusi asetusryhmä:
### Työaikaprosentti
  1. Epäsäännöllistä lyhennettyä viikkoa tekeville osa-aikaisille asetetaan tieto [työaikaprosentista](<https://support.nepton.com/hc/fi/articles/360003961118>), käyttämällä voimassaolotoimintoa. Kirjattua poissaoloa tai saldoa verrataan henkilön lyhennettyyn päivään ja korvataan henkilön työaikaprosentin mukaan. Viikon lopuksi korvattava poissaolon ja saldon määrä on oikein, jos työaikaprosentilla laskettu työviikon pituus on täyttynyt tai sitä ei ole ylitetty.  
  
Jos henkilö on poissa kokonaisen viikon, laskee Nepton koko viikolta miinussaldoa. Jos henkilö tekee seuraavalla viikolla kaksinkertaisen viikkotyömäärän, nollautuu edellisen viikon miinussaldot ja saldo tasaantuu.  
  
Alla olevan esimerkin henkilö tekee epäsäännöllistä 7,5h mittaista työviikkoa. Työaikaprosentin määrityksen mukaan Työpäivän pituus on 1 tunti 30 minuuttia ja Työviikon pituus 7 tuntia 30 minuuttia. Saldo on viikon alussa 0 minuuttia.


![mceclip1.png](https://support.nepton.com/hc/article_attachments/4408064280081)
  * Maanantaille on kirjattu työtapahtuma 08:00-10:30. Työaika sisältäen poissaolot on kaksi (2) tuntia (ruokatauko vähennetään). Työpäivän pituuden ollessa 1 tunti 30 minuuttia, saldoon lisätään 30 minuuttia.
  * Tiistaille ei ole kirjattu työtapahtumaa. Työpäivän pituus 1 tunti 30 minuuttia, joten saldosta vähennetään 1 tunti 30 minuuttia.
  * Keskiviikon työkirjaus on 08:00-10:30, joten työaika sisältäen poissaolot on kaksi (2) tuntia (ruokatauko vähennetään). Näin ollen saldoon lisätään 30 minuuttia (säännöllisen työajan ylittävän ajan osuus).
  * Torstaille ei ole kirjattu työtapahtumaa. Työpäivän pituus 1 tunti 30 minuuttia, joten saldosta vähennetään 1 tunti 30 minuuttia. Esimerkkihenkilön kokonaissaldo on torstain jälkeen miinuksella 2 tuntia.
  * Perjantain työkirjaus on 08:00-12:30. Työaika sisältäen poissaolot yhteensä neljä (4) tuntia (ruokatauko vähennetty). Työpäivän pituuden ollessa 1 tunti 30 minuuttia, saldoon lisätään 2 tuntia 30 minuuttia. Työviikon päätyttyä saldoa on siis kertynyt yhteensä 30 minuuttia. 


### Uusi asetusryhmä epäsäännöllistä lyhennettyä työviikkoa tekeville
Epäsäännöllistä lyhennettyä viikkoa tekeville osa-aikaisille voidaan vaihtoehtoisesti [luoda oma asetusryhmänsä.](<https://support.nepton.com/hc/fi/articles/360002558498>) Asetusryhmään määritellään henkilön [työpäivien pituudet](<https://support.nepton.com/hc/fi/articles/360002558417>) ja [työviikon pituus](<https://support.nepton.com/hc/fi/articles/360002558537>), tällöin henkilön työaikaprosenttia ei muuteta.  
  
Joka päivän pituudeksi määritellään sama pituus. Jotta työaikakalenteri osaa tulkita poissaolopäivän oikein niin, ettei henkilö saa siitä miinussaldoa, tulee lisäksi määrittää tapahtumatyyppi "Viikkovapaa" [oletetuksi tapahtumatyypiksi.](<https://support.nepton.com/hc/fi/articles/360002558717>) Tällöin tyhjille päiville tulee automaattisesti viikkovapaa-tapahtumatyyppi kuittaamaan kyseisen päivän työvelvoite.
Toisinaan voi olla tarve määrittää epäsäännöllistä lyhennettyä viikkoa tekeville osa-aikaisille voimaan asetus, joka vähentää vajaaksi jääneen työviikon toteutuneen ja työviikon säännöllisen työajan erotuksen saldosta. Alla esimerkki tilanteesta, jossa tällainen tulkinta voi olla tarpeellinen:
\- Henkilön on tarkoitus työskennellä neljänä päivänä viikossa 7,5h ja siten viikossa 30h (80 % työaika)  
\- Henkilölle muodostuu tämän toteutuksen mukaisesti yhdelle vapaapäivälle oletettuna tapahtumatyyppinä "Viikkovapaa", jolloin saldo ei vähene kyseiseltä päivältä  
\- Henkilö työskenteleekin poikkeuksellisesti **vain kolmena päivänä** (toteutunut työaika 22,50h) ja myös toiselle vapaapäivälle muodostuu saldomiinuksen estävä oletettu tapahtumatyyppi "Viikkovapaa"  
\- Henkilölle ei täten muodostu esimerkkiviikolta saldomiinusta, vaikka toteutunut työ 22,50h jää yhden työpäivän verran 7,5h vajaaksi viikon säännöllisestä työajasta 30h  
  
Mikäli henkilölle tulisi muodostua viikottaisen säännöllisen työajan täyttymättä jäämisen vuoksi yhden työpäivän verran saldomiinusta, asetus **"Täytä työviikon tunnit saldosta työviikon viimeisenä päivänä"** mahdollistaa yhden tekemättä jääneen työpäivän miinustamisen viikon päätteeksi saldosta. Asetus löytyy asetusryhmän asetuksista **Työtunnit - > Kertymät ja ylityötunnit -> Saldo**:  
  
![](https://support.nepton.com/hc/article_attachments/10022370148765)
Alla esimerkki työviikosta, jonka aikana on pidetty kaksi "ylimääräistä" vapaata:  
![MGOldDxMZi.jpg](https://support.nepton.com/hc/article_attachments/20219248505245)
## Säännöllistä lyhennettyä viikkoa tekevät osa-aikaiset
Säännöllinen lyhennetty viikko tarkoittaa, että henkilö työskentelee vain osan niistä työpäivistä, jotka hän työskentelisi ollessaan kokoaikainen. Säännöllisessä viikossa työpäivät ovat ennalta sovittu, eli henkilöllä on sovittu työrytmi.
Säännöllistä lyhennettyä työviikkoa tekeville osa-aikaisille [luodaan oma asetusryhmänsä.](<https://support.nepton.com/hc/fi/articles/360002558498>) Asetusryhmässä määritelty [työpäivien pituudet](<https://support.nepton.com/hc/fi/articles/360002558417>) ja [työviikon pituus](<https://support.nepton.com/hc/fi/articles/360002558537>) ovat laskennan perusteena, kun käsitellään säännöllistä työaikaa, poissaoloja tai arkipyhiä. Luodessa asetusryhmää, se asetetaan alaryhmäksi sille ryhmälle, josta muiden asetusten halutaan periytyvän uudelle asetusryhmälle. Asetusryhmälle määritellään:
  * Työpäivän pituudet määritellään sovitun pituisiksi ja päivät, jotka eivät ole työpäiviä, määritellään 0 minuutin mittaiseksi.
  * Työviikon pituus määritellään osa-aikaisuuden mukaiseksi.


Asetusryhmän luomisen jälkeen on hyvä tarkistaa testaamalla, miten ylemmältä asetusryhmätasolta periytyvät juhlapyhä- ja vuosiloma-asetukset toimivat käytännössä uudessa osa-aikaisten asetusryhmässä. Osa-aikaisille saattaa olla tarpeellista tehdä poikkeavia määrityksiä, jolloin tarvittavat ohjeet löytyvät artikkeleista [Juhla- ja arkipyhien käsittely](<https://support.nepton.com/hc/fi/articles/360002558797>) ja [Vuosiloman ansainnan asetukset](<https://support.nepton.com/hc/fi/articles/360002560698>). 
## Huomioitavaa vuosilomien tulkinnassa, kun henkilöllä on päiviä ilman työvelvoitetta
Epäsäännöllistä lyhennettyä työviikkoa tekeville merkitään todennäköisesti osalle työpäivistä velvoitteeksi nolla minuuttia eli henkilöillä on päiviä, joilla ei ole työvelvoitetta. Nämä päivät ovat huomioitava vuosilomien kohdalla, sillä vuosilomaa ei kulu, mikäli työpäivällä ei ole velvoitetta. Tutustu erilliseen vuosiloman ansainnan ohjeeseen [täällä](<https://support.nepton.com/hc/fi/articles/360002560698>), ohjeen kohdassa 4.4.
## Henkilön työaika kun vuorosuunnittelu on käytössä
Henkilön työvelvoite voi muodostua myös [vuorosuunnitelmasta.](<https://support.nepton.com/hc/fi/articles/360010081678>) Tällöin ei tehdä uutta asetusryhmää, vaan julkaistu vuorolista on poissaolo- ja työpäivien laskennan perusteena. Määrittelemällä työsuhdeosiosta henkilön [viikoittaisen työajan minimi- ja maksimivelvoitteet](<https://support.nepton.com/hc/fi/articles/360004769718>), määritellään kuinka monta tuntia henkilö voi tehdä töitä viikossa. Minimi- ja maksimivelvoitteita voidaan käyttää työvuorosuunnittelussa tavoitelukuina tukemaan suunnittelua.
## Työviikon velvoitteen muuttuminen kesken työviikon
Mikäli henkilön työviikon velvoite muuttuu kesken työviikon, ei palvelu automaattisesti tunnista, kumpaako työajan velvoitetta sen tulisi laskennassaan noudattaa. Tästä johtuen työviikon oikea pituus on laskettava ja syötettävä manuaalisella poikkeusasetuksella työviikon pituudeksi.
Esimerkiksi: henkilö tekee 80% työaikaa maanantaista keskiviikkoon, työpäivän pituus on 6h/päivä. Torstaista alkaen henkilö palaa tekemään täyttä työaikaa (työvelvoite on 100%), joten työpäivän pituus on 7,5h/päivä torstaina ja perjantaina.
Laske siis yhteen työpäivien tuntivelvoite saadaksesi koko työviikolle työvelvoite, edeltävän esimerkin mukaisesti näin:
Maanantai - Keskiviikko: 3 x 6h = 18h
Torstai - Perjantai: 2 x 7,5h = 15h 
Työviikon kokonaisvelvoite on siis 33h, kun työvelvoite on muuttunut kesken työviikon. 
Työviikon kokonaisvelvoitteen poikkeuksen voit asettaa painamalla päivämääräkuvaketta henkilön työajan kalenterissa ja valitsemalla Työviikon pituus. Uuteen ikkunaan aukeaa ''Kirjaa poikkeus''-näkymä, johon voi asettaa työviikon pituudelle poikkeusasetuksen.
![](https://support.nepton.com/hc/article_attachments/19986693876637)
## Asetuksien tekeminen asetusryhmiin takautuvasti
Jos muutoksia tehdään takautuvasti asetusryhmiin, ei henkilön tapahtumat ja kertymien kokonaisarvot välttämättä ole muutoksen jälkeen ajan tasalla työaikakalenterissa. Tästä saattaa hälyttää henkilön kalenterissa keltainen huomiokolmio. Näissä tapauksissa on manuaalisesti päivitettävä henkilö(ide)n työajan kalenterit ajan tasalle. Takautuvassa asetusmuutoksessa huomioitavista toimenpiteistä on kerrottu tarkemmin ohjeessa: [Takautuva asetusmuutos ja kertymän arvon uudelleenlasketus. ](<https://support.nepton.com/hc/fi/articles/4411220910865>)
