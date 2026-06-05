---
id: 360004437597
title: Filtering persons in worktime and project reports
url: https://support.nepton.com/hc/en-gb/articles/360004437597-Filtering-persons-in-worktime-and-project-reports
locale: en-gb
category: Support
category_id: 360000446658
section: Reporting in general
section_id: 360005870478
section_path:
- Reporting
- Reporting in general
labels: []
promoted: false
updated_at: '2026-02-03T06:07:06Z'
edited_at: '2025-03-10T13:41:31Z'
---

# Filtering persons in worktime and project reports

In all time work time and project reports, as well as integration data, various user selection options can be used to limit the information contained in the reports.
User selection is made directly from the opening view under **Person selection options**. Additional filters can be applied from the gear icon in the upper right corner. To filter users, the report creator must have at least the rights to view subordinates’ events.
![](https://support.nepton.com/hc/article_attachments/25731153155869)
## Additional search filters
When any of the filters below have been applied, the selection is confirmed by clicking the **Save** button, which updates the user list according to the filter.
![](https://support.nepton.com/hc/article_attachments/25731178258077)
## Load users for period
With the filter, you can search for users whose employment ended before the actual reporting period selection.
**Example:** The person’s employment is set to have ended on 15.1.2025. The actual reporting period is 1.2.2025 - 28.2.2025. If for filter Load users for period also January is chosen, the person will be selectable in the Select person section even though their employment was not active during this period.
## Group by
By default, user selections for reports are made based on **P****erson group**. By changing the filter to**Setting group** , user selections can be made based on work time forms. By changing the filter to **Payment Group** , user selections can be made based on payment groups.
**Example:** Reporting is desired to focus on employees working flexible hours. The selection can then be made based on the setting group(s).
## Filter to supervisor's subordinates
User selections can be limited to subordinates of a specific supervisor.
**Example:** Reporting is desired to focus only on the subordinates of Supervisor A.
## Filter users
**All users:** All possible selectable users will be available for selection. At the administrator level, this practically means all active users. At the supervisor level, it means all subordinates of the supervisor.
**All subordinates** : All subordinates for whom the report creator is the primary or secondary supervisor will be available for selection.
**Primary subordinates:** Only those subordinates for whom the report creator is the primary supervisor will be available for selection.
**Secondary subordinates:** Only those subordinates for whom the report creator is the secondary supervisor will be available for selection.
## Filter by salary type
User selection will include those whose setting group has a salary type defined as **Monthly wage** or **Hourly Wage** (in the setting group’s settings under Work hours -> TES -> Salary type).
**Example:** The Hours by salary type report is intended to focus only on hourly wage employees. The employees belong to a setting group where the salary type is defined. Only those who meet this filter criterion, i.e., hourly wage employees, will be available for selection.
