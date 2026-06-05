---
id: 360009227298
title: How to use Temporary lay-off event type
url: https://support.nepton.com/hc/en-gb/articles/360009227298-How-to-use-Temporary-lay-off-event-type
locale: en-gb
category: Support
category_id: 360000446658
section: Event recording
section_id: 360005850877
section_path:
- FAQ
- Event recording
labels:
- lomautuksen kirjaaminen
- lay-off
promoted: false
updated_at: '2024-08-23T11:59:33Z'
edited_at: '2024-07-30T07:57:48Z'
---

# How to use Temporary lay-off event type

The 'Temporary lay-off' event type behaves like an absence. It fulfills the missing work obligation up to the length of the working day but does not accumulate overtime, balance, or other accruals.
## Getting started
When Temporary lay-offs are started, either part-time or full-time, it is usually not necessary to change the length of the work day to reflect the reduced work obligation. This way it is easy to see work and Temporary lay-off in calendar and reports.
## Best practices
We recommend the following approaches for dealing with temporary lay-offs. The examples below handle the most common cases.
If it is necessary to get overtime or accumulated balance recorded during Temporary lay-off, a new event type must be created that behaves like the 'Work' event type. Follow this link for full instructions on how to [Manage and edit event types](<https://support.nepton.com/hc/en-gb/articles/360002519157>).
The order of events in the calendar impacts how working time is interpreted. If the day starts with a 'Temporary lay-off' event and continues with a 'Work' event, the work will accrue balance/overtime if desired. If the order of these events was reversed, there will never be balance/overtime.
If you use a custom event type, e.g. 'Temporary lay-off in flexitime', which behaves like 'Work', the order of the events does not matter.
The annotated screenshot below shows different examples of Temporary lay-off and their behavior.
![](https://support.nepton.com/hc/article_attachments/20521781565085)
  1. Temporary lay-off in flexitime \- custom event type that behaves like work
  2. Temporary lay-off \- the default service event type that behaves like an absence
  3. Overtime option Overtime - Salary
  4. Overtime option Hour to hour - Balance
  5. Nothing is accrued because the 'Temporary lay-off' event ends the business day and only fills up to the daily obligation
  6. Overtime option Overtime - Balance


If desired, 'Temporary lay-off' events can be reported with, Hours by event type.
![Lomautus_3.png](https://support.nepton.com/hc/article_attachments/360008760198)
