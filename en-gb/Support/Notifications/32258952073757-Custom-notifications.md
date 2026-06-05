---
id: 32258952073757
title: Custom notifications
url: https://support.nepton.com/hc/en-gb/articles/32258952073757-Custom-notifications
locale: en-gb
category: Support
category_id: 360000446658
section: Notifications
section_id: 32229019276445
section_path:
- Notifications
labels: []
promoted: false
updated_at: '2026-01-08T11:41:44Z'
edited_at: '2026-01-08T11:41:44Z'
---

# Custom notifications

[**Premade notifications**](<https://support.nepton.com/hc/en-gb/articles/32229098583965>) are available with the Worktime Pro service level and higher. Custom notifications are available with the Worktime Complete service level.
This article covers custom notifications. For more information about the Notifications view and creating notifications, see the article [**Creating a notification**](<href>).
## What are custom notifications?
Custom notifications allow you to create notifications tailored to your organisation’s needs. They are based on rulesets (SQL) that define which people and events are included in the notification. Rulesets can flexibly define:
  * The data to retrieve for the notification targets (e.g., persons, events, balances).
  * Conditions under which the notification is sent.
  * Filters based on person groups, pay groups, or other criteria.


Since the content of custom notifications is determined by the ruleset, they may include potentially sensitive information (e.g., sick leave details). Always ensure that the notification does not disclose information that must not be shared via email or that users would not normally see in the customer environment.
## Defining a custom notification
A custom notification is defined on the **Advanced** tab, where rules are managed. Rulesets determine the criteria for selecting the data included in the notification. In this view, you can edit the SQL-based rule that retrieves the required events, persons, and groups from the system’s database tables.
**Advanced view:**
  * **Rule:** Displays the SQL query that defines the notification content. The query can use predefined variables and include customer-specific rules.
  * **Buttons**
    * **View rule results:** Opens a new window where you can test the rule.
    * **Save** : Saves changes made to the rule.
    * **Cancel** : Closes the view without saving changes.
    * **Delete** : Permanently deletes the notification.

![notification17.png](https://support.nepton.com/hc/article_attachments/32480081670941)
## Structure of a rule
A typical rule includes the following parts:
  * **SELECT** – Defines which data is included in the notification (e.g., user ID, name, number of events). Each should have an alias (**AS**) so the data can be used in the email message.
  * **FROM** and **JOIN** – Joins the necessary tables, such as events (`UserEventData`) and users (`UserData`). Additional details can be retrieved from other tables, such as `UserInfoData`.
  * **WHERE** – Filters only specific data (e.g., unapproved events, certain groups).
  * **GROUP BY** – Groups data by person or other logic.
  * **HAVING** – Defines conditions for grouped data (e.g., number of events > 0).


## Common tables and fields
Here is basic information about the most common data needed for building notification rule sets. All database table contents are described in the article [**Database tables**](<https://support.nepton.com/hc/en-gb/articles/360002489257>).
**UserEventData**
  * `ActivityId` – event identifier
  * `StartDatetime` – event start time
  * `isApproved` – approval status (N = not approved)


**UserData**
  * `UserId` – person identifier
  * `firstName`, `lastName` – name
  * `UserGroupCode` – person group


**UserSalaryData**
  * `Amount` – value in seconds
  * `CompensationType` – indicates row type (e.g., `Accrual` = accrual)
  * `AccrualType` – indicates accrual target (e.g., `Balance` = worktime balance)
  * `SalaryRenderingDate` – date related to the event or accrual


## Person group and pay group filtering
In notification rule sets, you can filter targets based on person group or pay group. Filter conditions are added to the **WHERE section** of the rule, as they limit the rows included before grouping. Adding these rules creates a selector for person group or pay group in the notification interface.
### Person group filter
Add the following condition to the rule. The rule parameter creates a selection in the Notification view where person groups can be chosen.
[code]
    WHERE 
      ued.isApproved = 'N'  -- unapproved events, replace with your own condition
      AND ud.UserGroupCode IN (
        [notificationPersonFilter | {select_user_groups} | persongroupselect | ]
      )  -- person group filter
[/code]
### Pay group filter
Add the following condition to the rule. The rule parameter creates a selection in the Notification view where pay groups can be chosen.
[code]
    WHERE 
      ued.isApproved = 'N'  -- unapproved events, replace with your own condition
      AND uid.InfoTypeName = 'NeptonPaymentGroupCode_SDSQL'
      AND uid.Value IN (
        [notificationPersonFilter | {Select payment groups} | paymentgroupselect | ]
      )  -- pay group filter
[/code]
## Editing premade notifications
At the top of the rule for premade notifications, there is a section where customer-specific modifications must be added. If this is not done, these modifications will be lost if Nepton updates the notification functionality for all customers.
If you need to make broader changes to premade notifications, create a custom notification and copy the premade notification rule as a starting point.
[code]
    /* --- Add customer-specific notification rules BELOW this line --- */
      
     
    /* --- Add customer-specific notification rules ABOVE this line --- */
[/code]
## Examples of rules
### Custom notification: Balance over 40 hours
This notification lists persons whose worktime balance exceeds a defined threshold on the end date of the export period. The balance value is retrieved from accrual data (`AccrualType = Balance`) directly from the last day of the period, showing the current balance status.
  * The rule **sums the balance (Amount)** in seconds and converts it to hours.
  * The last line sets the **balance threshold (40 hours = 144000 seconds)**.


[code] 
    SELECT 
      usd.UserId AS 'affectedUserId', 
      -- Identifier of the person targeted by the notification
      CONCAT(ud.firstName, " ", ud.lastName) AS 'PersonName', 
      -- Person's name for the notification
      ROUND(
        SUM(usd.Amount) / 3600.0, 
        2
      ) AS 'BalanceHours' -- Calculate balance in hours. Amount is in seconds, so divide by 3600 and round to two decimals.
    FROM 
      UserSalaryData usd -- Table containing interpreted events and balance data
      INNER JOIN UserData ud ON ud.UserId = usd.UserId -- Join basic person data (name, group code)
    WHERE 
      usd.CompensationType = 'Accrual' -- Filter accrual rows
      AND usd.AccrualType = 'Balance' -- Select balance accrual
      AND usd.SalaryRenderingDate = DATE(:ExportPeriodEnd) -- Retrieve value for the last day of the period (snapshot)
      AND ud.UserGroupCode IN (
        [notificationPersonFilter | {select_user_groups} | persongroupselect | ] 
        ) -- Activate person group filter, applies only to selected groups
    GROUP BY 
      usd.UserId -- One row per person
    HAVING 
      SUM(usd.Amount) > 144000 -- Send notification if balance exceeds 40 hours (144000 seconds)
[/code]
### Premade notification: Unapproved events by person group
[code]
    /* --- Update this rule with the latest from the notification integration (unapproved events) template:[Yes] --- */
    
    SELECT 
      ued.userId as 'affectedUserId', 
      CONCAT(ud.firstName, " ", ud.lastName) AS 'PersonName', 
      COUNT(ued.ActivityId) AS 'UnapprovedCount' 
     
      /* --- Add customer-specific notification rules BELOW this line --- */
    
      
     
      /* --- Add customer-specific notification rules ABOVE this line --- */
    
    FROM 
      UserEventData ued 
      INNER JOIN UserData ud ON ued.UserId = ud.UserId 
    WHERE 
      ued.isApproved = 'N' 
      AND ud.UserGroupCode IN (
        [notificationPersonFilter | {select_user_groups} | persongroupselect | ]
      ) 
    GROUP BY 
      affectedUserId 
    HAVING 
      UnapprovedCount > 0
[/code]
### Premade notification: Unapproved events by payment group
[code]
    /* --- Update this rule with the latest from the notification integration (unapproved events) template:[Yes] --- */
    
    SELECT 
      ued.userId as 'affectedUserId', 
      CONCAT(ud.firstName, " ", ud.lastName) AS 'PersonName', 
      COUNT(ued.ActivityId) AS 'UnapprovedCount' 
     
      /* --- Add customer-specific notification rules BELOW this line --- */
    
      
     
      /* --- Add customer-specific notification rules ABOVE this line --- */
    
    FROM 
      UserEventData ued 
      INNER JOIN UserData ud ON ued.UserId = ud.UserId 
      LEFT JOIN UserInfoData uid ON ued.UserId = uid.UserId 
      AND datetime(ued.StartDatetime) BETWEEN uid.ValidFrom 
      AND uid.ValidTo 
    WHERE 
      ued.isApproved = 'N' 
      AND uid.InfoTypeName = 'NeptonPaymentGroupCode_SDSQL' 
      AND uid.Value IN (
        [notificationPersonFilter | {select_groups_of_persons_to_check_for_unapproved_events} | paymentgroupselect | ]
      ) 
    GROUP BY 
      affectedUserId 
    HAVING 
      UnapprovedCount > 0
[/code]
## Using rule data in the notification email
Data defined with **AS** aliases in the rule can be used in the message by writing them inside square brackets on the Notification tab when editing the message content. For example: `Hello [PersonName], your balance is [BalanceHours] hours.`
Data is named using **AS** aliases, as shown in the rule below for `'PersonName'` and `'BalanceHours'`.
![](https://support.nepton.com/hc/article_attachments/32480052510621)
After this, the **AS** aliases defined in the rule can be used in the message by writing them between square brackets, e.g. `[PersonName]`, so the message content updates automatically with the latest data.
![](https://support.nepton.com/hc/article_attachments/32480052512157)
