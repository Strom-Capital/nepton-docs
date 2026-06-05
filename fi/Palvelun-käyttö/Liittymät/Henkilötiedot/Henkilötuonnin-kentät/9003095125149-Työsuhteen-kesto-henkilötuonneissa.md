---
id: 9003095125149
title: Työsuhteen kesto henkilötuonneissa
url: https://support.nepton.com/hc/fi/articles/9003095125149-Ty%C3%B6suhteen-kesto-henkil%C3%B6tuonneissa
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
updated_at: '2025-10-15T07:43:52Z'
edited_at: '2025-10-15T07:43:39Z'
---

# Työsuhteen kesto henkilötuonneissa

Työsuhteen keston tietoja voidaan tuoda osana [henkilötuontia](<https://support.nepton.com/hc/fi/articles/360003762577>) ja sen kentät ovat osa [henkilötuonnin kenttiä](<https://support.nepton.com/hc/fi/articles/360015933397>). 
"Oletus"-henkilötuontityypissä työsuhteen alku- ja loppupäivän päivitys ei toimi alla olevien sääntöjen mukaan.
"Oletus"-henkilötuonnissa työsuhteen alku- ja loppupäivä tuodaan täysin aineiston arvojen mukaisesti. Jos haluat tuoda henkilötietoja oletus-tuonnin säännöin ja mahdollisuuksin, mutta haluat että tuonti voi vain pidentää työsuhdetta alla kuvatun mukaisesti, käytä tuontityyppiä "Jatka työsopimusten päiväyksiä".
Työsuhteen päiväyksiä päivitetään henkilötuonneissa seuraavasti:
  * Työsuhteen alkupäivä
    * Jos henkilön työsuhteen alkupäivää ei ole asetettu, tallennetaan tuonnissa oleva uusi arvo.
    * Jos henkilön työsuhteen alkupäivä on jo asetettu, tallennetaan tuonnissa oleva arvo ainoastaan, jos se on aikaisempi kuin olemassa oleva arvo tai arvo on tyhjä.
  * Työsuhteen päättymispäivä
    * Jos henkilön työsuhteen päättymispäivää ei ole asetettu, tallennetaan tuonnissa oleva uusi arvo.
    * Jos henkilön työsuhteen päättymispäivä on jo asetettu, tallennetaan tuonnissa oleva arvo ainoastaan, jos se on myöhäisempi kuin olemassa oleva arvo tai arvo on tyhjä.


Tällä rajoituksella taataan, että henkilöt, joilla on useampi Työsuhteen alkupäivä, käsitellään ja näytetään palvelussa oikein.
Jos henkilöitä tuodaan käyttöliittymän kautta, Työsuhde -> Henkilöt -> Tuo henkilöitä, mahdolliset tyhjät arvot näissä kentissä jätetään huomioimatta, ellei kohtaan "Tyhjät arvot tuontitiedostossa" valita "Olemassaolevia kenttien arvoja ei muuteta (turvallisin)".
