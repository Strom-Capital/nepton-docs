---
id: 360005401578
title: Person import - Kieku "Work time rules"
url: https://support.nepton.com/hc/fi/articles/360005401578-Person-import-Kieku-Work-time-rules
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
updated_at: '2023-08-31T07:00:17Z'
edited_at: '2023-08-31T06:59:44Z'
---

# Person import - Kieku "Work time rules"

Tätä artikkelia ei ole vielä käännetty suomeksi.
This import mapping is specifically designed for the Kieku source system and "Work time rules". It extends the general import rules with special business logic and data identifiers. Please also see the [Kieku "New accounts"](<https://support.nepton.com/hc/fi/articles/360005399958>) mapping to ensure you are picking the correct one for your purposes.
This mapping is primarily intended for XML file format and therefore does not have a column order defined. This makes node names mandatory (or column headers if using file types other than XML).
# Fields
Below is a list of the special identifiers and behaviours of fields related to this import mapping. Additional person information fields can be imported using the [general](<https://support.nepton.com/hc/fi/articles/360003762577>) import documentation.
Identifier | Import Column Index | Mapped to Nepton Field | Description  
---|---|---|---  
HenkiloNro | N/A | Employee Number |   
EtuNimi | N/A | Firstname(s) |   
SukuNimi | N/A | Lastname |   
SahkopostiosoiteTeksti | N/A | Email |   
LahiOsoite | N/A | Street Address |   
PostiNro | N/A | Post Code |   
PaikkakuntaKoodi | N/A | City |   
PalvelussuhdeAlkuPvm | N/A | Contract Start Date | Only ever extends the employee’s working contract duration  
PalvelussuhdeLoppuPvm | N/A | Contract End Date | Only ever extends the employee’s working contract duration  
TehtavaKuvausTeksti | N/A | Job Title |   
Organisaatiotaso1Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso2Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso3Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso4Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso5Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso6Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso7Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso8Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso9Koodi | N/A | User Group | See business logic heading  
Organisaatiotaso10Koodi | N/A | User Group | See business logic heading  
# Business logic
  * **Ignore data without '_TyoAikaSuunnitelmaSaantoKoodi_ ' node**   
Each person imported must contain an XML node named TyoAikaSuunnitelmaSaantoKoodi with **case sensitive** value 02 or 03A. Otherwise the data for that person is ignored.
  * **Username = Employee number**   
A username is usually generated based on the first and last names, but for this mapping the employee number is copied.
  * **Person group from OrganisaatiotasoKoodi**   
The person group is only updated by information coming from working contracts which cover the current date (i.e. start date is <= current date and end date > current date) 
    * i.e. Only information related to the working contract which is currently active will affect the person group
    * Although there are up to 10 values imported for the OrganisaatiotasoKoodi. Only the value in the highest field is used to determine the new person group (Where Organisaatiotaso1Koodi is considered the lowest)
  * **Extend working contract length  
** Check the details [here](<https://support.nepton.com/hc/en-gb/articles/13129687045789>)
  * **Email to lower-case**   
All emails are converted to lower-case
  * **Email ignored if Faulty**  
Emails which do not pass Nepton email validation will be silently dropped from the import
