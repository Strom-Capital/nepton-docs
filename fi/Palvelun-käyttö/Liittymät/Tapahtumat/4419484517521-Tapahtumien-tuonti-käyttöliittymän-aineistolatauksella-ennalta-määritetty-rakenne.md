---
id: 4419484517521
title: Tapahtumien tuonti käyttöliittymän aineistolatauksella - ennalta määritetty
  rakenne
url: https://support.nepton.com/hc/fi/articles/4419484517521-Tapahtumien-tuonti-k%C3%A4ytt%C3%B6liittym%C3%A4n-aineistolatauksella-ennalta-m%C3%A4%C3%A4ritetty-rakenne
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels: []
promoted: false
updated_at: '2025-07-14T11:23:01Z'
edited_at: '2025-07-14T11:17:07Z'
---

# Tapahtumien tuonti käyttöliittymän aineistolatauksella - ennalta määritetty rakenne

Tässä artikkelissa kuvataan tapahtumien aineistolataus asetuksiin tallennetulla rakenteella. Tapahtumien tuontiin käyttöliittymästä on muitakin tapoja, jotka on kuvattu [täällä](<https://support.nepton.com/hc/fi/articles/4404767615249>).
## Tiedon tuonnin rakenteen määrittely
Rakenne tapahtumien tuontiin tehdään valikossa **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Tapahtumien tuonti #1, #2, #3, #4 ...** . Tapahtumien tuonnin rakenteen määritykset tulee tehdä ennen ensimmäisen aineiston lataamista käyttöliittymästä tai ajastetusti. Liittymät-valikossa tehty manuaalinen tapahtumien tuonti vaatii samoja määrityksiä kuin ajastettu tuonti. **Ajastetussa tuonnissa** tulee alla olevan lisäksi määritellä siirron [lisäasetuksia](<https://support.nepton.com/hc/fi/articles/4403974690321>).
Asetuksissa määritellään, montako päivää historiaan aineiston rivejä käsitellään. Rivit käsitellään siten, että aineisto muodostaa palveluun ne tapahtumat, joita ei ole henkilön kalenterissa. Tapahtumat, jotka ovat poistuneet siirrettävästä aineistosta, poistetaan myös henkilön kalenterista. Näin kalenterissa esitettävät poissaolot vastaavat aina siirtoaineiston poissaoloja. Lähdejärjestelmän tulee muodostaa siirrettävä aineisto myös silloin, kun aineistossa on ainoastaan poistuvia rivejä. Huomaathan, että jokaisen tapahtumien tuonnin asetuksiin tulee määrittää henkilö, joka näytetään **tapahtumien tuojana**. Lisätietoa henkilöstä, joka näytetään tapahtumien luojana[ täältä.](<https://support.nepton.com/hc/fi/articles/4403974690321>)
## Tietojen tuonnin vaiheet
### Määrittele tapahtumien tuonnin asetukset
Tapahtumien tuonnin asetuksissa tulee määritellä seuraavat tiedot. **Työaika > Työyhteisön asetukset > Liittymät > Tapahtumien tuonti**.
  * **Kuvaus.** Tieto siitä, miten tapahtumien tuonnin asetukset on määritetty.


![mceclip1.png](https://support.nepton.com/hc/article_attachments/11614834145053)
  * **Henkilö,** **joka näytetään tapahtumien luojana** tapahtumien tuonnissa. Mikäli eri käyttäjä tuo samat tapahtumat, luodaan ne uudelleen poistamatta vanhoja. Oletusarvo on "Ei kukaan", jolloin tapahtuman luojana on kirjautunut käyttäjä.


![mceclip2.png](https://support.nepton.com/hc/article_attachments/11614834146589)
  * **Menneiden päivien määrä siirtotiedostossa.** Kuinka pitkältä ajanjaksolta tapahtumia on aineistossa. Mikäli asetus on määritelty, tapahtumien tuonti voi myös poistaa tapahtumia. Kaikki ne ajanjakson sisällä olevat tapahtumat poistetaan, jotka eivät ole aineistossa ja ovat henkilön "tapahtumien luojan" tallentamia.


![mceclip3.png](https://support.nepton.com/hc/article_attachments/11614834148509)
  * **Hyväksy tapahtumat tuonnin yhteydessä.** Mikäli asetus on käytössä, tapahtuman hyväksyjäksi asetetaan tapahtuman luoja.


![mceclip4.png](https://support.nepton.com/hc/article_attachments/11614788545949)
  * **Tapahtumatyyppien koodit.** Tapahtumien tuonnissa tapahtumatyyppi määräytyy aineiston sisältämän koodin mukaisesti. Tapahtumatyyppien koodit asetetaan valitsemalla **Työaika - > Työyhteisön asetukset -> Liittymät -> Tapahtumien tuonti. **


![mceclip0.png](https://support.nepton.com/hc/article_attachments/11614834153373)
Esimerkki: mikäli koodit on asetettu ylläolevan kuvan mukaisesti, ja tuontiaineisto sisältää tapahtumatyypin koodin "4", tuodaan tapahtuma vuosilomana.
Jos useita koodeja tarvitaan saman tapahtumatyypin luontiin, voidaan koodit lähettää pilkulla eriteltyinä esim. 1, 4. Jos koodissa itsessään tarvitaan pilkku, tulee se ympäröidä heittomerkeillä, esim. "1,2".
Huomaa, että voimassaolotoiminto ei päde tuonnissa määriteltäviin koodeihin, eli jos esim. koodi 4 on nyt käytössä vuosilomalle, koodilla 4 ei voida menneisyyteen tuoda mitään muuta tapahtumatyyppiä, kaikki koodilla 4 tulevat tapahtumat lisätään kalenteriin vuosilomana.
  * Jos tuontitiedosto sisältää otsikkorivin sarakkeille, aseta **Sarakkeiden järjestyksellä on väliä** arvoon **Ei**. 


![mceclip5.png](https://support.nepton.com/hc/article_attachments/11614788548637)
Tällöin tiedoston sarakkeiden otsikon on vastattava sarakkeen otsikkoa (Column title) ja kentän määritelmää asetuksissa. Esimerkiksi:  
  

![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080302541853)
  * Jos tuontitiedot eivät sisällä sarakkeiden otsikkoriviä, aseta **Sarakkeiden järjestyksellä on väliä** arvoon **Kyllä.**


![mceclip0.png](https://support.nepton.com/hc/article_attachments/11614834156445)
Valitse sarakkeen otsikkokenttä (Column title field) vastaamaan tiedoston sarakkaiden järjestystä. Esimerkiksi:  

![mceclip1.png](https://support.nepton.com/hc/article_attachments/21080324275357)
Huomioita tuonnin sarakkeista:
![](https://support.nepton.com/hc/article_attachments/18210942138013) | 
  * Tapahtumatyypin tunnus / Event type ID = vanha tapa viitata tapahtumaan, ei käyttöön uusissa toteutuksissa
  * Tapahtumatyypin sisäinen nimi / Event type internal name = vanha tapa viitata tapahtumaan, ei käyttöön uusissa toteutuksissa
  * **Merkitty tapahtumatyyppi** / **Customer defined event type code** = käytä tätä saraketta tapahtumien tuonneissa merkitsemään tuotavaa tapahtumaa (sairaspoissaolo, loma, jne)
  * Poissaolotyypin tunnus / Absence type ID = vanha tapa viitata tapahtumaan, ei käyttöön uusissa toteutuksissa
  * Poissaolo / sairauspoissaolo palkallinen päivämäärään/aikaan saakka sekä palkallinen päivämäärän/kellonajan jälkeen = sarakkeille voi antaa arvon vain poissolotapahtumille, joiden palkallisuutta voi muuttaa.

  
---|---  
## Muodosta aineisto oikeilla sarakkeilla ja sisällöllä
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080302547613)
### Siirtoaineiston tietosisällöt
Tapahtumalle voidaan tuoda seuraavia tietosisältöjä. Aineiston tuonnin yhteydessä voidaan valita sarakkeen tietosisältö. Tästä syystä sarakkeen otsikon tiedostossa ei tarvitse täsmätä tuotavan tietosisällön otsikkoon, eikä otsikkorivi ole pakollinen. Alla on kuvattu mahdolliset tietosisällöt ja niiden oikea muoto sarakkeella. Aineiston tulee sisältää pakolliseksi merkityt tiedot.
Tuotava tieto | Kuvaus  
---|---  
Henkilönumero | **Pakollinen tieto.**  
Henkilötunnus | Tapahtumaan liittyvän henkilön henkilötunnus.  
Tapahtumatyypin tunnus |  _Ei suositella käytettäväksi_. Tieto ei ole saatavilla kaikille tapahtumatyypeille.  
Tapahtumatyypin sisäinen nimi |  _Ei suositella käytettäväksi_. Tieto ei ole saatavilla kaikille tapahtumatyypeille.  
Merkitty tapahtumatyyppi |  **Pakollinen tieto.** Tuonnissa käytettävät tapahtumatyyppien koodit asetetaan valitsemalla**Työaika > Työyhteisön asetukset > Liittymät** **> Tapahtumien tuonti** #1 (tai muu tapahtumien tuonti, jos useita käytössä) **> Tapahtumatyyppien koodit.** ![mceclip0.png](https://support.nepton.com/hc/article_attachments/11614834153373) Mikäli koodit on asetettu ylläolevan kuvan mukaisesti, ja tuontiaineisto sisältää tapahtumatyypin koodin "4", tuodaan tapahtuma vuosilomana. Jos useita koodeja tarvitaan saman tapahtumatyypin luontiin, voidaan koodit lähettää pilkulla eriteltyinä esim. 1, 4. Jos koodissa itsessään tarvitaan pilkku, tulee se ympäröidä heittomerkeillä, esim. "1,2".  
Poissaolotyypin tunnus |  Mikäli luodaan poissaolo, tämä kenttä sisältää poissaolotyypin tunnuksen. Poissaolotyyppien tunnukset asetetaan valitsemalla **Työaika > Työyhteisön asetukset > Liittymät** **> Tapahtumien tuonti** #1 (tai muu tapahtumien tuonti, jos useita käytössä) > **Poissaolotyyppien koodit**.  
Aloituspäivä ja -aika / Lopetuspäivä ja -aika |  Tapahtuman aloituksen/lopetuksen päivä ja aika. Esimerkiksi. 2020-01-01 13:00:00. Ajat käsitellään käyttäjän paikallisena aikana ja näytetään, kuten ne on tuotu.  
Aloituspäivä ja -aika UTC /   
Lopetuspäivä ja -aika UTC |  Tapahtuman aloituksen/lopetuksen päivä ja aika, esimerkiksi. 2020-01-01 13:00:00. Ajat käsitellään UTC-aikavyöhykkeen aikana ja muutetaan Helsingin aikavyöhykkeeseen.  
Aloituspäivä / Lopetuspäivä |  Tapahtuman aloituksen/lopetuksen päivämäärä 2020-01-01 tai 01.01.2020  
Aloitusaika / Lopetusaika |  Tapahtuman aloituksen/lopetuksen kellonaika 24 tunnin muodossa Esimerkiksi 16:00:00, 16:00 tai 1600. Ajat käsitellään käyttäjän paikallisena aikana ja näytetään, kuten ne on tuotu.  
Kesto | Tapahtuman kesto desimaaleina tai HH:MM-muodossa. Esimerkiksi 4.5, 4,5 ja 04:30 ovat kaikki sallittuja muotoja.  
Kuvaus | Kuvaus.  
Ulkoinen tunniste |  Tapahtuman ulkoinen tunniste. Jos ulkoisella tunnisteella on jo olemassaoleva tapahtuma, tapahtuman tiedot päivitetään. Huom! Ulkoinen tunniste on tarkoitettu asetettavaksi liittymäkäyttäjän toimesta, kun tapahtuma tuodaan ulkoisesta järjestelmästä.  
Projektikoodi #_n_ | Tuonnin yhteydessä voidaan lisätä 6 projektia tapahtumaa kohden käyttäen eri sarakkeita: Ensimmäinen projektikoodi, toinen projektikoodi jne. Projektikoodit määritetään projektien hallinnassa. Jos tapahtumalle ei ole määritetty projektia, käytetään henkilön oletusprojektia.  
Työlisä #_n_ | Tapahtumaan voidaan liittää työlisiä käyttämällä työlisän koodeja (1 työlisä saraketta kohden), jotka on asetettu työlisät-asetuksissa. Tuonnissa lisätään tapahtumalle työlisän määrä (esim. 1h/kpl/€) riippuen työlisän tyypistä.  
Kertymän arvon asetus (tunnit desimaaleina) |  Asettaa kertymän arvon. Arvo annetaan desimaalitunteina. Tapahtumatyyppinä tulee olla jonkin kertymän arvon asetus.  
Kertymän arvon asetus (TT:MM) |  Asettaa kertymän arvon. Arvo annetaan muodossa TT:MM. Tapahtumatyyppinä tulee olla jonkin kertymän arvon asetus.  
Kertymän arvon asetus (päivää) | Asettaa kertymän arvon. Arvo annetaan päivissä. Tapahtumatyyppinä tulee olla jonkin kertymän arvon asetus.  
Kertymän arvon muutos (+tunnit desimaaleina) | Lisää tai vähentää kertymän arvoa. muutos annetaan desimaalitunteina. Tapahtumatyyppinä tulee olla jonkin kertymän arvon muutos.  
Kertymän arvon muutos (+TT:MM) | Lisää tai vähentää kertymän arvoa. Muutos annetaan muodossa TT:MM. Tapahtumatyyppinä tulee olla jonkin kertymän arvon muutos.  
Kertymän arvon muutos (+päivää) | Lisää tai vähentää kertymän arvoa. Muutos annetaan päivissä. Tapahtumatyyppinä tulee olla jonkin kertymän arvon muutos.  
Poissaolo tai sairauspoissaolo palkallinen päivämärään/kellonaikaan saakka |  Luo tapahtuman kahtena eri tapahtumana, joista
  * Ensimmäinen alkaa rivillä määritetyllä tapahtuman alkuajalla ja päättyy rivillä määritettyyn poissaolo / sairauspoissaolo palkallinen päivämäärään/kellonaikaan saakka -tietoon. Tapahtuma luodaan palkallisena.
  * Toinen alkaa rivillä määritetyllä poissaolo / sairauspoissaolo palkallinen päivämäärään/kellonaikaan saakka -tiedolla ja päättyy rivillä määritettyyn tapahtuman loppuaikaan. Tapahtuma luodaan palkattomana.

Tieto voidaan määrittää vain sairauspoissaoloille ja poissaoloille, joiden palkallisuus on muutettavissa.  
Poissaolo tai sairauspoissaolo palkallinen päivämärän/kellonajan jälkeen |  Luo tapahtuman kahtena eri tapahtumana, joista
  * Ensimmäinen alkaa rivillä määritetyllä tapahtuman alkuajalla ja päättyy rivillä määritettyyn poissaolo / sairauspoissaolo palkallinen päivämäärän/kellonajan jälkeen -tietoon. Tapahtuma luodaan palkattomana.
  * Toinen alkaa rivillä määritetyllä poissaolo / sairauspoissaolo palkallinen päivämäärän/kellonajan jälkeen -tiedolla ja päättyy rivillä määritettyyn tapahtuman loppuaikaan. Tapahtuma luodaan palkallisena.

Tieto voidaan määrittää vain sairauspoissaoloille ja poissaoloille, joiden palkallisuus on muutettavissa.  
## Tuo tapahtumat
Tapahtumat tuodaan valitsemalla **Työaika > Hallinta >** **Liittymät**** > Tapahtumien tuonti. **Menneiden päivien määrä-asetukseen ei tarvitse asettaa mitään siinä tapauksessa, jos liittymän asetuksiin ei ole määritetty menneiden tuontipäivien määrää ollenkaan. 
Huom! Manuaalista tuontia tehdessä tulee olla kirjautuneena Neptoniin samana käyttäjänä kuin ajastetussa tuonnissa. Mikäli käytetään muuta kuin ajastetun tuonnin asetuksissa määritettyä käyttäjää, poistetaan manuaalisen tuonnin suorittavan henkilön omat tapahtumat, mikäli tapahtumat eivät ole mukana siirrettävässä aineistossa.
Huom! Toistaiseksi "Tuo päivämäärästä alkaen" sijasta tulee käyttää vaihtoehtoa "menneiden päivien määrä siirtotiedostossa". Esimerkiksi jos tuontia ollaan tekemässä 10.4.2024 ja tuodaan tapahtumia päivämäärälle 1.4.2024 niin menneiden päivien määrä siirtotiedostossa -kenttään tulee määrittää arvoksi 9. Eli lasketaan taaksepäin päivien määrä siihen päivämäärään johon tapahtumia ollaan tuomassa, pois lukien parhaillaan kuluva päivä.
![](https://support.nepton.com/hc/article_attachments/16003696872733)
  * Valitse tiedosto laitteeltasi ja paina **käynnistä.**
