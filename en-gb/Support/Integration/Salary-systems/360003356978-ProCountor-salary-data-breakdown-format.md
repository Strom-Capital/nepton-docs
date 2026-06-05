---
id: 360003356978
title: ProCountor salary data, breakdown format
url: https://support.nepton.com/hc/en-gb/articles/360003356978-ProCountor-salary-data-breakdown-format
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
edited_at: '2023-06-08T11:09:45Z'
---

# ProCountor salary data, breakdown format

## File format
The integration file is a standard ProCountor file in csv format. The file transfers the interpreted amounts of events.
Row type E, event breakdown row
**Column** |  **Field** |  **Integration query field  
** |  **Type** |  **Notes**  
---|---|---|---|---  
A |  Row type |  Set automatically |  string |  Always with value "E"  
B |  Social security number |  Set automatically |  string |   
C |  Pay grade code |  SalaryCode |  string |  Salary code  
D |  Pay grade name |  ProcountorERowPaygradeName |  string |  Left empty in export. Overridden by ProcountorERowPaygradeName  
E |  Amount |  Amount |  decimal, comma as decimal separator |   
F |  Rate |  ProcounterERowRate |  decimal, comma as decimal separator |  Left empty in export. Overridden by ProcounterERowRate  
G |  Project 1 name |  ProjectName1 |  string |   
H |  Project 1 code |  ProjectCode1 |  string |   
I |  Project 2 name |  ProjectName2 |  string |   
J |  Project 2 code |  ProjectCode2 |  string |   
K |  Project 3 name |  ProjectName3 |  string |   
L |  Project 3 code |  ProjectCode3 |  string |   
M |  Project 4 name |  ProjectName4 |  string |   
N |  Project 4 code |  ProjectCode4 |  string |   
O |  Project 5 name |  ProjectName5 |  string |   
P |  Project 5 code |  ProjectCode5 |  string |   
Q |  Project 6 name |  ProjectName6 |  string |   
R |  Project 6 code |  ProjectCode6 |  string |
