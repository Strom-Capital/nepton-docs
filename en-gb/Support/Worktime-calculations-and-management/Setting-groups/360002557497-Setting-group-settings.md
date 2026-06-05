---
id: 360002557497
title: Setting group settings
url: https://support.nepton.com/hc/en-gb/articles/360002557497-Setting-group-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Setting groups
section_id: 360000707358
section_path:
- Worktime calculations and management
- Setting groups
labels:
- asetusryhmä
- asetukset
- setting group
- settings
promoted: false
updated_at: '2024-11-13T11:48:05Z'
edited_at: '2024-11-13T11:46:49Z'
---

# Setting group settings

Functions related to setting groups are managed in the **Work time** section under **Administration** -> **Setting Groups**.
You can view the settings for setting groups by selecting “**Setting Group Settings** ” from the **Action** menu and choosing the setting group you want to manage from the Setting Group menu. The settings for setting groups are categorized under their respective headings, which you can click on to view and modify settings related to that specific area.
## Principles of inheriting settings in Nepton
According to Nepton’s way of working, settings can be set on many different levels and then inherited from higher level to lower level. The inheritance order is as follows:
**Top Level:** Working community settings. Generally, only settings that apply organization-wide are configured at this level.
**Second Level:** Parent setting groups (setting groups that have no setting group above them, only the Working community setting level).
**Third Level:** Child setting groups (setting groups that are directly under a parent setting group or other sub-setting groups). Multiple child setting groups can be in the same chain.
**Final Level:** Person settings for each person. Settings made at this level take precedence. If a specific setting differs from the setting group or workplace level, the individual setting prevails. Managing individual-level settings can be challenging, so we recommend avoiding such configurations. More information about Person settings can be found [here](<https://support.nepton.com/hc/en-gb/articles/22964866012701-Person-settings>).
## Overview of Setting Group settings
You may have an overview of all the options visible in Setting Group settings -selection. Some of the settings are only visible in Nepton Worktime Management Pro or Complete -levels.
![](https://support.nepton.com/hc/article_attachments/20217017748893)
### Time, language & region
Under this section, you may choose the time zone and language that is in use in your deployment. For further details, please visit [this](<https://support.nepton.com/hc/en-gb/articles/360003994357-Time-language-and-region>) article.
### Recording terminal and current status
This section contains information about recording terminal and current status. More information from [this](<https://support.nepton.com/hc/en-gb/articles/360002560518-Work-time-terminal-and-current-status-view-settings>) article.
### Work Hours
**Work hours** section contains wide range of settings that are used in work time calculations.
![](https://support.nepton.com/hc/article_attachments/20217043489949)
**Rendering options** Here you can specify which day to display work events that span more than 24 hours. You can also set default work hours that the service suggests when creating new work events in the calendar view. More info can be found [here](<https://support.nepton.com/hc/en-gb/articles/360008777997-Rendering-options>).
**Event Types** : In this section, you can choose which event types are visible when recording an event in the calendar view, on the terminal, and when making mobile entries. You can also create new custom event types and define different behaviors for each event type. You can specify what information is shown when creating a new event and set the default event type for new entries on empty days. Additionally, you can configure default settings for the “sick leave” event type (default compensation type, whether it accrues vacation days, and the default for medical certificates).
**Absence Types:** From the “Absence Types” menu, you can select which absence types are visible when recording absence events. You can also set the default compensation method for each absence type and determine whether it accrues annual leave days. Please see more details in [this](<https://support.nepton.com/hc/en-gb/articles/360002520778-Event-types>) article.
**Quick start event types** Quick start events are a customisable, convenient, and quick way for employees to record fully or partially prefilled work events in Nepton Mobile. Read more about this feature [here](<https://support.nepton.com/hc/en-gb/articles/7074461491101-Quick-start-events>). **  
**
**Event locking and approval** Define settings related to locking and approval of events in the “Locking and Approval” section.
**Length of work day** : Set the default duration for a workday. After meeting work obligations, work hours are typically allocated to accruals, additional work, or overtime. For more information on determining workday duration, refer to the documentation [here](<https://support.nepton.com/hc/en-gb/articles/360002558417-Defining-the-length-of-work-day>).
**Permitted work times** Define the times during which work performed is considered work hours. You can set two different values for permitted work hours, which is useful, for example, when working night shift that spans over two different calendar days. More details on configuring permitted work hours can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002558597-Setting-up-permitted-work-times>).
**Expected Work times** Enable expected work times if you want overtime to accumulate before the scheduled shift or assumed work time. Learn more about configuring assumed work hours from [this](<https://support.nepton.com/hc/en-gb/articles/360002558617-Expected-work-times>) article.
**Rounding** Use the rounding function to round payable work hours to a specified minute value (e.g., rounded to the nearest five minutes, up or down). More about rounding [here](<https://support.nepton.com/hc/en-gb/articles/360002558557-Rounding-settings>).
**Lunch** Under this heading, set the default duration for lunch breaks. You can also define a minimum value for lunch breaks, which extends shorter lunch entries. Additionally, you can specify the minimum length of a work shift for the lunch hour to be considered in work hour calculations. Automatic deduction of lunch breaks can be used alongside manual lunchtime entries. Set a default time for lunch breaks to be deducted. Please find more details from [this](<https://support.nepton.com/hc/en-gb/articles/360002558757-Lunch-break-settings>) article.
**Paid time earned after normal work** : Choose whether to calculate hours based on planned shift duration (“Yes”) or based on the workday and workweek duration (“No”) for certain event types such as sick leave, other absences, and travel time that behave this way.
**TES** Wide selection of settings that affect the work time calculations, additional work and overtime.
**Levelling Period** Here you may define leveling periods and settings. More information about the set up of levelling periods can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002559537-Setting-up-a-levelling-period>) and details of defining levelling period overtime calculations can be found [here](<https://support.nepton.com/hc/en-gb/articles/4410630282257-Configuring-levelling-period-overtime-calculations>).
**Accruals and overtime hours** With these settings one can set rules what accruals are in use, when they are earned and how. Default accruals are Balance, Bank, Annual absence, Flexible bank, Levelling period hours and Holiday pay leave. You may also set up new, custom made accruals. More information about accrual usage [here](<https://support.nepton.com/hc/en-gb/articles/360005073918-Accruals>).
**Supplements** Under the “Supplements” section, you can define various additional allowances that are not based on worked hours but rather additional remunerations based on role, task or duty. These allowances might include contextual or other compensation paid on top of regular wages, which can vary based on the specific tasks. Supplements can be used in, for example, pieces or hours. Learn more about supplements [here.](<https://support.nepton.com/hc/en-gb/articles/360002559637-Supplements>)
**Work Rises** In this section, you can set time-dependent work increases, such as evening shift allowances, night shift allowances, Sunday allowances, or holiday pay. First, provide a name for the increase, then specify the situations in which it applies. Next, define the validity periods for the work rise. For example, the validity period for a Sunday allowance could be from 00:00 to 24:00 on Sundays, meaning it applies throughout the entire day. Explore work increases further in [this](<https://support.nepton.com/hc/fi/articles/360002560978-Ty%C3%B6korotukset>) article.
**Weekly rest period** Configure the conditions for weekly rest compensation in the “Weekly Rest period” settings. Check out different options and examples related to weekly rest in [this](<https://support.nepton.com/hc/en-gb/articles/360007389978-Weekly-rest-time-compensation>) article.
**Annual leave** Set the rules for earning and using annual leave in the “Annual Leave” settings. Learn more about annual leave [here](<https://support.nepton.com/hc/en-gb/articles/360002560698-Setting-up-annual-leave-earning>).
**Exceptional entries** Use these settings to define situations where a warning triangle appears in the calendar view. Warning triangles help supervisors or HR personnel when reviewing staff hours. Events with warning triangles also appear in the “Exceptional Entries” report. Explore exceptional entry settings [this](<https://support.nepton.com/hc/en-gb/articles/360002560618-Poikkeuksellisten-kirjausten-ilmoitusten-hallinta-EN-title-needed>). For instructions on the “Exceptional events” report, refer to [this ](<https://support.nepton.com/hc/en-gb/articles/360002548837-Exceptional-event-report>)article.
**Public holidays** Here you may specify the rules for public holidays and their impact on work hour calculations. Learn more about configuring holiday settings [here](<https://support.nepton.com/hc/en-gb/articles/360002558797-Public-holiday-management>).
**On call** Under the “On Call” heading, you can define the event types that reduce on call time. Familiarize yourself with recording and configuring on call [here](<https://support.nepton.com/hc/en-gb/articles/8040695057821-On-Call-Recording-and-settings>).
**Start-up and termination work** In this menu, you can specify whether work performed before or after a shift is compensated as either Start-up or Termination work. Refer to the comprehensive instruction [here](<https://support.nepton.com/hc/en-gb/articles/15073908826909-Start-up-and-Termination-work-compensations>).
## Shifts
Under “Shifts,” you can modify the behavior of shifts generated from work shift planning, including exceptions related to workday length, permitted work times and more. More information here.
## Projects
Under the “**Projects** ” heading, you can configure settings related to projects. The available configurations are described in [this](<https://support.nepton.com/hc/en-gb/articles/360002562658-Project-targeting-settings>) article. Note that project targeting is possible only with Nepton Pro and Complete service levels. Learn more about project management as a whole in a dedicated article [here](<https://support.nepton.com/hc/en-gb/sections/360000707398-Project-management>).
## Integrations
In the “**Integrations** ” section, you define settings for data transferred via integrations, such as salary & absence code mappings. Keep in mind that integration settings are done at the Working Community settings. The list below covers standard integrations available in the service.
![](https://support.nepton.com/hc/article_attachments/20221709667357)
