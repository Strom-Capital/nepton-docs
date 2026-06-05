---
id: 360002558557
title: Rounding settings
url: https://support.nepton.com/hc/en-gb/articles/360002558557-Rounding-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels: []
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-01-14T07:47:23Z'
---

# Rounding settings

The paid working time can be rounded to the desired precision either up or down with the rounding settings. The settings can be defined in the working community settings or at a setting group level. 
![rGith10djk.jpg](https://support.nepton.com/hc/article_attachments/20237652298525)  
  
Rounding can be defined for an individual event, work start time or work end time, or the total work time per day.
Rounding of standalone events with an exceptional setting to event type rounding is not possible in case the events on that day are adjacent to each other. If events are adjacent to each other, the events are considered as a **shift,** which is always rounded as an entity. 
![](https://support.nepton.com/hc/article_attachments/20237652302237)  
  
You can specify the **rounding interval** for the desired rounding precision. The**rounding method** determines whether the rounding is going to happen up or down. For example, if the start time work has a 15-minute interval set for rounding up, the start time of work will be rounded to the nearest quarter-hour. 
If both event-based rounding and start and end work rounding are active simultaneously, event-based rounding won't affect the start and end work.
When the **normal** rounding method is chosen, the work hours are rounded to the nearest value within the specified interval, either up or down. You can also set an exceptional **rounding threshold** for the normal rounding rule. This allows you to define a minute value below which it rounds down and above which it rounds up. 
## Rounding of accruals, overtime and work rises
Rounding settings can be defined also for balances and overtime, either in the working community settings or at a setting group level. The settings can be found in section _Work hours > Accruals and overtime hours > Calculation settings_ > _Overtime_ or _Balance_. Also here you can choose the**rounding mode** that determines whether the rounding is going to happen up or down and the**rounding interval**. 
![](https://support.nepton.com/hc/article_attachments/20237652305181)
![](https://support.nepton.com/hc/article_attachments/20237629717789)
**Rounding threshold**
With the "Up" rounding mode, time is rounded up only once the threshold has been reached.
With the "Normal" rounding mode, the time is rounded down only under the threshold, rounded up otherwise.
With the "Down" rounding mode, the time is rounded down only under the threshold.
### Move the down rounded time that has been rounded with down mode to an accrual
In overtime settings, it is possible to transfer the time that has been rounded down with the **down mode** to an accrual. For example, if the rounding method is down to the nearest 15 minutes, and the person works 20 minutes of overtime, the amount of overtime would be rounded to 15 minutes, and the remainder, i.e. the rounded 5 minutes, would be transferred to the selected accumulation, for example the balance.
If, when rounding down, the division remainder is transferred to an accrual, the amount of additional work to be formed is not rounded.
The rounding settings for work rises can be found in the **Work rises** section of the working community settings or setting group settings.
### Rounding off additional work in overtime rounding
When rounding overtime, it is possible to ignore additional work. In this case, additional work is earned normally and rounding of overtime is done for 50% and 100% overtime without taking additional work into account.
If the overtime was rounded up to the next half hour without rounding up the additional work and 44 minutes of additional work and 10 minutes of 50% daily overtime are earned during the day, the rounding result would be as follows:
44 minutes of additional work  
30 minutes 50% overtime
This setting can be found in the working community settings and setting group settings in the section _Working hours > Accruals and overtime hours > Calculation settings > Overtime_. The default value of this setting in the work community settings is "Yes".
## Rounding of Emergency work
Event type "Emergency work" follows the compensation basis according to the Work Time Act. Emergency work is always compensated for at least 1 hour. For the part exceeding one hour, the emergency work is compensated according to the duration of the emergency work event. 
Emergency work can, if necessary, be rounded using event rounding. In the exception settings, it must be defined that the rounding applies only to the Emergency Work event type.
