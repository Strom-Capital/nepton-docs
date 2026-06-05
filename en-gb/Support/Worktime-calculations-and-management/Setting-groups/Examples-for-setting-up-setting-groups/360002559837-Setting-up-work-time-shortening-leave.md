---
id: 360002559837
title: Setting up work time shortening leave
url: https://support.nepton.com/hc/en-gb/articles/360002559837-Setting-up-work-time-shortening-leave
locale: en-gb
category: Support
category_id: 360000446658
section: Examples for setting up setting groups
section_id: 360001483898
section_path:
- Worktime calculations and management
- Setting groups
- Examples for setting up setting groups
labels:
- työajanlyhennys
- työajan lyhennys
- työajanlyhennysvapaa
- pekkanen
- pekkaset
- lisävapaapäivä
- työlyhennysvapaa
- tasaamispäivä
promoted: false
updated_at: '2025-06-05T11:05:32Z'
edited_at: '2025-06-05T11:05:32Z'
---

# Setting up work time shortening leave

## About work time shortening leave
It is possible to set up work time shortening leave calculations to the service. Usually work time shortening leave is earned if the regular working hours under the collective agreement are the same as the regular working hours under the Working Hours Act, eight hours a day or 40 hours a week. Work time shortening leave settings and it's use are described in the guidance below.
## Work time shortening leave settings
Service counts work time shortening leave to be earned from those event types that are set to accumulate it. Work time shortening leave is earned by the regular hours calculated from the event.
It is possible to define in the settings the event types that are counted to earn work time shortening leave. If the event type has not set otherwise, the work time shortening leave is earned from every event except:
  * Absence (Unpaid)
  * Sick leave (Unpaid)
  * Annual leave
  * Balance leave
  * Work time shortening leave
  * Annual absence


Work time shortening leave settings can be set at either the Work Community level or the Settings groups level. If the basis for earning the work time shortening leave is generally the same for all employees of the company, the basis for earning it is easiest to define in the Work Community level settings, in which case they also apply to all setting groups.
**Administration - > Working community settings -> Work hours -> Accruals and overtime hours -> Calculation Settings -> Work time shortening leave  
**
or
**Administration - > Settings groups -> Settings group menu: Desired settings group -> Action menu: Settings group settings -> Work hours -> Accruals and overtime hours -> Calculation Settings -> Work time shortening leave  
**
Accrual is set in use on Work time shortening leave: Setting on. The calculation starts from the day the service is activated, unless the Valid from date is set via the [validity control](<https://support.nepton.com/hc/en-gb/articles/360002559358>). For an individual, the count starts from the person's first posting when the service is in use. The count resets at the beginning of each calendar year.
![WSL_01.png](https://support.nepton.com/hc/article_attachments/4423355106717)
The earning period can be defined as either a year or a month. If the earning period is one year, earning work time shortening leave will be earned during the calendar year according to the earnings table. If the earning period is a month, earnings are made for each calendar month according to the earnings table. If the value of the setting is not set, the earning period is one year.
The earnings criterion can be defined as either hours, days or months, the default is hours.
If the earnings basis is in months, the number of working days or hours worked in the calculation of the annual leave period is used to see whether the working month earns work time shortening leave.
If the earnings basis is in hours, earning threshold can be set with precision in minutes.
![WSL_02.png](https://support.nepton.com/hc/article_attachments/4423340422557)
Read more about the setting up of earning annual leave [here](<https://support.nepton.com/hc/en-gb/articles/360002560698>).
Note! The earning criterion cannot be used in months if the earning period is one month. If this is set, no work time shortening leave will be earned at all.
Under Earn, select whether to earn free hours or days, in the example image below, both are set to days.
If earning needs to be done according to employees' work time percentage, "Earn with work time percentage" needs to set to Yes. If for example employees would earn 8 hours of work time shortening leave after 17 days, with 50% work time percentage, the earned amount would be 4 hours.
If earning should be according to a specific percentage, which is different than work time percentage, you can set the specific percentage in "Earn percentage".
In the section Earn if the duration of employment exceeds, you can specify the minimum duration of employment for earning work time shortening leave. This is only available if the start date of the employment is specified in the Employees section.
Under Earned from the beginning of the employment, it can be specified that the work time shortening leave to be earned from the beginning of the employment when the employment has lasted for the number of months specified in the "Earn if the duration of the employment exceeds" section. If the value is "No" or the value is not set, the earning of work time shortening leave will not start until the employment has lasted for the specified number of months.
Under Earned only from regular time, it can be specified if work time shortening leave is earned only from worked regular time, excluding overtime.
Under Earn from time borrowed from accrual, it can be specified if work time shortening leave is earned by time borrowed from accrual, e.g. time borrowed from balance.
![](https://support.nepton.com/hc/article_attachments/27916367838877)
In the Event Type (Paid) and Event Type (Unpaid) sections, you can specify, depending on the type of event, whether the events earn work time shortening leave. By default, paid leave types other than those listed are earned as part-time leave. By default, the event types listed in the Event Type (Unpaid) section do not earn work time shortening leave unless the setting is turned on separately.
![](https://support.nepton.com/hc/article_attachments/21807122701213)
## Work time shortening leave earning and usage
Service counts work time shortening leave automatically based on the defined settings. When work time shortening leave earning treshold is reached, for example certain amount of time worked, then work time shortening leave accrual gets increased on that day.
Work time shortening leaves are used by using event type 'work time shortening leave'. This event type automatically reduces the work time shortening leave accrual.
If work time shortening leave is earned in days, and it is needed to have half a day of leave, work time shortening leave is marked with duration of half of the persons work day length. Service rounds the spent work time shortening leave to half days based on its duration. For example if work day length is 8 hours and 3,5 hours of work time shortening leave is recorded, this will be rounded so that 0,5 days of work time shortening leave is spent.
If work time shortening leave is needed to be held for half days over the duration of one day, the half day must be recorded as its own event. For example if a person wants to have 1,5 days of work time shortening leave, they should record one work time shortening leave with the duration of working day and one work time shortening leave with the duration of half their working day.
## Reporting Work time shortening leave
Accrued work time shortening leaves and used work time shortening leaves can be monitored with the report Work time shortening leaves, which shows the accrued and used work time shortening leaves in the selected year and the previous year. More detailed information on the report on Work time shortening leaves can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002548777>).
