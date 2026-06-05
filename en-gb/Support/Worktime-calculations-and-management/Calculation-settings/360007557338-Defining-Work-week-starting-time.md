---
id: 360007557338
title: Defining Work week starting time
url: https://support.nepton.com/hc/en-gb/articles/360007557338-Defining-Work-week-starting-time
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
updated_at: '2026-04-14T07:00:14Z'
edited_at: '2026-04-14T07:00:14Z'
---

# Defining Work week starting time

Work week starting time can be defined in Nepton. Work week starting time affects [work rises](<https://support.nepton.com/hc/en-gb/articles/360002560978>), [Weekly rest time compensation](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) and how overtime is calculated.
Setting can be found in **Worktime > Administration > Working community settings / Setting groups > Work hours > TES**
**Work week starting day –** setting defines, what day starts the week. If no value is set, the default is Monday.
**Work week starting time** – setting defines, what time the work week begins. It also defines what time the day changes to next. 
**![](https://support.nepton.com/hc/article_attachments/20998076555037)**  
If work week starting time is set to ‘00:00’ the work week and each day of the work week starts always at 00:00. Then also each day is considered to start at 00:00 and finishes at 24:00.
Monday 00:00 – 24:00
Tuesday 00:00 – 24:00
Wednesday 00:00 – 24:00
Thursday 00:00 – 24:00
Friday 00:00 – 24:00
Saturday 00:00 – 24:00
Sunday 00:00 – 24:00
= 1 week
If work week starting time is set to '07:00', the calculation is considered as follows:
Monday 07:00 – 07:00 (at Tuesday morning)
Tuesday 07:00 – 07:00 (at Wednesday morning)
Wednesday 07:00 – 07:00 (at Thursday morning)
Thursday 07:00 – 07:00 (at Friday morning)
Friday 07:00 – 07:00 (at Saturday morning)
Saturday 07:00 – 07:00 (at Sunday morning)
Sunday 07:00 – 07:00 (at Monday morning)
Depending on if day starts before or after the noon (12:00), also affects to the **Work week/day starting time.**
If your work week starts on Sunday at 22:00 for example, then:
  * Your first day of the week is MONDAY/next day (because the start time is after noon), but your Monday starts at 22:00 on SUNDAY and finishes on Monday 22:00.
  * The second day of the week is Tuesday but starts on Monday at 22:00 and ends on Tuesday at 22:00. And so on…
  * So, shifts starting on Sunday at 23:00 will display on Monday and calculated as a Monday shift and the week just starting.
  * Shifts starting before 22:00 on the Sunday will display on Sunday and calculated as a Sunday shift for the week just ending.


If your work week starts on Sunday at 04:00 then:
  * Your first day of the week is SUNDAY/same day (because the start time is before noon) and is from Sunday 04:00 to Monday 04:00.
  * Your second day of the week is Monday, starting from Monday 04:00 to Tuesday 04:0 And so on…
  * So, shifts starting on Sunday before 04:00 will be displayed and calculated as Saturday shifts for the week ending.
  * Shifts starting on Sunday after 04:00 will be displayed and calculated as Sunday shifts for the week starting.
  * Shifts starting on Monday before 4AM will be displayed and calculated as Sunday shifts.
