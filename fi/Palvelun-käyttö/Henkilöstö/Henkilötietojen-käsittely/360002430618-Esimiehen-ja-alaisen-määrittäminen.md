---
id: 360002430618
title: Esimiehen ja alaisen määrittäminen
url: https://support.nepton.com/hc/fi/articles/360002430618-Esimiehen-ja-alaisen-m%C3%A4%C3%A4ritt%C3%A4minen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötietojen käsittely
section_id: 360004485937
section_path:
- Henkilöstö
- Henkilötietojen käsittely
labels:
- NEPTONNEEDSREVIEW
- esihenkilö
- ensisijainen esimies
- supervisor
promoted: false
updated_at: '2026-11-06T10:36:08Z'
edited_at: '2026-11-04T14:16:16Z'
---

# Esimiehen ja alaisen määrittäminen

Esimies-alaissuhde määritetään henkilöiden tiedoissa työsuhdepuolella. Jos henkilölle A lisätään esimieheksi henkilö B, ilmaantuu henkilön B tietoihin alaiseksi henkilö A, ilman että tieto täytyy tallentaa kummankin henkilön tietoihin erikseen. 
Esimiehen/alaisen lisääminen tai vaihtaminen yksittäiselle henkilölle vaatii ylläpitäjältä tietynlaiset [roolit](<https://support.nepton.com/hc/fi/articles/360002425637>). Voit valita henkilölle vain sellaisen esimiehen, jolla on henkilönumero asetettuna.
Huomaathan, että esimies näkee vain omat alaisensa. Mikäli haluat antaa esimiehelle näkyvyyden toisen esimiehen alaisiin, tulee esimies asettaa sen esimiehen sijaiseksi, jonka alaisiin näkyvyys halutaan antaa. Ohje löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002430678>).
## Esimiehen asettaminen
Esimies asetetaan työntekijälle seuraavasti:
Avaa **Työsuhde** -osio ja valitse **Henkilöt >** **Henkilöt**.  
Avaa suurennuslasista halutun henkilön tiedot.  
Valitse valikosta **Organisaatio >** **Esimiehet > Lisää**. Aloita kirjoittamaan esimiehen nimeä ja valitse tuloksista haluttu henkilö esimieheksi.
Voit lisätä henkilölle useamman esimiehen. Mikäli henkilölle lisätään useampi esimies, tulee palveluun näkyviin valinta siitä, kuka henkilöistä on haluttu ensisijainen esimies. Huomioithan, että ilmoitukset arkaluonteisista toimista, kuten sairausloma-, saldo- ja vuosilomapyynnöistä, lähetetään ainoastaan ensisijaisille esimiehille.
Kun olet valinnut haluamasi henkilöt valitse **Valmis**.
Muista tallentaa tiedot sivun alalaidan **Tallenna** -linkistä.  
  
![](https://support.nepton.com/hc/article_attachments/29075204918557)  
  
Esimiestieto voidaan päivittää myös usealle työntekijälle samanaikaisesti. Ohjeen esimiestiedon massatuontiin löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002430658>).
Alaisen [tapahtumapyynnöstä](<https://support.nepton.com/hc/fi/articles/360017787717>) hyväksymispyynnön sähköposti-ilmoituksena saa vain ensisijainen esimies (ja/tai ensisijaisen esimiehen sijainen)
## Alaisen asettaminen
Alaisen lisääminen esimiehelle tai alaistiedon muokkaaminen tapahtuu henkilön tietokortilla **Työsuhde** -osiossa. Henkilöllä voi olla useita alaisia. Voidaksesi määrittää alaisen, täytyy alaisella olla henkilönumero tallennettuna.
Alainen voidaan asettaa työntekijälle seuraavasti:  
  
Avaa **Työsuhde** -osio ja valitse **Henkilöt > Henkilöt**.  
Avaa suurennuslasista halutun henkilön tiedot.  
Valitse valikosta **Organisaatio >** **Alaiset > Lisää.** Aloita kirjoittamaan henkilön nimeä avautuvaan laatikkoon ja valitse tuloksista haluttu henkilö alaiseksi.
Voit lisätä henkilölle useamman alaisen.
Muista tallentaa tiedot sivun alalaidan **Tallenna** -linkistä.
![](https://support.nepton.com/hc/article_attachments/39952428732573)
## Esimiestiedon päivittäminen tai asettaminen usealle henkilölle kerralla
Esihenkilötiedot voidaan päivittää massana sisäänluettavan tiedoston avulla. Tässä esimerkissä käytetään manuaalista henkilötuontia .csv-tiedostomuodossa UTF-8-koodauksella. Lisätietoja eri tuontivaihtoehdoista löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360003762577>).
  1. Mene Työsuhde-osiossa **Henkilöt > Henkilöt **ja paina **Vie sisäänluettavaan Exceliin -** painikkeesta.
  2. Poista Excel-tiedostosta kaikki muut sarakkeet paitsi **Henkilönumero, Ensisijaiset esimiehet ja Toissijaiset esimiehet**. Myös sarakkeet **Etunimi** ja **Sukunimi** voidaan jättää, mikäli ne helpottavat tiedoston käsittelyä.
  3. Mikäli henkilöllä on jo määritettyjä esimiehiä (esimiesten hlönumeroita), **älä** poista niitä aineistosta.
  4. Lisää kullekin henkilölle tämän uuden esimiehen henkilönumero Toissijaiset esimiehet -sarakkeeseen. Mikäli henkilöllä on jo esimiehiä, erota uuden esimiehen henkilönumero jo olemassa olevista | - merkillä, ilman välilyöntiä.
  5. Edellä mainittujen vaiheiden jälkeen Excel-tiedoston tulisi näyttää seuraavalta:  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/40415706691101)  

  6. Tämän jälkeen tallenna tiedosto **CSV UTF-8** -muodossa. 
  7. Tiedosto on nyt valmis ladattavaksi palvelun Työsuhde-osion Henkilöt-välilehdeltä löytyvän Tuo henkilöitä -työkalun avulla (ks. [Henkilöiden manuaalinen tuonti](<https://support.nepton.com/hc/fi/articles/360018767498>)). 
  8. Hae henkilöaineisto koneeltasi raahaamalla tiedosto viivoitetulle alueelle tai valitsemalla Valitse tiedosto -painikkeesta.  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/40415695740701)
  9. Valitse tiedostomuoto UTF-8 ja henkilötuonnin tyyppi "Oletus". Paina lopuksi Tuo henkilöt -painiketta. Palvelu ilmoittaa onnistuneesta tai epäonnistuneesta tuonnista. Jos tuonti epäonnistuu, antaa palvelu tarkemmat tiedot aineistossa olevasta virheestä.


On suositeltavaa testata esimiestiedon tuontia ensin yhdellä henkilöllä, jotta voidaan varmistua tiedostomuodon oikeellisuudesta sekä halutusta lopputuloksesta. Varmista, että ainakin yksi esimies on määritetty ensisijaiseksi esimieheksi. Ilmoitukset arkaluonteisista toimista, kuten sairausloma-, saldo- ja vuosilomapyynnöistä, lähetetään ainoastaan ensisijaisille esimiehille.
