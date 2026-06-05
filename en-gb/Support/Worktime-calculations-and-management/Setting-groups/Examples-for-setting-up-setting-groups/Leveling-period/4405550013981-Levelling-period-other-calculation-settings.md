---
id: 4405550013981
title: Levelling period other calculation settings
url: https://support.nepton.com/hc/en-gb/articles/4405550013981-Levelling-period-other-calculation-settings
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
labels:
- jaksolisätyö
promoted: false
updated_at: '2025-10-16T10:00:01Z'
edited_at: '2025-10-16T10:00:01Z'
---

# Levelling period other calculation settings

## Levelling period calculation settings  
Levelling period has settings, that can be used to control different accrual and event type functionality towards calculating levelling period and to take note of different working agreements. These settings are described below.
### Use TES settings for event type contribution towards period
If this setting is on, levelling period calculations will take use of TES-settings "[Event types that contribute to work week](<https://support.nepton.com/hc/en-gb/articles/25639644303645>)" and "[Absence types that contribute to work week](<https://support.nepton.com/hc/en-gb/articles/28576011538077>)" to dictate which event types are calculated as work towards levelling period. This allows for example to add unpaid absences to contribute to levelling period.
"Absence types that contribute to work week"-setting can be used to define that certain absence type is not calculated as work towards levelling period. For example if it has been set that unpaid absence contributes to work week/levelling period, it can be separately defined that for example "Leave of absence"-type does not contribute towards levelling period by setting it as "No".
### Additional work calculated as worked time
This setting determinates whether additional work hours resulting from regular daily or weekly overtime calculations are counted towards the total working hours of the levelling period.
For example, if the levelling period is one week and the expected working time is 40 hours, and a person works 40 hours of regular time and 2.5 hours of daily additional work (not levelling period additional work), then: 
  * If the setting is enabled, the total hours worked during the levelling period will be 42.5 hours
  * If the setting is disabled, the total hours worked during the levelling period will be 40 hours


This setting only applies to additional work that is compensated with pay.
### Treat public holidays as work days in maximum overtime calculations
Is a public holiday that falls on a weekday (Mon-Fri) and shortens the work week to be counted as a working day in the levelling period.
In the example, the levelling period is one week, Ascension Day (Thursday) is a public holiday, and the "Limits on work days in the period"-settings are as below. During the week (Tuesday, May 24, 2022), 2.5 hours of overtime have been accumulated.
![](https://support.nepton.com/hc/article_attachments/28580748903709)![](https://support.nepton.com/hc/article_attachments/28580789175837)
If setting is "No" or "Not set", 2,5 hours of overtime is divided to **four** working days as 50% overtime, and rest of the overtime in period is 100% overtime, which can be earned in this case an infinite amount.
![](https://support.nepton.com/hc/article_attachments/28580748905245)
If setting is set to "Yes", 2,5 hours of overtime is divided to **five** working days as 50% overtime.  
![](https://support.nepton.com/hc/article_attachments/28580748908061)
### Treat absence days as work days in maximum overtime calculations
Whether an absence on a weekday (Mon-Fri) is calculated towards work in the levelling period.
In the example below levelling period length is one week. Mon-Thu are work days, Friday is an absence day (sick leave). "Limits on work days in the period" is as in the image below. 2.5 hours of overtime were accumulated during the week (Tuesday, June 7, 2022).
![](https://support.nepton.com/hc/article_attachments/28580748903709)![](https://support.nepton.com/hc/article_attachments/28580789182237)
If setting is "No" or "Not set", 2,5 hours of overtime is divided to **four** working days as 50% overtime, and rest of the overtime in period is 100% overtime, which can be earned in this case an infinite amount.
![](https://support.nepton.com/hc/article_attachments/28580789183517)
If setting is set to "Yes", 2,5 hours of overtime is divided to **five** working days as 50% overtime.
![](https://support.nepton.com/hc/article_attachments/28580789184925)
### Treat annual leaves as work days in maximum overtime calculations
Whether an annual leave on a weekday (Mon-Fri) is calculated towards work in the levelling period.
In the example below levelling period length is one week. Mon-Thu are work days, Friday is an annual leave day. "Limits on work days in the period" is as in the image below. 2.5 hours of overtime were accumulated during the week (Tuesday, June 7, 2022).
![](https://support.nepton.com/hc/article_attachments/28580748903709)
![](https://support.nepton.com/hc/article_attachments/28580789185949)  
  
If setting is "No" or "Not set", 2,5 hours of overtime is divided to **four** working days as 50% overtime, and rest of the overtime in period is 100% overtime, which can be earned in this case an infinite amount.
![](https://support.nepton.com/hc/article_attachments/28580789183517)
If setting is set to "Yes", 2,5 hours of overtime is divided to **five** working days as 50% overtime.
![](https://support.nepton.com/hc/article_attachments/28580789184925)
### Use average length of work day for levelling period days outside employment
Is the number of hours defined in "Average length of work day"-setting added to the levelling period hours for each weekday (Mon-Fri) within the levelling period that is not included in the persons employment period.
For example, if the levelling period is one week and Mon-Fri are considered working days, but the employment starts on Tuesday, and the "Average length of work day"-setting is 8 hours, then:
  * If the setting is enabled, a calculated 8 hours will be added to the actual working hours during the levelling period (Tue-Fri)
  * 8 hours is added on days outside employment period if these days have hours borrowed from levelling period accrual. 


### Exclude event from levelling period overtime calculations
Is the time recorded for an event type calculated as work towards levelling period that adds to overtime calculations or not.
For example a levelling period length is one week and the expected working time is 40 hours, and the person performs 40 hours of regular work and 8 hours of travel time:
  * If travel time is set to be excluded from adding overtime to the levelling period, the total hours worked in the levelling period will be 40 hours
  * Otherwise, the total hours worked in the levelling period will be 48 hours.


![](https://support.nepton.com/hc/article_attachments/28580748919837)
### Absences that use average length of work day instead of activity duration
Is time recorded for an event type calculated towards levelling period work or is "Average length of work day"-setting used instead for each day that has event types that are configured with this setting.
For example levelling period average length is 8 hours and sick leaves are set to use average length of work day instead of the duration of the event:
  * If the person is on sick leave for the entire day, the number of hours counted for that day in the levelling period calculation is 8 hours.
  * If the person works 4 hours of the shift and then goes on sick leave, the number of hours counted for that day in the levelling period calculation is 8 hours (based on the average working day length)
  * If the person works 8.5 hours of the shift and then goes on sick leave, the number of hours counted for that day in the levelling period calculation is 8.5 hours (based on actual worked time, since it exceeds the average length of work day.


![](https://support.nepton.com/hc/article_attachments/28580789190941)
### Accrual hour to hour overtime calculated as worked time
These settings can be used to control whether hour-for-hour overtime is counted as working time in the levelling period or not. The calculation can be directed based on which accrual the work has been allocated to.
For example, if hour-for-hour overtime allocated to bank should be counted as working hours in the levelling period, this can be achieved with the following settings.
![](https://support.nepton.com/hc/article_attachments/28580789193629)
### Average length of work day
This defines the calculated length of a working day on weekdays (Mon-Fri). In the levelling period calculation, the assumed working days are Mon-Fri. If the total hours worked during the levelling period are distributed across the working days and the daily amount exceeds the average length of work day, additional and overtime hours are generated.
For example, if the levelling period is one week and the setting is 8 hours, then the total working hours for the levelling period would be 40 hours (5 x 8h) before any additional or overtime hours are generated.
### Get work day length from shift
Is the maximum working time of the levelling period calculated based on the scheduled shifts within the period.
For example, if the levelling period is one week and there is an 8-hour work shift on each day (Mon-Sun) and the setting is enabled, the maximum working time for the levelling period would be 56 hours (7 x 8 h).
### Limits on work days in the period
![](https://support.nepton.com/hc/article_attachments/28583183116573)
#### Exceeding the length of a workday is compensated as a maximum of - Additional work
Maximum amount of additional work per working day in the levelling period. The amount is set in the format HH:MM. For example, 12 minutes is entered as 00:12 and 1 hour 30 minutes as 01:30. 
For example, if the levelling period is one week and the setting is 00:12, then the maximum amount of additional work for the levelling period would be 1 hour (5 working days).
#### Exceeding the length of a workday is compensated as a maximum of - 50% overtime
Maximum amount of 50% overtime per working day in the levelling period. The amount is set in the format HH:MM. For example, 24 minutes is entered as 00:24 and 1 hour 30 minutes as 01:30. 
For example, if the levelling period is one week and the setting is 00:24, then the maximum amount of 50% overtime for the levelling period would be 2 hours (5 working days).
#### Exceeding the length of a workday is compensated as a maximum of - 100% overtime
Maximum amount of 100% overtime per working day in the levelling period. The amount is set in the format HH:MM. For example, 5 hours is entered as 05:00 and 1 hour 30 minutes as 01:30. 
For example, if the levelling period is one week and the setting is 05:00, then the maximum amount of 100% overtime for the levelling period would be 25 hours (5 working days).
### Levelling period compensation
![](https://support.nepton.com/hc/article_attachments/28583183117981)
#### Additional work earned after
The maximum amount of work for a levelling period after which additional work is earned. The amount is set in the format HH:MM. For example 10 hours and 30 minutes is set as 10:30 and 120 hours is set as 120:00.
#### 50% overtime earned after
After how many levelling period working hours is 50% overtime earned. Note that additional work is earned before this threshold. The amount is set in the format HH:MM. For example 10 hours and 30 minutes is entered as 10:30 and 126 hours as 126:00.
For example, if the maximum number of hours in the levelling period are 120 hours and this setting is 126 hours, then a maximum of 6 hours of additional work can be earned during the entire levelling period, and after these 6 additional hours, 50% overtime is earned.
#### 100% overtime earned after
After how many levelling period working hours is 100% overtime earned. Note that 50% overtime is earned before this threshold. The amount is set in the format HH:MM. For example 10 hours and 30 minutes is entered as 10:30 and 150 hours as 150:00.
For example, if the maximum working hours in the levelling period are 120 hours, the maximum amount of additional work is 6 hours, and this setting is 150 hours, then a maximum of 24 hours of 50% overtime can be earned during the entire levelling period, after which 100% overtime is earned.
#### Uncompensated after
After how many period working hours are hours no longer compensated. The amount is set in the format HH:MM. For example, 10 hours 30 minutes is entered as 10:30 and 500 hours as 500:00. 
For example, if the maximum working hours in the levelling period are 120 hours, the maximum amount of additional work is 6 hours, the maximum amount of 50% overtime is 24 hours, and this setting is 500 hours, then a maximum of 350 hours of 100% overtime can be earned during the entire levelling period, after which overtime hours are no longer compensated. 
This setting is usually set to a number high enough that the limit is never reached.
### Reductions to levelling period limits on public holidays
Public holidays that shorten work week can be set to reduce the levelling periods:
  * Maximum regular time
  * Maximum additional work
  * Maximum 50% overtime
