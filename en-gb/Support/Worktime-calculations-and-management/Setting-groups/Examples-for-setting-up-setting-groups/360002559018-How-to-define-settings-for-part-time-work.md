---
id: 360002559018
title: How to define settings for part-time work
url: https://support.nepton.com/hc/en-gb/articles/360002559018-How-to-define-settings-for-part-time-work
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
- NEPTONNEEDSREVIEW
- osatyöaika
promoted: false
updated_at: '2025-10-13T11:51:56Z'
edited_at: '2024-07-16T12:55:06Z'
---

# How to define settings for part-time work

## Different types of part-time work and how to define the settings in Nepton
In Nepton, different types of part-time work can be divided into three categories. However, these three categories can include an endless variety of work obligations. The options on how to define settings for these different kinds of part-time employees are:
  * Utilizing the work time percentage. A separate article about work time percentage can be found [here](<https://support.nepton.com/hc/en-gb/articles/360003961118>).
  * A new setting group for employees who work **shorter days**
  * A new setting group for employees who work **irregular** **shorter weeks**
  * A new setting group for employees who work **regular shorter weeks**


If the current setting group is using [Nepton's shift planning](<https://nepton.com/workshift-planning/>), check paragraph 6.
## Employees who work shorter days
This is a form of part-time work in which a person works the same working days as if they were working full-time, but works shorter days.
An example of this type of part-time work:  
  
The weekly working time of the working community is 37.5 hours and the daily working time is 7.5 hours per day, from Monday to Friday. A part-time worker working 80% of the hours, working a shortened day, therefore works 30 hours a week, six (6) hours a day, from Monday to Friday. The working days are the same as for a full-time employee, the length of the working day is shorter.
This type of part-time work can be defined in the following two ways:
### Work time percentage
You can set a work time percentage for a part-time worker who works shortened days. The work time percentage is set with [the validity function](<https://support.nepton.com/hc/en-gb/articles/360004856937>). An empty field is interpreted as a value of 100 %, i.e. full working time.
When the work time percentage is set, Nepton automatically calculates the percentage of daily and weekly work time from the settings of the setting group. The work time is calculated to be evenly distributed over the workind days of the week.
Absences and the minus and plus balance are compared to the person's shortened day and compensated in proportion to the person's work time percentage. The processing of absences and balance hours for those working a shortened day is automatic.
Read more about the work time percentage [here](<https://support.nepton.com/hc/en-gb/articles/360003961118>).
### A new setting group for employees working shorter days
You can create a new setting group for part-timers working shorter days. Instructions for creating a new setting group can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002557537>) (1 Add manually). It is recommended to place the new setting group below the full-time setting group, so that the same settings affecting the interpretation of work time are also inherited to the lower level part-time setting group. Make sure that the correct values ​​are set for the length of the working day ([instructions here](<https://support.nepton.com/hc/en-gb/articles/360002558417>)) and the length of the working week ([instructions here](<https://support.nepton.com/hc/en-gb/articles/360002558537>)) in the new part-time settings group.
## Employees who work irregular shorter weeks
This is a form of part-time work where a person only works part of the working days that they would work if they were full-time. In an irregular week, the work days are not agreed in advance, or the agreed days vary from week to week.
In Nepton, the work time settings for part-timers who work an irregular shortened work week can be defined in two ways, with the work time percentage or by creating a new setting group:
### Work time percentage
You can set [a work time percentage](<https://support.nepton.com/hc/en-gb/articles/360003961118>) for a part-time worker who works irregular shorter weeks. The work time percentage is set with [the validity function](<https://support.nepton.com/hc/en-gb/articles/360004856937>).
A recorded absence or balance is compared to the person's shortened day and compensated according to the person's work time percentage. The amount of absence and balance to be compensated at the end of the week is correct if the length of the work week calculated using the working time percentage has been met or hasn't been exceeded.
If the person is absent for a whole week, Nepton calculates a minus balance for the whole week.If the person does double the weekly workload the following week, the minus balances from the previous week are reset and the balance equalizes.
The person in the example below works an irregular 7.5-hour work week. According to the working time percentage, the length of a work day is 1 hour 30 minutes and the length of a work week is 7 hours 30 minutes. The balance is 0 minutes at the beginning of the week.
![osa-aikainen.jpg](https://support.nepton.com/hc/article_attachments/20217818894109)
  * The work event on Monday is from 08:00 to 10:30. Work time is two hours. Since he work day length is 1h 30min, 30 minutes is added to the balance.
  * There is no work event on Tuesday. Since the work day length is 1h 30min this 1h 30minutes is deducted from the balance.
  * The work event on Wednesday is from 08:00 to 10:30. Work time is two hours. Since the work day length is 1h 30min, 30 minutes is added to the balance.
  * There is no work event on Tuesday. Since the work day length is 1h 30min this 1h 30minutes is deducted from the balance.
  * The work event on Friday is from 08:00 to 12:00. Work time is four hours. Since the work day length is 1h 30min, 2 hours and 30 minutes is added to the balance. At the end of the work week, a total of 30 minutes has accumulated to the balance.


### A new setting group for employees who work irregular shorter weeks
You can also create a new setting group for part-timers working irregular shorter work weeks. Instructions for creating a new setting group can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002557537>) (1 Add manually). It is recommended to place the new setting group below the full-time setting group, so that the same settings affecting the interpretation of work time are also inherited to the lower level part-time setting group.
[Length of work day](<https://support.nepton.com/hc/en-gb/articles/360002558417>) and l[ength of work week](<https://support.nepton.com/hc/en-gb/articles/360002558537>) are defined for the part-time setting group, and t**he person's work time percentage is not changed**.
The same length of work day is set for all weekdays. In addition, the event type "Weekly leave" should be set as [the assumed event type](<https://support.nepton.com/hc/en-gb/articles/360002558717>) so that this event will be automatically added to work days without any event. This ensures that the work time calculations are correct in the work time calendar and the part-time worker doesn't get a negative balance.
At times, it may be necessary to use a setting that deducts the difference between the hours worked on a week and the length of work week from balance. 
This setting is '**Borrow at the end of the week if weekly obligation not fulfilled** '. and can be found the setting group setting in **Work hours - Accruals and overtime hours - Calculation settings: Balance**.
Here's an example of a week like this, when a part-timer has two "extra" absence days and these absences should be deducted from the balance:  
  
![FuVVu2qfnQ.png](https://support.nepton.com/hc/article_attachments/20219880338589)  

If this setting isn't in use, the assumed event "Weekly leave" causes absence days not to be deducted from balande.
## A new setting group for employees who work regular shorter weeks
This is a form of part-time work in which a person works only part of the working days that they would work if they were full-time. In a regular week, the working days are agreed in advance, meaning that the person has an agreed work rhythm. 
[A new setting group](<https://support.nepton.com/hc/en-gb/articles/360002557537>) (1 Add manually) is created for employees who work regular shorter weeks. The new setting group is created below the full-time setting group, so that the same settings affecting the interpretation of work time are also inherited to the lower level part-time setting group.
[Length of work day](<https://support.nepton.com/hc/en-gb/articles/360002558417>) and l[ength of work week](<https://support.nepton.com/hc/en-gb/articles/360002558537>) are defined for the part-time setting group and are the basis of the calculation for regular working hours, absences and public holidays. **The person's work time percentage is not changed**. When defining the length of work day and work week:  

  * Length of work day is the same as with full-time workers'. Weekdays that are not work days are set as 0 minutes long.
  * Length of work week is set according to the part-time worker's work week length.


After creating the part-time setting group, it is recommended to test how the public holiday settings and annual leave settings that are inherited from the full-time setting group work for the part-timers. It may be necessary to change some settings for the part-time setting group, in which case the necessary instructions can be found in the articles [Public holiday management](<https://support.nepton.com/hc/en-gb/articles/360002558797>) and [Setting up annual leave earning](<https://support.nepton.com/hc/en-gb/articles/360002560698>).
## This to consider when interpreting annual holidays when a person has days without a work obligation
For those working a shortened work week, zero minutes will probably be marked as an obligation for some of the workweek days, i.e. people have days where they do not have a work obligation. These days must be taken into account for annual holidays, because annual leave is not taken if there is no obligation on the working day. Check out the separate instructions for earning annual leave [here](<https://support.nepton.com/hc/en-gb/articles/360002560698>), in section 4.4 of the instructions.
## Person's work time when shift planning is in use
A person's work obligation can also come directly from shift planning. In this case, a new setting group is not created, but the published shift list is the basis for calculating absences and work days. By defining [the minimum and maximum obligations](<https://support.nepton.com/hc/en-gb/articles/360004769718>) of a person's weekly working time from the employment section, how many hours a person can work per week is defined. Minimum and maximum obligations can be used in shift planning as target numbers to support planning.
## Changing the work week hours in the middle of the work week
If a person's work week obligation changes in the middle of the work week, the service does not automatically identify which work time obligation it should follow in its calculation. Because of this, the correct length of the work week must be calculated and entered manually.
For example: a person works part-time, 80 % of the working time, from Monday to Wednesday. The length of the work day is 6 hours/day. From Thursday, the person will return to working full time (work obligation is 100 %), so the length of the working day is 7.5h/day on Thursday and Friday. So add up the hourly obligation of the working days to get the work obligation for the entire working week, according to the previous example like this:
Monday - Wednesday: 3 x 6h = 18h
Thursday - Friday: 2 x 7.5h = 15h
The total work week obligation is therefore 33 hours, when the work obligation has changed in the middle of the work week.
You can set an exception to the total work week obligation by pressing the date icon in the person's working time calendar and selecting the length of the work week. The "Edit length of work week" view opens in a new window, where you can set an exception setting for the length of the work week.
![](https://support.nepton.com/hc/article_attachments/20221375275805)
## Changing settings for the past
If setting group settings are changed retroactively, the person's accrual values may not be up-to-date in the work time calendar after the change. This may be alerted by a yellow triangle in the work time calendar. In these cases, the work time calendars must be manually updated. Instructions for updating the accruals for one person or multiple people can be found [here](<https://support.nepton.com/hc/en-gb/articles/4411220910865>).
