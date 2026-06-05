---
id: 360003685277
title: Kirjauspäätemallit
url: https://support.nepton.com/hc/fi/articles/360003685277-Kirjausp%C3%A4%C3%A4temallit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä kirjauspäätteistä
section_id: 360005942558
section_path:
- Kirjauspäätteet
- Yleistä kirjauspäätteistä
labels:
- leimauspäätteet
- kirjauspääte
- työaikaterminaali
- malli
- mallit
promoted: false
updated_at: '2025-09-03T07:04:24Z'
edited_at: '2025-09-03T07:04:24Z'
---

# Kirjauspäätemallit

Tässä artikkelissa kuvaamme millaisia kirjauspäätemalleja Nepton tällä hetkellä tarjoaa. Jos tarvitset tietoa vanhemmasta päätelaitemallista olethan yhteydessä omaan sopimustahoosi.
**Tiedot löytyvät myös osoitteesta****<https://nepton.fi/tyoaikapaatteet/>**
## Yleistä kirjauspäätteistä
Kirjauspäätteillä tapahtumat kirjataan reaaliaikaisesti.
Reaaliaikainen kirjaus näkyy kalenteri- ja taulukkonäkymissä ikonina kellonaikojen ja tapahtumatyypin nimen välissä.
Tapahtumaerittely-raportilla näkyy kirajuspäätteen Id, jos tapahtuma on kirjattu kokonaisuudessaan työaikapäätteellä. Tilanteessa, jossa kirjaus on aloitettu ja lopetettu eri työaikapäätteellä, näytetään sen kirjauspäätteen Id, jolla tapahtuma on aloitettu.
Käytettäessä Nepton Rugged -kirjauspäättettä, kalenteri- tai taulukkonäkymässä ei ole ikonia eikä Tapahtumaerittely-raportilla ole kirjauspäätteen Id:tä. Tämä johtuu käytetystä tekniikasta, jolla kirjauspäätteet keskustelevat palvelun kanssa ja Nepton Rugged -kirjauspäätteiden tekniikka ei mahdollista edellä mainittuja omiaisuuksia.
![](https://support.nepton.com/hc/article_attachments/26370836399261)
## Nepton Touch
Laitteessa on käytetty laadukkaita materiaaleja ja siinä on sisäänrakennettu kaiutin ja RFID-lukija. Tämä laite on ollut käytössä syyskuusta 2022 alkaen. 
Kirjauspäätteitä voidaan käyttää offline-tilassa, koska niissä on tilaa tuhansien työaikakirjausten tallentamiseen muistiin. Laitteeseen tallennetut kirjaukset siirretään Neptoniin heti, kun laite on jälleen yhteydessä internetiin.
![p__telaite_uusi.png](https://support.nepton.com/hc/article_attachments/21079175944989)
### Tärkeimmät ominaisuudet
  * Kirjautuminen PIN-koodilla tai RFID-tunnisteella
  * Korkean resoluution 10,1" A+-luokan LCD-kosketusnäyttö
  * Realtech RTL811E gigabit verkkokortti (RJ45/Ethernet)
  * Voidaan ottaa käyttöön heti, kun olet muodostanut yhteyden Internetiin
  * Helppo seinäasennus mukana toimitetulla VESA-seinäkiinnityssarjalla
  * Windows 10 IOT Enterprise LTSC -käyttöjärjestelmä
  * SSD-kiintolevy ja Intel Celeron -suoritin
  * Voidaan käyttää ruokalapäätteenä
  * Voidaan käyttää olemassa olevia kulunvalvonnan RFID-tunnisteita
  * ISO14443-A- ja ISO14443-B-standardien mukainen RFID-lukija taajuudella 13,56 MHz:  

    * Esimerkkejä yhteensopivista RFID-tunnisteista: MIFARE® DESFire: UID + Application files , MIFARE® Classic: UID + Sectors, MIFARE® Ultralight UID + pages, MIFARE® Plus UID security levels 1 and 3, MIFARE® SmartMX (MIFARE® Classic and MIFARE® DESFire EV1 emulation modes), NFC (UID), Mifare Classic 7 Byte UID + sectors, Legic, ISO15693 (UID)
  * Mahdollisuus käyttää ulkoista RFID-lukijaa, joka tarjoaa tuen usealle tunniste-teknologialle. Ohje ulkoisen lukijan tukemiin tunnisteisiin löytyy [täältä](<https://support.nepton.com/hc/fi/articles/10357648361757>).
  * Virransyöttöön voidaan käyttää POE+ ja POE++ jakolaitteita (30 Watin tehovaatimus). Jakolaitteessa tulee olla erillinen virran ulostulo (esim. Planet POE-172S), joka kytketään laitteen virtaliittimeen. Jos ethernet-johdossa ei ole PoE-syöttöä, tarvitaan vielä erillinen PoE-injektori (esim. Ernitec Electra-P2-60W).
  * Ympäristön käyttölämpötila -20 - +70 °C
  * Valmistettu kestävästä alumiiniseoksesta pitkäikäisyyden takaamiseksi  

  * Laitteen mitat:   
Korkeus 19,4 cm  
Leveys 37,4 cm  
Syvyys 6 cm


### Kosketusnäytön puhdistaminen
  * Käytä pehmeää, puhdasta, nukkaamatonta liinaa, mikrokuituliina toimii parhaiten.
  * Kostuta liina kevyesti vedellä tarvittaessa. Voit käyttää myös yleisesti kosketusnäyttöihin tarkoitettuja puhdistusaineita. Muista kuitenkin, että laitetta ei tule kastella märäksi.
  * Pyyhi näyttö varovasti liinalla.


## Nepton-Flexim 
Nepton-Flexim -pääte on otettu käyttöön osana Neptonin laitetarjontaa syksyllä 2024. Päätteissä on oma Nepton-ohjelmisto (tuotantojulkaisuversio 5.0.1). Seuraavat jo käytössä olevat Nepton-Flexim -pääterautamallit voidaan päivittää Neptonin tuottamaan ohjelmistoon:
  * SACCTP1_121000 : prox tunnistelukija
  * SACCTM1_121000 : mifare tunnistelukija
  * SACCTC1_121000 : ABLOY SEOS tunnistelukija
  * SACCWPM_121000 (monitunnistelukija: prox, mifare, SEOS)
  * SACCWPP_121000 (monitunnistelukija: prox, mifare, SEOS)


Edellä mainittuja päätemalleja käyttävät asiakkamme voivat tarkistaa omista päätteistään, ovatko ne päivitettävissä uuteen Nepton-ohjelmistoon seuraavasti: mikäli laitteesta löytyvä sarjanumero alkaa numerolla kolme (3), on laite mahdollista päivittää. 
Uutta päätemallia SACCWPP_121000 on saatavissa uutena Neptonilta. 
![](https://support.nepton.com/hc/article_attachments/23473490428317)
Tärkeimmät toiminnallisuudet:
  * **Kirjautuminen** : tunnisteella, PIN-koodilla (voidaan asettaa päälle/pois päätekohtaisesti) tai pikakirjaus (tunnisteen näyttäminen lukijaan aloittaa / lopettaa tehtävän. Pikakirjauskin voidaan asettaa päälle/pois päätekohtaisesti)
  * **Tapahtumien kirjaus** : samaan tapaan kuin nepton Touch-laitteessa 
    * Valittavia painikkeita aloitusnäytöllä kahdeksan (8) kappaletta kerrallaan. Mikäli useampi painike käytössä, sivunvaihtonuoli toimii indikaattorina.
    * Pääte kirjaa käyttäjän oletuksena ulos 20 sekunnin viiveellä, mikäli laite on tämän ajan käyttämättömänä. Uloskirjauksen viivettä voi muuttaa. ![](https://support.nepton.com/hc/article_attachments/23473490434333)
  * **Lisien kirjaus**
    * Lisien kirjaaminen mahdollista tapahtuman aloittamisen jälkeen
    * Lisät-välilehdellä näkyy neljä (4) kappaletta valittavissa olevaa lisää.
    * Lisien tyyppi ja oletusarvot tulevat Neptonin asetusryhmän mukaan. 
    * Pikavalintojen kautta lisiä voi vähentää (miinus-painike) tai lisätä (plus-painike) itse määritellyin välein, esimerkiksi 5, 10 tai 15min kerrallaan.   
![](https://support.nepton.com/hc/article_attachments/23473474042013)  
  

      * Kynäikonia painamalla voidaan antaa tarkempi, minuuttikohtainen arvo  
  
![](https://support.nepton.com/hc/article_attachments/23473474044445)  
  

  * **Ylityötyypin valinta**
    * Ylityö-välilehdeltä voidaan vaihtaa ylitöiden kohdenne. Näkyvillä henkilön asetusryhmän mukaiset vaihtoehdot.  
  
![](https://support.nepton.com/hc/article_attachments/23473474048797)
  * **Projektikohdistus**
    * Projektit-välilehdeltä voidaan valita työlle haluttu projektikohdistus
    * Vaihtoehtoina näytetään viimeksi kirjatut vaihtoehdot  
  
![](https://support.nepton.com/hc/article_attachments/23473490446365)
    * Hakutoimintoa hyödyntämällä saadaan muut kuin viimeksi kirjatut vaihtoehdot näkyville  
  
![](https://support.nepton.com/hc/article_attachments/23473490449181)
    * Projekti voidaan valita myös viivakoodinlukijalla, edellyttäen, että henkilö on kirjautunut tunnisteella päätteelle. Viivakoodinluvun jälkeen projektikohdistus käynnistyy ja henkilö kirjautuu automaattisesti ulos päätteeltä. Nepton tarjoaa Nepton Flexim-kirjauspäätteen toimituksissa viivakoodinlukijaa, josta tarkemmin tietoa [täällä.](<https://support.nepton.com/hc/fi/articles/30052854847517>)
  * **Päätteen käyttöönotto**
    * Uusi pääte ilmoittaa käynnistyessään päätteen numeron, jolla pääte voidaan liittää Nepton-ympäristöön.


## Nepton Rugged
Nepton Rugged (NFC TimeClean Basic) on kompakti ja kestävä, siinä on mobiiliyhteys tiedonsiirtoa varten ja sisäänrakennettu akku. Käyttöön tarvitaan ainoastaan virransyöttö verkkolaitteelle.
![](https://mlavatqvr5rz.i.optimole.com/w:702/h:702/q:90/f:best/https://nepton.fi/wp-content/uploads/nepton_rugged.png)
### Tärkeimmät ominaisuudet
    * Kirjautuminen PIN-koodilla tai RFID/NFC-tunnisteella
    * Kompakti suunnittelu ja rakenne, sisäänrakennettu akku ja internet-yhteys GSM-verkon kautta
    * Laite toimii joko verkkojännitteellä (100..250VAC) tai ajoneuvossa (10..30VDC)
    * Helppo seinäasennus
    * ISO14443-A- ja ISO14443-B-standardien mukainen RFID-lukija taajuudella 13,56 MHz:
      * Esimerkkejä yhteensopivista RFID-tunnisteista: MIFARE® DESFire: UID + Application files , MIFARE® Classic: UID + Sectors, MIFARE® Ultralight UID + pages, MIFARE® Plus UID security levels 1 and 3, MIFARE® SmartMX (MIFARE® Classic and MIFARE® DESFire EV1 emulation modes), NFC (UID), Mifare Classic 7 Byte UID + sectors, Legic, ISO15693 (UID)
    * IP66-suojattu kotelo, ympäristön käyttölämpötila 0 - +50 °C
    * Värilliset valot, summeri ja kaiutin
    * Valmistettu muovista mahdollistaen helpon ja kevyen asennuksen
