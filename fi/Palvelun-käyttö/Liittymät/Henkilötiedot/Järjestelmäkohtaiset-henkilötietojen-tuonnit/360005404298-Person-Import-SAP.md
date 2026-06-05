---
id: 360005404298
title: Person Import - SAP
url: https://support.nepton.com/hc/fi/articles/360005404298-Person-Import-SAP
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
updated_at: '2025-08-06T09:37:40Z'
edited_at: '2023-09-14T12:18:23Z'
---

# Person Import - SAP

Tätä artikkelia ei ole vielä käännetty suomeksi.
Not to be confused with the similarly named [SAP SuccessFactors](<https://support.nepton.com/hc/fi/articles/360004051897>) mapping. This import mapping is specifically designed for the SAP source system. It extends the general import rules with special business logic and data identifiers.
This mapping is primarily intended for CSV or Excel file format that includes a header row. It heavily relies upon use of additional fields from the [general](<https://support.nepton.com/hc/fi/articles/360003762577>) mapping.
# Fields
​Below is a list of the special identifiers and behaviours of fields related to this import mapping. Additional person information fields can be imported using the [general](<https://support.nepton.com/hc/fi/articles/360003762577>) import documentation.
Identifier | Import Column Index | Mapped to Nepton Field | Description  
---|---|---|---  
OrganisaatioKoodit | N/A | WT_UserGroupTreeCodes |   
OrganisaatioNimet | N/A | WT_UserGroupTreeNames |   
# Business logic
  * **Extend working contract length  
**
    * If a person has an existing working contract start date, imported start date can zero out the existing start date value, but start date value can't be changed to another value
    * If a person has an existing working contract end date, imported end date can zero out the the existing end date value, or change the end date value to later date, but end date value can't be changed to earlier date
    * These limitations ensure persons who have multiple contract dates can be viewed and managed properly in the service
    * At a later date, full support for multiple contracts per person will be added
