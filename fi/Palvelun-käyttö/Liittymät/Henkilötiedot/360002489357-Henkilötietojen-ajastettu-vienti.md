---
id: 360002489357
title: Henkilötietojen ajastettu vienti
url: https://support.nepton.com/hc/fi/articles/360002489357-Henkil%C3%B6tietojen-ajastettu-vienti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels:
- henkilöstönvienti
promoted: false
updated_at: '2026-04-08T07:29:51Z'
edited_at: '2026-04-08T07:22:35Z'
---

# Henkilötietojen ajastettu vienti

Henkilötietojen vientitoiminnolla saat siirrettyä henkilöstötietoja tiedostoon. Henkilötiedot voi ottaa palvelusta [manuaalisesti Excel-tiedostoon](<https://support.nepton.com/hc/fi/articles/360002430478>) tai ajastetusti ja automaattisesti CSV- tai JSON-muotoiseen tiedostoon. Tässä ohjeessa kuvataan, kuinka henkilötiedot voidaan siirtää Neptonista ajastetulla henkilöiden viennillä suoraan ulkoiseen palveluun.
Henkilötietojen ajastettu vienti tukee tietojen vientiä CSV- tai JSON-muodossa.
Määritys tehdään valikossa **Työsuhde - Hallinta - Ajastetut tehtävät**. Lisätäksesi automaattisen tuonnin määritykset valitse **Lisää tehtävä**. Valinnan jälkeen tulevalla lomakkeella pääset määrittelemään ajastetun tehtävän.
Aluksi valittavissa ovat vain kaikille tehtäville yhteiset tiedot. Valittuasi tehtävän tyypin "Vie henkilöitä" saat näkyville siirtotapavalinnan. Lisää valintamahdollisuuksia tulee näkyville tekemiesi valintojen perusteella.
Lomakekenttien kuvaukset:
  * **Yleiset tiedot**
    * **Nimi:** Valitse haluamasi nimi tehtävälle, esimerkiksi "Henkilöiden vienti Neptonista". Tällä tekstillä ei ole teknisesti vaikutusta toimintaan.
    * **Kuvaus:** Halutessasi voit lisätä tarkemman kuvauksen tehtävälle. Tällä tekstillä ei ole teknisesti vaikutusta toimintaan, eikä se näy muualla kuin ajastettujen tehtävien hallinnassa.
    * **Tyyppi:** Vie henkilöitä
    * **Suorita ylläpitäjänä:** Tässä kentässä valitaan, millä tunnuksella siirto tehdään ja millä tunnuksella se näkyy listauksessa. Tähän valitun käyttäjän tulee olla ylläpitäjä. Suosituksena on, että perustetaan tätä varten kokonaan uusi henkilö (esimerkiksi "Henkilötietojen vientitunnus"). Tähän ei suositella valittavan todellista henkilöä, koska se voi aiheuttaa sekaannuksia siinä, onko kyseessä oikeasti manuaalinen vai automaattinen siirto.
    * **Siirtotapa:** Siirto voidaan suorittaa ulkoiselle palvelimelle käyttäen SFTP-siirtoa tai REST API -sovellusliittymäpalvelun kautta.
  * **Henkilötiedot**
    * **Vientimuoto:** Valitse sen järjestelmän vientimuoto, johon tietoja ollaan viemässä (esim. Visma Nova). Jos järjestelmän muotoa ei ole saatavilla tai on tiedossa, että kohdejärjestelmä tukee oletusarvoista muotoa, valitse [Oletusarvoinen muoto](<https://support.nepton.com/hc/fi/articles/4405423095953-Vie-henkil%C3%B6t-Oletusarvoinen-CSV-tietomuoto>). 
    * **Merkistökoodaus:** Valitse merkistökoodaus vietävälle aineistolle ja tiedostolle. Mahdolliset valinnat ovat:
      * UTF-8
      * ISO-8859-1 
[UTF-8](<https://fi.wikipedia.org/wiki/Unicode#UTF-8>) on tapa koodata Unicode-merkistöä, [ISO-8859-1](<https://fi.wikipedia.org/wiki/ISO_8859-1>) on rajattu yleisiin eurooppalaisissa kielissä käytettyihin merkkeihin. Merkistökoodaus on valittavissa ainoastaan CSV-muotoisille tiedostoille – JSON-muotoiset tiedostot lähetetään aina UTF-8-muodossa. Yleisesti ottaen sen ohjelman tai palvelun, jota varten viet tiedoston, tulisi antaa tiedot tarvittavasta merkistökoodauksesta. Jos valitset virheellisen tiedostomuodon, tarkkeet latinalaisten aakkosten yhteydessä (kuten suomen ä- ja ö-kirjaimissa) tai ei-latinalaisten aakkosten merkit näkyvät todennäköisesti väärin.
    * **Sisällytä henkilöt integraatiotunnisteella / henkilönumerolla nolla:** Valitse "Kyllä" jos vientitiedostossa pitää olla mukana kaikki henkilöt. Valitse "Ei", jos henkilöitä, joilla ei ole henkilönumeroa tai joiden henkilönumero on nolla ("0"), ei haluta mukaan. Valinta "Ei" antaa mahdollisuuden estää esimerkiksi erikoistunnusten viennin yksinkertaisesti asettamalla henkilönumeroksi 0. Tätä valintaa ei tueta Visma Nova -vientimuodossa - siinä ovat aina mukana kaikki henkilöt.
    * **Tietomuoto:**[CSV](<https://fi.wikipedia.org/wiki/CSV>)\- tai [JSON](<https://fi.wikipedia.org/wiki/JSON>)-muotoinen tiedosto. CSV-tiedoston sisältö riippuu valitusta vientimuodosta, ks. kohtaa Vientimuoto ylempänä. Visma Nova -järjestelmälle tuotettava tiedosto on aina CSV-muotoinen. JSON-muodossa mukana olevat kentät on lueteltu artikkelissa [Vie henkilöt - JSON-tietomuoto](<https://support.nepton.com/hc/articles/7982660700189>).
    * **Tiedostonimen muoto:** Vientitiedoston nimi ilman .csv- tai .json-päätettä - pääte lisätään automaattisesti. Tämä asetus on käytettävissä vain SFTP-siirtotavalle.
    * **Sisällytä otsikkorivi CSV-tiedostoon:** Valitse "Kyllä", jos haluat, että vientitiedostossa ovat mukana kenttien nimet. Valitse muussa tapauksessa "Ei". Tämä asetus on käytettävissä vain CSV-tietomuodolle.
    * **Valitse lähetettävät tiedot:** Valitse "Kaikki henkilöt" viedäksesi kaikkien henkilöiden kaikki tiedot joka kerralla tehtävää ajettaessa. Valitse "Henkilöt, joilla muutoksia" viedäksesi niiden henkilöiden kaikki tiedot, joilla on mitä tahansa muuttunutta tietoa tehtävän edellisen suorituskerran jälkeen. Tämä asetus on käytettävissä vain JSON-tietomuodolle.
  * **Tiedostopalvelin (SFTP)**
    * **Palvelimen osoite:** Merkitse palvelimen osoite, johon aineisto siirretään.
    * **Portti:** Merkitse käytettävä palvelimen portti (tavallisin arvo SFTP-palvelimille on 22).
    * **Käyttäjätunnus:** Merkitse käytettävä käyttäjätunnus, jolla pääsee kirjautumaan aineiston viemistä varten palvelimelle.
    * **Salasana:** Merkitse käytettävä salasana käyttäjätunnukselle. Huomaa, että HTML-koodi (esim. **<** tekstin edellä) ei ole sallittua salasanakentässä.
    * **Työkansio:** Voit valinnaisesti määritellä tietyn kansion palvelimella siirtoa varten. Vientitiedosto tallennetaan kyseiseen kansioon. Kansio voi olla ainoastaan käyttäjätunnuksen oletushakemiston alla, esim. henkilot/Nepton
  * **REST-rajapinta**
    * **REST API -osoite:** Aseta sen REST API -palvelun sovellusliittymän URL, johon henkilötiedot voidaan siirtää.
    * **Autentikaatiotyyppi:** Aseta autentikaatio REST API -palvelun vaatimusten mukaisesti:
      * **Ei autentikointia:** Palvelu ei vaadi minkäänlaista tunnistautumista pääsyä varten.
      * **Perus-HTTP-autentikointi:** Palvelu vaatii tavanomaisen tunnistautumisen käyttäjätunnuksella ja salasanalla. Aseta käyttäjätunnus ja salasana REST APIlle **Parametri** -asetuksissa käyttäen kenttiä "username" ja "password" paremetrin **Nimi** -asetuksiin ja niille sopivia arvoja **Arvo-** asetuksiin.
      * **OAuth 2.0 (perus-HTTP-autentikointi):** Palvelu vaatii erillisen OAuth 2.0 -protokollaa käyttävän valtuutuspalvelimen käyttöä. Aseta vaadittu **valtuutuspalvelimen osoitteen** arvo. Aseta  _valtuutuspalvelimen_ käyttäjätunnus ja salasana **Parametri** -asetuksissa käyttäen kenttiä "username" ja "password" parametrin **Nimi** -asetuksiin ja niille sopivia arvoja **Arvo-** asetuksiin.
      * **Tunnussanavaltuutus:** Palveluun tunnistaudutaan käyttäen erityistä avainta. Aseta vaadittu avain **parametrin** asetuksiin: **Nimi** -kenttään "apikey" ja avaimen arvo **Arvo** -kenttään.
    * **Parametrit 1 - 4:** Ks. yllä parametrit, joita autentikaatio vaatii. Voit myös määritellä tässä ylimääräisiä REST API -palvelun vaatimia HTTP-parametreja.
  * **Ajastus**
    * **Suorita:** Näissä kentissä määritellään milloin tehtävä ajastetaan suoritettavaksi.
      * **Vain manuaalisesti:** Jos et halua käyttää tehtävän automaattista ajastusta, valitse tämä vaihtoehto. Tehtävä suoritetaan vain, jos valitset **Suorita nyt** -painikkeen tehtävän tallennuksen jälkeen.
      * **Kerran** : Tehtävä ajastetaan suoritettavaksi vain yhden kerran. Valitse suoritushetken päiväys ja kellonaika **Suoritusaika** -kentässä.
      * **Tietojen muuttuessa:** Tehtävä suoritetaan heti, kun mitä tahansa henkilötietoja muokataan. Tämän lisäksi vaaditaan päivittäinen ajo, sillä tiedot saattavat muuttua myös niiden voimassaolojen takia. Täytä silloin myös kohta "Ja päivittäin klo". Jos valitset tämän ajastustavan, **Valitse lähetettävät tiedot** -kentässä pitäisi yleensä olla arvo _Henkilöt, joilla muutoksia_ valittuna. Tämä vaihtoehto on käytettävissä vain JSON-tietomuodolle.
      * **Kerran tunnissa:** Tehtävä suoritetaan joka tunti sillä minuutilla, joka on asetettu **Tällä minuutilla** -kentässä. Esim. jos "tällä minuutilla" on 30, tehtävä suoritetaan 0:30, 1:30, 2:30 jne.
      * **Päivittäin:** Tehtävä suoritetaan joka päivä sinä kellonaikana, joka on asetettu **Kellonaikana** -kenttään.
      * **Viikoittain:** Tehtävä suoritetaan vain niinä viikonpäivinä, jotka on määritelty **Viikonpäivinä** -kentässä. Aseta kellonaika suoritukselle **Kellonaikana** -kenttään.
      * **Kuukausittain:** Tehtävä suoritetaan **Kuukausina-** ja **Päivinä** -kentissä valittuina kuukausina ja päivinä. **Päivinä** -kentässä on valittavissa päivät numeron mukaan tai kuukauden viimeinen päivä. Aseta **kellonaika** -kenttään suoritusajankohta suorituspäivänä.
    * **Käytössä:** Valitse säännöllisesti suoritettaviksi ajastetuille tehtäville aikaväli, jolla ajastus on käytössä. Tehtävä suoritetaan muiden asetusten mukaisesti, mutta ei kuitenkaan ennen **Alkaen** -kentän päiväystä ja kellonaikaa eikä **Päättyen** -kentän päiväyksen ja kellonajan jälkeen. **Alkaen** -kentän oletusarvona tehtävä on heti käytössä. **Päättyen** -kenttä on valinnainen.


Kun määritykset on tehty valitse **Tallenna**. Palvelu ilmoittaa tallennuksen onnistuneen, jos kaikki kentät on täytetty asianmukaisesti.   
  
Henkilöiden vienti voidaan suorittaa manuaalisesti sivun alalaidan valinnoilla. Ensimmäisenä valitaan siirretäänkö kaikki henkilötiedot koko historian ajalta, vai annetaanko haluttu päivämäärä, jonka jälkeisten muutosten halutaan siirtyvän. Tämän lisäksi annetaan syy manuaalisen henkilötiedon viennin ajamiselle.   
  
Kun nämä kentät ovat täytetty, painetaan **Suorita nyt** , jolloin henkilötietojen vienti suoritetaan välittömästi.
![](https://support.nepton.com/hc/article_attachments/35209730797725)
