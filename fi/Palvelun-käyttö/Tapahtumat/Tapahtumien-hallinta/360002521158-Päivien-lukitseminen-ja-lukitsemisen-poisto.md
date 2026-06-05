---
id: 360002521158
title: Päivien lukitseminen ja lukitsemisen poisto
url: https://support.nepton.com/hc/fi/articles/360002521158-P%C3%A4ivien-lukitseminen-ja-lukitsemisen-poisto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumien hallinta
section_id: 360000667978
section_path:
- Tapahtumat
- Tapahtumien hallinta
labels:
- NEPTONNEEDSREVIEW
- lukko
- lukituspäivämäärä
- aikajakson sulkeminen
- lukitseminen
- lukituspäivä
- aseta tapahtumien lukituspäivä
- poista lukitus
- locking events
- lock
- lukituksen avaus
- lukituksen asettaminen
- lukitsemisen avaaminen
- lukituksen purkaminen
promoted: false
updated_at: '2026-04-07T08:16:35Z'
edited_at: '2026-04-07T08:04:44Z'
---

# Päivien lukitseminen ja lukitsemisen poisto

Työajan kalenterin päivien lukitseminen tai lukituksen poistaminen on mahdollista oletuksena ainoastaan palvelun pääkäyttäjälle. Ohje oikeuksien muokkaamiseen löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002554338>).
Palvelussa voidaan lukita päiviä, jonka jälkeen niillä olevia tapahtumia ei voida enää työntekijän toimesta muokata. Tätä voidaan hyödyntää esimerkiksi silloin, kun tunnit on jo siirretty palkanmaksuun. HUOM: Kun päivä on lukittu, ei koko päivälle voi enää lisätä uusia tapahtumia muutoin kuin pääkäyttäjän toimesta. 
Mikäli käytössä on poikkeava Työviikon aloitusaika (muu kuin klo 00:00), lukitus seuraa asetettua työviikon aloitusaikaa eikä kalenterivuorokautta.
## Lukitsemisoikeus
Päivien lukituksen voivat tehdä kaikki henkilöt, joilla on oikeus tapahtumien lukitsemiseen myönnetyn työajan roolin perusteella. Päivien lukitsemisoikeus ja lukituksen poisto löytyy ylemmän tason työajan roolin oikeuksista:  
![](https://support.nepton.com/hc/article_attachments/34186985586973)
**Voi lukita tapahtumapäiviä** -oikeus antaa oikeuden lukita tapahtumia niiden hyväksymisen yhteydessä.
**Voi poistaa tapahtumien lukituksen päiviltä** antaa oikeuden poistaa lukituksen. Tämä on yleensä myönnetty vain pääkäyttäjälle, mutta voidaan aktivoida työajan roolin kautta myös muille tarpeen vaatiessa.
## Lukitseminen ja lukituksen poisto manuaalisesti
### Päivien lukitseminen
Päivä voidaan lukita Työaika-osiossa valitsemalla **Työkalut** -valikosta valinta **Aseta tapahtumien lukituspäivä.**
![](https://support.nepton.com/hc/article_attachments/29564710961309)
Tapahtumat voidaan lukita tulevaisuuteen mihin tahansa päivämäärään. Jo tehtyjen lukitusten lukituspäivän voi muuttaa asettamalla **Valitse lukituspäivä** -kenttään se päivämäärä, jonne saakka tapahtumat halutaan säilyttää lukittuina eli esimerkiksi edellisen palkkajakson loppuun saakka. 
![](https://support.nepton.com/hc/article_attachments/29564700997917)  
Päivä voidaan lukita yksittäiseltä henkilöltä, Työaika-osion henkilöryhmältä tai koko henkilöstöltä. Oletuksena henkilöt haetaan viimeisen vuoden ajalta valittavaksi. Aikajaksoa ja muita henkilöiden valinnan asetuksia pääsee muokkaamaan hammasratas-kuvakkeen takaa.
Kun henkilöt on valittu, painetaan **Aseta lukituspäivä-** painiketta toiminnon toteuttamiseksi.
Kun lukitus on tehty, tulee henkilön kalenteriin lukon kuva, joka kertoo, että kyseinen päivä on lukittu.  
![](https://support.nepton.com/hc/article_attachments/21977575122077)
### Päivien lukituksen poisto
Päiviltä voidaan poistaa lukitus Työaika-osiossa valitsemalla **Työkalut** -valikosta valinta **Aseta tapahtumien lukituspäivä.**
![](https://support.nepton.com/hc/article_attachments/29564710961309)
Lukituspäivä voidaan poistaa jättämällä **Valitse lukituspäivä** tyhjäksi ja valitsemalla halutut henkilöt, joilta lukitus poistetaan. Tapahtumien lukitus voidaan poistaa yksittäiseltä käyttäjältä, käyttäjäryhmältä tai koko henkilöstöltä.
![](https://support.nepton.com/hc/article_attachments/29564700997917)
Kun valitaan **Aseta lukituspäivä,** poistuu lukitus henkilöltä koko historian ajalta.
Kun lukinta on poistettu, poistuu henkilön kalenterista lukon kuva päiviltä, jotka eivät ole enää lukittuja.
## Tapahtumien automaattinen lukitus
Palvelun Työaika-osiossa Työyhteisö- tai Asetusryhmä-tasolla voidaan määritellä myös automaattinen lukitus tapahtumille. Määritys löytyy valikosta **Työaika > Hallinta > Työyhteisön asetukset/Asetusryhmän asetukset > Työtunnit > Tapahtumien lukitseminen ja hyväksyntä > Lukitse tapahtumat automaattisesti kun on kulunut.**
Automaattinen lukitseminen tapahtuu klo 00:30.
![](https://support.nepton.com/hc/article_attachments/29564710965917)
