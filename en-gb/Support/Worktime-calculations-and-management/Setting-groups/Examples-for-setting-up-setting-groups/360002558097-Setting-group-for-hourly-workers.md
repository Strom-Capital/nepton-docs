---
id: 360002558097
title: Setting group for hourly workers
url: https://support.nepton.com/hc/en-gb/articles/360002558097-Setting-group-for-hourly-workers
locale: en-gb
category: Support
category_id: 360000446658
section: Examples for setting up setting groups
section_id: 360001483898
section_path:
- Worktime calculations and management
- Setting groups
- Examples for setting up setting groups
labels:
- tuntityöntekijä
- nollatunti
- tuntipalkka
- nolla
- työaikamuutokset
- töihin kutsuttava
- tuntityö
- tuntityöläinen
promoted: false
updated_at: '2024-09-11T09:47:39Z'
edited_at: '2024-08-12T10:05:51Z'
---

# Setting group for hourly workers

Just like for any worktime form, it is recommended to create a dedicated [setting group](<https://support.nepton.com/hc/en-gb/articles/360002557497>) for hourly workers.
This article guides you through the most important settings when creating a setting group for hourly workers. The example situation is having an employee who is being paid by each hour worked. So all work is targeted hour by hour to salary.
It is also possible to enable overtime and balance calculations for hourly workers.
## Defining work day length
Even though only actual working time is being monitored, the length of work day (average daily obligation) must be set for each day (Mon-Fri) . The setting can be found in **Worktime > Administration > Setting groups > Select the correct setting group > Setting group settings > Work hours > Length of workday.**
In this example the length of workday is 8 hours.
![](https://support.nepton.com/hc/article_attachments/20824145844765)
## Defining the length of work week
Like the length of the work day, also the length of the work week needs to be set. This can be done in setting group settings > Work hours > TES > TES work week length. In this example the work week length is 40 hours (5 days * 8 hours).
![](https://support.nepton.com/hc/article_attachments/20826955705117)
## Settings for worktime calculation
Because only worked hours are monitored, and there is no balance or overtime calculation, some settings need to be set in **Setting group settings > Work hours > Accruals and overtime hours** as shown in picture below. Balance and any other irrelevant accruals should be turned off.
![](https://support.nepton.com/hc/article_attachments/20826939183645)
Under the 'Calculation settings: Overtime' all the hours are targeted by default hour to hour to salary as shown in the picture:
![](https://support.nepton.com/hc/article_attachments/20826939185821)
All other overtime options will be deactivated under the listing in "Visible overtime options on event creation", so that all events will always be directed hour to hour to salary. 
If balance or some other accruals are needed, they can be taken into use in 'Accrual is in use' listing. In the setting below balance is enabled.
![](https://support.nepton.com/hc/article_attachments/20826939190173)
After the person's regular work hours (length of work day) are filled, the rest will automatically be targeted to balance. Note: If balance is activated in hourly worker's setting group, this also means borrowing hours from balance if regular hours are not filled.
