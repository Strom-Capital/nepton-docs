---
id: 360003461977
title: Take a terminal into use (Hardware models before September 2022)
url: https://support.nepton.com/hc/en-gb/articles/360003461977-Take-a-terminal-into-use-Hardware-models-before-September-2022
locale: en-gb
category: Support
category_id: 360000446658
section: New terminal setup
section_id: 360002103958
section_path:
- Terminals
- New terminal setup
labels:
- Deploy
- Quick start
- seinäpääte
promoted: false
updated_at: '2022-10-07T08:44:06Z'
edited_at: '2022-08-16T06:42:12Z'
---

# Take a terminal into use (Hardware models before September 2022)

The following instructions are intended for hardware models delivered before September 2022.
For the latest instructions please see the dedicated article [here](<https://support.nepton.com/hc/en-gb/articles/6231723616925>)
The instructions below will help you get terminals up and running in a customer environment. If you haven't ordered your new terminals yet, please see [Order a new terminal](<https://support.nepton.com/hc/en-gb/articles/360003612837>).
Once your new terminals have arrived, you can follow the steps below to get the device connected, online, and ready for end-users. If any step is unclear, or you simply need some help, please contact your service provider.
## Setup & Getting started
**Before starting:** you will need an active customer environment configured on the Nepton platform. If you need assistance with this, please contact your service provider.
**1)** Unpack the device
  * If you are setting up an Idesco device, you will need to remove the external cover on the rear, and feed cables through the rubber gasket to the inputs inside. See [Idesco hardware setup (Wall mounting)](<https://support.nepton.com/hc/en-gb/articles/360003778457>) for more information.


**2)** If you have an external RFID reader, connect it to one of the terminal's USB ports
**3)** Connect an Ethernet cable, that provides access to the internet, to the terminal
**4)** Unless utilising Power over Ethernet (PoE), attach the device to a power source
  * Not all terminals support PoE. Please consult your device's technical documentation. At the moment only Idesco Touch devices support PoE power supply.
  * PoE requires the other end of the Ethernet cable to be connected to PoE switch or injector. Otherwise, the terminal will not get power from the Ethernet cable, even if it does support it


**5)** The device will automatically startup and attempt connecting. Once it has established a connection, it will automatically update to the latest version of the terminal software.
  * It is normal for the device to initially appear offline during startup, and also to restart and show multiple different windows during the automatic update and deployment process
  * If the device continues to indicate it is offline for more than 15 minutes or encounters other problems, please see the [Connectivity troubleshooting](<https://support.nepton.com/hc/en-gb/articles/360002588757>) article and contact your network administrator


**6)** Once the device has started and updated, it will wait to be linked to a customer environment.  
While waiting, the terminal will show it's assigned terminal Id on the screen. Take a note of this for the following steps.
**7)** You can now link the device to the customer environment using the terminal Id. Login to Nepton as an administrator, and visit Employees > Administration > Terminals.
  * Under the 'Add' heading, enter the new terminal's Id and click the 'Save' button
  * See [Add a terminal](<https://support.nepton.com/hc/en-gb/articles/360004790097>) for more information on this step.
  * If you have any problems with this step, please contact your service provider


**8)** If you have an external RFID reader, contact your service provider to determine the length of the RFID code.
**9)** After having been added to the customer environment, the terminal will automatically download settings so that it can be used by the end-users. It may automatically restart during this step.
**10)** Your terminal is now configured to automatically start and update and will show the terminal login screen. Your device is now ready for use!
  * Depending on your setup, end-users can now use your preferred identification method to log in and make recordings.


For end-users to log in to terminals and make records, they must have the method of identification linked to their personnel data in the Nepton platform (e.g. a PIN number, RFID tag number, or Biometric data).
Unknown RFID tags will allow login and recording data before the tag has been assigned to a person. The recorded data will be attributed to the user when the RFID tag number is added to that person's data
## Switching off the terminal
**Olink**
-To turn off the app, touch the corner of the screen clockwise with your finger from the top left corner, top right corner, bottom right corner, and bottom left corner
\- Press the power button on the right for at least five seconds to turn off the terminal
**Idesco**
\- To turn off the app, touch the corner of the screen clockwise with your finger from the top left corner, top right corner, bottom right corner, and bottom left corner  
\- To turn off the terminal, press the Start button -> Suspend  
\- Disconnect the Ethernet cable (PoE power supply) or power cord
