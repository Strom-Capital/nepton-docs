---
id: 360002868137
title: Tapahtumien tuonti käyttöliittymän aineistolatauksella - tuonnissa valittava
  rakenne
url: https://support.nepton.com/hc/fi/articles/360002868137-Tapahtumien-tuonti-k%C3%A4ytt%C3%B6liittym%C3%A4n-aineistolatauksella-tuonnissa-valittava-rakenne
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels:
- lomat
- vuosiloma
- tapahtumien tuonti
- tapahtumatuonti
- vuosilomaoikeus
- lomaoikeus
- vuosilomasaldo
- lomapäivä
- lomatuonti
- esikatselu
promoted: false
updated_at: '2026-03-04T09:21:44Z'
edited_at: '2025-01-08T13:06:40Z'
---

# Tapahtumien tuonti käyttöliittymän aineistolatauksella - tuonnissa valittava rakenne

Tässä artikkelissa kuvataan tapahtumien aineistolataus tuonnissa valittavalla rakenteella. Tapahtumien tuontiin käyttöliittymästä on muitakin tapoja, jotka ovat kuvattu [täällä](<https://support.nepton.com/hc/fi/articles/4404767615249>).
Tässä artikkelissa käydään läpi **Työkaluvalikon Tapahtumatietojen tuonti toiminnallisuus ja sille vaadittavat määritykset.** Artikkelin lopussa liitteenä on esimerkkitiedosto tapahtumien tuomiseksi.
Tapahtumien tuonti tehdään valikossa **Työaika** > **Työkalut** > **Tapahtumien tuonti**. Tapahtumien tuonnin määritykset tulee tehdä ennen ensimmäisen aineiston lataamista käyttöliittymästä tai ennen ensimmäistä aineiston ajastettua lataamista.
Tämä tuontitapa toimii vain silloin jos on asetettu yhdet Tapahtuman tuonti - asetukset. Jos on tarve tehdä useita Tapahtumien tuonti - asetuksia, tulee käyttää [Tapahtumien tuonti käyttöliittymän aineistolatauksella - ennalta määritetty rakenne](<https://support.nepton.com/hc/fi/articles/4419484517521>) \- tuontia.
## Tapahtumien manuaalinen tuonti (Työkalut)
### Yleistä aineistosta
  * Tiedot voidaan lukea palveluun otsikkorivillä tai ilman otsikkoriviä. Otsikon sarakkeet voivat olla minkä nimisiä tahansa. Sarakkeiden tietosisällöt määritellään luettavaan muotoon Neptonissa tapahtumatietojen tuonnin yhteydessä.
  * Tapahtumia tuodaan henkilöille, joilla on palvelussa henkilönumero.
  * Tiedostossa yhden tapahtuman tiedot tulee olla yhdellä rivillä.
  * Jos yhdessä tiedostossa on yli 10 000 riviä, on suositeltavaa jakaa se useampaan tiedostoon.
  * Mikäli projekti on asetettu tapahtumien kirjaamisessa pakolliseksi, niin aineistolla tulee olla tapahtuman projektitieto.
  * Muotoile sarakkeet Excelissä tekstiksi ennen tuontia, näin tieto pysyy oikeanlaisena.
  * Tapahtumien tuonti -toiminto mahdollistaa tuonnin käyttäen seuraavia tiedostotyyppejä: CSV, XLSX, XLS, ODS.


## Tietojen tuonnin vaiheet (Työkalut)
### Määrittele tuotavien tapahtumien tapahtumatyyppikoodit
Tapahtumien tuonnilla tapahtumatyyppi muodostuu aineistossa siirretyn koodin mukaisena. Koodi voi olla mikä tahansa tuotavaa tapahtumaa kuvaava, esim. Saldon asetus-tapahtuman koodilla SA. Tapahtumatyyppien koodit asetetaan valitsemalla **Työaika > Työyhteisön asetukset > Liittymät > Tapahtumien tuonti #1. **
**HUOM!** Tapahtumatyypin koodi tulee aina asettaa nimenomaan **Tapahtumien tuonti #1:n määrityksissä.**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080302494877)
Jos esimerkiksi koodit on asetettu yllä olevan esimerkin mukaisesti ja tuontitiedostossa on tapahtumatyypin koodi "4", tuodaan tapahtuma vuosilomana. Aineistolta löytyvä koodi "3" taas tuotaisiin Neptoniin viikkovapaana.
Jos useita koodeja tarvitaan saman tapahtumatyypin luontiin, voidaan koodit lähettää pilkulla eriteltyinä esim. 1, 4. Jos koodissa itsessään tarvitaan pilkku, tulee se ympäröidä heittomerkeillä, esim "1,2".
### Muodosta aineisto oikeilla sarakkeilla ja sisällöllä
Esimerkkiaineisto löytyy ladattavana Excel-tiedostona tämän ohjeen lopusta.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080324213277)
### Siirtoaineiston tietosisällöt
Tapahtumalle voidaan tuoda seuraavia tietosisältöjä. Aineiston tuonnin yhteydessä voidaan valita sarakekohtaisesti minkä tietosisällön sarake sisältää. Tästä syystä sarakkeen otsikon tiedostossa ei tarvitse täsmätä tuotavan tietosisällön otsikkoon, eikä otsikkorivi ole pakollinen. Alla on kuvattu eri tietosisällöt ja missä muodossa tieto tulee olla sarakkeella. Aineiston tulee sisältää pakolliseksi merkityt tiedot.
Huomioithan, että jokin kolmesta aloitusajan tiedosta on oltava aineistolla. Useimpia tapahtumatyyppejä tuodessa myös lopetusaika on oltava aineistolla.
Tuotava tieto | Kuvaus  
---|---  
Henkilönumero | **Pakollinen tieto.**  
Tapahtumatyypin koodi |  **Pakollinen tieto.** Tuonnissa käytettävät tapahtumatyyppien koodit asetetaan valitsemalla**Työaika > Työyhteisön asetukset > Liittymät** **> Tapahtumien tuonti** #1 (tai muu tapahtumien tuonti jos useita käytössä) **> Tapahtumatyyppien koodit.** Tätä ei tule sekoittaa Työtuntien alla oleviin Tapahtumatyyppien asetuksiin. ![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080302494877) Jos esimerkiksi koodit on asetettu yllä olevan esimerkin mukaisesti ja tuontitiedostossa on tapahtumatyypin koodi "4", tuodaan tapahtuma vuosilomana. Jos useita koodeja tarvitaan saman tapahtumatyypin luontiin, voidaan koodit lähettää pilkulla eriteltyinä esim. 1, 4. Jos koodissa itsessään tarvitaan pilkku, tulee se ympäröidä heittomerkeillä, esim "1,2".  
Poissaolotyypin tunnus |  Mikäli luodaan poissaolo, tässä kentässä määritellään poissaolotyyppin tunnus. Poissaolotyyppien tunnukset määritetään työyhteisön asetuksissa **Liittymät > Tapahtumien tuonti** #1 (tai muu tapahtumien tuonti jos useita käytössä) **> Poissaolotyyppien koodit.**  
Aloituspäivä ja -aika / Lopetuspäivä ja -aika |  Tapahtuman aloituksen/lopetuksen päivä ja aika, esimerkiksi. 2020-01-01 13:00:00. Ajat käsitellään käyttäjän paikallisena aikana ja näytetään kuten on tuotu.  
Aloituspäivä ja -aika UTC /   
Lopetuspäivä ja -aika UTC |  Tapahtuman aloituksen/lopetuksen päivä ja aika, esimerkiksi. 2020-01-01 13:00:00. Ajat käsitellään UTC-aikavyöhykkeen aikana ja muutetaan Helsingin aikavyöhykkeeseen.  
Aloituspäivä / Lopetuspäivä |  Tapahtuman aloituksen/lopetuksen päivämäärä 2020-01-01 tai 01.01.2020.  
Aloitusaika / Lopetusaika |  Tapahtuman aloituksen/lopetuksen kellon aika 24 tunnin muodossa, esimerkiksi 16:00 tai 1600. Ajat käsitellään käyttäjän paikallisena aikana ja näytetään kuten on tuotu.  
Kuvaus | Kuvaus.  
Ulkoinen tunniste |  Tapahtuman ulkoinen tunniste. Jos ulkoisella tunnisteella löytyy jo olemassaoleva tapahtuma, tapahtuman tiedot päivitetään. Huom! Ulkoinen tunniste on tarkoitettu asetettavaksi integraatiokäyttäjän toimesta, kun tapahtuma tuodaan ulkoisesta järjestelmästä.  
Projektikoodi #_n_ | Tuonnin yhteydessä voidaan viedä 6 projektia per tapahtuma käyttäen eri sarakkeita: ensimmäinen projektikoodi, toinen projektikoodi jne. Projektikoodit määritetään projektien hallinnassa. Jos tapahtumalle ei ole määritetty projektia, käytetään kohdehenkilön oletusprojektia.  
Työlisä #_n_ | Tapahtumaan voidaan liittää työlisiä käyttämällä Työlisän koodeja (1 työlisä per sarake), jotka oon asetettu Työlisät-asetuksissa. Tuonnin yhteydessä tuodaan työlisän arvo tapahtumalle esim. 1h/kpl/€, riippuen työlisän tyypin määrityksistä.  
Kertymän arvon asetus (tunnit desimaaleina) |  Asettaa kertymän arvon. Arvo annetaan tunnit desimaaleina -muodossa. Tapahtumatyyppinä tulee olla jonkin kertymän arvon asetus.  
Kertymän arvon asetus (TT:MM) |  Asettaa kertymän arvon. Arvo annetaan TT:MM -muodossa. Tapahtumatyyppinä tulee olla jonkin kertymän arvon asetus.  
Kertymän arvon asetus (päivää) | Asettaa kertymän arvon. Arvo annetaan päivissä. Tapahtumatyyppinä tulee olla jonkin kertymän arvon asetus.  
Kertymän arvon muutos (+tunnit desimaaleina) | Lisää tai vähentää kertymän arvoa. Muutos annetaan tunnit desimaaleina -muodossa. Tapahtumatyyppinä tulee olla jonkin kertymän arvon muutos.  
Kertymän arvon muutos (+TT:MM) | Lisää tai vähentää kertymän arvoa. Muutos annetaan TT:MM -muodossa. Tapahtumatyyppinä tulee olla jonkin kertymän arvon muutos.  
Kertymän arvon muutos (+päivää) | Lisää tai vähentää kertymän arvoa. Muutos annetaan päivissä. Tapahtumatyyppinä tulee olla jonkin kertymän arvon muutos.  
### Tuo tapahtumat
Tuodaksesi tapahtumat, valitse **Työaika - > Työkalut -> Tapahtumien tuonti.**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080324218909)
  * Valitse **tiedosto** laitteeltasi.
  * Tarvittaessa valitse onko ensimmäinen rivi **otsikko**. Oletuksena tämä on automaattinen.


![mceclip7.png](https://support.nepton.com/hc/article_attachments/21080302496413)
  * Tässä vaiheessa voidaan määrittää, **hyväksytäänkö tuodut tapahtumat.**


![mceclip2.png](https://support.nepton.com/hc/article_attachments/21080302511517)
  * **Tuonnin esikatselussa** määritä jokaiselle sarakkeen **tietosisältö**. Mikäli joidenkin sarakkeiden tiedot ovat tuonnissa tarpeettomia, voit ohittaa ne valitsemalla **ohita sarake**. Ohitettujen sarakkeiden tietoja ei tuoda.


![mceclip8.png](https://support.nepton.com/hc/article_attachments/21080302501277)
  * Palvelu tarkistaa tiedoston ja korostaa virheelliset sarakkeet punaisella. Sarakkeessa olevan virheen kuvauksen näet napsauttamalla virheellistä saraketta hiirellä.


![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080324215325)
  * Kun tuotavista tiedoista ei löytynyt virheitä, palvelu palauttaa viestin:


![mceclip9.png](https://support.nepton.com/hc/article_attachments/21080324235037)
  * Palvelu ilmoittaa, että tapahtumat on tuotu.


![mceclip10.png](https://support.nepton.com/hc/article_attachments/21080302506909)
## Esimerkkejä vuosilomasaldon tuonnista
### Vuosilomasaldon muuttaminen (olemassa olevan vuosilomasaldon päälle)
Henkilön tällä hetkellä käytettävissä olevan vuosilomasaldon muutos tuodaan palveluun sille päivälle, josta eteenpäin muutos halutaan voimaan. Muutos lisää tai vähentää henkilöllä käytettävissä olevia vuosilomapäiviä. 
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4914271245341)
Kun tiedosto luetaan palveluun, aineiston sarakkeille valitaan niiden sisältämä tieto alasvetovalikoista. Solut esitetään vihreänä silloin kun sisällön muoto vastaa valittua saraketta. Tapahtumien tuonti kuvattu tässä ohjeessa ylempänä kohdassa 3. 
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4914349617821)
Esimerkiaineistossa on havainnollisuuden vuoksi vain yksi henkilö. Lopputuloksena henkilölle henkilönumerolla 0101 luodaan tapahtuma Vuosilomasaldon ansainnan muutos päivälle 31.3.2022. Tämä vuosilomasaldo on käytettävissä 1.4.2022 alkaen sisältäen henkilöllä jo mahdollisesti aiemmin olleen vuosilomasaldon. 
### Vuosilomasaldon asettaminen (korvaten jo olemassa olevan vuosilomasaldon)
Henkilön edellisenä lomanmääräytymisvuotena ansaitsema lomaoikeus tulee asettaa saman lomanmääräytymisvuoden puolelle. Näin henkilöllä on käytössään nämä vuosilomat 1.4. alkaen. Lomaoikeudet voi tuoda palveluun alla olevan esimerkin mukaisella tiedostolla. 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4914264468381)
Kun tiedosto luetaan palveluun, aineiston sarakkeille valitaan niiden sisältämä tieto alasvetovalikoista. Solut esitetään vihreänä silloin kun sisällön muoto vastaa valittua saraketta. Tapahtumien tuonti kuvattu tässä ohjeessa ylempänä kohdassa 3. 
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4905253810973)
Esimerkiaineistossa on havainnollisuuden vuoksi vain yksi henkilö. Lopputuloksena henkilölle henkilönumerolla 0101 luodaan tapahtuma Vuosilomasaldon ansainnan asetus päivälle 31.3.2022. Tämä vuosilomasaldo on käytettävissä 1.4.2022 alkaen ja se korvaa mahdollisesti aiemmin henkilöllä olleen vuosilomasaldon määrän.
