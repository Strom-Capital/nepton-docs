---
id: 360002575438
title: Miten toimin, kun henkilön työsuhde päättyy?
url: https://support.nepton.com/hc/fi/articles/360002575438-Miten-toimin-kun-henkil%C3%B6n-ty%C3%B6suhde-p%C3%A4%C3%A4ttyy
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilöiden hallinta
section_id: 360005884798
section_path:
- FAQ
- Henkilöiden hallinta
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-05-22T05:37:35Z'
edited_at: '2026-05-22T05:34:05Z'
---

# Miten toimin, kun henkilön työsuhde päättyy?

Tässä ohjeessa kerrotaan, mitä toimenpiteitä Neptonissa tulee tehdä, kun henkilön työsuhde päättyy. Pelkkä työsuhteen päättymispäivä ei estä kirjautumista, eikä käyttäjätunnuksen poisto yksin poista aiempia rooleja tai oikeuksia.
Huolellinen työsuhteen päättämiseen liittyvien vaiheiden suorittaminen:
  * vähentää tietoturva- ja tietosuojariskejä
  * estää tarpeettoman pääsyn tietoihin
  * helpottaa henkilön mahdollista palauttamista Neptoniin myöhemmin


## Huomio ennen aloittamista
Pelkkä työsuhteen päättymispäivän asettaminen **ei estä henkilöä kirjautumasta palveluun**.
Muistathan tehdä kaikki työsuhteen päättymiseen liittyvät tehtävät, mikäli näitä ei hoideta automaattisesti käytössä olevan liittymän kautta.
### Vaihe 1: Valmistelut ennen työsuhteen päättymistä
Kun henkilön työsuhde on päättymässä:
  * tarkasta henkilön kalenteri
  * päätä mahdolliset keskeneräiset leimaukset viimeistään työsuhteen päättymispäivään
  * poista mahdolliset työvuorot ja vuorotarpeet
  * hyväksy tapahtumat


### Vaihe 2: Avaa henkilön työsuhdetiedot
  1. Hae henkilön tiedot **Työsuhde** ‑välilehdeltä
  2. Avaa tiedot suurennuslasin kuvakkeesta


### Vaihe 3: Poista RFID‑tunniste
Mikäli henkilöllä on ollut RFID‑tunniste käytössä:
  * poista tunnisteen tiedot henkilön tiedoista


![mceclip0.png](https://support.nepton.com/hc/article_attachments/360006246018)
### Vaihe 4: Päätä työsuhde ja asetusryhmä
  1. Lisää henkilölle työsuhteen loppupäivä
  2. Päätä asetusryhmän voimassaolo lisäämällä **tyhjä asetusryhmä** , joka alkaa työsuhteen päättymistä seuraavana päivänä


![TSloppu.png](https://support.nepton.com/hc/article_attachments/5369923433117)
### Vaihe 5: Poista esimies‑ ja alaisuussuhteet
Poista henkilöltä:
  * alaiset
  * esimiehet


Samalla suosittelemme tarkistamaan henkilön käyttöoikeudet ja **alentamaan ne mahdollisimman matalalle tasolle**.
Työsuhteensa päättävällä henkilöllä tulisi olla korkeintaan:
  * työntekijätasoiset oikeudet
  * ei merkittyjä alaisia
  * ei esihenkilörooleja


![Esimalais.png](https://support.nepton.com/hc/article_attachments/5369921841821)
Tallenna tiedot sivun alalaidasta **Tallenna** ‑painikkeesta.
### Vaihe 6: Päätä mahdolliset sijaisuudet
Merkitse mahdolliset sijaisuudet päättyneiksi ja tallenna.
![Sijaiset.png](https://support.nepton.com/hc/article_attachments/5369893359389)
Vaikka sijaistettavan henkilön työsuhde on päätetty Neptonissa, jatkuu sijaisuussuhde kunnes sijaistettavan henkilön käyttäjätunnus on poistettu. 
Mikäli sijaisuutta ei erikseen pureta työsuhteen päättyessä ja henkilö palautetaan myöhemmin työsuhteeseen, henkilölle aktivoituu palautuksen yhteydessä vanhat sijaisuudet.
### Vaihe 7: Poista käyttäjätunnus
  1. Avaa henkilön tiedoista välilehti **Lisätoiminteet**
  2. Valitse kohdasta **Poista käyttäjätunnus** → **Poista**


![mceclip1.png](https://support.nepton.com/hc/article_attachments/360004506657)
Käyttäjätunnuksen poisto **estää henkilön kirjautumisen palveluun** , mutta **ei poista mitään henkilön relaatioita** , kuten: esimies‑ ja alaisuussuhteita tai aiemmin myönnettyjä käyttöoikeuksia. Siksi oikeuksien ja relaatioiden purkaminen tulee aina tehdä **ennen käyttäjätunnuksen poistoa**. 
## Raportit
Henkilö näkyy raporteilla, kun tarkastellaan ajanjaksoa jolloin henkilön työsuhde on vielä ollut aktiivinen. Työsuhteen loppupäivän jälkeisillä raporteilla henkilö ei enää näy.
Työsuhteen loppupäivä on siis esimerkiksi raportoinnin kannalta oleellinen, mutta se ei kuitenkaan estä henkilöä kirjautumasta palveluun. Tästä syystä on tärkeää muistaa myös poistaa henkilön käyttäjätunnus.
## Tietoturva ja GDPR
Kirjautumiseen vaikuttaa käytössä oleva kirjautumistapa:
  * **Kertakirjautuminen (SSO):** kirjautuminen poistuu usein käytöstä automaattisesti työsuhteen päättyessä organisaation IT:n määrittelyiden mukaisesti
  * **Neptonin käyttäjätunnus ja salasana:** henkilö voi kirjautua, kunnes käyttäjätunnus poistetaan


Käyttäjätunnuksen poiston yhteydessä asiakkaan tulee arvioida GDPR‑näkökulmasta:
  * mitä henkilötietoja on tarpeen säilyttää palvelussa
  * kuinka kauan tietoja säilytetään


Suosittelemme poistamaan tarpeettomat henkilötiedot erityisesti silloin, kun samat tiedot löytyvät myös esimerkiksi HR‑järjestelmästä.
## Muistilista työsuhteen päättyessä
  * Kalenteri ja leimaukset tarkastettu
  * Työsuhteen päättymisen jälkeiset vuorot poistettu
  * Työsuhteen loppupäivä asetettu
  * Asetusryhmä päätetty
  * Esimiehet ja alaiset poistettu
  * Käyttöoikeudet rajattu
  * RFID‑tunniste poistettu
  * Sijaisuudet päätetty
  * Käyttäjätunnus poistettu
  * Henkilötiedot arvioitu (GDPR)


## Henkilön palaaminen työsuhteeseen
Tämän ohjeen vaiheiden toteuttaminen varmistaa, että henkilö voidaan tarvittaessa palauttaa työsuhteeseen turvallisesti ja hallitusti.
Mikäli käyttöoikeuksia, rooleja tai relaatioita ei ole purettu työsuhteen päättyessä, henkilölle aktivoituu palautuksen yhteydessä vanhat oikeudet, jotka eivät välttämättä vastaa hänen uutta tehtäväänsä.
Huolellinen oikeuksien purkaminen:
  * ehkäisee virheellisiä käyttöoikeuksia
  * tukee tietoturvaa ja tietosuojaa
  * mahdollistaa puhtaan ja hallitun käyttäjän palautuksen


Katso tarkemmat ohjeet työsuhteeseen palaavia henkilöitä varten [täältä](<https://support.nepton.com/hc/fi/articles/360002575458>).
