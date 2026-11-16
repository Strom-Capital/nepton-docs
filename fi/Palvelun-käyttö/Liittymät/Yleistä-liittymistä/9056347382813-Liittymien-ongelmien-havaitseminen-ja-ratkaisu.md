---
id: 9056347382813
title: Liittymien ongelmien havaitseminen ja ratkaisu
url: https://support.nepton.com/hc/fi/articles/9056347382813-Liittymien-ongelmien-havaitseminen-ja-ratkaisu
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels: []
promoted: false
updated_at: '2026-08-14T10:05:38Z'
edited_at: '2023-05-13T02:33:12Z'
---

# Liittymien ongelmien havaitseminen ja ratkaisu

Liittymiä käyttöönotettaessa ja käytettäessä varmista, että mahdolliset ongelmat huomataan ja ratkaistaan. Tämä on erityisen tärkeää, kun liittymä siirtää tiedot vain muutoksista Neptonin ja ulkoisen järjestelmän välillä, sen sijaan että liittymä lähettäisi kaikki tiedot säännöllisin väliajion. Tämän tyyppisissä liittymissä tiedot muutoksista jäävät helposti pysyvästi siirtämättä, ellei mahdollisia ongelmia havaita ja ratkaista.
Liittymää suunniteltaessa suosittelemme että:
  1. Tunnistakaa ja sopikaa tavat, joilla mahdolliset ongelmat havaitaan.
  2. Suunnitelkaa tavat, joilla havaitut ongelmat ratkaistaan.


Tämän saavuttamiseksi Nepton tarjoaa työkaluja ja esimerkkiratkaisumalleja:
  * [Palveluloki](<https://support.nepton.com/hc/fi/articles/360002575478>)
    * Näyttää Neptonin havaitsemat liittymäongelmat
  * Nepton sovellusliittymän (API) palautearvot 
    * Kertovat mahdollisista API kutsun ongelmista 
      * [Henkilötieto-sovellusliittymän (API) vastauskoodit](<https://support.nepton.com/hc/fi/articles/4406446686609>)
      * [Työaika sovellusliittymän (API) vastauskoodit](<https://support.nepton.com/hc/fi/articles/360019841477>)


## Palvelulokin käyttö liittymäongelmien havaitsemiseen ja ratkaisuun
Neptonin havaitsemat ongelmat liittymissä löydät palvelulokista. Tässä esimerkkejä siitä miten palvelulokia voi käyttää liittymien ongelmien havaitsemisessa ja ratkaisussa.
### Esimerkki 1
  1. Asiakas huomaa liittymäongelman säännöllisen palvelulokien tarkastuksen yhteydessä.
  2. Lokitiedoista selviää, että kerran yössä siirrettävän siirtotiedoston tietosisällössä on ongelma, joten asiakas korjaa tiedot HR-järjestelmässä, josta tiedot lähetetään.
  3. Korjatut tiedot lähetetään Neptoniin automaattisesti ajastetulla tuonnilla.


### Esimerkki 2
  1. Asiakas huomaa liittymäongelman säännöllisen palvelulokien tarkastuksen yhteydessä.
  2. Lokitiedoista selviää, että kutsu Nepton API:in uuden projektin lisäämiseksi epäonnistui puuttuvan projektin nimen takia.
  3. Asiakas pyytää projektista vastaavaa henkilöä täyttämään projektin nimen lähdejärjestelmään ja tallentamaan projektitiedot, jolloin tiedot lähetetään Neptoniin uudelleen.


## Nepton API:n palautearvojen käyttö liittymäongelmien havaitsemiseen ja ratkaisuun
Nepton API:n palautearvot kertovat, mikäli API kutsussa on ongelmia. Palaute sisältää myös kuvauksen kutsun ongelmista.
### Muutosten siirtymisen varmistaminen järjestelmien välillä
Liittymätoteutukset, jotka käyttävät Nepton API:a, usein siirtävät vain muutoksista tiedoissa. Näissä tapauksissa, jos ongelmia esiintyy on tärkeää varmistaa että muutokset saadaan uudelleenlähetettyä ongelmien korjausten jälkeen järjestelmien välillä. Tässä esimerkkitapoja, joilla uudelleenlähetys voidaan hoitaa:
  * Tietojen uudelleentallennus lähdejärjestelmässä tietojen uudelleenlähetykseksi
  * Kyvykkyys manuaalisesti lähettää uudelleen kaikki ongelma-alueen tiedot 
    * Esim. Kaikkien projektien tietojen taikka henkilötietojen lähetys kerta-ajona
  * Säännöllisesti tapahtuva kaiken aihealueeseen liittyvän tiedon lähetys järjestelmästä toiseen


Tässä esimerkki siitä miten API pyynnön vastausta voidaan käyttää liittymien ongelmien havaitsemisessa ja ratkaisussa.
  1. Lähettävä järjestelmä saa Nepton API:lta palautearvon, joka kertoo, että projektin lisääminen Neptoniin epäonnistui.
  2. Lähettävä järjestelmä ilmoittaa asiakkaan nimetylle henkilölle ongelmasta sähköpostilla, joka sisältää API-vastauksen ongelmakuvauksen.
  3. Sähköpostin saanut nimetty henkilö ohjeistaa projektivastaavaa projekti tietojen korjaamiseen lähdejärjestelmässä, sekä tietojen tallennukseen uudelleen. Korjatut tiedot lähetetään uudelleentallennuksen yhteydessä Neptoniin.


HUOM! Tiedot epäonnistuneista Nepton API kutsuista tallennetaan myös Neptonin [palvelulokiin](<https://support.nepton.com/hc/fi/articles/360002575478>).
Lisätietoja:
[Henkilötieto-sovellusliittymän (API) vastauskoodit](<https://support.nepton.com/hc/fi/articles/4406446686609>)
[Työaika sovellusliittymän (API) vastauskoodit](<https://support.nepton.com/hc/fi/articles/360019841477>)
## Täydentävät tavat liittymäongelmien havaitsemiseen ja ratkaisuun
On hyvä muistaa, että Neptonin tarjoamat välineet liittymäongelmien havaitsemiseen eivät kata kaikkea, vaan tämän lisäksi usein tarvitaan lisämenetelmiä.
Esimerkiksi:
  * Jos ulkoinen järjestelmä ei jostain syystä saa yhteyttä Nepton API:in tai SFTP-palvelimeen, ei Nepton voi tätä havaita, vaan yhteysongelmien mahdollinen seuranta pitää hoitaa muilla tavoilla
  * Jos Neptoniin siirrettävän tiedon luomisessa on ongelmia, Nepton ei ole tietoinen näistä ongelmista, joten näiden ongelmien seuranta pitää hoitaa muilla tavoilla
