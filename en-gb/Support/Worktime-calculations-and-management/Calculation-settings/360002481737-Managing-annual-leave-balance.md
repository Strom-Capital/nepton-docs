---
id: 360002481737
title: Managing annual leave balance
url: https://support.nepton.com/hc/en-gb/articles/360002481737-Managing-annual-leave-balance
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- vuosiloma
- Käyttöönotto
- annual leave settings
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-04-30T05:23:33Z'
---

# Managing annual leave balance

If the amount of annual leave accrual does not match, the first thing you need to do is refresh the accrual calculation.
The easiest way to do this is to save a Notes event in the calendar, for example, before the time when the calculation does not match.
## Principles of annual leave calculations
The remaining annual leave balance can be seen from reports and event editing window when recording annual leave. The vacation entitlement for the current vacation year is the value of the vacation balance at the end of the vacation season (March 31). When setting and changing annual holidays, it is important to understand that the vacation earning year is April-March, and holidays earned in this period can be used only on the next holiday year (April-March). When setting annual holidays, you should always be careful that the earned days are registered for the right holiday year, so that they are available at the right time.
## Setting annual leaves
When the annual leave calculation is defined when the service is first taken into use, the earned annual leaves that have accrued from the period before the recording of working time events in the previous and the current leave year must be reported to the service. For example, if Nepton is taken into use on June 1:
  * the person's unused annual leave days from the previous holiday year must be set to March of the vacation year previously ended. Then the person has the right amount of accrued leave on March 31, which is used as holiday entitlement for the current vacation year.
  * In addition to that, another export is made for April, which includes the holidays earned during April and May before Nepton was taken into use. When the use starts in June, leave is accrued for people starting from that day, as per the settings. Thus, at the end of this holiday year, the person has earned the right amount of vacation for each month, including the first 2 months when Nepton was not yet in use.


If the calculation of annual leave earnings is not implemented in Nepton until later than at the time of the service being taken into use, we recommend, for the sake of clarity, to implement the calculations at the beginning of the holiday year, i.e. from April. However, if earning is implemented in the middle of the holiday year, the service must be informed of the earned annual leave rights that have been accumulated or not used before the time of annual leave calculation begins.
  * the person's unused annual leave days from the previous holiday year must be set to March of the vacation year previously ended. Then the person has the right amount of accrued leave on March 31, which is used as holiday entitlement for the current vacation year.
  * Annual leave earning settings must be activated from 1st of April onwards using the [validity tool](<https://support.nepton.com/hc/en-gb/articles/360002559358>).
  * Please note: the annual leave report 'annual leave, earned days' cannot show the correct accumulation of annual leave from the previous year, when the calculation was not yet in use. This report can only be used for the period when the calculation of annual leave earnings has been in use.


Examples for setting annual leave can be found [here](<https://support.nepton.com/hc/en-gb/articles/4409591067409>).
Further instructions for Setting up annual leave earning can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002560698>).
## Manual changes to annual leave balance
The annual leave balance can be set, changed or locked per user. Functions are done in the person's calendar view under **Work time > Work hours > Events in calendar.** Only persons who have the [right](<https://support.nepton.com/hc/en-gb/articles/360002554338>) to manage Annual Leave can make manual changes to annual leave. In order for the functions to be performed, the event types "Annual leave earning reset", "Annual leave earning change", and "Annual leave balance locking" must be activated at the Working community (or desired setting group) level. All administrative events, such as a change or setting of annual leave earnings, are shown in pink color in the calendar.
### Annual leave earning reset
With this setting, a new value can be set for the employee's annual leave balance. The value is set when Nepton is first taken into use in order to update current annual leave balances.
The annual leave balance is set in the person's Events in calendar view by clicking on the date for which the setting is to be made. The event type to be used is 'Annual leave earning reset'. The setting applies to that month and by default appears in the calendar on the first day of the selected month. The change affects the annual leave balance of the following holiday year. Whole days are marked in amount of days and half days as 12 hours. The days can be set to either + i.e. a positive value, or - i.e. a negative value in a situation where more holidays have been used than earned.
![](https://support.nepton.com/hc/article_attachments/20918611219869)
### Annual leave earning change
This setting can be used to change the employee's accrued annual leave balance, for example when the employee exchanges holiday money for annual leave days. The change is made for the holiday year in which the days are earned, so that the annual leave days are available in the correct holiday year. The change is visible on the day it is made.
The annual leave balance is changed in the person's Events in calendar view by clicking on the date for which the setting is to be made. The event type to be used is 'Annual leave earning change'. The change can be either negative (days are subtracted from the accrual) or positive (days are added to the accrual).
![](https://support.nepton.com/hc/article_attachments/20918715233565)
### Annual leave balance locking
With this setting, the employee's annual leave balance can be locked, after which the annual leave balance can no longer be changed. Locking the annual leave balance is done in the person's Events in calendar view by clicking on the date for which the setting is to be made. 'Annual leave balance locking' is selected as the event type. The start and end dates are given for the event, the interval between which will be locked, and during this period no changes can be made to the annual leave balance. Also, the annual leave days recorded for that time period do not decrease the annual leave balance, and thus do not fulfill the day's work obligation.
![](https://support.nepton.com/hc/article_attachments/20918825832989)
## Annual leave balance reset for multiple persons at once
Annual leave balances can also be updated for individuals by filling in the data in one file and importing it to Nepton. This is done, for example, when the service is first taken into use and the annual leaves earned in the previous holiday year must be updated for the entire personnel at the same time. If annual leave is updated for two different holiday years, the balances of the previous holiday year must be imported with the annual leave earning reset, and the changes to the current annual leave balance with the Annual leave earning change. This is done with [Event import](<https://support.nepton.com/hc/en-gb/articles/360002868137>) function.
