---
id: 32229098583965
title: Premade notifications
url: https://support.nepton.com/hc/en-gb/articles/32229098583965-Premade-notifications
locale: en-gb
category: Support
category_id: 360000446658
section: Notifications
section_id: 32229019276445
section_path:
- Notifications
labels: []
promoted: false
updated_at: '2026-09-24T11:56:10Z'
edited_at: '2026-09-24T11:56:10Z'
---

# Premade notifications

Premade notifications are available with the Worktime Pro service level and higher. [**Custom notifications**](<https://support.nepton.com/hc/en-gb/articles/32258952073757>) are available with the Worktime Complete service level.
This article covers premade notifications. For more information about the Notifications view and creating notifications, see the article [**Creating a new notification**](<https://support.nepton.com/hc/en-gb/articles/32259026029213>).
## What are premade notifications?
Premade notifications are predefined email alerts that help monitor worktime management processes. They can automatically notify managers about events that require action. Notifications can be scheduled and tailored to your organisation’s needs using various settings, ensuring timely communication and relevant message content.
Nepton sends notifications from the default sender address [noreply@nepton.com](<mailto:noreply@nepton.com>). Shift notifications can instead be sent from a customer-specific sender address configured in the customer settings. If your organisation filters incoming email, allow the sender domains @nepton.com and @nepton.fi so that Nepton notifications are delivered.
## Types of premade notifications
The following premade notifications are currently available:
### Unapproved events (by payment group)
Notify people of unapproved events. Events are checked for persons in selected payment groups. No notification is sent for assumed events.
### Unapproved events (by person group)
Notify people of unapproved events. Events are checked for persons in selected person groups. No notification is sent for assumed events.
### Anniversaries (employment)
This notification can be used to remind about upcoming work anniversaries (e.g., 1, 5, 10 years of employment).
**Important before use:**
  * The **employment start date** must be correct in Nepton to calculate the anniversary accurately. Please note that this date might be different in Nepton because of worktime calculations.
  * Employees with an **employment end date set** and who no longer work for the organization **are not included in the notification**.


**Notification settings:**
  * **Anniversary years:** Enter the years for which you want notifications (e.g., 1, 5, 10, 15…).
  * **Number of days to warn in advance:** Define how many days before the anniversary the notification should be sent (e.g., 14).
  * **Recipients:** Select who will receive the notification (e.g., primary supervisors, deputies).
  * **Notification content:**
    * Title: e.g., _Work anniversary reminders_
    * Starting paragraph: e.g., _The following employees have work anniversaries approaching:_
    * Per-row message: _[PersonName], [AnniversaryYear] year work relationship anniversary ([ContractStartDate])_
  * Once checked and saved all the details, add a schedule from the schedule tab. It is important to set it on a daily schedule to ensure no anniversaries are missed.


**Privacy note:**
The notification includes the employment start date and years of service. Ensure it is not sent to recipients who are not authorized to view this information.
![](https://support.nepton.com/hc/article_attachments/33077165166109)
### Accrual balances
Notify selected recipients of employees’ accrual balances when the balance exceeds or falls below defined thresholds.
**Notification logic:**
  * The notification checks the balances of the selected accruals for the chosen person groups
  * The notification is generated for individuals whose balance:
    * is greater than the defined upper limit, or
    * is less than the defined lower limit
  * The notification includes only those individuals whose balance is outside the defined limits
  * Balances are presented in hours and minutes


**Notification settings:**
  * **Accruals to send notifications about:** Select one or more accruals to monitor
  * **Warn if balance falls below (hours):** Defines the lower limit, e.g. -20 hours
    * If notifications about negative balances are not required, set the lower limit to a value that will not realistically be reached (e.g. -999). In this case, notifications will only be sent when the upper limit is exceeded.
  * **Warn if balance rises above (hours):** Defines the upper limit, e.g. 20 hours
  * **Select groups of people whose accrual balances are checked:** Defines the person groups included in the check (note: inheritance is not supported)


**Things to note:**
  * The notification checks only the accrual balances at the time of execution
  * The limits are defined within the notification and are not retrieved from other settings (e.g. setting groups)
  * The notification applies directly to the selected person groups (not via setting groups)
  * Only the accruals selected in the settings are included in the notification
