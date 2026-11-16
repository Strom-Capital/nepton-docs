---
id: 4417295059985
title: Overtime calculation basic settings
url: https://support.nepton.com/hc/en-gb/articles/4417295059985-Overtime-calculation-basic-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- vrk-ylityö
- ylityöleikkuri
- ylityöohje
promoted: false
updated_at: '2026-06-29T10:27:26Z'
edited_at: '2026-06-29T10:27:26Z'
---

# Overtime calculation basic settings

The calculation of overtime in the service is affected by a large number of settings and they can still be fine-tuned with setting exceptions.
Instructions on making basic settings for length of work day and TES work week length, see [Defining the length of work day](<https://support.nepton.com/hc/en-gb/articles/360002558417>) and [Defining the length of work week](<https://support.nepton.com/hc/en-gb/articles/360002558537>).
This article describes the main settings that affect overtime calculation and can be found in Working Community - or Settings Group Settings under **Work hours >TES**, unless otherwise noted.
## TES maximum working time
TES maximum working time determines the overtime limit for both daily and weekly overtime.
Settings can be made in either Working Community - or Settings Group settings under Work hours >TES.
More on the calculation of additional work in article [Additional work, formation](<https://support.nepton.com/hc/en-gb/articles/360002559438>) and overtime in article [Calculation of daily and weekly working hours](<https://support.nepton.com/hc/en-gb/articles/360005058217>)
### TES maximum work day length
Settings are made for each day of the week separately.
The time between the length of the work day and the maximum work day length is, by default, additional work, unless other settings limit the amount of additional work per day.
When daily working hours exceeds the maximum work day length, daily overtime begins to form.
![](https://support.nepton.com/hc/article_attachments/33384368919837)
### TES maximum hours of work per week
The time between work week length and maximum hours of work per week is, by default, additional work, unless other settings limit the amount of additional work per week.
When weekly working hours exceed the maximum hours of work per week, weekly overtime begins to form.
![](https://support.nepton.com/hc/article_attachments/33384407509789)
## Daily overtime
![](https://support.nepton.com/hc/article_attachments/35449340776221)
**Maximum additional work per day**  
Determines maximum amount of additional work per day. Can affect weeks with public holidays, sick leaves or other absences.
**TES daily 50% overtime compensated hours**  
According to Working Time Act first 2 daily overtime hours are compensated with 50% increased salary and hours after that are compensated with 100% increased salary. This is also the default setting.
Collective agreements might have different definitions for daily overtime. 
**Earn 100% overtime after weekly overtime**  
When weekly overtime has been earned during the day and the TES maximum working hours per day are exceeded, the daily overtime is compensated at 100% instead of 50%. Some TES' say that in such a case a 100% increased salary is earned.
It is also possible to choose that the 100% increased salary is earned only after TES maximum weekly 50% overtime.
![](https://support.nepton.com/hc/article_attachments/35449317309469)
**Calculate agreed overtime towards maximum work day length**  
Setting is used when events which behave like agreed overtime are recorded. These events are not in use by default but can be implemented by creating new event type which behaves like agreed overtime.
Example: work day length is 7 h 30 mins and TES maximum work day length 8 h. 7 h 30 mins is recorded as work and 30 mins is recorded as agreed overtime. Maximum work day length is reached if this setting is "Yes".
## Weekly overtime
![](https://support.nepton.com/hc/article_attachments/35449317309725)
**Maximum additional work per week**  
Determines maximum amount of additional work per week. Can affect weeks with public holidays, sick leaves or other absences. Once the threshold is reached, weekly overtime earning is earned instead of additional work.
**TES maximum weekly 50% overtime hours**  
According to Working Time Act weekly overtime is compensated with 50% increased salary. Collective agreements might have different definitions for weekly overtime. This setting determines maximum amount of weekly 50% overtime.
**TES maximum weekly 50% overtime hours per day**  
Determines maximum amount of 50% weekly overtime hours per day. 
**Earn weekly overtime on work days without a planned shift / obligation**  
If work day length is not set for day or day does not have planned shift, weekly overtime is earned when working on that day. If set to 'Yes', work done on a day off is always weekly overtime and does not constitute additional work.
**Weekly overtime on public holidays that shorten work week counted towards overtime limits**  
Determines if weekly overtime on public holiday affects also limits of weekly overtime later on the same week.
Example with setting in use: 6 hours of 50% weekly overtime on public holiday and TES maximum weekly 50% overtime hours is 8 hours. 2 hours of 50% of weekly overtime is earned before earning 100% weekly overtime.
**Daily additional earned over the additional rise threshold contributes to weekly additional rise threshold**  
0% additional work always contributes to threshold set in "TES additional work rise percentage - Only earn after total weekly hours". This setting determines if additional work with rise (e.g. 50%) also contributes to that threshold. Example below uses the following additional work rise settings.
![](https://support.nepton.com/hc/article_attachments/35449317309981)
Setting value "No" or "Not set". 5 h and 30 mins of additional work is needed on Saturday before weekly additional rise threshold is reached. During the past four days there has been 32 h and 30 mins of work from which 2 h is 0% additional work and 30 mins is 50% additional work. 50% additional work does not contribute to weekly additional rise threshold so threshold of 37 h and 30 mins is 5 h and 30 mins away.
![](https://support.nepton.com/hc/article_attachments/35449317310621)
Setting value "Yes". 5 h of additional work is needed on Saturday before weekly additional rise threshold is reached. During the past four days there has been 32 h and 30 mins of work from which 2 h is 0% additional work and 30 mins is 50% additional work. 50% additional work contributes to weekly additional rise threshold so threshold of 37 h and 30 mins is 5 h away.
![](https://support.nepton.com/hc/article_attachments/35449340782877)
## Sunday overtime
**Sunday overtime start offset**  
The time and allocation value from which Sunday overtime begins to accumulate can be defined. The entered time and allocation value together determine to which day the Sunday overtime is allocated.
**Maximum 50% Sunday overtime on Sundays and public holidays**  
Determines maximum amount of 50% overtime on Sunday. If this setting has any value, Sunday overtime is earned when working on Sundays and public holidays. If collective agreement states that Sunday overtime is 100% compensated, then value of this setting is set to 0 minutes.
**Threshold calculation mode**  
It can be defined how the fulfilment of the 50% Sunday overtime threshold is checked. The threshold used is the value defined in the setting "Maximum 50% Sunday overtime on Sundays and public holidays". When the threshold is full, all overtime exceeding it is counted as 100% Sunday overtime. The Daily setting checks the threshold daily, allowing 50% Sunday overtime to accumulate on multiple days. By calendar week setting reviews the entire calendar week. The default value works the same way as the Daily value.
**Sunday overtime earned on public holidays after weekly obligation fulfilled**  
It can be defined whether Sunday overtime on public holidays is earned only after the weekly obligation is fulfilled.
**Holidays earning Sunday overtime**  
It can be defined from which public holidays Sunday overtime is earned. Public holidays are inherited from the Working community settings (Working community settings > Work Hours > TES), but they can be modified by setting group if necessary.
![Screenshot 2026-03-25 104430.png](https://support.nepton.com/hc/article_attachments/34877182150045)
## TES overtime
TES overtime is formed when:
Length of work day is exceeded, TES maximum work day length is not exceeded and work is not additional work.
Length of work week is exceeded, TES maximum hours of work per week is not exceeded and work is not additional work.
Typically TES overtime is formed when working on Saturdays on a week which has public holiday on weekday. 
Setting: Hour to hour -overtime contributes towards calculating collective agreement overtime:
This setting determines whether hour to hour overtime already recorded during the day or week is included when deciding if overtime (before the TES maximum weekly lengths is reached) counts as TES overtime or not.
## Overtime paid with fixed salary
If overtime needs to be displayed without percentage compensation in the calendar, you can enable a fixed overtime compensation. This is done with the setting "Overtime paid with fixed salary".
![](https://support.nepton.com/hc/article_attachments/37221594820509)
By default, the setting is off, in which case overtime is interpreted and displayed with compensation percentages according to other settings in the calendar. If the setting is set to "Setting on", the presentation of overtime in the calendar view changes. Overtime is displayed under the titles "Overtime 1" and "Overtime 2".
![](https://support.nepton.com/hc/article_attachments/37221607402397)
"Overtime1" is 50% overtime and "Overtime2" is 100% overtime, meaning that overtime is picked up for salary integration in the same way as 50% and 100% overtime normally. Overtime is still generated according to other TES settings, meaning that Overtime1 and Overtime2 can be earned either according to the settings or time-based by making definitions in the "Times when 50% overtime is not earned" section.
## Times when 50 percent overtime is not earned
With this setting it is possible to set times when 50% overtime is converted into 100% overtime. Setting takes effect on the day work is [rendered](<https://support.nepton.com/hc/en-gb/articles/360008777997>). If Event rendering setting is default "Salary earned is shown on the day the shift starts", Monday has settings shown below, work starts on Monday and continues overnight, then setting of Monday will affect also on Tuesday until 07:00. If 50% overtime is earned during this time, it will be converted into 100% overtime.
The example below has no settings on Tuesday. If work _starts_ on Tuesday, settings won't be applied. 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/5511945639709)
