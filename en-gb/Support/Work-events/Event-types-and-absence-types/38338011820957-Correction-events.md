---
id: 38338011820957
title: Correction events
url: https://support.nepton.com/hc/en-gb/articles/38338011820957-Correction-events
locale: en-gb
category: Support
category_id: 360000446658
section: Event types and absence types
section_id: 360005841257
section_path:
- Work events
- Event types and absence types
labels:
- korjaaminen
promoted: false
updated_at: '2026-08-14T08:59:18Z'
edited_at: '2026-08-14T08:59:18Z'
---

# Correction events

Correction event type is used to manually correct the interpretation of compensation. The visibility of the correction event is set by permissions within the worktime role. A supplement is always used in conjunction with the correction event.
## Activating the event
The correction event is activated for use [in the same way as other event types](<https://support.nepton.com/hc/en-gb/articles/360002519157>) from the event type list. It is recommended to activate the event at the work community level, as only persons with sufficient worktime role rights will see it in the event list and can record it.
## Required permissions
To be able to record a Correction event, a person must have sufficient [worktime role permissions.](<https://support.nepton.com/hc/en-gb/articles/360002554338>) The required permission can be found under the medium-level Work hours category, "Can edit correction events". Administrators always have this permission automatically, but it can also be granted, for example, to supervisors.
![](https://support.nepton.com/hc/article_attachments/38361943076765)
## Activating related work allowances
The correction event itself does not yet affect the interpretation of work hours. A [Supplement ](<https://support.nepton.com/hc/en-gb/articles/360002559637>)must always be added to it, which determines the amount and target of the correction.
![](https://support.nepton.com/hc/article_attachments/38361943078557)
The supplement must be set to be used in Correction events. This means it can only be linked to those specific events, so only persons with the right to record correction events can use these supplements. The supplement must be given a descriptive name, and its effect is defined in the fields "Increase accrual with duration" and "Increase accrual in accordance with rate of increase".
## Recording a correction event
Once the supplement is defined, a correction event can now be recorded with that supplement for any user. The correction event does not have start and end times, only the date on which the supplement is to be recorded.
![](https://support.nepton.com/hc/article_attachments/38361943080733)
The amount of the supplement can be positive, in which case the accrual it is directed to increases by the desired amount, or negative, in which case the accrual it is directed to decreases by the desired amount. The supplement can also be directed to pay.
![](https://support.nepton.com/hc/article_attachments/38361943084189)
In the above example, 10 days (the accrual unit is days) have been added to the Test accrual with a correction event. The change is visible in the interpretation on the same day.
For changes made by the Correction event to be transferred to salaries in a possible integration, the supplement must be picked by the salary rule.
