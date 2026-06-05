---
id: 4404282746641
title: Absences by person report
url: https://support.nepton.com/hc/en-gb/articles/4404282746641-Absences-by-person-report
locale: en-gb
category: Support
category_id: 360000446658
section: Worktime reports
section_id: 360005870318
section_path:
- Reporting
- Worktime reports
labels: []
promoted: false
updated_at: '2025-05-12T10:08:23Z'
edited_at: '2025-05-12T10:08:23Z'
---

# Absences by person report

The "Absences by person" report shows a row for each continuous absence per person. All event types that behave like an absence (absences, annual holidays, accrual leaves) are shown on the report. Public holidays are not shown on the report.
Multiple absence events are shown grouped as a single row (i.e. as a continuous absence) by default, if they are of the same event type and share the same basic information (absence type, sick leave type, compensation type) and there is no work event between the absences. For example, an absence marked as 'Military or civilian service time' for Friday is displayed as one row with the same absence type marked for Monday, because both are 'Military or civilian service time' and both have the same compensation type unpaid/paid, and there are no work events between these absences. If another event had been marked between these absences, they would be displayed as separate rows in the report. Absences can also be shown individually without grouping into a single row. 
## Report options
The report can be run either with the data grouped (default) or without grouping. For example, in a two-week period, sick leave has been marked in the calendar as two separate events, as well as one paid absence:
![](https://support.nepton.com/hc/article_attachments/27305208638493)
**_Report with grouping_ _:_** Sick leave entries, one of which is marked 2.6.- 6.6. and the other 9.6.2022, are grouped on the same line as a continuous absence, because they are absences of the same type, and no other events are marked between them. If there were other events in between, both entries would be on their own rows, because the absence is not continuous.
The duration in working hours and working days shown in the report depend on how much work obligation the person has had during the continuous absence.
![](https://support.nepton.com/hc/article_attachments/27305208641309)
**_Report without grouping_ _:_** A report taken from the same time period with the "no grouping" option selected would look like this:
![](https://support.nepton.com/hc/article_attachments/27305179043869)
Separately marked sick leaves are displayed on their own rows, just like they are entered in the person's calendar. The report only shows the "Duration (calendar days)" column when it is run without grouping.
The report can be printed or downloaded to Excel.
## Column descriptions
  * "Personnel number" - Person's personnel number (if set)
  * "Employee" - Person's name
  * "Person group" - Person's Worktime person group (if set)
  * "Additional reporting info" - Additional reporting information that can be added to the person's details in the Employee tab
  * "Absence type" - Basic information on the nature of absence. Sensitive information like absence type is only shown if the person has permission to see it
  * "Compensation" - Paid, unpaid, or reduced salary as defined in the absence event(s). This is hidden if the person viewing the report does not have permission to see it
  * "Date range" - If grouping is set as `Continuous absences of same type` then it will show date range of the consecutive absence(s) that fulfills the person's work obligation and share the same basic criteria, while when `No grouping` is set then it will show the date range of absence event(s) as it is marked on calendar.
  * "Duration (work hours)" - How many hours of the person's work obligation has the absence fulfilled. e.g. if a person records an unpaid absence from 00:00 -> 24:00, the duration in hours will be 07:30 (or whatever their daily obligation is).
  * "Duration (work days)" - How many days does it fulfill a person's work obligation for.
  * "Duration (calendar days)" - How many calendar days it covers including days with no work obligation days. Column is included in the report if `No grouping` is set.
