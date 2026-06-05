---
id: 360005399958
title: Person import - Kieku "New accounts"
url: https://support.nepton.com/hc/en-gb/articles/360005399958-Person-import-Kieku-New-accounts
locale: en-gb
category: Support
category_id: 360000446658
section: System specific person imports
section_id: 7976634441629
section_path:
- Integration
- HR data
- System specific person imports
labels:
- Person Import
promoted: false
updated_at: '2025-06-10T11:36:42Z'
edited_at: '2025-06-10T10:10:50Z'
---

# Person import - Kieku "New accounts"

This import mapping is specifically designed for the Kieku source system and "new accounts". It extends the general import rules with special business logic and data identifiers. Please also see the [Kieku "Work time rules"](<https://support.nepton.com/hc/en-gb/articles/360005401578>) mapping to ensure you are picking the correct one for your purposes.
This mapping is primarily intended for XML file format and therefore does not have a column order defined. This makes node names mandatory (or column headers if using file types other than XML).
## Fields
Below is a list of the special identifiers and behaviours of fields related to this import mapping. Additional person information fields can be imported using the [general](<https://support.nepton.com/hc/en-gb/articles/360003762577>) import documentation.
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
## Business logic
  * **Username will be automatically set to be the employee number**  
Since Kieku system doesn't have username information for the person, and a username is mandatory in Nepton, the employee number will be used as the username for newly imported persons. In case the data to be imported contains the username information, that is used instead of employee number.
  * **Only consider data from active working contracts**  
This mapping only includes information from active working contracts 
    * Active contracts are determined by the ‘tyosuhdetilakoodi’ node, under the parent node ‘palvelussuhdetyyppi’. If the value is 3 then the contract is considered active. Otherwise it is considered inactive and skipped
  * **Person group from OrganisaatiotasoKoodi**  
The person group is only updated by information coming from active working contracts which also cover the current date (i.e. start date is <= current date and end date > current date) 
    * i.e. Only information related to the working contract which is currently active will affect the person group
    * Although there are up to 10 values imported for the OrganisaatiotasoKoodi. Only the value in the highest field is used to determine the new person group (Where Organisaatiotaso1Koodi is considered the lowest)
  * **Extend working contract length  
** Check the details [here](<https://support.nepton.com/hc/en-gb/articles/13129687045789>)
  * **Email to lower-case**  
All emails are converted to lower-case
  * **Email ignored if Faulty**  
Emails which do not pass Nepton email validation will be silently skipped and not imported
