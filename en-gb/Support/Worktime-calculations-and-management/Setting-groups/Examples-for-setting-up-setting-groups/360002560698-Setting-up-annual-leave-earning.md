---
id: 360002560698
title: Setting up annual leave earning
url: https://support.nepton.com/hc/en-gb/articles/360002560698-Setting-up-annual-leave-earning
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
- lomakalenteri
- lomat
- lomalaskenta
- vuosilomalaskenta
- loma
- lomamäärä
promoted: false
updated_at: '2026-02-16T11:10:16Z'
edited_at: '2026-01-21T07:35:56Z'
---

# Setting up annual leave earning

Below are the steps required to take annual leave calculations in use.
## Define rules for annual leave earning
Annual leave earning settings can be defined either in Working community or Setting group level:
**Worktime > Working community / Setting group settings > Work hours > Annual leave**
## Start date of annual leave earning
The earning of annual leave starts from the day when the first work-type event has been logged in the calendar, and the person earns annual leave according to the regulations.
Please note that assumed event on an empty working day does not start the calculation of annual leave earnings.
## Annual leave settings
Below is a list and explanation of all settings regarding annual leave. 
![](https://support.nepton.com/hc/article_attachments/19205556763165)
### Accrual in use
This setting defines whether Annual leave calculations are in use at all.
  * "Not set" - For existing customer the default value is "not set", which behaves the same way as "yes".
  * "Yes" - Annual leave calculations are in use.
  * "No" - Annual leave calculations are not in use. Earning annual leave is not calculated and the accrual values are not shown when adding a new event or when approving event requests. 


This setting benefits for example situations where annual leave earning is being calculated in an external system. 
### Hide instructions for adding Annual leave when adding new event
The setting defines whether instructions for marking annual leave events over Saturdays are shown or not. 
### Calculations for annual leave earning
The settings control how many annual vacation days are earned based on either the hours worked or the number of working days.
Hourly workers who regularly work less than 14 days a month (called to work if necessary) should have setting "If less than xx hours in a month, 0 days of annual leave are earned, otherwise 2.5 days of leave are earned"
Annual leave earnings for employees with monthly salaries are determined based on the number of working days. A rule is set for a monthly employee in the form of 'if less than 14 working days in a month, 0 days of annual leave are earned, otherwise 2.5 days of leave are earned.
In both situations, exception rule can be used to define the situations when a person earns annual leave 2 days a month. The setting '...Earned annual leave at another time' is set to be earned as shown in the picture below. In this case, the person earns 2.5 days of annual leave, unless an exception rule applies, in which case 2 days are earned. The exception rule is valid if the employment has lasted less than 12 months from the start of the holiday year.
![](https://support.nepton.com/hc/article_attachments/19205602423581)
More information about [setting exceptional settings](<https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings>).
## Rules of use
### Days of week that leave/holiday can spend balance
The setting controls which days are used up as annual leave. The options are 'Monday to Friday', 'Monday to Saturday' or 'Monday to Sunday'. If the value is not set and the value is not inherited from above, the value 'Monday to Saturday' is used.
Please note, that for example, Easter Saturdays are not counted as annual leave days according to Section 4 of the Annual Leave Act.
### Only days with obligation counted as leave/holiday days
If this settings is set to 'yes'. only days with work day length longer than 0 are counted as annual holiday.
### Leave/holiday ignored if work on day / public holiday
If the settings are set to 'yes', the marked annual leave will not be counted as an annual leave day if work has been recorded for the day / the day in question is a public holiday.
### Amount leave/holiday should pay (per day)
How to calculate the amount of annual leave to be used when a person is on annual leave.
  *     * "Not set" - The value is inherited from the parent if set. If the value is not set at a higher level, no annual leave is used. 
    * "Amount of obligation used" - Annual leave is used based on person's daily obligation
    * "Fixed amount per day" - A fixed amount of annual leave is used per day in accordance with the following two settings (Amount on leave days with a work day length / zero work day length). The amount of annual leave to be used is automatically calculated according to the "Amount on leave days with a work day length" setting, if it is set. If it is not set, the amount is calculated from the length of the work day specified in the person's setting group. If the length of the work day is not specified, the amount is calculated from one fifth of the length of the work week specified in the person's setting group.
    * "Workday length" - Annual leave is used based on the length of the person's working day for each day.
    * "One fifth of work week length" - One-fifth of the length of the person's working week / amount of work obligation per day of Annual leave is used. 
    * "Max work day length" - Annual leave is used based on person's maximum work day length
    * "Legacy annual leave rules" - Annual leave is used by one fifth of the length of the work week.  
  
If, on the other hand, the length of the work day and work week has not been set and therefore the amount of annual leave to be used cannot be calculated, the default value is 8 hours. This kind of situation can occur in a situation where the person's Worktime setting group and the calculation of working time have been implemented intentionally without standardized work obligations.
The settings listed above define the way in which annual leave is used. They also define how annual holidays shorten the length of the work week. Annual holidays do not however, shorten the length of the work week on days with workday length 0. If you want the annual holiday to shorten the work week on such days, an [exception](<https://support.nepton.com/hc/en-gb/articles/360002560677-Configure-exceptions-to-settings>) to the length of the work day must be made for that day. 


### Amount on leave days with a work day length
Applies to the situation when the setting "Amount leave/holiday should pay" is set to "Fixed amount/day". A fixed amount of annual leave that is used on annual leave days that would have the length of a working day / work obligation.
_Note: This setting is ignored if the value "Based on the length of the working day" is selected._
### Amount on leave days with zero work day length
Applies to the situation when the setting "Amount leave/holiday should pay" is set to "Fixed amount/day" or "Workday length". A fixed amount of annual leave that is used up from annual leave days that do not have a work obligation / the length of the work day is 0.
If amount of leave/holiday should pay (per day) is set based on legacy annual leave rules, and amount on leave days with zero work day has not been set, the amount is determined based on the work day length of previous days. If determining the amount from previous days is not possible, default of 8 hours is used.
### Amount leave/holiday should contribute to weekly thresholds (per day)
The setting can be used to determine how annual leave fills the working week. By default, one annual leave day can only fill the working week for 8 hours (If the settings in the TES section have specified that annual leave is included in the working week, this means a maximum of 8 hours). However, this setting can be used to define different effective amounts.
It can be said that annual leave fills the working week by a **fixed amount** , in which case "fixed amount" is selected for the setting. In this case, the following setting, "Amount on leave days with a work day length" should also be defined with the desired fixed amount. For example, if you work 12-hour shifts, and you want annual leave to affect weekly working hours by this duration, the setting would be defined as follows:
![](https://support.nepton.com/hc/article_attachments/33377307510685)
Without this setting, if the weekly working time is 36 hours and the shift length is 12 hours, and 3 x 12-hour shifts are planned for the week and these obligations are fulfilled with annual leave, the weekly work would be incomplete, as one annual leave day would only fulfill one fifth of the working week:
![](https://support.nepton.com/hc/article_attachments/33377307512477)
If "Borrow at the end of the week if weekly obligation not fulfilled" is set to yes in the settings group, 14h24min is deducted on Sunday, because the annual leave is calculated into the work week as specified in the "Amount leave/holiday should pay (per day)" setting, with a maximum of 8h. In this case, the annual leave fills the work week with 7h12min daily according to the "Amount leave/holiday should pay (per day)" setting.
If the annual leave is set to cover 12h of the work week, this borrowing doesn't happen, because the recorded annual leave covers 3 x 12 = 36h:
![](https://support.nepton.com/hc/article_attachments/33377283435165)
Voidaan myös sanoa, että vuosiloma lasketaan työviikkoon perustuen "**Vapaa/lomapäivän palkallinen kesto** " määriteltyyn arvoon. Tällöin asetuksen "Korvaus vapaa/lomapäivänä" valittu määritys vaikuttaa siihen, miten vuosiloma lasketaan työviikkoon mukaan. Esimerkiksi, jos asetukseen "Korvaus vapaa/lomapäivänä" on asetettu yksi viidesosa työviikosta, laskettaisiin myös vuosilomasta yhdeltä päivältä viikkotyön viidesosa viikkotyöaikaan.
It can also be said that annual leave is calculated into the workweek based on the value defined in "**Paid duration of leave/holiday** ". In this case, the setting selected in the "Amount leave/holiday should pay (per day)" setting affects how annual leave is calculated into the workweek. For example, if the "Amount leave/holiday should pay (per day)" setting is set to one fifth of the workweek, one fifth of the weekly work from one day of annual leave would also be calculated into the weekly working time.
![](https://support.nepton.com/hc/article_attachments/33377307514013)
The effect of annual leave on weekly work is important, for example, in situations where, at the end of work, a week's obligation that has not been fulfilled during the week is automatically deducted, or in a situation where the beginning of the week has been annual leave and overtime is worked during the end of the week.
### Event types that earn year leave
Event types that are counted as earning annual leave. Customized event types have a star sign in front.
![](https://support.nepton.com/hc/article_attachments/19205556776605)
## Ensure the retroactive validity of the annual leave rules
If changes to the annual leave settings have been made retroactively, the calculations must be [refreshed](<https://support.nepton.com/hc/en-gb/articles/4411220910865-Retrospective-change-of-settings-and-recalculation-of-accrual-value>) in the calendar view. After refreshing the calculation, the correct annual leave earnings and uses are shown in the annual leave reports.
