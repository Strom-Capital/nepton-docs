---
id: 360002560518
title: Terminal and current status view settings
url: https://support.nepton.com/hc/en-gb/articles/360002560518-Terminal-and-current-status-view-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- leimauspäätteet
- työaikapääte
- work time terminal
- recording terminal
- current status view
- nykytilanäkymä
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-08-18T11:44:25Z'
---

# Terminal and current status view settings

Worktime terminal (in Nepton recording terminal) and current status view settings can be defined in working community level and setting group level. Most of the settings are only available on the working community level.
Please note: Event type visibility in terminals and current status is set in event types table. Further instructions [here](<https://support.nepton.com/hc/en-gb/articles/360002519157>).
## Settings
At the working community settings level, the settings can be found in **Worktime > Administration > Working community settings > Current Status.**
![](https://support.nepton.com/hc/article_attachments/28380483573789)
**Current status page enabled** setting is Yes by default. It indicates whether the [Current State View](<https://support.nepton.com/hc/en-gb/articles/360002603258-Recording-events-in-current-status-view-or-terminal>) is active. 
**Current status terminal enabled** is a setting that applies to older implementations. This setting must be set to yes for the web address link on the page to work.
**Web page address** can be used to open the service's Current Status view via aweb address. The link requires that the setting "Current Status terminal enabled" is set to yes. This can be useful, for example, when users need to use the Current Status View on an external device (such as a tablet within the organization’s premises). If RFID authentication or PIN code authentication is required, it must also be done when using this link.
**Log in possible with the Recording Terminal** setting defines if it´s possible to log in using the [PIN code](<https://support.nepton.com/hc/en-gb/articles/360002430798-Manage-PIN-codes>).
“PIN-code login not in use” = Only RFID login enabled
“PIN-code login in use” = Both PIN code and RFID login enabled 
“Only RFID-login in use” = Only RFID login enabled
![](https://support.nepton.com/hc/article_attachments/28380473159069)
**Comment input visible in web terminal and current status page** defines, whether a comment can be left when recording events in terminal and current status. It is set to ‘No’ by default.
**Show notifications in the recording terminal and current status page** The option displays notifications created in the Communication section both in the recording terminal and on the Current Status page. The setting is set to 'Yes' by default. The Communication section is not enabled by default. If you would like to enable the Communication section in your organization, please contact your contract contact.
**Ability to edit start and end times in terminal** The setting tells whether a person can edit the start and end times of an event when logging an event using the Current status page or the Current status terminal. This can be useful, for example, if the person is working at a location and then moves to another location for the rest of the day. By default, the setting for editing start and end times is 'No'. Note: This setting does not apply to recording events on[ a terminal](<https://support.nepton.com/hc/en-gb/articles/360003685277>) such as Nepton Touch. Instructions on how to set start and end times for chosen events on a terminal can be found [here](<https://support.nepton.com/hc/en-gb/articles/4406224046097>).
**Input interval of start and end times** setting allows you to define the precision (in minutes) with which start and end times can be adjusted. This can be useful in situations where working hours need to be handled with a minimum accuracy of 15 minutes. Note: This setting does not apply to recording events on a terminal such as Nepton Touch. With terminals you can enter start and end times in 15-minute intervals.
**Show projects** setting determines whether the Project tab is displayed when recording an event on the recording terminal and in the current status view. Enabling this allows [work to be allocated](<https://support.nepton.com/hc/en-gb/articles/360002593398-Recording-an-event-with-a-project-using-the-terminal>) to specific projects or targets when using the recording terminal and current status view.
**Has terminals working in cafeteria mode** setting indicates whether the organization uses so-called “lunch terminals” or recording terminals for handling lunch and café payments. This setting is enabled by Nepton or the partner’s contact person if required. It should not be modified.
**Show today's work hours** setting determines whether the person's working hours for the current day are displayed in the current state.
**Show week's work hours** setting determines whether the person's working hours for the current week are displayed in the current state.
![](https://support.nepton.com/hc/article_attachments/28380483576477)
**Go to current status page after log in** If the setting is active, the user will be redirected directly to the current status page after recording events.
