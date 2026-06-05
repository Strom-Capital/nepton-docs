---
id: 360008777997
title: Rendering options
url: https://support.nepton.com/hc/en-gb/articles/360008777997-Rendering-options
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- Työajan kohdennus vuorokauden vaihteen ylittyessä
- Työtapahtuman oletusalku- ja loppuajankohta
- oletustyöaika
- Tapahtumatyypin oletusajankohta
- Tapahtuman oletuskellonaika
- Tapahtuman oletusaika
promoted: false
updated_at: '2026-05-04T09:18:45Z'
edited_at: '2026-01-30T14:04:55Z'
---

# Rendering options

Rendering options can be set either in working community level or setting group level. Settings can be found in **Worktime > Administration > Working community settings / Setting groups > Work hours > Rendering options. **
![](https://support.nepton.com/hc/article_attachments/33609136850589)
The following settings can be configured here:
  * Whether basic pay information is shown in the calendar or not (working community level only). By default, the setting is always on. If this is set to no, the calendar view is simplified and the interpretation of working time is not displayed in the view.
  * On which calendar day the events and the interpretation of working hours are shown. Options are:
    1. Salary is shown on the day it is earned.
![](https://support.nepton.com/hc/article_attachments/33609122675485)
    2. Salary earned is shown on the day the shift starts.
![](https://support.nepton.com/hc/article_attachments/33609122677021)
    3. Salary earned is shown on the day the shift ends.
![](https://support.nepton.com/hc/article_attachments/33609136854557)
Default value for setting is 'Salary earned is shown on the day the shift starts'. If day has planned work shift it is used when determining on which day events are shown. In the example below setting value is 'Salary earned is shown on the day the shift ends'. Work event continues to the next day but planned shift determines on which day events are shown.
![](https://support.nepton.com/hc/article_attachments/33609136857373)
It is worth noting that the selected setting also affects the day on which the weekly rest compensation is calculated. If the setting 'Salary earned is shown on the day the shift ends' is used, the interpretation of events recorded at the end of the week will always be transferred to the following day - and following week. In order for such event entries to be taken into account in the calculation of the weekly rest compensation, the weekly rest compensation is not formed until the following week (usually on Monday).
  * In addition, you can specify the default business hours that the service suggests when creating a new event. When a new event is created, it automatically has the start and end times set here. The user can change the default times for each event. Unless otherwise specified, the service suggests a default start time of 08:00 on current day and an end time of 16:00 on current day.
  * Default business hours can be set for each event type separately. This can be done by setting the hours for each event type in the Event type specific default start and end times - section. First the event type that requires to have specific business hours is selected from the dropdown and Add - button is clicked. After that specific start and end times can be set for this event type.


![](https://support.nepton.com/hc/article_attachments/33609122680605)
