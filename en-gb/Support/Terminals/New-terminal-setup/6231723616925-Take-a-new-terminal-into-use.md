---
id: 6231723616925
title: Take a new terminal into use
url: https://support.nepton.com/hc/en-gb/articles/6231723616925-Take-a-new-terminal-into-use
locale: en-gb
category: Support
category_id: 360000446658
section: New terminal setup
section_id: 360002103958
section_path:
- Terminals
- New terminal setup
labels:
- Hatteland
- Nepton touch
- leimaustunniste
- kirjauspääteohje
- työpöytäpääte
promoted: false
updated_at: '2025-02-04T12:25:09Z'
edited_at: '2025-02-03T05:54:45Z'
---

# Take a new terminal into use

The instructions below will help you get terminals up and running in a customer environment. If you haven't ordered your new terminals yet, please contact your service provider.
Before the terminal arrives you can already save the RFID tag identifier in each employee's information. Please see the guidance [here.](<https://support.nepton.com/hc/en-gb/articles/360002425517>)
Once your new terminals have arrived, you can follow the steps below to get the device connected, online, and ready for end-users. If any step is unclear, or you simply need some help, please contact your service provider.
## Nepton Touch
### Setup steps
**Before starting:** you will need an active customer environment configured on the Nepton platform. If you need assistance with this, please contact your service provider.
**1)** Unpack the device. You should find the following parts:
  * Quick start guide paper
  * Terminal
  * Power adapter and extension cord
  * Adjustable wall mount & flush wall mounting brackets


**2)** Connect and power on the device
  * Connect an Ethernet cable that provides access to the internet
  * If the device is supplied with an external RFID reader, connect it to the USB connector next to the Ethernet cable
  * Connect the power adapter to the terminal
  * Connect the power adapter to a power source. The terminal will automatically turn on. 
    * There is also a power button on the top of the device if needed


The terminals do not directly support PoE power supply, but the use of PoE requires at least the purchase of a separate PoE splitter, which divides the network cable into a power cord and a network cable. These are connected to the Nepton Touch terminal. In addition, the use of PoE naturally requires that the network cable be powered. This may not be the case by default. To enable this, a PoE injector should be installed. The required equipment according to the PoE+ standard can be obtained directly by the customer or partner or they can be purchased through Nepton.
![20220810_101619s.jpg](https://support.nepton.com/hc/article_attachments/6260761122717)
_Power and Ethernet connections_
![20220810_095248s.jpg](https://support.nepton.com/hc/article_attachments/6260761115421)
_Power button - The terminal powers on automatically whenever a power source is present, even after a powercut_
**3)** The terminal software will automatically start and attempt connecting. Once it has established a connection, it will automatically update to the latest version of the terminal software. If it is necessary to assign a **fixed IP address** to the device, the instructions can be found [here](<https://support.nepton.com/hc/en-gb/articles/7132764025373>).
  * It is normal for the device to initially appear offline during startup, and also to restart and show multiple different windows during the automatic update and deployment process. New desktop shortcuts will also appear as the first-time setup is carried out. This process can take several minutes.
  * If the device continues to indicate it is offline for more than 15 minutes or encounters other problems, please see the [Connectivity troubleshooting](<https://support.nepton.com/hc/en-gb/articles/360002588757>) article and contact your network administrator


The terminal will acquire an IP automatically, but if you need to manually configure a specific one, or find out it's network information, please see the [Find or edit a terminal's network information](<https://support.nepton.com/hc/en-gb/articles/360007577678>) article.
**4)** Once the device has started and updated, it will wait to be linked to a customer environment, by organisation Nepton administrator.  
While waiting, the terminal will show it's assigned terminal Id on the screen. Take note of this number for use in the next step. If at this point there is already a login view on the screen, go to step 7.
**5)** Link the device to the customer environment using the terminal Id.
  * Login to **Nepton as an administrator** , and visit Employees > Administration > Terminals.
  * Under the 'Add' heading, enter the new terminal's Id and click the 'Save' button
  * See [Add a terminal](<https://support.nepton.com/hc/en-gb/articles/360004790097>) for more information on this step.
  * If you have any problems with this step, please contact your service provider


**6)** After being added to the customer environment, the terminal will automatically download settings so that it can be used by the end-users. It can take a little time for the terminal to receive this change, and it may automatically restart during this step.
**7)** Once connected to the customer environment, the terminal will show the login screen. It is recommended that the device and software are tested with at least one user. If the terminal is not working as expected, please check out the [terminal troubleshooting articles](<https://support.nepton.com/hc/en-gb/sections/360005896337-Troubleshooting>).
For end-users to log in to terminals and make records, they must have the method of identification linked to their personnel data in Nepton (PIN code or RFID tag number).
**8)** For the best experience and performance, mount and adjust the angle of the device using the included wall mount, and remove the protective films from the touch screen and reader. These usually come away easily just using your fingers.
It is also possible to install the terminal in a vertical position (Portraid) and the operating system supports this, but the service is not designed to scale to that display format.
If the terminal is supplied with an external RFID reader, attach it with double-sided tape over the device's built-in reader module, the point marked in yellow in the picture.
![Attaching_RFID_reader.png](https://support.nepton.com/hc/article_attachments/7108911705245)
The terminal is now ready for use! It is configured to automatically update and start the terminal software and will show the terminal login screen when ready.
### Troubleshooting
Having trouble with one of the setup steps? Please check out the [terminal troubleshooting articles](<https://support.nepton.com/hc/en-gb/sections/360005896337-Troubleshooting>).
## Nepton Flexim
### Setup steps
### Troubleshooting
