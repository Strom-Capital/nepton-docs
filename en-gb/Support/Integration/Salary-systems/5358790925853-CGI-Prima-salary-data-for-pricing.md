---
id: 5358790925853
title: CGI Prima salary data for pricing
url: https://support.nepton.com/hc/en-gb/articles/5358790925853-CGI-Prima-salary-data-for-pricing
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2022-11-24T08:48:21Z'
---

# CGI Prima salary data for pricing

# File format
Transfer file is a delimited text file in CSV format where the fields are separated with a semicolon (;). Line break is CR+LF. Strings are not enclosed with quotation marks. Character encoding is ISO-8859-1. Header row is not generated in the file but instead data content starts from the first row. Decimal numbers use a dot (.) as decimal separator.
# File fields
Column | Field | Ruleset field name | Format | Description  
---|---|---|---|---  
1 | Social security number or personnel number | OverrideUserIntegrationId | string | By default Finnish social security number. Can be overridden with a ruleset.  
2 | Start date | OverrideStartDate | date | Format dd.mm.yyyy  
3 | End date | OverrideEndDate | date | Format dd.mm.yyyy  
4 | Salary code | OverrideSalaryCode | string | Mandatory, salary code in Prima. Fetched from settings.  
5 | Hours | OverrideAmount | string | Optional, format 5.2, e.g. 4.00, no leading zeros; if a salary type does not use units, empty in file. Can be overridden.  
6 | Multiplier | Multiplier | decimal | Optional, format 5.2, e.g. 4.00, no leading zeros; if a salary type does not use units, empty in file. Can be overridden.  
7 | Price per unit | PricePerUnit | decimal | Optional, e.g. 234.56, no leading zeros. Can be overridden.  
8 | Identifier | EmploymentIdentifier | string | Optional, unique identifier for service period. Can be overridden.  
9 | Account | Account | string | Optional, if transferred, should match Prima accounting, if accounting from service period and/or salary type for pricing can not be used. Can be overriden
