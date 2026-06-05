---
id: 360014650697
title: Henkilötietojen tuonti - Sympa API
url: https://support.nepton.com/hc/fi/articles/360014650697-Henkil%C3%B6tietojen-tuonti-Sympa-API
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels:
- Person Import
promoted: false
updated_at: '2025-05-20T11:37:15Z'
edited_at: '2025-05-20T11:37:15Z'
---

# Henkilötietojen tuonti - Sympa API

Hakemalla henkilötietoja Sympa API:sta saadaan henkilötiedot päivitettyä Neptoniin useita kertoja päivässä. Sympa API:sta voidaan tuoda myös tiedot tulevista henkilötietojen muutoksista etukäteen.
Lisätietoa: [Henkilötietojen tuonti voimassa alkaen ja päättyen -tiedolla](<https://support.nepton.com/hc/articles/360015842238>)
## Käyttöönotto
Henkilötietojen siirto Sympan APIa hyödyntäen otetaan käyttöön määrittelemällä Sympaan tuotavan tiedon poimintasäännöt ja Neptoniin henkilötietojen noudon ajastus. Sympan poimintasäännöt määrittelee Sympan asiantuntija vakioidulla tavalla. Henkilötietojen noudon ajastuksen voit tehdä seuraavilla ohjeilla.
### Ajastuksen määritys
Käytä ajastetun tehtävän määrityksessä seuraavia valintoja. Lisäohjeet ajastettujen tehtävien lisäämisestä[ täältä](<https://support.nepton.com/hc/articles/360002489317>).
  * Merkistökoodaus: UTF-8
  * Tiedoston tyyppi: JSON
  * Henkilötuonnin tyyppi: Sympa HR Integraatio API
  * Autentikaatiotyyppi: Perus HTTP-autentikointi
  * REST API osoite: Sympan antama osoite
  * Parametri 1: Käyttäjätunnus - Nimi: "username", Arvo: "SympaltaSaatu_API_KEY"
  * Parametri 2: Salasana - Nimi: "password", Arvo: "SympaltaSaatu_Salainen_Avain"
  * Ajastus: Suosittelemme kerran päivässä klo 00:15 - 01:00 välillä.


### Siirrettävän tietomäärän rajoittaminen
Liittymän määrittelyssä on mahdollista rajata haettavaa tietoa. Tiedon rajaukset tehdään pääsääntöisesti Sympan puolella tiedon poiminnassa, mutta etenkin liittymän käyttöönottoprojektin aikana voi olla hyödyllistä rajata siirrettävää sisältöä. Tällä voidaan varmistua siirrettävän sisällön oikeellisuudesta, ennen kuin liittymässä siirretään tieto kaikkien työntekijöiden osalta.
Tiedon tuontia voidaan rajata ajastuksen määrityksen yhteydestä löytyvälllä, REST API -osoitteen komennoilla. Niissä komennoissa, joissa voidaan määritellä kentän nimi, voidaan käyttää mitä tahansa liittymän kentistä. Käytettävissä ovat seuraavat rajauksena käytettävät komennot. 
$top  
$skip  
$orderby  
$filter
Esimerkiksi, jos halutaan palauttaa liittymästä 5 henkilöä järjestettynä sukunimellä niin REST API -osoitteen komentoon lisätään hipsujen sisällä oleva teksti "/?$orderby=Sukunimi&$top=5". Tällöin määrittely REST API - osoitteeksi olisi 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21078997032349)
Alla on kuvattuna toiminnoittain komentojen käyttö
**Top**  
The query $top=XX will return the first XX matches to the query.  
Example:/?$top=200  
**Skip**  
The query $skip=XX will leave out the first XX matches to the query.  
Example: /?$skip=10  
Example: /?$skip=10&$top=10
**Order by**  
The query $orderby=somealias, someotheralias desc will sort the result set, primarily by the alias “somealias”, ascending, and  
secondarily by the alias “someotheralias”, descending.  
Example: /?$orderby=id  
Example: /?$orderby=id desc  
Example: /?$orderby=surname,age desc
**Filter**  
The following subset of OData filters are supported by the API.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/21078993525661)  
Filter examples by field type
  * All the field types can be filtered by null or by text  
api/testinterface?$filter=not (email eq null)  
api/testinterface?$filter=name eq 'no values'
  * Numeric field  
eq =equal, gt=greater than, lt = less than, ge=greater than or equal to, le=less than or equal to  
/?$filter=not (number eq null)  
/?$filter=number ge 0  
decimal number as filter  
/?$filter=number ge 1.14d
  * Dates  
eq =equal, gt=greater than, lt = less than, ge=greater than or equal to, le=less than or equal to  
/?$filter=not (date eq null)  
/?$filter=birthday gt 1980-12-17  
between api/testinterface?$filter=(date gt 2020-02-29) and (date lt 2020-03-02)
  * Timestamps  
Datacard's created and modified timestamps can also be used as filter.  
/?$filter=(modified gt 2015-12-31T23:59:59Z)  
Special case: If you don't specify the time, the timestamp is interpreted as T00:00:00, e.g:  
/?$filter=(created le 2014-01-01)  
comparison is done with timestamp 2014-01-01T00:00:00  
A good idea would be to always specify the time with the as a DateTime attribute.  
Note: Datacard's empty created date is shown "0001-01-01T00:00:00" but empty modified date is shown as "null"
  * Identification field  
Identification field can be used in filter as the "raw" numeric value, not the formatted value  
e.g. /?$filter=sympaID eq '123'  
Using values that are not numbers (e.g. sympaID eq 'a123') will give an error ("message": "Error with SQM query:  
MissingFilterField")


## Kentät ja kenttäryhmät
Henkilötietojen tuonnissa voi käyttää kaikkia [yleisen henkilötuonnin kenttiä](<https://support.nepton.com/hc/articles/360015933397>). Myös [henkilön lisätietokentät](<https://support.nepton.com/hc/fi/articles/360002430918>) saadaan tuotua, kun kentän nimi API:n datassa vastaa kentän nimeä Neptonissa. Voimassaoloja tukevat kentän arvot voidaan [siirtää voimassaolotiedoilla](<https://support.nepton.com/hc/articles/360015842238>) siirtämällä ne osana mitä tahansa kenttäryhmää, mutta suosittelemme käyttämään alla mainittuja kenttäryhmiä näiden kenttien osalta. Kaikki kentät eivät tällä hetkellä tue voimassaoloaikojen tallennusta, vaikka ne siirretään kenttäryhmissä voimassaolotiedoin. Tässä tapauksessa vain tuontihetkellä voimassaolevat tiedot tallennetaan - ks. tarkemmin kunkin kentän kuvauksesta. Kentät jotka tuodaan API:n datassa ilman voimassaolotietoja, tallennetaan [ilman voimassaoloja tuonnin säännöin](<https://support.nepton.com/hc/fi/articles/360015741097>).  
  
**Alla luetellut kentät on siirrettävä osana kenttäryhmää** , sillä ne sisältävät tiedon päättelyä.
Huom! Jos samaa kenttäryhmää tuodaan useammassa eri liittymässä, vain viimeisimmän tiedot jäävät voimaan, kaikki aiemmat rivit poistetaan.
**Kenttä** | **Kenttäryhmä** |  **Siirretään** **voimassaolo-tiedoilla** | **Kuvaus**  
---|---|---|---  
Ammattinimike |  Työsuhde_TAULUKKO |  X |   
Työaika prosentteina |  Työsuhde_TAULUKKO |  X |   
Työsuhteen alkupäivä |  Työsuhde_TAULUKKO |  |  Työsuhteen alkupäivän arvoista valitaan aikaisin, joka tallennetaan mikäli olemassa oleva arvo on myöhäisempi päivä tai tyhjä.  
Työsuhteen päättymispäivä |  Työsuhde_TAULUKKO |  |  Työsuhteen päättymispäivän arvoista tuodaan voimassaolojen mukaan viimeisin. Mikäli viimeisimpiä on useampia, valitaan päättymispäivän arvoista myöhäisin.  
Työajan asetusryhmä |  Asetusryhmä_TAULUKKO |  X |  [Lisätiedot](<https://support.nepton.com/hc/articles/360015933397>)  
Toissijaiset esimiehet |  Toissijaiset_esimiehet_TAULUKKO |  |  Toissijaisia esimiehiä voi tuoda useampia, yksi per kenttäryhmän rivi, jossa toissijaisen esimiehen henkilönumero ja voimassaolotiedot. Katso esimerkki alempaa vakioidun liittymän aineistoesimerkistä. Vain voimassaolevat esimiestiedot tallennetaan.  
Oletuskustannuspaikka |  Kustannuspaikka_TAULUKKO |  X |   
Organisaatiotaso1Koodi -  Organisaatiotaso10Koodi |  Organisaatio_TAULUKKO |  |  Nämä kymmenen kenttää kertovat mihin henkilöryhmään henkilö kuuluu. Kentät myös kuvaavat henkilöryhmähierarkian. Tasolta yksi löytyy hierarkian juurisolmut, joista katsoen ylemmät tasot kertovat näiden lapsisolmut. Näiden koodien lisäksi, tuonnin pitää sisältää koodeja vastaavat henkilöryhmien nimet. Katso Organisaatiotaso1Nimi - Organisaatiotaso10Nimi. Mikäli hierarkian mukaisia henkilöryhmiä ei ole vielä olemassa, luodaan nämä tuonnin yhteydessä. Vain voimassaolevat organisaatiotiedot tallennetaan.  
Organisaatiotaso1Nimi -  Organisaatiotaso10Nimi |  Organisaatio_TAULUKKO |  |  Nämä kymmenen kenttää kertovat mihin henkilöryhmään henkilö kuuluu. Kentät myös kuvaavat henkilöryhmähierarkian. Tasolta yksi löytyy hierarkian juurisolmut, joista katsoen ylemmät tasot kertovat näiden lapsisolmut. Näiden nimien lisäksi, tuonnin pitää sisältää nimiä vastaavat henkilöryhmien koodit. Katso Organisaatiotaso1Koodi - Organisaatiotaso10Koodi. Mikäli hierarkian mukaisia henkilöryhmiä ei ole vielä olemassa, luodaan nämä tuonnin yhteydessä. Vain voimassaolevat organisaatiotiedot tallennetaan.  
Näiden kenttäryhmien lisäksi voidaan käyttää lisätieto-taulukoita. Näitä taulukoita on 10 kpl ja niiden nimi on Lisatieto{1}_TAULUKKO, jossa aaltosulkeissa korvataan se taulukko jota täytetään. Näihin taulukoihin voidaan lisätä mitä tahansa sellaista tietoa, joiden voimassaolo on kaikille taulukkoon lisätyille tiedoille yhteinen. Esimerkiksi henkilön kuukausipalkan voisi tuoda sanomassa lisäämällä sinne taulukon 
"Lisatieto1_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Kuukausipalkka": "2700"  
}  
],
Mikäli Sympan tiedoissa kuukausipalkka sekä tehtävänimike jakaisivat saman voimassaolon, niin taulukko olisi seuraavanlainen
"Lisatieto1_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Kuukausipalkka": "2700",   
"Ammattinimike": "Hitsaaja"  
}  
],
### Voimassaoloaikojen päiväyksen muoto
"Voimassa alkaen"- ja "Voimassa päättyen"-kenttissä käytetään päivämäärämuotoa "YYYY-MM-DD".
## Vakioitu liittymä
Tämän ohjeen alussa mainitun vakioidun Sympa API liittymän kohdalla, siirretään vakiomutoinen siirtoainesto. Alla vakioidun liittymän siirtoaineiston kentät.
**Kenttä** | **Kenttäryhmä** |  **Siirretään** **voimassaolo-tiedoilla** | **Kuvaus**  
---|---|---|---  
Henkilönumero |  |  |  Toimii henkilön tunnisteena Sympan ja Neptonin välillä.  
Sukunimi |  |  |   
Kutsumanimi |  |  |  Etunimi jolla henkilöä kutsutaan. **Pakollinen kenttä** jota käytetään käyttäjätunnuksen luonnissa (Kutsumanimi Sukunimi).  
Etunimet |  |  |  Henkilön etunimet. Ei tällä hetkellä tallenneta Neptoniin, vaan etunimenä toimii sen sijaan "Kutsumanimi"-kenttä.  
Sähköposti |  |  |   
Puhelinnumero |  |  |   
Ensisijainen esimies |  |  |  Ensisijaisen esimiehen henkilönumero.  
IBAN |  |  |   
Katuosoite |  |  |   
Postinumero |  |  |   
Postitoimipaikka |  |  |   
RFID-tunniste |  |  |   
Yksiköt |  |  |  [Lisätiedot](<https://support.nepton.com/hc/articles/360015933397>)  
Rooli |  |  |  [Lisätiedot](<https://support.nepton.com/hc/articles/360015933397>) Vain uusille henkilöille roolin tyhjä arvo asetetaan Neptonissa "Työntekijä". Jos Sympasta tuodaan jo olemassa olevalle henkilölle rooli arvo tyhjänä, Nepton ei muuta henkilön roolia. Rooli tiedon tuomista tyhjänä ei suositella, sillä roolin tuonti tyhjällä arvolla aiheuttaa varoituksen henkilötuonnin tuloksiin.   
Työajan roolit |  |  |  [Lisätiedot](<https://support.nepton.com/hc/articles/360015933397>)  
Käyttäjätili käytössä |  |  |  [Lisätiedot](<https://support.nepton.com/hc/articles/360015933397>)  
Ammattinimike |  Työsuhde_TAULUKKO |  X |   
Työaika prosentteina |  Työsuhde_TAULUKKO |  X |   
Työsuhteen alkupäivä |  Työsuhde_TAULUKKO |  |  Työsuhteen alkupäivän arvoista valitaan aikaisin, joka tallennetaan mikäli Neptonissa olemassa oleva arvo on myöhäisempi päivä tai tyhjä. Jos tuodaan yksikin tyhjä arvo, Neptonissa oleva mahdollinen olemassaoleva työsuhteen alkupäivä tyhjennetään.  
Työsuhteen päättymispäivä |  Työsuhde_TAULUKKO |  |  Työsuhteen päättymispäivän arvoista tuodaan voimassaolojen mukaan viimeisin. Mikäli viimeisimpiä on useampia, valitaan päättymispäivän arvoista myöhäisin.  
Työajan asetusryhmä |  Asetusryhmä_TAULUKKO |  X |  [Lisätiedot](<https://support.nepton.com/hc/articles/360015933397>)  
Toissijaiset esimiehet |  Toissijaiset_esimiehet_TAULUKKO |  |  Toissijaisia esimiehiä voi tuoda useampia, yksi per kenttäryhmän rivi, jossa toissijaisen esimiehen henkilönumero ja voimassaolotiedot. Katso esimerkki alempaa vakioidun liittymän aineistoesimerkistä. Vain voimassaolevat esimiestiedot tallennetaan.  
Oletuskustannuspaikka |  Kustannuspaikka_TAULUKKO |  X |   
Organisaatiotaso1Koodi -  Organisaatiotaso10Koodi |  Organisaatio_TAULUKKO |  |  Nämä kymmenen kenttää kertovat mihin henkilöryhmään henkilö kuuluu. Kentät myös kuvaavat henkilöryhmähierarkian. Tasolta yksi löytyy hierarkian juurisolmut, joista katsoen ylemmät tasot kertovat näiden lapsisolmut. Näiden koodien lisäksi, tuonnin pitää sisältää koodeja vastaavat henkilöryhmien nimet. Katso Organisaatiotaso1Nimi - Organisaatiotaso10Nimi. Vain voimassaolevat organisaatiotiedot tallennetaan.  
Organisaatiotaso1Nimi -  Organisaatiotaso10Nimi |  Organisaatio_TAULUKKO |  |  Nämä kymmenen kenttää kertovat mihin henkilöryhmään henkilö kuuluu. Kentät myös kuvaavat henkilöryhmähierarkian. Tasolta yksi löytyy hierarkian juurisolmut, joista katsoen ylemmät tasot kertovat näiden lapsisolmut. Näiden nimien lisäksi, tuonnin pitää sisältää nimiä vastaavat henkilöryhmien koodit. Katso Organisaatiotaso1Koodi - Organisaatiotaso10Koodi. Vain voimassaolevat organisaatiotiedot tallennetaan.  
Toimipiste |  Organisaatio_TAULUKKO |  |  Kenttää ei tallenneta Neptoniin tällä hetkellä. Kenttä kertoo henkilön pääasiallisen työskentelypaikan.  
_FilterLiiketoimintayksikko |  |  |  Kenttää ei tallenneta Neptoniin. Kenttää käytetään Sympan puolella tiedon poiminnassa lähetysvaiheessa.  
_TESTUSER |  |  |  Kenttää ei tallenneta Neptoniin. Kenttää käytetään Sympan puolella tiedon poiminnassa lähetysvaiheessa.  
Muut tässä mainitsemattomat kentät |  |  |  Vakioidussa liittymän siirtoaineistossa on myös muita kenttiä, kuten kenttäryhmäkohtaisia "id" ja "Muokkaus päivä"-tietoja, mutta nämä eivät ole tuotavan tiedon kannalta olennaisia, vaan auttavat mahdollisissa erityistilanteiden selvittelyissä.  
### Vakioidun liittymän aineistoesimerkki
{  
"@odata.context": "<https://api.az-sympa.com/api/$metadata#NeptonKaikkiTiedot>",  
"value": [  
{  
"Henkilönumero": "123",  
"Kutsumanimi": "Erkki",  
"Etunimet": "Erkki Esko Eemeli",  
"Sähköposti": "maili@maili.com",  
"Puhelinnumero": "040 456 7890",  
"Ensisijainen esimies": "Esimerkki",  
"IBAN": "FI0453260051234567",  
"Katuosoite": "Katu 1",  
"Postinumero": "00000",  
"Postitoimipaikka": "Turku",  
"RFID-tunniste": "ABCDE123456",  
"Yksiköt": "Tuotekehitys",  
"Rooli": "Työntekijä",  
"Työajan roolit": "Työntekijät",  
"Käyttäjätili käytössä": "Kyllä",  
"_FilterLiiketoimintayksikko": "3",  
"_TESTUSER": false,  
"Työsuhde_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": "2020-10-13",  
"Ammattinimike": "Testaaja",  
"Työaika prosentteina": 80.0,  
"Työajan asetusryhmä": "1234"  
},  
{  
"Voimassa alkaen": "2020-10-14",  
"Voimassa päättyen": null,  
"Ammattinimike": "Ohjelmistokehittäjä",  
"Työaika prosentteina": 100.0,  
"Työajan asetusryhmä": "2456"  
}  
],  
"Kustannuspaikka_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Oletuskustannuspaikka": "103"  
"Toimipiste": "Kamppi"  
}  
],  
"Organisaatio_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Organisaatiotaso1Nimi": "Ohjelmistotalo Oy",  
"Organisaatiotaso2Nimi": "Turku",  
"Organisaatiotaso3Nimi": "Tuotekehitys",  
"Organisaatiotaso1Koodi": "10",  
"Organisaatiotaso2Koodi": "120",  
"Organisaatiotaso3Koodi": "1500"  
}  
],  
"Toissijaiset_esimiehet_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-09-15",  
"Voimassa päättyen": "2022-01-01",  
"Toissijaiset esimiehet": "1234"  
},  
{  
"Voimassa alkaen": "2016-01-01",  
"Voimassa päättyen": null,  
"Toissijaiset esimiehet": "4321"  
}  
],  
"Asetusryhmä_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Työajan asetusryhmä": "Liukuva työaika"  
}  
] }  
]  
}
## Kenttien arvojen tuonti ilman voimassaolotietoja
Mikäli siirrettävässä aineistossa ei määritellä tiedon voimassaoloja niin tuotava tieto käsitellään [ilman voimassaoloja](<https://support.nepton.com/hc/articles/360015741097>). Alla aineistoesimerkki siirrosta ilman voimassaolotietojen tuontia.
{  
"@odata.context": "<https://api.az-sympa.com/api/$metadata#NeptonKaikkiTiedot>",  
"value": [  
{  
"Henkilönumero": "123",  
"Käyttäjätunnus": "[esko.esimerkki@yritys.fi](<mailto:esko.esimerkki@yritys.fi>)",  
"Sukunimi": "Esimerkki",  
"Etunimi": "Esko",  
"Sähköposti": "[esko.esimerkki@yritys.fi](<mailto:esko.esimerkki@yritys.fi>)",  
"Ensisijainen esimies": "21",  
"Käyttäjätili käytössä": "Kyllä"  
}  
]  
}
## Kenttien arvojen tuonti voimassaolotiedoilla
Sympa API henkilötuonti tukee voimassaolojen siirtämistä osalle kentistä. Kun voimassaoloja tukeva kenttä, siirretään kenttäryhmän kenttänä, voidaan sille määritellä voimassaolot kenttäryhmän tiedoissa.
Tiedon tuonnissa kentät saavat voimassaolon kenttäryhmän 'Voimassa alkaen' ja 'Voimassa päättyen' kenttien mukaan. Katso lisätiedot voimassaolotietojen siirrosta [täältä](<https://support.nepton.com/hc/articles/360015842238>). Voimassaolovälit siirretään kenttäryhmien riveinä. Kenttäryhmän kentät voidaan myös halutessa, tuoda ilman voimassaolotietoja. Mikäli kenttäryhmä siirretään tyhjänä ilman yhtäkään riviä, kenttäryhmän kaikkien kenttien kaikki arvot poistetaan Neptonista. Alla aineistoesimerkki siirrosta voimassaolotiedoilla kenttäryhmän avulla.
{  
"@odata.context": "<https://api.az-sympa.com/api/$metadata#NeptonKaikkiTiedot>",  
"value": [  
{  
"Henkilönumero": "123",  
"Sukunimi": "Esimerkki",  
"Etunimi": "Esko",  
"**Työsuhde_TAULUKKO** ": [  
{  
"**Voimassa alkaen** ": "2020-06-02",  
"**Voimassa päättyen** ": "2020-10-13",  
"Ammattinimike": "Myyjä",  
"Työaika prosentteina": 80.0,  
"Työajan asetusryhmä": "1234"  
},  
{  
"Voimassa alkaen": "2020-10-14",  
"Voimassa päättyen": null,  
"Ammattinimike": "Myyntipäällikkö",  
"Työaika prosentteina": 100.0,  
"Työajan asetusryhmä": "2456"  
}  
]  
}  
]  
}
## Lisätietoja tuonnista
Nepton hakee henkilötiedot kutsumalla Sympa API:a. Sympa palauttaa henkilötiedot JSON-muodossa, noudattaen sisällön rakenteen osalta [OData Versio 4 standardia](<https://www.odata.org/getting-started/basic-tutorial/>). Tiedon poiminnan sisältö ja hakurajaukset määritellään Sympan käyttöliittymässä.
