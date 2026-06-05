---
id: 360002492518
title: Projektien ajastettu tuonti
url: https://support.nepton.com/hc/fi/articles/360002492518-Projektien-ajastettu-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Projektit
section_id: 360001075297
section_path:
- Liittymät
- Projektit
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2023-09-11T12:28:52Z'
edited_at: '2023-05-16T07:48:54Z'
---

# Projektien ajastettu tuonti

Palveluun voidaan tuoda ja päivittää projekteja ajastetusti joko API-rajapinnalla tai tiedostolatauksen kautta.
## Projektien tuonti tiedostolatauksella
Tiedostolatausta käytettäessä projektien tuonti määritellään valikossa **Työaika - > Hallinta -> Työyhteisön asetukset -> Liittymät -> Projektien tuonti. **Siirrossa käytetään tiedostoa, jonka Nepton hakee SFTP-palvelimelta ja SFTP-palvelimen tiedot määritellään tässä valikossa Neptoniin. Tiedoston tulee sisältää sarakkeita, jotka on kuvattu [tässä artikkelissa.](<https://support.nepton.com/hc/fi/articles/360003737078>)
Huomioithan tiedostolatauksen määrittelyjä tehdessä; Mikäli Public key -autentikointi on päällä, niin salasanan sijaan SFTP-palvelimen kirjautumiseen käytetään epäsymmetristä RSA-avainparia. Tällöin salasanaa ei aseteta. Avainparin julkinen osa pyydetään asiakkaan IT-toimittajalta ja se toimitetaan SFTP-palvelimen ylläpitäjälle. Mikäli SFTP-palvelimen ylläpitäjä on Nepton, toimitetaan avainparin julkinen osa Neptonin asiakaspalveluun.
Projektien tuonti voidaan ajastaa automaattisesti tapahtuvaksi. Ajastukset löytyvät valikosta:
**Työaika - > Hallinta -> Työyhteisön asetukset -> Liittymät -> Ajastus**.
Ajastusosiosta voit lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/10510800700573>)
## Projektien tuonti API-rajapinnalla
Projektien API:n tarkemman kuvauksen löydät [tästä artikkelista.](<https://support.nepton.com/hc/fi/articles/360019840237>)
