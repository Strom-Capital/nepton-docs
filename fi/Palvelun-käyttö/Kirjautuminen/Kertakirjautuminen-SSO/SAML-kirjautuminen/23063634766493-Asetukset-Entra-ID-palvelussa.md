---
id: 23063634766493
title: Asetukset Entra ID palvelussa
url: https://support.nepton.com/hc/fi/articles/23063634766493-Asetukset-Entra-ID-palvelussa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: SAML-kirjautuminen
section_id: 360004542757
section_path:
- Kirjautuminen
- Kertakirjautuminen (SSO)
- SAML-kirjautuminen
labels: []
promoted: false
updated_at: '2026-11-03T13:46:04Z'
edited_at: '2026-11-03T13:46:03Z'
---

# Asetukset Entra ID palvelussa

Tätä menetelmää tulee käyttää vain mikäli ette pysty käyttämään suositeltua [Microsoft Kirjautuminen](<https://support.nepton.com/hc/fi/articles/360002590137>) -menettelyä.
Alla on yksityiskohtaiset tekniset ohjeet asiakkaan Entra ID palvelun määrittämiseen SAML-pohjaiselle SSO:lle (Single Sign On) Nepton palvelussa. Nämä ohjeet on tarkoitettu henkilöille, joilla on kokemusta Entra ID -palvelun käytöstä.
Katsothan myös [Configuring SSO](<https://support.nepton.com/hc/fi/articles/360002590097>) -osiossa olevat muut artikkelit.
## Entra ID asetukset
1) Nepton SP (Service Provider) metatiedot löytyvät alla olevasta linkistä. Lataa tämä XML tiedosto ja tallenna se tietokoneellesi.
[https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V8_21_Apr_2026_To_20_Apr_2028.xml](<https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V8_21_Apr_2026_To_20_Apr_2028.xml> "https://go.nepton.com/externallogin/metadata/entitydescriptor_sp_go.nepton.com_v8_21_apr_2026_to_20_apr_2028.xml")
2) Kirjaudu Microsoft Entra admin centeriin ylläpitotunnuksillasi.
3) Navigoi Identity, Applications, Enterprise Applications, New application, Create your own application
4) Lisää uusi sovellus "SSO Nepton SAML 2". Valitse "Integrate any other application you don't find in the gallery (Non-gallery)". Paina Create.
5) Navigoi "SSO Nepton SAML 2" -sovellukseen. Valitse Manage, Single-sign-on, ja valitse SAML menettelytapa. Sivulla "Set up Single Sign-On with SAML" valitse "Upload metadata file" ja lataa XML tiedosto jonka teit askeleessa 1. Tarkista asetukset. Paina Save.
6) Kopioi seuraavat arvot notepadiin:
  * App Federation Metadata Url
  * Login URL
  * Microsoft Entra Identifier


7) Navigoi "SSO Nepton SAML 2" -sovellukseen. Valitse Manage, Properties, ja tarkista että "Assignment required" on asetettu arvoon "No". Paina Save.
## Nepton asetukset
8) Kirjaudu Neptoniin ylläpitotunnuksillasi
9) Navigoi Työsuhde, Hallinta, Kertakirjautuminen (SSO)
10) Paina "Add"
  * Hallinta: manuaalinen
  * Verkkopalvelun tunnus (Entity ID): "Microsoft Entra Identifier" arvo jonka kopioit notepadiin askeleessa 6.
  * Kirjautumispalvelun URL: "Login Url" arvo jonka kopioit notepadiin askeleessa 6.
  * Kirjautumispalvelun URL binding: HTTP-POST
  * Varmenteen hajautusalgoritmi: SHA-256
  * Henkilöllisyyden tunnisteen muoto (name id format): unspecified
  * Käytä NameId tunnistetta henkilön tunnistamiseen: Kyllä
  * Henkilön tunnistetieto: Sähköposti


11) Tallenna
12) Katso "App Federation Metadata URL" osoite, jonka kopioit notepadiin askeleessa 6. Avaa tämä osoite. Katso ds:X509Certificate tagien välissä oleva pitkä teksti ja kopioi tämä teksti notepadiin. Lisää puuttuva varmenne (tämä pitkä teksti) Neptoniin ja tallenna varmenne.
