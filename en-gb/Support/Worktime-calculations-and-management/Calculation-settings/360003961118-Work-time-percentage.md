---
id: 360003961118
title: Work time percentage
url: https://support.nepton.com/hc/en-gb/articles/360003961118-Work-time-percentage
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- työaikaprosentti
- osa-aikaisuus
- work time percentage
- part time
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2024-07-15T13:31:43Z'
---

# Work time percentage

If a person has a reduced daily working time, for example 60% of normal, a work time percentage can be set for them. More detailed description about part-time options can be found in [this](<https://support.nepton.com/hc/en-gb/articles/360002559018-Configure-setting-group-for-part-timers>) article.
If the normal daily working time was 7 hours 30 minutes and the weekly working time 37 hours 30 minutes, 60% of the working time would be
  * 4 hours 30 minutes daily
  * 22 hours and 30 minutes weekly


The work time percentage can be set via **Employees > Persons >** search the person you were looking for and open the person's information from the magnifying glass icon and go to the **Employment information** section.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4413353060241)
NOTE! The working time percentage is entered without a percentage sign. An empty field and 100% are both interpreted as full-time (100%). The work time percentage field works with the[ validity function](<https://support.nepton.com/hc/en-gb/articles/360004856937>).
The work time percentage does not affect:
  * daily and weekly maximum TES time
  * daily work time interpreted from a shift
  * if the daily or weekly work time comes from a daily exception entry
  * leveling period hours, unless it is [configured that work time percentage considers work time percentage](<https://support.nepton.com/hc/en-gb/articles/14849123960989>)


## Work time changing in the middle of work week
When employee's work percentage changes during the workweek, the system does not know which percentage to use for calculating the length of work week. In such cases, the balance accrual at the end of the week might be too positive or negative. To address this, manually adjust the balance for the next day using the balance reset or balance change methods, please see instructions [here](<https://support.nepton.com/hc/en-gb/articles/360002481797-Setting-and-changing-the-value-of-balance>).
Alternatively, you can set an exception to the length of workweek in the person’s work calendar. To do this, add up the required hours for different work obligations to determine the total weekly work obligation. For example:
Monday to Wednesday (when person is under 60% obligation): 3 x 6 hours = 18 hours
Thursday to Friday (when person is under 100% obligation): 2 x 7.5 hours = 15 hours
The total work obligation for the week is 33 hours. To set an exception to the length of work week, follow instructions below:
Click on the date icon (1)
Select ‘**Length of work week’** (2)
Set the exception for the work week length. (3)
Save the changes by clicking **‘Save exception.’** (4) You may remove the exception from this same window by clicking **Remove exception**.
These exceptions apply only to the work week you are currently doing modifications to. 
![](https://support.nepton.com/hc/article_attachments/20197025091229)
