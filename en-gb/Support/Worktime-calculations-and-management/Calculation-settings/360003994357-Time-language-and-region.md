---
id: 360003994357
title: Time, language and region
url: https://support.nepton.com/hc/en-gb/articles/360003994357-Time-language-and-region
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- aikaero
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2021-11-19T11:20:24Z'
---

# Time, language and region

Service can be defined the default language and time zone for a person, setting group or working community. By setting the time zone, real-time job starts and stops functions of service can also be used in organizations, where work is being done in different time zones. When a supervisor or other person views the calendar of a person working in a different time zone, they also see real-time recorded events in that time zone. The calendar does not change the times according to the viewer's time zone.
## Settings
The language and time zone to be used can be defined in the person settings (Worktime -> Administration -> Persons -> Time, language and region), in setting group settings (Worktime -> Administration -> Setting groups -> Action: Setting group settings -> Time, language and region) or in the working community settings (Worktime -> Administration - > Working Community Settings-> Time, language and region).
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4411334332177/mceclip0.png)
## Defaults
The default language in the service is Finnish and the time zone is Finnish time zone.
## Time zones and event creation at the terminal
  * If an event is recorded using a terminal, the start and end times of the event are saved in to Nepton based on the time zone and time set in the posting terminal. If an employee momentarily travels to a different time zone, he or she can log his or her work time according to local time.
  * If an event is recorded via Current Status view or Mobile, the start and end times of the event will be saved in to Nepton according to the settings defined at the Working Community settings / Setting group level. This ensures the correctness of the working time entries. For this reason, it is recommended that the time zone of a person in Nepton always is set to the correct current location.


Note: If you change the time zone retrospectively, the change will not affect events that have already been recorded.
## Restrictions
Only one time zone per day can be valid in one day.
API: If you send times in UTC zero format, they will be converted to local times based on your time zone setting (2019-12-25T10:11:12Z).
When [persons are imported](<https://support.nepton.com/hc/en-gb/articles/360003762577-Person-Import>) without a service usage language, the language set in the working community settings does not affect the language of the person's service usage language. If persons are imported without a service usage language, the default language of the customership is used, which is Finnish by default. Changing the default language can be requested from Nepton Customer Service.
