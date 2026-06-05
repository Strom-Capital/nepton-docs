---
id: 360002560618
title: Exceptional entries settings
url: https://support.nepton.com/hc/en-gb/articles/360002560618-Exceptional-entries-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- varoitusmerkki
- kolmio
- huomiokolmio
- poikkeukselliset kirjaukset
promoted: false
updated_at: '2026-04-22T13:10:53Z'
edited_at: '2026-04-22T13:10:53Z'
---

# Exceptional entries settings

With the management of exceptional entries, it is possible to highlight situations that should be paid special attention to. These situations are highlighted with an 'Exceptional entry' attention triangle in the work time calendar view, mobile view, approval view and some reports. Please note that the attention triangle of some exceptional entries does not appear in the calendar for future dates. 
Some of the exceptional entries are shown only in the [Exceptional entries](<https://support.nepton.com/hc/en-gb/articles/360002548837>) -report. These type of exceptional entries have the mention 'only shown in exceptional entries report' in the settings.
When the events have been approved, the attention triangle is no longer displayed in the calendar or table view.
The exceptional entries notifications are intended to draw the attention of the employee and the approver of events to a situation that deviates from normal. The settings for exceptional entries can be defined either in the Working community settings or at a setting group level. The settings can be found in **Worktime** **> Administration > Working community / setting group settings > Work hours > Exceptional entries**.
![](https://support.nepton.com/hc/article_attachments/35564468055325)
**The exceptional entries that can be disabled** are set on by default unless they have been separately defined to be turned off either at the Working Community level or at the setting group level. If you want an exceptional entry (attention triangle) off, set the value of that exceptional entry to "Yes".
The **Exceptional entries report** can be run on the work time events according to the settings defined in the working community settings or setting group settings. The report can be used to check the status of logged events for example before approving hours. More information about the report can be found in [this article](<https://support.nepton.com/hc/en-gb/articles/360002548837>). 
When the event is edited via the calendar or mobile view and the system recognizes that the event recording leads to an exceptional entry, a warning message is displayed. The event editor can then decide whether to accept the recording despite the warning or cancel the change and go back to editing the event.
## Exceptional entries
The existing exceptional entries and the situations in which they are shown are described below.
### Overlapping events on the day
The exceptional entry notification is shown when overlapping events have been entered for the day. No warning is shown if one of the following is true for an overlapping event:
  * The event does not have a separate end time or the end time is the same as the start time.
  * The event is a travel invoice or a public holiday. 
  * The event type can be recorded on top of another event (For example an 'On call' -event).
  * The event is annual leave and the work event recorded overlapping it is interpreted as overtime during the annual leave.
  * The event is annual leave and travel time has been recorded overlapping it.


### Unfinished events
The exceptional entry notification is shown when there is an event on the day without an end time and the day of the event is not the current day.
Note! If the exceptional entry 'Overlapping events on the day' is set not to be shown, then this exceptional entry will not be shown either.
### Working hours restricted due to work time limitations
The exceptional entry notification is shown when calculated working hours of the day have been limited due to the permitted work times. Note! This exceptional entry notification is not visible for future dates.
It is possible to set a threshold value for this exceptional entry and choose after how many minutes or hours the notification is shown.
![](https://support.nepton.com/hc/article_attachments/35564468056861)
### Day has work obligation but no entry has been made
The exceptional entry notification is shown when there is a work obligation for the day but no work event has been recorded for the day.
### Scheduled shift but no work entry
The exceptional entry notification is shown when there is a work shift during the day but no work event has been recorded for the day.
### No planned shifts for the day, but work is marked
The exceptional entry notification is shown when there is no work obligation for the day but a work event has been recorded for the day.
### Unpaid recorded time
The exceptional entry notification is shown when the calculated working hours of the day are not compensated. This is most often the case when the overtime hours calculated from the event are targeted as _Not compensated_.
It is possible to set a threshold value for this exceptional entry and choose after how many minutes or hours of uncompensated time the notification is shown.
![](https://support.nepton.com/hc/article_attachments/35564502725917)
### Maximum overtime amount exceeded
The exceptional entry notification is shown when the marked overtime amount for the day exceeds the calculated overtime hours.
### Sick leave (only shown in exceptional entries report)
An exceptional entry is shown on the report when sick leave has been logged for the day.
### Year leave (only shown in exceptional entries report)
An exceptional entry is shown on the report when annual leave has been logged for the day.
### Balance leave (only shown in exceptional entries report)
An exceptional entry is shown on the report when balance leave has been logged for the day.
This exceptional entry is shown on the report only for the balance leave and not for any other accruals.
### Absence (only shown in exceptional entries report)
An exceptional entry is shown on the report when an absence event has been logged for the day.
### Paid absence (only shown in exceptional entries report)
An exceptional entry is shown on the report when a paid absence event has been logged for the day.
### Planned work and recorded work have a difference in start time or end time
The exceptional entry notification is shown when the shift planned for the day does not match the recorded work event on the day.
It is possible to set a threshold value for this exceptional entry and choose after how many minutes or hours of difference the notification is shown.
![](https://support.nepton.com/hc/article_attachments/35564468061469)
### Maximum balance has been reached at the beginning of the day
The exceptional entry notification is shown when the accrual value has reached the maximum amount at the beginning of the day and the accrual value has been cut.
This exceptional entry notification is shown for all accruals visible in the calendar view.
### Maximum balance has been reached at the end of the day
The exceptional entry notification is shown when the accrual value has reached the maximum amount at the end of the day and the accrual value has been cut.
This exceptional entry notification is shown for all accruals visible in the calendar view.
### Minimum balance has been reached at the beginning of the day
The exceptional entry notification is shown when the accrual value has reached the minimum amount at the beginning of the day and the accrual value has been raised to the minimum amount.
This exceptional entry notification is shown for all accruals visible in the calendar view.
### Minimum balance has been reached at the end of the day
The exceptional entry notification is shown when the accrual value has reached the minimum amount at the end of the day and no more hours can be borrowed from the accrual. 
This exceptional entry notification is shown for all accruals visible in the calendar view.
### Earned balance has been limited because or daily earning restrictions
The exceptional entry notification is shown when the earned amount of an accrual has been limited due to the daily earning limit.
This exceptional entry notification is shown for all accruals visible in the calendar view.
### Stored balance incorrect exceptional entries
The exceptional entry notification is shown when the accrual value shown in the calendar view doesn't match the calculated value for the day. This usually happens in a situation where settings have been changed retrospectively after the events in the calendar have already been saved. By re-saving any event on the day the change of settings take place, the value of the accrual is updated. You can find more detailed instructions on recalculating the accrual value in [this article](<https://support.nepton.com/hc/en-gb/articles/4411220910865>).
### Balance reset or change on current day or in the future
The exceptional entry notification is shown when a Balance change or Balance reset event has been saved to the future. 
This exceptional entry is shown only for the balance accrual and not for any other accruals.
### Project duration over allocation
The exceptional entry notification is shown when the project duration assigned to the event is more than the recorded time of the event.
### Project duration under allocation
The exceptional entry notification is shown when the project duration assigned to the event is less than the recorded time of the event.
### Compensated time less than daily obligation
The exceptional entry notification is shown when the time compensated during the day is less than the work obligation set for the day. In this case, the time automatically borrowed from the balance is also counted as compensated time.
### Overtime has been manually modified
The exceptional entry notification is shown when there is manually set overtime in the day's events. Manually modified overtime means using an event type with a behaviour like "agreed overtime", so it is always overtime no matter what overtime settings are in use. 
### Unapproved events on the day (only shown in exceptional entries report)
The exceptional entry notification is shown for events that have not been approved.
### Work day length exception on the day
The exceptional entry notification is shown when there is an exceptional setting for the length of the work day.
### Permitted work times exception on the day
The exceptional entry notification is shown when there is an exceptional setting for permitted work times of the work day.
### Expected work times exception on the day
The exceptional entry notification is shown when there is an exceptional setting for the expected work times of the day.
### Suspiciously long worked shift
The exceptional entry notification is shown when the work shift done during the day is suspiciously long. 
It is possible to set a threshold value for this exceptional entry and choose after how many minutes or hours of difference the notification is shown. The default threshold value is 12 hours. The threshold value only applies to a continuous event, i.e. even if the combined time of several events exceeds the threshold value, the warning triangle is not displayed. Note! This exceptional entry notification is not visible for future dates.
![](https://support.nepton.com/hc/article_attachments/35564502726941)
### No project when project is mandatory
The exceptional entry notification is shown when no project has been entered for the transaction and project entry is mandatory.
### Event has projects with no allocated time
The exceptional entry notification is shown when a project has been added to an event but no project hours have been calculated. For example, three different projects have been added for an event and one of them has not been allocated any time.
### Missing data from travel invoice
The exceptional entry notification is shown for a travel invoice event for which all the necessary information has not been entered.
The following information is required on all travel invoices:
  * The start and end time of the travel event
  * The place of departure and destination of the travel event
  * Reimbursement of the travel invoice (i.e. supplement such as reimbursement of the route of the travel invoice, daily allowance or other expenses)


Also the following information is required on the travel invoice, when the mode of travel is by plane or ship:
  * The start and end time of the journey
  * The area of ​​the journey's departure and destination
