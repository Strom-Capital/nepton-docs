---
id: 31928468706845
title: Sallitut IP-osoitteet työaikakirjausten tekemiseen
url: https://support.nepton.com/hc/fi/articles/31928468706845-Sallitut-IP-osoitteet-ty%C3%B6aikakirjausten-tekemiseen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palvelimet ja tietosuoja
section_id: 360005870038
section_path:
- Palvelimet ja tietosuoja
labels: []
promoted: false
updated_at: '2025-12-11T10:36:28Z'
edited_at: '2025-12-11T10:36:28Z'
---

# Sallitut IP-osoitteet työaikakirjausten tekemiseen

## Työaikakirjausten sijainti- ja laiterajoitukset
Palveluun voidaan määrittää rajoituksia, joilla rajataan tai estetään henkilöstöä kirjaamasta työaikaansa tietyistä fyysisistä sijainneista, verkoista tai päätelaitteista. Näin voidaan varmistaa, että työtä kirjataan vain sallituista työntekopaikoista.
**Esimerkki 1:**  
Työntekijä on oikeutettu kirjaamaan työnsä vain työpisteensä lähimmältä päätteeltä. Kirjaaminen muilta tehtaan päätteiltä voidaan estää.
**Esimerkki 2:**  
Työntekijä on oikeutettu kirjaamaan työ-tapahtumia vain toimistonsa Wifi-verkosta. Vain hälytystyö-tapahtuma on sellainen, joka sallitaan mistä tahansa sijainnista tai laitteelta.
**Rajoitusten määrittäminen pähkinänkuoressa:**
  * Palveluun määritetään työaikakirjausten tekemiseen sallitut työaikapäätteet ja/tai IP-osoitteet.
  * Henkilöryhmille määritetään, millä työaikapäätteillä / mistä ennaltamääritetyistä IP-osoitteista työajan kirjaaminen on sallittua.
  * Kielletyltä sijainnilta tehtyjen tiettyjen tapahtumatyyppien kirjaaminen voidaan joko estää kokonaan tai merkitä ne poikkeuksellisiksi kirjauksiksi.
  * Poikkeukselliset kirjaukset näkyvät sekä työntekijälle itselleen että tämän esihenkilölle työtuntien hyväksynnässä.


## Käyttöönotto
### Aktivointi
Tämä ominaisuus on aktivoitava ennen käyttöönottoa. Ota yhteyttä avainasiakaspääliikköösi tai Neptonin myyntiin saadaksesi lisätietoja aktivoinnista.
### Sallittujen päätteiden ja verkkojen (IP-osoitteiden) määrittäminen
#### Työaikakirjausten rajoittaminen Nepton Touch- ja Nepton Flexim-päätteistä
  * Nepton-ympäristöön liitetylle työaikapäätteelle annetaan ensin kuvaava nimi, esimerkiksi _"Helsingin toimisto sisäänkäynti"_.
  * Nimet määritetään kohdassa **Työsuhde > Hallinta > Kirjauspäätteet** päätteen tunnuksen perusteella.  
  
![](https://support.nepton.com/hc/article_attachments/32235977705117)
  * Nelinumeroinen päätteen tunnus näkyy työaikapäätteen oikeassa alakulmassa.
  * Nimetyt päätelaitteet voidaan myöhemmin liittää henkilöryhmiin työaikakirjausten rajaamista varten.


#### Työaikakirjausten rajoittaminen verkko-/IP-pohjaisesti 
  * Työaikakirjausten tekemistä voidaan rajoittaa mobiilissa, Nykytila-näkymässä tai muissa eri työajan kirjaamiseen käytettävissä tavoissa. 
  * Rajoituksen määrittämiseksi tarvitaan WiFi-verkkojen tai sisäosastojen IP-osoitteet tai -alueet organisaation IT-osastolta.
  * Työajan kirjaamiseen sallitut IP-osoitteet määritetään **Työsuhde > Hallinta > Turvallisuus > Sallitut IP-osoitteet-osiossa:**  
  
![](https://support.nepton.com/hc/article_attachments/32236466818333)  

  * Yllä olevassa esimerkissä on määritetty Helsingin ja Tampereen toimiston WiFi:n osalta kummallekin IP-osoite IP-osoitteen tulee olla julkinen (IPv4 tai IPv6). Nimen on suositeltavaa kuvata sallittavaa sijaintia, laitetta tai yhteyttä mahdollisimman tarkasti.
  * Sallittuja IP-osoitteita voi olla rajattomasti. Tällä tavoin palveluun luodaan nimettyjen verkkojen/IP-osoitteiden lista, joka voidaan liittää henkilöryhmiin myöhemmässä vaiheessa työaikakirjausten rajaamista varten.
  * IP-osoitteiden asettaminen on mahdollista useammalla eri tavalla, esimerkiksi:
    * 10.0.0.1 -> Työaikakirjaukset nimenomaisesti tästä IP-osoitteesta ovat sallittuja
    * 192.168.1.* -> Työaikakirjaukset tästä IP-osoitedimensiosta olevista osoitteista ovat sallittuja.
    * 192.168.1-10.7 -> Työaikakirjaukset asetetulla IP-osoitevälillä välillä ovat sallittuja.
    * 172.16.0.0/16 ->Työaikakirjaukset tästä IP-osoitteesta ja tietyllä aliverkon peitteellä (subnet mask) ovat sallittuja.


### Rajoitusten liittäminen henkilöryhmiin
Kohdan 2 jälkeisten toimenpiteiden jälkeen, palveluun määritetyt työaikapäätteeiden tunnukset tai IP-osoitteet voidaan liittää henkilöryhmiin sallimaan työaikakirjausten tekeminen vain näistä ennaltamääritetyistä lähteistä. 
  * Henkilöryhmän määritykset löytyvät **Työaika > Hallinta > Henkilöryhmät **alta. Näkymästä valitaan henkilöryhmä, johon rajoituksia halutaan asettaa:  
  
**![](https://support.nepton.com/hc/article_attachments/32237072886557)**
  * **Rajoitukset** -välilehdellä määritetyt rajoitukset koskevat valittua ryhmää sekä sen alaryhmiä (ellei alaryhmä ole ohittanut rajoituksia omilla säännöillään).


**Esimerkki (kuva yllä):**  
Helsingin toimiston henkilöryhmälle voidaan asettaa sääntö, että tapahtumat kirjataan vain Helsingin toimiston WiFi-verkosta tai Helsingin toimiston sisäänkäynnin työaikapäätteellä. Jokaisella osastolla/henkilöryhmällä voi olla tarkempia sääntöjä, jotka voivat olla tiukempia tai joustavampia.
**Huomio rajoitusten periytymisestä:**
  * Asetukset periytyvät henkilöryhmärakenteessa
  * Jos sääntö on peritty, se näkyy harmaana tekstinä kentässä.
  * Kun kenttään asetetaan arvo (tummempi teksti), se ohittaa rakenteessa ylemmästä henkilöryhmästä perityn säännön.


Lisätietoja kunkin kentän toiminnasta löytyy alla olevasta **Rajoitukset-välilehden kenttäkuvauksesta**.
## Henkilöryhmän rajoitusten valinnat
###  Toiminta, kun tapahtumia kirjataan sallitun päätelaitteen tai sijainnin ulkopuolella
  * **Ei mitään**  
Oletusarvoinen toiminta. Ei seurauksia, jos tapahtuma kirjataan ei-sallitusta päätelaitteesta tai verkosta. Tämä käytännössä poistaa rajoitustoiminnon käytöstä.
  * **Estä henkilöitä luomasta tapahtumia**  
Käyttäjälle näytetään varoitus tuetuissa päätteissä ja käyttöliittymässä, että hän on ei-sallitussa sijainnissa. Tietyt tapahtumatyypit eivät ole käytettävissä. 
    * Modernit Nepton Touch -päätteet, Nykytila-näkymä sekä tapahtumien muokkausnäkymät (työpöytä ja mobiili) rajoittavat käytettävissä olevia tapahtumatyyppejä.
    * Tapahtumatyyppejä. joita pääsääntöisesti käytetään työajan kirjaamiseen muualla kuin työntekopaikalla ei rajata tässä valinnassa pois käytöstä. Näitä tapahtumatyyppejä ovat 
      * Poissaolot (tapahtumat, joiden ActivityTypeCategoryID = 2)
      * Matka-aika
      * Etätyö
      * Varallaolo
      * Huomautus
      * Uudet tapahtumatyypit, joiden käyttäytyminen on joku yllämainituista
      * Hallinnolliset tapahtumatyypit (kertymien asetukset ja muutokset)
    * Kolmannen osapuolen päätteissä, jotka käyttävät APIa, sallittujen tapahtumatyyppien lista voidaan hakea TerminalLogin API -metodeilla.
  * **Varoita käyttäjiä ja näytä poikkeuksellinen kirjaus, jos tapahtuma kirjataan varoituksesta huolimatta**  
Käyttäjälle näytetään varoitus tuetuissa päätteissä ja käyttöliittymissä, että hän on ei-sallitussa sijainnissa. Tapahtuma voidaan varoituksesta huolimatta luoda, mutta sen yhteyteen liitetään keltainen varoituskolmio merkiksi poikkeuksellisesta kirjauksesta. 
    * Tämä edellyttää, että henkilöille on etukäteen kerrottu, missä ja mitä tapahtumia voi kirjata.
    * Esihenkilöt näkevät poikkeuskirjaukset Poikkeukselliset kirjaukset-raportissa, hyväksyntänäkymissä ja Työajan kalenteri- ja taulukkonäkymissä (tapahtumassa keltainen varoituskolmio tai ilmoitus).


### Sallitut kirjauspäätteet
Tässä kentässä voidaan valita Nepton Touch -työaikapäätteet, joita valitun henkilöryhmän (ja sen alaryhmien, ellei ohitettu) henkilöt voivat käyttää ilman varoituksia tai rajoituksia.
### Sallitut IP-osoitealueet
Tässä kentässä voidaan määrittää ne verkot/IP-osoitteet/IP-alueet, joita valitun henkilöryhmän (ja sen alaryhmien, ellei ohitettu) henkilöt voivat käyttää ilman varoituksia tai rajoituksia.
### Tapahtumatyypit, joita rajoitukset eivät koske
Yleensä ei ole järkevää rajoittaa tapahtumia, joita käytetään työajan kirjaamiseen henkilön tavanomaisen työntekopaikan ulkopuolella, kuten poissaolot, matka-aika tai etätyö. Nämä ovat oletuksena poissuljettuja rajoituksista.  
  
Jos haluat ohittaa oletuksen, voit määrittää listan tapahtumatyypeistä, jotka voidaan kirjata ilman varoitusta tai estoa mistä tahansa sijainnista/päätteestä/verkosta.  
  
**HUOM!** Käytettäessä rajoitusten toimintavalintaa "**Estä henkilöitä luomasta tapahtumia"** tähän asetukseen tulee määrittää kaikki ne tapahtumatyypit, joita henkilöstön halutaan pystyä valitsemaan ja kirjaamaan sallittujen päätelaitteiden tai sijaintien ulkopuolella. Jos asetukseen lisätään yksikin tapahtumatyyppi, kumotaan tällä oletuksena perityt arvot, joten täytyy myös oletustapahtumat listata manuaalisesti jos niiden käyttö halutaan estää.
## Vanhat päätelaitteet (Legacy terminals)
Jos käytössä on vanha päätelaite, käyttäjälle ei voida näyttää varoitusta siitä, että hän on ei-sallitussa sijainnissa. Tapahtumien lisääminen ja muokkaaminen johtaa kuitenkin virheilmoitukseen tai tapahtuman merkitsemiseen poikkeuskirjaukseksi.
**Suositus:**  
Käytä IP-pohjaisia rajoituksia (kohta 2.2) vanhoilla päätteillä, jotta tapahtumatyypit näkyvät oikein.
**Vanha päätelaite = laite, jota ei voida enää päivittää.**
