---
id: 360003762577
title: Henkilöiden tuonti
url: https://support.nepton.com/hc/fi/articles/360003762577-Henkil%C3%B6iden-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels:
- Person Import
- Henkilöiden tuonti
- Työsuhteen keston muuttaminen
- Työsuhteen päivämäärien jatkaminen
- Work contract's duration change
- henkilötietoliittymä
- henkilöryhmien puurakenne
promoted: false
updated_at: '2024-04-18T11:17:47Z'
edited_at: '2024-04-18T11:17:38Z'
---

# Henkilöiden tuonti

Henkilöiden tuonti mahdollistaa henkilötietojen (HR-tiedon) tuonnin Neptoniin. Henkilöiden tuonnilla voidaan rikastaa palvelun Henkilöstö-osioon tallennettuja ja siellä käsiteltäviä tietoja. Tuonti voidaan tehdä manuaalisesti, ajastettuna siirtona tai palvelun ohjelmallisia rajapintoja käyttäen. 
Mikäli käytössä on sellainen järjestelmä, johon on toteutettu järjestelmäkohtainen tuontitapa, niin henkilötuonnin sisältö tulee perustaa tämän ohjeen mukaisesti. [Järjestelmäkohtaiset](<https://support.nepton.com/hc/fi/articles/360002494538>) tuonnit ovat esitetty tässä artikkelissa.
## Tuontitavat
1\. **Manuaalinen tuonti:** Yksittäinen henkilöstötietoja sisältävä tiedosto voidaan valita manuaalisesti tuotavaksi Neptoniin työsuhdeosion kautta. Katso ohje henkilöiden manuaaliseen tuontiin [täältä](<https://support.nepton.com/hc/fi/articles/360018767498>).
2\. **Ajastettu tuonti** : Ajastettu tuonti on määriteltävissä ja tarkasteltavissa valikossa Työsuhde -> Hallinta -> Ajastetut tehtävät.
Tätä tietojen tuontia voidaan käyttää silloin, kun tiedot tuodaan SFTP-palvelimelta tai REST-verkkopalvelulta. Jos henkilötuonti tehdään SFTP-palvelimelta tiedostonimeen täytyy sisältyä aikaleima. Tällä varmistetaan, että olemassa olevaa tiedostoa ei korvata. Tiedot voidaan tuoda myös useammalla tiedostolla. Nepton käsittelee SFTP-palvelimelle siirretyt tiedostot sen mukaisesti, mikä tiedostoista on siirretty SFTP-palvelimelle ensin, vanhimmasta uusimpaan. 
Otsikot voidaan asettaa joko ajastetussa tehtävässä tai tuontitiedostossa. Jos kenttien otsikkotietoja ei ole tuontitiedostossa, ne on asetettava ajastetussa tehtävässä.
Ohjeet ajastetun tehtävän luomiseen löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360002489317>).
3\. **Nepton API:n kautta** : Henkilötietojen tuonti onnistuu käyttämällä web service-metodeja ImportUsersFromCSV tai ImportUsersFromXML. Rajapintakuvaus on löydettävissä [täältä](<https://support.nepton.com/hc/fi/articles/360004855857>).
## Tuetut tiedostomuodot
Manuaalisen tuonnin Oletus-henkilötuonnin tyyppi tukee alla listattuja tiedostomuotoja.
  * CSV 
    * Puolipiste (;) kenttäerottimena
    * Windows-tyylinen \r\n tai UNIX-tyylinen \n rivinvaihtomerkkinä
    * Ensimmäisellä rivillä on lueteltava käytettävät henkilötuonnin kentät puolipisteillä eroteltuina kentille, joita käytetään jokaisella seuraavalla rivillä - ellei kenttälistaa ole toimitettu erikseen (kuten Otsikkorivi-asetuksessa [henkilötietojen ajastetussa tuonnissa](<https://support.nepton.com/hc/fi/articles/360002489317>)). Tällöin otsikkoriviä ei tule lisätä.
  * Excel 
    * Ensimmäisellä rivillä on lueteltava käytettävät henkilötuonnin kentät sarakekohtaisesti kentille, joita käytetään jokaisella seuraavalla rivillä. Jos tiedosto sisältää sarakkeita, joita ei pidä tuoda, tuotavien kenttien lista voidaan määritellä Tuotavat kentät -asetuksessa [henkilötietojen ajastetussa tuonnissa](<https://support.nepton.com/hc/fi/articles/360002489317>).
  * XML 
    * Solmujen niminä voi käyttää [tuontikenttien nimiä](<https://support.nepton.com/hc/fi/articles/360015933397>). Välilyönnit on korvattava alaviivalla ( _ ), XML-aineistossa kun niitä käytetään solmun nimessä. Esimerkiksi "Ensisijainen esimies" tulee olla "Ensisijainen_esimies".
    * Solmun nimen tulee täyttää seuraavat ehdot: 
      * se alkaa kirjaimella tai alaviivalla ( _ )
      * se ei ala merkkijonoilla xml tai Xml
      * se ei sisällä välilyöntejä (XML-aineisto)
      * se voi sisältää kirjaimia, numeroita, väliviivoja, alaviivoja ja pisteitä
    * Henkilön erotinsolmu sisältää henkilön tiedot 
      * API-rajapintaa käytettäessä (käytettävissä vain XML-muodolle) solmun nimi annetaan _SeparatorNodeName_ -parametrina
      * Ajastettua tehtävää käytettäessä solmun nimi annetaan _XML-erotin_ -kentässä (asetettavissa vain XML-muodolle)
      * Jos erotinsolmun nimeä ei määritellä, palvelu etsii henkilöiden tiedot _ImportUserData_ -solmuista
    * Katso aineistomuoto esimerkki alempana sivulla
  * JSON 
    * Kentän niminä käytetään [tuontikenttien nimiä](<https://support.nepton.com/hc/fi/articles/360015933397>).
    * Oletustuontityypissä henkilötiedot tuodaan "ImportUserData"-taulukon elementteinä
    * Tyhjä arvo tuodaan kentän avolla "null" tai ""
    * Käytä tiedoistossa tiedostopäätettä ".json"
    * Katso aineistomuoto esimerkki alempana sivulla


**Xml-esimerkkitiedosto:****< ImportuserData>** -solmu on henkilön tietojen erotinsolmu esimerkissä alla
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <Persons>  
    ** <ImportUserData>**  
            <First_name>User</First_name>  
            <Last_name>1</Last_name>  
            <Username>User 1</Username>  
            <Email>testuser1@test.com</Email>  
    ** </ImportUserData>**  
    ** <ImportUserData>**  
            <First_name>User</First_name>  
            <Last_name>2</Last_name>  
            <Username>User 2</Username>  
            <Email>testuser2@test.com</Email>  
    ** </ImportUserData>**  
    </Persons>
[/code]
**JSON-esimerkkitiedoston sisältö** :
[code] 
    {  
       "ImportUserData":[  
          {  
             "Henkilönumero":"123456",  
             "Etunimi":"Matti",  
             "Sukunimi":"Esimerkki",  
             "Ammattinimike":"Suunnittelija",  
             "Työsuhteen alkupäivä":"01.04.2019",  
             "Työsuhteen päättymispäivä":""  
          },  
          {  
             "Henkilönumero":"23456",  
             "Etunimi":"Juha",  
             "Sukunimi":"Esimerkki",  
             "Työsuhteen alkupäivä":"01.07.2022",  
             "Työsuhteen päättymispäivä":null  
          }  
       ]  
    }
[/code]
## Tuetut merkkikoodaukset
  * UTF-8
  * ISO-8859-1


## Henkilötuonnin kentät
Henkilötuonnin kentillä kuvataan ne sarakkeet, jota siirrettävä aineisto sisältää. Sarakkeen nimi voi olla määritetty ajastetun tuonnin otsikoksi tai se voi olla osa siirrettävää aineistoa. Henkilötuonnin tukemat kentät löydät [täältä](<https://support.nepton.com/hc/fi/articles/360015933397>). Nämä kentät ovat käytettävissä kun henkilötuonnin tyypiksi valitaan 'oletus'. Lisäksi käytettävissä voi olla järjestelmäkohtaisia kenttiä, joita voidaan käyttää, ja jotka on kuvattu ohjeessa järjestelmäkohtaisesti.
  * Kenttä voidaan jättää huomioimatta tuonnissa asettamalla kentän nimeksi suuraakkosin **IGNORE.**
  * **Jos aineisto sisältää voimassa alkaen -kentän ja se on tyhjä, poistetaan koko historia kyseisestä asetuksesta.**
  * **Jos aineisto EI sisällä voimassa alkaen -kenttää, tulee muutos voimaan siitä päivästä alkaen, jolloin tuonti tehdään. Asetuksen aiempi arvo säilyy palvelussa.**


## Henkilötietojen voimassaolot - Tulevien muutosten tuonti
Henkilötuonti tukee henkilötietojen tuontia [ilman voimassaoloja](<https://support.nepton.com/hc/fi/articles/360015741097>), sekä [voimassa alkaen -tiedon kanssa](<https://support.nepton.com/hc/fi/articles/360015754117>). Siirrettävät aineistot tulisi ensisijaisesti muodostaa siten, että ne sisältävät tiedon voimassaolosta. Tällöin siirrettävä aineisto voi välittää tietoja myös takautuvista muutoksista henkilötietoihin. Mikäli aineisto ei sisällä tietoa voimassaolosta, niin takautuvat muutokset siirrettyyn aineistoon eivät ole mahdollisia.
