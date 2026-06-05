---
id: 14849123960989
title: Defining levelling period for part-timers
url: https://support.nepton.com/hc/en-gb/articles/14849123960989-Defining-levelling-period-for-part-timers
locale: en-gb
category: Support
category_id: 360000446658
section: Leveling period
section_id: 4410638658833
section_path:
- Worktime calculations and management
- Setting groups
- Examples for setting up setting groups
- Leveling period
labels: []
promoted: false
updated_at: '2024-08-23T08:51:51Z'
edited_at: '2024-03-04T13:03:33Z'
---

# Defining levelling period for part-timers

Levelling periods can be configured to consider the worktime percentage of part-time employees. This scales the additional work-earning threshold according to the set percentage. It can be defined in settings at Worktime > Settings > Work hours > Leveling period:
![](https://support.nepton.com/hc/article_attachments/14870728392861)
For example, if an employee is a part-timer with a 60% worktime percentage and the limits of the one-week levelling period in settings are as follows:
![](https://support.nepton.com/hc/article_attachments/14870748814237)
The limits of the employee's entire period would be as follows:
  * Maximum working hours: 22.5 hours
  * Maximum additional work: 17.5 hours
  * Maximum 50% overtime: 10 hours


If worktime percentage is not used to calculate additional work earning threshold, the limits for the entire period would be as follows:
  * Maximum working hours: 37.5 hours
  * Maximum additional work: 2.5 hours
  * Maximum 50% overtime: 10 hours


## Differentiating additional work between 0% and TES additional work rise percentage
Service can be configured to differentiate calculation of additional work so that 0% additional work is earned until full-time obligation is reached and after that additional work is earned based on TES additional work rise percentage. This is achieved by defining both "Use work time percentage to calculate additional work earning threshold" and "Part-time workers should earn additional work 0% under their full-time threshold"-settings to be set as "Yes".
![](https://support.nepton.com/hc/article_attachments/17293510458909)
Example: In a two week levelling period, additional work is earned after 72 hours. A part-time workers work time percentage is 60%. Part-time worker starts to earn additional work after 48 hours, and will earn 0% additional work until 72 hours, the threshold for full-time workers additional work. So for example if part-time workers maximum working hours in the period are 45 hours and they have worked 79 hours during the levelling period, they will earn 30 hours worth of 0% additional work and 4 hours of additional work with their TES additional work rise percentage, as they have worked for 4 hours after fulfilling full-time workers additional work threshold, i.e. 79 h - (45h +30h) = 4h.
## Defining the amount of reduction from absences
Absences shorten the maximum work hours of the levelling period depending on the work obligation on the days of absence.
For example, if the length of the work day (Mon-Fri) is set to 7:30, with a 60% working time percentage, absences would reduce the maximum work hours by 4.5 hours on weekdays.
![](https://support.nepton.com/hc/article_attachments/14870748814621)
If you want to define which three days are absence days in the week, you can do so by setting work day length exceptions to the days.
![](https://support.nepton.com/hc/article_attachments/14870728393885)
## Defining the amount of reduction from public holidays
As with absences, public holidays shorten the levelling period according to the worktime percentage. So, for example, with a worktime percentage of 60%, a public holiday would shorten the maximum work hours of the levelling period by 4.5 hours.
You can also define how much holiday shortens the levelling period by setting work day length exception for the day.
