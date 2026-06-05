---
id: 360016976178
title: Terminal offline mode
url: https://support.nepton.com/hc/en-gb/articles/360016976178-Terminal-offline-mode
locale: en-gb
category: Support
category_id: 360000446658
section: Troubleshooting
section_id: 360005896337
section_path:
- Terminals
- Troubleshooting
labels:
- vianselvitys
promoted: false
updated_at: '2024-08-23T09:20:17Z'
edited_at: '2024-05-21T07:45:04Z'
---

# Terminal offline mode

Nepton terminal software can temporarily operate without an internet connection. When a loss of connectivity is detected, the software enters "offline-mode". It allows users to continue marking events with only minor changes and limitations to functionality. When connectivity is restored the terminal will automatically reconnect and synchronise offline markings to the Nepton platform.
This feature is provided to mitigate the impact of short internet interruptions and temporary network problems. Internet connectivity should always be restored as soon as possible.
## Troubleshooting
In exceptional circumstances or at customer request, the offline-mode can be disabled. This will prevent login or markings using the terminal when there is not an active connection to the Nepton platform.
There are many terminal troubleshooting and guidance articles, please use the search, or see the **Terminal Use** section.  
See also: [Terminal remains in offline mode, or cannot connect to the internet (Connectivity troubleshooting).](<https://support.nepton.com/hc/en-gb/articles/360002588757>)
## How do I know if a terminal is offline?
Nepton terminal software enters offline-mode when it detects that a connection to the Nepton servers is not available. This functionality is provided to mitigate the impact of short internet interruptions and temporary network problems. Internet connectivity should be restored as soon as possible.
Offline mode is indicated by a red status bar at the bottom of the software.
**![Terminal_offline_2.png](https://support.nepton.com/hc/article_attachments/360015697097)**
## Reconnection & synchronisation
Whilst in offline-mode the software frequently checks for connectivity, and when possible, will automatically reconnect. When the terminal re-establishes connection with the Nepton servers it will systematically synchronise any data that was recorded by users in the offline-mode.
The synchronisation of offline markings is fast once reconnected, but please allow some time for events to appear in employee calendars if there are large amounts of data.
When the terminal has good connectivity, normal features are available and the status bar will be green as shown here.
**![Terminal_online_2.png](https://support.nepton.com/hc/article_attachments/360015770778)**
## Limitations
### Login
Whilst in offline-mode, logins cannot be authenticated using the Nepton server and therefore an on-board cache is used. Using RFID tags, unknown and first-time users are permitted to login to the terminal software, but will only be able to mark default event types and projects. Depending on your environment's configuration, this might mean that no projects are available. Please see the next heading for more detailed information on event types and projects limitations in offline-mode.
**Important Note:** If markings are recorded with unknown tags and these tags are still not configured for a person in the Nepton platform by the time the terminal reconnects, then the markings **will not** be synchronised to Nepton.
### Event types and projects
When in offline-mode, each terminal relies upon a cache to determine the activity types and projects which should be available to an individual. The cache is updated when a person uses the terminal whilst connected to the Nepton servers, i.e. **not** when in offline-mode.
Providing the terminal has had at least one successful login with connection to the Nepton servers, default event types and projects will be cached, and therefore unknown and first-time users can still record basic markings and projects.
**Important note:** The cache used in offline-mode is device-specific and is not shared between devices. Therefore, depending on when a person used a terminal last, they might see different options between two devices, when both are in offline-mode.
### Marking events & person status
As the terminal software cannot communicate with the Nepton servers a person's current status and accruals information cannot be shown.
As the current status cannot be determined, the terminal cannot intelligently offer or interpret whether a marking should Start, Stop, or Stop and Start an event. Therefore, in offline-mode users must indicate whether their marking is a Stop or Start action. To support this, both options are made available for saving the marking. However, you must first select the event type, i.e. "Work", for the Start button to be activated. If you want to end the ongoing event, you have to press the Work button again so that the Stop button is activated, see images:
**![Terminal_offline_4.png](https://support.nepton.com/hc/article_attachments/360015697457)**
**![mceclip2.png](https://support.nepton.com/hc/article_attachments/9082252631581)**
**![mceclip3.png](https://support.nepton.com/hc/article_attachments/9082281621533)**
### Duration of offline mode
It is recommended that terminals are always online. The offline mode is provided to be of assistance during short internet interruptions and temporary network problems. The only restriction of offline mode is the hard disk space of the terminal. If for some reason, the terminal is offline for such a long period of time that the markings made during it will fill up the hard disk space of the terminal, the markings would not be transferred to Nepton once a network connection was re-established. Depending on the usage level and markings made on the terminal, the disk space might run out in a week or two of offline mode. This kind of usage is not recommended.
