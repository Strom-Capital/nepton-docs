---
id: 360005404298
title: Henkilön tuonti - SAP
url: https://support.nepton.com/hc/fi/articles/360005404298-Henkil%C3%B6n-tuonti-SAP
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels: []
promoted: false
updated_at: '2026-06-26T07:06:51Z'
edited_at: '2026-06-26T07:06:51Z'
---

# Henkilön tuonti - SAP

Ei pidä sekoittaa samannimiseen [SAP SuccessFactors](<https://support.nepton.com/hc/fi/articles/360004051897>) -tuontiin. Tämä tuontitapa on erityisesti suunniteltu SAP-lähdejärjestelmälle. Se laajentaa yleisiä tuontisääntöjä erityisellä liiketoimintalogiikalla ja tietojen tunnisteilla.
Tämä tapa on ensisijaisesti tarkoitettu CSV- tai Excel-tiedostomuodolle, joka sisältää otsikkorivin. Se perustuu vahvasti [yleisen](<https://support.nepton.com/hc/fi/articles/360003762577>) kartoituksen lisäkenttien käyttöön.
## Kentät
​Alla on luettelo erityisistä tunnisteista ja kenttien käyttäytymisestä, jotka liittyvät tähän tuontikartoitukseen. Henkilön lisätietokenttiä voidaan tuoda käyttämällä [yleistä](<https://support.nepton.com/hc/fi/articles/360003762577>) tuontitapaa.
**Tunniste** | **Tuontisarakkeen indeksi** | **Vastaava Nepton-kenttä** | **Kuvaus**  
---|---|---|---  
OrganisaatioKoodit | Ei sovellu | WT_UserGroupTreeCodes |   
OrganisaatioNimet | Ei sovellu | WT_UserGroupTreeNames |   
## Liiketoimintalogiikka
Työsopimuksen pituuden pidentäminen:
  * Jos henkilöllä on olemassa oleva työsopimuksen alkamispäivä, tuotu alkamispäivä voi nollata olemassa olevan alkamispäivän arvon, mutta alkamispäivää ei voi muuttaa toiseksi arvoksi.
  * Jos henkilöllä on olemassa oleva työsopimuksen päättymispäivä, tuotu päättymispäivä voi nollata olemassa olevan päättymispäivän arvon tai muuttaa päättymispäivän myöhemmäksi päiväksi, mutta päättymispäivää ei voi muuttaa aikaisemmaksi päiväksi.
  * Nämä rajoitukset varmistavat, että henkilöitä, joilla on useita sopimuspäiviä, voidaan tarkastella ja hallita oikein palvelussa.
