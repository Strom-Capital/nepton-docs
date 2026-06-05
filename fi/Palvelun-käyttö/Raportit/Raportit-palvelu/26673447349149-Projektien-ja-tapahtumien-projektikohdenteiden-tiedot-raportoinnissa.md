---
id: 26673447349149
title: Projektien ja tapahtumien projektikohdenteiden tiedot raportoinnissa
url: https://support.nepton.com/hc/fi/articles/26673447349149-Projektien-ja-tapahtumien-projektikohdenteiden-tiedot-raportoinnissa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Raportit-palvelu
section_id: 25746849648925
section_path:
- Raportit
- Raportit-palvelu
labels: []
promoted: false
updated_at: '2025-09-01T09:00:31Z'
edited_at: '2025-04-22T05:33:55Z'
---

# Projektien ja tapahtumien projektikohdenteiden tiedot raportoinnissa

Tämä artikkeli liittyy Raportit-palveluun. Tarkat tietojen poimintoihin käytettävät tietokantakentät löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
##  Perusperiaatteet
Palvelussa voidaan poimia projekteihin liittyviä tietoja seuraavasti:
  * Kaikki projektin tiedoissa olevat kentät
  * Projekteille kirjatut tapahtumat ja niiden kohdenteet


Tiedot voidaan rajata esimerkiksi
  * Koskemaan tiettyä projektia (projektipuun osaa)


##  Mitä voidaan poimia – Projektin tiedot
  * Tunnisteet (sisäinen ja ulkoinen)
  * Nimi, koodi ja kuvaus
  * Projektin alkamis- ja päättymispäivä
  * Yläprojektin sisäinen tunniste
  * Projektityypin sisäinen nimi
  * Onko projektilla ylä- tai alaprojekteja
  * Onko mahdollista kohdentaa tämä projekti tapahtumalle 
    * Arvona on ei, jos projekti on tapahtumalle kirjatun projektin yläprojekti
    * Puurakenteessa vain alimman tason projektille voi kohdentaa
  * Numeerinen arvo siitä, millä tasolla projekti on puurakenteessa


##  Mitä voidaan poimia – Projekteille kirjatut tapahtumat
  * Projektille kirjattu aika, joka ylittää tapahtuman keston 
    * Esim tapahtuman kesto 6h, projekteille kirjattu aika 8h -> ylimenevä 2h voidaan raportoida
  * Tapahtumalla tietyllä järjestysnumerolla olevan projektin sisäinen ja ulkoinen tunniste, koodi, nimi, projektityyppi
  * Projektille tallennettu kesto kuten merkitty 
    * Joko prosentteina tai aika-arvona (minuutteja), riippuen miten merkitty tapahtumalle
    * Työajan tulkinta ei rajaa tai vaikuta muutoin (esim jos projekteille kirjattu pidempi aika kuin tapahtuman kesto)
  * Projektimerkinnän hyväksynyt henkilö (projektituntien hyväksyjä) 
    * Eri asia kuin tapahtuman hyväksyjä
    * Projektituntien hyväksyntähetkeä ei voida poimia
  * Projektimerkinnän sisäinen ja ulkoinen huomautus
