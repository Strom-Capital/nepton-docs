---
id: 360015754117
title: Importing Personal Data with 'Valid From' Information
url: https://support.nepton.com/hc/en-gb/articles/360015754117-Importing-Personal-Data-with-Valid-From-Information
locale: en-gb
category: Support
category_id: 360000446658
section: Field validities in person imports
section_id: 360004603778
section_path:
- Integration
- HR data
- Field validities in person imports
labels: []
promoted: false
updated_at: '2026-06-26T09:56:55Z'
edited_at: '2026-06-26T09:56:54Z'
---

# Importing Personal Data with 'Valid From' Information

Importing with 'Valid From' information allows you to import future personal data changes in advance. The import brings in the values of personal data fields as well as a row-specific "Valid From" date. 
More information:
[Field validities in person imports](<https://support.nepton.com/hc/articles/360015807338>)  
[Person import](<https://support.nepton.com/hc/articles/360003762577>)  
[Person import fields ](<https://support.nepton.com/hc/articles/360015933397>)  
[Mandatory Personal Data Fields](<https://support.nepton.com/hc/articles/360003762577-Person-Import#h_01F1F00HRZTD78QCZXSP1KE28P>)
## Format of the 'Valid From' Date
The date must be given in the format DDMMYYYY, D.M.YYYY, DD/MM/YYYY, YYYYMMDD or YYYY-MM-DD, i.e. in the order day-month-year or year-month-day. The separator can be a dot (.), dash (-), or slash (/). The year must be given in four digits, the month and day must be given in two digits. When using separators, the day and month can also be given as a single digit. Any possible exceptions to the format are described in system-specific instructions.
For example, 3rd of May 2022:
  * 03052022
  * 3.5.2022
  * 03.05.2022
  * 3/05/2022
  * 2022-05-03
  * 20220503


## Sample Data File
Data can be imported with 'Valid From' information, for example, using [manual import](<https://support.nepton.com/hc/articles/360018767498>) with an Excel document as follows:
Employee Number | First Name | Last Name | Job Title | Valid From  
---|---|---|---|---  
1234 | Esa | Example | Salesperson | 1.1.2019  
1234 | Esa | Example | Sales Manager | 1.1.2021  
## Importing Future Personal Data Changes in Advance
If you want to import future personal data changes in advance, do the following:
  * Add one row per person to the data, with the field values being those valid on the import date
  * Additionally, add one row per future date for the same person, for each date on which any personal data field that supports validity will change
    * Set the "Valid From" information to the date the change comes into effect, without a time
    * Set the values of fields supporting validity to those that will be valid on the change effective date
    * Set the values of fields that do not support validity to the value valid on the import date


## Import Without Future Changes
Importing with 'Valid From' information enables a more reliable import of personal data than [importing personal data without validity](<https://support.nepton.com/hc/articles/360015741097>). If the import data is brought into Nepton late, the import data also contains information on the date the changes in the data were intended to take effect. For this reason, even if future personal data changes are not imported, you can use the benefits of this import method by adding one row per person to the data, with the field values being those valid on the import date, and by adding the import date as the "Valid From" information in the import data.
More information about personal import:
[Person Import](<https://support.nepton.com/hc/articles/360003762577>)
[Person import fields](<https://support.nepton.com/hc/articles/360015933397>)
## Rules for Saving Data
Prerequisites:  
[Person import fields](<https://support.nepton.com/hc/articles/360015933397>)  
[Mandatory Personal Data Fields](<https://support.nepton.com/hc/articles/360003762577-Person-Import#h_01F1F00HRZTD78QCZXSP1KE28P>)
### Fields Supporting Validity
Saving validity differs between fields that support validity and those that do not. The following fields do not support validity: "Primary Supervisor", "Secondary Supervisors", "Worktime Roles", "Units", "Person Group", "Default Project", "Balance", as well as alternative fields that import this information. Other fields support validity.
  * The value valid on the 'Valid From' date as well as any future values will be replaced with the new value, effective from the 'Valid From' date
  * Imported values do not change validity for the period before the "Valid From" date
    * Exception: if a mandatory field that supports validity does not have an existing value, e.g. when adding a new person, the validity is also extended into the past
    * Mandatory additional personal data fields are handled like optional fields, i.e. the imported field receives the given start time.
  * You can import multiple values for the same field with effective dates by adding multiple rows/nodes with different "Valid From" dates to the data
  * If the "Valid From" date information is present in the data but its value is empty, all existing values are replaced with the new value, so that the new value is always valid. If the import data also contains values with a "Valid From" date, these will be imported afterwards.


### Fields Not Supporting Validity
Saving validity differs between fields that support validity and those that do not. The following fields do not support validity: "Primary Supervisor", "Secondary Supervisors", "Worktime Roles", "Units", "Person Group", "Default Project", "Balance", as well as alternative fields that import this information. Other fields support validity.
  * Regardless of the "Valid From" date, the values take effect on the import date
  * If the import data contains multiple rows/nodes for the same person, the value from the row/node with the latest "Valid From" date will remain in effect


NOTE!: If future values are imported, the value for fields that do not support validity must be the value valid at the time of import.
## Examples
### Example: New Person, Import Date 1.1.2020
Import date 1.1.2020, data to be imported:
Employee Number | First Name | Last Name | Job Title | Person Group | Valid From  
---|---|---|---|---|---  
1234 | Esa | Example | Salesperson | Sales | 1.1.2020  
1234 | Esa | Example | HR Specialist | Sales | 1.1.2021  
Result:
Field | Explanation  
---|---  
Employee Number: 1234, from 1.1.2020 | Field supporting validity is imported with the 'Valid From' date.  
First Name *: Esa | Mandatory field supporting validity. The validity of the first value is extended into the past.  
Last Name *: Example | Same as above.  
Job Title: Salesperson, from 1.1.2020; HR Specialist, from 1.1.2021 | Field supporting validity. Values are imported from two different rows with different 'Valid From' dates.  
Person Group: Sales | Field not supporting validity. The value valid on the import date must always be imported for a field that does not support validity.  
### Example: Updating Personal Data, Import Date 16.1.2020
Initial situation:
Employee Number: 1234, from 1.1.2020  
---  
First Name *: Esa  
Last Name *: Example  
Job Title: Salesperson, from 1.1.2020; HR Specialist, from 1.1.2021  
Person Group: Sales  
Import date: 16.1.2020, data to be imported:
Employee Number | First Name | Last Name | Job Title | Person Group | Valid From  
---|---|---|---|---|---  
1234 | Esa | Example | Salesperson | Sales | 16.1.2020  
1234 | Esa | Example | Marketing Director | Sales | 1.8.2020  
Result:
Field | Explanation  
---|---  
Employee Number: 1234, from 1.1.2020 | The value is the same, so it is not updated.  
First Name *: Esa | Same as above.  
Last Name *: Example | Same as above.  
Job Title: Salesperson, from 1.1.2020; Marketing Director, from 1.8.2020 | Field supporting validity. The first value, "Salesperson", does not change values for the past as it is already valid on 16.1. The second new value becomes effective from the 'Valid From' date, replacing other future values.  
Person Group: Sales | Field not supporting validity. The value valid on the import date must always be imported for a field that does not support validity.  
### Example: Updating Personal Data, Import Date 23.1.2020
Initial situation:
Employee Number: 1234, from 1.1.2020  
---  
First Name *: Esa  
Last Name *: Example  
Job Title: Salesperson, from 1.1.2020; Marketing Director, from 1.8.2020  
Person Group: Sales  
Import date: 23.1.2020, data to be imported:
Employee Number | First Name | Last Name | Job Title | Person Group | Valid From  
---|---|---|---|---|---  
1234 | Esa | Example | Software Developer | Product Development |   
1234 | Esa | Example | Test Manager | Product Development | 1.10.2020  
Result:
Field | Explanation  
---|---  
Employee Number: 1234 | The first row without a 'Valid From' date clears the validities. The second value is the same, so it is not updated.  
First Name *: Esa | Same as above.  
Last Name *: Example | Same as above.  
Job Title: Software Developer; Test Manager, from 1.10.2020 | Field supporting validity. The first row sets the row value as always valid. The second new value becomes effective from the 'Valid From' date.  
Person Group: Product Development | Field not supporting validity. The value valid on the import date must always be imported for a field that does not support validity.
