---
id: 33334659658525
title: Recording absences
url: https://support.nepton.com/hc/en-gb/articles/33334659658525-Recording-absences
locale: en-gb
category: Support
category_id: 360000446658
section: Event recording
section_id: 360000934997
section_path:
- Work events
- Event recording
labels: []
promoted: false
updated_at: '2026-05-12T06:35:20Z'
edited_at: '2026-05-12T06:35:20Z'
---

# Recording absences

Absences are added to Nepton in the same way as other events. Depending on the settings, absences can be added in the worktime calendar, in the current status, on mobile or on worktime terminal. Some absences can be recorded in advance also on the terminal, depending on the settings. Some absences may be event requests that require approval before the entry is created in the calendar.
## Recording absences in calendar view
Absences are recorded in the calendar in the same way as Work entries. Click on the date and select “add event”. Select the correct event type from the Add event window. The event types are divided into the categories “Work”, “absence” and “administration” in the menu, the latter of which is only visible to the administrator or other person who has been granted rights to administrative events. Basic users usually see events in the “Work” and “absence” categories. Select the correct absence event from the menu and save it like any other event. 
![](https://support.nepton.com/hc/article_attachments/35047306248989)
Long absences can be marked by start and end dates, and there is no need to make separate entries for each day. Absences only cover the regular time of the day (or how each absence is defined to behave), so even if the absence entry itself is longer than the work obligation of the day, it will not earn, for example, balance or overtime. Long absences appear in the calendar as a daily entry with the start and end days times. By clicking on an event, its total duration is shown.
![](https://support.nepton.com/hc/article_attachments/35047322855453)  

## Sick leave
Some ansences, like Sick leave, have additional fields that appear when the absence type has been selected. The right to edit these fields depends on the person's worktime role and permissions. 
![](https://support.nepton.com/hc/article_attachments/35047306260125)
In the **Additional info** field you can choose the type of the sick leave. The options are Sick, Child sick, Accident at work, Accident while commuting and Accident in free time. These default fields can't be modified.
In the **Medical certificate** field you can enter the status of medical certificate: Not known, Not received, Received, Permission from supervisor. These default fields can't be modified. Medical certificate - field is visible for only roles that have the permissions to see or edit this field. Usually these roles are for payroll and administrative personnel. 
In the **Reason code** field you can enter for example doctor's given reason code or other code used in your company. Reason code - field is visible for only roles that have the permissions to see or edit this field. Usually these roles are for payroll and administrative personnel. 
**Compensation** field is used to define the compensation of the absence. 
**Earns vacation days** is chosen as a default, but it can be unticked.
**Notes** field can be used to write a message to the supervisor or person who approves the absence.
Sick leave hours can also be targeted to a project like any other event when creating or modifying the event.
Sick leave certificates cannot be saved in Nepton. This is because the certificates contain health information, which is considered special personal data according to the GDPR and the Finnish Data Protection Act.
## Annual leave
Annual leave can also be found in the menu under the Absence category, and it is recorded in the same way as other events. When recording annual leave, the service calculates by default how much of the annual leave balance is used by the absence in question, and how much is left after the event. The calculation can be turned off in the [annual leave settings](<https://support.nepton.com/hc/en-gb/articles/360002560698>).
![](https://support.nepton.com/hc/article_attachments/35047306261277)
The entire holiday period is recorded as one event. The event must include the last Saturday used. Sundays do not consume the accrual if the settings have defined Mon-Sat as annual holiday days. If a day does not consume the accrual, it will be displayed in gray colour in the calendar:
![](https://support.nepton.com/hc/article_attachments/35047322862365)
The accrual value is only displayed if the annual leave is registered for the future. The value of the Annual Leave accrual is not displayed in connection with an Annual Leave event that is scheduled for the past or for the same day, or is already in the calendar. A person can view their available annual leave days using the 'Annual Leave Usage by Season' report.
Annual leave hours can also be targeted to a project like any other event when creating or modifying the event.
### Working during annual leave
Sometimes it is necessary to work during annual leave. Working during annual leave is generally interpreted as overtime.
If work during annual leave should be interpreted as overtime, the work event must be recorded at the same time with Annual leave in calendar. For example, if Annual leave event is recorded 8:00-16:00, Work event needs to be recorded between 8:00-16:00, for example 12:00-13:00. Then the work event is targeted automatically to person's default overtime target.
In this example person's overtime target is 'Hour to hour - Balance', so one hour moves to balance as a result.
![](https://support.nepton.com/hc/article_attachments/35047322864413)
If the work event is recorded outside of the Annual leave event (partly or entirely) Nepton interprets that work is done and the annual leave for the day is ignored. Then person earns minus balance, because person's daily working hours (work obligation) are not met. 
![](https://support.nepton.com/hc/article_attachments/35047306272925)
If a workday has both annual leave and work events that are equal in lengths, the recording that was first made will be interpreted.
Please note: If a clocked event is logged at the same time as annual leave (or any other absence), the annual leave event will end as the clocked event begins. If Emergency Work is recorded on annual holiday, it is always interpreted as 100% overtime.
### Getting sick during Annual leave
According to the Annual Leave Act, there are six deductable days of sick leave during annual leave. If you become ill during annual leave, the annual leave event is shortened so that the days of sick leave remain as annual leave. The days of sick leave are not considered annual leave for the purposes of interpretation. The remaining time is recorded as sick leave.
## Accrual leaves
An event type "accrual leave" has been automatically created for each accrual in use. For example, if balance accrual is used in the settings group, the event type menu also includes the events balance leave (as well as the administrative events balance setting and balance change). When accrual leave is used, the work obligation is fulfilled for the duration of the event/ length of work day from the accrual. The administrator can change the [settings ](<https://support.nepton.com/hc/en-gb/articles/360005073918>)to specify which event types are in use and how they behave, as well as which days are considered accrual leave.
![](https://support.nepton.com/hc/article_attachments/35047322869917)
When you record accrual leave, the service calculates the impact of using the accrual leave on the accrual balance according to your settings. The value of the accrual leave is only displayed if it is recorded for the future. The value is not displayed for accrual leave that is scheduled for the past or the same day, or for an accrual leave that is already in the calendar.
## Absence requests
Some absences may have been set as event requests. In this case, the person can record the absence as an event, but it will wait for approval from a supervisor before it becomes a confirmed event. More about event requests in [this article](<https://support.nepton.com/hc/en-gb/articles/360017787717>).
