---
id: 26673418239901
title: Henkilö- ja työsuhdetiedot raportoinnissa
url: https://support.nepton.com/hc/fi/articles/26673418239901-Henkil%C3%B6-ja-ty%C3%B6suhdetiedot-raportoinnissa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Raportit-palvelu
section_id: 25746849648925
section_path:
- Raportit
- Raportit-palvelu
labels: []
promoted: false
updated_at: '2025-09-01T09:02:01Z'
edited_at: '2025-08-20T04:48:17Z'
---

# Henkilö- ja työsuhdetiedot raportoinnissa

Tämä artikkeli liittyy Raportit-palveluun. Tarkat tietojen poimintoihin käytettävät tietokantakentät löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
# 
# Perusperiaatteet
Palvelussa voidaan poimia henkilö- ja työsuhdetietoihin tallennettuja tietoja seuraavasti:
  * Lähes kaikki henkilötietokentät on poimittavissa 
    * Katso poikkeukset alla
    * Kaikille tietokentille, joissa on voimassaolotoiminto, voidaan poimia myös arvon voimassaoloaika 
      * Voidaan hyödyntää esim jos halutaan raportoida henkilön kaikki asetusryhmät kautta historian
    * Myös [lisätietokenttiin](<https://support.nepton.com/hc/fi/articles/360002430918-Henkil%C3%B6n-lis%C3%A4tietokenttien-hallinta>) merkityt tiedot voidaan poimia raportille
  * Henkilön työsuhteen alku- ja loppupäivä 
    * Kesto saadaan myös. 
      * Ei saada sellaisenaan valmiina tietyllä tietokantakentällä, mutta raportille saadaan tehtyä valmiiksi kenttä, johon tieto lasketaan sille päivälle, kun raportti ajetaan


Henkilö- ja työsuhdetiedot voidaan ryhmitellä
  * Henkilöittäin
  * Henkilöryhmittäin
  * Asetusryhmittäin


#  Mitä voidaan poimia
  * Tietojen voimassaoloajat (päivä ja aika, milloin tiedon voimassaoloaika alkaa tai päättyy) 
    * Vain kentissä, joissa on voimassaolotoiminto
  * Etunimi
  * Sukunimi
  * Yhteystiedot (osoite, sähköpostiosoite, puhelinnumero, pankkiyhteystiedot)
  * Lähiomaisen tiedot
  * RFID-tunnisteen koodi
  * Käyttäjänimi
  * Työsuhteen rooli (rooli)
  * Työajan rooli (sisäinen tunniste ja/tai nimi)
  * Henkilöryhmä (koodi, sisäinen tunniste ja/tai nimi)
  * Juuritason henkilöryhmä (koodi, sisäinen tunniste ja/tai nimi)
  * Ensisijainen ja toissijainen esihenkilö
  * Työskentelyalue
  * Ammattinimike
  * Oletusprojekti (koodi, sisäinen tunniste ja/tai nimi)
  * Asetusryhmä (koodi, sisäinen tunniste ja/tai nimi)
  * Kalleusluokka
  * Oletuskustannuspaikka
  * Palkkaus (kk tai tp) 
    * Sopimuksen tyyppi -kenttä henkilön tiedoissa TAI Palkkaus-kenttä asetusryhmässä (kummatkin voidaan poimia)
    * Käytetään ensisijaisesti asetusryhmän palkkaus-kenttää, paitsi jos käytössä Palkat-palvelu, jolloin ensisijaisesti käytetään Sopimuksen tyyppi -kenttää.
    * Sopimuksen tyyppi -kenttä yliajaa palkkaus-kentän liittymillä
  * Palkan määrä (numeerinen) 
    * pakollinen ja käytetään vain, jos Palkat-palvelu on käytössä
    * Kuukausipalkka- ja tuntipalkka-kentät henkilön tiedoissa
  * Työsuhteen alku- ja loppupäivä
  * Syy työsopimuksen päättymiseen
  * Työsuhde-osioon tallennetut (Vuorosuunnitteluun liittyvät): 
    * Vuorokautinen työaika
    * Viikottaiset tunnit MIN ja MAX
  * Henkilön liittymässä yksilöivä tunniste, muodostuu valitun liittymän mukaisesti, voi olla 
    * Henkilönumero
    * Henkilötunnus
    * Tiettyä integraatiota varten asetettu tunniste
  * Lisätietokenttiin merkitty tieto


#  Ei voida poimia
  * Osaamiset
