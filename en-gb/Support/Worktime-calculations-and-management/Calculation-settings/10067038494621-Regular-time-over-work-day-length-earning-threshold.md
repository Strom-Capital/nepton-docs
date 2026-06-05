---
id: 10067038494621
title: Regular time over work day length earning threshold
url: https://support.nepton.com/hc/en-gb/articles/10067038494621-Regular-time-over-work-day-length-earning-threshold
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
edited_at: '2024-10-03T12:25:53Z'
---

# Regular time over work day length earning threshold

In Nepton's settings, under [the length of work day](<https://support.nepton.com/hc/en-gb/articles/360002558417>), there are settings "Regular time over work day length earning threshold" (Worktime > Administration > Working community/Setting group settings > Work hours > Length of work day), which can be defined according to [event types](<https://support.nepton.com/hc/en-gb/articles/360002520778>). The setting's is typically used with event types that normally accumulate only regular work hours up to the length of the work day, for example sick leave and travel time. The setting can for example, allow 9 hours of working time to be earned from sick leave, even if the length of the work day is 7 hours 30 minutes. The setting limits the maximum amount of work time that can be earned. Another typical use for the setting is Travel time, when time exceeding regular work hours needs to be [directed in the balance](<https://support.nepton.com/hc/en-gb/articles/360002559737>).
## Settings
The setting will display a field for each event type that is in use in the deployment.
![](https://support.nepton.com/hc/article_attachments/22005059119645)
**Regular time over work day length earning threshold - "Event type"** \- Enter the value that
is the maximum work time threshold for earning with this event type. For example, if 2 hours worktime should be earned from travel time after the regular time is filled, would the value be 2 hours + the length of the workday (7,5 hours in this case) = 9,5 hours. In this case, travel time can be earned until the day's work hours have reached 9.5 hours. 
**Of which is unpaid** \- the value defines, how many hours are unpaid before worktime is earned after the length of work day.
The setting doesn't enable earning a set amount of hours per event type, but it limits earning per event type when the day's work hours have reached set limit. If there are also hour to hour work done on top of regular hours, earning for event type decreases accordingly.
## Use case examples
Few examples of how this setting can be used can be found below.
### Travel time
By default, "travel time" only accumulates regular hours. If work time should also be earned after the day's obligation has been fulfilled, you must set the correct value for the setting. As an example, a case where you can earn 3 hours of travel time on weekdays and 12 hours on weekends to balance. The length of the working day is 7.5 hours, so the settings would be set as follows:
![](https://support.nepton.com/hc/article_attachments/22005059125917)
Then, on work days travel time can't earn worktime after the work hours have reached 10,5 hours and at the weekends 12,5 hours.
![](https://support.nepton.com/hc/article_attachments/22005029209373)
  * Thursday 10.10.: First a full work day of 7,5 hours has been done, which follows by 2 hours of travel time. No hours have been limited, because the total hours of the day don't exceed 10,5 hours.
  * Friday 11.10.: First a full work day of 7,5 hours has been done, which follows by 5 hours of travel time. Only 3 hours are earned from travel time, because by then the maximum hours of 10,5 have been reached.
  * Saturday 12.10.: The day has only travel time 14h. Only 12 hours go to balance as that is the maximum set in the setting.


### Sick leave
By default, "sick leave" only accumulates regular hours. If work time should also be earned after the day's obligation has been fulfilled, you must set the correct value for the setting. As an example, a case where the length of the work day is 7,5h, but sick leave can be earned up to 9 hours. One hour is unpaid time.
![](https://support.nepton.com/hc/article_attachments/22005715543197)
  * Regular time over work day length earning threshold = 9:00
  * Of which is unpaid = 1:00


Sick leave earning would go as follows:
  * 07:00 - 15:00 -> 7,5 regular hours (includes 30 min unpaid lunch break)
  * 15:00 - 16:00 -> 1h unpaid time as set
  * 16:00 - 17:00 -> 1h regular time over work day length earning. Worktime can be earned up to 9 hours.


![](https://support.nepton.com/hc/article_attachments/22005715545245)
