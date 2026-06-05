---
id: 360002559438
title: Additional work, formation
url: https://support.nepton.com/hc/en-gb/articles/360002559438-Additional-work-formation
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- enimmäistyöaika vuorokaudessa
- jaksolisätyö
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2026-02-25T13:04:34Z'
---

# Additional work, formation

Additional work is formed when working hours exceed regular time but do not exceed maximum work day length. Regular time can be based on local agreements, collective agreements or Working Time Act.
If work week length is exceeded, additional work is earned up to maximum hours of work per week limit. For example, a person working 37,5h per week could earn additional work after regular time up to 40h. Additional work would be 2,5h in a week.
If maximum hours of work per week is not exceeded, additional work is earned up to maximum work day length. For example, a person working 7,5h per day could earn 30 mins of additional work per day.
When daily or weekly maximum hours are exceeded, overtime is formed, except when working on hour to hour basis targeting work time balance. 
## Earning additional work and additional work rise
Addition work can be earned with or without rise percentage. Additional work rise percentage and thresholds after which rise is earned can be found in working community and setting group settings Work hours > TES.
Setting **Only earn after total daily hours** determines after how many daily hours earning of additional work rise starts. By default the value is work day length before the work time percentage is applied. 
Setting **Only earn after total weekly hours** determines after how many weekly hours earning of additional work rise starts. By default the value is work week length before the work time percentage is applied.  
  
Setting **Apply worktime percentage when a public holiday shortens the work week** , you can define whether the additional work rise percentage weekly threshold for a part‑time employee during a public‑holiday week is calculated in the same way as for a full‑time employee, or according to the employee’s work time percentage. By default, this setting is **“Yes”** , meaning that during a public‑holiday week, the additional work rise percentage weekly threshold is calculated according to the work time percentage.
![](https://support.nepton.com/hc/article_attachments/34220981966237)
If person is a part-time worker with 6h work day length, maximum work day length of 8h and settings above are used, then earnings during 9h working day would be as follows (time after work day is marked as overtime):
  * 6h regular time
  * 1,5h 0% additional work
  * 0,5h 50% additional work
  * 1h 50% daily overtime


### Additional work rise and work time percentage
With following settings:
  * Length of work day 7,5h
  * Work time percentage 80%, which results to work day length of 6h


Work day length of 7,5h is used as a daily threshold after which additional work rise is earned.
## Considering weekly regular time before forming additional work
According to some collective agreements such as Kunnallinen yleinen virka- ja työehtosopimus (KVTES) and Avaintyönantajat AVAINTA ry työehtosopimus (Avaintes) additional work is earned weekly between time of work week length and maximum hours of work per week. This setting can be set on working community and setting group level.
Below is an example how to implement additional work settings to setting group which follows Avaintes collective agreement.
\- Work day length 7h 21min  
\- Maximum work day length 8h  
\- Work week length 36h 45min  
\- Maximum hours of work per week 38h 45min  
  
1\. From settings group settings choose TES  
  
![mceclip1.png](https://support.nepton.com/hc/article_attachments/6433965032349)  
  
2\. **Work week calculation mode** sets how work week and possible additional work and overtime is calculated:  
  
![mceclip2.png](https://support.nepton.com/hc/article_attachments/6433993863325)  
  
3\. Work week calculation mode: **Calculate regular time for whole week before calculating additional work and overtime**. Weekly hours are taken in consideration when calculating daily additional work. 
Example below illustrates how daily additional work cannot exceed 39 mins and weekly additional work cannot exceed 2 h. With this setting total amount of daily additional work cannot exceed maximum weekly additional work limit.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/6434402571805)
If calculation would be done on a daily basis, additional work would be 39 mins every weekday.
With the setting "Workweek calculation mode: **Calculate work hours on public holidays that shorten work week after work days** ", the working hours of the work week can be set to be calculated in such a way that:  
First, the hours of normal working days are calculated (days with a work obligation)  
Next, the hours of public holidays that shorten the workweek are calculated  
Last, the hours of working days that do not have a work obligation are calculated
The setting can be used, for example, in cases where overtime should be earned on public holidays only if the obligation of a shortened workweek has been fulfilled on other working days (including when the public holiday is on a Monday).
## Considering weekly accruals on weekend before forming additional work
Worktime setting Work hours > TES > Work week calculation mode > **KVTES** takes in consideration weekly accruals and regular time on weekend before forming additional work, according to TES Kunnallinen yleinen virka- ja työehtosopimus (KVTES). More detailed examples are shown below.
![](https://support.nepton.com/hc/article_attachments/13825878926493)
For clarity, Saturday and Sunday represent weekend in this chapter. Setting "KVTES" works on weekday accruals on the second last and the last working day of the week. These days may be different depending on [work week starting time](<https://support.nepton.com/hc/en-gb/articles/360007557338-Defining-Work-week-starting-time>). 
Other relevant settings used in examples:
\- Length of work day: 7h 15min
\- TES maximum work day length: 8h
\- TES work week length: 36h 15min
\- TES maximum hours of work per week: 38h 15min
\- TES daily 50% overtime compensated hours: 2h
\- Earn 100% overtime after weekly overtime: After TES maximum weekly 50% overtime
\- TES maximum weekly 50% overtime hours: 5h
\- Borrowed from balance contributes towards weekly obligation: No
When work week calculation mode "KVTES" is in use, accumulated accruals during the week are taken in consideration on weekend. If accrual value is negative, same amount of regular time is earned on weekend before earning additional work and overtime. 
In the example below balance accrual from Monday to Friday is 2h 45min negative. Saturday work is marked as overtime to salary. Regular time of 2h 45min is earned on Saturday before earning additional work and overtime. This corresponds to the value of negative balance from Monday to Friday.
![](https://support.nepton.com/hc/article_attachments/13825945269917)
Positive amount of accrual contributes only until work week length (e.g. 36h 15min) and does not reduce amount of additional work. In the example below balance accrual from Monday to Friday is 45min positive. Saturday work is marked as overtime to salary. Extra 45 min of work during the weekdays does not reduce amount of additional work (time between 36h 15min and 38h 15min, 2 hours).
![](https://support.nepton.com/hc/article_attachments/13825934335901)
Because setting "KVTES" interprets weekday negative balance as regular time on weekend, it is recommended to [define length of work day](<https://support.nepton.com/hc/en-gb/articles/360002558417-Defining-the-length-of-work-day>) on weekend as a setting exception if there is work events. In this way daily overtime is earned in a consistent manner. Otherwise only regular time is earned on a long weekend working day if there is a large amount of negative accrual during the week. 
In the example below balance accrual from Monday to Friday is 14h 30min negative. Saturday work is marked as overtime to salary but there is no length of work day on Saturday. 14h 30min is earned as regular time due to absence of work day length.
![](https://support.nepton.com/hc/article_attachments/13826063767325)
When length of work day is set to 7h 15min on Saturday, regular time is earned only until work day length after which daily overtime is earned.
![](https://support.nepton.com/hc/article_attachments/13826130448285)
Exception to above-mentioned behavior when weekday accruals are taken in consideration on weekend, is the usage of event type weekly leave. If weekly leave is used, weekday accrual check is postponed accordingly. 
In the example below weekly leave is marked on Monday and Saturday has overtime. Saturday is interpreted as regular working day because one working day was skipped with the usage of weekly leave event. Regular time until work day length is earned on Saturday and daily overtime after that.
![](https://support.nepton.com/hc/article_attachments/13826188532125)
If there wouldn't be any event on Monday, regular time on Saturday would be the amount of negative accrual between Monday and Friday. This is the default behavior of "KVTES" setting. 
![](https://support.nepton.com/hc/article_attachments/13826192593821)
In the example below weekly leave is marked on Monday and Tuesday, Saturday and Sunday have overtime. Saturday and Sunday are interpreted as regular working days because two working days were skipped with the usage of weekly leave event. Regular time until work day length is earned on Saturday and Sunday, and daily overtime after that.
![](https://support.nepton.com/hc/article_attachments/13826231035037)
If there wouldn't be any event on Monday and Tuesday, overtime would be earned on Saturday and Sunday because weekly working hours are reached already in this case. 
![](https://support.nepton.com/hc/article_attachments/13826234037405)
## Addition work and public holiday on weekday
By default public holiday on weekday does not affect additional work formation.
Additional work can be formed in a different way if public holiday shortens work week length and maximum hours of work per week. More information about weekly working hours [here](<https://support.nepton.com/hc/en-gb/articles/360005058217>).
On public holiday regular time can be 0 minutes and additional work is paid up to maximum work day length. In this case additional work can be, for example, 8 hours when working on public holiday.
Setting group and working community levels have setting Work hours > Public holidays > **Treat working on public holidays that shorten the week as**. This setting controls work time calculations on public holiday. The options are:
**Normal day** : Regular time and additional work is formed like on any other work day.
**Additional** **work** : Additional work is formed whole day up to maximum work day length. Time after that is overtime.
**Daily / weekly overtime** : Overtime. Weekly overtime after maximum hours of work per week. No regular time or additional work is formed.
**Daily overtime** : Only daily overtime. No regular time, additional work or weekly overtime is formed.
## Additional work on planned holiday
Work on planned holiday can be either weekly overtime or additional work up to daily or weekly limit. This is controlled with setting Work hours > TES >**Earn weekly overtime on work days without a planned shift / obligation**. If the value is 'Yes' work on planned holiday is always weekly overtime and no additional work is formed. 
## Daily additional work contribution to weekly obligation
Setting Work hours > TES > **Daily additional earned over the additional rise threshold contributes to weekly additional rise threshold** controls whether daily additional rise contributes to weekly obligation or not. More information about this setting in article [Overtime calculation basic settings.](<https://support.nepton.com/hc/en-gb/articles/4417295059985>)
