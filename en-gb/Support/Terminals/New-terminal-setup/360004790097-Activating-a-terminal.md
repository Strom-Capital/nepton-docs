---
id: 360004790097
title: Activating a terminal
url: https://support.nepton.com/hc/en-gb/articles/360004790097-Activating-a-terminal
locale: en-gb
category: Support
category_id: 360000446658
section: New terminal setup
section_id: 360002103958
section_path:
- Terminals
- New terminal setup
labels: []
promoted: false
updated_at: '2026-01-30T11:19:38Z'
edited_at: '2026-01-30T11:19:38Z'
---

# Activating a terminal

An administrator can activate a terminal into Nepton service with this guidance.
## New terminal behaviour after powering up
New terminals will automatically install after powering up. This should not take more than a couple of minutes. After the initial installation the terminals will wait for activation. Eventually there will be a notice similar to the following:
![mceclip2.png](https://support.nepton.com/hc/article_attachments/8598215690397)
(Terminal may display its messages in Finnish or other language selected, see the exact Finnish messages in the [Finnish version of this guide](<https://support.nepton.com/hc/fi/articles/360004790097>).)
At the lower edge of the screen the "Online" notice and the green background indicate that there is a connection to the service.
The terminal ID is shown in the notice displayed. It can also be found near the lower right corner of the screen. The ID is the numeric code after the # sign. Write down the ID for activating the terminal.
If there is no connection to the service the terminal may display an error message about the connection problem. Also, if the terminal ID displayed is #0 or a negative number with minus (-) prefix, this will indicate that the terminal has not been connected to the Nepton service.
Check that the device cables are correctly connected and, if necessary, restart the device. If the connection problems continue, check with the IT representative of your organization that there is access from your network to the following addresses:
  * <https://go.nepton.com/>
  * <https://time.nepton.com/>


## Activating terminal in Nepton service
You can activate a terminal in the Employees section of Nepton service.
Select **Employees > Administration > Terminals.**
Click Add new terminal. Add the terminal ID in the field reserved for it. Select **Save**.
![](https://support.nepton.com/hc/article_attachments/33604393257117)
If the activation was successful, there will be a notice: "Terminal added". If the device has already been activated, there will be a notice: "Terminal X is already reserved. Please check the id and try again."
![mceclip22.png](https://support.nepton.com/hc/article_attachments/8599803311645)
Double-check the terminal id directly from the terminal screen. If the id is correct and the terminal does not display information of an activated terminal (see below), follow the instructions above at "if there is no connection to the service".
## Activated terminal appearance
When a terminal has been activated successfully, it will display a login screen after a connection check done when starting up. The appearence of the terminal depends on if the PIN code login is in use.
### PIN code login not in use
When the setting **Worktime > Administration > Working community settings > Current status > Log in possible with the recording terminal **value is "PIN-code login not in use" (default)
![](https://support.nepton.com/hc/article_attachments/33604365328925)
or "Only RFID-login in use"
![](https://support.nepton.com/hc/article_attachments/33604348653981)
an activated terminal will display: "Place your ID on the reader and wait for the signal".
![mceclip19.png](https://support.nepton.com/hc/article_attachments/8599734003997)
### PIN code login in use
When the setting **Worktime > Administration > Working community settings > Current status > Log in possible with the recording terminal **value is "PIN-code login in use"
![](https://support.nepton.com/hc/article_attachments/33604348654621)
an activated terminal will display: "Login with PIN Code or RFID Tag".
![mceclip20.png](https://support.nepton.com/hc/article_attachments/8599734856093)
