---
id: 4411066690833
title: Lyhytaikaislainojen maksuaineiston luonti
url: https://support.nepton.com/hc/fi/articles/4411066690833-Lyhytaikaislainojen-maksuaineiston-luonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Lyhytaikaislainat henkilöstölle
section_id: 4411038990225
section_path:
- Henkilöstö
- Lyhytaikaislainat henkilöstölle
labels: []
promoted: false
updated_at: '2026-11-04T12:56:46Z'
edited_at: '2026-11-04T12:37:59Z'
---

# Lyhytaikaislainojen maksuaineiston luonti

## Lyhytaikaislainojen massahyväksyntä ja maksuaineiston luonti
Lyhytaikaislainojen maksuaineiston luontiin pääset menemällä Työsuhde > Palvelupyynnöt > Lyhytaikaislainojen maksuaineiston luonti. Maksuaineiston luonnin lisäksi näkymässä massahyväksytään, sekä tarvittaessa hylätään, avoimet lyhytaikaislainapyynnöt. Luotavan aineiston avulla lainat saadaan maksettua henkilöstölle massana, eikä manuaalista yksittäisten maksujen käsittelyä tarvita. Maksuaineisto muodostetaan ISO20022 pain.001.001.02 standardin mukaisesti.
Maksuaineiston luonti ja massahyväksyntä tapahtuu seuraavasti:
  1. Valitse yritys, jonka lyhytaikaislainoista maksuaineisto halutaan luoda.
  2. Aseta jakson alku- ja loppupäivämäärä, jolta listauksessa lainapyyntöön liittyvä työtuntimäärä ja siihen liittyvä ansaittu summa lasketaan.
  3. Määritä työtunnin hinta €/h jonka mukaan "Ansaittu summa" lasketaan.
  4. Valitse lähetetäänkö lainapäätöksen tuloksesta viesti lainan pyytäjälle.
  5. Paina "Hae avoimet lainat jaksolle" **HUOM.** Listalle haetaan kaikki avoimet lainapyynnöt valitusta jaksosta huolimatta.
  6. Hyväksy/hylkää lainapyynnöt rivikohtaisesti ja muuta lainasummaa tarvittaessa. Lisää halutessasi myös lainan pyytäjälle näkyvä kommentti.
  7. Määritä maksuunmenopäivä sekä maksupäivä.
  8. Paina "Päivitä / Luo tiedostot".
  9. Saat ladattavaksesi zip-tiedoston, joka sisältää pankille lähetettävän maksuaineiston, sekä Mepcoon sisäänluettavaksi tarkoitetun siirtotiedoston hyväksytyistä lyhytaikaisista lainoista.


![mceclip0.png](https://support.nepton.com/hc/article_attachments/21077191854365)
## Miksi maksuaineiston luonti ei onnistu?
**Avoimia lyhytaikaislainapyyntöjä ei löydy maksuaineiston luontia varten**
  1. Tarkista että lyhytaikaislainapyynnön tehneen henkilön lisätietokentistä löytyvä "Työnantaja"-kenttä on asetettu.
  2. Tarkista että henkilön [lisätietokenttien hallinnasta](<https://support.nepton.com/hc/fi/articles/360002430918>) "Työnantaja"-lisätietokentän valittavissa olevien arvojen lista (Työsuhde > Hallinta > Henkilön lisätietokentät > Työnantaja-kenttä > Muokkaa (kynäkuvake)). Listalla pitäisi näkyä työnantaja, joka on valittu henkilön "Työnantaja"-kenttään. Tämän "Nimi"-sarakkeesta pitäisi löytyä työnantajan nimi, sekä **"Arvo"-sarakkeesta työnantajaan liittyvä IBAN-tilinumero**. IBAN-tilinumero on tilinumero, josta työntekijöille maksetaan lyhytaikaiset lainat.
  3. Lisäksi varmista, että tähän työnantajaan liittyvä IBAN-tilinumero, sekä muut maksamiseen tarvittavat tiedot on ilmoitettu Neptonin asiakaspalveluun. Neptonin tarvitsee tietää lainan maksavan työnantajan nimi, yritystunnus, maksajan tunniste, katuosoite, sekä maksutilin BIC ja IBAN. Tiedot tarvitsee ilmoittaa vain kerran uuden työnantajan lisäämisen yhteydessä.
