---
id: 24730505042077
title: Nepton Flexim päätteen käyttö
url: https://support.nepton.com/hc/fi/articles/24730505042077-Nepton-Flexim-p%C3%A4%C3%A4tteen-k%C3%A4ytt%C3%B6
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Kirjauspäätteen käyttö
section_id: 360002084697
section_path:
- Kirjauspäätteet
- Kirjauspäätteen käyttö
labels: []
promoted: false
updated_at: '2026-11-09T13:24:34Z'
edited_at: '2026-11-09T13:23:06Z'
---

# Nepton Flexim päätteen käyttö

Tässä ohjeessa kerrotaan, kuinka kirjataan työaikaa käyttämällä Nepton Flexim päätteitä.
## Alkunäyttö
Oletuksena päätteen alkunäyttö näytetään suomenkielisenä. Alkunäyttö voidaan muuttaa myös englannin- tai ruotsinkieliseksi admin-PIN koodilla päätteen asetuksista. Kun henkilö kirjautuu sisään, pääte näkyy sillä kielellä, mikä henkilölle on asetettu Neptonissa.
![](https://support.nepton.com/hc/article_attachments/24832606724509)
Päätteellä näkyy yläpalkissa Neptonin logo, kysymysmerkki-symboli ja kellonaika. Kysymysmerkkiä klikkaamalla avautuu lisätietoa päätteestä; Laitteen ID, ohjelmaversio, QR-koodi tukisivuston ohjeisiin sekä mahdollisuus käynnistää laite uudelleen. Asetukset-painike esitellään tämän ohjeen lopussa "Kirjauspäätteen asetusten muuttaminen" osiossa.
![](https://support.nepton.com/hc/article_attachments/24836801806749)
Näytön keskellä esitetään ne kirjautumisvaihtoehdot, jotka päätteelle on otettu käyttöön. Kirjautumistavat avattu tarkemmin tämän ohjeen seuraavassa osiossa.
## Päätteelle kirjautuminen
Päätteelle voidaan kirjautua seuraavin eri tavoin:
### RFID-tunnisteella kirjautuminen
Tunniste näytetään lukijaan, jolloin käyttäjä kirjautuu sisään, ja voi leimata työaikaa. Tunniste täytyy olla tallennetuna henkilön tietoihin. Henkilöllä voi olla useampi RFID-tunniste käytössä samaan aikaan.
### PIN-koodilla kirjautuminen
Pin-koodilla kirjautuessa käyttäjä näppäilee oman PIN-koodinsa numerotauluun, jonka jälkeen hän pääsee leimaamaan työaikaa. PIN-koodi pitää olla tallennettuna henkilön tietoihin. PIN-koodilla kirjautuminen voidaan myös estää päätekohtaisesti, jolloin kirjautumisnäyttö antaisi mahdollisuuden kirjautua vain RFID-tunnisteella:
![](https://support.nepton.com/hc/article_attachments/24832622930205)
Huom: Nepton Flexim päätteissä PIN-koodilla kirjautuminen määritetään päätteittäin, päätteen asetuksisssa. Asetusryhmän asetuksella ei siis vaikuteta Nepton Flexim päätteiden kirjautumistapaan.
### Pikakirjautuminen
Päätekohtaisesti voidaan asettaa myös pikakirjautuminen käyttöön. Pikakirjautuminen on tarkoitettu etenkin tilanteisiin, jossa suuri määrä ihmisiä kirjautuu samanaikaisesti sisälle. Kun pikakirjautuminen on käytössä riittää, että henkilö näyttää tunnistettaan lukijaan, ja Työ-kirjaus (tai se tapahtumatyyppi, mikä asetettu oletustapahtumaksi käyttäjän asetusryhmässä) alkaa automaattisesti siitä hetkestä alkaen. Mikäli henkilöllä on avoin kirjaus, päättyy se uuden pikakirjauksen alkaessa. Jos henkilölle on asetettu oletusprojekti, kohdistuu työ automaattisesti tälle projektille. Kun pikakirjaustoiminto on käytössä, päätteen alkunäytöltä jokainen käyttäjä voi määrittää onko se käytössä vai ei. Pikakirjaustoiminto toimii myös tilanteissa, joissa pääte on offline-tilassa.
## Kirjauspäätteen näkymä sisäänkirjautumisen jälkeen
Jos henkilöllä on aktiivinen tapahtuma, näytetään se tapahtumavalikossa sinisellä värillä. Tämä tapahtuma päättyy automaattisesti, mikäli päätteeltä valitaan toinen tapahtuma, ja painetaan "Aloita". 
Jos kirjautumisen jälkeen ei tehdä mitään, kirjataan käyttäjä automaattisesti ulos 20 sekunnin viiveellä. Viiveen määrää voidaan säätää päätteen asetuksista. Viive esitetään näytön alareunassa pienenevänä palkkina. Palkin yläpuolella näytetään kahden käytössä olevan kertymän arvo sillä hetkellä. Näytön alareunassa on myös peruuta-painike, jolla voidaan kirjautua ulos päätteeltä, sekä Aloita/Lopeta-painike, jolla voidaan aloittaa tai lopettaa uusi tapahtuma.
Näytön yläreunassa näkyy valikko; ensimmäisenä on Tapahtuman valinta, seuraavana työlisien lisäys, sen jälkeen ylityön kohdenne ja viimeisenä projektikohdennus. Oikeassa yläreunassa näkyy, kuka käyttäjä on kirjautuneena sisään, ja mitä kello on sillä hetkellä.
## Tapahtuman lisääminen
Kun henkilö on kirjannut itsensä laitteelle, hän voi kirjata ennalta määrättyjä tapahtumia. Näytöllä näkyy 8 tapahtumaa. Mikäli tapahtumia on asetettu näytettävän enemmän, sivuttuu näkymä, ja sivunuolella siirrytään seuraavalle sivulle. Uusi tapahtuma aloitetaan klikkaamalla haluttua tapahtumatyyppiä ja sen jälkeen "aloita"-painiketta. Kun tapahtuma aloitetaan, kirjautuu käyttäjä automaattisesti päätteeltä ulos. Jos pääte on offline-tilassa, tapahtumia ei voi lisätä kuin vain pikakirjaamisen kautta.
![](https://support.nepton.com/hc/article_attachments/24836814537757)
Kirjauspäätteellä voidaan tehdä kirjauksia enintään 2 vuotta tulevaisuuteen. Menneisyyteen kirjauksia voidaan tehdä kolmen kuukauden taakse.
### Tapahtuman aloitus- ja lopetusajan asettaminen
Päätteellä voidaan myös lisätä tapahtumia tulevaisuuteen antamalla niille alkamis- ja/tai loppumisaika jo leimausvaiheessa. Jotta tämä on mahdollista, pitää Neptonissa olla asetusryhmässä määritelty tapahtumatyypille tämä mahdollisuus käyttöön. Kun päätteellä aktivoidaan tapahtuma, ilmestyy "Aloita"-painikkeen viereen "Muokkaa"-painike. 
![](https://support.nepton.com/hc/article_attachments/24888102373789)
Tätä painamalla avautuu uusi valikko, josta tapahtumalle voidaan valita sen alku- ja loppuaika.
![](https://support.nepton.com/hc/article_attachments/24888114740253)
Kun tapahtuman päivämäärät on valittu, tulee seuraavaan näkymään kellonajat valittavaksi.
![](https://support.nepton.com/hc/article_attachments/24888102378909)
## Tapahtuman ylityökohdennus
Ylityö-välilehdeltä voidaan vaihtaa ylitöiden käsittelytapa valitulle tapahtumatyypille. Vaihtoehdot tulevat henkilön asetusryhmän mukaisista määrityksistä. Välilehden nimen vieressä näytetään sen hetkisten aktiivisten valintojen määrä.
![](https://support.nepton.com/hc/article_attachments/24832622934685)
## Työlisän lisääminen
Työlisiä on mahdollista kirjata, kun jokin tapahtuma on valittu. Lisät-välilehdellä näkyy neljä työlisää per sivu. Sivunuolella voidaan siirtyä seuraavalle sivulle, mikäli lisiä on enemmän kuin neljä.
![](https://support.nepton.com/hc/article_attachments/24836801815709)
Lisien tyyppi ja oletusarvot tulevat asetusryhmän asetusten mukaan. Pikavalinnoilla voi vähentää tai lisätä lisän määrää joko kpl tai 15 min kerrallaan. Jos tarve, kynäikonia painamalla voidaan antaa tarkempi arvo.
![](https://support.nepton.com/hc/article_attachments/24832622935837)
Välilehden nimen vieressä näytetään sen hetkisten aktiivisten valintojen määrä.
## Projektikohdennus
Projektit-välilehdeltä voidaan painikkeilla valita, mille projektille tapahtuma kohdistetaan. Näkymässä esitetään yhdellä sivulla 8 projektia. Mikäli projekteja on enemmän, sivunuolella voi siirtyä seuraavalle sivulla. Painikkeissa näytetään viimeksi käytetyt, eli samat projektit, mitä henkilölle tarjotaan tapahtuman luonnissa selaimessakin. Haulla voidaan projektin nimellä tai koodilla löytää myös viimeksi käytetyt -listan ulkoinen projekti. Nepton Flexim päätteellä voidaan tapahtumille kirjata vain yksi projektikohdennus kerrallaan. Mikäli projektikohdennus halutaan vaihtaa kesken päivän, tulee aloittaa uusi tapahtuma uudella projektikohdennuksella.
![](https://support.nepton.com/hc/article_attachments/25051244701725)
### Projektikohdennus viivakoodilukijalla
Projekti voidaan myös valita viivakoodilukijalla sen jälkeen, kun henkilö on kirjautunut tunnisteella. Viivakoodiluvun jälkeen projektille kohdistus käynnistyy ja henkilö kirjautuu ulos päätteeltä. Näytöllä näytetään, että kirjaus on aloitettu onnistuneesti.
![](https://support.nepton.com/hc/article_attachments/24837907493277)
Mikäli viivakoodilukijalla aloitetaan tapahtuma projektilla, jota ei vielä löydy Neptonista, ja käyttäjällä on tarvittavat oikeudet, luo kirjaus projektin automaattisesti uudeksi projektiksi Neptoniin (projekti ilmestyy projektipuurakenteessa juureen). Tarvittavat oikeudet tähän annetaan työajan roolin keskitason oikeudella "Voi luoda puuttuvia projekteja työaikapäätteen viivakoodilukijalla":
  
![](https://support.nepton.com/hc/article_attachments/24837463490845)
## Kirjauspäätteen asetusten muuttaminen
Kirjauspäätteeltä voi suoraan muuttaa joitakin päätteen asetuksia. Tätä varten tarvitaan hallinta PIN-koodi. Asetuksiin pääsee päätteen alkunäytöltä klikkaamalla kysymysmerkki-symbolia, ja siitä avautuvasta näytöstä "asetukset" -nappia. Tässä vaiheessa pääte pyytää PIN-koodia. Jos et tiedä päätteidesi hallinta PIN-koodia, olethan yhteydessä Neptonin asiakaspalveluun.
Kun PIN-koodi on annettu, avautuu seuraava hallintavalikko:
![](https://support.nepton.com/hc/article_attachments/24837888927645)
Näytön yläreunassa näytetään päätteen tiedot; sarjanumero, ohjelmaversio sekä IP-osoite.
![](https://support.nepton.com/hc/article_attachments/24837888932253)
Valikossa voidaan muuttaa laitteen lähiverkkoasetuksia, määrittää salattu palvelinyhteys ja käynnistää laite uudelleen. Salattu palvelinyhteys tarvitaan vain tilanteissa, joissa käytössä on palomuuri, joka avaa yhteyden uudelleen. Seuraavalla sivulla voi muuttaa käyttökokemukseen liittyviä asetuksia:
Automaattisen uloskirjautumisen viive  
Automaattisen uudelleenkäynnistyksen sykli  
PIN-koodilla kirjautumisen salliminen  
Pikaleimauksen salliminen  
Päätteen kieli
