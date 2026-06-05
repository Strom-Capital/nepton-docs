---
id: 360002521338
title: Event grouping
url: https://support.nepton.com/hc/en-gb/articles/360002521338-Event-grouping
locale: en-gb
category: Support
category_id: 360000446658
section: Event management
section_id: 360000667978
section_path:
- Work events
- Event management
labels:
- NEPTONNEEDSREVIEW
- piilotettu
- piilotus
- tapahtumien näkyminen
promoted: false
updated_at: '2026-04-02T10:13:17Z'
edited_at: '2026-04-02T10:13:16Z'
---

# Event grouping

If there are a large number of events during the day, they are grouped under a separate menu to make it easier to view the calendar view. Grouping events also speeds up the loading time.
In the example below, the same events are shown under a separate **"9 events hidden"** menu.   
  
![](https://support.nepton.com/hc/article_attachments/35076012101149)  
  
Events are based on how much space they take up in calendar view.
In practice, the service groups events together, based on rows that are:
**Event type + duration (e.g. 07:00 - 07:30) =** counted as one line  
**Project (s) assigned to the event =** counted as a half line  
**Comment =** counted as a half line
For example, if an event has two projects (0.5 + 0.5 lines) in addition to the duration (1 line), its height is calculated as two lines. If an event has three projects (0.5 + 0.5 + 0.5 = 1.5 lines) and a comment (0.5 lines) in addition to the duration (1 line), its height is calculated as 1 + 1.5 + 0.5 = 3 lines. If the event only has the duration, its height is one line.
Events are hidden under the menu if there are more than 12 lines in total. When the menu is clicked, all events grouped under are shown:  
![](https://support.nepton.com/hc/article_attachments/35076012102941)
Few customers have a special solution for grouping events, where events imported into Nepton are hidden based on the event creator. This solution will not be implemented for new customers.
