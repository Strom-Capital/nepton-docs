---
id: 360002492898
title: Työajan liittymät
url: https://support.nepton.com/hc/fi/articles/360002492898-Ty%C3%B6ajan-liittym%C3%A4t
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels:
- liittymä
- sääntöjoukko
- liittymät
- integraatio
- liittymäaineisto
- manuaalinen
- palkkaliittymä
- palkka-ajo
- vakiomuotoinen
promoted: false
updated_at: '2026-08-14T12:38:50Z'
edited_at: '2026-08-14T12:35:44Z'
---

# Työajan liittymät

Nepton työajankirjausten ja toisen palvelun välille on toteutettu [vakiomuotoisia](<https://support.nepton.com/hc/fi/articles/360002494538>) liittymiä. Liittymiä voidaan toteuttaa palvelusta ladattavina siirtotiedostoina, ajastettuina tiedostosiirtoina tai web service -rajapintoja hyödyntäen. Voit lukea lisää liittymistä [täältä](<https://support.nepton.com/hc/fi/articles/360002489417>).
## Vakiomuotoisen aineiston lataaminen käyttöliittymässä
Vakiomuotoisen aineiston voi ladata käyttöliittymästä seuraavalla tavalla:
Navigoi **Työaika** > **Hallinta** > **Liittymät > Haluamasi palkkajärjestelmä**
![](https://support.nepton.com/hc/article_attachments/38369710023965)
  * Valitse aikaväli
  * Valitse tasoittumisjakson aikaväli tarvittaessa
  * Valitse se sääntöjoukko, jonka määrittelemä tieto poimitaan. Aineiston poimintaa ilman valittua sääntöjoukkoa ei suositella, koska tällöin palvelun muodostamaan sisältöön ei voida tehdä muutoksia. Liittymien poiminta tulee toteuttaa sääntöjoukkoja käyttäen. Lisää sääntöjoukoista voi lukea [täältä](<https://support.nepton.com/hc/fi/articles/360002492278>).
  * Tee poiminnan lisäasetukset:
    * Hyväksytyt tapahtumat ovat tapahtumia, joille on annettu hyväksyntä, esimerkiksi esihenkilö on hyväksynyt tapahtuman. ("Siirrä vain hyväksytyt tapahtumat" -valinnan voi valita silloin kun Sääntöjoukkoa ei ole valittu. Kun valitaan itse luotu sääntöjoukko, poimintasäännössä tulee määritellä se, tuleeko siirrettävien tapahtumien olla hyväksyttyjä.)
    * Lukitse tapahtumat siirtotiedoston loppupäivämäärän saakka tarkoittaa, että päivämäärät lukitaan valitun aikavälin loppupäivämäärän saakka. HUOM. Jos valinnoille ei muodostu aineistoa, päivämääriä ei lukita.
    * Lähetä siirtotiedosto sähköpostiosoitteisiin. Aineisto lähetetään valittuun sähköpostiin. Tätä kenttää ei ole pakko täyttää. Viimeisimmän lähetyksen sähköpostiosoitteet tallentuvat ja ovat oletuksena seuraavassa lähetyksessä.
  * Lähetä siirtotiedosto SFTP-palvelimelle. Aineisto lähetetään joko liittymän tai valitun sääntöjoukon asetuksissa määritellylle SFTP-palvelimelle. Tätä kenttää ei ole pakko täyttää.
    * SFTP-asetusten tulee olla valmiina
    * Jos kohdepalvelin on käytössä, käytetään tätä
    * Jos sääntöjoukkoa ei ole valittu, käytetään liittymän SFTP-asetuksia
    * Kun sääntöjoukko on valittu, käytetään valitun sääntöjoukon SFTP-asetuksia
    * Vaihtoehtoisesti liittymän kohdepalvelin voidaan valita alemmasta valinnasta "liittymän kohdepalvelin"
  * Lähetä siirtotiedosto web-servicelle. Web-servicen asetukset on oltava määritettyinä. Tämä vaihtoehto tulee olla valittuna kun lähetetään tietoja esim. Netvisoriin tai muutoin rajapinnan kautta Neptonista toiseen järjestelmään.
  * Liittymän kohdepalvelin. Oletuksena käytetään sääntöjoukon tai liittymän asetuksiin määriteltyä kohdepalvelinta, ellei tähän olla toisin määritelty.
  * Esikatselu. Tätä tilaa hyödyntämällä voi tehdä ajon vain tarkastelua (ei siirtoa) varten.
  * Valitse henkilöt joiden tiedot poimitaan aineistoon
