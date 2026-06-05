---
id: 360003473498
title: Mepco Salary data
url: https://support.nepton.com/hc/en-gb/articles/360003473498-Mepco-Salary-data
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
- S365
promoted: false
updated_at: '2025-08-06T07:55:18Z'
edited_at: '2025-08-06T07:55:16Z'
---

# Mepco Salary data

## Configuration
**1\. Configuring person identifiers**
Person's identifiers can be defined by editing persons information in Employees > Person's information > Identifiers - view.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/8611040697245)
If person has no Mepco-identifier set, person's employee number is used.
**2\. Integration settings**
Settings like salary codes and export options for the integration can be configured in Worktime > Administration > Working community settings > Integrations > Accountor Mepco HRM.  
  
Also the date format of the file can be set in general settings:
![mepco-general-settings-en.png](https://support.nepton.com/hc/article_attachments/29392735671453)
For example if the desired date format is DD.MM.YYYY, annetaan asetuksen arvoksi "d.m.Y"
If there is no date format set or it is empty, date format is YYYY-MM-DD
**3\. Creating a ruleset**
Integration can use integration rulesets. Instructions can be found in the article [Setting up integration rulesets](<https://support.nepton.com/hc/en-gb/articles/360002489257>).
## File format
Integration file is in UTF-8 format and the data is a csv file with text values separated with a semicolon (;) . Field lengths can be found in this article's table in Fields - section. Settings for reading and handling the file in Mepco needs to be defined accordingly to these settings.
A semicolon (;) is added after the last row of the file.
In Worktime > Administration > Working community settings > Integrations > Accountor Mepco HRM there is a setting "Include five project levels in salary data". If the setting is on, file will have 5 project levels. If the setting is off, only one project level is included in the file. **"Include five project levels in salary data" - must be set on in new implementations. Including only one project will be deprecated from the service.**
Mepco import can have fields that are defined to be skipped. Using this adding several project levels does not cause the file's column structure to change. These instructions describe the recommended five project level structure. With setting "Split project code into multiple codes by forward slash (/)" a project code can be split to parts with a forward slash. For example if project code 1 is "1234/5678/90", it would be automatically split into project code 1 = "1234", project code 2 = "5678" and project code 3 = "90".
In Worktime > Administration > Working community settings > Integrations > Accountor Mepco HRM there is a setting "Include end of line character on last line of the export file". If the setting is on, the file will include an end of line character at the end of the export file, and will appear as an empty new line in a text editor. Depending on the system to which the file is exported, this setting may need to be enabled.
## Limitations
  * Employees with employee number 0 are not included in the file
  * If project code has no value, e.g. it is NULL, project codes are moved to the left. For example if project code 1 and project code 3 have a value and project code 2 is NULL, project code 3's value will be in the project code 2 field. By setting project code 2 empty as "", project codes will have their columns accordingly.


## Fields
A ruleset configured for the integration will fill the values automatically. If a field needs to have a customised value, the field can be replaced by setting an override for it by having the ruleset pick a value which is named 'Override' combined with the column name. Field names for using override are represented in the table below. For example by having a rule which picks a field with 'AS OverrideSalaryCode', the picked value will automatically replace the SalaryCode field. More information can be found in [Setting up integration rulesets](<https://support.nepton.com/hc/en-gb/articles/360002489257>) \- article.
Column number | Column contents | Field name used in ruleset | Format | Description  
---|---|---|---|---  
1 | Employee integration ID | Set automatically, can not be replaced | string  
nvarchar(max) | Person's Mepco-identifier or employee number if Mepco-identifier is not set  
2 | Employee name | Set automatically, can not be replaced | string  
nvarchar(max) |   
3 | Event begin date | OverrideStartDateTime | date | Date format is according to"Date format" setting. Default format is `YYYY-MM-DD`  
4 | Event end date | OverrideEndDateTime | date | Date format is according to"Date format" setting. Default format is `YYYY-MM-DD`  
5 | Amount | OverrideAmount | decimal | Decimal separated with a dot, two decimals. E.g. 12.50  
6 | Salary code | OverrideSalaryCode | string  
nvarchar(max) | Ruleset rule's salary code  
7 | Project code 1 | OverrideProjectCode1 | string  
nvarchar(255) | Project code 1  
8 | Project code 2 | OverrideProjectCode2 | string  
nvarchar(255) | Project code 2. Note: included when "Include five project levels in salary data" - setting is on.  
9 | Project code 3 | OverrideProjectCode3 | string  
nvarchar(255) | Project code 3. Note: included when "Include five project levels in salary data" - setting is on.  
10 | Project code 4 | OverrideProjectCode4 | string  
nvarchar(255) | Project code 4. Note: included when "Include five project levels in salary data" - setting is on.  
11 | Project code 5 | OverrideProjectCode5 | string  
nvarchar(255) | Project code 5. Note: included when "Include five project levels in salary data" - setting is on.  
12 | Ruleset rule name | Set automatically, can not be replaced | string  
nvarchar(max) | Name of the ruleset rule  
13 | Project IDs | Set automatically, can not be replaced | string  
nvarchar(max) |  List of internal project identifiers separated with a forward slash, e.g: 1234/4342/5343  
14 | Project ID of related project | Set automatically, can not be replaced | integer | Identifier of the first related project (might be required in some ERP-systems)  
15 | Project names | Set automatically, can not be replaced | string  
nvarchar(max) | List of project names separated with a forward slash  
16 | Cost group | OverrideUserCostGroup | string  
nvarchar(max) | Can be replaced by using OverrideUserCostGroup  
17 | Setting group code | Set automatically, can not be replaced | string  
nvarchar(max) | Code of person's setting group  
18 | Custom data 1 | CustomData1 | string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test1' as CustomData1  
19 | Custom data 2 | CustomData2 | string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test2' as CustomData2  
20 | Custom data 3 | CustomData3 | string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test3' as CustomData3  
21 | Custom data 4 | CustomData4 |  string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test4' as CustomData4  
22 | Custom data 5 | CustomData5 |  string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test5' as CustomData5  
23 | Custom data 6 | CustomData6 |  string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test6' as CustomData6  
24 | Custom data 7 | CustomData7 |  string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test7' as CustomData7  
25 | Custom data 8 | CustomData8 |  string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test8' as CustomData8  
26 | Custom data 9 | CustomData9 |  string  
nvarchar(max) | Can be used on adding customised data in the export, e.g. 'test9' as CustomData9  
CustomData4-CustomData9 fields are included in the export file only if they have been added to be selected in the ruleset rule. If even one of CustomData4 - CustomData9 fields is added to be selected in the ruleset, all CustomData4 - CustomData9 columns are included in the file, and the CustomData - fiels that don't have a value are exported as empty fields.
###  Example
Below is an example of a file which has one persons salary items for two days.
[code] 
    72144; Elisa Example;2011-01-03;2011-01-03;4.00;1012;16141;20234;;;;Regular working hours;10437;10437;20234/Packing;200;500;;;
    72144; Elisa Example;2011-01-04;2011-01-04;3.50;1012;16141;20234;;;;Regular working hours;10437;10437;20234/Packing;200;500;;;
    
[/code]
