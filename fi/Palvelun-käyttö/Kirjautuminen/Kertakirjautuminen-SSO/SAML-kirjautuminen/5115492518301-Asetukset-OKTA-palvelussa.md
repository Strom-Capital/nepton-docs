---
id: 5115492518301
title: Asetukset OKTA palvelussa
url: https://support.nepton.com/hc/fi/articles/5115492518301-Asetukset-OKTA-palvelussa
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
updated_at: '2026-01-21T12:35:16Z'
edited_at: '2026-01-21T12:35:16Z'
---

# Asetukset OKTA palvelussa

Alla on yksityiskohtaiset tekniset ohjeet asiakkaan OKTA palvelun määrittämiseen SAML-pohjaiselle SSO:lle (Single Sign On) Nepton palvelussa. Nämä ohjeet on tarkoitettu henkilöille, joilla on kokemusta OKTA-palvelun käytöstä.
Katsothan myös [kertakirjautumisen määrittäminen](<https://support.nepton.com/hc/fi/articles/360002590097>) -osiossa olevat muut artikkelit.
Nepton SP (Service Provider) -metatiedot löytyvät täältä:
https://go.nepton.com/ExternalLogin/Metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml
## OKTA asetukset
Luo uusi sovellus nimeltä Nepton
Määritä SAML asetukset
Single sign-on URL: https://go.nepton.com/ExternalLogin/Saml2Consumer.aspx
Audience URI (SP Entity ID): https://go.nepton.com/ExternalLogin/Saml
Name ID format: Transient
Application username: Email
Response: Signed
Assertion Signature: Signed
Signature Algorithm: RSA-SHA256
Assertion Encryption: Unecrypted
Lataa Identity Provider (IdP) varmenne OKTA:sta
Katso ja kopioi kirjautumispalvelun URL OKTA:sta
Katso ja kopioi EntityID arvo OKTA:n metadatasta
## Nepton asetukset
Lisää SSO:n määritykset ja sertifikaatti Neptoniin. Ohjeet löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360002590097>).
