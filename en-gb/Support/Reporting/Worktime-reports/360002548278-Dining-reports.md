---
id: 360002548278
title: Dining reports
url: https://support.nepton.com/hc/en-gb/articles/360002548278-Dining-reports
locale: en-gb
category: Support
category_id: 360000446658
section: Worktime reports
section_id: 360005870318
section_path:
- Reporting
- Worktime reports
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2025-05-13T09:00:16Z'
edited_at: '2025-05-13T09:00:00Z'
---

# Dining reports

Dining reporting relates to supplement markings made by employees either using Nepton terminal software in cafeteria mode, or via a browser, to indicate the kind of purchases they have made. Below are details of the various types of reports and the information available within them.
## Dining by person
Report can be used to report lunch supplements that are recorded in dining events. The report shows persons dining events on a daily level by each lunch supplement type. The report can be printed and saved as a spreadsheet file.
![](https://support.nepton.com/hc/article_attachments/25731656210077)
## Dining totals by person
Report displays each persons total amount of lunch supplements grouped by supplement type.
The report can be printed and saved as a spreadsheet file.
![](https://support.nepton.com/hc/article_attachments/25731656214685)
## Dining report for restaurant/cafeteria staff and other third parties
It can be beneficial for third parties, that do not have access to the Nepton service, to still get a report of the supplements which have been recorded, whilst avoiding any other personal or sensitive data.
This is achieved by configuring a recurring scheduled [custom export](<https://support.nepton.com/hc/en-gb/articles/10758741671581>) that emails the report to the third party as a spreadsheet.
  1. Create an integration ruleset with an integration rule that exposes only the data the third party needs. Below is a recommended query which does not include any sensitive employee information:  

[code] SELECT   
         s.startDateTime, s.WorkIncrementName as SupplementName, s.Amount, s.UnitType, e.TerminalId   
         FROM UserSalaryData s   
         INNER JOIN UserEventData e ON s.activityId = e.activityid   
         WHERE s.CompensationType = 'WorkIncrement'   
         and TerminalId IS NOT NULL 
[/code]
  2. In the same ruleset you will need to define which columns to export based on the data you are querying and to include the headers in the file. Below is a recommended example, detailed instructions can be found [here](<https://support.nepton.com/hc/en-gb/articles/10758741671581>).  
![d1.png](https://support.nepton.com/hc/article_attachments/10868083208093)
  3. Finally, a schedule can be created to export the data on a daily basis to the email addresses of the 3rd parties. More information on creating schedules can be found [here](<https://support.nepton.com/hc/articles/10510800700573>).
