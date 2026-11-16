---
id: 9056218915229
title: Siirtotiedoston nimeäminen
url: https://support.nepton.com/hc/fi/articles/9056218915229-Siirtotiedoston-nime%C3%A4minen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: SFTP siirrot
section_id: 360001029457
section_path:
- Liittymät
- SFTP siirrot
labels: []
promoted: false
updated_at: '2026-07-01T05:22:04Z'
edited_at: '2026-07-01T05:22:04Z'
---

# Siirtotiedoston nimeäminen

Siirtotiedostoja käytetään SFTP-liittymätoteutuksissa siirtämään tietoa joko Nepton järjestelmään tai Neptonista ulkopuoliseen järjestelmään. Suosittelemme että siirtotiedoston nimeen sisällytetään aineiston tyyppi, tiedonsiirron suunta, sekä päivämäärä ja aika, jolloin aineisto on muodostettu. Tällä tavalla tiedostoa ei voi sekoittaa muihin siirtotiedostoihin ja mahdollisten ongelmien selvittelytilanteissa eri päivien aineistot on helppo tunnistaa. Tiedostonimessä tulee olla oikea tiedostotyyppi aineiston muodosta riippuen, esimerkiksi csv, xls tai txt.
Henkilötietoliittymässä korvauskuviot eivät toimi.  
  
Suosittelemamme nimen muoto on:
AineistonTyyppi_TiedonsiirronSuunta_YYYYMMDD_HHmm.tiedostotyyppi
Käytettävissä olevat korvauskuviot. **Huomaathan, että kaikki formaatit ovat suomenkielisessä muodossa.**  
\- [vvvvkkpphhmmss] Päivämäärä ja aika, esimerkiksi 20181201120000  
\- [vvvvkkpphhmm] Päivämäärä ja aika ilman sekunteja, esimerkiksi 201812011200  
\- [vvvvkkpp] Päivämäärä, esimerkiksi 20181201  
Eli siis esimerkiksi Lomat_Neptoniin_[vvvvkkpphhmm].csv
Esimerkiksi:
Kun Neptoniin lähetetään henkilödataa csv-muodossa 30.1.2023 klo 23:35 tiedoston nimi olisi:  
Persons_ToNepton_20230130_2335.csv
Kun Neptoniin lähetetään henkilödataa txt-muodossa 30.1.2023 klo 23:35 tiedoston nimi olisi:  
Persons_ToNepton_20230130_2335.txt
