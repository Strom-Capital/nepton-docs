---
id: 360003473418
title: SD Worx absence events
url: https://support.nepton.com/hc/en-gb/articles/360003473418-SD-Worx-absence-events
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
- sdworks
- sdworx
- SD worx
promoted: false
updated_at: '2026-03-11T11:59:15Z'
edited_at: '2025-07-09T04:54:09Z'
---

# SD Worx absence events

SD Worx was previously known as Personec W.
## File format
Integration file is in ISO-8859-1 format and the data is text values separated with a semicolon (;) . File does not contain headers. Field lengths have no limit defined.
## Limitations
  * Employees with personnel number 0 are not included in the integration file


## Fields
**Column** |  **Description** |  **Integration rule field name  
** |  **Format** |  **Notes**  
---|---|---|---|---  
A |  Cost group |  UserCostGroup |  string |  Employees cost group  
B |  Employee identifier |  Set automatically, cannot be overridden in query |  string |  If integration ID is empty, employee number will be used.  
C |  Start date |  StartDateTime |  string |  Row start date. Format DD.MM.YYYY  
D |  End date |  EndDateTime |  string |  Row end date. Format DD.MM.YYYY  
E |  Salary code |  SalaryCode |  string |   
F |  Checklist |  |  string |  Left empty in export  
G |  Amount |  Amount |  decimal |  With accuracy of 2 decimals, , as decimal separator. Unit conversion is automatic  
H |  Custom data 1 | CustomData1 |  |  Can be overridden in the query to add additional data to the export e.g. SELECT *, 123 as OverrideCustomData1  
I |  Custom data 2 | CustomData2 |  |  Same as above  
J |  Custom data 3 |  CustomData3 |  |  Same as above  
#
