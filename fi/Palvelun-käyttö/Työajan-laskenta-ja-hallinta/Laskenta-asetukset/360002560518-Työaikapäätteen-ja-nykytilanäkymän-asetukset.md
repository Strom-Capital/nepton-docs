---
id: 360002560518
title: Työaikapäätteen ja nykytilanäkymän asetukset
url: https://support.nepton.com/hc/fi/articles/360002560518-Ty%C3%B6aikap%C3%A4%C3%A4tteen-ja-nykytilan%C3%A4kym%C3%A4n-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- leimauspäätteet
- työaikapääte
- work time terminal
- recording terminal
- current status view
- nykytilanäkymä
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-08-18T11:44:19Z'
---

# Työaikapäätteen ja nykytilanäkymän asetukset

**Työaikapäätteen** (kirjauspäätteen) ja **Nykytila** -näkymän asetuksia voidaan määritellä sekä **Työyhteisö** -tasolla että **Asetusryhmät** -tasolla. Suurin osa asetuksista on vain työyhteisötasolla, eli asetusryhmittäin voidaan määrittää vain muutama täsmäasetus. 
Huom: Tapahtumatyyppien näkyminen nykytilassa/työaikapäätteellä määritetään Tapahtumatyypit-valikosta. Tarkat ohjeet löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002519157>).
## Asetusten määritteleminen
Työyhteisötasolla asetukset löytyvät valikosta **Työaika > Hallinta > Työyhteisön asetukset > Nykytila.**
**![](https://support.nepton.com/hc/article_attachments/28356733924765)**
**Nykytila käytössä** -asetus on oletuksena aina 'Kyllä'. Siihen ei tarvitse tehdä muutoksia. Asetus mahdollistaa Nykytila-näkymän palvelussa.
**Nykytilanne-työaikapääte käytössä** on asetus, joka koskee vanhoja toteutuksia. Tässä asetuksessa tulee olla kyllä, jotta sivun verkko-osoitelinkki toimii.
**Sivun verkko-osoite** -linkistä voi avata palvelun Nykytila-näkymän verkko-osoitteessa. Linkin toimiimsen edellytys on, että asetus "Nykytilanne-työaikapääte käytössä" on kyllä. Tätä voi hyödyntää esimerkiksi tilanteissa, joissa käyttäjille halutaan mahdollistaan Nykytila-näkymän käyttäminen ulkoisella laitteella (esimerkiksi tablet-laite organisaation tiloissa). Jos käytössä on RFID-tunnisteella tai PIN-koodilla tunnistautuminen tulee tarvittava tunnistautuminen tehdä myös tätä linkkiä käytettäessä.
**Kirjautuminen työaikapäätteellä mahdollista** -kohdan asetuksista voidaan määritellä, onko [PIN-koodilla](<https://support.nepton.com/hc/fi/articles/360002430798>) mahdollista kirjautua työaikapäätteellä (koskee Nepton Touch päätteitä).
Kirjautuminen PIN-kodilla ei käytössä = Vain RFID-kirjautuminen käytössä  
Kirjautuminen PIN-koodilla = sekä PIN-koodikirjautuminen että RFID-kirjautuminen käytössä  
Kirjautuminen vain RFID-lukijaan = Vain RFID-kirjautuminen käytössä
![](https://support.nepton.com/hc/article_attachments/28356715802525)
**Kommentin antaminen mahdollista web terminaalissa ja nykytila** -asetus määrittää, voidaanko tapahtuman yhteydessä jättää kommentti työaikapäätteellä ja nykytilassa. Oletuksena asetus on 'Ei'.
**Näytä ilmoituksia työaikapääte & nykytilanne -sivulla **-valinta näyttää Viestintä-osiossa luodut ilmoitukset työaikapäätteessä ja Nykytila-sivulla. Määritys on oletuksena 'Kyllä'. Viestintä-osio ei ole oletuksena päällä. Jos haluatte ottaa käyttöön Viestintä-osion organisaatiossanne, olettehan yhteydessä sopimusyhteyshenkilöönne.
**Mahdollista työaikapäätteellä muokattavat aloitus- ja lopetusajat** -määritys kertoo, voiko henkilö kirjatessaan tapahtumaa Nykytila-näkymässä tai Nykytilanne-työaikapäätteellä muokata tapahtuman aloitus- ja lopetusaikoja. Tämä voi olla hyödyllistä esimerkiksi, jos henkilö on ensin kohteessa tekemässä työtä ja siirtyy loppupäiväksi toiseen kohteeseen. Oletuksena aloitus- ja lopetusaikojen muokkausmääritys on 'Ei'. HUOM: Tämä asetus ei koske [kirjauspäätteitä](<https://support.nepton.com/hc/fi/articles/360003685277>) kuten Nepton Touch. Kirjauspäätteille on mahdollista asettaa aloitus- ja lopetusaikojen leimaus tapahtumatyyppikohtaisesti [tämän](<https://support.nepton.com/hc/fi/articles/4406224046097>) ohjeen mukaan.
**Aloitus- ja lopetusaikojen syöttöväli** -määrityksessä voidaan määritellä minuuteissa syöttöväli, jonka tarkkuudella aloitus- ja lopetusaikoja voidaan muokata Nykytila-näkymässä tai Nykytilanne-työaikapäätteellä. Tätä voidaan hyödyntää esimerkiksi tilanteissa, joissa työaikaa halutaan käsitellä minimissään 15 minuutin tarkkuudella. HUOM: Tämä asetus ei koske [kirjauspäätteitä](<https://support.nepton.com/hc/fi/articles/360003685277>) kuten Nepton Touch. Kirjauspäätteillä aloitus- ja lopetusajat on mahdollista syöttää 15 minuutin välein.
**Näytä projektit** -määritys kertoo, näytetäänkö kirjauspäätelaitteella ja Nykytila-näkymässä tapahtumaa kirjattaessa Kohde-välilehti. Tämä mahdollistaa [työn kohdentamisen](<https://support.nepton.com/hc/fi/articles/360002593398>) projektille/kohdenteelle kirjauspäätettä ja Nykytila-näkymää käytettäessä.
**Käytössä on ruokalapäätteitä** -määritys kertoo, onko organisaatiossa käytössä ns. lounaspäätteitä, eli kirjauspäätelaitteita, joita käytetään lounas- ja kahvilamaksujen välittämiseen. Tämä asetus laitetaan Neptonin tai kumppanin yhteyshenkilön toimesta päälle, jos määritykset niin vaativat. Tätä ei tule muokata.
**Näytä päivän työtunnit** asetus määrittää, näytetäänkö nykytilassa henkilön sen hetken päivän työtunnit.
**Näytä viikon työtunnit** asetus määrittää, näytetäänkö nykytilassa henkilön sen hetken viikon työtunnit.
![](https://support.nepton.com/hc/article_attachments/28362942373533)
**Siirry nykytila-sivulle kirjautumisen jälkeen** Jos täppä on aktiivisena, käyttäjä ohjataan suoraan nykytila-sivulle työn kirjaamisen jälkeen.
