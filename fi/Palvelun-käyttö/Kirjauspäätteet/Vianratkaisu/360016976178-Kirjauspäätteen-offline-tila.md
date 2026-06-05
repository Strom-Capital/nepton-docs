---
id: 360016976178
title: Kirjauspäätteen offline-tila
url: https://support.nepton.com/hc/fi/articles/360016976178-Kirjausp%C3%A4%C3%A4tteen-offline-tila
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Vianratkaisu
section_id: 360005896337
section_path:
- Kirjauspäätteet
- Vianratkaisu
labels:
- vianselvitys
promoted: false
updated_at: '2024-08-23T09:20:17Z'
edited_at: '2024-05-21T07:24:42Z'
---

# Kirjauspäätteen offline-tila

Nepton-pääteohjelmisto voi toimia väliaikaisesti ilman Internet-yhteyttä. Kun yhteys katkeaa, ohjelmisto siirtyy "offline-tilaan". Sen avulla käyttäjät voivat jatkaa tapahtumien merkitsemistä vain pienillä muutoksilla ja rajoituksilla toiminnallisuuteen. Kun yhteys on palautettu, päätelaite muodostaa automaattisesti yhteyden ja synkronoi offline-merkinnät Nepton-alustaan.
Tämä ominaisuus on tarkoitettu lieventämään lyhyiden Internet-keskeytysten ja tilapäisten verkko-ongelmien vaikutusta päivittäiseen työelämään. Internet-yhteys on pyrittävä palauttamaan mahdollisimman pian.
## Ongelman kartoittaminen
Offline-tila voidaan ottaa pois käytöstä poikkeuksellisissa olosuhteissa tai asiakkaan pyynnöstä. Tämä estää kirjautumisen tai merkintöjen tekemisen päätelaitteella silloin kun laite ei ole yhteydessä Neptonin palvelimiin.
Ohjeita päätelaitteiden käyttöön ja ongelmien kartoittamiseen löytyy useista artikkeleista. Voit hakea artikkeleita haulla tai tutustua [**Kirjauspäätteen käyttö**](<https://support.nepton.com/hc/fi/sections/360002084697-Kirjausp%C3%A4%C3%A4tteen-k%C3%A4ytt%C3%B6>) -osioon.
Katso myös: [Kirjauspääte ei löydä verkkoyhteyttä](<https://support.nepton.com/hc/fi/articles/360002588757>)  
  

## Mistä tiedän että päätelaite on offline-tilassa?
Nepton -päätelaite menee offline-tilaan tunnistaessaan, että yhteyttä Neptonin palvelimiin ei ole saatavilla. Tämä toiminnallisuus on tehty vähentämään lyhyiden Internet-yhteyden katkoksien ja väliaikaisten verkko-ongelmien vaikutusta päivittäiseen työelämään. Internet-yhteys tulee palauttaa niin pian kuin mahdollista.
Offline-tila ilmoitetaan punaisella tilarivillä näytön alareunassa kuten alla olevassa kuvassa.
**![Terminal_offline_1.png](https://support.nepton.com/hc/article_attachments/360015697077)**
## Yhteyden uudelleen ottaminen ja synkronointi
Kun päätelaite on offline-tilassa, se tarkistaa pienin väliajoin yhteyden tilaa, ja ottaa yhteyden uudelleen heti kun mahdollista. Kun päätelaite saa uudelleen yhteyden Neptonin palvelimiin, se synkronisoi automaattisesti datan, jonka käyttäjä on tallentanut offline-tilassa Neptonin palvelimille.
Offline-tilan merkintöjen synkronisointi on nopeaa, mutta merkintöjen ilmestymisessä kalenteriin voi esiintyä viivettä, jos offline-tilasta siirrettävän tiedon määrä on suuri.
Kun päätelaitteen yhteys on toiminnassa, normaalit toiminnot ovat käytettävissä ja laitteen alareunan tilarivi näyttää vihreää kuten alla olevassa kuvassa.
**![Terminal_online_1.png](https://support.nepton.com/hc/article_attachments/360015697117)**
## Rajoitukset
### Kirjautuminen
Offline-tilassa sisäänkirjautumista ei voida vahvistaa Neptonin palvelinta vasten, vaan kirjautumiseen käytetään päätelaitteen omaa välimuistia. Tuntemattomat ja ensimmäistä kertaa päätelaitetta käyttävät käyttäjät voivat kirjautua päätelaitteeseen RFID-tunnisteella, mutta pystyvät tallentamaan vain oletustapahtumatyyppejä ja projekteja. Riippuen ympäristön asetuksista, tämä voi tarkoittaa, että projekteja ei ole saatavilla. Katso seuraavasta otsikosta lisätietoja tapahtumatyyppien ja projektien rajoitteista offline-tilassa.
**Tärkeä huomio:** Jos merkinnät tehdään tuntemattomilla tunnisteilla ja näitä tunnisteita ei ole asetettu Neptonin palveluun, kun päätelaite ottaa uudelleen yhteyden, merkintöjä **ei** synkronoida Neptoniin.
### Tapahtumatyypit ja projektit
Kaikki päätelaitteet turvautuvat päätelaitteen välimuistiin tapahtumatyyppien ja projektien määrittämiseen offline-tilassa. Välimuisti päivittyy silloin kun päätelaitetta käytetään sen ollessa yhteydessä Neptonin palvelimiin, eli toisin sanoen välimuisti **ei** päivity offline-tilassa.
Jos päätelaitteella on tehty vähintään yksi onnistunut sisäänkirjautuminen päätelaitteen ollessa yhteydessä Neptonin palvelimiin, oletustapahtumatyypit ja oletusprojektit tallennetaan välimuistiin. Tämän johdosta tuntemattomat ja ensimmäistä kertaa palvelua käyttäjät voivat tehdä merkintöjä käyttäen oletustapahtumatyyppejä ja oletusprojekteja.
**Tärkeä huomio:** Offline-tilassa käytetty välimuisti on päätelaitekohtainen eikä sitä jaeta eri päätelaitteiden välillä. Tämän johdosta käyttäjä voi nähdä erilaisia valintoja eri päätelaitteiden offline-tilassa, riippuen siitä kumpaa päätelaitetta käyttäjä on viimeksi käyttänyt.  
  

### Tapahtumien kirjaaminen ja henkilön tila
Koska päätelaite ei ole yhteydessä Neptonin palvelimiin, henkilön sen hetkistä työn tilaa tai kertymätietoa ei voida näyttää.
Koska sen hetkinen työn tila ei ole tiedossa, päätelaite ei pysty tarjoamaan tai tulkitsemaan pitääkö tehdyn merkinnän aloittaa, lopettaa vai lopettaa ja aloittaa tapahtuma. Tästä johtuen offline-tilan käyttäjien tulee määrittää, onko tehdyn merkinnän toimenpide tapahtuman aloittaminen vai lopettaminen. Tapahtuman aloittaminen tai lopettaminen tehdään kirjauksen yhteydessä käyttäen "Aloita" tai "Lopeta" - painikkeita, esimerkki näkymästä alla olevassa kuvassa. Kuitenkin ensin pitää valita tapahtumatyyppi, eli esimerkiksi "Työ", jotta Aloita-nappi aktivoituu. Jos halutaan päättää käynnissä oleva tapahtuma, pitää Työ-nappia painaa vielä uudelleen, jotta Lopetus-nappi aktivoituu kts. kuvat:
**![Terminal_offline_3.png](https://support.nepton.com/hc/article_attachments/360015771098)**
**![mceclip0.png](https://support.nepton.com/hc/article_attachments/9082153680413)**
**![mceclip1.png](https://support.nepton.com/hc/article_attachments/9082155316381)**
### Offline-tilan kesto
Käytössä olevien päätteiden suositellaan olevan aina verkkoyhteydessä ja offline-tila tarjoaa avun tilapäisten ja lyhyiden verkkokatkojen varalta. Ainoa rajoite offline-tilan käyttöön tuo päätteen kovalevyn tallennustila, eli jos jostain syystä pääte olisi niin kauan pois verkkoyhteyden piiristä, että tuona aikana tehdyt leimaukset täyttäisivät päätteen kovalevyn, leimaukset eivät enää verkkoyhteyden palautumisen jälkeen siirtyisi Neptoniin. Riippuen päätteen käyttöasteesta ja leimauksista, kovalevy saattaisi täyttyä viikon/kahden viikon offline-tilan aikana. Tällaista käyttötapaa ei kuitenkaan suositella.
