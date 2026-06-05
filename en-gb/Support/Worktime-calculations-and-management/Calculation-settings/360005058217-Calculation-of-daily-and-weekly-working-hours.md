---
id: 360005058217
title: Calculation of daily and weekly working hours
url: https://support.nepton.com/hc/en-gb/articles/360005058217-Calculation-of-daily-and-weekly-working-hours
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- Ylityöviikon laskentamallit
- vuorokausiraja
- yleistyöaika
- overtime
- tes
- collective agreement
- daily and weekly working hours
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-11-28T09:02:52Z'
---

# Calculation of daily and weekly working hours

Overtime is accumulated on a daily basis, not per event, meaning all accrued overtime is summed together. After this, it is interpreted according to the settings whether it is 50% or 100% overtime. If rounding applies to the overtime, the rounding is formed temporally to the last overtime period. The exception to this is the 'Agreed 100% Overtime', which rounds independently and does not affect the other overtime calculations of the day.
A person’s daily and weekly working hours are determined based on the settings group associated with the person and the person’s work time percentage. The length of the working day and week used can be seen in the **Events Calendar** or in the **Events in table** view by clicking on the date.
![](https://support.nepton.com/hc/article_attachments/20545516878365) ![](https://support.nepton.com/hc/article_attachments/20545516879133)
When calculating working hours, regular working hours for a person are formed from those time entries that fall below the length of the workday and the workweek. In interpretation, regular working hours are scheduled so that they are compensated starting from the beginning of the workday as set in the settings. Regular working hours are compensated for subsequent events in chronological order. The scheduling of regular working hours can be directed by entering [assumed working hours](<https://support.nepton.com/hc/en-gb/articles/360002558617-Expected-work-times>) into the service.
The settings mentioned below can be found in the settings under **Work Hours > TES**.
For the portion exceeding regular working hours, the calculation first examines the length of the workweek. Working time is treated as exceeding the weekly working hours to the extent that it exceeds the value of the ‘TES work week length’ setting but still falls below the length of the workday.
Time exceeding the length of the workweek can be allocated to accruals or paid as overtime. If the time exceeding the workweek is compensated as overtime, then the time is compensated as weekly additional work up to the 'TES maximum hours of work per week**'** setting. See a more detailed description of additional work [here.](<https://support.nepton.com/hc/en-gb/articles/360002559438-Additional-work-formation>) Weekly 50% overtime is compensated up to the 'TES maximum weekly 50% overtime hours' setting. After this, the resulting weekly overtime is compensated with a 100% increase.
When the maximum weekly working hours have not been reached, weekly overtime can be set to accrue with the setting**'** Weekly overtime threshold if earned before TES max week length**'.** In this case, work that exceeds the weekly working hours is compensated as TES overtime when the threshold amount of work for the week is exceeded. In this case, no weekly additional work is formed. Threshold value must be smaller than TES work week length for it to have effect. This setting can be used in accumulating of overtime for part-time employees.
Working time is treated as exceeding the daily working hours to the extent that it exceeds the ‘length of the workday’ setting. Time exceeding the length of the day can be allocated to accruals or paid as overtime. If the time exceeding the workday is compensated as overtime, then the time is compensated as daily additional work up to the ‘TES maximum work day length’ setting. See a more detailed description of additional work [here](<https://support.nepton.com/hc/en-gb/articles/360002559438-Additional-work-formation>). Daily 50% overtime is compensated up to the 'TES daily 50% overtime compensated hours**'** setting. After this, the resulting daily overtime is compensated with a 100% increase.
Setting "Earn 100% overtime after weekly overtime" can be used to set when 100% overtime earning begins. If the setting is set to:  
-"No", overtime earning goes as per the settings.  
-"Yes", 100% overtime earning starts immediately after weekly overtime has been earned, regardless of the amount. For example if on Wednesday 3 hours of weekly50% has been earned, will all overtime be 100% on Thursday.  
-"TES maximum weekly 50% overtime hours" 100% overtime earning starts after the maximum amount of weekly 50% overtime has been earned. For example, if the maximum amount of weekly 50% overtime is 8h, will 100% overtime earning begin after the 8 hours of 50% weekly overtime has been earned. 
When the maximum daily working hours have not been reached, daily overtime can be set to accrue with the setting 'Daily overtime threshold if earned before TES max day length**'.** In this case, work that exceeds the daily working hours is compensated as daily TES overtime as soon as the time to be compensated for the day exceeds the threshold. In this case, no daily additional work or weekly overtime is formed. Threshold value must be smaller than maximum work day length for it to have effect. This setting can be used in accumulating of overtime for part-time employees.
The compensation for event types and their consideration in the calculation of the actual weekly working hours can be changed in the settings under **Work Hours > TES > Event types that contribute to work week.**
Note! By default, only paid event types are counted towards the workweek
If event type-specific settings have not been changed, the following paid event types are not counted towards the workweek:
  * Training
  * Union steward work
  * Travel time
  * Health care
  * Workplace health and safety work


## Reducing the maximum weekly working hours
The maximum weekly working hours can be reduced when there is a public holiday during the week, or when the person has absences. Absences that reduce the maximum weekly working hours are defined in TES settings under the title 'Extra time to be deducted from max week length on absence days' .
![](https://support.nepton.com/hc/article_attachments/20547615083293)
For example, if you want sick leave to reduce the workweek by 7 hours and 30 minutes according to the entry and to reduce the maximum working hours for the day by a total of 8 hours, the setting value for sick leave would be given as 30 minutes.
## Reducing the length of the workweek on a public holiday week
A public holiday can be set to reduce the weekly working hours as follows:
  1. According to the daily obligation. In this option, one day reduces the workweek by a maximum of 8 hours, even if the length of the day is longer
  2. According to the weekly obligation. In this option, the length of the workweek is divided by five (5). For example, with a 30-hour workweek, each public holiday reduces both the weekly working hours and the maximum weekly working hours by 6 hours. Additionally, in the TES settings, the setting Public and annual leaves shorten whole week first must be defined as ‘Yes’ so that the reducing effect of the public holiday is also processed on the weekdays preceding the public holiday
  3. According to the maximum weekly working hours. In this option, both the length of the workweek and the maximum weekly working hours are divided by five (5). For example, if there is a 30-hour workweek and a 40-hour maximum weekly working hours, then each public holiday reduces the weekly working hours by 6 hours and the maximum working hours by 8 hours.


The method of reduction can be defined in the settings of the work community or settings group under **Work Hours - > Public Holidays -> Public holidays shortens work week by**
![](https://support.nepton.com/hc/article_attachments/20550623302301)
In addition to the method of reduction, it must be defined how the weekly working hours are shortened. The reduction can affect the length of the workweek (TES work week length) and the maximum weekly working hours
![](https://support.nepton.com/hc/article_attachments/20550609007645)
Weekly overtime is compensated as additional work if the length of the workweek is exceeded, but the maximum weekly working hours are not exceeded. If the maximum weekly working hours are not shortened, weekly overtime is paid as additional work up to the maximum working hours, after which weekly overtime is paid. Detailed instructions for defining additional work can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002559438-Additional-work-formation>)
## Weekly Overtime Formation Before Completion of Weekly Hours
The collective agreement (TES) may interpret that weekly overtime is accrued even before the completion of weekly hours. With the setting ‘threshold for the formation of weekly overtime’, it can be directed that after a set amount of work, weekly overtime is earned regardless of the length of the workweek.
The collective agreement (TES) may also interpret that when certain event types occur, no weekly additional work is formed, but work done on a day off is compensated as weekly overtime. With the setting 'Collective labour agreement for the salaried employees in the real estate sector' > 'Event types which cause overtime on days off to be compensated as weekly overtime', these event types can be selected. In addition, the same functionality can be chosen for public holidays that shorten the workweek.
![](https://support.nepton.com/hc/article_attachments/20550623304221)
If overtime according to the collective agreement (TES) is accrued before the completion of weekly hours, this overtime can be set as separate from the weekly overtime with the setting 'TES overtime earned separately to weekly overtime'**.** In this case, overtime according to TES is calculated separately from weekly overtime, and it is possible to first earn overtime according to TES up to the weekly threshold and correspondingly weekly overtime.
When 'TES overtime earned separately to weekly overtime**'** is set to 'Yes' and there are absence days during the week that trigger overtime on the weekend according to the real estate sector TES rules, overtime for the weekend would be calculated as follows:
![](https://support.nepton.com/hc/article_attachments/20598137640605)
## The length of the workday/week and the maximum working hours
In interpretation, the length of the workday or workweek is considered fulfilled when the maximum working hours are filled, even if the length of the workday or workweek has not yet been met. After this, the working time is interpreted as overtime.
If the maximum working hours per day/week in the settings are shorter than the length of the workday/week, the maximum working hours are increased to match the length of the workday/week.
## Hour to hour -overtime contributes towards weekly obligation
By default no hour to hour time contributes to weekly obligation.
Also if the event type is set to not contribute towards weekly obligation then its hour to hour time won't contribute either regardless of what is set to these settings.
If needed, this setting can specify that hours exceeding regular time, which are compensated hour to hour, are counted toward weekly obligated work time in one of the following ways:
  * Both week and max work week length
  * Only work week length
  * Only max work week length
  * Only on non obligated days (with this setting, the hour to hour interpreted time is considered only in max work week length)

![](https://support.nepton.com/hc/article_attachments/32136911681309)
The week and max work week length are defined in the TES section under the following settings:
![](https://support.nepton.com/hc/article_attachments/32136925198877)
