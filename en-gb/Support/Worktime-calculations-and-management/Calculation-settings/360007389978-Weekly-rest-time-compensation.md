---
id: 360007389978
title: Weekly rest time compensation
url: https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- viikkovapaakorvaus
- kertapalkkio
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-02-02T06:29:50Z'
---

# Weekly rest time compensation

## General
The service can be configured to award the employee compensation for not reaching a specified minimum threshold of _uninterrupted_ rest time over a single week, or an average over multiple weeks, as defined in the Finnish Working hours act 27 §.
The amount of rest in the weekly rest period is evaluated on the final day in the period, relative to the employee's work weeks before and the weekly rest starting date setting if used.
If a work rise needs to be earned with increase during weekly rest compensation, it can be done in [work rise settings](<https://support.nepton.com/hc/en-gb/articles/360002560978>).
## Weekly rest period configuration
The weekly rest compensation can be defined in the **Worktime > Administration > Working community settings > Work Hours > Weekly rest period** section or in the **Worktime > Administration > Setting groups > Work Hours > Weekly rest period** section, respectively.
### "Weekly rest period calculations" settings
![](https://support.nepton.com/hc/article_attachments/13230126410653)
This section defines whether an employee is due weekly rest time compensation (but not how much they are due).
  * **Average weekly rest time length** \- Defines the minimum uninterrupted rest time an employee must receive on average over the duration of the weekly rest period. This is typically 35 hours.
  * **Number of weeks to check** \- Defines the length of the weekly rest period in weeks.
  * **Starting date if multiple weeks checked** \- If the weekly rest period is more than 1 week long, the system needs to know what date it's relative to. The weekly rest calculations are evaluated and compensated (if required) at the end of a multi-week period. For example, if your starting date is 02.01.2023 and you have a 2 week period, then your first weekly rest calculation period is 02.01.2023 to 15.01.2023 and if the average weekly rest time is not met, then the compensation will be awarded on the 15.01.2023 (+/- offsets). If the start date does not coincide with the first day of an employee's normal work week, then the starting date is automatically rounded down, this ensures that the compensation is awarded at the end of their week.
  * **Work week start/end offset** \- Offsets can be added to the work we are checking if, for example, your work week is Monday 00:00 to Sunday 24:00 but the rest time should be checked until 6AM on the day after the week, then the end offset would be +6 hours. The offset can be added both to work week start and work week end simultaneously. 
When using positive work week end offsets, the date the weekly rest compensation is compensated moves to the calculation day the offset ends on e.g. for a standard work week with an end offset of +6 hours, the weekly rest compensation will be paid on Mondays. Similarly, the setting Rendering options - Event rendering also affects when the weekly rest allowance is paid. If the setting is Salary earned is shown on the day the shift ends, the compensation will be paid on Monday.
  * **Event types treated as rest time** \- Any event types that should be treated as contributing to an employee's rest should be configured here e.g. balance leave, annual leave etc
  * **Accrual hour to hour overtime calculated as rest time** \- Configures whether any time that is paid as "hour to hour" over the work obligation should be treated as rest.
  * **Overtime compensation treated as rest time** \- Configures whether any time that is paid as "overtime" should be treated as rest.


### "Compensation when average weekly rest threshold is not met" settings
This section defines how compensation is awarded to the employee if they have not met their average rest time threshold defined above.
  * **Pay compensation to** \- By default, compensation will be paid as part of the employee's salary, but it can also be configured so employees can take leave instead. Start by picking an accrual to pay the compensation into, typically this would be the "Viikkolepo" balance accrual. You will then need to ensure the Weekly rest accrual is enabled and the "Viikkolepovapaa" event type is available to employees when recording events. More information can be found in the [Accruals guidance](<https://support.nepton.com/hc/en-gb/articles/360005073918-Accruals>).  
_Note: when exporting weekly rest compensation to an external system using the integration rulesets, the target for the pay can be determined using the "basePartTarget" field._
  * **How compensation is earned** :
    * Not set - setting value is inherited from upper levels. (in Working community settings "Not set" means the feature is not in use)
    * Not earned - no compensation is paid to the employee even if they haven't met the legal obligation for rest time.
    * Earned as fixed amount - a fixed amount can be paid in hours/minutes (see "Fixed compensation amount").
    * Earned based on worked time - the compensation amount is based on work done during the rest period (see "If compensation based on worked time").
    * Earned based on rest deficit - e.g. if you have a 35 hour rest threshold and the employees longest uninterrupted rest is only 30 hours, then 5 hours of weekly rest time is earned.
    * Earned based on worked time (or rest deficit if none) - If there is work during the earning period, that is used to form the compensation, otherwise it is earned based on the rest deficit, as described above


  * **Fixed compensation amount** \- If the above setting is configured to be "Earned as fixed amount" and the employee has not had enough rest, they will be compensated the amount specified here. If a multi-week period is used, the compensation is paid once at the end.


  * **If compensation based on worked time**
  *     * **Earning period based on**
      * Not set - setting value is inherited from upper levels (in Working community settings "Not set" means the feature is not in use)
      * Work at end of calculation week - Work performed during the "end of the week" will be compensated for the same amount of time. What constitutes the "end of the week" can be configured with the "Earning period duration" setting. If there are multiple weeks in the weekly rest period, the end of each week is checked for the rest deficit and the amounts summed to formed the total compensation.
      * Work after Friday shift or before end of week - The amount of Work performed after the Friday shift (up to the earning period duration), and before the end of the calculation week (as described above) are both evaluated. The approach which would result in the least compensation is used. When using this mode please also complete the Friday shift end time.
      * Work before first shift of next week - The earning period is checked back from before the start of next week's first shift. If there is no shift on the day or it's a public holiday, the default work start time is used. Note: this also overrides the rest evaluation period to check 7 days back from the same point.
      * Week day with the least work - The day in the work week with the least work is used as the basis for the compensation amount. For example, if every day has 10 hours of work except for Wednesday that has 8 hours, then 8 hours would be compensated. If there are multiple weeks in the weekly rest period, the day with the least work is checked for each week and the amounts summed to formed the total compensation. By default, the full time of an overnight shift on the day with the least work is compensated but this can be overridden by setting the earning period duration to 24 hours and then only the work time overlapping the day is compensated.
      * Sunday after 00:00 - Compensation is earned for work done after Sunday midnight (i.e. the first minute of Sunday). If the earning period duration is set, this is used to set the end of the earning period, for example, 24h would set the earning period from Sunday 00:00 to Sunday 24:00. If the earning period duration is not set, any shifts belonging to Sunday will earn compensation, even ones that go overnight to Monday.
    * **Earning period duration** \- The number of hours that we are checking for work that should be compensated i.e. so we can see how much work was done during the period that the employee should have uninterrupted rest. For example, when used with "Work at end of calculation week", if the normal work week ends on Sunday at 24:00 and a +6:00 offset is applied so weekly rest time calculations check for rest up to 6am on the Monday, then an earning period duration of 35h be checking for any work during the 35 hours before Monday 6am and compensating that time. If there were 5 hours of work in that period, then 5 hours of weekly rest compensation would be awarded for that week.


  * **Additional options**
    * Rounding method/interval - Rounds the total compensation earned according to settings
    * Rounding threshold - Threshold value for rounding
      * When the rounding method is "up" and the threshold value is set, rounding is performed only if the remainder is above the threshold value
      * When rounding method is "normal" and the threshold value is set, the rounding down is performed when the remainder is less than the threshold value, otherwise rounding up occurs
      * Rounding "down" will occur if the threshold is not set, or if the remainder is less than the threshold
    * Minimum/maximum compensation amount - Sets limits on the minimum or maximum amount of compensation that can be earned


The setting **Rendering options - Event rendering** also affects when the weekly rest allowance is paid. If the setting is 'Salary earned is shown on the day the shift ends', the compensation is formed after the last day of the week (usually on Monday).
## Examples
### Example 1. One week to check, fixed compensation to balance
Below is an example of a case where weekly rest is checked from a one-week period. In this example, we look at whether the 35-hour rest period has been completed within a week.
![](https://support.nepton.com/hc/article_attachments/19834533293085)
The compensation is set at a fixed 10 hours, which is compensated in the balance.
![](https://support.nepton.com/hc/article_attachments/19834524613789)
The minimum rest period of 35 hours has not been met, so a compensation of 10 hours is created for Sunday, and it is directed directly to the balance. By clicking on the info button next to the weekly rest time compensation, a more detailed summary of the weekly rest calculation opens up:
![](https://support.nepton.com/hc/article_attachments/19834533305245)
The pop-up window shows that the review period for the weekly rest time calculation in question is the week of June 10-16. The minimum rest period is 35 hours, but the longest rest period in the period has been 22 hours, i.e. 13 hours short of the target. Since a fixed compensation has been set, the amount of the compensation is 10h, which is compensated to the balance.
### Example 2. One week to check, compensation based on rest deficit
If the compensation is not fixed, but is based on the shortest rest period in the review period, the compensation for the same situation would look like this:
![](https://support.nepton.com/hc/article_attachments/19835885515805)
![](https://support.nepton.com/hc/article_attachments/19835885520541)
The weekly rest time compensation is 13h, because the longest rest period in the period has been 22h, i.e. 13h less than 35h. In this case, the compensation is paid in the salary instead of transferred to the accumulated balance.
### Example 3. One week to check, work week end offset +6h, compensation based on worked time
In this example, the work week end offset is set to +6h, which means that the review period does not end until Monday at 06:00.
![](https://support.nepton.com/hc/article_attachments/19836752723229)
The review period therefore is 10.6. 00:00 - 17.6. 06:00. Compensation is based on worked time, and is formed according to how much work has been done at the end of the calculation week, counting back 24 hours.
![](https://support.nepton.com/hc/article_attachments/19836737238685)
Since the work week end offset is set to +6h, the end of the review period is moved to Monday. For this reason, the weekly rest time compensation also appears in the calendar on Monday.
![](https://support.nepton.com/hc/article_attachments/19836752730909)
By clicking the info button again opens a more detailed explanation of how the compensation is calculated.
![](https://support.nepton.com/hc/article_attachments/19836737245469)
In this case, the compensation is 5 hours, because counting back 24 hours from Monday morning at 06:00, until Sunday morning at 06:00, a total of 5 hours of work has been done.
### Example 4. Two weeks to check, compensation based on work done on the weekday with least work
In the following example, instead of one week, the length of the review period is two weeks. When examining the two-week rest period, the service checks the time period two weeks back, takes into account the longest rest period in both weeks, and concludes whether there was enough rest time on average. If there is not, the compensation is formed according to the settings, in this case the compensation is based on worked time, and is formed according to the hours of the day when the least amount of work has been done during the review period.
![](https://support.nepton.com/hc/article_attachments/19837432306973)
In the calendar view it looks like this:
![](https://support.nepton.com/hc/article_attachments/19837432311581)
The weekly rest compensation is shown at the end of the two-week review period. When clicked on the information ball, the pop up window displays that the review period has been June 3-16. Both weeks' calculation is detailed in their own sections. In the first week, the longest rest period has been 21:00 (between Sat-Sun), while in the second week, the rest period has been 20:00. The 35-hour weekly rest has therefore not been fulfilled in either week. Since the compensation is based on the worked hours of the day when the least amount of work has been done, there will be a total of 7 hours of weekly rest compensation: 3 hours from Saturday of the first week and 4 hours from Saturday of the following week.
If no work had been done on the second weekend (the last work event was Friday's entry), the average minimum rest period of the review period would have been met, and no compensation would have been received. If the work was done only on Sunday so that the rest period of one week is fulfilled, but not the other, the compensation is calculated according to the two-week review period according to the shortest working day of both weeks:
![](https://support.nepton.com/hc/article_attachments/19837432318237)
##  Disabling the earning of weekly rest compensation
In certain setting groups, it may be necessary to disable the weekly rest compensation so that the settings are not inherited from a higher-level setting group. In this case, set the value of How compensation is calculated under the Compensation when weekly rest period is not met settings as **Not earned**.
![](https://support.nepton.com/hc/article_attachments/21472316380573)
