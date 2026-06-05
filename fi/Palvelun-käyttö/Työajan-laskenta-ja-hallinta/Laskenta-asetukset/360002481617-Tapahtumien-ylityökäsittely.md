---
id: 360002481617
title: Tapahtumien ylityökäsittely
url: https://support.nepton.com/hc/fi/articles/360002481617-Tapahtumien-ylity%C3%B6k%C3%A4sittely
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- NEPTONNEEDSREVIEW
- ylityökorvaus
- Ylityöohjaus kirjausta tehdessä
- ylityöohje
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-03-13T07:54:41Z'
---

# Tapahtumien ylityökäsittely

Ylityötä muodostuu työpäiväkohtaisesti, ei tapahtumakohtaisesti, eli kaikki muodostunut ylityö lasketaan yhteen.  
Tämän jälkeen tulkitaan asetusten mukaisesti, onko kyseessä 50% vai 100% ylityö.  
Jos ylityöhön kohdistuu pyöristys, pyöristys muodostuu ajallisesti viimeiseen ylityöjaksoon.  
Poikkeus tähän on Sovittu 100% ylityö, joka pyöristyy itsenäisesti, eikä vaikuta päivän muuhun ylityölaskentaan.
Säännöllisen työajan ylittävä osuus voidaan kohdistaa tapahtuman muokkauksessa eri tulkintojen mukaisesti. On myös mahdollista valita, ettei säännöllisen työajan ylittäviä tunteja korvata lainkaan. Määritys voidaan tehdä Työaika-osiossa joko **Työyhteisö-tason** tai **Asetusryhmä-tason** määrityksissä **Työaika - Hallinta - Työyhteisön/Asetusryhmän asetukset -Työtunnit- Ylityö.**
## Ylityön oletuskohdenne
Tapahtuman muokkauksen Ylityö-valikon tulkintavaihtoehdoista voidaan esivalita oletus asettamalla arvot asetuksiin **Ylityön perusosa/korotusosa oletuksena web/reaaliaikaista kirjausta tehtäessä.** Asetukset voi määritellä erikseen reaaliaikaista kirjausta (työaikapääte, mobiili) tai web-kirjausta tehdessä.
Ylityön perusosalle ja korotusosalle määritellään oletukset. Jos halutaan korvata tunti tunnista, valitaan korvaustyyppi perusosalle. Korotusosaan määritellään 'Ei korvata'.
Jos taas halutaan määritellä korvattavaksi ylityötä, tulee sekä perusosalle että korotusosalle määritellä oletustyyppi.
Jos ylityön oletuskohdenteeksi halutaan 'Tunti tunnista -Saldoon' määritellään asetukset tämän esimerkin tavoin:**  
**
![](https://support.nepton.com/hc/article_attachments/25821275015197)
Jos ylityön oletuskohdenteeksi halutaan 'Ylityö - Palkkaan' määritellään asetukset tämän esimerkin tavoin:
![](https://support.nepton.com/hc/article_attachments/25821275016349)
Ylityölaskenta noudattaa asetusryhmään määritettyä tulkintaa. Oletuskohdennetta voidaan muuttaa tapahtumakohtaisesti avaamalla tapahtumakirjauksen käyttäjän kalenterinäkymässä ja valitsemalla tapahtumassa kohdan Ylityö.
![](https://support.nepton.com/hc/article_attachments/25821268060061)
Tapahtuman muokkauksessa näkyviä ylityön korvaustyyppejä voi muokata kohdassa **Kertymät ja ylityötunnit - Ylityö - Näkyvissä olevat ylityöasetukset tapahtuman luonnissa**.
## Erilaisia ylityön kohdenteita
Tässä kerromme esimerkkinä joitain korvaustyyppejä. Näkyvillä olevia korjaustyyppejä on kymmeniä erilaisia.
**Oletus  
** Tunnit kohdistetaan käyttäjän asetusryhmän asetusten mukaisesti.
**Ei korvata  
** Säännöllisen työajan ylittäviä tunteja ei korvata.
**Tunti tunnista - Pankkiin**  
Säännöllisen työajan ylittävä työ kohdistuu yksinkertaisena työaikapankkiin.
**Tunti tunnista - Palkkaan  
** Säännöllisen työajan ylittävä työ kohdistuu yksinkertaisena palkanmaksuun.
**Ylityö - Saldoon  
** Säännöllisen työajan ylittävät tunnit kohdistetaan ylityön mukaisilla korotuksilla työtuntisaldoon.
**Ylityö - pankkiin**  
Säännöllisen työajan ylittävät tunnit kohdistetaan ylityön mukaisilla korotuksilla työaikapankkiin.
**Ylityö - palkkaan**  
Säännöllisen työajan ylittävät tunnit kohdistetaan ylityönä palkanmaksuun.
**Ylityö - perusosa saldoon, korotusosa palkkaan**  
Säännöllisen työajan ylittävät tunnit kohdistetaan perusosan osalta työaikasaldoon ja ainoastaan korotusosa tehdystä työstä (esim. 50 % ylityö) kohdistetaan palkanmaksuun.
**Ylityö - perusosa pankkiin, korotusosa palkkaan**  
Säännöllisen työajan ylittävät tunnit kohdistetaan perusosan osalta työaikapankkiin ja ainoastaan korotusosa tehdystä työstä (esim. 50 % ylityö) kohdistetaan palkanmaksuun.
**100% ylityökorvaus**  
Pakottaa kaiken säännöllisen työajan ylittävän ajan 100% ylityöksi. Lisätyöstä muodostuu vuorokautista 100% ylityötä, 50% vuorokautinen/viikkoylityö korotetaan 100% ylityöksi. Ei vaikuta 50% viikkoylityön enimmäisrajan laskentaan, 100%:iin pakotettu 50% viikkoylityö huomioidaan ko. rajaa tarkastellessa. Tätä asetusta tulee käyttää ainoastaan pakottavissa tilanteissa, jos muilla asetuksilla ei ole mahdollista saada muodostumaan 100% ylityötä.
