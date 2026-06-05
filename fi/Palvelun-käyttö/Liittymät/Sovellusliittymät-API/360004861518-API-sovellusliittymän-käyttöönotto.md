---
id: 360004861518
title: API (sovellusliittymän) käyttöönotto
url: https://support.nepton.com/hc/fi/articles/360004861518-API-sovellusliittym%C3%A4n-k%C3%A4ytt%C3%B6%C3%B6notto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sovellusliittymät (API)
section_id: 360000921798
section_path:
- Liittymät
- Sovellusliittymät (API)
labels:
- liittymäkuvaus
promoted: false
updated_at: '2025-09-08T07:26:22Z'
edited_at: '2025-09-08T07:25:44Z'
---

# API (sovellusliittymän) käyttöönotto

Kun on tarve siirtää tietoa Neptonin ja toisen järjestelmän välillä, Nepton API -sovellusliittymä on hyvä vaihtoehto perinteiselle SFTP-liittymälle. Integraatiot voidaan siis toteuttaa API:n kautta.
Pyytävä järjestelmä voi tehdä palvelupyyntöjä Nepton API:lle milloin tahansa. Se, mikä on pyytävä järjestelmä, on asiakkaan päätettävissä ja se voi olla kolmannen osapuolen toteutus. API-kutsut voidaan luoda erilaisten sovellusten kautta tai esimerkiksi asiakkaan palvelimella ajettavien skriptien avulla. Joka tapauksessa, API-kutsujen toteutustapa riippuu asiakkaasta. Tämä ja muut API-aiheiset artikkelit auttavat asiakkaan tai kolmannen osapuolen rajapinnoista vastaavia henkilöitä ottamaan käyttöön API-toteutuksen.  
  
![](https://support.nepton.com/hc/article_attachments/13812483983389)
Käytännössä API-sovellusliittymää hyödynnetään mm. [projektien](<https://support.nepton.com/hc/fi/articles/360019840237>) tai [tapahtumien tuonnissa](<https://support.nepton.com/hc/fi/articles/360019840217>) Neptoniin, jolloin lähettävään järjestelmään tehtävät lisäykset tai muutokset päivittyvät reaaliajassa Neptoniin.
Neptonissa on API sovellusliittymälle 2 eri endpointtia, jonne kutsuja voidaan tehdä. Toisessa endpointissa ovat [Henkilötietojen sovellusliittymät](<https://support.nepton.com/hc/fi/articles/360004855857>)
  * Henkilöstö-, työsuhde- ja muut henkilöihin liittyvät kentät


ja toisessa endpointissa [Työajan toiminnot](<https://support.nepton.com/hc/fi/articles/360004861558>), eli
  * Poissaolot
  * Työaikakirjaukset, jotka ovat tapahtumia palvelussa
  * Projektit, kustannuspaikat ja työmääräykset, jotka ovat työn kohdennuksia tai projekteja palvelussa


## API liittymän käyttöönotto
API-kutsuja rakennettaessa on otettava huomioon, että parametrin kirjainkoolla on merkitystä. Varmista siis, että kutsussa kaikki isot ja pienet kirjaimet ovat täsmälleen samalla tavalla kuin ohjeessamme.
  1. Työaikatapahtumien, poissaolojen tai projektien sovellusliittymän käyttöön tarvitaan **CustomerId-tunnus,** jonka saa Neptonin yhteyshenkilöltä tai asiakaspalvelusta. Lisää työajan API:ssa tunnistautumiseen [täältä.](<https://support.nepton.com/hc/fi/articles/360019983978>)  
  

  2. Henkilötietojen API vaatii autentikoitumiseen **DeploymentId** \- ja **Webservicepassword** -tiedot, jotka saa Neptonin yhteyshenkilöltä tai asiakaspalvelusta. Lisätietoja [Henkilötietojen API ](<https://support.nepton.com/hc/fi/articles/360004855857-Henkil%C3%B6tietojen-API-yleisesti>)-artikkelista.  
  

  3. API-kutsut todennetaan. Todentaminen edellyttää kirjautumistietoja ja muutokset tietoihin kirjataan lokiin tämän käyttäjän suorittamana. Jokaiselle sovellusliittymää käyttävälle ratkaisulle tulee hyvän tietoturvan takaamiseksi perustaa oma henkilö eli **käyttäjätunnus**. Luomalla yksilölliset käyttäjätunnukset, saadaan myös lokeihin tiedot, mitä käyttäjätunnusta ja mitä API-toteutusta on käytetty missäkin API-kutsuissa. Näitä käyttäjätunnuksia ei käytetä mihinkään muuhun tarkoitukseen kuin API-sovellusliittymien käyttöön. Hyvän tietoturvan takaamiseksi on suositeltavaa myöntää vain tarvittavat Neptonin roolit käyttäjätunnukselle, jota käytetään API-todennuksessa. Esimerkiksi jos sovellusliittymän toteutus ei käytä HR-tietoja, käyttäjätunnukselle tulee antaa rooli pienimmillä oikeuksilla HR-tietojen saamiseksi. 


## API liittymän käyttöönotto aineiston vientiin
Neptonista mm. **projektien tai tapahtumien viennissä** tarvitaan edellä mainittujen määritysten lisäksi [sääntöjoukkojen poimintasäännöt](<https://support.nepton.com/hc/fi/articles/360002492278>), joiden perusteella määriteltyä sisältöä viedään toiseen palveluun. 
API-sovellusliittymän käyttö sisältyy kaikkiin Neptonin palvelutasoihin.
