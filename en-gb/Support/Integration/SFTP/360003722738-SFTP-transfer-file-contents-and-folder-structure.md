---
id: 360003722738
title: SFTP transfer file contents and folder structure
url: https://support.nepton.com/hc/en-gb/articles/360003722738-SFTP-transfer-file-contents-and-folder-structure
locale: en-gb
category: Support
category_id: 360000446658
section: SFTP
section_id: 360001029457
section_path:
- Integration
- SFTP
labels: []
promoted: false
updated_at: '2026-11-04T09:37:26Z'
edited_at: '2026-06-04T10:46:32Z'
---

# SFTP transfer file contents and folder structure

Sorry, but this article has not been translated yet
SFTP siirtojen avulla voidaan tuoda ja viedä aineistoja seuraaviin kokonaisuuksiin liittyen:
  * Henkilötiedot, työsuhdetiedot ja muut henkilön lisätiedot.
  * Työaikakirjaukset. Näitä käsitellään palvelussa tapahtumina.
  * Projekti-, kustannuspaikka tai työnumerotiedot. Näitä käsitellään palvelussa työn kohteina eli projekteina.


SFTP palvelimelle perustetaan kansiorakenne siten, että jokaista siirrettävää tietosisältöä varten on oma kansionsa. Jokaisen kansion alla on alikansio **/ToNepton** tai **/FromNepton** riippuen siitä tuodaanko tieto Neptoniin vai siirretäänkö tieto Neptonista toiseen palveluun. Jokaisessa alikansiossa on vielä valinnainen **/archive** kansio, johon käsitellyt tiedostot arkistoidaan.
Huom! Neptonin tuomaa poissaoloaineistoa tai palkka-aineistoa varten tarvitaan **/stage** -alakansio. Jos kansiota ei löydy, liittymä yrittää perustaa sen SFTP-palvelimelle.
Nepton lähettää aineiston omaan alakansioonsa jotta keskeneräistä tiedostoa ei käsiteltäisi. Tiedoston lähetyksen jälkeen se siirretään hakemistoon, mistä aineiston hakeva järjestelmä sen käsittelee.
  
Huom! SFTP-käyttöoikeudet on määritettävä niin, että tiedostoja voidaan siirtää hakemistojen välillä. Tiedostojen siirto-/uudelleennimeämisoikeus vaaditaan sekä työaika-vientiä, että -tuontia varten. Vienti perustuu tiedostojen siirtämiseen /stage -kansiosta, ja useimmat tuontitavat siirtävät tiedostot "archive/"-hakemistoon, kun ne on käsitelty.
Alla on esimerkki kansiorakenteesta, jossa Neptoniin tuodaan henkilöt ja projektit sekä Neptonista viedään palkanlaskennan lähtöaineisto.
  * ~/absences/ToNepton/
  * ~/absences/ToNepton/archive
  * ~/employees/ToNepton/
  * ~/employees/ToNepton/archive
  * ~/projects/ToNepton/
  * ~/projects/ToNepton/archive
  * ~/salary/FromNepton/
  * ~/salary/FromNepton/archive
  * ~/salary/FromNepton/stage


### Siirtotiedostojen nimeäminen
Lue [suosituksemme siirtotiedoston nimeämiseen](<https://support.nepton.com/hc/fi/articles/9056218915229>).
