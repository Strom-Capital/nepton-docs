---
id: 360003762477
title: Implementation of SFTP integrations
url: https://support.nepton.com/hc/en-gb/articles/360003762477-Implementation-of-SFTP-integrations
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
updated_at: '2025-07-25T09:57:54Z'
edited_at: '2025-07-25T09:57:54Z'
---

# Implementation of SFTP integrations

Sorry, but this article has not been translated yet
Integraatiot voidaan toteuttaa Neptoniin eräsiirtoina käyttäen SFTP-palvelinta siirtokanavana. SFTP-palvelin voidaan perustaa joko**Asiakkaan** tai **Toimittajan** (kumppani tai Nepton) toimesta. Käytännössä SFTP-palvelimen eräsiirtoa voidaan hyödyntää mm. [_projektien_](<https://support.nepton.com/hc/fi/articles/360002492518>)tai [_tapahtumien tuonnissa_](<https://support.nepton.com/hc/fi/articles/4403974690321>), jolloin lähettävään järjestelmään tehtävät lisäykset tai muutokset päivittyvät seuraavana aamuna. 
Neptonin SFTP-palvelimen tiedonsiirto on suojattu SSH2-protokollalla. Salasanat tallennetaan PBKDF2 HMAC SHA256 hajautuksella..
SFTP-siirron periaatteena on, että lähdepalvelu muodostaa aineiston ajastetusti SFTP-palvelimelle. Tämän jälkeen kohdepalvelu noutaa ja käsittelee aineiston toisella ajastuksella. Tyypillisesti aineistoja **siirretään yöaikaan** ja muodostamisen sekä noutamisen väliin jätetään riittävästi aikaa, jotta lähdepalvelu on varmasti muodostanut aineiston. Sekä lähde- että kohdepalvelun ajastukset sovitaan osana käyttöönottoprojektia.
SFTP-liittymien käyttö sisältyy kaikkiin Neptonin palvelutasoihin. Neptonin hallinnoima SFTP-palvelu on erillishinnoiteltu lisäpalvelu. Nepton poistaa SFTP-palvelimelta kunkin vuoden tammikuussa yli 2 vuotta vanhat tiedostot. SFTP-siirto Neptonista voidaan käynnistää myös manuaalisesti, kuten on ohjeistettu [_täällä_.](<https://support.nepton.com/hc/fi/articles/360002492898>)   
  

## SFTP liittymän käyttöönotto
  1. SFTP-tiedonsiirtoa tarvitaan tiedostojen siirtämiseksi palvelimelle. SFTP-palvelimena voidaan käyttää joko asiakkaan tai toimittajan (kumppani tai Nepton) SFTP-palvelinta. SFTP-tiedonsiirron asetuksissa Neptonissa määritetään mm. millä käyttäjätunnuksilla SFTP-palvelimelle tunnistaudutaan. SFTP-palvelimelle voidaan kirjautua joko käyttäjätunnus/salasana -yhdistelmällä tai käyttäen[ Public Key-autentikointia](<https://support.nepton.com/hc/fi/articles/360015591697>). Lisää asetusten määrittämisestä Neptonissa [_täältä_](<https://support.nepton.com/hc/fi/articles/360003722778>).
  2. Aineiston vastaanottavan pään tulee kertoa missä muodossa aineisto halutaan lähetettävän. Nepton tukee useiden eri järjestelmien vaatimaa aineistomuotoa. Tuetuista järjestelmistä [lisää täältä.](<https://support.nepton.com/hc/fi/articles/360002494538>) Projektien tuontiin käytetty CSV-muotoinen mallitiedosto löytyy [täältä.](<https://support.nepton.com/hc/fi/articles/360003737078>)


### SFTP liittymän käyttöönotto aineistovientiin
Neptonista mm. **projektien tai tapahtumien viennissä** tarvitaan edellä mainittujen määritysten lisäksi [_sääntöjoukon poimintasäännöt_ ,](<https://support.nepton.com/hc/fi/articles/360002492278>) joiden perusteella määriteltyä sisältöä viedään toiseen palveluun.
