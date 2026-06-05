---
id: 32259026029213
title: Creating a new notification
url: https://support.nepton.com/hc/en-gb/articles/32259026029213-Creating-a-new-notification
locale: en-gb
category: Support
category_id: 360000446658
section: Notifications
section_id: 32229019276445
section_path:
- Notifications
labels: []
promoted: false
updated_at: '2026-04-24T12:00:21Z'
edited_at: '2026-01-08T11:38:29Z'
---

# Creating a new notification

Premade notifications are available with the Worktime Pro service level and higher. Custom notifications are available with the Worktime Complete service level.
Notifications are automated email messages that can be sent on various topics to managers or employees. They help inform managers about events that require action in the system. Notifications can be scheduled and customised to meet your organisation’s needs using different settings, ensuring timely communication and relevant content.
This article explains how to create a new notification and how to use the Notifications view. More information about different types of notifications can be found in the articles [](<href>)[**Premade notifications**](<https://support.nepton.com/hc/en-gb/articles/32229098583965>) and [**Custom notifications**](<https://support.nepton.com/hc/en-gb/articles/32258952073757>).
## Notifications view
**The** **Notifications** section is visible only if the user has:
  * **Role:** Administrator
  * **Worktime role:** “Kaikki oikeudet” or an equivalent customer-specific worktime role that includes _High-level permissions > All higher and below level permissions_.


If the worktime role is lower than this, notifications cannot be created because they may be based on any data stored in Nepton.
Notification settings are managed in the menu **Worktime > Administration > Notifications**.
![](https://support.nepton.com/hc/article_attachments/32480281178909)
Add a new notification by clicking the **Add** button in the top right corner. Detailed instructions for creating a new notification are below.
At the top of the view, you can also see information about the **number of notifications sent** and the **number of recipients**. Notifications sent during the current day are shown in green next to the number as +1.
![](https://support.nepton.com/hc/article_attachments/32480281180189)
Next to the Add button there is a menu with option for **full screen view** and access the **help link**.
![](https://support.nepton.com/hc/article_attachments/32480252127645)
The view also includes **search** and **filter functions**.
![](https://support.nepton.com/hc/article_attachments/32480281184029)
Notification has **a menu** that allows you to **edit** or **delete** the notification. You can also open a notification for editing by **clicking its name**.
![](https://support.nepton.com/hc/article_attachments/32480281185181)
## Steps to create a notification
Notification settings are managed in the menu **Worktime > Administration > Notifications**.
![notifications1.png](https://support.nepton.com/hc/article_attachments/32480281178909)
New notification is created by clicking the **Add** button in the top right corner.
![](https://support.nepton.com/hc/article_attachments/32480281186333)
This opens the **Add notification** view, where you define the **Name** and **Type** of the notification.
You can choose from **premade notifications** or create **custom notifications** depending on your service level. Premade notifications are available with Worktime Pro, and custom notifications with Worktime Complete.
Once the Name and Type are selected, click **Add**.
![](https://support.nepton.com/hc/article_attachments/32480281188893)
Once an notification has been added, the settings for that notificaiton will be displayed. The settings are in the panel on the right side of the view.
![](https://support.nepton.com/hc/article_attachments/32480252138269)
There are multiple tabs where you can edit settings related to different themes:
  * **Notification**
  * **Preview and send**
  * **Schedule**
  * **Advanced**


At the top of the view, arrows allow you to easily navigate between notifications.
The three dots in the top left corner provide options for **full screen view** , **pinning** , and a **help link**. The cross in the top right corner closes the view.
To ensure the newly created notification starts sending emails to recipients, you must define at least a **person group/payment group** in the Notification tab and a **schedule** in the Schedule tab. These are mandatory settings; without them, notifications will not be sent. More details on defining settings are below.
![](https://support.nepton.com/hc/article_attachments/32480281191069)
When the notification settings have been configured, the notification schedule will be displayd in **the main view**. If the schedule settings are incomplete, it will appear in grey, indicating the notification is not active.
![](https://support.nepton.com/hc/article_attachments/32480252139933)
## Defining notification settings
### Notification
In the notification settings view, you define the content of the email notification and its recipients.
**Fields:**
  * **Name:** Give the notification a clear name that describes its purpose (for example, _Unapproved events_).
  * **Description:** Add a detailed description of the notification’s content, person groups, or intended use.
  * **Type:** Select the notification type. The available option is Email.
  * **Select person groups / Select payment groups** _(mandatory)_**:** Defines which groups the notification applies to. Inheritance is not supported, so each group must be selected individually.
  * **Message section**
    * **Recipients** : Choose who will receive the notification (managers, employees, substitutes).
    * **Notification title** : Appears as the email subject line.
    * **Notification content** : The body text of the message. You can use variables defined in the Advanced settings rule so that the content adapts automatically.
      * Variables for premade notifications are `[ApprovalLink]`, `[PersonName]` & `[UnapprovedCount]`
    * **Other languages:** The message content can be translated into different languages.
  * **Buttons**
    * **Save** : Saves the changes made.
    * **Cancel** : Closes the view without saving changes.
    * **Delete** : Permanently deletes the notification.


![](https://support.nepton.com/hc/article_attachments/32480252141213)
### Preview and send
On the Preview and Send tab, you can test the notification and send it manually using data from a selected period. This feature is useful when you want to send the notification immediately without scheduling.
  * **Date range:** Defines the time range from which data is retrieved for the notification.
  * **Preview:** Displays the content of the notification. This allows you to check that the message and recipients are correct.
  * **Send:** Starts sending the notification using data from the selected period.


The **History** section shows previously previewed and sent notifications, their status, start time, sender, and the period used. If no notifications have been sent, the section is empty. If a preview or sending fails, a yellow triangle appears next to the row. Clicking the triangle provides more details about the error.
![](https://support.nepton.com/hc/article_attachments/32480281194013)
### Schedule
On the Schedule tab, you define when the notification is active and the schedule for sending it. Schedule allows notifications to be enabled or disabled.
Schedule options appear when you click **Add**.
![](https://support.nepton.com/hc/article_attachments/32480252143901)
A warning appears on the tab and at the top of the view if schedule is not currently active. To activate schedule, define the validity period and save the settings.
**Fields:**
  * **Schedule enabled from** _(mandatory):_ Date and time can be set to the current moment if the schedule should be active immediately. It can also be activated at a future time. Technically, it is possible to set a past date, but this will cause the notification to run for previous days (max. 3 days back). This is not a typical use case. Time zone: Europe/Helsinki.


After setting the start or end date fields, also set the time. Without a time, the service will not save the information.
![](https://support.nepton.com/hc/article_attachments/32480281196445)
  * **Schedule validity to** _(optional):_ End date if you want to limit the schedule to a specific period. If the field is empty, the schedule remains active indefinitely. Time zone: Europe/Helsinki.
  * **Description:** A freely defined name for the schedule. This is pre-filled with the notification details by default. The description is shown in the list of schedules (Worktime > Administration > Working community settings > Integrations > Integration scheduling) and helps identify different schedules.
  * **Daily interval rule:** The rule that controls how the schedule repeats and defines on which days it runs. Clicking the magic wand icon opens a tool where you can select predefined rules from a list.
  * **Daily start time:** Defines the time of day when the execution occurs. There are no restrictions on the time, but it is recommended to avoid times during maintenance windows or periods of high system load. Information about maintenance windows can be found [](<https://support.nepton.com/hc/fi/articles/360006554777>)
  * **Import/export period start date rule** and **end date rule:** Controls which period data is retrieved for the notification. If these fields are left empty, the previous month’s data is selected by default. Clicking the magic wand icon opens a tool where you can select predefined rules from a list.


The **History section** shows previously sent notifications, their status, start time, and the period used. If no notifications have been sent, the section is empty. If sending fails, a yellow triangle appears next to the row. Clicking the triangle provides more details about the error.
![](https://support.nepton.com/hc/article_attachments/32480252150429)
### Advanced
The Advanced tab manages rulesets for notifications _(available only if the Worktime Complete service level is active)_. More details about rulesets and how to create them can be found in the article [**Custom notifications**](<https://support.nepton.com/hc/en-gb/articles/32258952073757>). Rlesets define the criteria for selecting the data included in the notification. In this view, you can edit the SQL-based rule that retrieves the required events and persons.
  * **Rule:** Displays the SQL query that defines the notification content. The query can use predefined variables and include customer-specific rules.
    * Instructions for where to add customer-specific rules are shown at the top of the premade notifications.
  * **Buttons**
    * **View rule results:** Opens a new window where you can test the rule.
    * **Save** : Saves the changes made.
    * **Cancel** : Closes the view without saving changes.
    * **Delete** : Permanently deletes the notification.


![](https://support.nepton.com/hc/article_attachments/32480252151453)
