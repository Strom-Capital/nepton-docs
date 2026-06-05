---
id: 360003751058
title: Projektien tuonti - Visma L7/LTR
url: https://support.nepton.com/hc/fi/articles/360003751058-Projektien-tuonti-Visma-L7-LTR
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Projektit
section_id: 360001075297
section_path:
- Liittymät
- Projektit
labels: []
promoted: false
updated_at: '2024-08-23T08:51:50Z'
edited_at: '2024-03-20T09:58:44Z'
---

# Projektien tuonti - Visma L7/LTR

Palveluun voidaan tuoda projekteja Visma L7 -palvelusta. Tuonnissa käytetään Visman tarjoamaa REST rajapintaa.
Visma L7:ssä olevat projektit ovat kolmessa tasossa:
  1. Yritysnumero
  2. Ylänumero
  3. Alanumero


Esimerkiksi
  * 100001 - Yritys Oy  

    * 5432 - Tuotekehitys  

      * 110205 - Ohjelmointi


Yritysnumeron tuominen Neptoniin on valinnaista ja sen voi määrittää asetuksista. Tästä lisää alempana.
Huomioi että jos olet vaihtamassa tuontia vanhasta SFTP-tuonnista uuteen REST - rajapintaan, tulee SFTP -tuonti ajaa yhden kerran ennen rajapinnan vaihtoa, jotta projektien tunnisteet päivittyvät niin että ne tukevat REST - rajapintaa oikein.
Mikäli projekti on jo palvelussa, päivitetään sen tietoja. Mikäli projektin (alanumeron) tila (`orderStatus` -tieto) on arvoltaan jokin muu kuin 8 (valmis) tai 9 (lukittu), projektin päättymispäivä asetetaan tuotavilla projekteilla tyhjäksi, jotta tuodut projektit ovat käytettävissä tapahtumilla. Projektin alkupäivä asetetaan tyhjäksi tuonnin yhteydessä.
## Määrittäminen
**1\. Perusasetusten määrittäminen**
Tuonnin perusasetukset pystyy määrittämään työyhteisön asetuksista, **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Projektit > Visma L7 projektien tuonti**.
![](https://support.nepton.com/hc/article_attachments/17494420521373)
Vähintään seuraavat tiedot täytyy määrittää jotta projektit pystytään tuomaan Visma L7 rajapinnasta:
Asetuksen nimi | Lisätiedot  
---|---  
Rajapinta-asetukset > Henkilö, joka näytetään projektien luojana | Käyttäjätunnus, joka toimii integraation suorittajana. Esimerkiksi valittu käyttäjä kirjataan henkilöksi joka on asettanut projektipäälliköt (Huom! jos käytät vielä vanhaa SFTP-toteutusta, ensimmäinen rivi määrittää tälle siirtotavalle käytettävän henkilön.  
Rajapinta-asetukset > Tuonnin web service -osoite |  Projektit haetaan käyttäen kahta eri päätepistettä, `/projects/` (GET) ja `/salesorders/` (GET). Jos päätepisteet ovat esimerkiksi seuraavat:
  * https://rajapinnan.verkkotunnus.com/ltrws/REST/L7/projects/
  * https://rajapinnan.verkkotunnus.com/ltrws/REST/L7/salesorders/

Tuonnin web service -osoitteeksi tulee antaa: https://rajapinnan.verkkotunnus.com/ltrws/REST/L7/  
Rajapinta-asetukset > Yrityksen hash (company hash) | Toimii yrityksen tunnisteena  
Rajapinta-asetukset > API token (user token) | Valtuutusavaimen tunnus  
Jos et tiedä mitä seuraaviin tietoihin pitäisi antaa:
  * Rajapinta-asetukset > Tuonnin web service -osoite
  * Rajapinta-asetukset > Yrityksen hash (company hash)
  * Rajapinta-asetukset > API token (user token)


Ole yhteydessä Visma-tukihenkilöösi.
Tämän lisäksi seuraavat tiedot on mahdollista määrittää:
Asetuksen nimi | Lisätiedot  
---|---  
Yrityskoodia käytetään juuriprojektina |  Tuodaanko rajapinnasta löytyvä yritysnumero ylänumeroiden yliprojektiksi vai ei. Tämä vaikuttaa myös projektikoodin muodostumiseen. Projektikoodi muodostetaan:
  * Yritysnumerosta, jos yritysnumerot tuodaan projekteiksi
  * Ylänumerosta
  * Alanumerosta

Alla esimerkit projektikoodeista:
  * Ylänumero ilman yritysnumeroa: 110205
  * Ylänumero yritysnumerolla: 100001/110205
  * Alanumero ilman yritysnumeroa: 110205/5432
  * Alanumero yritysnumerolla: 100001/110205/5432

  
Tuo projektityypit |  Tuodaanko alanumeroiden tyypit projektityypeiksi Neptoniin vai ei. Tyypit tuodaan nimellä. Jos projektityyppejä ei tuoda, käytetty tyyppi on "Projektit". Ylänumerot ja yritysnumerot tuodaan aina tyyppinä "Projektit".  
Tuo projektipäälliköt | Tuodaanko ylänumeroiden projektipäälliköt vai ei. Tätä varten projektipäälliköiden Visma-tunnisteet tai henkilönumerot tarvitsee määrittää.  
Lisää kustannuspaikka tuodun projektin koodiin |  Lisätäänkö projektin Visma L7:n alanumeron kustannuspaikka tuodun projektin koodiin.  Esimerkki projektista jonka ylänumero on 110205, alanumero 5432 ja kustannuspaikka 1001
  * Koodi ilman kustannuspaikkaa (Asetus ei ole päällä): 110205/5432
  * Koodi kustannuspaikan kanssa (Asetus on päällä): 110205/5432/1001

  
Rajapinta-asetukset > Tuotujen projektien yliprojekti | Tuodaanko koko Visma L7 projektipuu valitun yliprojektin alle vai ei. Jos mitään projektia ei ole valittuna, L7 projektit tuodaan juuritasolle.  
Projektien tuonti on myös mahdollista useammasta lähteestä. Jokaiselle lähteelle asetetaan oma:
  * Tuonnin web service -osoite
  * Yrityksen hash
  * API token
  * Tuotujen projektien yliprojekti
  * Henkilö, joka näytetään projektien luojana


Tätä käytettäessä tulee varmistaa, että yritysnumerot tai ylänumerot ovat uniikkeja. Muutoin toinen lähde voi ylikirjoittaa ensimmäisestä lähteestä tuotuja projekteja.
**2\. Henkilöiden tunnusten määrittäminen**
Jos rajapinnan kautta halutaan myös asettaa projektipäälliköt, täytyy henkilöiden tunnisteet määrittää _Työsuhde > Henkilön tiedot > Tunnisteet_ -näkymässä. Jos henkilön Visma -tunnusta ei ole asetettu, käytetään henkilön henkilönumeroa.
## Liittymän tekninen toiminta
### Rajaukset
  * Jos yritysnumerot on asetettu tuotavaksi, yritysnumeroa tyhjällä numerolla ei tuoda. Jos yritysnumeroa ei tuoda, sen ylä- tai alanumeroakaan ei tuoda.
  * Ylänumeroita tyhjällä numerolla ei tuoda. Jos ylänumeroa ei tuoda, sen alanumeroakaan ei tuoda.,
  * Alanumeroita tyhjällä numerolla ei tuoda


### Autentikaatio
Yrityksen hash ja API-token lähetetään HTTP-otsakkeessa. Yrityksen hash lähetetään HTTP-otsakkeena `hash` ja API token HTTP-otsakkeena `token`.
### Rajapinta tuonnin ajastus
Ajastusasetukset löytyvät kohdasta **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Ajastus**.
Visma L7 liittymän ajastus on mahdollista tehdä joko minuuttiajastuksella (esim. 15 minuutin välein, joka tunti jne.) tai päivittäisajastuksella. Rajapinnasta tuontia varten valitse liittymävalikosta jokin 'Visma L7 projektien tuonti #{numero} valinnoista. Valikosta löytyy oma valintansa jokaiselle erikseen määritetylle rajapintariville. Joudut tällöin määrittämään ajastuksen jokaiselle rajapintariville, mutta tarvittaessa voit myös määrittää erillisen aikataulun jollekin näistä.
Ajastuksien määrittelystä lisää voit lukea [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>).
### Odotettu vastaus rajapinnasta
#### /projects/ päätepiste
Vastauksen odotetaan olevan JSON-muodossa. Tätä varten myös lähetetään HTTP-otsake `Accept: application/json`.
Päätepistettä käytetään vain ylänumeroiden tuontiin. Alanumerot tuodaan /salesorder/ päätepisteestä.
Taso | Kentän nimi | Muoto | Selite  
---|---|---|---  
Juuri | _project_ | Joukko projektitietoja (ylänumeroita) |   
Projektitietojen joukko | _rec_ | numero | Tietueen numeerinen tunnus. Tietoa ei käytetä Neptonissa.  
Projektitietojen joukko | _mainNumber_ | merkkijono | Ylänumeron projektikoodi  
Projektitietojen joukko | _mainNumberName_ | merkkijono | Ylänumeron projektin nimi  
Projektitietojen joukko | _mainNumbercostCentre_ | merkkijono | Ylänumeron kustannuspaikka. Tietoa ei käytetä.  
Projektitietojen joukko | _mainNumbercostCentreName_ | merkkijono | Ylänumeron kustannuspaikan nimi.  
Tietoa ei käytetä.  
Projektitietojen joukko | _mainNumbersalesMan_ | merkkijono | Projektipäällikön Visma-tunnus / henkilönumero.  
Projektitietojen joukko | _mainNumbersalesManName_ | merkkijono | Projektipäällikön nimi. Tietoa ei käytetä.  
Projektitietojen joukko | _mainNumberworkQuality_ | merkkijono | Tietoa ei käytetä.  
Projektitietojen joukko | _mainNumberworkQualityName_ | merkkijono | Tietoa ei käytetä.  
Projektitietojen joukko | _subNumber_ | merkkijono | Alanumeron projektikoodi. Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberName_ | merkkijono | Alanumeron projektin nimi.  
Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberCostCentre_ | merkkijono | Alanumeron kustannuspaikka. Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberCostCentreName_ | merkkijono | Alanumeron kustannuspaikan nimi.  
Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberType_ | merkkijono | Alanumeron tyyppi.  
Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberTypeName_ | merkkijono | Alanumeron tyypin nimi.  
Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberOrderDate_ | merkkijono | Alanumeron tilauspäivä.  
Tietoa ei käytetä.  
Projektitietojen joukko | _subNumberStatus_ | merkki | Alanumeron tila.  
Tietoa ei käytetä.  
Projektitietojen joukko | _partyByNumber_ | merkkijono | Yritysnumero. Tuodaan projektin koodina jos yrityskoodi tuodaan ylänumeroiden yliprojektiksi.  
Projektitietojen joukko | _partyByBusinessId_ | merkkijono | Yrityksen y-tunnus.  
Tietoa ei käytetä.  
Projektitietojen joukko | _partyByName1_ | merkkijono | Yrityksen nimi. Tuodaan projektin nimenä jos yrityskoodi tuodaan ylänumeroiden yliprojektiksi.  
Projektitietojen joukko | _modifiedTs_ | päivämäärä | Tietoa ei käytetä.  
Projektitietojen joukko | _deleted  
_ | merkki | Onko ylänumero poistettu vai ei (1 = Kyllä, 0 = ei).  
Poistettua ylänumeroa ei lisätä uutena projektina.  
**Esimerkkisanoma**
[code] 
    {  
      "project": [  
        {  
          "rec": "1",  
          "mainNumber": "000001",  
          "mainNumberName": "Turku",  
          "mainNumbercostCentre": "1000",  
          "mainNumbercostCentreName": "MYYNTI",  
          "mainNumbersalesMan": "5000",  
          "mainNumbersalesManName": "Matti Myyjä",  
          "mainNumberworkQuality": "",  
          "mainNumberworkQualityName": "",  
          "subNumber": "1",  
          "subNumberName": "Projektin aloitustyö",  
          "subNumberCostCentre": "1000",  
          "subNumberCostCentreName": "MYYNTI",  
          "subNumberType": "1001",  
          "subNumberTypeName": "Myyntitilaus",  
          "subNumberOrderDate": "",  
          "partyByNumber": "100027",  
          "partyByBusinessId": "1234567-7",  
          "partyByName1": "Yritys Oy",  
          "deleted": "0"  
        }  
      ]  
    }
[/code]
#### /salesorders/ päätepiste
Vastauksen odotetaan olevan JSON-muodossa. Tätä varten myös lähetetään HTTP-otsake `Accept: application/json`.
Taso | Kentän nimi | Muoto | Selite  
---|---|---|---  
Juuri | _salesorder_ | Joukko myyntitilauksia (alanumeroita) |   
Myyntitilauksien joukko | _rec_ | numero | Tietueen numeerinen tunnus. Tietoa ei käytetä Neptonissa.  
Myyntitilauksien joukko | _orderNumber_ | merkkijono | Ylänumeron projektikoodi.  
Myyntitilauksien joukko | _subNumber_ | merkkijono | Alanumeron projektikoodi.  
Myyntitilauksien joukko | _orderType_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _orderTypeName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _orderName_ | merkkijono | Alanumeron projektin nimi.  
Myyntitilauksien joukko | _currency_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _costCentre_ | merkkijono | Alanumeron kustannuspaikka.  
Tieto lisätään tuodun projektin koodiin jos asetus "Lisää kustannuspaikka tuodun projektin koodiin" on päällä.  
Myyntitilauksien joukko | _orderDate_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _deliveryDate_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _paymentTerms_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _deliveryTermsCode_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _deliveryTerms_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _deliveryMethodCode_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _deliveryMethod_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _orderStatus_ | merkki | Alanumeron tila. Jos tilana on 8 tai 9, tai alanumero on poistettu ja projektilla ei vielä ole päättymispäivää, päättymispäiväksi asetetaan nykyinen päivä.  
Myyntitilauksien joukko | _mainOrderType_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _mainOrderTypeName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _mainOrderCostCentre_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _mainOrderCostCentreName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1Rec_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1Type_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1BusinessId_ | merkkijono | Yrityksen y-tunnus.  
Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1CompanyNumber_ | merkkijono | Yritysnumero. Tuodaan projektin koodina jos yrityskoodi tuodaan ylänumeroiden yliprojektiksi.  
Myyntitilauksien joukko | _party1Name1_ | merkkijono | Yrityksen nimi. Tuodaan projektin nimenä jos yrityskoodi tuodaan ylänumeroiden yliprojektiksi.  
Myyntitilauksien joukko | _party1Name2_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1visitAddress_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1postalAddress_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1postalZip_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1postalCity_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1countryCode_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1countryName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1PersonName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1ContactNumber1_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party1ContactNumber2_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2Rec_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2Type_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2BusinessId_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2CompanyNumber_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2Name1_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2Name2_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2visitAddress_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2postalAddress_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2postalZip_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2postalCity_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2countryCode_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2countryName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2PersonName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2ContactNumber1_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _party2ContactNumber2_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _subNrStatus_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _projectWorkQuality_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _orderNrCostcentre_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _orderNrCCName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _orderNrName_ | merkkijono | Tietoa ei käytetä.  
Myyntitilauksien joukko | _modifiedTs_ | päivämäärä | Tietoa ei käytetä.  
Myyntitilauksien joukko | _deleted_ | merkki | Onko alanumero poistettu vai ei (1 = Kyllä, 0 = ei). Jos tilana on 8 tai 9, tai alanumero on poistettu ja projektilla ei vielä ole päättymispäivää, päättymispäiväksi asetetaan nykyinen päivä.  
**Esimerkkisanoma**
[code] 
    {  
      "salesorder": [  
        {  
          "rec": "1",  
          "orderNumber": "000001",  
          "subNumber": "1",  
          "orderType": "1",  
          "orderTypeName": "Myyntitilaus",  
          "orderName": "Projektin aloitustyö",  
          "currency": "EUR",  
          "costCentre": "1000",  
          "orderDate": "",  
          "deliveryDate": "2023-11-23",  
          "paymentTerms": "30 pv netto",  
          "deliveryTermsCode": "",  
          "deliveryTerms": "",  
          "deliveryMethodCode": "",  
          "deliveryMethod": "",  
          "orderStatus": "1",  
          "mainOrderType": "1",  
          "mainOrderTypeName": "Myyntitilaus",  
          "mainOrderCostCentre": "1000",  
          "mainOrderCostCentreName": "MYYNTI",  
          "party1Rec": "1057",  
          "party1Type": "BY",  
          "party1BusinessId": "1234567-7",  
          "party1CompanyNumber": "100027",  
          "party1Name1": "Yritys Oy",  
          "party1Name2": "",  
          "party1visitAddress": "Osoite 1",  
          "party1postalAddress": "",  
          "party1postalZip": "00000",  
          "party1postalCity": "PAIKKAKUNTA",  
          "party1countryCode": "FI",  
          "party1countryName": "Suomi",  
          "party1PersonName": "Antti Asiakas",  
          "party1ContactNumber1": "",  
          "party1ContactNumber2": "",  
          "party2Rec": "1058",  
          "party2Type": "DP",  
          "party2BusinessId": "1234567-7",  
          "party2CompanyNumber": "100027",  
          "party2Name1": "Yritys Oy",  
          "party2Name2": "",  
          "party2visitAddress": "Osoite 1",  
          "party2postalAddress": "",  
          "party2postalZip": "00000",  
          "party2postalCity": "PAIKKAKUNTA",  
          "party2countryCode": "FI",  
          "party2countryName": "Suomi",  
          "party2PersonName": "",  
          "party2ContactNumber1": "",  
          "party2ContactNumber2": "",  
          "subNrStatus": "avoin",  
          "projectWorkQuality": "",  
          "orderNrCostcentre": "1000",  
          "orderNrCCName": "MYYNTI",  
          "orderNrName": "",  
          "modifiedTs": "2023-05-26 12:57:02",  
          "deleted": "0"  
        }  
      ]  
    }
[/code]
## Tuonti SFTP-palvelimelle muodostetuista tiedostoista
Huom! Projektien tuontiin suositellaan käyttämään rajapintaratkaisua, joka kuvataan ylempänä artikkelissa.
SFTP-palvelimelle tulee muodostaa tekstimuotoinen aineisto kyseisestä tiedosta. Projektien haku määritellään työyhteisön asetuksissa, liittymissä otsikon 'Visma' alta. SFTP-palvelimelta käsitellään kaikki tiedostot, joten aineisto voi olla jaettuna useampaan tiedostoon.
Tiedosto on tallennettava ISO-8859-1-merkistökoodauksella. Tietueet on erotettava pystyviivalla (`|`). Rivinvaihto voidaan koodata Windows- (`CR`+`LF`) tai UNIX-muodossa (`LF`).
Aineisto ei sisällä otsikkoriviä. Aineistossa kukin L7-päänumero tai L7-alanumero siirretään omalla rivillään. Aineisto voi sisältää sekä päänumeroita että alanumeroita. Päänumeron tulee olla aineistossa ennen alanumeroa.
Siirretyt projektit muodostuvat palveluun automaattisesti. Mikäli projekti on jo palvelussa, päivitetään sen tietoja. Mikäli projektin tila (project status -kenttä) on arvoltaan jokin muu kuin 8 tai 9 niin projektin päättymispäivä asetetaan tuotavilla projekteilla tyhjäksi, jotta tuodut projektit ovat käytettävissä tapahtumilla. Projektin alkupäivä asetetaan tyhjäksi tuonnin yhteydessä.
### SFTP tuonnin ajastus
Ajastusasetukset löytyvät kohdasta Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Ajastus. Ajastus on mahdollista tehdä joko minuuttiajastuksella (esim. 15 minuutin välein, joka tunti jne.) tai päivittäisajastuksella.
SFTP-tuontia varten ajastuksen liittymävalikosta tulee valita 'Visma L7 projektien tuonti (vanha)'
Ajastuksien määrittelystä lisää voit lukea [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>).
### Rivityyppi päänumero
Column number | Data contents | Additional information  
---|---|---  
1 | Grandparent project code |  Sets the parent projects parent project when setting parameter ‘First column denotes root project’ is enabled. If project does not exist, then it’s created. Note that if this column is empty, row is skipped.  
2 | Project Code | Code of the project. If code does not exist, then it’s created. If it exists, then it will be updated.  
3 | Project Name | Name of the project. If name is empty, then project code is used.  
4 | Project Status | If project status is 8 or 9 then project end date is set to current day. Other values are ignored.  
### Rivityyppi alanumero
Column number | Data contents | Additional information  
---|---|---  
1 | Grandparent project code |  Sets the parent projects parent project when setting parameter ‘First column denotes root project’ is enabled. If project does not exist, then it’s created. Note that if this column is empty, row is skipped.  
2 | Parent Project Code | Code of the parent project. This code must exist. The project imported will be created as a child of the parent project.  
3 | Project Code | Code of the project. If code does not exist, then it’s created. If it exists, then it will be updated.  
4 | Project Name | Name of the project. If name is empty, then project code is used.  
5 | Project manager | Person number of the project manager. Can be empty.  
6 | Project Status | If project status is 8 or 9 then project end date is set to current day. Other values are ignored.  
7 | Project Type | Project type. Defaults to Projects. If incorrect type is set project will not be added.
