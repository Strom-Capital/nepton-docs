---
id: 360003515217
title: SD Worx salary data
url: https://support.nepton.com/hc/en-gb/articles/360003515217-SD-Worx-salary-data
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels:
- sdworks
- sdworx
- SD worx
promoted: false
updated_at: '2026-06-04T12:09:17Z'
edited_at: '2026-06-04T12:09:17Z'
---

# SD Worx salary data

SD Worx was previously known as Personec W.
## File format
The transfer file is ISO-8859-1 format semicolon (;) separated text data. Material does not contain titles. There is no upper limit for field lengths. The salary data schema file can be downloaded from the service.
## Restrictions
  * Employees with Employee identifier 0 will not be included in the material
  * Empty project codes are replaced as follows. Project codes 1 and 2: the value is not replaced even if their value is NULL. Project codes 3-5: if the value is NULL, then the value is replaced by the value of the next project code. For example, project code3 = NULL, project code4 = 123, and project code5 = NULL, are the values project code3 = 123, project code4 = NULL, and project code5 = NULL.


## Data records
A ruleset configured for the integration will fill the values automatically. If a field needs to have a customised value, some fields can be replaced by setting an override for it by having the ruleset pick a value which is named 'Override' combined with the column name. Field names for using override are represented in the table below. For example by having a rule which picks a field with 'AS OverrideSalaryCode', the picked value will automatically replace the SalaryCode field. The fields that can be overridden are: Salary code, unit type, amount, project codes 1-5, StartDateTime ja EndDateTime. More information can be found in [Setting up integration rulesets](<https://support.nepton.com/hc/en-gb/articles/360002489257>) \- article.
**Column** | **Description** |  **Integration query field**  
| **Format** | **Notes**  
---|---|---|---|---  
A | Employee identifier | Set automatically, cannot be overridden | string | " is used as enclosure for this field. If integration ID is empty, employee number will be used  
B | Salary code | SalaryCode | string |   
C | Start date | StartDateTime | string | Format DD.MM.YYYY  
D | End date | EndDateTime | string | Format DD.MM.YYYY  
E | Amount, hours | "Amount" field if UnitType is 'H' or 'S', otherwise 0 | decimal | Amount of hours with accuracy of 2 decimals. , as decimal separator. This field contains information if field is outputted as hours.  
F | Amount, days | "Amount" field if UnitType is 'J', otherwise 0 | decimal | Amount of days with accuracy of 2 decimals. , as decimal separator. This field contains information if field is outputted as days.  
G | Amount, decimal / units | "Amount" field if UnitType is 'U' or 'D', otherwise 0 | decimal | Amount with accuracy of 2 decimals. , as decimal separator. This field contains information if field is outputted as decimal or units.  
H | Project code 1 | ProjectCode1 | string | " is used as enclosure for this field  
I | Project code 2 | ProjectCode2 | string | " is used as enclosure for this field  
J | Project code 3 | ProjectCode3 | string | " is used as enclosure for this field  
K | Project code 4 | ProjectCode4 | string | " is used as enclosure for this field  
L | Project code 5 | ProjectCode5 | string | " is used as enclosure for this field  
M | Amount, currency | "Amount" field if UnitType='C', otherwise 0 | decimal | Amount of currency with accuracy of 2 decimals. , as decimal separator. This field contains information if field is outputted as currency.
