---
id: 9002553468829
title: Esimiestiedot henkilötuonnissa
url: https://support.nepton.com/hc/fi/articles/9002553468829-Esimiestiedot-henkil%C3%B6tuonnissa
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
updated_at: '2024-07-12T05:52:31Z'
edited_at: '2024-03-05T14:33:12Z'
---

# Esimiestiedot henkilötuonnissa

Henkilön esimiestietoja voidaan tuoda osana [henkilötuontia](<https://support.nepton.com/hc/fi/articles/360003762577>) ja sen kentät ovat osa [henkilötuonnin kenttiä](<https://support.nepton.com/hc/fi/articles/360015933397>).
HUOM! Jos olet päivittämässä tai asettamassa esimiestietoa usealle henkilölle kerralla, tutustu [tähän artikkeliin.](<https://support.nepton.com/hc/fi/articles/360002430658-Esimiestiedon-p%C3%A4ivitt%C3%A4minen-tai-asettaminen-usealle-henkil%C3%B6lle-kerralla>)
## Ensisijainen esimies/toissijaiset esimiehet  

  * Nämä kaksi tuontikenttää on tarkoitettu ensisijaisten ja/tai toissijaisten esimiesten asettamiseen. Asettaminen tehdään henkilönumerolla.
  * Ensisijainen esimies -kenttä käyttäytyy seuraavasti  

    * Jos tuonnissa on määritetty ensisijainen esimies, korvataan olemassa oleva uudella.
    * Jos tuonnissa on määritetty useampi kuin yksi esimies tässä kentässä, ensimmäisenä olevasta tulee ensisijainen esimies ja muut esimiehet jätetään huomioimatta.
    * Ensisijainen esimies poistetaan, jos kenttä on tuonnissa jätetty tyhjäksi tai arvona tuodaan NOLLA-avainsana, riippumatta siitä, onko IgnoreEmptyValues-asetus (valittavissa esim. tuonnissa web service -rajapinnan kautta) käytössä vai ei.
  * Toissijaiset esimiehet -kenttä käyttäytyy seuraavasti  

    * NOLLA|-etuliite kentässä - Korvataan kaikki olemassa olevat toissijaiset esimiehet tuonnissa olevilla
    * NOLLA|-etuliitettä ei ole kentässä - Lisätään tuonnissa olevat toissijaiset esimiehet olemassa olevien esimiesten listaan
    * Tukee NOLLA-avainsanaa sekä IgnoreEmptyValues-asetusta eli toissijaiset esimiehet jätetään ennalleen, jos kenttä on tuonnissa jätetty tyhjäksi ja IgnoreEmptyValues on Kyllä (esim. tuonti web service-rajapinnan kautta)
  * Toistaiseksi ensisijainen esimies -kenttä tukee vain yhtä esimiestä, mutta myöhemmin tullaan lisäämään tuki useammalle ensisijaiselle esimiehelle


Huomioithan, että ilmoitukset arkaluonteisista toimista, kuten sairausloma-, saldo- ja vuosilomapyynnöistä, lähetetään ainoastaan ensisijaisille esimiehille.
