---
id: 360002481617
title: Event overtime targeting
url: https://support.nepton.com/hc/en-gb/articles/360002481617-Event-overtime-targeting
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
- ylityökorvaus
- Ylityöohjaus kirjausta tehdessä
- ylityöohje
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2024-01-30T14:11:12Z'
---

# Event overtime targeting

Overtime is interpreted per working day, not per event, i.e. all interpreted overtime is added together.  
After this, it is interpreted according to the settings, whether it is 50% or 100% overtime.  
If overtime is subject to rounding, the rounding is based on the last overtime period.  
The exception to this is Agreed 100% overtime, which is rounded up independently and does not affect the rest of the day's overtime calculation.
Any hours exceeding regular working hours can be targeted to different accruals or salary in the event modification. It is also possible to choose not to compensate for the hours in excess of regular working hours. The settings can be done in the Worktime section in either the **Working Community** level or **Setting Group** level: **Worktime > Administration > Working Community / Settings Group Settings > Work hours > Accruals and overtime hours > Overtime**.
## Default overtime target
From the Overtime menu for event editing, you can preselect the default by setting the values to **Calculation settings - Overtime**. The settings can be specified separately for real-time recordings (work time terminal, mobile) or web recordings.
Defaults are defined for the basic part of the overtime and the increase part. If you want to compensate hour by an hour, select the compensation type for the base part. The increase part is defined as 'Not compensated.
If, on the other hand, you want to compensate for overtime, you must define the default type for both the basic part and the increase part.
If you want 'Hour to hour - balance' as the default target for overtime, define the settings as in this example:
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4413108053393)
If you want 'Overtime - Salary' as the default target for overtime, define the settings as in this example:
![mceclip4.png](https://support.nepton.com/hc/article_attachments/4413122635281)
Overtime calculations are done based on the setting group settings. The default overtime target can be changed for each event by opening an event entry in the user's calendar view and selecting Overtime options.
![mceclip5.png](https://support.nepton.com/hc/article_attachments/4413108448145)
The options for overtime compensation types that are shown in event edit can be modified in **Accruals and Overtime Hours - Overtime - Visible overtime options on event creation**.
## Various overtime targets
Here are some types of compensation as an example. There are various of different types of compensations available.
**Default  
** The hours are targeted as per the user's setting group settings.
**Not compensated**  
Hours exceeding regular working hours are not compensated.
**Hour to Hour - Bank**  
Hours exceeding regular working hours are simply targeted to bank.
**Hour to Hour - Salary  
** Hours exceeding regular working hours are simply targeted to salary.
**Overtime - Balance  
** Hours exceeding regular working hours are targeted to balance with overtime increase.
**Overtime - Bank**  
Hours exceeding regular working hours are targeted to bank with overtime increase.
**Overtime - Salary**  
Hours exceeding regular working hours are targeted to salary with overtime increase.
**Overtime - Base hours to Balance, overtime hours to Salary**  
Hours exceeding regular working hours are targeted to balance for the base part, and only the overtime increase (50% for example) is paid in salary. 
**Overtime - Base hours to Bank, overtime hours to Salary**  
Hours exceeding regular working hours are targeted to bank for the base part, and only the overtime increase (50% for example) is paid in salary. 
**100% overtime compensation**
Forces all time in excess of regular working hours to be 100% overtime. Additional work will be forced to 100% daily overtime, 50% daily/weekly overtime will be forced to 100% overtime. This does not affect the calculation of the maximum limit of 50% weekly overtime, 50% weekly overtime forced to 100% overtime will be taken into account. when looking at the threshold. This setting should only be used in compelling situations if other settings do not interpret to 100% overtime.
