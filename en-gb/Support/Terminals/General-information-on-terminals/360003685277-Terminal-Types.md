---
id: 360003685277
title: Terminal Types
url: https://support.nepton.com/hc/en-gb/articles/360003685277-Terminal-Types
locale: en-gb
category: Support
category_id: 360000446658
section: General information on terminals
section_id: 360005942558
section_path:
- Terminals
- General information on terminals
labels:
- leimauspäätteet
- kirjauspääte
- työaikaterminaali
- malli
- mallit
promoted: false
updated_at: '2025-09-03T07:04:24Z'
edited_at: '2025-04-04T07:36:36Z'
---

# Terminal Types

Below is an outline of the different terminal hardware currently offered by Nepton. If you need information about an older terminal model, please make a support request.
**For marketing information, please visit<https://nepton.com/challenges-and-solutions/terminals/>**
## General information about terminals
Terminals record events in real time.
Real-time recording is displayed in the calendar and table views as an icon between the time and the event type name.
The Event listing report displays the terminal ID if the event was recorded entirely with a terminal. In a situation where recording was started and ended with a different terminal, the ID of the terminal with which the event was started is displayed.
When using Nepton Rugged terminal, there is no icon in the calendar or table view and the Event listing report does not have the terminal ID. This is due to the technology used to communicate with the service, and the technology of Nepton Rugged terminals does not enable the above-mentioned features.
![](https://support.nepton.com/hc/article_attachments/26371303018781)
## Nepton Touch
The device uses modern materials and has a built-in speaker and RFID reader. It replaces the original Nepton Touch devices from September 2022 onwards.
Terminals can be used when offline as they have space for saving thousands of records into memory until they are reconnected. Offline records are transferred to Nepton as soon as the device is back online.
![p__telaite_uusi.png](https://support.nepton.com/hc/article_attachments/6388171240989)
### Main features
  * Log in with a PIN or RFID
  * High resolution 10.1" industrial A+ grade LCD touch screen
  * Realtech RTL811E gigabit network card (RJ45/Ethernet)
  * Can be used immediately after being connected to the internet
  * Easy wall mounting with included basic VESA-wall mount kit
  * Windows 10 IOT Enterprise LTSC operating system
  * Onboard SSD hard drive and Intel Celeron CPU for performance
  * Can be used as a cafeteria terminal
  * Existing access control tags can be used
  * RFID reader complying with ISO14443-A and ISO14443-B standards at 13,56 MHz: 
    * Example compatible tags: MIFARE® DESFire: UID + Application files , MIFARE® Classic: UID + Sectors, MIFARE® Ultralight UID + pages, MIFARE® Plus UID security levels 1 and 3, MIFARE® SmartMX (MIFARE® Classic and MIFARE® DESFire EV1 emulation modes), NFC (UID), Mifare Classic 7 Byte UID + sectors, Legic, ISO15693 (UID)
  * Possibility to use external RFID-reader to support a wide range of RFID tags. Guidance to the external readers' supported tags can be found [here](<https://support.nepton.com/hc/en-gb/articles/10357648361757>).
  * POE+ and POE++ distribution devices can be used for power supply (30 Watt power requirement). The distribution device must have a separate power output (e.g. Planet POE-172S), which is connected to the device's power connector. If there is no PoE supply in the ethernet cable, a separate PoE injector is still needed (e.g. Ernitec Electra-P2-60W).
  * Rated to operate between -20 to +70 degrees centigrade
  * Constructed from an Aluminum alloy for durability
  * Device measurements:  
Height 19,4 cm  
Width 37,4 cm  
Depth 6 cm


### Cleaning the touch screen
  * Use a soft, clean cloth, a microfiber cloth is recommended.
  * Moisten the cloth lightly with water. You can also use cleansers meant for touch screens. Remember that the device should not get too wet.
  * Wipe the screen carefully using the cloth.


## Nepton-Flexim terminal device
The Nepton-Flexim terminal was introduced as part of Nepton’s device offering in the fall of 2024. The terminals come with their own Nepton software (production release version 5.0.1). The following Nepton-Flexim terminal hardware models already in use can be updated to the software produced by Nepton:
  * SACCTP1_121000 : prox tag reader
  * SACCTM1_121000 : mifare tag reader
  * SACCTC1_121000 : ABLOY SEOS tag reader
  * SACCWPM_121000 (tag reader that supports multiple tags: prox, mifare, SEOS)
  * SACCWPP_121000 (tag reader that supports multiple tags: prox, mifare, SEOS)


Customers using the aforementioned terminal models can check from their terminals whether they can be updated to the new Nepton software as follows: if the serial number found on the device starts with the number three (3), the device can be updated.
New device model SACCWPP_121000 can be obtained from Nepton directly.
![](https://support.nepton.com/hc/article_attachments/23497149479325)
Key functionalities:
  * **Login** : With a tag, PIN code (can be enabled/disabled per terminal), or Quick Recording (showing the tag to the reader starts/stops the task. Quick Recording can also be enabled/disabled per terminal).


![](https://support.nepton.com/hc/article_attachments/23497149484829)
  * **Event logging** : In the same way as on the Nepton Touch device.


![](https://support.nepton.com/hc/article_attachments/23497133001245)
  * **Selectable buttons on the home screen** : Eight (8) buttons at a time. If more buttons are in use, the page turn arrow acts as an indicator.


![](https://support.nepton.com/hc/article_attachments/23497149495837)
  * **Automatic logout** : The terminal logs the user out by default after 20 seconds of inactivity. The logout delay can be changed.
  * **Supplement logging** : Possible after starting an event. 
    * **Supplements tab** : Shows four (4) selectable supplements.
    * **Supplement type and default values** : Come according to the Nepton settings group.
    * **Quick selections** : Supplements can be increased (plus button) or decreased (minus button) at user-defined intervals, for example, 5, 10, or 15 minutes at a time.


![](https://support.nepton.com/hc/article_attachments/23497133012125)
  *     *       * **Pen icon (see screenshot above)** : Allows for a more precise, minute-by-minute value alteration


![](https://support.nepton.com/hc/article_attachments/23497149506589)
  * **Overtime target selection** : From the **Overtime tab** , the overtime target can be changed. Options are visible according to the person’s settings group.


![](https://support.nepton.com/hc/article_attachments/23497133018909)
  * **Project allocation** : From the **Projects tab** , the desired project allocation for the work can be selected. The last recorded options are shown. Using the search function, options other than the last recorded ones can be displayed. The project can also be selected with a barcode reader, provided the person is logged into the terminal with an identifier. After reading the barcode, the project allocation starts, and the person is automatically logged out of the terminal.


![](https://support.nepton.com/hc/article_attachments/23497133022109)
  * **Terminal setup** : A new terminal announces its number when it starts, which can be used to connect the terminal to the Nepton environment.


## Nepton Rugged
Nepton Rugged (NFC TimeClean Basic) device is compact and rugged with a built-in battery and mobile connection for use in remote, on the move, or hard-to-wire areas.
![](https://mlavatqvr5rz.i.optimole.com/w:702/h:702/q:90/f:best/https://nepton.fi/wp-content/uploads/nepton_rugged.png)
### Main features
  * Log in with a PIN or RFID
  * Compact design that can be used almost anywhere thanks to an onboard battery and GSM mobile internet connection
  * Easy wall mounting
  * Digital text display with backlight
  * RFID reader complying with ISO14443-A and ISO14443-B standards at 13,56 MHz: 
    * Example compatible tags: MIFARE® DESFire: UID + Application files , MIFARE® Classic: UID + Sectors, MIFARE® Ultralight UID + pages, MIFARE® Plus UID security levels 1 and 3, MIFARE® SmartMX (MIFARE® Classic and MIFARE® DESFire EV1 emulation modes), NFC (UID), Mifare Classic 7 Byte UID + sectors, Legic, ISO15693 (UID)
  * IP66 case, rated to operate between 0 to +50 degrees centigrade
  * Coloured lights, buzzer and speaker
  * Constructed from plastic for light-weight portability
