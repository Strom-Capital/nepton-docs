---
id: 360002559537
title: Setting up a levelling period
url: https://support.nepton.com/hc/en-gb/articles/360002559537-Setting-up-a-levelling-period
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
- tasoittumis
- jaksoylityö
- työajantasaamis
- tasoitusjakso
- tasoittuva
- periodityö
promoted: false
updated_at: '2025-11-19T13:27:59Z'
edited_at: '2025-03-06T14:21:58Z'
---

# Setting up a levelling period

Levelling period overtime calculation can be configured in Nepton. Calculation results are shown as additional work and overtime percentages.
Instructions on Setting up Annual worktime following can be found [here](<https://support.nepton.com/hc/en-gb/articles/360016341617>).
## Requirements for setup
It is recommended that levelling period is set in its own setting group. The setting group that has levelling periods can be named with a descriptive name such as Levelling period work. If possible, setting group is recommended to be its own main setting group, i.e. it does not have a parent setting group. This prevents unnecessary inheritance of other settings to levelling period setting group. Instructions in adding a new setting group can be found here [here.](<https://support.nepton.com/hc/en-gb/articles/360002557537>)
Levelling period setting group should take note of the following matters:
\- Work day length in working contract as defined (e.g 38h 15min / 5 days = 7h 39min per day)   
\- Work week length is not defined, because done work is tracked through periods. Actual calculation from periods is defined in Levelling period settings which will be reviewed later in this guidance  
\- If work shift planning is used and work day length comes from planned shifts, work day lengths are not required to be set in the setting group
Guidance about defining the length of work day can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002558417>). 
## Levelling period settings
Configuring levelling period calculations is described below step by step (1-7).
1\. Define levelling period accrual to be in use in **Work hours > Accruals and overtime hours** **> Levelling period hours**
![](https://support.nepton.com/hc/article_attachments/18667813486365)
2\. Define accrual hour to hour overtime calculated as work time for Levelling period hours by setting it "Yes".
![](https://support.nepton.com/hc/article_attachments/18667825348253)
3\. Define overtime calculations for levelling period
Levelling period overtime limits can be configured to be either by period or by day. See further instructions [here](<https://support.nepton.com/hc/en/articles/4410630282257>).
4\. Define accrual to borrow automatically from levelling period balance when done work is under the amount of regular work time length. This can be configured in **Work hours > Accruals and overtime hours > Calculation settings > Levelling period hours > Borrowing rules > Accrual automatically borrows from balance **by setting it "Yes". 
![](https://support.nepton.com/hc/article_attachments/18667813500445)
5\. Define overtime targets so that base and/or increment part of overtime are targeted correctly to levelling period hours accrual. This can be done in **Work hours > Accruals and overtime hours > Calculation Settings > Overtime**-section.
![](https://support.nepton.com/hc/article_attachments/18667813510557)
6\. Define reset of levelling period balance on the first day of a levelling period as a setting exception in **Work hours > Accruals and overtime hours > Levelling period hours-**section using the validity control. In the example below rule command [ACCRUAL-EARNING-PERIOD-START-DATE|levellingperiodhours] is used so that accrual balance will be reset to 0 minutes every time on the date a levelling period is starting. You can also use specific dates in the field, but it is recommended to use the rule command where possible so that the setting does not need maintenance for adding different periods. Read more about using validity control in settings [here](<https://support.nepton.com/hc/en-gb/articles/360002559358>) and about configuring setting exceptions [here](<https://support.nepton.com/hc/en-gb/articles/360002560677>).
![](https://support.nepton.com/hc/article_attachments/18667813515933)
7\. Finally configure period start dates in **Work hours > Accruals and overtime hours > Levelling period hours**-section**.** Period end dates do not need to be defined as the period ends the day before the next period begins. If period repeats periodically, it can have repeating period length defined in weeks or days and the period will repeat automatically for the set period. In the example below levelling period begins 24.1.2022 and will be repeating every 3 weeks.
![](https://support.nepton.com/hc/article_attachments/18667825409565)
If period lengths are irregular and can not be set as repeating, period start dates can be configured separately by adding period start dates for each row. Every period start date must be added when configuring levelling periods this way.
## Tracking additional work and overtime in a levelling period
Additional work, 50% overtime and 100% overtime formed in a levelling period is shown in a summary on the final day of the levelling period in Activities in calendar - view.
In the example below a 2 week levelling period from 1.1.2024 to 14.1.2024 which has maximum working hours of 67h 30min. Maximum is exceeded by two hours, and thus two hours of additional work is earned. Levelling period additional work and overtime for that period is displayed on the end date of period, i.e. 14.1.2024, regardless of what period is selected for the calendar view.
![](https://support.nepton.com/hc/article_attachments/18667825422749)
Levelling period hours accrual calculates the daily deviation between realised work time and length of work day. Levelling period hours accrual's balance can be spent as a separate levelling period hours leave.
If less work is done in the levelling period than maximum working hours, this is displayed in red in the calendar. In the example below a 2 week levelling period from 4.12.2023 to 17.12.2023 with 67h 30min of maximum working hours has fallen 2h 30min short of maximum working hours
![](https://support.nepton.com/hc/article_attachments/18667813555741)
Note! Before version 2.14.9, time borrowed from the accrual was calculated as work time by default. However, now the setting "Time automatically borrowed from accrual calculated as worked time" has been added to Work hours > Leveling period settings. The default setting is "No". When the day's worked time is below the regular working time, it is now possible to choose how the time borrowed from the accrual is handled. It can be included in the working time, which affects the working hours of the levelling period, or it can be chosen not to do so.
## Approval of levelling period
Levelling period is considered approved when the events it contains are approved. If levelling period length is over one week, check is done for if the last week of the period contains only approved events. Levelling period additional work and overtime are considered approved when the levelling period is approved.
