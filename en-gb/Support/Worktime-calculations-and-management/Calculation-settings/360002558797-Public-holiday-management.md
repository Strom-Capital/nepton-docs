---
id: 360002558797
title: Public holiday management
url: https://support.nepton.com/hc/en-gb/articles/360002558797-Public-holiday-management
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- NEPTONNEEDSREVIEW
- pyhäkalenteri
- arkipyhä
- juhlapyhä
- Arkipyhänä tehdyn työn ja arkipyhäviikkojen käsittely
- Arkipyhäviikko
- juhlapyhäasetukset
- lyhennetty työpäivä
- Aattolisä
- arkivapaa
- juhannus
- arkipyhävapaa
- pääsiäissunnuntai
- aattotyö
- pyhäpäiväkoodi
- pyhäpäiväkoodit
- juhlapyhäkorvaus
promoted: false
updated_at: '2026-05-21T09:29:48Z'
edited_at: '2025-08-29T07:33:50Z'
---

# Public holiday management

The service allows you to configure settings for each holiday. In the settings, you can determine whether the holiday is displayed in the calendar and whether it has calculated effects on working hours or compensation.
## Defining settings
Settings can be configured in **Worktime > Working community/Setting group settings > Work hours > Public holidays**. 
![](https://support.nepton.com/hc/article_attachments/26815153260957)
### General settings
The first settings define how public holidays affect working hours.
![](https://support.nepton.com/hc/article_attachments/26815128299677)
The "Treat working on public holidays that shorten the week as" setting determines what happens if work events are recorded on a public holiday.
**Normal day** = All work recorded to the public holiday is handled as it would be normal working day. Calculations are done according to work day length and balance is deducted when working less than the work day length. In shiftwork shifts can occur on public holidays and should be treated as normal working days.  
**Additional work** = All work recorded on public holiday is handled as additional work, however depending on defined [additional work settings](<https://support.nepton.com/hc/en-gb/articles/360002559438>).   
**Daily- / weekly overtime** = All work recorded on public holiday is first weekly overtime, and then daily overtime, once TES maximum work day length has been crossed.  
**Daily overtime** = All work recorded to the public holiday is directly daily overtime. 
It is important to notice which overtime target is used when calculating work on public holiday. Such as if work which is targeted as "Hour to hour - Balance", overtime is not automatically interpreted by increment percentage.
If work recorded on public holiday is wanted to be compensated hour by hour, 'Treat working on public holidays that shorten the week as' should be set as "Daily / weekly overtime" or "Daily overtime", depending on how work on public holiday should be compensated if work is targeted as overtime to salary. 
With setting "**Public holidays shorten work week by** " you can define, whether public holiday should shorten work week length by daily obligation, weekly obligation or maximum weekly obligation. The setting is described in more detail [here](<https://support.nepton.com/hc/en-gb/articles/360005058217>).
![](https://support.nepton.com/hc/article_attachments/26815128301085)
Please note! Public holiday shortens work week max 8 hours per one day.   
  

The setting "**Show public holiday compensation** " defines whether a possible compensation is shown on it's own row in calendar view or not. The compensation is determined by the settings in "Public holidays: Show/Earn compensation/Shorten workweek". The compensation is based on length of work day.
![](https://support.nepton.com/hc/article_attachments/26815153265053)
### Fixed compensation
The settings in this section allow you to define a fixed compensation for public holiday compensation. The first setting determines whether the fixed compensation is in use, and the second determines the amount of the compensation. Exception settings can also be used in both settings, for example if fixed compensation is not in use at all on a certain day, or there is a different amount of compensation on a certain public holiday. The compensation is linked to the "compensation is earned" setting in the public holiday table. For example, if you want to earn 8 hours of public holiday compensation for every public holiday on weekdays, regardless of work obligation, the settings would be set as follows:
![](https://support.nepton.com/hc/article_attachments/29941749970461)
And in addition, for each holiday that constitutes compensation, "Earn compensation: Only on weekdays".
![](https://support.nepton.com/hc/article_attachments/29941739136029)
In this case, an 8-hour compensation will appear on every public holiday that falls on a weekday:
![](https://support.nepton.com/hc/article_attachments/29941739136925)
The image above shows that a 12-hour fixed compensation is created for public holidays that fall on a weekday, but no compensation is created for Boxing Day, which falls on a Saturday.
### Public holidays that shorten work week, shorten...
You can also define how work week shortening on public holidays behave and which determination of the length of the working week they shorten.
![](https://support.nepton.com/hc/article_attachments/26815153265309)
**Shortening of work week and border of overtime**
If work week is wanted to be shortened, but not the border of the overtime, then values should set as:
  * TES work week length = Yes
  * TES maximum hours of work per week = No


If also the border of overtime is wanted to be shortened, then values should be set as:
  * TES work week length = Yes
  * TES maximum hours of work per week = Yes


All these three settings can have [exceptions,](<https://support.nepton.com/hc/en-gb/articles/360002560677>) which are valid only on certain days.
The third setting, "Weekly overtime threshold if earned before TES max week length" does not matter, if it is not set in the TES settings (Work hours > TES). 
### Public Holidays
The section lists the days in the service that can be defined as public holidays. There are three separate settings for each holiday; "Show", "Earn compensation" and "Shorten work week".
![](https://support.nepton.com/hc/article_attachments/26815128306589)
The setting "Show" defines, how the day is shown in the worktime calendar.
![](https://support.nepton.com/hc/article_attachments/26815128307357)
If set to **No** , the day in question will be displayed in the calendar like any other day (white background).  
If set to **As important day** , the day in question will be displayed in the calendar with a red title highlighted (white background).  
If set to **As public holiday** , the day in question will be displayed in the calendar with a red title and a red background.
The picture below displays first a day set as "no" (normal day), then a day set as important day, then a day set as public holiday:
![](https://support.nepton.com/hc/article_attachments/26815153271325)
**Earn compensation** setting defines, whether a compensation is paid for said day. The options are:  
No  
Only on weekdays  
Only on days with work obligation  
Only when public holiday shortens work week  
Always
![](https://support.nepton.com/hc/article_attachments/26815128311837)
In order for the compensation based on the selected settings to be displayed in the calendar, the "show public holiday compensation" setting must also be set to "yes". The compensation is based on length of work day.
**Shortens work week** setting defines if the work week shortens during the week in which the public holidays falls. The options are:
No  
Only on weekdays  
Only on days with work obligation  
Always  
![](https://support.nepton.com/hc/article_attachments/26815153274397)
Other settings related to shortening the work week can be found above the table.
## Shortening work week length in the beginning of the week 
Public holidays and annual leave can shorten work week already in the beginning of the week. Then for example if public holiday or annual leave is on Friday, the work week is shortened on Monday. 
The setting can be found in **Worktime > Administration > Working community level/ Setting group settings > Work hours >****TES.** ******  
**
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4418085218193)
## Public holiday settings for planning
If the planning is in use, the settings for the public holidays can be defined in the **Employees** section. Planning settings can be found from **Employees > Administration > Settings > Planning**. A shortened length can be specified for the public holiday and whether a daily work obligation is added in addition to the planned work. You can find more detailed description of the shift planning public holiday settings and calculation in the planning view [here](<https://support.nepton.com/hc/en-gb/articles/360017908457-Planning-view-calculations>).
[code] 
    ![Screenshot 2024-05-24 133249.png](https://support.nepton.com/hc/article_attachments/19084930368285)
[/code]
