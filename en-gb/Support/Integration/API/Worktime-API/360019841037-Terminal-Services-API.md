---
id: 360019841037
title: Terminal Services API
url: https://support.nepton.com/hc/en-gb/articles/360019841037-Terminal-Services-API
locale: en-gb
category: Support
category_id: 360000446658
section: Worktime API
section_id: 360005706218
section_path:
- Integration
- API
- Worktime API
labels:
- API
- pääte
promoted: false
updated_at: '2025-09-08T12:00:20Z'
edited_at: '2025-09-08T12:00:20Z'
---

# Terminal Services API

This article describes Worktime API methods for handling terminal services. The methods described are technically possible to use in other contexts as well, but they are primarily designed for worktime terminal entries.
## Starting an event
It is possible to start a new event with API. For example a user starts their day by recording a work event.
API methods for starting events:
  * [BeginActivity (obsolete)](<https://support.nepton.com/hc/fi/articles/6869807559453>)
  * [BeginActivityV2](<https://support.nepton.com/hc/fi/articles/6869562936221>)


## Ending an event
It is possible to end an event with API. For example a user finishes their day by ending a work event.
API methods for ending events:
  * [EndActivity (obsolete)](<https://support.nepton.com/hc/fi/articles/6870299031581>)
  * [EndActivityV2](<https://support.nepton.com/hc/fi/articles/6870443544477>)


## Päätekirjautuminen
It is possible to obtain information about a specific user at the current time, e.g. information about an open event or the event types that the user can select.
API methods:
  *     * [TerminalLogin (obsolete)](<https://support.nepton.com/hc/fi/articles/6887099778333>)
    * [TerminalLoginV2](<https://support.nepton.com/hc/fi/articles/360021180898>)
