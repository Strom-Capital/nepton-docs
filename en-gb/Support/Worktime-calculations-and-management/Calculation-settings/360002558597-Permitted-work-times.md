---
id: 360002558597
title: Permitted work times
url: https://support.nepton.com/hc/en-gb/articles/360002558597-Permitted-work-times
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
updated_at: '2026-10-09T07:36:13Z'
edited_at: '2026-10-09T07:36:13Z'
---

# Permitted work times

Permitted work times define the times outside of which work is not considered working hours. Permitted work times can be determined either in settings or from a planned work shift.
In this article, we describe the possible definitions for permitted work times.
## Setting permitted work times 
Permitted work times can be defined in the Worktime section either in the Working community settings or Setting groups level settings in the menu under **Worktime > Administration > Working community / Setting group settings > Work hours > Permitted work times. **The first setting determines whether permitted working times are used at all. The "Enabled" setting can be used to prevent the settings from being inherited from a higher setting group level to a lower level if you do not want to use permitted work times at this level.
![](https://support.nepton.com/hc/article_attachments/30081342612637)
There are two ways to set the permitted work times in the settings. The setting methods are "Day the shift belongs to" and "Days the shift overlaps". If no value is set, the "Days the shift overlaps" setting is used.
### Setting method: Day the shift belongs to
We recommend using the "Day the shift belongs to" setting. This is a newer way (released on March 8, 2025) to define permitted work times, and with this setting method, the validity periods of permitted work times are defined with a single validity setting. The permitted work times are therefore valid every day of the week by default. Exception settings for validity periods, such as date or event type -based exceptions, can still be defined with this setting method.
The most significant difference from the older method of defining permitted work times (Setting method: Days the shift overlaps) is the utilization of the validity periods according to the day to which the [interpretation of the working hours also belongs](<https://support.nepton.com/hc/en-gb/articles/360008777997>).
![](https://support.nepton.com/hc/article_attachments/30081374093341)
The times of the permitted work times are defined on one or two lines (if there are two different sets of permitted work times in a day), and they then apply to each day of the week. [Exception settings](<https://support.nepton.com/hc/en-gb/articles/360002560677>) define exceptions to this pattern. For example, an exception can be defined for the "in use" setting that the permitted work times are not in use on Saturdays and Sundays. In this case, the permitted work times only apply to weekdays.
![](https://support.nepton.com/hc/article_attachments/30081342616605)
Multiple exception settings can also be made for example depending on the date, event types used, and overtime targets. More detailed instructions for defining different exception settings can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002560677>).
#### Example 1 - Exceptional permitted work times on public holidays
For example, let's take a case where the permitted work times are normally Mon-Fri 07:00-18:00. On Saturdays and Sundays there are no permitted work times at all (settings as described in the previous paragraph). However, on public holidays we want to limit the permitted work times to only be between 10:00 and 15:00. In this case, the default value of the setting is set to 07:00-18, the permitted work times are disabled on Saturdays and Sundays, and the following exception is made to the 'Valid' setting:
![](https://support.nepton.com/hc/article_attachments/30081342618013)
With these specifications, the permitted work times are Mon-Fri 7am-6pm and on holidays 10am-3pm.
#### Example 2 - Permitted work times over two days
When the permitted work times apply to two different days, the "Event rendering" setting has a large impact on the interpretation. For example, if you want events to be displayed on the day the shift ends:
![](https://support.nepton.com/hc/article_attachments/30081342619421)
And we want to set the permitted work times to be 23:00-07:00, i.e. to apply to two days. In this case, the 'valid' settings for the permitted work times would be defined as being valid from 23:00 on the **previous day** and ending at 07:00 on the**current day** :
![](https://support.nepton.com/hc/article_attachments/30081374097565)
This will allow the permitted work times to be interpreted correctly in line with the work event rendering:
![](https://support.nepton.com/hc/article_attachments/30081374098717)
If the permitted work times were set to 23:00 on the current day and 07:00 on the next day, nothing would be interpreted from the work entry made for the time period of 23-07, because it would be outside the permitted work times. On the other hand, if the event rendering settings were set to show events on the day the shift starts, the correct definition of permitted work times would be 23:00 on the current day - 07:00 on the next day.
### Setting method: Days the shift overlaps
Although a newer method for determining permitted work times has been released, the older method "Setting method: Days the shift overlaps" can still be used in to determine permitted work times.
Permitted work times are defined to start and end per weekday. In the definition, the start time is selected, and whether the time is for the previous, current, or next day.
![](https://support.nepton.com/hc/article_attachments/20578918511773)
It is possible to set two different values for the valid times. This is necessary, for example, when working across the change of day. The first valid value goes into the upper fields, and the subsequent values go into the lower fields. By using two values, the permitted work times can be split for the day, for example, so that the permitted work times are from 06:00-11:00 and 16:00-21:00.
![](https://support.nepton.com/hc/article_attachments/20578856070045)
The setting "or permitted work time duration if the end time depends on start time:" can be used to specify that the permitted work time has a certain duration, after which work is no longer permitted. In this case, the times themselves vary depending on when the work starts.
### Overtime targets that permitted work times can be defined for
In the permitted work times settings, under the section **Limit when overtime pay target** , it is defined in which overtime targets the permitted work times are considered and correspondingly where they are not considered. If no restrictions are defined, all work hours exceeding the permitted work times are restricted.
If the type of overtime target is not restricted, the overtime target is used to define how the time exceeding regular work hours is to be compensated. The overtime target is saved as part of the event and can be seen under the Overtime in the event addition or editing window.
![](https://support.nepton.com/hc/article_attachments/30086645174557)
### Event type specific overrides
![](https://support.nepton.com/hc/article_attachments/20578918516765)
The validity of permitted wor times can also be defined based on the event type according to the overtime target. For example, if **Limit when overtime pay target** is valid for the target **overtime - to salary** , but you do not want the permitted work times to be valid when the event type is Work. This can be done with an event type-specific override, as shown in the image above.
### Allow work before and after shift
![](https://support.nepton.com/hc/article_attachments/20578918518941)
For specified event types, it is possible to allow a certain amount of permitted time that can be earned before and after the shift. The permitted time is earned even if the allowed working hours would otherwise restrict this. In the above example, with the event type ‘Work,’ it would be possible to earn paid time 2 hours before the shift and 3 hours after the shift. However, the 'Work' event entry must partially fall within the shift time so that work time is allowed according to this setting before and after the shift.
Note! The setting restricts the earned time before and after the shift even if the allowed work hours are not valid.
## Setting an exception to the permitted work times for a single day
Permitted work times can be edited on a daily basis if there is a need to extend the permitted work times for a single day for one person. The editing is made directly from the individual’s calendar view by clicking on the desired day’s date and selecting **Permitted work times** from the menu that opens.
![](https://support.nepton.com/hc/article_attachments/30086628646045)
After clicking **Permitted work times** , a new window opens up. In this window you can define exceptional permitted work times for that day. When using the exception setting for a single day, the permitted work times must always be set using the times ‘On current day’
![](https://support.nepton.com/hc/article_attachments/30086628647325)
For example, if the permitted work times from the settings group are 7 am to 6 pm, but in an exceptional situation you want to allow work from 6 am to 8pm, set the desired start and end times in the exception window and press 'Save exception'.
By selecting **Save exception** , the differing setting is saved, and the set exception can be seen in the calendar view by clicking the date.
![](https://support.nepton.com/hc/article_attachments/30086628648733)
## Setting permitted work times from a scheduled shift
In addition to the permitted work times defined by the settings, permitted work times can be set to based on shifts. The settings can be found at the Working community or setting group level in the menu **Worktime > Administration > Working community / Setting group settings > Shifts**. 
With the settings **Allowed amount of offset in the beginning of work shift** and **Allowed amount of offset at the end of planned shift** , you can control from which time work hours can be earned before or after a shift.
![](https://support.nepton.com/hc/article_attachments/26620860369693)
In addition to the permitted work start/end time settings, also the **Permitted work times** functionality needs to be enabled in the **Work hours** section and the necessary **Limit when overtime pay target** settings in the same section need to be set. For more information on the overtime pay targets, please see [this](<https://support.nepton.com/hc/en-gb/articles/360002558597-Permitted-work-times>) article.
## Setting permitted work times for individual shifts
Permitted work time limits can also be defined directly in the Shift Planning view for individual shifts. This functionality is available when creating a single shift and can also be used when editing existing shifts.
The fields **Permitted work time start offset** and **Permitted work time end offset** are available as separate fields in the shift details.  
![](https://support.nepton.com/hc/article_attachments/39777405562013)  
An offset for the permitted work times can be defined in both fields in relation to the shift start and end times. The offset can be set in two different ways:
  * A minute-based HH:MM offset relative to the shift start or end time (e.g. -10 and +10)
  * A specific time in hh:mm format, where the permitted work time starts or ends at the defined time (e.g. 06:50–14:10)


For example, for a morning shift from 07:00 to 14:00, setting the **Permitted work time start offset** field to **-10** will make the allowed working time begin 10 minutes before the shift starts, at 06:50. Setting the **Permitted work time end offset** field to **+10** will make the allowed working time end 10 minutes after the shift ends, at 14:10. A value of **0** means that the allowed working time exactly matches the scheduled shift time.  
  
An example with the same shift but with offsets using the minute-based HH:MM format with the same result in permitted work times:  
![](https://support.nepton.com/hc/article_attachments/39777405562909)  

The **Permitted work time start offset** and **Permitted work time end offset** settings can also be used in shift types within shift calendars. When defined at the shift-type level, the allowed working time offset always applies to that specific shift type.
The principle for defining offsets in shift calendar shift types is the same: separate fields are available for both the start and end time offsets when creating and editing shift types.  
  
![](https://support.nepton.com/hc/article_attachments/39779107638173)
  
Permitted work times defined for an individual shift in Shift Planning override the offsets configured in the Worktime settings under **"Permitted work start time comes from planned shift"** and **"Permitted work end time comes from planned shift"**. If the permitted work time offset fields for an individual shift are left empty, these settings will continue to be applied as before.
