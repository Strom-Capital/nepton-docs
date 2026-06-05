---
id: 24730787957021
title: Nepton Flexim troubleshooting
url: https://support.nepton.com/hc/en-gb/articles/24730787957021-Nepton-Flexim-troubleshooting
locale: en-gb
category: Support
category_id: 360000446658
section: Troubleshooting
section_id: 360005896337
section_path:
- Terminals
- Troubleshooting
labels: []
promoted: false
updated_at: '2026-04-27T09:46:19Z'
edited_at: '2025-02-21T11:55:55Z'
---

# Nepton Flexim troubleshooting

Troubleshooting with Nepton Flexim terminals.
## The terminal is disconnected
If the terminal is offline, you will see a red bar at the bottom of it. Logging cannot be done on the terminal in offline mode (NOTE: Quick clocking mode works also in offline mode). The terminal tries to connect to the server at regular intervals. Often the offline situation resolves itself within a short period of time. However, if the terminal cannot connect to the service, test the functionality of the internet connection first. The functionality of the network can be tested by connecting another device to it, and checking if the connection works with it.
If there is a firewall that re-establishes HTTPS connections, the terminal must be set to "allow certificate errors". See [terminal management settings](<https://support.nepton.com/hc/en-gb/articles/24730505042077>) for help.
If the network connection to the time.nepton.com server is slow, you can increase the connection waiting time by entering a value in milliseconds (ask the IT department to contact Nepton's customer service).
REQUESTTIMEOUT=15000 => 15 seconds. Default is 5 seconds = 5000 ms.
## The terminal is not reacting to anything
Sometimes the terminal can go into such a state that it does not react to anything, i.e. it is stuck. It is a computer with an operating system and like any computer, the terminal can stop responding to inputs. The simplest way to fix the situation is to turn off the device, which is done by disconnecting the device's power cord. First, the device must be removed from the wall mount by unscrewing the screw in its lower part. The terminal can be turned around to get access to the power cord. Now the power cord can be disconnected from the device. After disconnecting, wait a moment and reattach the cord. Note: The device can be connected either with a POE cable, or the power cord and network cables can be separate.
## The terminal is slow
If the terminal is slow, this may be due to the device's software or network connection. The device should be restarted and the functionality of the network connection tested with another device. The restart is done through the help menu. On the main view, press the question mark button, from which you can press the Reboot button from the menu that opens. This can be done by any user without a management PIN code. The same function can also be found in the management menu that opens behind the management PIN code. The reboot will take a few minutes.
![](https://support.nepton.com/hc/article_attachments/25055851498013)
Another action to take on your device is to make sure it is updated to the latest software version. The current version of the device is displayed in the menu that opens behind the question mark symbol. Check this and contact Nepton's customer service to perform a possible software update.
## Reporting a problem with terminal
If the device is still not working after following the instructions in this article, contact Nepton's customer service to resolve the situation. Instructions for filing a fault report can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002588797>).
## Instructions for IT department
  * Login to the device with SSH: root / password
  * Test the network connection 
    * Nameservice: nslookup google.com
    * ![](https://support.nepton.com/hc/article_attachments/25055823152157)
    * Timeservice: date
    * ![](https://support.nepton.com/hc/article_attachments/25055823153565)
    * ntpq -p
    * ![](https://support.nepton.com/hc/article_attachments/25055851502365)
    * Network
    * traceroute -Il elisa.fi
traceroute to elisa.fi (195.197.95.175), 30 hops max, 38 byte packets
1 * * *
2 * * *
3 * * *
4 * * *
5 * * *
6 * * *
7 * * *
8 * * *
9 elisa.fi (195.197.95.175) 7.531 ms (246) 7.437 ms (246) 4.281 ms (246)
    * Server connection and login issues
The log details show if the server is connected and what happens when logging in. The log details can be passed on to Nepton customer service for investigation.
/tmp/ita.log   
/tmp/itaio.log  
/var/local/ita/ita.log.0  
/var/local/ita/itaio.log.0  
/var/local/ita/itaupgrade/itaupgrade.log
