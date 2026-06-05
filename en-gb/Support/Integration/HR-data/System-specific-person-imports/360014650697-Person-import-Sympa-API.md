---
id: 360014650697
title: Person import - Sympa API
url: https://support.nepton.com/hc/en-gb/articles/360014650697-Person-import-Sympa-API
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
updated_at: '2025-05-20T11:37:15Z'
edited_at: '2025-05-20T11:35:00Z'
---

# Person import - Sympa API

By retrieving person data from Sympa API, personal data can be updated in Nepton several times a day. Sympa API can also be used to import information about future changes to person data in advance.
Additional information: [Person imports with validity start and end information](<https://support.nepton.com/hc/en-gb/articles/360015842238>)
## Introduction
Person data transfer using Sympa API is implemented by defining the rules for extracting data to be exported from Sympa and the schedule of retrieving data to Nepton. Sympa's integration rules are defined by a Sympa expert in a standardized manner. You can use the following instructions to schedule the retrieval of person data.
### Scheduling settings
Use the following options to define a scheduled task. For more information on adding scheduled tasks, click [here](<https://support.nepton.com/hc/en-gb/articles/360002489317>).
  * Character encoding: UTF-8
  * File type: JSON
  * Person import type: Sympa HR Integration API
  * Authentication type: Basic HTTP authentication
  * REST API address: Address provided by Sympa
  * Parameter 1: Username - Name: "username", Value: "SympaltaSaatu_API_KEY"
  * Parameter 2: Password - Name: "password", Value: "SympaltaSaatu_Salainen_Avain"
  * Timing: We recommend once a day between 00:15 and 01:00.


### Limiting the amount of data to be transferred
When defining the integration, it is possible to limit the information to be retrieved. Data limitations are mainly made on the Sympa side when extracting information, but it can be useful, especially during the Nepton implementation project, to limit the content that's to be transferred. This can be used to ensure the correctness of the content to be transferred before the information is transferred in the interface for all employees.
Data import can be limited using the commands found in the REST API address in the scheduling definitions. In the commands where the field name can be defined, any of the interface fields can be used. The following commands are available for use as limitations:
$top  
$skip  
$orderby  
$filter
For example, if you want to return 5 people from the interface, ordered by last name, then the text "/?$orderby=LastName&$top=5" inside the brackets is added to the REST API address command. In this case, the definition for the REST API address would be:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4410127663889)
Below is a description of the use of commands by function:
**Top**  
The query $top=XX will return the first XX matches to the query.  
Example:/?$top=200  
**Skip**  
The query $skip=XX will leave out the first XX matches to the query.  
Example: /?$skip=10  
Example: /?$skip=10&$top=10
**Order by**  
The query $orderby=somealias, someotheralias desc will sort the result set, primarily by the alias “somealias”, ascending, and  
secondarily by the alias “someotheralias”, descending.  
Example: /?$orderby=id  
Example: /?$orderby=id desc  
Example: /?$orderby=surname,age desc
**Filter**  
The following subset of OData filters are supported by the API.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4410144105873)  
Filter examples by field type
  * All the field types can be filtered by null or by text  
api/testinterface?$filter=not (email eq null)  
api/testinterface?$filter=name eq 'no values'
  * Numeric field  
eq =equal, gt=greater than, lt = less than, ge=greater than or equal to, le=less than or equal to  
/?$filter=not (number eq null)  
/?$filter=number ge 0  
decimal number as filter  
/?$filter=number ge 1.14d
  * Dates  
eq =equal, gt=greater than, lt = less than, ge=greater than or equal to, le=less than or equal to  
/?$filter=not (date eq null)  
/?$filter=birthday gt 1980-12-17  
between api/testinterface?$filter=(date gt 2020-02-29) and (date lt 2020-03-02)
  * Timestamps  
Datacard's created and modified timestamps can also be used as filter.  
/?$filter=(modified gt 2015-12-31T23:59:59Z)  
Special case: If you don't specify the time, the timestamp is interpreted as T00:00:00, e.g:  
/?$filter=(created le 2014-01-01)  
comparison is done with timestamp 2014-01-01T00:00:00  
A good idea would be to always specify the time with the as a DateTime attribute.  
Note: Datacard's empty created date is shown "0001-01-01T00:00:00" but empty modified date is shown as "null"
  * Identification field  
Identification field can be used in filter as the "raw" numeric value, not the formatted value  
e.g. /?$filter=sympaID eq '123'  
Using values that are not numbers (e.g. sympaID eq 'a123') will give an error ("message": "Error with SQM query:  
MissingFilterField")


## Fields and field groups
All fields of [general person import](<https://support.nepton.com/hc/en-gb/articles/360015933397>) can be used for person data import. [Additional person data fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>) can also be imported when the field name in the API data matches the field name in Nepton. Field values ​​that support validity periods can be transferred with validity information by transferring them as part of any field group, but we recommend using the field groups mentioned below for these fields. Not all fields currently support saving validity periods, even though they are transferred in field groups with validity information. In this case, only the data valid at the time of import is saved - see the description of each field for more details. Fields that are imported in the API data without validity information are saved [without validity periods](<https://support.nepton.com/hc/en-gb/articles/360015741097>) according to the import rules.
**The fields listed below must be imported as part of a field group** , as they contain data inference.
Note: If the same field group is imported in multiple integrations, only the data from the most recent one will remain valid, all previous rows will be deleted.
**Field** | **Field group** |  **Imported with validity period** | **Description**  
---|---|---|---  
Ammattinimike |  Työsuhde_TAULUKKO |  X |  Job title  
Työaika prosentteina |  Työsuhde_TAULUKKO |  X |  Worktime percentage  
Työsuhteen alkupäivä |  Työsuhde_TAULUKKO |  |  The earliest of the employment start date values ​​is selected, which is saved if the existing value is a later date or empty.  
Työsuhteen päättymispäivä |  Työsuhde_TAULUKKO |  |  The latest employment end date values ​​are imported based on the validity periods. If there are multiple latest employment end date values, the latest end date value is selected.  
Työajan asetusryhmä |  Asetusryhmä_TAULUKKO |  X |  [Additional info](<https://support.nepton.com/hc/en-gb/articles/360015933397>)  
Toissijaiset esimiehet |  Toissijaiset_esimiehet_TAULUKKO |  |  Multiple secondary supervisors can be imported, one per field group row, with the secondary supervisor's employee number and validity information. See the example below in the standardized integration data example. Only valid supervisor information is saved.  
Oletuskustannuspaikka |  Kustannuspaikka_TAULUKKO |  X |  Default cost group  
Organisaatiotaso1Koodi -  Organisaatiotaso10Koodi |  Organisaatio_TAULUKKO |  |  These ten fields tell which person group the person belongs to. The fields also describe the person group hierarchy. Level one contains the root nodes of the hierarchy, from which the higher levels tell their child nodes. In addition to these codes, the import must include the names of the person groups corresponding to the codes. See Organization Level1Name - Organization Level10Name. If the person groups according to the hierarchy do not yet exist, these will be created during the import. Only valid organizational information will be saved.  
Organisaatiotaso1Nimi -  Organisaatiotaso10Nimi |  Organisaatio_TAULUKKO |  |  These ten fields tell which person group the person belongs to. The fields also describe the person group hierarchy. Level one contains the root nodes of the hierarchy, from which the higher levels tell their child nodes. In addition to these names, the import must include the person group codes corresponding to the names. See Organization level 1Code - Organization level 10Code. If person groups according to the hierarchy do not yet exist, these will be created during the import. Only valid organizational information will be saved.  
In addition to these field groups, additional information tables can be used. There are 10 of these tables and their name is Lisatieto{1}_TAULUKKO, where the curly brackets replace the table that is being filled in. Any information can be added to these tables, the validity of which is common to all the information added to the table. For example, a person's monthly salary could be included in a message by adding the table there
"Lisatieto1_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Kuukausipalkka": "2700"  
}  
],
If the monthly salary and job title in Sympa's data shared the same validity period, the table would look like this:
"Lisatieto1_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Kuukausipalkka": "2700",   
"Ammattinimike": "Hitsaaja"  
}  
],
### Validity period date format
The "Valid from" and "Valid to" fields use the date format "YYYY-MM-DD".
## Standardized integration
For the standardized Sympa API integration, standard data is transferred. Below are the fields of the standardized integration transfer data.
**Field** | **Field group** |  **Imported with validity period** | **Description**  
---|---|---|---  
Henkilönumero |  |  |  Employee number. Serves as a person identifier between Sympa and Nepton.  
Sukunimi |  |  |  Last name.  
Kutsumanimi |  |  |  First name by which the person is called. Required field used when creating a username (Kutsumanimi Sukunimi).  
Etunimet |  |  |  The person's first names. Not currently stored in Nepton, but the "Kutsumanimi" field serves as the first name instead.  
Sähköposti |  |  |  email  
Puhelinnumero |  |  |  phone number  
Ensisijainen esimies |  |  |  Employee number of primary supervisor.  
IBAN |  |  |  IBAN  
Katuosoite |  |  |  Street Address  
Postinumero |  |  |  Postal code  
Postitoimipaikka |  |  |  Town  
RFID-tunniste |  |  |  RFID identifier  
Yksiköt |  |  |  [Units. Additional info.](<https://support.nepton.com/hc/articles/360015933397>)  
Rooli |  |  |  Role. Only for new people, the empty role value is set to "Employee" in Nepton. If an existing person is imported from Sympa with an empty role value, Nepton will not change the person's role. Importing role information with an empty value is not recommended, as importing a role with an empty value will cause a warning in the person import results.  
Työajan roolit |  |  |  Work time roles  
Käyttäjätili käytössä |  |  |  User account active  
Ammattinimike |  Työsuhde_TAULUKKO |  X |  Job title  
Työaika prosentteina |  Työsuhde_TAULUKKO |  X |  Worktime percentage  
Työsuhteen alkupäivä |  Työsuhde_TAULUKKO |  |  The earliest employment start date value is selected, which is saved if the existing value in Nepton is a later date or empty. If even one empty value is imported, any existing employment start date in Nepton will be cleared.  
Työsuhteen päättymispäivä |  Työsuhde_TAULUKKO |  |  The latest employment end date values ​​are imported based on the validity periods. If there are multiple latest employment end date values, the latest end date value is selected.  
Työajan asetusryhmä |  Asetusryhmä_TAULUKKO |  X |  Setting group  
Toissijaiset esimiehet |  Toissijaiset_esimiehet_TAULUKKO |  |  Multiple secondary supervisors can be imported, one per field group row, with the secondary supervisor's employee number and validity information. See the example below in the standardized integration data example. Only valid supervisor information is saved.  
Oletuskustannuspaikka |  Kustannuspaikka_TAULUKKO |  X |   
Organisaatiotaso1Koodi -  Organisaatiotaso10Koodi |  Organisaatio_TAULUKKO |  |  These ten fields tell which person group the person belongs to. The fields also describe the person group hierarchy. Level one contains the root nodes of the hierarchy, from which the higher levels tell their child nodes. In addition to these codes, the import must include the names of the person groups corresponding to the codes. See Organization Level1Name - Organization Level10Name. Only valid organization information is saved.  
Organisaatiotaso1Nimi -  Organisaatiotaso10Nimi |  Organisaatio_TAULUKKO |  |  These ten fields tell which person group the person belongs to. The fields also describe the person group hierarchy. At level one, the root nodes of the hierarchy are found, from which the higher levels tell their child nodes. In addition to these names, the import must include the person group codes corresponding to the names. See Organization level 1 Code - Organization level 10 Code. Only valid organization data is saved.  
Toimipiste |  Organisaatio_TAULUKKO |  |  Location. This field is not currently stored in Neptun. This field indicates the person's main place of work.  
_FilterLiiketoimintayksikko |  |  |  The field is not stored in Nepton. The field is used on Sympa's side to extract information during the submission phase.  
_TESTUSER |  |  |  The field is not stored in Nepton. The field is used on Sympa's side to extract information during the submission phase.  
Muut tässä mainitsemattomat kentät |  |  |  The standardized integration transfer data also contains other fields, such as field group-specific "id" and "Modification date" information, but these are not essential for the imported data, but rather help in investigating possible special situations.  
### Standardized integration data example
{  
"@odata.context": "<https://api.az-sympa.com/api/$metadata#NeptonKaikkiTiedot>",  
"value": [  
{  
"Henkilönumero": "123",  
"Kutsumanimi": "Erkki",  
"Etunimet": "Erkki Esko Eemeli",  
"Sähköposti": "maili@maili.com",  
"Puhelinnumero": "040 456 7890",  
"Ensisijainen esimies": "Esimerkki",  
"IBAN": "FI0453260051234567",  
"Katuosoite": "Katu 1",  
"Postinumero": "00000",  
"Postitoimipaikka": "Turku",  
"RFID-tunniste": "ABCDE123456",  
"Yksiköt": "Tuotekehitys",  
"Rooli": "Työntekijä",  
"Työajan roolit": "Työntekijät",  
"Käyttäjätili käytössä": "Kyllä",  
"_FilterLiiketoimintayksikko": "3",  
"_TESTUSER": false,  
"Työsuhde_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": "2020-10-13",  
"Ammattinimike": "Testaaja",  
"Työaika prosentteina": 80.0,  
"Työajan asetusryhmä": "1234"  
},  
{  
"Voimassa alkaen": "2020-10-14",  
"Voimassa päättyen": null,  
"Ammattinimike": "Ohjelmistokehittäjä",  
"Työaika prosentteina": 100.0,  
"Työajan asetusryhmä": "2456"  
}  
],  
"Kustannuspaikka_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Oletuskustannuspaikka": "103"  
"Toimipiste": "Kamppi"  
}  
],  
"Organisaatio_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Organisaatiotaso1Nimi": "Ohjelmistotalo Oy",  
"Organisaatiotaso2Nimi": "Turku",  
"Organisaatiotaso3Nimi": "Tuotekehitys",  
"Organisaatiotaso1Koodi": "10",  
"Organisaatiotaso2Koodi": "120",  
"Organisaatiotaso3Koodi": "1500"  
}  
],  
"Toissijaiset_esimiehet_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-09-15",  
"Voimassa päättyen": "2022-01-01",  
"Toissijaiset esimiehet": "1234"  
},  
{  
"Voimassa alkaen": "2016-01-01",  
"Voimassa päättyen": null,  
"Toissijaiset esimiehet": "4321"  
}  
],  
"Asetusryhmä_TAULUKKO": [  
{  
"Voimassa alkaen": "2020-06-02",  
"Voimassa päättyen": null,  
"Työajan asetusryhmä": "Liukuva työaika"  
}  
] }  
]  
}
## Importing field values ​​without validity
If the data being transferred does not specify validity periods, the imported data will be processed [without validity periods](<https://support.nepton.com/hc/en-gb/articles/360015741097>). Below is an example of a data without importing validity information.
{  
"@odata.context": "<https://api.az-sympa.com/api/$metadata#NeptonKaikkiTiedot>",  
"value": [  
{  
"Henkilönumero": "123",  
"Käyttäjätunnus": "[esko.esimerkki@yritys.fi](<mailto:esko.esimerkki@yritys.fi>)",  
"Sukunimi": "Esimerkki",  
"Etunimi": "Esko",  
"Sähköposti": "[esko.esimerkki@yritys.fi](<mailto:esko.esimerkki@yritys.fi>)",  
"Ensisijainen esimies": "21",  
"Käyttäjätili käytössä": "Kyllä"  
}  
]  
}
## Importing field values ​​with validity
Sympa API person import supports importing validity periods to some of the fields. When a field that supports validity periods is imported as a field group field, validity periods can be defined for it in the field group data.
When importing data, the fields are given validity according to the 'Valid from' and 'Valid to' fields of the field group. See more information about transferring validity information [here](<https://support.nepton.com/hc/en-gb/articles/360015842238>). Validity intervals are imported as rows of field groups. Field group fields can also be imported without validity information if desired. If a field group is transferred empty without a single row, all values ​​of all fields in the field group will be deleted from Nepton. Below is a data example of a transfer with validity information using a field group.
{  
"@odata.context": "<https://api.az-sympa.com/api/$metadata#NeptonKaikkiTiedot>",  
"value": [  
{  
"Henkilönumero": "123",  
"Sukunimi": "Esimerkki",  
"Etunimi": "Esko",  
"**Työsuhde_TAULUKKO** ": [  
{  
"**Voimassa alkaen** ": "2020-06-02",  
"**Voimassa päättyen** ": "2020-10-13",  
"Ammattinimike": "Myyjä",  
"Työaika prosentteina": 80.0,  
"Työajan asetusryhmä": "1234"  
},  
{  
"Voimassa alkaen": "2020-10-14",  
"Voimassa päättyen": null,  
"Ammattinimike": "Myyntipäällikkö",  
"Työaika prosentteina": 100.0,  
"Työajan asetusryhmä": "2456"  
}  
]  
}  
]  
}
## Additional information about integration
Nepton retrieves person data by calling the Sympa API. Sympa returns person data in JSON format, following the [OData Version 4 standard](<https://www.odata.org/getting-started/basic-tutorial/>) for content structure. The content and search limits of data extraction are defined in the Sympa user interface.
