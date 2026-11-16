---
id: 360005073918
title: Accrual settings
url: https://support.nepton.com/hc/en-gb/articles/360005073918-Accrual-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Accruals
section_id: 360000705197
section_path:
- Worktime calculations and management
- Accruals
labels:
- Työaikapankki
- Pankki
- Saldo
- Liukumasaldo
- työajanlyhennys
- työajanlyhennysvapaa
- pekkanen
- pekkaset
- jousto
- saldokertymä
- saldotilanne
- työlyhennysvapaa
- ylityö
- täytä työviikon tunnit
- pankkisaldo
- joustosaldo
- ylityöpankki
- pankkitunnit
- ylityöohje
promoted: false
updated_at: '2026-09-02T11:42:33Z'
edited_at: '2026-09-02T11:42:33Z'
---

# Accrual settings

Accruals can be edited in **Worktime > Administration > Working Community / Setting Group settings** **> Work hours > Accruals. **Click on the accrual which settings you want to edit. The service's standard accruals have the settings that have been assigned to them (work time shortening leave and levelling period hours are accrued according to the earnings table, others do not have this table), all possible settings are available for new custom accruals, meaning they can be configured exactly as desired. 
## Accrual Settings
Every accrual has the following basic settings:
![](https://support.nepton.com/hc/article_attachments/27996309197981)
**Name** The name given to the accrual and possible variations in different languages.
**Accrual unit type** can be either days or hours. Default setting is hours. NOTE: This setting is not visible for accruals that have an earning table, because the unit is defined with settings "Earn based on" and "Earned as".
**Visible in week tables** setting defines whether the accrual and it's value are shown in each users' calendar and table views. The accrual is shown on it's own row at the bottom of the day's activities. The value is shown in green if it's positive and in red if it's negative.
**Calculate future accrual predictions** setting defines, if the system should predict what the accrual value will be in the future. Defaults to 'Yes'. Events that directly affect accrual will be shown in the future, i.e., for example, accrual leave, or work exceeding the work obligation that has been directed to accrual. A mere obligation that fell short of a working day does not show negative hours in the future.
**Code** is the unique code given to the accrual, can be used in integrations to identify the accrual.
### Borrowing rules
The settings in this section can be used to determine in which situations unfilled work obligation is automatically borrowed from the accrual.
![](https://support.nepton.com/hc/article_attachments/27996369184797)
**Accrual automatically borrows from balance if there's not enough work on the day** \- Whether or not time will be automatically borrowed from the accrual if the daily obligation isn't met.
**Do not borrow from balance if obligation has been manually set** \- Whether or not time will be borrowed from the accrual if the daily obligation has been manually set. The obligation can be manually set in the calendar view by setting 'Length of work day' to a different value.
**Borrow at the end of the week if weekly obligation not fulfilled** \- Whether or not time will be borrowed from the accrual at the end of the week, if the weekly obligation isn't met.
### Earning rules
The settings in this section determine in which situations and under what conditions value is earned to accrual.
![](https://support.nepton.com/hc/article_attachments/27996369186205)
**Year start date** setting can be used to define the restart time for the earning table to be any other date than the default. The default reset is January 1st. Please note: When adding a new value to the setting, the year is shown as 2000 for technical reasons. This doesn't need changing, it is enough to set correct day and month.
**Earning table counts reset every** setting can be set to either year or month. If the earning period is year, the accrual earning is based on the earning table during the year. If the earning period is month, the earning happens during every calendar month as per the earning table. The default setting is a year.
**Earn based on** can be set either hours, days or months, the default being hours. 
If earn based on is set to months, the number of working days or the number of working hours from the calculation of annual leave will be used to see if accrual is earned for the month worked. Read more about the implementation of annual leave earning [here](<https://support.nepton.com/hc/en-gb/articles/360002560698>).
If the earning basis is in hours, the earning threshold can be set to the minute.
Note! You cannot use months as the earning basis if the earning period is a month. If this is set, no accrual will be earned at all.
**Earned as** can be set to be earned as days or hours.
**Calculation method for part-time employees** setting lets you specify that earnings will be based on the person's worktime percentage. For example, if employees would earn 8 hours of accrued leave after 17 working days, with a 50% worktime percentage, the employee would earn 4 hours of accrued leave after 17 working days.
**Override earn percentage** In this section, you can specify that earnings will be based on a specific percentage, for example, if the earnings percentage needs to be different from the employee's worktime percentage.
**Do not earn leave unless this many months into contract** setting defines a minimum length of the working contract until leave is earned. This setting requires work contract start date to be filled in person's details.
**Earn from the beginning of employment** lets can specify that the accrual is earned from the beginning of the employment. If the value is "No" or the value is not set, the accrual will only start after the employment has lasted for the number of months specified in the setting Do not earn leave unless this many months into contract.
**Earned only from regular time** setting allows the accrual to be earned only from regular time, so not from over time or any other work time exceeding regular hours.
**Earn from time borrowed from accrual** defines, whether accrual can be earned also from time that has been borrowed from another accrual, balance for example.
**Earning table** If accrued leave is earned after a certain amount of work has been done, the required working hours and the leave earned from them are filled in the earnings table. The table can be filled in either in working hours or working days.
![](https://support.nepton.com/hc/article_attachments/38837919234205)
### Spending rules
The settings in this section can be used to determine in which situations value is deducted from the accrual and by how much.
![](https://support.nepton.com/hc/article_attachments/27996369188637)
**Days of week that leave/holiday can spend balance** \- Which days of the week can compensate the user if they have recorded leave/holiday for those days. The other settings below can also influence whether the leave is paid. The default is Monday to Sunday.
**Only days with obligation counted as leave/holiday days** \- Whether the day must have a work day length/obligation or not to be considered as a compensated leave/holiday day.
**Leave/holiday ignored if work on day** \- If set to yes, then any work events on the day will prevent the accrual leave/holiday from paying the employee or deducting from their accrual balance. Defaults to no.
**Leave/holiday ignored if public holiday** \- If set to yes, then any work events on the day will prevent the accrual leave/holiday from compensating the employee or deducting from their accrual balance. Defaults to no.
**Leave/holiday paid as** \- How the employee should be compensated/paid for their leave. In reality this affects how the time is displayed in the calendar and exported out of the system to payroll systems. For example "Regular time" will display in the calendar and export as regular pay, but "Annual leave" will not display in the calendar and be exported as annual leave according to the integation rules. Note: Accruals that compensate as "Annual leave" will not currently show in Annual leave/holiday reports as customers should still be using the current Annual holiday system to track annual holiday days.
**Amount leave/holiday should pay (per day) and Amount to deduct from accrual balance (per day) when on leave/holiday** \- How much compensation is paid to the employee for a valid leave/holiday, and how much is deducted from the accrual to cover that pay respectively. Both settings share the same options listed below but are separated as it is sometimes desirable to compensate the user a different amount to what is deducted from their balance e.g. if the compensation is paid in hours and the balance is measured in days.
  * **Amount of obligation used** \- Compensation is paid to the employee that matches how much has been recorded up to their work day length/obligation e.g. On a workday, if you record 1 hour of leave, there will be 1 hour of pay, if you take 10 hours of leave, there will be 7.5 hours of pay (or whatever the work day length is set to). On a non-workday, there will be no pay, regardless of other settings.
  * **Percentage (0-1) of obligation used** \- Only available for the deduction setting. The amount deducted from the accrual is based on the percentage of the obligation you used during the day as a value between 0 and 1. For now it can only deduct 0, 0.5 or 1, and is useful if you have an accrual recorded in days and want to allow employees to record either half or full days. The threshold between whether it deducts a half day or a full day is if 60% of the day length has been used.
  * **Fixed amount per day** \- You can define how much the accrual leave should compensate the user and/or deduct from their accrual balance as a fixed amount on obligated and non-obligated days (see below).
  * **Work day length** \- Compensates the user and/or deducts from the accrual balance the amount that is defined as their work day length for the day.
  * **Fifth of work day length** \- Compensates the user and/or deducts from the accrual balance a fifth of their weekly obligation. This is useful for deducting on days where they are not expected to work but is otherwise defined as a day of the week that should pay accrual leave.
  * **Max work day length** \- Compensates the user and/or deducts from the accrual balance the amount that is defined as their work day length for the day.


**Amount on leave days with/without a work day length** \- These should be set when using "Fixed amount per day" to specify how much is compensated and/or deducted from the accrual on days where the user is expected to work and not expected to work respectively.
### Limits and adjustments
These settings allow you to define the minimum and maximum balance at the beginning or the end of the day and what should happen if you exceed it. It is recommended to use the default behavior that the limit _can_ be exceeded and only a warning is generated for the person and their supervisor.
![](https://support.nepton.com/hc/article_attachments/27997463203741)
**Maximum negative/positive balance at the end/beginning of the day** settings define, what is the maximum/minimum value the accrual can reach at the end or beginning of the day.
**Behaviour of negative / maximum positive limit** defines what happens when that limit is reached. More on how to manage maximum and minimum limits [here](<https://support.nepton.com/hc/en-gb/articles/360010514358>).
**Maximum balance that can be earned per day** sets a limit for daily accrual increase.
## Example - Balance
The most important settings for the balance accrual are the maximum daily accrual of the balance and the minimum and maximum amounts. It is generally not advisable to set a minimum amount because then it is not easily seen if the negative balance starts to accumulate larger than the set value.
![](https://support.nepton.com/hc/article_attachments/27997474045469)
With the setting **Borrowed from default accrual contributes towards weekly obligation** , it is possible to determine that any balance deductions are to be made only on the last day of the workweek. If this setting is in use and it is desired to avoid reducing the balance when using certain event types, it can be defined in the section **Work hours > TES > ****Event types that contribute to work week** Event Types that are counted in the workweek.
  * **Yes** : The event type affects the formation of weekly overtime, and hours are not filled from the balance on the last day of the workweek.
  * **No** : The event type does not affect the formation of weekly overtime, and hours are filled from the balance on the last day of the workweek.
  * **Yes, but not to the formation of overtime:** The event type does not affect the formation of weekly overtime, but hours are not filled from the balance on the last day of the workweek.


![](https://support.nepton.com/hc/article_attachments/20289288487965)
## Example - Use of holiday pay leave on Saturdays
If you want the holiday pay leave to be consumed as annual leave from Monday to Saturday, and you want the holiday pay leave days recorded for Saturdays to be included in the salary data along with other holiday pay leaves, there are four different options available in the service for this purpose.
**Option 1** \- Saturday does not rise to the salary data if the day’s work obligation (the length of the workday) is 0 hours. An exception can be set for Saturday in the [Length of Workday](<https://support.nepton.com/hc/en-gb/articles/360002558417>) setting and an exception for the entire workweek in the [Length of Workweek ](<https://support.nepton.com/hc/en-gb/articles/360002558537>)setting, so that if the event ‘Holiday Pay Leave’ is recorded for the day, the length of the workday and the length of the workweek are automatically set to value X. This results in regular working hours being formed in the calendar for the holiday pay leave days, and the amount of work done during the week increases. Holiday pay leave creates interpreted working time for the salary data, but without increasing the length of the workweek, this does not happen if the length of the workweek has already been completed earlier in the week. For this reason, an exception is needed for both the length of Saturday’s workday and the entire workweek.
**Option 2** \- Set in the holiday pay leave accrual settings, to the**Amount to deduct from accrual balance (per day) when on leave/holiday** section, a fixed hour amount for **Amount on leave days with a work day length** and******Amount on leave days with zero work day length**. The setting determines how much the employee is compensated on a free/holiday day and how much the compensation is for days that have a set length of the workday and for days without the length of the workday. 
![](https://support.nepton.com/hc/article_attachments/20289288496541)
**Option 3** \- Forming a salary rule for holiday pay leave based on the marked working time (MarkedTime). The salary rule can be found [here](<https://support.nepton.com/hc/en-gb/articles/360008045337>), under the section ‘Holiday pay leave selected from Saturdays with no work obligation’. The rule takes into account that Sunday is not included in the data, even if holiday pay leave has been recorded for Sunday.
**Option 4** \- If you want the holiday pay leave to behave like annual leave, then the fourth option is to create a new, customized holiday pay leave event type in the service, which behaves like annual leave and the corresponding accrual for this event type. See below for instructions on creating a new accrual. Instructions for creating a new event type can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002519157>).
