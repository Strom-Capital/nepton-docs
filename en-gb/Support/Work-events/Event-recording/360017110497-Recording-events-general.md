---
id: 360017110497
title: Recording events - general
url: https://support.nepton.com/hc/en-gb/articles/360017110497-Recording-events-general
locale: en-gb
category: Support
category_id: 360000446658
section: Event recording
section_id: 360000934997
section_path:
- Work events
- Event recording
labels:
- tuntikirjaus
- työaikaleimaus
- leimausohje
- työaikakirjaus
promoted: false
updated_at: '2026-02-02T13:29:36Z'
edited_at: '2025-09-01T05:56:32Z'
---

# Recording events - general

This article is about general principals about recording events to Nepton when work time is performed unequivocally. 
Recording events can be descripted as follows:  
1\. Start work day, record event type Work-Start  
2\. Go to lunch, record event type Lunch break-Start  
3\. Continue work day, record event type Work-Start  
4\. Finish work day, record event type Work-Stop
In the beginning of the work day record Start and at the end of the work day record Stop. All other events of the day can be done with Start record. Nepton ends the previous event automatically when new event is started.
This is how continuous event chain is gained and work time can be interpret unequivocally. If events are not in continuous chain, for example automated lunch break does not form right. 
The easiest way to use event recording is to use above descripted real time recording. There are several options to use real time event recording: [mobile](<https://support.nepton.com/hc/en-gb/articles/360002602638-Add-an-event-using-Nepton-mobile>), [terminal](<https://support.nepton.com/hc/en-gb/articles/360002593338-Start-an-event-using-the-terminal>) and [Current status](<https://support.nepton.com/hc/en-gb/articles/360002603258-Recording-events-in-current-status-view-or-terminal>) -view. Events can be also recorded real time in Events in Calendar or Events in table view.
Note: Events should not be saved more than four years into the future, or there may be errors in recording real-time events or event requests.
## New event start time logic
You can set a default Start and End time for an event in the [Rendering options](<https://support.nepton.com/hc/en-gb/articles/360008777997>). When adding the first event for any day, whether in mobile or calendar, Nepton will suggest a default start and end time for the event based on the rendering options. If no default start and end times are set, Nepton will suggest a default times of 0800-1600 for the event.
If there is already an event on the current day and another event is added to the same day, Nepton will suggest the current time as the default start time for the event.
If there is already an event on the day in the past or future and another event is added to the day, Nepton will suggest the end time of the previous event as the default start time for the event.
![](https://support.nepton.com/hc/article_attachments/29995759457821)
