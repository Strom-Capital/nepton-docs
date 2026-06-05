---
id: 360003722778
title: SFTP-tiedonsiirron määrittäminen
url: https://support.nepton.com/hc/fi/articles/360003722778-SFTP-tiedonsiirron-m%C3%A4%C3%A4ritt%C3%A4minen
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
updated_at: '2026-06-04T10:41:39Z'
edited_at: '2026-06-04T10:40:47Z'
---

# SFTP-tiedonsiirron määrittäminen

Tässä ohjeessa kerrotut tavat määrittää SFTP-palvelin liittymille koskee ennen 25.9.2025 määriteltyjä liittymiä. Tämän jälkeen luotujen liittymien SFTP-palvelimen asetukset määritellään [kohdepalvelimen](<https://support.nepton.com/hc/fi/articles/26861716054045>) kautta.
SFTP-tiedonsiirtoa tarvitaan tiedostojen siirtämiseksi palvelimelle. SFTP-palvelimena voidaan käyttää joko asiakkaan tai toimittajan (kumppani tai Nepton) SFTP-palvelinta.
Nepton ottaa yhteyden SFTP-asetuksissa määritellyllä tavalla asetetun ajastuksen mukaisesti. Nepton kirjautuu SFTP-palvelimelle käyttäjätunnuksella ja salasanalla, jotka ovat saatu SFTP-toimittajalta. Asiakkaan tulee huolehtia tarpeellisista palomuuriavauksista tiedonsiirron onnistumiseksi omista lähde- tai kohdejärjestelmistään. Lisätietoa näistä vaatimuksista saat tukipalvelun artikkelista [täältä](<https://support.nepton.com/hc/fi/articles/360009237257-Asiakasverkkojen-vaatimukset>).
Kansio- tai tiedostonimissä ei tueta erikoismerkkejä, eikä skandinaavisia merkkejä.
## SFTP-palvelimen määrittäminen Työsuhde-osiossa
Tiedostopalvelimen tiedot löytyvät valikosta **Työsuhde - > Hallinta -> Ajastetut tehtävät -> Lisää tehtävä.**
Työsuhde-osiossa määritetään sekä viennin että tuonnin asetukset.
SFTP-palvelimen omistajan tulee huolehtia palvelimen osoitteesta ja käyttäjätunnuksista. 
SFTP-siirtojen portti on tavallisesti 22.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080521436829)
Huomaa, että HTML-koodi (esim. **<** tekstin edellä) ei ole sallittua salasanakentässä.
Työkansio määritetään suhteellisena polkuna kirjautumisen jälkeen avautuvaan kansioon, esimerkiksi "in".
Käsiteltyjen tuontitiedostojen arkistointikansio määritetään vastaavasti, esimerkiksi "ToNepton/Processed". Kummassakaan tapauksessa "-merkkejä ei kirjoiteta polkuun. Tieto on pakollinen.
Tarkempi ohjeistus henkilötietojen ajastetun tuonnin määritykseen[ täällä](<https://support.nepton.com/hc/fi/articles/360002489317>) ja ajastetun viennin määritykseen [täällä](<https://support.nepton.com/hc/fi/articles/360002489357>).
## SFTP-palvelimen määrittäminen Työaika-osiossa
Tapahtumatietojen ja projektitietojen tuonnissa Nepton kirjautuu SFTP-palvelimelle joko käyttäjätunnuksella tai Nepton-palvelun julkisella varmenteella (''Public Key'').
Mikäli siirto halutaan ajastaa, on asetukset määritettävä Työyhteisön asetukset-tasolla Liittymien ajastus-kohdassa.
Oletuksena portti on 22. Tähän voidaan myös määrittää eri portti SFTP-palvelimen osoite-kentässä, esimerkiksi "192.168.0.1:22" ohjaa porttiin 22. 
### Tapahtumien tuonti
Tapahtumien tuonnin asetukset löytyvät valikosta **Työaika - > Työyhteisön asetukset -> Liittymät -> Tapahtumien tuonti.**
![SFTP_path_5.png](https://support.nepton.com/hc/article_attachments/21080526519837)
SFTP suhteellisen hakemiston polku määritetään suhteellisena polkuna kirjautumisen jälkeen avautuvaan kansioon, esimerkiksi "in".
SFTP arkistoinnin suhteellisen hakemiston polku määritetään vastaavasti, esimerkiksi "ToNepton/Processed". Kummassakaan tapauksessa "-merkkejä ei kirjoiteta polkuun.
### Projektien tuonti
Projektien tuonnin asetukset löytyvät valikosta **Työaika - > Työyhteisön asetukset -> Liittymät -> Projektien tuonti.**
![SFTP_path_3.png](https://support.nepton.com/hc/article_attachments/21080521434141)
SFTP suhteellisen hakemiston polku määritetään suhteellisena polkuna kirjautumisen jälkeen avautuvaan kansioon, esimerkiksi "in".
SFTP arkistoinnin suhteellisen hakemiston polku määritetään vastaavasti, esimerkiksi "ToNepton/Processed". Kummassakaan tapauksessa "-merkkejä ei kirjoiteta polkuun.
Työaika-osion vienneissä SFTP-palvelimen määrittäminen tehdään erikseen kutakin vientiä koskien.
## SFTP-käyttäjätunnuksen määrittely
Palvelusta on mahdollista kirjautua SFTP-palvelimelle kahdella eri tavalla. Perinteinen käyttäjätunnus/salasana-yhdistelmä on yleisimmin käytetty tapa. Toinen tapa on kirjautua käyttäen Public Key-autentikointia. Tarkempi ohje löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360015591697>).
Huom. Molemmat tavat eivät voi olla yhtä aikaa käytössä.
Palvelu käyttää stage-kansiota aineiston muodostamisen aikaisena työkansiona ja kyseinen kansio toimii määritetyn työkansion alikansiona.
Huomioithan, että käyttäjätunnus tarvitsee riittävät oikeudet työkansioon sekä sen alikansioihin:
  * Tiedostojen luonti
  * Tiedostojen poisto


Mikäli oikeudet eivät ole riittävät, voi Nepton palauttaa esimerkiksi alla olevan kaltaisen virheilmoituksen. Virheilmoitus viittaa siihen, että Neptonilla ei ole oikeuksia luoda uutta kansiota palvelimelle:
![](https://support.nepton.com/hc/article_attachments/19962334945053)
## SFTP-arkistointi 
Palvelussa on mahdollista arkistoida käsiteltyjä tuontitiedostoja. Tätä varten pitää luoda arkistoinnin kansio ja määrittää tämän kansion polku palvelussa. Arkistoinnin kansioon muodostuu automaattisesti VUOSI-KK muotoisia alakansioita, johon arkistoitavat tiedostot siirretään.
Jos tiedoston tuonti epäonnistuu kokonaan virheiden takia, ei kyseistä tiedostoa arkistoida. Tällä tavoin estämme ongelmat, joita saattaa aiheutua, jos aikaisempi (epäonnistunut) tiedosto sisältää tietoja, jotka ovat kriittisiä myöhemmille tiedostoille. On monia muitakin käyttötapauksia, joissa tämä voi aiheuttaa ongelmia.
Huomioithan, että mikäli arkistointi on käytössä, käyttäjätunnus tarvitsee riittävät oikeudet arkistokansioon
  * Tiedostojen luonti
  * Tiedostojen poisto
  * Kansioiden luonti
  * Kansioiden poisto


Mikäli oikeudet eväti ole riittävät, voi Nepton palauttaa esimerkiksi alla olevan kaltaisen virheilmoituksen. Virheilmoitus viittaa siihen, että Neptonilla ei ole oikeuksia luoda uutta kansiota palvelimelle:
![](https://support.nepton.com/hc/article_attachments/19962334945053)
