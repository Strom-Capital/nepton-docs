---
id: 360002558417
title: Defining the length of work day
url: https://support.nepton.com/hc/en-gb/articles/360002558417-Defining-the-length-of-work-day
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- NEPTONNEEDSREVIEW
- työtuntimäärä
- työajanraja
- oletustyöaika
- työaikamuutokset
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-03-11T11:02:42Z'
---

# Defining the length of work day

The length of the work day can be set in Worktime section either in Working community or Setting group level. The settings can be found in **Worktime > Administration > Working community / Setting group settings > Workhours > Length of work day.**
![](https://support.nepton.com/hc/article_attachments/34553925403037)
## Set length of work day
The length of the workday is defined by each weekday separately. If you do not want to specify the length of the workday for the day (for example, in situations where a person never works on Saturdays), you can leave the setting empty for that day.
It is recommended to set the length of the working day via the validity function (small calendar button next to the setting). This allows you to set the Valid from and Valid until dates.
![](https://support.nepton.com/hc/article_attachments/34553927759517)  
If this is the first time setting the workday length, it can be set without start date (always valid) or from wanted date onwards.  
![](https://support.nepton.com/hc/article_attachments/34553927762589)
If an existing value is to be changed, you must first end the old value by setting the date to Valid to -field. To add a new value, click Add setting value. The new value automatically takes effect on the day following the end of the previous value. In this way, the changes do not affect the past worktime calculations.
If you want to set an exception to the length of the working day, for example a shorter day than usually on New Year's Eve, you need to add a setting exception for that day. More detailed instructions and examples can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002560677>).
![](https://support.nepton.com/hc/article_attachments/34553925411485)
A workday length exception setting can also be set by [mass entering](<https://support.nepton.com/hc/en-gb/articles/360002560837>).
## Planned shift determines the length of the workday
The Planned event types that override workday length setting allows you to specify that the planned shift determines the workday length on days when a shift is planned for the day. This setting can be set at the Working Community level in the menu **Work time > Administration > Working Community Settings > Shifts.** If the workday length comes from the planned shift, there is no need to specify the length of day in the setting group.
## Day-level exception also sets maximum work day length
The setting "Day-level exception also sets maximum work day length" can be used to determine whether the daily TES maximum work time changes in a situation where an exception has been made to the length of a person's working day in the calendar view for one day. If the setting is "yes", the TES maximum working time changes by the amount of the exception made.
