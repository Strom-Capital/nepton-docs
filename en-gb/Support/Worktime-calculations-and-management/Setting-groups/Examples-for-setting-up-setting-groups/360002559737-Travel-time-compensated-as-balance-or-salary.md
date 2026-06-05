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
updated_at: '2024-08-23T10:40:39Z'
edited_at: '2023-02-24T14:05:08Z'
---

# Travel time compensated as balance or salary

There is an event type called Travel time in Nepton. Travel time event type do not accumulate balance or overtime as default, even if user has these accruals set to use.   
  
Exceptions for this compensation can be set in Worktime Working community settings or Setting group settings. In Working community settings this can be found from Worktime -> Administration -> Working community settings -> Work hours -> Length of work day -> Regular time over work day length earning threshold. In Setting group settings this can be found from Worktime -> Administration -> Setting groups: Wanted setting group -> Action: Setting group settings -> Work hours -> Length of work day -> Regular time over work day length earning threshold. 
## Example of Travel time compensated as balance
If over regular time recorded travel time is wanted to be compensated as balance, so that day is compensated max 10 hours and person's regular time is 8 hours a day. 
![mceclip1.png](https://support.nepton.com/hc/article_attachments/9517889469213)
### Settings
In this example Regular time over work day length earning threshold - Travel time - is set as 10 hours. Hours set here include length of work day hours plus hours wanted to be compensated. [Event overtime targeting](<https://support.nepton.com/hc/en-gb/articles/360002481617>) needs to be set active. 
In this example, default overtime target is hour to hour - Balance. According to the settings Travel time has accumulated 2 hours of balance.
### Interpretation
Below is a interpretation of situation, where is 14 hours of recorded travel time which is compensated until 10 hours. 
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4417837933201/mceclip1.png)
## Compensating travel time other than as balance 
Event overtime target can be other than balance if they are set to use, such as hour to hour - Salary. In person's calendar salary targeted travel time is shown in regular time (10:00) which in this example is two hours more than the set work day length. In the interpretation travel time is compensated total 10 hours. 
### Interpretation
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4417844602129/mceclip2.png)
Please note that with this configuration work cannot be targeted as overtime or increment overtime to balance. With this configuration can be dealt only with salary base part hours.
