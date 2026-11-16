---
id: 360015754117
title: Henkilötietojen tuonti Voimassa alkaen -tiedolla
url: https://support.nepton.com/hc/fi/articles/360015754117-Henkil%C3%B6tietojen-tuonti-Voimassa-alkaen-tiedolla
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tietojen voimassaolot henkilötuonneissa
section_id: 360004603778
section_path:
- Liittymät
- Henkilötiedot
- Tietojen voimassaolot henkilötuonneissa
labels: []
promoted: false
updated_at: '2026-06-26T09:56:55Z'
edited_at: '2026-06-26T09:52:43Z'
---

# Henkilötietojen tuonti Voimassa alkaen -tiedolla

Voimassa alkaen-tiedolla tuonti mahdollistaa tulevien henkilötietomuutoksien tuomisen etukäteen. Tuonnissa tuodaan henkilötietokenttien arvot sekä rivikohtainen "Voimassa alkaen"-tieto. 
Lisätietoa:
[Tietojen voimassaolot henkilötuonneissa](<https://support.nepton.com/hc/articles/360015807338>)  
[Henkilöiden tuonti](<https://support.nepton.com/hc/articles/360003762577>)  
[Henkilötuonnin kentät](<https://support.nepton.com/hc/articles/360015933397>)  
[Pakolliset henkilötietokentät](<https://support.nepton.com/hc/articles/360003762577-Person-Import#h_01F1F00HRZTD78QCZXSP1KE28P>)
## Voimassa alkaen-päiväyksen muoto
Päiväys on annettava muodossa PPKKVVVV, P.K.VVVV, PP/KK/VVVV, VVVVKKPP tai VVVV-KK-PP eli järjestyksessä päivä-kuukausi-vuosi tai vuosi-kuukausi-päivä. Välimerkkinä voi olla piste (.), viiva (-) tai kauttaviiva (/). Vuosiluku on annettava nelinumeroisena, kuukausi ja päivä on annettava kahdella numerolla. Välimerkkejä käytettäessä päivä ja kuukausi on mahdollista antaa myös yksinumeroisena. Mahdollisista poikkeuksista muotoon kerrotaan järjestelmäkohtaisissa ohjeissa.
Esim. 3. toukokuuta 2022:
  * 03052022
  * 3.5.2022
  * 03.05.2022
  * 3/05/2022
  * 2022-05-03
  * 20220503


## Aineistoesimerkki
Tietoja voidaan tuoda voimassa alkaen-tiedolla esimerkiksi [manuaalisella tuonnilla](<https://support.nepton.com/hc/articles/360018767498>) Excel-dokumentin avulla seuraavasti:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike | Voimassa alkaen  
---|---|---|---|---  
1234 | Esa | Esimerkki | Myyjä | 1.1.2019  
1234 | Esa | Esimerkki | Myyntipäällikkö | 1.1.2021  
## Tulevien henkilötietomuutoksien tuominen etukäteen
Mikäli tulevia henkilötietomuutoksia halutaan tuoda etukäteen toimi seuraavasti:
  * Lisää aineistoon yksi rivi per henkilö, jossa kenttien arvoina on tuontipäivänä voimassa oleva arvo
  * Lisää lisäksi samalle henkilölle yksi rivi per tulevaisuuden päivämäärä, jona jokin henkilötieto, joka tukee voimassaoloja muuttuu
    * Aseta "Voimassa alkaen"-tiedoksi muutoksen voimaantulopäivämäärä ilman kellonaikaa
    * Aseta voimassaoloja tukevien kenttien arvoiksi arvot, jotka ovat voimassa muutoksen voimaantulopäivämääränä
    * Aseta voimassaoloja tukemattomien kenttien arvoiksi tuontipäivänä voimassa oleva arvo


## Tuonti ilman tulevia muutoksia
Voimassa alkaen-tiedolla tuonti mahdollistaa varmemman henkilötietojen tuonnin kuin [henkilötietojen tuonti ilman voimassaoloja](<https://support.nepton.com/hc/articles/360015741097>). Mikäli tuontiaineisto tuodaankin Neptoniin myöhässä, sisältää tuontiaineisto myös tiedon siitä minä päivänä aineiston sisältämien muutosten oli tarkoitus tulla voimaan. Tästä syystä, vaikka tulevia henkilötietomuutoksia ei tuotaisikaan, saa tämän tuontitavan hyödyt käyttöön lisäämällä aineistoon rivin per henkilö, jossa kenttien arvoina on tuontipäivänä voimassa olevat arvot, sekä lisäämällä tuontiaineistoon "Voimassa alkaen"-tiedoksi tuontipäivän.
Lisätietoja henkilötuonnista:
[Henkilöiden tuonti](<https://support.nepton.com/hc/articles/360003762577>)
[Henkilötuonnin kentät](<https://support.nepton.com/hc/articles/360015933397>)
## Tietojen tallennuksen säännöt
Esitiedot:  
[Henkilötuonnin kentät](<https://support.nepton.com/hc/articles/360015933397>)  
[Pakolliset henkilötietokentät](<https://support.nepton.com/hc/articles/360003762577-Person-Import#h_01F1F00HRZTD78QCZXSP1KE28P>)
### Voimassaoloja tukevat kentät
Voimassaolojen tallennus eroaa voimassaoloja tukevien ja tukemattomien kenttien osalta. Voimassaoloja eivät tue kentät: "Ensisijainen esimies", "Toissijaiset esimiehet", "Työajan roolit", "Yksiköt", "Henkilöryhmä", "Oletusprojekti", "Saldo", sekä vaihtoehtoiset näitä tietoja tuovat kentät. Muut kentät tukevat voimassaoloja.
  * Voimassa alkaen -päivänä voimassaoleva arvo sekä mahdolliset tulevat arvot korvataan uudella arvolla, voimassa alkaen -päivästä alkaen
  * Tuotavat arvot eivät muuta voimassaoloja "Voimassa alkaen"-päivää edeltävältä ajalta
    * Poikkeuksena, jos aina pakollisella voimassaoloja tukevalla kentällä ei ole olemassa olevaa arvoa esim. uutta henkilöä lisättäessä, ulotetaan voimassaolo myös menneisyyteen
    * Pakollisia henkilön lisätietokenttiä käsitellään kuten valinnaisia kenttiä eli tuotava kenttä saa annetun alkuajan.
  * Samalle kentälle voi tuoda useita arvoja voimaantulopäivätiedon kanssa, lisäämällä aineistoon useita rivejä/solmuja eri "Voimassa alkaen"-päivällä
  * Jos "Voimassa alkaen"-päivä tieto on aineistossa, mutta sen arvo on tyhjä, korvataan kaikki olemassa olevat arvot uudella arvolla, siten että uusi arvo on aina voimassa. Jos tuontiaineistossa on arvoja myös "Voimassa alkaen"-päivän kanssa, tuodaan nämä tämän jälkeen.


### Voimassaoloja tukemattomat kentät
Voimassaolojen tallennus eroaa voimassaoloja tukevien ja tukemattomien kenttien osalta. Voimassaoloja eivät tue kentät: "Ensisijainen esimies", "Toissijaiset esimiehet", "Työajan roolit", "Yksiköt", "Henkilöryhmä", "Oletusprojekti", "Saldo", sekä vaihtoehtoiset näitä tietoja tuovat kentät. Muut kentät tukevat voimassaoloja.
  * Arvot tulevat voimaan tuontipäivänä ja ovat voimassa takautuvasti, vaikka rivillä olisikin voimassaolo-sarake
  * Jos tuontiaineistossa on useita rivejä/solmuja samalle henkilölle, jää myöhäisimmän "Voimassa alkaen"-päivän omaavan rivin/solmun arvo voimaan


HUOM!: Mikäli tuonnilla tuodaan tulevia arvoja, voimassaoloja tukemattomien kenttien arvoina pitää tuoda tuontihetkellä voimassaoleva arvo.
## Esimerkit
### Esimerkki: Uusi henkilö, tuontipäivä 1.1.2020
Tuontipäivä 1.1.2020, tuotava aineisto:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike | Henkilöryhmä | Voimassa alkaen  
---|---|---|---|---|---  
1234 | Esa | Esimerkki | Myyjä | Myynti | 1.1.2020  
1234 | Esa | Esimerkki | HR-asiantuntija | Myynti | 1.1.2021  
Tulos:
Kenttä | Selitys  
---|---  
Henkilönumero: 1234, alkaen 1.1.2020 | Voimassaoloja tukeva kenttä tuodaan voimassa alkaen päivän kanssa.  
Etunimi *: Esa | Voimassaoloja tukeva pakollinen kenttä. Ensimmäisen arvon voimassaolo ulotetaan menneisyyteen.  
Sukunimi *: Esimerkki | Sama kuin yllä.  
Ammattinimike: Myyjä, alkaen 1.1.2020, HR-asiantuntija, alkaen 1.1.2021 | Voimassaoloja tukeva kenttä. Arvot tuodaan kahdelta eri riviltä eri voimassa alkaen päivällä.  
Henkilöryhmä: Myynti | Voimassaoloja tukematon kenttä. Voimassaoloja tukemattomaan kenttään pitää aina tuoda tuontipäivänä voimassa oleva arvo.  
### Esimerkki: Henkilötietojen päivitys, tuontipäivä 16.1.2020
Alkutilanne:
Henkilönumero: 1234, alkaen 1.1.2020  
---  
Etunimi *: Esa  
Sukunimi *: Esimerkki  
Ammattinimike: Myyjä, alkaen 1.1.2020, HR-asiantuntija, alkaen 1.1.2021  
Henkilöryhmä: Myynti  
Tuontipäivä: 16.1.2020, tuotava aineisto:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike | Henkilöryhmä | Voimassa alkaen  
---|---|---|---|---|---  
1234 | Esa | Esimerkki | Myyjä | Myynti | 16.1.2020  
1234 | Esa | Esimerkki | Markkinointijohtaja | Myynti | 1.8.2020  
Tulos:
Kenttä | Selitys  
---|---  
Henkilönumero: 1234, alkaen 1.1.2020 | Arvo on sama, jolloin arvoa ei päivitetä.  
Etunimi *: Esa | Sama kuin yllä.  
Sukunimi *: Esimerkki | Sama kuin yllä.  
Ammattinimike: Myyjä, alkaen 1.1.2020, Markkinointijohtaja, alkaen 1.8.2020 | Voimassaoloja tukeva kenttä. Ensimmäinen arvo, "Myyjä", ei jo 16.1. voimassaolevana arvona muuta arvoja menneisyyteen. Toinen uusi arvo tulee voimaan voimassa alkaen päivästä korvaten muut tulevat arvot.  
Henkilöryhmä: Myynti | Voimassaoloja tukematon kenttä. Voimassaoloja tukemattomaan kenttään pitää aina tuoda tuontipäivänä voimassa oleva arvo.  
### Esimerkki: Henkilötietojen päivitys, tuontipäivä 23.1.2020
Alkutilanne:
Henkilönumero: 1234, alkaen 1.1.2020  
---  
Etunimi *: Esa  
Sukunimi *: Esimerkki  
Ammattinimike: Myyjä, alkaen 1.1.2020, Markkinointijohtaja, alkaen 1.8.2020  
Henkilöryhmä: Myynti  
Tuontipäivä: 23.1.2020, tuotava aineisto:
Henkilönumero | Etunimi | Sukunimi | Ammattinimike | Henkilöryhmä | Voimassa alkaen  
---|---|---|---|---|---  
1234 | Esa | Esimerkki | Ohjelmistokehittäjä | Tuotekehitys |   
1234 | Esa | Esimerkki | Testauspäällikkö | Tuotekehitys | 1.10.2020  
Tulos:
Kenttä | Selitys  
---|---  
Henkilönumero: 1234 | Ensimmäinen rivi ilman voimassa alkaen päivää tyhjentää voimassaolot. Toinen arvo on sama, jolloin arvoa ei päivitetä.  
Etunimi *: Esa | Sama kuin yllä.  
Sukunimi *: Esimerkki | Sama kuin yllä.  
Ammattinimike: Ohjelmistokehittäjä, Testauspäällikkö, alkaen 1.10.2020 | Voimassaoloja tukeva kenttä. Ensimmäinen rivi asettaa rivin arvon voimassa olevaksi aina. Toinen uusi arvo tulee voimaan voimassa alkaen päivästä.  
Henkilöryhmä: Tuotekehitys | Voimassaoloja tukematon kenttä. Voimassaoloja tukemattomaan kenttään pitää aina tuoda tuontipäivänä voimassa oleva arvo.
