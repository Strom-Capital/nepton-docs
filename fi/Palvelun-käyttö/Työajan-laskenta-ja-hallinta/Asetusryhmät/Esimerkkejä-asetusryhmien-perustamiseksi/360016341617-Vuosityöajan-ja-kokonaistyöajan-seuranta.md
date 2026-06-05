---
id: 360016341617
title: Vuosityöajan ja kokonaistyöajan seuranta
url: https://support.nepton.com/hc/fi/articles/360016341617-Vuosity%C3%B6ajan-ja-kokonaisty%C3%B6ajan-seuranta
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Esimerkkejä asetusryhmien perustamiseksi
section_id: 360001483898
section_path:
- Työajan laskenta ja hallinta
- Asetusryhmät
- Esimerkkejä asetusryhmien perustamiseksi
labels:
- kokonaistyöaika
- kokonaistyöajan seuranta
promoted: false
updated_at: '2024-08-23T12:05:54Z'
edited_at: '2021-11-26T07:07:46Z'
---

# Vuosityöajan ja kokonaistyöajan seuranta

## Vuosityöajan seuranta raportoinnin kautta
Yksinkertaisin tapa seurata vuosityöaikaa tai kokonaistyöaikaa halutulla ajanjaksolla on työajan raportti [Toteutuneen työajan määrä](<https://support.nepton.com/hc/fi/articles/360016836978>).
## Vuosityöajan lisä- ja ylityöiden seuranta tasoittumisjaksojärjestelmän kautta
Joissakin tapauksissa, esim. opetustyössä, on lisä- ja ylitöiden ansainta määritetty vuosityöajan kokonaismäärän mukaisin portain. Tällöin seuranta edellyttää tasoittumisjaksojen asetusten käyttämistä. Ohjeet tasoittumisjakson seurannan määrityksiin löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002559537>).
## Vuosityöajan tai kokonaistyöajan seuranta kertymän kautta
Vuosityöaikaa tai kokonaistyöaikaa halutulla ajanjaksolla voidaan seurata kertymän kautta. Palvelussa ei ole Vuosityöaika tai Kokonaistyöaika-nimistä kertymää, mutta seurannassa voidaan hyödyntää mitä tahansa palvelussa vakiona olevaa kertymää, kunhan se ei ole toisaalla jo käytössä.
Alla kuvaamme esimerkin, jossa vuosityöajan seuranta on otettu käyttöön hyödyntäen Tasoittumisjaksotunnit-kertymää. Käytännössä palveluun määritellään työkorotus, joka kerryttää vuosityöajan seurannan piirissä olevat tapahtumat tasoittumisjaksokertymään. Tasoittumisjaksokertymään kerrytetyt tunnit näkyvät kalenterinäkymässä.
Esimerkin organisaatiossa ei ole käytössä tasoittumisjaksotuntien kertymää sellaisenaan. Näin ollen sitä voidaan hyödyntää vuosityöajan seuraamiseen, vaikka nimi ei olekaan vuosityöaika. Jos organisaatiossa on käytössä tasoittumisjaksotuntien seuranta, voidaan käyttöön ottaa mikä tahansa toinen palvelussa oleva kertymä, jos se ei ole muutoin jo käytössä.
Ensin on määriteltävä kenelle vuosityöajan seuranta kalenterinäkymässä näkymän kertymän kautta on käytössä. Kun tämä on määritelty tehdään seuraavat määritykset ko. asetusryhmään.
**1\. Määritellään tasoittumisjaksotuntien kertymä käyttöön.**
Kertymä aktivoidaan asetuksissa kohdasta **Työtunnit - > Kertymät ja ylityötunnit.**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360014544797/mceclip0.png)
**2\. Määritellään tasoittumisjaksotuntien nollaamiseen tarvittava tapahtumatyyppi näkyviin.**
Jotta vuosityöajan tai kokonaistyöajan seuranta voidaan nollata seurantajakson alussa tulee näkyvissä olla tapahtumatyyppi 'Tasoittumisjaksotuntien arvon asetus'. Tarkempi ohje tapahtumatyypin näkyvyyden asettamiseen löytyy [tästä artikkelista.](<https://support.nepton.com/hc/fi/articles/360002560298>)
Tasoittumisjaksotuntien arvo asetetaan arvoon 00:00 jokaisen seurantajakson ensimmäisellä päivällä.
**3\. Määritellään työkorotus, joka kerryttää vuosityöajan seurannan piirissä olevat tapahtumat tasoittumisjaksokertymään.**
Tarkempi ohje työkorotusten määrittelystä löytyy [tästä artikkelista](<https://support.nepton.com/hc/fi/articles/360002560978>).
Tässä käyttötapauksessa tulee huomioida seuraavien kenttien määrittely.
**\- Näkyvissä viikkotaulussa**
Tämän kentän arvoksi asetetaan **Asetus po****is päältä.** Työkorotuksen ei haluta näkyvän viikkotaulussa, koska se voi aiheuttaa hämmennystä sellaiselle käyttäjälle, joka ei tunne asian teknistä toteutusta. 
**\- Työaikahyvitystyypit joista ansaitaan korotusta**
Tähän valitaan ne työaikahyvitystyypit, jotka lasketaan mukaan vuosityöajan seurantaan. Yleisimmässä käyttötapauksessa tähän valitaan 'Kyllä' arvoksi kaikkiin työaikahyvityyppeihin, pois lukien Tunti tunnista - Ei korvata.
**\- Tapahtumatyypit joista ansaitaan korostusta**
Tähän valitaan ne tapahtumatyypit, jotka lasketaan mukaan vuosityöajan seurantaan. Yleisimmässä käyttötapauksessa tähän valitaan 'Kyllä' arvoksi kaikkiin tapahtumatyyppeihin, pois lukien palkattomat poissaolotunnit, yleiset vapaapäivät (palkallinen vapaapäivä ma-pe eli arkipyhät) tai vuosilomat, sekä saldosta tai muusta kertymästä lainattu aika sekä vastaavat kertymäpoissaolot, esim. saldovapaa.  
**\- Voimassaoloajat**
Voimassaoloajoiksi määritellään kaikille viikonpäiville klo 00:00 Nykyisenä päivänä - 24:00 Nykyisenä päivänä.
