---
id: 9728029579165
title: Vakioidut liittymät BI-ratkaisuun
url: https://support.nepton.com/hc/fi/articles/9728029579165-Vakioidut-liittym%C3%A4t-BI-ratkaisuun
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laajat toteutukset
section_id: 4405119312657
section_path:
- Liittymät
- Laajat toteutukset
labels: []
promoted: false
updated_at: '2023-10-11T06:18:34Z'
edited_at: '2023-03-09T14:16:38Z'
---

# Vakioidut liittymät BI-ratkaisuun

Neptonista on mahdollista tuottaa tietoja Business Intelligence analysointia ja raportointia varten. Vakioituja liittymiä voidaan esimerkiksi käyttää [Greenstepin BI Book](<https://support.nepton.com/hc/fi/articles/4407929772433>) -palvelussa tai muissa BI palveluissa BI Book rajapinnan kautta. Tiedot on myös mahdollista hakea suoraan omaan BI-ratkaisuun.
Tiedot BI-ratkaisua varten tarjotaan [vakioitujen liittymien kautta](<https://support.nepton.com/hc/fi/sections/360000921798>), työtunnit tarjotaan vakioidussa muodossa joka on kuvattu alhaalla.
Esimerkiksi Greenstepin BI Book palvelu ja BI Book -rajapintapalvelu hyödyntää seuraavia Neptonista noudettavia tietoja:
  * Työtunnit, sisältäen työkirjauksilla käytetyt projektit. Tiedot haetaan [RunIntegrationRulesetV2](<https://support.nepton.com/hc/fi/articles/360014449458>) -liittymän kautta.
  * Koko projektipuun rakenne, [GetProjectsV2](<https://support.nepton.com/hc/fi/articles/6904062030621>) -liittymän kautta.
  * Kaikki käytettävissä olevat tapahtumatyypit, [GetActivityTypes](<https://support.nepton.com/hc/fi/articles/6899092915101>) -liittymän kautta.


Neptonista noudettuja tietoja on myös mahdollista täydentää muilla liittymillä tai muista järjestelmistä saatavilla tiedoilla, esimerkiksi:
  * Henkilötiedot Neptonista, esimerkiksi [henkilötietoliittymän](<https://support.nepton.com/hc/fi/articles/360004855857>) kautta.
  * Henkilötiedot muusta HR-järjestelmästä, esimerkiksi Sympa- tai Mepco-järjestelmästä.
  * Myyntiseurannan raportointitiedot, esimerkiksi Pipedrive-järjestelmästä.


Vietävä tieto BI-ratkaisuun on ns. raakaa rivitietoa, jota BI-ratkaisu käyttää analysointiin ja raportointiin. Asiakas tai BI-ratkaisun tarjoaja rakentaa tarvittavat raportit ja analytiikan BI-ratkaisuun.
Lisää tietoa ratkaisusta (Analytics Connector) voit kysyä [Neptonin yhteyshenkilöltäsi](<https://nepton.fi/yhteys/>).
## Työtuntien tiedostomuoto
Työtuntien tiedostomuotona käytetään [Mepcon palkkatapahtumien](<https://support.nepton.com/hc/fi/articles/360003473498>) tiedostomuotoa. Tiedot on ryhmitelty seuraavalla perusteella:
  * Kirjattu tapahtuma
  * Käytetty palkkalajikoodi
  * Päivä, jonka vuorolle tunnit kuuluvat (`SalaryRenderingDate`)
  * Tapahtuman 6 ensimmäistä monidimensioprojektia
  * Tapahtuman huomautus
  * Tapahtumatyypin koodi
  * Tapahtuman ylityökohdenteen perus- ja korotusosa


Vietävät sarakkeet ovat seuraavat:
Sarakenumero | Sarakkeen sisältö | Muoto | Kuvaus  
---|---|---|---  
1 | Henkilönumero | merkkijono |  Henkilön Mepco-tunniste tai henkilönumero, jos Mepco-kenttää ei ole asetettu Jos BI tietoja täydennetään henkilötiedoilla muista lähdejärjestelmistä, henkilönumeron tulee täsmätä muiden järjestelmien henkilönumeroiden kanssa.  
2 | Henkilön nimi | merkkijono |   
3 | Tapahtuman alkupvm | päivämäärä | Päiväysmuoto on päivämäärämuodon asetuksen mukaan, oletuksena `VVVV-KK-PP`  
4 | Tapahtuman päättymispvm | päivämäärä | Päiväysmuoto on päivämäärämuodon asetuksen mukaan, oletuksena `VVVV-KK-PP`  
5 | Määrä | desimaaliluku | Tuntien määrä tai esimerkiksi työlisän kappale- tai euromäärä. Piste desimaalierottimena, kaksi desimaalia. Esim. `12.50`  
6 | Palkkalajikoodi | merkkijono | Käytetyt palkkalajikoodit listattuna alempana olevassa taulukossa.  
7 | Projektikoodi 1 | merkkijono | Huom! Jos projektikoodia käytetään projektien tunnisteena, niiden tulee olla yksilöllisiä.  
8 | Projektikoodi 2 | merkkijono  
9 | Projektikoodi 3 | merkkijono  
10 | Projektikoodi 4 | merkkijono  
11 | Projektikoodi 5 | merkkijono  
12 | Sääntöjoukon säännön nimi | merkkijono |   
13 | Projektien Nepton-tunnukset | merkkijono | Kauttaviivoilla eroteltu lista Neptonin projektitunnuksista, esim: 1234/4342/5343  
14 | Ensimmäisen liitännäisprojektin projektitunnus | kokonaisluku |   
15 | Projektien nimet | merkkijono | Kauttaviivoilla eroteltu lista projektinimiä  
16 | Henkilön kustannusryhmän koodi | merkkijono |   
17 | Asetusryhmän koodi | merkkijono |   
18 | Rivin määrän yksikkö | merkki | Käytössä seuraavat yksiköt: 
  * `U` \- määrä yksikköinä/kokonaislukuna
  * `D` \- määrä desimaalilukuna
  * `S` \- määrä sekunteina
  * `H` \- määrä tunteina
  * `J` \- määrä päivinä
  * `C` \- valuuttamäärä, esimerkiksi euroina

  
19 | Tapahtumatyypin koodi | merkkijono |   
20 | Tapahtuman ylityön perusosan ja korotusosan kohdenne | merkkijono |  Kohdenteet erotettuna toisistaan putkimerkillä `|`. Seuraavat kohdenteet ovat mahdollisia:
  * `salary` \- palkkaan
  * `uncompensated` tai tyhjä - perusosaa tai korotusosaa ei korvata
  * `balance` \- työaikasaldoon
  * `bank` \- työaikapankkiin
  * `flexiblehours` \- joustokertymään
  * `overtimebalance` \- ylityökertymään
  * `worktimeshorteningleave` \- työajan lyhennysvapaa -kertymään
  * `annualabsence` \- vuosivapaakertymään
  * `flexibleworkhours` \- joustotyötunnitkertymään
  * `levellingperiodhours` \- tasoittumisjaksotunnit -kertymään

Arvo voisi esimerkiksi olla:
  * `balance|` \- tunti tunnista - saldo
  * `salary|salary` \- ylityö - palkkaan
  * `salary|bank` \- ylityö - perusosa: palkkaan, korotusosa: pankki

  
21 | Tapahtuman huomautus | merkkijono |   
22 | Raportin lisätieto | merkkijono | Työsuhde-osiossa asetettava henkilökohtainen raportin lisätieto.  
23 | Projektin 1 julkinen huomautus | merkkijono |   
24 | Projektin 1 sisäinen huomautus | merkkijono |   
25 | Projektin 2 julkinen huomautus | merkkijono | Projekti 2 on vain käytössä vain tunneilla, jotka on kirjattu yhtäaikaisesti useammalle projekteille.  
26 | Projektin 2 sisäinen huomautus | merkkijono  
## Palkkalajikoodit
Koodi | Kuvaus  
---|---  
NORM | Palkan perustunnit. Sisältää kertymävapaat ja kertymästä lainatun ajan. Ei sisällä sairauslomaa tai poissaoloja.  
MADALLETTU_NORM | Palkan perustunnit vähennetyllä palkalla.  
PALKATON | Palkaton aika. Ei sisällä sairauslomaa tai poissaoloja.  
LISATYO | Lisätyö  
YLIVRK50 | 50% vuorokautinen ylityö  
YLIVRK100 | 100% vuorokautinen ylityö  
YLIVIIKKO50 | 50% viikkoylityö  
YLIVIIKKO100 | 100% viikkoylityö  
YLISUNNUNTAI50 | 50% sunnuntaiylityö  
YLISUNNUNTAI100 | 100% sunnuntaiylityö  
YLI_YLITYO1 | Ylityö 1. Joissain pohjoismaissa käytetty ylityömääritys.  
YLI_YLITYO2 | Ylityö 2. Joissain pohjoismaissa käytetty ylityömääritys.  
LISATYO_TASOITTUMISJAKSO | Tasoittumisjaksolta kertynyt lisätyö.  
YLI50_TASOITTUMISJAKSO | Tasoittumisjaksolta kertynyt 50% ylityö.  
YLI100_TASOITTUMISJAKSO | Tasoittumisjaksolta kertynyt 100% ylityö.  
SAANNOLLISEN_YLITTAVA_AIKA_EI_KORVATA | Säännöllisen työajan ylittävä työaika jota ei korvata.  
VUOSILOMA_TUNTEINA | Pidetty vuosiloma tunteina.  
VIIKKOLEPOKORVAUS | Viikkolepokorvaus.  
PYHA | Työviikon pituutta lyhentävä juhlapyhä tunteina.  
KERTYMA_[NIMI] | Kaikkien kertymien loppupäivän saldo kertymän sisäisen nimen mukaan. Esimerkiksi palkkalajikoodi `KERTYMA_Balance` olisi työaikasaldon kertymän määrä.  
KERTYMAMUUTOS_[NIMI] | Kaikkien kertymien muutos päivänä kertymän sisäisen nimen mukaan. Esimerkiksi palkkalajikoodi `KERTYMAMUUTOS_Balance` olisi työaikasaldon muutos.  
RAAKALEIMA_[KOODI] | Kaikkien raakaleimojen tiedot tapahtumatyypin koodin mukaan. Esimerkiksi palkkalajikoodi `RAAKALEIMA_1` olisi työ-tapahtuman raakaleima.  
OLETETTU_TAI_KIRJATTU_LOUNAS | Lounastauko, oletettu tai kirjattu.  
PROJEKTIKIRJAUS_YLITTAA_TYOAJAN | Projektille kohdistettu aika, joka ylittää kirjatun työajan.  
R_[KOODI] | Työkorotukset koodin mukaan. Koodi haetaan työkorotuksen asetuksista. Palkkalajikoodi voisi esimerkiksi olla `R_224`.  
Rp_[KOODI] | Työkorotuksien korotusoasat koodin mukaan. Koodi haetaan työkorotuksen asetuksista. Palkkalajikoodi voisi esimerkiksi olla `Rp_224`.  
I_[KOODI] | Työlisät koodin mukaan. Koodi haetaan työlisän asetuksista. Palkkalajikoodi voisi esimerkiksi olla `I_224`.  
Ip_[KOODI] | Työlisien korotusoasat koodin mukaan. Koodi haetaan työlisän asetuksista. Palkkalajikoodi voisi esimerkiksi olla `Ip_224`.  
PALKATON_ITSESAIRAS | Palkaton sairausloma, henkilö itse sairas.  
PALKATON_LAPSISAIRAS | Palkaton sairausloma, lapsi sairas.  
PALKATON_TYOTAPATURMA_TOISSA | Palkaton sairausloma, työtapaturma töissä.  
PALKATON_TYOTAPATURMA_TYOMATKALLA | Palkaton sairausloma, työtapaturma työmatkalla.  
PALKATON_TAPATURMA_VAPAALLA | Palkaton sairausloma, tapaturma vapaa-ajalla.  
PALKALLINEN_ITSESAIRAS | Palkallinen sairausloma, henkilö itse sairas.  
PALKALLINEN_LAPSISAIRAS | Palkallinen sairausloma, lapsi sairas.  
PALKALLINEN_TYOTAPATURMA_TOISSA | Palkallinen sairausloma, työtapaturma töissä.  
PALKALLINEN_TYOTAPATURMA_TYOMATKALLA | Palkallinen sairausloma, työtapaturma työmatkalla.  
PALKALLINEN_TAPATURMA_VAPAALLA | Palkallinen sairausloma, tapaturma vapaa-ajalla.  
AMMATTIYHDISTYSTOIMINTA [PALKALLISUUS] |  Poissaolo palkallisuuden mukaan, tyyppinä ammattiyhdistystoiminta. Poissaolon palkallisuus tällä ja kaikilla alla olevilla poissaoloilla voi olla seuraava:
  * `BasicTime` \- palkallinen
  * `UnpaidBasicTime` \- palkaton

Palkkalajikoodi voisi esimerkiksi olla `AMMATTIYHDISTYSTOIMINTA BasicTime`.  
ASEPALVELUS [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä asepalvelus. Palkkalajikoodi voisi esimerkiksi olla `ASEPALVELUS BasicTime`.  
ERITYISAITIYSVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä erityisäitiysvapaa. Palkkalajikoodi voisi esimerkiksi olla `ERITYISAITIYSVAPAA BasicTime`.  
HOITOVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä hoitovapaa. Palkkalajikoodi voisi esimerkiksi olla `HOITOVAPAA BasicTime`.  
KERTAUS [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä kertaus. Palkkalajikoodi voisi esimerkiksi olla `KERTAUS BasicTime`.  
KUNTOUTUS [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä kuntoutus. Palkkalajikoodi voisi esimerkiksi olla `KUNTOUTUS BasicTime`.  
KUTSUNTA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä kutsunta. Palkkalajikoodi voisi esimerkiksi olla `KUTSUNTA BasicTime`.  
MUU_POISSAOLO [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä muu poissaolo. Palkkalajikoodi voisi esimerkiksi olla `MUU_POISSAOLO UnpaidBasicTime`.  
MUUTTOVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä muuttovapaa. Palkkalajikoodi voisi esimerkiksi olla `ASEPALVELUS BasicTime`.  
OMAT50_60_JUHLAT [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä omat 50v tai 60v juhlat. Palkkalajikoodi voisi esimerkiksi olla `MUUTTOVAPAA BasicTime`.  
PARISUHTEEN_REKISTEROINTI [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä parisuhteen rekisteröinti. Palkkalajikoodi voisi esimerkiksi olla `PARISUHTEEN_REKISTEROINTI BasicTime`.  
OPINTOVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä opintovapaa. Palkkalajikoodi voisi esimerkiksi olla `OPINTOVAPAA BasicTime`.  
OSA_AIKAELAKE [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä osa-aikaeläke. Palkkalajikoodi voisi esimerkiksi olla `OSA_AIKAELAKE BasicTime`.  
OSA-AIKAISUUS [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä osa-aikaisuus. Palkkalajikoodi voisi esimerkiksi olla `OSA-AIKAISUUS BasicTime`.  
PERHEENJASENEN_KUOLEMA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä perheenjäsenen kuolema. Palkkalajikoodi voisi esimerkiksi olla `PERHEENJASENEN_KUOLEMA BasicTime`.  
HAUTAJAISET [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä hautajaisen. Palkkalajikoodi voisi esimerkiksi olla `HAUTAJAISET BasicTime`.  
PERHEENJASENEN_SAIRASTUMINEN [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä perheenjäsenen sairastuminen. Palkkalajikoodi voisi esimerkiksi olla `PERHEENJASENEN_SAIRASTUMINEN BasicTime`.  
PAKOTTAVAT_PERHESYYT [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä pakottavat perhesyyt. Palkkalajikoodi voisi esimerkiksi olla `PAKOTTAVAT_PERHESYYT BasicTime`.  
TILAPAINEN_HOITOVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä tilapäinen hoitovapaa. Palkkalajikoodi voisi esimerkiksi olla `TILAPAINEN_HOITOVAPAA BasicTime`.  
TOIMIVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä toimivapaa. Palkkalajikoodi voisi esimerkiksi olla `TOIMIVAPAA BasicTime`.  
TYONTEKIJAN_PYYNTO [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä työntekijän pyyntö. Palkkalajikoodi voisi esimerkiksi olla `TYONTEKIJAN_PYYNTO BasicTime`.  
VANHEMPAINVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä vanhempainvapaa. Palkkalajikoodi voisi esimerkiksi olla `VANHEMPAINVAPAA BasicTime`.  
VIRKAPAVAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä virkavapaa. Palkkalajikoodi voisi esimerkiksi olla `VIRKAPAVAA BasicTime`.  
VUOROTTELUVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä vuorotteluvapaa. Palkkalajikoodi voisi esimerkiksi olla `VUOROTTELUVAPAA BasicTime`.  
AITIYSVAPAA [PALKALLISUUS] | Poissaolo palkallisuuden mukaan, tyyppinä äitiysvapaa. Palkkalajikoodi voisi esimerkiksi olla `AITIYSVAPAA BasicTime`.  
Poissaolo: [TUNNUS] - [PALKALLISUUS] | Muut kuin yllä listatut poissaolot sisäisen poissaolotunnuksen ja palkallisuuden mukaan. Palkkalajikoodi voisi esimerkiksi olla `Poissaolo: 412 - BasicTime`.  
NOT DEFINED | Määrittämätön palkkalaji
