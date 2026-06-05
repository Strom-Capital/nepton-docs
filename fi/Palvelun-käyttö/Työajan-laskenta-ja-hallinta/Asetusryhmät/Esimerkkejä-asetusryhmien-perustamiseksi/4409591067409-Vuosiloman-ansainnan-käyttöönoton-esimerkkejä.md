---
id: 4409591067409
title: Vuosiloman ansainnan käyttöönoton esimerkkejä
url: https://support.nepton.com/hc/fi/articles/4409591067409-Vuosiloman-ansainnan-k%C3%A4ytt%C3%B6%C3%B6noton-esimerkkej%C3%A4
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
- vuosilomalaskenta
- loma
- lomasaldo
promoted: false
updated_at: '2025-11-07T08:05:28Z'
edited_at: '2025-11-07T08:05:27Z'
---

# Vuosiloman ansainnan käyttöönoton esimerkkejä

Tässä artikkelissa on kuvattu vuosilomasaldon käsittelyn esimerkkejä. Ohjeet vuosiloman laskennan käyttöönottoon löytyy tukiartikkelista [Vuosiloman ansainnan asetukset](<https://support.nepton.com/hc/fi/articles/360002560698>).
## Esimerkki 1
Palvelu on ollut käytössä, mutta vuosilomalaskenta otetaan käyttöön alkaen 1.4.
Kun vuosilomalaskenta otetaan käyttöön takautuvasti, tulee jokaiselle henkilölle asettaa aiemmalta lomanansaintakaudelta siirtyvä lomaoikeuden määrä. Lomaoikeuden määrä asetetaan edellisen kauden maaliskuulle (1.3.2024) tapahtumatyyppinä Vuosiloman ansainnan asetus. Vuosilomasaldon määräksi asetetaan se lomakertymä, joka on ollut voimassa 1.3.2024. Tähän lomakertymään lasketaan mukaan mahdollisesti maaliskuu 2024 ansaittu lomaoikeus ja siitä huomioidaan vähentävänä maaliskuussa pidetty vuosiloma.
Esimerkiksi henkilöllä tulisi olla 1.4.2024 alkaen 30 päivää lomaoikeutta. Henkilö on ollut maaliskuussa 2024 lomalla 6 päivää ja hänen vuosilomalaskennan ansainta on käytössä, josta syntyy 2.5 päivän lomaoikeus. Kun 1.4.2024 voimassa olevaksi lomaoikeudeksi halutaan 30 päivää niin maaliskuun vuosilomasaldon asetukseksi asetetaan 30 + 6 - 2.5 päivää, eli 33.5 päivää.
Vuosiloman ansainnan asetus -tapahtumatyyppi antaa vuosilomasaldolle uuden kertymän lähtöarvon. Vuosilomasaldon kertymää tai käyttöä ennen kirjattua tapahtumaa "vuosiloman ansainnan asetus" ei huomioida laskennassa, joten kaikki aikaisemmat kertymät tulee sisällyttää asetettuun vuosilomasaldon arvoon.
## Esimerkki 2
Palvelu on ollut käytössä ja vuosilomalaskenta otetaan käyttöön kesken lomanmääräytymisvuoden, esim. 1.10.
\- Kaikki vuosilomalaskennan asetukset asetetaan voimaan alkaen 1.10.  
\- Jos Vuosilomapäiviä EI ole merkitty palveluun, 30.9 mennessä ansaitut sekä vielä käyttämättä olevat edellisen lomanmääräytymisvuoden lomat tehdään Vuosiloman ansaintamuutos -tapahtumatyypillä 30.9. Tästä eteenpäin käytetyt Vuosilomapäivät merkitään palveluun.  
\- Jos Vuosilomapäivät ON merkitty palveluun, lasketaan 30.9 käyttämättä olevat edellisen lomanmäätäytymisvuoden lomapäivät sekä 1.4. alkaen ansaitut lomapäivät ja tehdään Vuosiloman ansainnan asetus 1.10. Tästä eteenpäin käytetyt Vuosilomapäivät merkitään palveluun.
## Esimerkki 3
Vuosilomalaskenta otetaan käyttöön yhtä aikaa palvelun käyttöönoton kanssa.
Palvelun käyttöönotto on esim. 1.9. Henkilöllä A on käyttämättömiä vuosilomapäivä 6 päivää, tämä 6 päivää asetetaan vuosiloman ansainnan asetuksella saman vuoden maaliskuulle, eli 1.3. Tällöin henkilöllä A on 1.9. käytettävissään 6 lomapäivää.
Koska palvelun käyttö on aloitettu 1.9., eikä sitä ennen löydy työaikakirjauksia, ei lomien ansainnasta ole tietoja palvelussa ajalta 1.4.-31.8.
Tässä esimerkissä aikavälillä 1.4.-31.8. henkilö A on ansainnut 2,5 päivää lomaa per kuukausi, eli yhteensä 12,5 päivää. Tämä 12,5 päivää kirjataan käyttöönottokuukauden ensimmäiselle päivälle, eli 1.9. vuosiloman ansaintamuutostapahtumalla, lisäämällä kertymään +12,5pv.
Tätä 12,5 päivän lomakertymää (ja sen lisäksi 1.9. alkaen kertyviä lomapäiviä) henkilö A voi käyttää seuraavalla lomakaudella, eli seuraavan vuoden huhtikuun alusta alkaen.
