---
id: 360003355918
title: Populus salary export, CSV
url: https://support.nepton.com/hc/en-gb/articles/360003355918-Populus-salary-export-CSV
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
updated_at: '2025-06-12T07:50:20Z'
edited_at: '2025-06-12T07:50:20Z'
---

# Populus salary export, CSV

## File format
  * Transfer file is text data separated with a semicolon. Line break is line feed (`LF`). Character encoding is UTF-8. File does not have a header row.


## Limitations
  * Persons with employeenumber 0 are not included in the transfer file.
  * Works only with integration rulesets.
  * If integration ruleset rule picks any of columns N - Y (CustomData1 - 12), all of these columns are included in the file, and custom data not defined in the rule will have an empty value. If none of CustomData columns N - Y are used in the rule, only columns up to M are included in the export file. 


### Transfer file columns
Column | Description | Integration query field | Format | Notes  
---|---|---|---|---  
A | Personnel number | Set automatically, cannot be overridden | number | Maximum length: 6 characters  
B | Ps-ID | PopulusPsId | number | Maximum length: 8 characters. Populated from `PopulusPsId`  
C | Salary type | SalaryCode | number | Salary code, for example "1000". Maximum length: 4 characters.  
D | Start date | StartDateTime (format conversion handled automatically) | date | Format: `YYYYMMDD`. Row start date  
E | End date |  EndDateTime (format conversion handled automatically) | date | Format: `YYYYMMDD`. Row end date  
F | Amount | Amount | decimal | Comma `,` acts as decimal separator, accuracy 2 decimals. Maximum length: 8 characters  
G | Unit price | UnitPrice | decimal | Period `.` acts as decimal separator, accuracy 2 decimals. Populated from `UnitPrice`. Maximum length: 8 characters  
H | Total price | TotalPrice | decimal | Period `.` acts as decimal separator, accuracy 2 decimals. Populated from `TotalPrice`. Maximum length: 8 characters  
I | Account | PopulusAccount | string | Populated from `PopulusAccount`. Maximum length: 8 characters  
J | Cost centre | UserCostGroup | string | Populated from user cost group. Maximum length: 10 characters  
K | Order | PopulusOrder | number | Populated from `PopulusOrder`. Maximum length: 12 characters  
L | VAT | PopulusVat | string | Populated from `PopulusVat`. Maximum length: 2 characters  
M | Additional identifier | PopulusAdditionalIdentifier | string | Populated from `PopulusAdditionalIdentifier`. Maximum length: 15 characters  
N | Custom data 1 | CustomData1 | string | Can be used for adding customized data in the export, e.g. 'test1' as CustomData1  
O | Custom data 2 | CustomData2 | string | Can be used for adding customized data in the export, e.g. 'test2' as CustomData2  
P | Custom data 3 | CustomData3 | string | Can be used for adding customized data in the export, e.g. 'test3' as CustomData3  
Q | Custom data 4 | CustomData4 | string | Can be used for adding customized data in the export, e.g. 'test4' as CustomData4  
R | Custom data 5 | CustomData5 | string | Can be used for adding customized data in the export, e.g. 'test5' as CustomData5  
S | Custom data 6 | CustomData6 | string | Can be used for adding customized data in the export, e.g. 'test6' as CustomData6  
T | Custom data 7 | CustomData7 | string | Can be used for adding customized data in the export, e.g. 'test7' as CustomData7  
U | Custom data 8 | CustomData8 | string | Can be used for adding customized data in the export, e.g. 'test8' as CustomData8  
V | Custom data 9 | CustomData9 | string | Can be used for adding customized data in the export, e.g. 'test9' as CustomData9  
W | Custom data 10 | CustomData10 | string | Can be used for adding customized data in the export, e.g. 'test10' as CustomData10  
X | Custom data 11 | CustomData11 | string | Can be used for adding customized data in the export, e.g. 'test11' as CustomData11  
Y | Custom data 12 | CustomData12 | string | Can be used for adding customized data in the export, e.g. 'test12' as CustomData12
