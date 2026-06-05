---
id: 24730505042077
title: How to use Nepton Flexim terminal
url: https://support.nepton.com/hc/en-gb/articles/24730505042077-How-to-use-Nepton-Flexim-terminal
locale: en-gb
category: Support
category_id: 360000446658
section: Terminal use
section_id: 360002084697
section_path:
- Terminals
- Terminal use
labels: []
promoted: false
updated_at: '2025-09-23T11:30:33Z'
edited_at: '2025-09-23T11:30:33Z'
---

# How to use Nepton Flexim terminal

This article guides you through how to use Nepton Flexim terminal.
## Main display
By default, the terminal screen is displayed in Finnish. The language can be changed to English or Swedish with the admin PIN code from the terminal's settings (see instructions at the end of this article). When a person logs in, the terminal uses the language set for the person in Nepton.
![](https://support.nepton.com/hc/article_attachments/25046505072797)
On the terminal, the top bar shows Nepton logo, question mark symbol and the current time. Clicking on the question mark opens additional information about the terminal; Terminal ID, software version, QR code for instructions on the support website and the option to restart the device. The Settings button is introduced at the end of this article.
![](https://support.nepton.com/hc/article_attachments/25046492159517)
  
In the middle of the screen, the enabled login options are presented. Login methods are explained in more detail in the next section of this article.
## Logging in
There are different ways to login to Nepton Flexim terminal:
### Logging in with RFID-tag
The tag is shown to the reader, and the user is logged in. Then they can register work time. The tag number must be saved under person's information. A person can have multiple RFIDs saved in their information.
### Logging in with PIN-code
When logging in with a PIN code, the user keys in their own PIN code on the number board, after which they are logged in and can register working hours. The PIN code must be saved in the person's information. Logging in with a PIN code can also be blocked on each terminal, in which case the terminal log in mode would look like this:
![](https://support.nepton.com/hc/article_attachments/25046505090205)
### Quick clocking
Terminals can be set to offer quick clocking mode at the login screen. Quick clocking mode is intended for situations where there are large volumes of people, or where editing of events isn't necessary at the terminal. When quick clocking mode is on, showing your tag to the reader starts a work event from that moment on. If the person has an open event, it ends when a new quick registration starts. If a default project has been set for the person, the work is automatically assigned to this project. When the quick clocking function is enabled, each user can determine whether it is in use or not from the terminal's home screen. Quick clocking method can be used also when the terminal is offline.
## Screen view after logging in
If there already is an active event, it is highlighted in the event menu in blue. This event ends automatically if another event is selected from the terminal and "Start" is pressed.
If nothing is done after logging in, the user is automatically logged out after a 20-second delay. The length of delay can be adjusted in the terminal settings. The delay is shown as a decreasing bar at the bottom of the screen. Above the bar, the current value of two accruals is displayed. There is also a Cancel button at the bottom of the screen, which allows you to return to the previous view, and an Exit button, which allows you to log out of the terminal.
A menu appears at the top of the screen; the first is the event selection, next is the adding work supplements, after that is target for possible overtime and the last is project targeting. The upper right corner shows which user is logged in and what time it is at that moment.
## Adding an event
Once a person is logged in on the device, predetermined events are shown. A maximum of eight events are shown on the screen. If more events have been set to be displayed, the view is split on multiple pages, and the side arrow is used to move to the next page. A new event is started by clicking on the desired event type and then the "start" button. When the event is started, the user is automatically logged out of the terminal. If the terminal is in offline, only quick recording events will be registered.
![](https://support.nepton.com/hc/article_attachments/25047288224669)
### Adding an event with start and end times
The terminal can also be used to add events to the future by giving them a start and/or end time. In order for this to be possible, this option must be enabled for the event type in the user's setting group in Nepton. When an event is activated on the terminal, the "Edit" button appears next to the "Start" button.
![](https://support.nepton.com/hc/article_attachments/25050679289373)
When clicking this a new menu opens, from which you can select the start and end time for the event.
![](https://support.nepton.com/hc/article_attachments/25050704703389)
After the dates have been chosen, the next view will let you set the times.
![](https://support.nepton.com/hc/article_attachments/25050679297565)
## Targeting overtime
In the overtime tab the target for overtime can be changed. The options shown are determined in setting group settings. The number of currently active selections is displayed next to the name of the tab.
![](https://support.nepton.com/hc/article_attachments/25047348289565)
## Adding a supplement
Supplements can be added when an event has been started. The supplements tab shows four supplements per page. The side arrow can be used to move to the next page, if there are more than four supplements.
![](https://support.nepton.com/hc/article_attachments/25051729451421)
The type and default values ​​of the supplements come from the settings in the settings group. You can reduce or increase the amount of the supplement either by pcs or by 15 min at a time with quick dials. If necessary, a more precise value can be given by pressing the pencil icon.
![](https://support.nepton.com/hc/article_attachments/25050704711197)
The number of currently active selections is displayed next to the name of the tab.
## Project targeting
From the Projects tab, you can select which project the event is assigned to. The view shows 8 projects on one page. If there are more projects, you can move to the next page with the side arrow. The user is offered the most recently used ones, i.e. the same projects that are offered to the person when creating an event in the browser. With the search function, you can also find other projects by using the project name or code.
![](https://support.nepton.com/hc/article_attachments/25051754348061)
### Project targeting with bar code reader
The project can also be selected with a barcode scanner after the person has logged in on the terminal. After reading the barcode, the event with the project starts and the person logs out of the terminal. The screen shows that event has started successfully.
![](https://support.nepton.com/hc/article_attachments/25052088604317)
If an event is started with a barcode reader with a project that is not yet in Nepton, and the user has the necessary rights, the project will automatically be created as a new project in Nepton (the project will be in the root of the project tree). The necessary rights for this are given by the mid-level rights in the worktime roles "Can create missing projects via terminal barcode reader":
![](https://support.nepton.com/hc/article_attachments/25051729456029)
## Changing the settings on the terminal
Some terminal settings can be changed directly from the terminal. For this, a management PIN code is required. The settings can be accessed from the terminal's home screen by clicking on the question mark symbol, and from the screen that opens, the "settings" button. At this point, the terminal will ask for a PIN code. If you do not know the PIN code for managing your terminals, please contact Nepton's customer service.
Once the PIN code has been entered, the following management menu opens (please note, the admin menu is only in Finnish):
![](https://support.nepton.com/hc/article_attachments/25052088605469)
Terminal information is displayed at the top of the screen; serial number, software version and IP address.
![](https://support.nepton.com/hc/article_attachments/25052088606621)
In the menu, you can change the device's local network settings, configure an encrypted server connection, and restart the device. Encrypted server connection is only needed in situations where there is a firewall in use that reopens the connection. On the next page, you can change settings related to the user experience:
Automatic logout delay  
Automatic restart cycle  
Allowing login with a PIN code  
Allowing quick clocking  
Terminal language
