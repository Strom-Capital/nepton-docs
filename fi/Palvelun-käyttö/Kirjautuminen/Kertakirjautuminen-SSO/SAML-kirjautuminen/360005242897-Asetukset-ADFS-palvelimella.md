---
id: 360005242897
title: Asetukset ADFS palvelimella
url: https://support.nepton.com/hc/fi/articles/360005242897-Asetukset-ADFS-palvelimella
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
updated_at: '2025-04-22T05:35:41Z'
edited_at: '2025-04-22T05:35:41Z'
---

# Asetukset ADFS palvelimella

Alla on yksityiskohtaiset tekniset ohjeet asiakkaan ADFS-palvelimen (Active Directory Federation Services) määrittämiseen SAML-pohjaiselle SSO:lle (Single Sign On) Nepton palvelussa. Nämä ohjeet on tarkoitettu henkilöille, joilla on kokemusta ADFS-palvelimen käytöstä.
Katsothan myös [kertakirjautumisen määrittäminen](<https://support.nepton.com/hc/fi/articles/360002590097>) -osiossa olevat muut artikkelit.
Nepton SP (Service Provider) -metatiedot löytyvät täältä:
<https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml>
## Luottavan osapuolen luottamuksen määrittäminen (palveluntarjoaja)
valitse toinen alla olevista kahdesta vaihtoehdosta:
### Tuo tietoja verkossa tai paikallisessa verkossa 
  * Kirjaudu ADFS-palvelimelle ja avaa hallintakonsoli.
  * Napsauta hiiren kakkospainikkeella "Relying Party Trusts" kohdassa "Trust Relationships" > Add Relying Party Trust... > Start
  * Valitse " Import data about the relying party published online or on a local network".
  * Syötä: 
    * <https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml>
  * Next
  * Anna näyttönimi, esim. "go.nepton.com" > Next
  * Ohita monivaiheinen todennus napsauttamalla Next
  * Valitse " Permit all users to access this relying party" (voit muuttaa tätä myöhemmin) > Next
  * Napsauta Next jatkaaksesi
  * Poista valinta " Open the claim rules dialog..” > Close
  * Napsauta hiiren kakkospainikkeella juuri luomaasi uutta luottamusta > Properties
  * Lisäasetukset-välilehti > Valitse haluamasi algoritmi, joka määritetään myös Neptonissa
  * Klikkaa OK


### Syötä tiedot manuaalisesti
  * Kirjaudu ADFS-palvelimelle ja avaa hallintakonsoli.
  * Napsauta hiiren kakkospainikkeella "Relying Party Trusts" kohdassa "Trust Relationships" > Add Relying Party Trust... > Start
  * Valitse " Enter data about the relying party manually" > Next
  * Anna näyttönimi, esim. "go.nepton.com" > Next
  * Napsauta profiilia "AD FS 2 (or 3)" > Next
  * Napsauta Next ohittaaksesi Tokenin salaussertifikaatin
  * Ohita “Configure URL section” napsauttamalla Next
  * Syötä: <https://go.nepton.com/ExternalLogin/Saml> kohtaan ” Relying party trust identifier"
  * Add > Next
  * Ohita monivaiheinen todennus napsauttamalla Next
  * Valitse "Permit all users to access this relying party" (voit muuttaa tätä myöhemmin) > Next
  * Ohita seuraava kohta napsauttamalla Next
  * Poista valinta "Open the claim rules dialog..." > Close
  * Napsauta hiiren kakkospainikkeella juuri luomaasi uutta luottamusta > Properties
  * Monitoring-välilehti
  * Syötä seuraava: 
    * <https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml> kohtaan ”Relying party's metadata URL”
  * Add > Next
  * Valitse "Monitor Relying Party"
  * Valitse "Automatically update relying party"
  * Advanced-välilehti > Valitse oikea algoritmi ja **lähetä hash-algoritmi Neptonille**
  * Endpoints-välilehdellä syötä seuraava > SAML Assertion Consumer POST-sidoksella
  * <https://go.nepton.com/ExternalLogin/Saml2Consumer.aspx>
  * Klikkaa OK


## Varmista, että vaaditut varmenteet on määritetty
  1. Kirjaudu ADFS-palvelimelle ja avaa hallintakonsoli.
  2. Varmista, että sinulla on **VRK Gov. Root CA – G2** ja **VRK CA for Service Providers – G4** sertifikaatit asennettuna Trusted Intermediate & Trusted Root varastoissa. Nämä varmenteet ovat saatavilla osoitteesta https://dvv.fi/fi/ca-certificates
  3. Tuo go.nepton.com sertifikaatti 
     1. Napsauta hiiren kakkospainikkeella Relying Party > Update from Federation Metadata 
        1. Jos tämä ei toimi, tarkista, voitko ADFS-palvelimelta käyttää metatietojen URL-osoitetta. Jos tämä on estetty, sinun on ehkä avattava palomuuri.
     2. Varmista, että varmenteen polku on kelvollinen varmenteen ominaisuuksien "Certificate Path" -välilehdellä.
  4. Vaatimussääntöjen määrittäminen 
     1. Napsauta hiiren kakkospainikkeella juuri luomaasi uutta luottamusta > Edit Claim Rules...
     2. Add Rule > **Send LDAP Attributes as Claims** > Next 
        1. Claim rule name > enter "Get LDAP Attributes"
        2. Attribute store > select Active Directory
        3. LDAP Attribute > Email Addresses
        4. Outgoing Claim Type > Email Address
        5. Finish
     3. Add Rule > **Transform an incoming claim** > Next 
        1. Claim rule name > syötä "Convert Email to Name Id"
        2. Incoming claim type > Email Address
        3. Outgoing claim type > Name ID
        4. Outgoing Name ID format > Transient Identifier
        5. Finish
     4. Apply > OK


## Nouda Token-Signing sertifikaatti
  * Kirjaudu ADFS-palvelimelle ja avaa hallintakonsoli.
  * Selaa kohtaan Service > Certificates > Napsauta hiiren kakkospainikkeella Token-Signing Certificate > View Certificate > Details Tab > Copy to File > Next
  * Klikkaa "No, do not export the private key" > Next
  * Valitse "Base-64-koodattu X.509" > Next
  * Valitse tiedoston tallennuspaikka > Next > Finish
  * Tarvitset varmennetiedoston seuraavassa vaiheessa


## Määritysten teko Neptonissa
  * Lisää SSO:n määritykset ja sertifikaatti Neptoniin. Ohjeet löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360002590097>).
