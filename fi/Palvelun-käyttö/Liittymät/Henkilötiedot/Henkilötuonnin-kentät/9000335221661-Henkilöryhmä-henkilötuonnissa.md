---
id: 9000335221661
title: Henkilöryhmä henkilötuonnissa
url: https://support.nepton.com/hc/fi/articles/9000335221661-Henkil%C3%B6ryhm%C3%A4-henkil%C3%B6tuonnissa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötuonnin kentät
section_id: 9000763181981
section_path:
- Liittymät
- Henkilötiedot
- Henkilötuonnin kentät
labels: []
promoted: false
updated_at: '2026-06-26T06:10:39Z'
edited_at: '2026-06-26T06:10:15Z'
---

# Henkilöryhmä henkilötuonnissa

Henkilöryhmätietoja voidaan tuoda osana [henkilötuontia](<https://support.nepton.com/hc/fi/articles/360003762577>) ja on yksi [henkilötuonnin kentistä](<https://support.nepton.com/hc/fi/articles/360015933397>).
### Tuonnin säännöt
  * Jos tuotavaa henkilöryhmää ei ole olemassa, se luodaan hierarkian juuritasolle.
  * NOLLA-avainsana poistaa henkilön kaikista henkilöryhmistä. Henkilöryhmiin kuulumisella ei ole voimassaoloaikoja.


###  Henkilöryhmällä on hierarkiarakenne eli puurakenne  

  * Käytetään sekä henkilöryhmän asettamiseen että henkilöryhmähierarkian tuomiseen.
  * Näiden tietojen tuonnin tuki riippuu lähdejärjestelmän/tuonnin asetuksista.


### Henkilöryhmän tuonnissa on kaksi tapaa
  * Käytetään yhtä kenttää henkilöryhmän koodille ja toista henkilöryhmän nimelle
    * Esim. Koodi, Nimi
      * Kenttien nimet riippuvat lähdejärjestelmästä
    * Koodi-kentässä on erotettu koodit toisistaan piippu (|) merkillä
      * Oikeanpuoleisin koodi on asetettavan henkilöryhmän koodi ja tästä vasemmalle olevat koodit määrittävät henkilöryhmän hierarkian
    * Nimi-kenttä käyttäytyy samalla tavalla Koodi-kenttä, mutta siinä on henkilöryhmien nimet
      * Nimi-kentän käyttö on valinnaista ja ainoastaan lisäinformaatiota koodeille. Jos ainoastaan koodit on määritetty, tulee koodeista uusien ryhmien nimet.


  * Käytetään useampaa kenttää henkilöryhmän koodeille ja useampaa henkilöryhmän nimille
    * Esim. Koodi1, Koodi2 ja Nimi1, Nimi2
      * Kenttien nimet riippuvat lähdejärjestelmästä
    * Kenttien järjestyksellä on merkitystä, ei niiden nimillä
      * Oikeanpuoleisin kenttä on asetettavan henkilöryhmän koodi/nimi ja tästä vasemmalle olevat koodit/nimet määrittävät henkilöryhmän hierarkian
  * Jos tuonnissa määriteltyä henkilöryhmähierarkiaa ei ole olemassa, se luodaan
    * Jos tuonnissa vasemmanpuoleisinta ryhmää ei ole olemassa, se luodaan hierarkian juuritasoksi
      * Tuonnissa ryhmät vasemmanpuoleisen ryhmän jälkeen luodaan sen alle, ellei vastaavia ryhmiä löydy. Jos vastaava ryhmä löytyy, siirretään olemassa olevat ryhmät uuteen paikkaan hierarkiassa.
    * Jos tuonnissa vasemmanpuoleisin ryhmä on olemassa, tuonnissa oleva hierarkia luodaan sen alle, jos sitä ei ole olemassa.
  * Kaikkien henkilöryhmäkoodien on oltava yksilöllisiä - samaa koodia ei siis voi olla kahdella eri henkilöryhmällä vaikka ne olisivat eri hierarkioiden alla.
