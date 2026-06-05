---
id: 360003751058
title: Project import - Visma L7/LTR
url: https://support.nepton.com/hc/en-gb/articles/360003751058-Project-import-Visma-L7-LTR
locale: en-gb
category: Support
category_id: 360000446658
section: Projects
section_id: 360001075297
section_path:
- Integration
- Projects
labels: []
promoted: false
updated_at: '2024-08-23T08:51:50Z'
edited_at: '2024-03-20T09:58:33Z'
---

# Project import - Visma L7/LTR

Projects can be imported to the service from Visma L7. Import uses REST api provided by Visma.
In Visma L7 projects are in three levels:
  1. Company number
  2. Main number
  3. Sub number


For example
  * 100001 - Yritys Oy  

    * 5432 - Tuotekehitys  

      * 110205 - Ohjelmointi


Importing company number to Nepton is optional and can be defined in settings. More about this below.
Note that if you are migrating from old SFTP-import to new REST-api solution, SFTP-import must be run once before switching the interface so that project identifiers are updated so that they are supported by REST api correctly.
If project already exists in Nepton, its information is updated. If project's (subnumber) state (`orderStatus` -information) value is something else than 8 (completed) or 9 (locked), project end date is set empty so that they are available for event recordings. Project start date is set as empty in the import.
## Configuration
**1\. Configuring basic settings**
Basic settings can be defined in working community settings, **Worktime > Administration > Working community settings > Integrations > Projects >Visma L7 project import**
![](https://support.nepton.com/hc/article_attachments/17494550732957)
At least the following settings must be configured so that projects can be imported from Visma L7 API:
Setting name | Description  
---|---  
API settings > Person used to create projects | Person who is used in running the integration. For example this user will be set as the person who has defined project managers for the project (Note! If you are using old SFTP-implementation, first row defines the person used in that import)  
API settings > Import web service address |  Projects are fetched from two different end points, `/projects/` (GET) ja `/salesorders/` (GET). E.g. if endpoints are as following:
  * https://rajapinnan.verkkotunnus.com/ltrws/REST/L7/projects/
  * https://rajapinnan.verkkotunnus.com/ltrws/REST/L7/salesorders/

Import web service address is set as: https://rajapinnan.verkkotunnus.com/ltrws/REST/L7/  
API settings > Company hash | Identifier for company  
API settings > API token (user token) | Token for authorization  
If you don't know what to set in the following fields:
  * API settings > Import web service address
  * API settings > Company hash
  * API settings > API token


Contact your Visma supporting person.
Other configurations for import:
Setting name | Description  
---|---  
Company code as root project |  If company number found from API is imported as the parent project for main numbers. This also has an effect on how project code is formed. Project code is formed as such:
  * Company number, if company codes are imported as root projects
  * Main number
  * Sub number

Project code examples:
  * Main number without company number: 110205
  * Main number with company number: 100001/110205
  * Sub number without company number: 110205/5432
  * Sub number with company number: 100001/110205/5432

  
Import project types |  Are project types of sub numbers imported to Nepton or not. Types are imported by their name. If project types are not imported, project type is "Projects". Main numbers and company numbers are always imported as "Projects" project type.  
Import project managers | Are project managers imported to Nepton or not. If imported, project managers need to have their Visma-identifier or employee number set.  
Add cost centre into imported project code |  Is the cost centre from Visma L7 added to the code of the imported project. Example of a project that has main number 110205, subnumber 5432 and cost centre 1001 Project code without cost centre (setting is not "Yes"): 110205/5432  
Project code with cost centre (setting is "Yes"): 110205/5432/1001  
API settings > Parent project for imported projects | Is the whole project tree from Visma L7 imported as children of the selected project. If no project is selected, projects are imported to the root level.  
Project import can use multiple Visma REST api sources. Each source requires their own:
  * Import web service address
  * Company hash
  * API token
  * Parent project for imported projects
  * Person used to create projects


When multiple sources are used, it must be checked that company numbers and main numbers are unique between sources. Otherwise one source can overwrite projects imported from another source.
**2\. Configuring person identifiers**
If also project managers need to be set in the import, person identifiers must be set in _Employees > Person's information > Identifiers_ -view. If persons Visma identifier is not set, employee number is used as an identifier.
## Technical functionality of import
### Limitations
  * If company numbers are set to be imported, empty company numbers are not imported. If company number is not imported in this case, its main or sub number are not imported either.
  * Main numbers with empty number are not imported. In this case its sub number is not imported either.
  * Sub numbers with empty number are not imported.


### Authentication
Company hash and API token are send in HTTP headers. Company hash is sent as HTTP header `hash` and API token in HTTP header `token`.
### Scheduling import
Scheduling settings can be found in **Worktime > Administration > Working community settings > Integrations > Scheduling > Integration scheduling**.
Visma L7 schedule can be done on either with minutely (e.g. every 15 minutes, every hour etc.) or daily interval. Select one of the 'Visma L7 project import #{number}' selections from the Integration dropdown. Dropdown shows a selection for each interface source configured for import. This means that a schedule needs to be configured separately for each source, but in this way you can define an individual schedule for each source.
Read more about configuring schedules [here](<https://support.nepton.com/hc/articles/10510800700573>).
### Expected responses
#### /projects/ end point
Response is expected to be in JSON format. For this an HTTP header is sent as `Accept: application/json`.
End point is used only to import main numbers. Sub numbers are imported from /salesorder/ end point.
Level | Field name | Format | Description  
---|---|---|---  
Root | _project_ | List of project information (main numbers) |   
List of project information | _rec_ | integer | Numeric identifier for information. Not used in Nepton.  
List of project information | _mainNumber_ | string | Main number project code  
List of project information | _mainNumberName_ | string | Main number project name  
List of project information | _mainNumbercostCentre_ | string | Main number cost center. Not used.  
List of project information | _mainNumbercostCentreName_ | string | Main number cost center name. Not used.  
List of project information | _mainNumbersalesMan_ | string | Visma identifer / employee number of project manager.  
List of project information | _mainNumbersalesManName_ | string | Project manger name. Not used.  
List of project information | _mainNumberworkQuality_ | string | Not used.  
List of project information | _mainNumberworkQualityName_ | string | Not used.  
List of project information | _subNumber_ | string | Sub number project code. Not used.  
List of project information | _subNumberName_ | string | Sub number project name. Not used.  
List of project information | _subNumberCostCentre_ | string | Sub number cost center. Not used.  
List of project information | _subNumberCostCentreName_ | string | Sub number cost center name. Not used.  
List of project information | _subNumberType_ | string | Sub number type. Not used.  
List of project information | _subNumberTypeName_ | string | Sub number type name. Not used.  
List of project information | _subNumberOrderDate_ | string | Sub number order date. Not used.  
List of project information | _subNumberStatus_ | bit | Sub number status. Not used.  
List of project information | _partyByNumber_ | string | Company number. Imported as project code if company code is imported as root project for main numbers.  
List of project information | _partyByBusinessId_ | string | Company business id. Not used.  
List of project information | _partyByName1_ | string | Company name. Imported as project name if company code is imported as root project for main numbers.  
List of project information | _modifiedTs_ | date | Not used.  
List of project information | _deleted  
_ | bit | Is main number deleted or not (1 = Yes, 0 = No).  
A deleted main number is not imported as a new project.  
**Example response**
[code] 
    {  
      "project": [  
        {  
          "rec": "1",  
          "mainNumber": "000001",  
          "mainNumberName": "Turku",  
          "mainNumbercostCentre": "1000",  
          "mainNumbercostCentreName": "MYYNTI",  
          "mainNumbersalesMan": "5000",  
          "mainNumbersalesManName": "Matti Myyjä",  
          "mainNumberworkQuality": "",  
          "mainNumberworkQualityName": "",  
          "subNumber": "1",  
          "subNumberName": "Projektin aloitustyö",  
          "subNumberCostCentre": "1000",  
          "subNumberCostCentreName": "MYYNTI",  
          "subNumberType": "1001",  
          "subNumberTypeName": "Myyntitilaus",  
          "subNumberOrderDate": "",  
          "partyByNumber": "100027",  
          "partyByBusinessId": "1234567-7",  
          "partyByName1": "Yritys Oy",  
          "deleted": "0"  
        }  
      ]  
    }
[/code]
#### /salesorders/ end point
Response is expected to be in JSON format. For this an HTTP header is sent as `Accept: application/json`.
Level | Field name | Format | Description  
---|---|---|---  
Root | _salesorder_ | List of sales orders (sub numbers) |   
List of sales orders | _rec_ | numero | Numeric identifier for information. Not used in Nepton.  
List of sales orders | _orderNumber_ | string | Main number project code.  
List of sales orders | _subNumber_ | string | Sub number project code.  
List of sales orders | _orderType_ | string | Not used  
List of sales orders | _orderTypeName_ | string | Not used  
List of sales orders | _orderName_ | string | Sub number project name.  
List of sales orders | _currency_ | string | Not used  
List of sales orders | _costCentre_ | string | Subnumber cost centre. Is included in project code if setting "Add cost centre into imported project code" is set to "Yes".  
List of sales orders | _orderDate_ | string | Not used  
List of sales orders | _deliveryDate_ | string | Not used  
List of sales orders | _paymentTerms_ | string | Not used  
List of sales orders | _deliveryTermsCode_ | string | Not used  
List of sales orders | _deliveryTerms_ | string | Not used  
List of sales orders | _deliveryMethodCode_ | string | Not used  
List of sales orders | _deliveryMethod_ | string | Not used  
List of sales orders | _orderStatus_ | char | Sub number status. If status is 8 or 9 or sub number is deleted and project does not have an end date, end date is set as the current date.  
List of sales orders | _mainOrderType_ | string | Not used  
List of sales orders | _mainOrderTypeName_ | string | Not used  
List of sales orders | _mainOrderCostCentre_ | string | Not used  
List of sales orders | _mainOrderCostCentreName_ | string | Not used  
List of sales orders | _party1Rec_ | string | Not used  
List of sales orders | _party1Type_ | string | Not used  
List of sales orders | _party1BusinessId_ | string | Company business id.  
Not used  
List of sales orders | _party1CompanyNumber_ | string | Company number. Imported as project code if company code is imported as root project for main numbers.  
List of sales orders | _party1Name1_ | string | Company name. Imported as project name if company code is imported as root project for main numbers.  
List of sales orders | _party1Name2_ | string | Not used  
List of sales orders | _party1visitAddress_ | string | Not used  
List of sales orders | _party1postalAddress_ | string | Not used  
List of sales orders | _party1postalZip_ | string | Not used  
List of sales orders | _party1postalCity_ | string | Not used  
List of sales orders | _party1countryCode_ | string | Not used  
List of sales orders | _party1countryName_ | string | Not used  
List of sales orders | _party1PersonName_ | string | Not used  
List of sales orders | _party1ContactNumber1_ | string | Not used  
List of sales orders | _party1ContactNumber2_ | string | Not used  
List of sales orders | _party2Rec_ | string | Not used  
List of sales orders | _party2Type_ | string | Not used  
List of sales orders | _party2BusinessId_ | string | Not used  
List of sales orders | _party2CompanyNumber_ | string | Not used  
List of sales orders | _party2Name1_ | string | Not used  
List of sales orders | _party2Name2_ | string | Not used  
List of sales orders | _party2visitAddress_ | string | Not used  
List of sales orders | _party2postalAddress_ | string | Not used  
List of sales orders | _party2postalZip_ | string | Not used  
List of sales orders | _party2postalCity_ | string | Not used  
List of sales orders | _party2countryCode_ | string | Not used  
List of sales orders | _party2countryName_ | string | Not used  
List of sales orders | _party2PersonName_ | string | Not used  
List of sales orders | _party2ContactNumber1_ | string | Not used  
List of sales orders | _party2ContactNumber2_ | string | Not used  
List of sales orders | _subNrStatus_ | string | Not used  
List of sales orders | _projectWorkQuality_ | string | Not used  
List of sales orders | _orderNrCostcentre_ | string | Not used  
List of sales orders | _orderNrCCName_ | string | Not used  
List of sales orders | _orderNrName_ | string | Not used  
List of sales orders | _modifiedTs_ | date | Not used  
List of sales orders | _deleted_ | char |  Is sub number deleted or not (1 = Yes, 0 = No). If status is 8 or 9 or sub number is deleted and project has no end date set, current date is set as project end date.  
**Example response**
[code] 
    {  
      "salesorder": [  
        {  
          "rec": "1",  
          "orderNumber": "000001",  
          "subNumber": "1",  
          "orderType": "1",  
          "orderTypeName": "Myyntitilaus",  
          "orderName": "Projektin aloitustyö",  
          "currency": "EUR",  
          "costCentre": "1000",  
          "orderDate": "",  
          "deliveryDate": "2023-11-23",  
          "paymentTerms": "30 pv netto",  
          "deliveryTermsCode": "",  
          "deliveryTerms": "",  
          "deliveryMethodCode": "",  
          "deliveryMethod": "",  
          "orderStatus": "1",  
          "mainOrderType": "1",  
          "mainOrderTypeName": "Myyntitilaus",  
          "mainOrderCostCentre": "1000",  
          "mainOrderCostCentreName": "MYYNTI",  
          "party1Rec": "1057",  
          "party1Type": "BY",  
          "party1BusinessId": "1234567-7",  
          "party1CompanyNumber": "100027",  
          "party1Name1": "Yritys Oy",  
          "party1Name2": "",  
          "party1visitAddress": "Osoite 1",  
          "party1postalAddress": "",  
          "party1postalZip": "00000",  
          "party1postalCity": "PAIKKAKUNTA",  
          "party1countryCode": "FI",  
          "party1countryName": "Suomi",  
          "party1PersonName": "Antti Asiakas",  
          "party1ContactNumber1": "",  
          "party1ContactNumber2": "",  
          "party2Rec": "1058",  
          "party2Type": "DP",  
          "party2BusinessId": "1234567-7",  
          "party2CompanyNumber": "100027",  
          "party2Name1": "Yritys Oy",  
          "party2Name2": "",  
          "party2visitAddress": "Osoite 1",  
          "party2postalAddress": "",  
          "party2postalZip": "00000",  
          "party2postalCity": "PAIKKAKUNTA",  
          "party2countryCode": "FI",  
          "party2countryName": "Suomi",  
          "party2PersonName": "",  
          "party2ContactNumber1": "",  
          "party2ContactNumber2": "",  
          "subNrStatus": "avoin",  
          "projectWorkQuality": "",  
          "orderNrCostcentre": "1000",  
          "orderNrCCName": "MYYNTI",  
          "orderNrName": "",  
          "modifiedTs": "2023-05-26 12:57:02",  
          "deleted": "0"  
        }  
      ]  
    }
[/code]
## Import from SFTP-server
Note! REST API solution described above is the recommended method for importing projects.
Project information must be formed in text format files to the SFTP-server. Settings can be found in Worktime > Administration > Working community settings > Integrations > Visma. All files from the set SFTP-server are handled, so material can be split into separate files.
File must be saved with ISO-8859-1 character encoding. Fields must be separated with a pipe (`|`). Line break can be in either Windows- (`CR`+`LF`) or UNIX-format (`LF`).
File does not include header row. In the file each L7 main number or L7 sub number is transferred in its own row. File can include both main numbers and sub numbers. Main number must be present in the file before sub number.
Imported projects are formed into the service automatically. If project already exists in Nepton, its information is updated. If project's (subnumber) state (project status -field) value is something else than 8 (completed) or 9 (locked), project end date is set empty so that they are available for event recordings. Project start date is set as empty in the import.
### Scheduling SFTP import
Scheduling settings can be found in **Worktime > Administration > Working community settings > Integrations > Scheduling > Integration scheduling**.
SFTP-import schedule can be done on either with minutely (e.g. every 15 minutes, every hour etc.) or daily interval. Select 'Visma L7 project import (old)' from the Integration dropdown.
Read more about configuring schedules [here](<https://support.nepton.com/hc/articles/10510800700573>).
### Row type main number
Column number | Data contents | Additional information  
---|---|---  
1 | Grandparent project code |  Sets the parent projects parent project when setting parameter ‘First column denotes root project’ is enabled. If project does not exist, then it’s created. Note that if this column is empty, row is skipped.  
2 | Project Code | Code of the project. If code does not exist, then it’s created. If it exists, then it will be updated.  
3 | Project Name | Name of the project. If name is empty, then project code is used.  
4 | Project Status | If project status is 8 or 9 then project end date is set to current day. Other values are ignored.  
### Row type sub number
Column number |  Data contents |  Additional information  
---|---|---  
1 |  Grandparent project code |  Sets the parent projects parent project when setting parameter ‘First column denotes root project’ is enabled. If project does not exist, then it’s created. Note that if this column is empty, row is skipped.  
2 |  Parent Project Code |  Code of the parent project. This code must exist. The project imported will be created as a child of the parent project.  
3 |  Project Code |  Code of the project. If code does not exist, then it’s created. If it exists, then it will be updated.  
4 |  Project Name |  Name of the project. If name is empty, then project code is used.  
5 |  Project manager |  Person number of the project manager. Can be empty.  
6 |  Project Status |  If project status is 8 or 9 then project end date is set to current day. Other values are ignored.  
7 |  Project Type |  Project type. Defaults to Projects. If incorrect type is set project will not be added.
