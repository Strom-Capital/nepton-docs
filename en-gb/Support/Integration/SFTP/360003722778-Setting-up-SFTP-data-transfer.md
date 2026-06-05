---
id: 360003722778
title: Setting up SFTP data transfer
url: https://support.nepton.com/hc/en-gb/articles/360003722778-Setting-up-SFTP-data-transfer
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
updated_at: '2026-06-04T10:41:39Z'
edited_at: '2026-06-04T10:41:39Z'
---

# Setting up SFTP data transfer

This article has not been translated yet.
SFTP-tiedonsiirtoa tarvitaan tiedostojen siirtämiseksi palvelimelle. SFTP-palvelimena voidaan käyttää joko asiakkaan tai toimittajan (kumppani tai Nepton) SFTP-palvelinta.
Nepton ottaa yhteyden SFTP-asetuksissa määritellyllä tavalla asetetun ajastuksen mukaisesti. Nepton kirjautuu SFTP-palvelimelle käyttäjätunnuksella ja salasanalla, jotka ovat saatu SFTP toimittajalta. Asiakkaan tulee huolehtia tarpeellisista palomuuriavauksista tiedonsiirron onnistumiseksi omista lähde- tai kohdejärjestelmistään.
Kansio- tai tiedostonimissä ei tueta erikoismerkkejä, eikä skandinaavisia merkkejä.
## SFTP-palvelimen määrittäminen Työsuhde-osiossa
Tiedostopalvelimen tiedot löytyvät valikosta **Työsuhde - > Hallinta -> Ajastetut tehtävät -> Lisää tehtävä.**
Työsuhde-osiossa määritetään sekä viennin, että tuonnin asetukset.
SFTP-palvelimen omistajan tulee huolehtia palvelimen osoitteesta ja käyttäjätunnuksista. 
Portti on SFTP-siirroissa tavallisesti 22.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4409329930129)
Työkansio määritetään suhteellisena polkuna kirjautumisen jälkeen avautuvaan kansioon, esimerkiksi "in".
Käsiteltyjen tuontitiedostojen arkistointikansio määritetään vastaavasti, esimerkiksi "ToNepton/processed". Kummassakaan tapauksessa "-merkkejä ei kirjoiteta polkuun. Tieto on pakollinen.
## SFTP palvelimen määrittäminen Työaika-osiossa
Tapahtumatietojen ja projektitietojen tuonnissa Nepton kirjautuu SFTP-palvelimelle joko käyttäjätunnuksella tai Nepton palvelun julkisella varmenteella.
Asetukset tulee määrittää työyhteisötasolle, jotta ajastuksen määritykset toimivat.
Oletuksena portti on 22. Tähän voidaan myös määrittää eri portti SFTP-palvelimen osoite-kentässä, esimerkki "192.168.0.1:22" ohjaa porttiin 22. 
### Tapahtumien tuonti
Tapahtumien tuonnin asetukset löytyvät valikosta **Työaika - > Työyhteisön asetukset -> Ulkoiset palvelut -> Tapahtumien tuonti.**
![SFTP_path_5.png](https://support.nepton.com/hc/article_attachments/360015198617)
SFTP suhteellisen hakemiston polku määritetään suhteellisena polkuna kirjautumisen jälkeen avautuvaan kansioon, esimerkiksi "in".
SFTP arkistoinnin suhteellisen hakemiston polku määritetään vastaavasti, esimerkiksi "ToNepton/Processed". Kummassakaan tapauksessa "-merkkejä ei kirjoiteta polkuun.
### Projektien tuonti
Projektien tuonnin asetukset löytyvät valikosta **Työaika - > Työyhteisön asetukset -> Ulkoiset palvelut -> Projektien tuonti.**
![SFTP_path_3.png](https://support.nepton.com/hc/article_attachments/360015257158)
SFTP suhteellisen hakemiston polku määritetään suhteellisena polkuna kirjautumisen jälkeen avautuvaan kansioon, esimerkiksi "in".
SFTP arkistoinnin suhteellisen hakemiston polku määritetään vastaavasti, esimerkiksi "ToNepton/Processed". Kummassakaan tapauksessa "-merkkejä ei kirjoiteta polkuun.
Työaika-osion vienneissä SFTP-palvelimen määrittäminen tehdään erikseen kutakin vientiä koskien.
## SFTP-käyttäjätunnuksen määrittely
Palvelusta on mahdollista kirjautua SFTP-palvelimelle kahdella eri tavalla. Perinteinen käyttäjätunnus/salasana-yhdistelmä on yleisimmin käytetty tapa. Toinen tapa on kirjautua käyttäen Public Key-autentikointia. Tarkempi ohje löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360015591697>).
Huom. Molemmat tavat eivät voi olla yhtä aikaa käytössä.
Palvelu käyttää stage-kansiota aineiston muodostamisen aikaisena työkansiona ja ko. kansio on määritetyn työkansion alikansiona.
Huomioithan, että käyttäjätunnus tarvitsee riittävät oikeudet työkansioon sekä sen alikansioihin:
  * Tiedostojen luonti
  * Tiedostojen poisto


## SFTP-arkistointi 
Palvelussa on mahdollista arkistoida käsiteltyjä tuontitiedostoja. Tätä varten pitää luoda arkistoinnin kansio ja määrittää tämän kansion polku palvelussa. Arkistoinnin kansioon muodostuu automaattisesti VUOSI-KK muotoisia alakansioita, johon arkistoitavat tiedostot siirretään.
Jos tiedoston tuonti epäonnistuu kokonaan virheiden takia ei kyseistä tiedostoa arkistoida. Tällä tavoin estämme ongelmat, joita saattaa aiheutua, jos aikaisempi (epäonnistunut) tiedosto sisältää tietoja, jotka ovat kriittisiä myöhemmille tiedostoille.On monia käyttötapauksia, joissa tämä voi aiheuttaa ongelmia.
Huomioithan, että mikäli arkistointi on käytössä, käyttäjätunnus tarvitsee riittävät oikeudet arkistokansioon
  * Tiedostojen luonti
  * Tiedostojen poisto
  * Kansioiden luonti
  * Kansioiden poisto
