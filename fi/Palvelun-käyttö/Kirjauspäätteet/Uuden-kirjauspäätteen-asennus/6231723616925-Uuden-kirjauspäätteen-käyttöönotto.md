---
id: 6231723616925
title: Uuden kirjauspäätteen käyttöönotto
url: https://support.nepton.com/hc/fi/articles/6231723616925-Uuden-kirjausp%C3%A4%C3%A4tteen-k%C3%A4ytt%C3%B6%C3%B6notto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Uuden kirjauspäätteen asennus
section_id: 360002103958
section_path:
- Kirjauspäätteet
- Uuden kirjauspäätteen asennus
labels:
- Hatteland
- Nepton touch
- leimaustunniste
- kirjauspääteohje
- työpöytäpääte
promoted: false
updated_at: '2025-02-04T12:25:09Z'
edited_at: '2025-02-04T12:25:09Z'
---

# Uuden kirjauspäätteen käyttöönotto

Tässä ohjeessa kerrotaan, kuinka saat kirjauspäätteen käyttöön omassa Nepton ympäristössäsi. Jos organisaatiosi käytössä ei ole vielä kirjauspäätettä, olethan yhteydessä palveluntarjoajaasi tilataksesi kirjauspäätteen.
Huomaathan, että jo ennen kirjauspäätteen saapumista voit myös määrittää valmiiksi RFID-tunnisteet työntekijöiden tietoihin. Tarkemmat ohjeet löytyvät [täältä.](<https://support.nepton.com/hc/fi/articles/360002425517>)
Kun olet saanut uuden kirjauspäätteen, seuraa alla olevia ohjeita, kuinka saat kirjauspäätteen liitettyä verkkoyhteyteen ja valmiiksi käyttöön loppukäyttäjille. Jos jokin ohjeen kohdista on epäselvä, tai tarvitset apua käyttöönotossa, olethan yhteydessä palveluntarjoajaasi. 
## Nepton Touch
### Käyttöönotto
**Ennen kuin aloitat käyttöönoton** organisaatiollasi tulee olla aktiivinen asiakasympäristö Neptonissa. Jos tarvitset tähän apua, ota yhteyttä palveluntarjoajaasi.
**1)** Ota kirjauspääte ulos pakkauksestaan. Pakkaus sisältää seuraavat osat:
  * Pika-aloituksen ohjeet
  * Kirjauspääte
  * Virta-adapteri ja virtajohto
  * Säädettävä seinäteline & kiinnitysruuvit


**2)** Yhdistä ja käynnistä kirjauspääte
  * Liitä verkkokaapeli kirjauspäätteeseen, jolla saat kirjauspäätteen Internet-yhteyteen.
  * Jos laitteen mukana on toimitettu ulkoinen RFID-lukija, liitä se verkkokaapelin vieressä olevaan USB-liittimeen.
  * Liitä virtajohto kiinni kirjauspäätteeseen.
  * Liitä virtalähde pistorasiaan. Kirjauspääte käynnistyy automaattisesti. 
    * Kirjauspäätteessä on tarvittaessa myös virtapainike päätteen yläosassa.


Päätteet eivät tue suoraan PoE-virransyöttöä, vaan PoE:n käyttö vaatii vähimmillään erillisen PoE-splitterin hankinnan, mikä jakaa verkkokaapelin virtajohdoksi ja verkkokaapeliksi. Nämä liitetään Nepton Touch päätteeseen. Lisäksi PoE:n käyttö vaatii luonnollisesti sen, että verkkokaapelissa kulkee virta. Näin ei välttämättä oletuksena ole. Tämän mahdollistamiseksi tulee asentaa PoE-injektori. Vaadittavat PoE+ standardin mukaiset laitteet asiakas tai kumppani voi hankkia suoraan itse tai ne voi ostaa Neptonin kautta.
![20220810_101619s.jpg](https://support.nepton.com/hc/article_attachments/21077146581405)
_Virta- ja verkkoyhteysliitännät_
![20220810_095248s.jpg](https://support.nepton.com/hc/article_attachments/21077192089885)
_Virtapainike - Kirjauspääte käynnistyy automaattisesti, kun virtajohto on kiinni päätteessä sekä pistorasiassa._
**3)** Kirjauspäätteen ohjelmisto käynnistyy automaattisesti ja yrittää ottaa verkkoyhteyden. Kun ohjelmisto on löytänyt verkkoyhteyden, se päivittää automaattisesti ohjelmiston uusimpaan versioon. Jos on tarve määrittää laitteelle **kiinteä IP-osoite,** ohjeet löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/7132764025373>).
  * Kirjauspäätteelle on normaalia, että automaattisen päivityksen ja käyttöönoton aikana se uudelleenkäynnistyy, verkkoyhteys on offline-tilassa ja ruudulla esiintyy useampia ohjelmaikkunoita. Niiden pikakuvakkeet ilmestyvät työpöytänäkymään käyttöönoton yhteydessä. Tämä vaihe voi kestää useamman minuutin.
  * Jos kirjauspääte näyttää olevan offline-tilassa kauemmin kuin 15 minuuttia tai ilmoittaa muista ongelmista, katsothan ohjeen [Kirjauspääte ei löydä verkkoyhteyttä](<https://support.nepton.com/hc/fi/articles/360002588757>) ja ota yhteyttä verkon ylläpitäjään.


Kirjauspääte hakee IP-osoitteen automaattisesti. Joskus voi kuitenkin olla tarpeen määrittää tai tarkastella päätteen verkkoasetuksia, katso silloin ohje artikkelista [Kirjauspäätteen tiedot ja verkkoasetukset](<https://support.nepton.com/hc/fi/articles/360007577678>).
**4)** Kun kirjauspääte on käynnistynyt ja päivitetty, se odottaa linkittämistä Nepton asiakasympäristöön, pääkäyttäjän toimesta. Tässä vaiheessa kirjauspääte näyttää ID numeron eli päätteen tunnuksen ruudulla. Ota tämä ID numero ylös seuraavaa käyttöönottovaihetta varten. Jos tässä vaiheessa ruudulla on jo sisäänkirjautumisnäkymä, siirry kohtaan 7.
**5)** Yhdistä kirjauspääte Nepton asiakasympäristöön käyttämällä päätteen tunnusta eli ID numeroa.
  * Kirjaudu **Neptoniin pääkäyttäjänä** ja mene kohtaan Työsuhde -> Hallinta -> Kirjauspäätteet.
  * Kohdassa 'Lisää', kirjoita päätteen tunnus ID kenttään ja klikkaa 'Tallenna'.
  * Katso tarvittaessa lisäohjeita artikkelista [Kirjauspäätteen yhdistäminen organisaation tietoihin](<https://support.nepton.com/hc/fi/articles/360004790097>).
  * Jos kohtaat ongelmia tämän käyttöönottokohdan kanssa, otathan yhteyttä palveluntarjoajaasi.


**6)** Kun yhdistäminen Nepton asiakasympäristöön on tehty, kirjauspääte lataa automaattisesti asetukset, joita tarvitaan kirjauspäätteen käyttöä varten loppukäyttäjille. Tämä voi kestää joitakin minuutteja. Kirjauspääte uudelleenkäynnistyy automaattisesti tämän prosessin aikana.
**7)** Kun yhteys asiakasympäristöön on muodostettu, ruudulle ilmestyy sisäänkirjautumisnäkymä. Tässä vaiheessa kannattaa testata ohjelman toiminta vähintään yhden käyttäjän tunnistautumisella. Jos kirjautumispääte ei toimi odotetusti, tarkista seuraavat vianratkaisun ohjeistukset: [Vikailmoituksen teko ja tarvittavat tiedot](<https://support.nepton.com/hc/fi/articles/360002588797>)
Käyttääkseen kirjauspäätettä ja tehdäkseen kirjauksia, loppukäyttäjillä tulee olla tunnistautumistieto tallennettuna omissa henkilötiedoissaan Neptonin työsuhdeosiossa (PIN koodi tai RFID-tunnisteen numero).
**8)** Parhaan käyttökokemuksen varmistamiseksi, kiinnitä kirjauspääte seinään ja säädä päätteen asento seinätelineessä, poista suojamuovit näytöltä ja lukijasta.
Pääte on mahdollista asentaa myös pystyasentoon (Portraid) ja käyttöjärjestelmä tukee tätä, mutta palvelua ei ole suunniteltu skaalautumaan kyseiseen näyttöformaattiin.
Jos päätteen mukana on toimitettu ulkoinen RFID-lukija, kiinnitä se kaksipuolisella teipillä laitteen sisäänrakennetun lukijamoduulin päälle, kuvassa keltaisella merkitty kohta.
![Attaching_RFID_reader.png](https://support.nepton.com/hc/article_attachments/21077192107549)
Kirjauspääte on nyt valmiina käytettäväksi! Se on konfiguroitu päivittämään ja käynnistämään kirjauspäätteen ohjelmisto automaattisesti, ja näyttää ruudulla sisäänkirjautumisnäkymän, kun se on valmis käytettäväksi.
### Vianratkaisu
Jos kohtaat ongelmia jonkun käyttönotto-ohjeen kohdan kanssa, katso artikkeli [Vianratkaisu](<https://support.nepton.com/hc/fi/sections/360005896337-Vianratkaisu>).
## Nepton Flexim
### Käyttöönotto
**Ennen kuin aloitat käyttöönoton** organisaatiollasi tulee olla aktiivinen asiakasympäristö Neptonissa. Jos tarvitset tähän apua, ota yhteyttä palveluntarjoajaasi.
**1)** Ota kirjauspääte ulos pakkauksestaan. Pakkaus sisältää seuraavat osat:
  * Pika-aloituksen ohjeet
  * Kirjauspääte
  * Seinäteline & kiinnitysruuvit
  * Virransyötön ja sarjaportin liittimet  
  
![](https://support.nepton.com/hc/article_attachments/24914806946461)


**2)** Yhdistä ja käynnistä kirjauspääte
  * Liitä verkkokaapeli kirjauspäätteeseen, jolla saat kirjauspäätteen Internet-yhteyteen. Jos käytössä on POE-virransyöttö, verkkokaapeli antaa laitteelle myös virran.
  * Liitä virtajohto kiinni kirjauspäätteeseen (ellei käytössä ole POE-virransyöttö).
  * Kun virta on päällä, kirjauspääte käynnistyy automaattisesti.


Verkkokaapeli ja samalla POE-virransyöttö:  
![](https://support.nepton.com/hc/article_attachments/24914806949917)  
  

Erillinen virtaliitäntä (HUOM! Älä koskaan käytä yhtäaikaa POE-virransyöttöä ja erillistä DC-virransyöttöä)
![](https://support.nepton.com/hc/article_attachments/24921297029021)
**3)** Kirjauspäätteen ohjelmisto käynnistyy automaattisesti ja yrittää ottaa verkkoyhteyden. Kun ohjelmisto on löytänyt verkkoyhteyden, se päivittää automaattisesti ohjelmiston uusimpaan versioon. Oletuksena kirjauspääte hakee IP-osoitteen automaattisesti (DHCP). Jos on tarve määrittää laitteelle **kiinteä IP-osoite,** ohjeet löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/24730505042077>).
  * Kirjauspäätteelle on normaalia, että automaattisen päivityksen ja käyttöönoton aikana se uudelleenkäynnistyy, verkkoyhteys on offline-tilassa ja ruudulla esiintyy useampia ohjelmaikkunoita. Niiden pikakuvakkeet ilmestyvät työpöytänäkymään käyttöönoton yhteydessä. Tämä vaihe voi kestää jopa 15 minuuttia.
  * Jos kirjauspääte näyttää olevan offline-tilassa kauemmin kuin 15 minuuttia tai ilmoittaa muista ongelmista, katsothan ohjeen [Nepton Flexim vianratkaisu](<https://support.nepton.com/hc/fi/articles/24730787957021>).


**4)** Kun kirjauspääte on käynnistynyt ja päivitetty, se odottaa linkittämistä Nepton asiakasympäristöön, pääkäyttäjän toimesta. Tässä vaiheessa kirjauspääte näyttää ID numeron eli päätteen tunnuksen ruudulla. Ota tämä ID numero ylös seuraavaa käyttöönottovaihetta varten. Jos tässä vaiheessa ruudulla on jo sisäänkirjautumisnäkymä, siirry kohtaan 7.
**5)** Yhdistä kirjauspääte Nepton asiakasympäristöön käyttämällä päätteen tunnusta eli ID numeroa.
  * Kirjaudu **Neptoniin pääkäyttäjänä** ja mene kohtaan Työsuhde > Hallinta > Kirjauspäätteet.
  * Kohdassa 'Lisää', kirjoita päätteen tunnus ID kenttään ja klikkaa 'Tallenna'.
  * Katso tarvittaessa lisäohjeita artikkelista [Kirjauspäätteen yhdistäminen organisaation tietoihin](<https://support.nepton.com/hc/fi/articles/360004790097>).
  * Jos kohtaat ongelmia tämän käyttöönottokohdan kanssa, otathan yhteyttä palveluntarjoajaasi.


**6)** Kun yhdistäminen Nepton asiakasympäristöön on tehty, kirjauspääte lataa automaattisesti asetukset, joita tarvitaan kirjauspäätteen käyttöä varten loppukäyttäjille. Tämä voi kestää joitakin minuutteja. Kirjauspääte uudelleenkäynnistyy automaattisesti tämän prosessin aikana.
**7)** Kun yhteys asiakasympäristöön on muodostettu, ruudulle ilmestyy sisäänkirjautumisnäkymä. Tässä vaiheessa kannattaa testata ohjelman toiminta vähintään yhden käyttäjän tunnistautumisella. Jos kirjautumispääte ei toimi odotetusti, tarkista seuraavat vianratkaisun ohjeistukset: [Vikailmoituksen teko ja tarvittavat tiedot](<https://support.nepton.com/hc/fi/articles/360002588797>)
Käyttääkseen kirjauspäätettä ja tehdäkseen kirjauksia, loppukäyttäjillä tulee olla tunnistautumistieto tallennettuna omissa henkilötiedoissaan Neptonin työsuhdeosiossa (PIN-numero tai RFID-tunnisteen numero).
**8)** Parhaan käyttökokemuksen varmistamiseksi, kiinnitä kirjauspääte seinään ja poista suojamuovit näytöltä.
Kirjauspääte on nyt valmiina käytettäväksi! Se on konfiguroitu päivittämään ja käynnistämään kirjauspäätteen ohjelmisto automaattisesti, ja näyttää ruudulla sisäänkirjautumisnäkymän, kun se on valmis käytettäväksi.
### Vianratkaisu
Jos kohtaat ongelmia jonkun käyttönotto-ohjeen kohdan kanssa, katso artikkeli [Nepton Flexim vianratkaisu](<https://support.nepton.com/hc/fi/articles/24730787957021>).
