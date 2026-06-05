---
id: 360003272618
title: Fivaldi salary export, CSV
url: https://support.nepton.com/hc/en-gb/articles/360003272618-Fivaldi-salary-export-CSV
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-10-05T10:59:08Z'
---

# Fivaldi salary export, CSV

Nepton can be configured to export salary data from recorded events to Visma Fivaldi-system.
## Configuration
**1\. Configuring person identifiers**
Person identifiers can be configured by editing person information in Employees > Person's information > Identifiers view.
![](https://support.nepton.com/hc/article_attachments/13988909138589)
If person does not have Fivaldi identifier set, personnel number is used as an identifier.
**2\. Creating a ruleset**
Integration supports the use of rulesets. Instructions on creating rulesets can be found in [Setting up integration rulesets](<https://support.nepton.com/hc/en-gb/articles/360002489257>).
## File format
Transfer file is text data separated with a semicolon (`;`). If some field contains special characters, it will be surrounded by double quotes (`"`). Line break is `CR` & `LF`. Character encoding is in UTF-8.
Column A will contain the identifier of the export batch (`FivaldiBatchIdentifier`), which has the value in format 'Palkat dd.mm.yy'. Date comes from the first date of the selected period. E.g data is selected from period of 1.1.2022-15.1.2022 and the value for column A will be 'Palkat 01.01.22'.
File contains the following header row:
[code] 
    ERA;PVM;HENKILO;PALKKALAJI;MAARA;SK1;SK2;SK3;SK4;KERROIN;HINTA;KULUTILI;SELITE;PAIVITYSTAPA;LOMA_ALKUPVM;LOMA_LOPPUPVM
[/code]
## Limitations
  * Fivaldi Business ID must be added to Nepton in _Worktime > Administration > Working community settings > Integrations > Visma Fivaldi_.   
  
![](https://support.nepton.com/hc/article_attachments/11466940097309)
  * Persons with employeenumber 0 are not included in the transfer file


## Transfer file columns
Column | Field | Ruleset field name | Format | Description  
---|---|---|---|---  
A | Batch identifier | FivaldiBatchIdentifier | string | Can be overridden in ruleset with field `FivaldiBatchIdentifier`.  
B | Date | SalaryRenderingDate | date | Format: `DD.MM.YYYY`.  
C | Person identifier | OverrideUserIntegrationId | string | Fivaldi identifier or employee number of person. Can be overridden in ruleset with field `OverrideUserIntegrationId`.  
D | Salary code | SalaryCode | string |   
E | Amount | Amount | decimal | Amount in two decimal precision. For example pieces or hours in decimal. Decimal separator is comma (`,`).  
F | Project 1 code | ProjectCode1 | string | Project code 1. Note that if only 1 project is set up with '/' separator it will be split to other project codes.  
G | Project 2 code | ProjectCode2 | string |   
H | Project 3 code | ProjectCode3 | string |   
I | Project 4 code | ProjectCode4 | string |   
J | Multiplier | Multiplier | decimal | Empty by default. Can be overridden in ruleset with field `Multiplier`. Decimal separator is comma (`,`).  
K | Unit price | UnitPrice | decimal | Empty by default. Can be overridden in ruleset with field `UnitPrice`. Decimal separator is comma (`,`).  
L | Expense account | ExpenseAccount | string | Empty by default. Can be overridden in ruleset with field `ExpenseAccount`.  
M | Comment | Comment | string | Description of related event.  
N | Update method | FivaldiUpdateMethod | character | Default value is 1. Can be overridden in ruleset with field `FivaldiUpdateMethod`.  
O | Vacation start date | FivaldiVacationStartDate | date |  Empty by default. Can be overridden in ruleset with field `FivaldiVacationStartDate`. Format: `DD.MM.YYYY`. Information is used in reporting absences to Incomes Register.  
P | Vacation end date | FivaldiVacationEndDate | date |  Empty by default. Can be overridden in ruleset with field `FivaldiVacationEndDate`. Format: `DD.MM.YYYY`. Information is used in reporting absences to Incomes Register.  
### Example
[code] 
    ERA;PVM;HENKILO;PALKKALAJI;MAARA;SK1;SK2;SK3;SK4;KERROIN;HINTA;KULUTILI;SELITE;PAIVITYSTAPA;LOMA_ALKUPVM;LOMA_LOPPUPVM  
    Palkat 01.01.12;08.12.2011;78050;101;3,50;63111;81323;;;;;;"TT Iltavuoro";1;;  
    Palkat 01.01.12;08.12.2011;78050;101;1,00;63111;81323;;;;;;;1;;  
    Palkat 01.01.12;05.12.2011;78055;101;4,00;63111;81333;;;;;;"TT Iltavuoro";1;;  
    Palkat 01.01.12;07.12.2011;78055;200;16,00;63111;81333;;;;;;;1;07.12.2011;08.12.2011
[/code]
