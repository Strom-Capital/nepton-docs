---
id: 360005401578
title: Person import - Kieku "Work time rules"
url: https://support.nepton.com/hc/en-gb/articles/360005401578-Person-import-Kieku-Work-time-rules
locale: en-gb
category: Support
category_id: 360000446658
section: System specific person imports
section_id: 7976634441629
section_path:
- Integration
- HR data
- System specific person imports
labels: []
promoted: false
updated_at: '2026-06-26T06:36:51Z'
edited_at: '2021-05-05T08:57:14Z'
---

# Person import - Kieku "Work time rules"

This import mapping is specifically designed for the Kieku source system and "Work time rules". It extends the general import rules with special business logic and data identifiers. Please also see the [Kieku "New accounts"](<https://support.nepton.com/hc/en-gb/articles/360005399958>) mapping to ensure you are picking the correct one for your purposes.  
This mapping is primarily intended for XML file format and therefore does not have a column order defined. This makes node names mandatory (or column headers if using file types other than XML).
# Fields
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
**
    * If a person has an existing working contract start date, imported start date can zero out the existing start date value, or change the start date value to an earlier date, but start date value can't be changed to later date
    * If a person has an existing working contract end date, imported end date can zero out the the existing end date value, or change the end date value to later date, but end date value can't be changed to earlier date
    * These limitations ensure persons who have multiple contract dates can be viewed and managed properly in the service
    * At a later date, full support for multiple contracts per person will be added
    * Examples: 
        1. No existing working contract dates  
imported values  
PalvelussuhdeAlkuPvm: 20210501  
PalvelussuhdeLoppuPvm 20220831  
result: 01.05.2021 - 31.08.2022 (new dates can be added when there are no existing dates are 
        2. Existing working contract dates 01.05.2021 - 31.08.2022  
imported values  
PalvelussuhdeAlkuPvm: 20210101  
PalvelussuhdeLoppuPvm: 20211231  
Result: 01.01.2021 - 31.08.2022 (start date can be changed to an earlier value but end date cannot)
        3. Existing working contract dates 01.01.2021 - 31.08.2022  
imported values  
PalvelussuhdeAlkuPvm: 20220101  
PalvelusuhdeLoppuPvm: 20221231  
Result: 01.01.2021 - 31.12.2022 (end date can be extended to a later value but start date cannot)
        4. Existing working contract dates 01.01.2021 - 31.12.2022  
imported values  
PalvelussuhdeAlkuPvm:  
PalvelussuhdeLoppuPvm:  
Result: no working contract start or end dates (working contract start date and end date can always be cleared)
  * **Email to lower-case**   
All emails are converted to lower-case
  * **Email ignored if Faulty**  
Emails which do not pass Nepton email validation will be silently dropped from the import
