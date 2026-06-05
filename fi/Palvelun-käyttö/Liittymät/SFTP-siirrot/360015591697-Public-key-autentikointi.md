---
id: 360015591697
title: Public key -autentikointi
url: https://support.nepton.com/hc/fi/articles/360015591697-Public-key-autentikointi
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
updated_at: '2024-09-13T07:14:30Z'
edited_at: '2024-09-13T07:09:03Z'
---

# Public key -autentikointi

Jos käytetään Public key -autentikointia, ei käyttäjätunnus/salasana -kirjautumistapa ole käytettävissä
**HUOM: Seuraavat Työsuhde-osion ajastetun tehtävän tyypit eivät ole mahdollisia Public key -autentikointia käyttäen:**
  * **Henkilötietojen tuonti Nepton-palveluun (Tuo henkilöitä)  
**
  * **Henkilötietojen vienti Nepton-palvelusta (Vie henkilöitä)  
**
  * **Maksuryhmien vienti Nepton-palvelusta (Vie maksuryhmät)  
**


Muissa tiedonsiirroissa voidaan hyödyntää RSA public key-autentikointia.
Tällöin vain Nepton palvelu voi muodostaa yhteyden SFTP palvelimelle.
Määritä sopiva käyttäjätunnus ja jätä salasana kokonaan määrittämättä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360013441618)
Nepton palvelu on jo luonut sekä julkisen että yksityisen avaimen. Voit ladata julkisen avaimen tämän artikkelin alalaidasta. Tiedostossa on useita versioita julkisesta avaimesta, jotka ovat eri formaatissa. Julkisen avaimen versio valitaan sen mukaan, mitä kohdejärjestelmä tai sovellus vaatii.
Toimita julkinen avain ja määrittämäsi käyttäjätunnus SFTP palvelimen ylläpitäjälle.
