---
id: 360002559737
title: Travel time compensated as balance or salary
url: https://support.nepton.com/hc/en-gb/articles/360002559737-Travel-time-compensated-as-balance-or-salary
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
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-08-21T11:05:22Z'
edited_at: '2026-08-21T11:05:22Z'
---

# Travel time compensated as balance or salary

There is an event type called Travel time in Nepton. Travel time event type does not accumulate balance or overtime as default, even if user has these accruals set to use.   
  
Exceptions for this compensation can be set in Worktime in Working community or Setting group level settings. They can be found in Worktime > Administration > Working community / setting group settings > Work hours > Length of work day > Regular time over work day length earning threshold. 
## Example of Travel time compensated as balance
Travel time exceeding regular workhours is to be credited to the employee's time balance, subject to a maximum of 10.5 hours per day. As the employee's regular working time is 7.5 hours per day, a maximum of 3 hours of travel time can be accrued daily.
### Settings
In this scenario, we define "Regular time over work day length earning threshold – Travel time" as 10.5 hours. The individual must also have overtime and balance tracking enabled. The value of the setting is in another words the hours of a standard workday plus the hours to be compensated.
### ![](https://support.nepton.com/hc/article_attachments/38534963288989)
### Interpretation
Travel time is recorded with overtime target hour to hour to balance. The duration of the travel time is 12 hours, but since the maximum daily compensation is 10.5 hours, only 3 hours are accrued to the balance in addition to regular working hours:
![](https://support.nepton.com/hc/article_attachments/38534963291677)
## Compensating travel time in other accruals 
Travel time can also be targeted to any other accrual in use, or as hour to hour to salary In the employee's calendar, travel time targeted to salary appears as regular time. The interpretation shows a total of 10.5 hours of travel time compensation.
### Interpretation
![](https://support.nepton.com/hc/article_attachments/38534985195677)
